/**
 * ПРОБА ЗАЩИТЫ — прежде была ПОКАЗОМ ДЕФЕКТА. Пункт `S3-08`, решение оператора 2.
 *
 * ── ЧЕМ БЫЛА ──────────────────────────────────────────────────────────────────────────────
 *
 * До 2026-09-11 повтор возвращал прежний исход **по одному лишь `actionKey`**, не сверяя
 * содержимое запроса. Под чужим ключом проходило и денежное действие без квитанций, и
 * запрещённое `aml.override`. Отдельная проба утверждала худшее:
 *
 *     «объявленный отказ ALREADY_ENFORCED_DIFFERENTLY НЕ ПРОИЗВОДИТСЯ НИ ОДНОЙ СТРОКОЙ»
 *
 * **Имя отказа было выбрано, а проверка — не написана.** Решение оператора 2 требовало прямо:
 * «Повторный запрос не должен обходить проверку через чужой ранее использованный ключ.»
 *
 * ── ЧТО СТЕРЕЖЁТ ТЕПЕРЬ ───────────────────────────────────────────────────────────────────
 *
 * Что повтор сверяет **каноническую форму запроса**, а не ссылку и не один ключ: тот же запрос
 * даёт тот же исход и работы не повторяет; **иной запрос под тем же ключом — отказ**.
 *
 * ── ЧТО СДЕЛАЕТ ЭТУ ПРОБУ КРАСНОЙ ─────────────────────────────────────────────────────────
 *
 * Возврат к выдаче прежнего исхода по ключу без сверки содержимого. Красный цвет здесь будет
 * доказательством отката починки.
 *
 * ЧЕГО НЕ УТВЕРЖДАЕТ. Что `LocalEnforcement` собран в производственном процессе — это свойство
 * композиции и меряется отдельно.
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

const полный = {
  actionKey: "ОДИН-И-ТОТ-ЖЕ", functionId: "FN-1", action: "payment.send", subject: "acc-1",
  correlationId: "cor-1", authorityRef: "env-1",
  allowedActions: ["payment.send"], prohibitedActions: [],
  dataClasses: ["PSEUDONYMISED"], permittedDataClasses: ["PSEUDONYMISED"],
  authorIdentity: { agentId: "a1", model: "модель-автора" },
  evidenceRefs: ["ev-1"],
  modelReceiptId: "model-1", reviewReceiptId: "rev-1", oversightReceiptId: "ovr-1",
};
const сделать = () => new LocalEnforcement(брокер as never, надзор as never,
                                           () => "2026-09-11T00:00:00Z", ревью as never);

describe("S3-08 · повтор привязан к СОДЕРЖИМОМУ, а не к ключу", () => {
  it("КОНТРОЛЬ: тот же запрос дважды — исход тот же", () => {
    const e = сделать();
    const первый = e.enforce({ ...полный } as never);
    const второй = e.enforce({ ...полный } as never);
    expect(первый.enforced).toBe(true);
    expect(второй.enforced).toBe(первый.enforced);
  });

  it("КОНТРОЛЬ: порядок полей значения не имеет — сверка по КАНОНИЧЕСКОЙ форме", () => {
    const e = сделать();
    e.enforce({ ...полный } as never);
    const переставленный = {
      evidenceRefs: полный.evidenceRefs, authorIdentity: полный.authorIdentity,
      oversightReceiptId: полный.oversightReceiptId, reviewReceiptId: полный.reviewReceiptId,
      modelReceiptId: полный.modelReceiptId, permittedDataClasses: полный.permittedDataClasses,
      dataClasses: полный.dataClasses, prohibitedActions: полный.prohibitedActions,
      allowedActions: полный.allowedActions, authorityRef: полный.authorityRef,
      correlationId: полный.correlationId, subject: полный.subject, action: полный.action,
      functionId: полный.functionId, actionKey: полный.actionKey,
    };
    expect(e.enforce(переставленный as never).enforced).toBe(true);
  });

  it("ЗАЩИТА: тот же ключ, ДРУГОЕ действие — прежний успех НЕ возвращается", () => {
    const e = сделать();
    expect(e.enforce({ ...полный } as never).enforced).toBe(true);
    const иное = e.enforce({ ...полный, action: "aml.override",
                             allowedActions: ["aml.override"] } as never);
    expect(иное.enforced).toBe(false);
  });

  it("ЗАЩИТА: объявленный отказ ALREADY_ENFORCED_DIFFERENTLY ПРОИЗВОДИТСЯ", () => {
    const e = сделать();
    e.enforce({ ...полный } as never);
    const иное = e.enforce({ ...полный, subject: "acc-ДРУГОЙ" } as never);
    expect(иное.enforced).toBe(false);
    expect(иное.refusal).toBe("ALREADY_ENFORCED_DIFFERENTLY");
  });

  it("ЗАЩИТА: под чужим ключом не проходит ЗАПРЕЩЁННОЕ действие", () => {
    const e = сделать();
    e.enforce({ ...полный } as never);
    const запрещённое = e.enforce({ ...полный, action: "aml.override",
                                    allowedActions: ["payment.send"],
                                    prohibitedActions: ["aml.override"] } as never);
    expect(запрещённое.enforced).toBe(false);
  });
});
