/**
 * ПРОБА ЗАЩИТЫ — прежде была ПОКАЗОМ ДЕФЕКТА. Пункт `S3-06`, решение оператора 2.
 *
 * ── ЧЕМ БЫЛА ──────────────────────────────────────────────────────────────────────────────
 *
 * До 2026-09-11 порт модели отвечал «выдана ли ЗДЕСЬ» (`issuedHere → boolean`), а порт ревью —
 * «кто проверял», и только. **Ни один не отвечал, ПОД ЧТО квитанция выдана.** Денежное действие
 * проходило с квитанциями, выданными под разбор отчёта.
 *
 * Образец правильного был рядом и в тот же день: квитанция НАДЗОРА уже несла `permittedAction`.
 * **Один из трёх портов делал верно, и это показывало, что верное возможно.**
 *
 * ── ЧТО СТЕРЕЖЁТ ТЕПЕРЬ ───────────────────────────────────────────────────────────────────
 *
 * Что все три квитанции связаны с ДЕЙСТВИЕМ, СУБЪЕКТОМ и КОНТЕКСТОМ, и что «выдана не под это»
 * есть отказ, ОТЛИЧНЫЙ от «не выдана»: это разные предметы и разные починки.
 *
 * Плюс два свойства независимости, которых прежняя редакция не знала вовсе:
 *   - личность ревьюера берётся У ВЫДАВШЕГО и сверяется с автором **и по агенту, и по модели**;
 *   - независимость — **по СЕМЕЙСТВУ модели**, и её знает доверенная сторона. Разные строки
 *     идентификаторов независимостью не являются (решение 2 дословно).
 *
 * ── ЧТО СДЕЛАЕТ ЭТУ ПРОБУ КРАСНОЙ ─────────────────────────────────────────────────────────
 *
 * Возврат портов к вопросу «выдана ли здесь» либо снятие сверки связи. Красный цвет здесь будет
 * доказательством отката починки.
 */
import { LocalEnforcement } from "./local-enforcement";

const СВЯЗЬ = { action: "payment.send", subject: "acc-1", correlationId: "cor-1" };
const ЧУЖАЯ = { action: "report.review", subject: "rep-9", correlationId: "cor-9" };

const годный = (b = СВЯЗЬ) => ({
  брокер: { bindingOf: (id: string) => (id.startsWith("model-") ? b : null) },
  надзор: { decisionOf: (id: string) => (id.startsWith("ovr-") ? b : null) },
  ревью: {
    bindingOf: (id: string) =>
      id.startsWith("rev-")
        ? { reviewerId: "r1", reviewerModel: "иная-модель", reviewed: b,
            emulated: false, independent: true }
        : null,
  },
});

const основа = {
  actionKey: "k1", functionId: "FN-1", action: "payment.send", subject: "acc-1",
  correlationId: "cor-1", authorityRef: "env-1",
  allowedActions: ["payment.send"], prohibitedActions: [],
  dataClasses: ["PSEUDONYMISED"], permittedDataClasses: ["PSEUDONYMISED"],
  authorIdentity: { agentId: "a1", model: "модель-автора" },
  evidenceRefs: ["ev-1"],
  modelReceiptId: "model-1", reviewReceiptId: "rev-1", oversightReceiptId: "ovr-1",
};

const собрать = (п: ReturnType<typeof годный>) =>
  new LocalEnforcement(п.брокер as never, п.надзор as never,
                       () => "2026-09-11T00:00:00Z", п.ревью as never);

describe("S3-06 · квитанции связаны с действием, субъектом и контекстом", () => {
  it("КОНТРОЛЬ: все три связаны с ТЕМ ЖЕ — исполнение", () => {
    expect(собрать(годный()).enforce({ ...основа } as never).enforced).toBe(true);
  });

  it("ЗАЩИТА: квитанция МОДЕЛИ от чужого действия — свой отказ, не «отсутствует»", () => {
    const п = годный();
    п.брокер = { bindingOf: () => ЧУЖАЯ };
    const o = собрать(п).enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("MODEL_RECEIPT_FOR_OTHER_SUBJECT");
    expect(o.refusal).not.toBe("MODEL_RECEIPT_ABSENT");
  });

  it("ЗАЩИТА: квитанция РЕВЬЮ от чужого действия — свой отказ", () => {
    const п = годный();
    п.ревью = { bindingOf: () => ({ reviewerId: "r1", reviewerModel: "иная-модель",
                                    reviewed: ЧУЖАЯ, emulated: false, independent: true }) };
    const o = собрать(п).enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("REVIEW_RECEIPT_FOR_OTHER_SUBJECT");
  });

  it("ЗАЩИТА: квитанция НАДЗОРА от чужого действия — отказ", () => {
    const п = годный();
    п.надзор = { decisionOf: () => ЧУЖАЯ };
    const o = собрать(п).enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
  });

  it("ЗАЩИТА: происхождение — квитанция, здесь НЕ выдававшаяся, отвергается", () => {
    const п = годный();
    п.брокер = { bindingOf: () => null };
    const o = собрать(п).enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("MODEL_RECEIPT_NOT_ISSUED_BY_BROKER");
  });

  it("ЗАЩИТА: ревьюер-автор отвергается — совпадение по МОДЕЛИ, не только по агенту", () => {
    const п = годный();
    п.ревью = { bindingOf: () => ({ reviewerId: "иной-агент",
                                    reviewerModel: "модель-автора",   // ← та же модель
                                    reviewed: СВЯЗЬ, emulated: false, independent: true }) };
    const o = собрать(п).enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("REVIEWER_IS_AUTHOR");
  });

  it("ЗАЩИТА: независимость — по СЕМЕЙСТВУ, и её ставит доверенная сторона", () => {
    const п = годный();
    п.ревью = { bindingOf: () => ({ reviewerId: "r1", reviewerModel: "иная-строка-того-же-семейства",
                                    reviewed: СВЯЗЬ, emulated: false,
                                    independent: false }) };   // ← доверенная сторона сказала: нет
    const o = собрать(п).enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("REVIEWER_NOT_INDEPENDENT");
  });
});
