/**
 * ДОКАЗАННАЯ ПРОБА — исчерпывающий прогон 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `TOOL_OUTSIDE_CONTEXT_SET` — «вызов инструмента, которого никогда не предлагали, пришёл
 * не из того разговора, что мы разрешили». Отказ не назван ни одной пробой дерева, и проба
 * `execution-authority.spec.ts` — покрывающая ДЕСЯТЬ других кодов — его не называет тоже.
 *
 * ЧТО ИЗМЕРЕНО: он НЕДОСТИЖИМ, и недостижим ПО ПОСТРОЕНИЮ.
 *
 *     toolsForContext(identity) = registered().map(lookup).filter(s => identity.effective.has(s.verb))
 *
 * То есть набор контекста ВЫВОДИТСЯ из того же множества глаголов, которым судит `assertMay`,
 * стоящий строкой выше. Инструмент, прошедший `assertMay`, обязан быть в наборе.
 *
 * Прогон по ВСЕМУ реестру × пять наборов глаголов даёт ровно два исхода:
 *
 *     VERB_OUTSIDE_EFFECTIVE_AUTHORITY | НЕ БРОСИЛ
 *
 * КАНАРЕЙКИ ЗДЕСЬ НЕТ, и это сказано вслух: ослеплять нечего — страж не срабатывает ни при каком
 * входе. Проба доказывает не работу меры, а её НЕДОСТИЖИМОСТЬ, и именно это её предмет.
 *
 * ЧЕМ ЭТО ОТЛИЧАЕТСЯ ОТ `PROPOSAL_FOR_ANOTHER_CUSTOMER`. Там второй рубеж достижим подсадкой
 * ПРОРЫВА первого: есть состояние, которое можно испортить. Здесь состояния нет — набор
 * вычисляется на месте из того же источника. Испортить нечего, и потому недостижимость здесь
 * структурная, а не практическая.
 *
 * ЧТО ЭТО НЕ ЗНАЧИТ: что страж лишний. Если `toolsForContext` однажды станет брать набор из
 * РАЗГОВОРА, а не из полномочия, — а именно так звучит его собственное объяснение, — страж станет
 * несущим в тот же час. Сегодня он ждёт этого часа.
 *
 * Служба вне карантина переноса.
 */
import { compose } from "./composite-identity";
import { authorizeAtExecution, toolsForContext } from "./execution-authority";
import { registered, lookup } from "./tool-registry";

const личность = (verbs: readonly string[]) => compose(
  { kind: "customer", ref: "cust-1", tenant: "t-1", grants: verbs as never },
  { ref: "banksy-client", grants: verbs as never },
);
const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? "ОТКАЗ"; }
};
const СЕЙЧАС = new Date("2026-09-10T00:00:00Z");

describe("TOOL_OUTSIDE_CONTEXT_SET: достижим ли страж, стоящий ЗА assertMay", () => {
  it("инструмент, чей глагол вне полномочия, ловится ПРЕДЫДУЩЕЙ проверкой", () => {
    const реестр = registered().map(lookup);
    const исполняющий = реестр.find((s) => s.verb === "execute");
    expect(исполняющий).toBeDefined();
    const бедная = личность(["explain"]);
    expect(код(() => authorizeAtExecution(
      { correlationId: "c1", tool: исполняющий!.tool, identity: бедная } as never, СЕЙЧАС)))
      .toBe("VERB_OUTSIDE_EFFECTIVE_AUTHORITY");
  });

  it("НАБОР КОНТЕКСТА выводится из полномочия, а не задаётся отдельно", () => {
    // Отсюда и недостижимость: `toolsForContext` фильтрует ТЕМ ЖЕ множеством глаголов, которым
    // судит `assertMay`. Пройдя вторую, инструмент обязан быть в наборе.
    const б = личность(["explain"]);
    const набор = toolsForContext(б).map((s) => s.tool);
    for (const s of registered().map(lookup)) {
      expect(набор.includes(s.tool)).toBe(s.verb === "explain");
    }
  });

  it("на всём реестре: НИ ОДИН инструмент не доходит до TOOL_OUTSIDE_CONTEXT_SET", () => {
    const все = registered().map(lookup);
    const исходы = new Set<string>();
    for (const s of все) {
      for (const набор of [["explain"], ["prepare"], ["submit"], ["execute"],
                           ["explain", "prepare", "submit", "execute"]]) {
        исходы.add(код(() => authorizeAtExecution(
          { correlationId: "c1", tool: s.tool, identity: личность(набор) } as never, СЕЙЧАС)));
      }
    }
    // eslint-disable-next-line no-console
    console.log("исходы по всему реестру →", [...исходы].sort().join(" | "));
    expect([...исходы]).not.toContain("TOOL_OUTSIDE_CONTEXT_SET");
  });
});
