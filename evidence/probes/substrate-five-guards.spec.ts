/**
 * ДОКАЗАННАЯ ПРОБА — прогон и ПЯТЬ канареек 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: пять отказов подложки дирижёра, ни один из которых не назывался пробой дерева:
 *   `CONFIDENCE_INFLATION`     — «сложение не создаёт уверенности, которой не было ни у части»
 *   `SAMPLE_COMPLETENESS_LIE`  — неполная выборка не объявляется полной
 *   `ORPHAN_CLAIM`             — «утверждение без происхождения не уезжает»
 *   `UNCORRELATED_RECORD`      — «событие, не привязанное к такту, бесполезно при разборе»
 *   `SHARE_EXCEEDED`           — доля канареечного прогона выше позволенной
 *
 * ШЕСТАЯ ПРОБА НАЙДЕНА ПРИ НАПИСАНИИ и оказалась сильнее остальных: часть БЕЗ происхождения
 * отбрасывается (`kept = parts.filter(p => Boolean(p.lineageId))`), и если происхождения нет ни у
 * одной, слабейшее звено равно НУЛЮ — всякое заявление выше нуля отвергается.
 * **Нет происхождения — нет уверенности.** Первая редакция пробы падала именно на этом: я подала
 * части без `lineageId` и ждала от них веса.
 *
 * ПЯТЬ КАНАРЕЕК, каждая ослепляет СВОЙ страж:
 *   сравнение с слабейшим звеном  →  2 failed, 4 passed  (обе уверенностные — верно)
 *   ложь о полноте разрешена      →  1 failed, 5 passed
 *   сирота пропускается           →  1 failed, 5 passed
 *   запись без такта пропускается →  1 failed, 5 passed
 *   доля не ограничена            →  1 failed, 5 passed
 *
 * КАЖДАЯ ПРОБА НЕСЁТ КОНТРОЛЬ — годный случай рядом с отказным. Без него «отвергает всегда» было
 * бы неотличимо от «отвергает верно»: неполная выборка БЕЗ заявления о полноте законна,
 * утверждение С входами проходит, запись С тактом проходит, доля РОВНО в пределе даёт `PASS`.
 *
 * Служба вне карантина переноса.
 */
import { compose } from "./composition";
import { Observability } from "./observability";
import { Lineage } from "./lineage";
import { Recorders } from "./recorders";
import { evaluate, MAX_SHARE } from "./canary";

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? "ОТКАЗ"; }
};

describe("подложка дирижёра: пять отказов, каждый о своём", () => {
  it("CONFIDENCE_INFLATION — сложение не создаёт уверенности, которой не было ни у части", () => {
    const части = [{ claim: "a", lineageId: "l-a", confidence: 0.9 },
                   { claim: "b", lineageId: "l-b", confidence: 0.4 }];
    expect(код(() => compose(части, 0.8))).toBe("CONFIDENCE_INFLATION");
    // КОНТРОЛЬ: заявление РОВНО по слабейшему звену проходит
    expect(compose(части, 0.4).weakestLink).toBe(0.4);
  });

  it("часть БЕЗ происхождения отбрасывается, и уверенность падает до нуля", () => {
    // Свойство сильнее, чем кажется: если происхождения нет НИ У ОДНОЙ части, слабейшее звено
    // равно НУЛЮ, и всякое заявление выше нуля отвергается. Нет происхождения — нет уверенности.
    const без = [{ claim: "a", confidence: 0.9 }, { claim: "b", confidence: 0.95 }];
    const c = compose(без);
    expect(c.composed).toEqual([]);
    expect(c.omitted).toEqual(["a", "b"]);
    expect(c.weakestLink).toBe(0);
    expect(код(() => compose(без, 0.01))).toBe("CONFIDENCE_INFLATION");
  });

  it("SAMPLE_COMPLETENESS_LIE — неполная выборка не объявляется полной", () => {
    const о = new Observability();
    expect(код(() => о.report({}, { observed: 7, expected: 10 }, true)))
      .toBe("SAMPLE_COMPLETENESS_LIE");
    // КОНТРОЛЬ: та же неполная выборка БЕЗ заявления о полноте — законна
    expect(код(() => о.report({}, { observed: 7, expected: 10 }, false))).toBe("НЕ БРОСИЛ");
  });

  it("ORPHAN_CLAIM — утверждение без входов не уезжает", () => {
    const l = new Lineage();
    expect(код(() => l.attach({ claim: "вывод", producedBy: "модель", inputs: [],
                                correlationId: "c1" }, "role-1"))).toBe("ORPHAN_CLAIM");
    expect(код(() => l.attach({ claim: "вывод", producedBy: "модель", inputs: ["док-1"],
                                correlationId: "c1" }, "role-1"))).toBe("НЕ БРОСИЛ");
  });

  it("UNCORRELATED_RECORD — событие без такта бесполезно при разборе", () => {
    const r = new Recorders();
    expect(код(() => r.record("нечто", "актор", ""))).toBe("UNCORRELATED_RECORD");
    expect(код(() => r.record("нечто", "актор", "c1"))).toBe("НЕ БРОСИЛ");
  });

  it("SHARE_EXCEEDED — доля канареечного прогона выше позволенной", () => {
    const прогон = { changeRef: "изм-1", share: MAX_SHARE + 0.01, observed: 100,
                     successes: 100, minObservations: 10 };
    expect(код(() => evaluate(прогон))).toBe("SHARE_EXCEEDED");
    expect(evaluate({ ...прогон, share: MAX_SHARE })).toBe("PASS");
  });
});
