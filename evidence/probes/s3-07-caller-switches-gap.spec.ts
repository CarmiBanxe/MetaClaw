/**
 * ПОКАЗ ДЕФЕКТА — прогон 2026-09-11 на снимке `b87a9041`. Пункт `S3-07`.
 *
 * Решение оператора 2: «**Обязательность review и oversight должна задаваться серверной
 * политикой, а не переключателями вызывающего.**»
 *
 * ИЗМЕРЕНО: сегодня — переключателями вызывающего. `requiresModel`, `requiresReview`,
 * `requiresOversight` суть ПОЛЯ ЗАПРОСА (`local-enforcement.ts:65-71`), и каждая проверка
 * начинается с `if (r.requiresX)`.
 *
 *     S3-07 все три выключены → {"enforced":true}
 *
 * Вызывающий, выставивший три поля в `false`, получает исполнение с НУЛЁМ квитанций — включая
 * денежное действие `payment.send`. Доктрина четырёх квитанций исполняется ровно тогда, когда
 * вызывающий сам об этом попросит.
 *
 * ВТОРАЯ ПРОБА — КОНТРОЛЬ ЧЕСТНОСТИ: при `requiresReview: true` без квитанции ревью отказ
 * НАСТОЯЩИЙ (`REVIEW_RECEIPT_ABSENT`). Мера работает; она лишь спрашивает разрешения работать.
 *
 * ЧЕГО ЭТА ПРОБА НЕ УТВЕРЖДАЕТ. Что дефект ЖИВОЙ: `LocalEnforcement` не собран ни в одном
 * производственном процессе (14 построений, все в пробах). Это ЗАПАДНЯ, а не течь.
 *
 * И ровно поэтому она важна СЕЙЧАС: решение оператора 2 велит собрать композицию
 * (`S3-02`…`S3-05`). Собранная с этими переключателями, западня становится течью в тот же час.
 *
 * ПОСЛЕ ИСПОЛНЕНИЯ `S3-07` третья и четвёртая пробы обязаны ПОКРАСНЕТЬ, а первые две — остаться
 * зелёными.
 */
import { LocalEnforcement } from "./local-enforcement";

const брокер = { issuedHere: (id: string) => id.startsWith("model-") };
const ревью = { identityOf: (id: string) =>
  id.startsWith("rev-") ? { reviewerId: "r1", reviewerModel: "иная-модель" } : null };
const надзор = { permittedAction: (id: string) => id.startsWith("ovr-") ? "payment.send" : "" };

const основа = {
  actionKey: "k1", functionId: "FN-1", action: "payment.send", authorityRef: "env-1",
  allowedActions: ["payment.send"], prohibitedActions: [],
  dataClasses: ["PSEUDONYMISED"], permittedDataClasses: ["PSEUDONYMISED"],
  authorIdentity: { agentId: "a1", model: "модель-автора" },
  evidenceRefs: ["ev-1"],
};
const сделать = () => new LocalEnforcement(брокер as never, надзор as never,
                                           () => "2026-09-11T00:00:00Z", ревью as never);

describe("S3-07 · обязательность проверок задаётся ВЫЗЫВАЮЩИМ", () => {
  it("полный комплект проходит — контроль", () => {
    const e = сделать();
    const o = e.enforce({ ...основа, requiresModel: true, requiresReview: true,
                          requiresOversight: true, modelReceiptId: "model-1",
                          reviewReceiptId: "rev-1", oversightReceiptId: "ovr-1" } as never);
    expect(o.enforced).toBe(true);
  });

  it("БЕЗ квитанции ревью при requiresReview=true — отказ", () => {
    const o = сделать().enforce({ ...основа, requiresModel: false, requiresReview: true,
                                  requiresOversight: false } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("REVIEW_RECEIPT_ABSENT");
  });

  it("ДЕФЕКТ: вызывающий ставит requiresReview=false и ревью не требуется вовсе", () => {
    const o = сделать().enforce({ ...основа, requiresModel: false, requiresReview: false,
                                  requiresOversight: false } as never);
    // eslint-disable-next-line no-console
    console.log("S3-07 все три выключены →", JSON.stringify({ enforced: o.enforced, refusal: o.refusal }));
    expect(o.enforced).toBe(true);   // ← исполнение БЕЗ единой квитанции
  });

  it("ДЕФЕКТ ТЯЖЕЛЕЕ: переключатели выключены у ДЕНЕЖНОГО действия", () => {
    const o = сделать().enforce({ ...основа, action: "payment.send",
                                  allowedActions: ["payment.send"],
                                  requiresModel: false, requiresReview: false,
                                  requiresOversight: false } as never);
    expect(o.enforced).toBe(true);
  });
});
