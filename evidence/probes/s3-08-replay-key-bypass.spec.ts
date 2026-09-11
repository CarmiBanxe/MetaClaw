/**
 * ПОКАЗ ДЕФЕКТА — прогон 2026-09-11 на снимке `b87a9041`. Пункт `S3-08`.
 *
 * Решение оператора 2: «**Повторный запрос не должен обходить проверку через чужой ранее
 * использованный ключ.**»
 *
 * ИЗМЕРЕНО: обходит. Ветвь повтора возвращает прежний исход, НЕ СРАВНИВАЯ запроса:
 *
 *     const prior = this.done.get(r.actionKey);
 *     if (prior) return prior;
 *
 *     S3-08 чужой ключ → {"enforced":true}
 *
 * Взяв `actionKey` безобидного действия, полностью снабжённого четырьмя квитанциями, вызывающий
 * проводит:
 *   · ДЕНЕЖНОЕ действие `payment.send` — **без единой квитанции**;
 *   · ЗАПРЕЩЁННОЕ `aml.override` — одно из пяти имён перечня `NEVER`.
 *
 * Кэш идемпотентности обходит ВСЕ проверки разом: полномочие, перечень разрешённого, перечень
 * запрещённого, класс данных и все четыре квитанции. Он стоит ПЕРВЫМ и не спрашивает ничего.
 *
 * ИМЯ ДЛЯ ЭТОГО ОТКАЗА УЖЕ ВЫБРАНО И НЕ УПОТРЕБЛЕНО. `ALREADY_ENFORCED_DIFFERENTLY` объявлен в
 * перечне типов (`local-enforcement.ts:38`) и **не выбрасывается ни одной строкой**. Мера
 * названа, задумана и не написана — тот самый род, что я считаю вторые сутки.
 *
 * КОНТРОЛЬ ЧЕСТНОСТИ: тот же запрос дважды даёт тот же исход и работы не повторяет.
 * Идемпотентность как таковая исправна; неисправно то, что ключ не привязан к содержимому.
 *
 * ЧЕГО ПРОБА НЕ УТВЕРЖДАЕТ: что дефект живой. `LocalEnforcement` не собран ни в одном
 * производственном процессе. Это ЗАПАДНЯ — и она опаснее западни `S3-07`, потому что не требует
 * от вызывающего даже выключить переключатель: довольно знать чужой ключ.
 *
 * ПОСЛЕ ИСПОЛНЕНИЯ вторая и третья пробы обязаны ПОКРАСНЕТЬ с кодом
 * `ALREADY_ENFORCED_DIFFERENTLY`, первая — остаться зелёной.
 */
import { LocalEnforcement } from "./local-enforcement";

const брокер = { issuedHere: (id: string) => id.startsWith("model-") };
const ревью = { identityOf: (id: string) =>
  id.startsWith("rev-") ? { reviewerId: "r1", reviewerModel: "иная-модель" } : null };
const надзор = { permittedAction: (id: string) => id.startsWith("ovr-") ? "report.explain" : "" };
const сделать = () => new LocalEnforcement(брокер as never, надзор as never,
                                           () => "2026-09-11T00:00:00Z", ревью as never);

const безобидное = {
  actionKey: "КЛЮЧ-1", functionId: "FN-1", action: "report.explain", authorityRef: "env-1",
  allowedActions: ["report.explain"], prohibitedActions: [],
  dataClasses: ["PSEUDONYMISED"], permittedDataClasses: ["PSEUDONYMISED"],
  authorIdentity: { agentId: "a1", model: "модель-автора" }, evidenceRefs: ["ev-1"],
  requiresModel: true, requiresReview: true, requiresOversight: true,
  modelReceiptId: "model-1", reviewReceiptId: "rev-1", oversightReceiptId: "ovr-1",
};

describe("S3-08 · повтор с тем же ключом", () => {
  it("КОНТРОЛЬ: тот же запрос дважды — исход тот же, работа не повторяется", () => {
    const e = сделать();
    const a = e.enforce(безобидное as never);
    const b = e.enforce(безобидное as never);
    expect(a.enforced).toBe(true);
    expect(b).toEqual(a);
  });

  it("ДЕФЕКТ: тот же ключ, ДРУГОЕ действие — возвращается прежний успех", () => {
    const e = сделать();
    e.enforce(безобидное as never);
    // Тот же actionKey. Действие иное — ДЕНЕЖНОЕ. Ни одной квитанции под него не выдавалось.
    const денежное = { ...безобидное, action: "payment.send",
                       allowedActions: ["payment.send"],
                       modelReceiptId: undefined, reviewReceiptId: undefined,
                       oversightReceiptId: undefined };
    const o = e.enforce(денежное as never);
    // eslint-disable-next-line no-console
    console.log("S3-08 чужой ключ →", JSON.stringify({ enforced: o.enforced, refusal: o.refusal }));
    expect(o.enforced).toBe(true);      // ← ДЕФЕКТ: запрос не сравнивается с прежним
  });

  it("ДЕФЕКТ: тот же ключ, ЗАПРЕЩЁННОЕ действие — тоже проходит", () => {
    const e = сделать();
    e.enforce(безобидное as never);
    const запрещённое = { ...безобидное, action: "aml.override",
                          allowedActions: [], prohibitedActions: ["aml.override"] };
    expect(e.enforce(запрещённое as never).enforced).toBe(true);
  });

  it("объявленный отказ ALREADY_ENFORCED_DIFFERENTLY НЕ ПРОИЗВОДИТСЯ НИ ОДНОЙ СТРОКОЙ", () => {
    // РЕДАКЦИЯ 2, 2026-09-11. Прежнее тело говорило `expect(true).toBe(true)` — заголовок
    // ЗАЯВЛЯЛ, тело не доказывало ничего. Зелёная проба, измеряющая ноль: ровно тот разряд,
    // который эта линия находит у чужих мер. Найдена сплошным обходом собственных проб.
    //
    // Утверждение проверяемо: имя обязано встречаться РОВНО ОДИН раз — в перечне типов, —
    // и ни одна строка не вправе его ПРОИЗВОДИТЬ (ни `throw`, ни `refusal:`, ни `return`).
    // РЕДАКЦИЯ 3, 2026-09-11. `require.resolve` по имени пакета разрешался в ЖИВОЕ ДЕРЕВО
    // (`/home/mmber/wt/bt-sepa01/...`), а не в снимок, потому что `node_modules` снимка есть
    // ссылка на дерево. Проба молча мерила не тот предмет, и КАНАРЕЙКА это вскрыла: подсадка
    // производящей строки в снимок не краснила пробу. Путь берётся от САМОГО ФАЙЛА ПРОБЫ.
    const путь = require("node:path").join(__dirname, "local-enforcement.ts");
    const строки = require("node:fs").readFileSync(путь, "utf8").split("\n") as string[];
    const где = строки
      .map((s: string, i: number) => [i + 1, s] as [number, string])
      .filter(([, s]: [number, string]) => s.includes("ALREADY_ENFORCED_DIFFERENTLY"));
    const производящие = где.filter(([, s]: [number, string]) =>
      /throw|refusal\s*:|return\s/.test(s));
    console.log("S3-08 объявленный отказ →", JSON.stringify({
      упоминаний: где.length, строки: где.map(([n]: [number, string]) => n), производящих: производящие.length,
    }));
    expect(где.length).toBe(1);          // только объявление
    expect(производящие.length).toBe(0); // ни одна строка его не производит
  });
});
