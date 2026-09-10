/**
 * ПОКАЗ ДЕФЕКТА — прогон 2026-09-11 на снимке `b87a9041`. Пункт `S1-04`.
 *
 * Эта проба ЗЕЛЕНА и показывает дефект: она закрепляет СЕГОДНЯШНЕЕ поведение, которое решением
 * оператора признано неверным.
 *
 *     S1-04 предложен card.freeze, вызван payment.send → ПРОШЛО
 *
 * `card.freeze` (класс `mutate`) и `payment.send` (класс `money`) несут ОДИН глагол `execute`.
 * Разговор предложил заморозку карты — исполняется перевод денег. Проверка глагола проходит
 * законно, а сказать «этого не предлагали» нечем: набор вычисляется на месте из полномочия.
 *
 * ПОСЛЕ ИСПОЛНЕНИЯ S1-04 эта проба обязана ПОКРАСНЕТЬ, и её место займёт ключевая проба
 * оператора, ждущая `TOOL_OUTSIDE_CONTEXT_SET`. Красный цвет здесь будет означать, что работа
 * сделана, — и поэтому файл назван показом дефекта, а не пробой защиты: чтобы никто не «починил»
 * его возвратом старого поведения.
 */
import { compose } from "./composite-identity";
import { authorizeAtExecution, toolNamesForContext } from "./execution-authority";

const личность = (verbs: readonly string[]) => compose(
  { kind: "customer", ref: "cust-1", tenant: "t-1", grants: verbs as never },
  { ref: "banksy-client", grants: verbs as never },
);
const код = (f: () => unknown): string => {
  try { f(); return "ПРОШЛО"; } catch (e) { return (e as { code?: string }).code ?? "ОТКАЗ"; }
};
const СЕЙЧАС = new Date("2026-09-11T00:00:00Z");

describe("S1-04 · КЛЮЧЕВАЯ ПРОБА ОПЕРАТОРА: предложен один инструмент, вызван другой", () => {
  it("два инструмента одного глагола: card.freeze и payment.send оба execute", () => {
    const имена = toolNamesForContext(личность(["execute"]));
    expect(имена).toContain("card.freeze");
    expect(имена).toContain("payment.send");
  });

  it("ПРЕДЛОЖЕН card.freeze — ВЫЗВАН payment.send: сегодня проходит", () => {
    // Разговор предложил заморозку карты. Вызывается перевод денег. Глагол тот же — execute.
    // Ограничения контекста НЕТ, и потому вызов проходит.
    const итог = код(() => authorizeAtExecution(
      { correlationId: "c1", tool: "payment.send", identity: личность(["execute"]) } as never,
      СЕЙЧАС));
    // eslint-disable-next-line no-console
    console.log("S1-04 предложен card.freeze, вызван payment.send →", итог);
    expect(итог).toBe("ПРОШЛО");   // ← ДЕФЕКТ. После S1-04 обязано стать TOOL_OUTSIDE_CONTEXT_SET
  });

  it("набор контекста НЕ хранит предложенного: он вычисляется из полномочия", () => {
    // Отсюда и невозможность отличить предложенное от лишь разрешённого.
    const один = toolNamesForContext(личность(["execute"]));
    const два = toolNamesForContext(личность(["execute"]));
    expect(один).toEqual(два);          // не зависит от разговора вовсе
    expect(один.length).toBeGreaterThan(1);
  });
});
