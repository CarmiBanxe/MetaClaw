/**
 * ПРОБА ЗАЩИТЫ — прежде была ПОКАЗОМ ДЕФЕКТА. Пункт `S3-07`, решение оператора 2.
 *
 * ── ЧЕМ ЭТА ПРОБА БЫЛА И ПОЧЕМУ ПЕРЕИМЕНОВАНА ─────────────────────────────────────────────
 *
 * До 2026-09-11 файл звался `…-caller-switches-gap` и утверждал, что дефект ЕСТЬ:
 * `requiresModel/Review/Oversight` были ПОЛЯМИ ЗАПРОСА, и вызывающий, выставив три поля в
 * `false`, получал исполнение с НУЛЁМ квитанций — включая денежное `payment.send`.
 *
 * Проба назвала своё покраснение ЗАРАНЕЕ: «после исполнения S3-07 третья и четвёртая пробы
 * ОБЯЗАНЫ ПОКРАСНЕТЬ, а первые две — остаться зелёными».
 *
 * **Предсказание сбылось наполовину, и вторая половина поучительнее первой.** Дефектные
 * покраснели как обещано. Но покраснели и КОНТРОЛЬНЫЕ — потому что исполнение пошло ДАЛЬШЕ
 * ожидания автора:
 *
 *   1. политика стала fail-closed: функция, о которой политика молчит, требует ВСЕХ квитанций,
 *      и `REVIEW_RECEIPT_ABSENT` сменился на `MODEL_RECEIPT_ABSENT` — модель спрашивается раньше;
 *   2. порт брокера сменил контракт: `issuedHere(id) → boolean` стал `bindingOf(id) → ReceiptBinding`,
 *      потому что вопрос «выдана ли здесь» слабее вопроса «выдана ли ПОД ЭТО действие и этот
 *      субъект» (R7). Старая подделка брокера перестала быть подделкой этого порта.
 *
 * **Имя файла со словом «gap» стало устаревшей прозой, и потому файл переименован, а не оставлен
 * под прежним именем с новым содержанием.** История сохранена `git mv`.
 *
 * ── ЧТО ЭТА ПРОБА СТЕРЕЖЁТ ТЕПЕРЬ ─────────────────────────────────────────────────────────
 *
 * Что обязательность квитанций задаётся СЕРВЕРНОЙ ПОЛИТИКОЙ, а не полями запроса: вызывающий
 * вправе УЖЕСТОЧИТЬ и не вправе ослабить.
 *
 * ── ЧТО СДЕЛАЕТ ЭТУ ПРОБУ КРАСНОЙ ──────────────────────────────────────────────────────────
 *
 * Возврат обязательности в поля запроса: если `callerDemands` снова начнёт ОСЛАБЛЯТЬ требование
 * (а не только ужесточать), пробы «ослабить нельзя» станут красными. Красный цвет здесь будет
 * доказательством отката починки.
 *
 * ЧЕГО ЭТА ПРОБА НЕ УТВЕРЖДАЕТ. Что `LocalEnforcement` собран в производственном процессе.
 * Это свойство композиции, и оно меряется отдельно.
 */
import { LocalEnforcement } from "./local-enforcement";

const СВЯЗЬ = { action: "payment.send", subject: "acc-1", correlationId: "cor-1" };

const брокер = { bindingOf: (id: string) => (id.startsWith("model-") ? СВЯЗЬ : null) };
const надзор = { decisionOf: (id: string) => (id.startsWith("ovr-") ? СВЯЗЬ : null) };
const ревью = {
  bindingOf: (id: string) =>
    id.startsWith("rev-")
      ? { reviewerId: "r1", reviewerModel: "иная-модель", reviewed: СВЯЗЬ,
          emulated: false, independent: true }
      : null,
};

const основа = {
  actionKey: "k1", functionId: "FN-1", action: "payment.send", subject: "acc-1",
  correlationId: "cor-1", authorityRef: "env-1",
  allowedActions: ["payment.send"], prohibitedActions: [],
  dataClasses: ["PSEUDONYMISED"], permittedDataClasses: ["PSEUDONYMISED"],
  authorIdentity: { agentId: "a1", model: "модель-автора" },
  evidenceRefs: ["ev-1"],
};
const сделать = () => new LocalEnforcement(брокер as never, надзор as never,
                                           () => "2026-09-11T00:00:00Z", ревью as never);

describe("S3-07 · обязательность задаётся СЕРВЕРНОЙ ПОЛИТИКОЙ", () => {
  it("КОНТРОЛЬ: полный комплект связанных квитанций проходит", () => {
    const o = сделать().enforce({ ...основа, modelReceiptId: "model-1",
                                  reviewReceiptId: "rev-1",
                                  oversightReceiptId: "ovr-1" } as never);
    expect(o.enforced).toBe(true);
  });

  it("ЗАЩИТА: вызывающий требует МЕНЬШЕ — требование не ослабевает", () => {
    const o = сделать().enforce({
      ...основа,
      callerDemands: { requiresModel: false, requiresReview: false, requiresOversight: false },
    } as never);
    expect(o.enforced).toBe(false);
  });

  it("ЗАЩИТА ТЯЖЕЛЕЕ: то же у ДЕНЕЖНОГО действия — исполнения нет", () => {
    const o = сделать().enforce({
      ...основа, action: "payment.send", allowedActions: ["payment.send"],
      callerDemands: { requiresModel: false, requiresReview: false, requiresOversight: false },
    } as never);
    expect(o.enforced).toBe(false);
  });

  it("ПОРЯДОК ОТКАЗА НАЗВАН: без единой квитанции первым отвечает модель", () => {
    const o = сделать().enforce({ ...основа } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("MODEL_RECEIPT_ABSENT");
  });

  it("ЗАЩИТА: квитанция модели под ЧУЖОЙ субъект — отказ ОТЛИЧЕН от «отсутствует»", () => {
    const чужой = { bindingOf: () => ({ ...СВЯЗЬ, subject: "acc-ДРУГОЙ" }) };
    const e = new LocalEnforcement(чужой as never, надзор as never,
                                   () => "2026-09-11T00:00:00Z", ревью as never);
    const o = e.enforce({ ...основа, modelReceiptId: "model-1",
                          reviewReceiptId: "rev-1", oversightReceiptId: "ovr-1" } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("MODEL_RECEIPT_FOR_OTHER_SUBJECT");
    expect(o.refusal).not.toBe("MODEL_RECEIPT_ABSENT");
  });

  it("ЗАЩИТА: ЭМУЛИРОВАННОЕ ревью не есть независимое заключение", () => {
    const эмул = {
      bindingOf: () => ({ reviewerId: "r1", reviewerModel: "иная-модель", reviewed: СВЯЗЬ,
                          emulated: true, independent: true }),
    };
    const e = new LocalEnforcement(брокер as never, надзор as never,
                                   () => "2026-09-11T00:00:00Z", эмул as never);
    const o = e.enforce({ ...основа, modelReceiptId: "model-1",
                          reviewReceiptId: "rev-1", oversightReceiptId: "ovr-1" } as never);
    expect(o.enforced).toBe(false);
    expect(o.refusal).toBe("REVIEW_RECEIPT_EMULATED");
  });
});
