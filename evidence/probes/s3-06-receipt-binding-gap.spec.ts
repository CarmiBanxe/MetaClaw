/**
 * ПОКАЗ ДЕФЕКТА — прогон 2026-09-11 на снимке `b87a9041`. Пункт `S3-06`.
 *
 * Решение оператора 2: «Исполнение разрешается только после получения всех обязательных
 * действительных квитанций, **связанных с тем же действием, субъектом и контекстом**.»
 *
 * ИЗМЕРЕНО: связана с действием ТОЛЬКО квитанция надзора.
 *
 *   квитанция модели   broker.issuedHere(id)        — выдана ли ЗДЕСЬ вообще · с действием НЕ связана
 *   квитанция ревью    review.identityOf(id)        — КТО проверял, и не автор ли · с действием НЕ связана
 *   квитанция надзора  permittedAction(id) !== action — связана
 *
 *     S3-06 чужие квитанции → {"enforced":true}
 *
 * Квитанция модели, выданная под разбор отчёта, и ревью того же отчёта проводят ПЕРЕВОД ДЕНЕГ.
 *
 * ДВА КОНТРОЛЯ доказывают, что проверки работают в том, что проверяют: выдуманная квитанция даёт
 * `MODEL_RECEIPT_NOT_ISSUED_BY_BROKER`, ревьюер-автор — `REVIEWER_IS_AUTHOR`. Меры не сломаны;
 * они отвечают на вопрос «откуда это» и не задают вопроса «о чём это».
 *
 * ОБРАЗЕЦ ПОЧИНКИ СТОИТ В ТОЙ ЖЕ ФУНКЦИИ, ДЕСЯТЬЮ СТРОКАМИ НИЖЕ: надзор сверяется с `r.action`.
 * Правило написано, применено к одной квитанции из трёх — третий случай этого рода за сутки.
 *
 * ЧЕГО ПРОБА НЕ УТВЕРЖДАЕТ: что дефект живой. Композиции нет. Это ЗАПАДНЯ, и она третья:
 * `S3-07` (переключатели вызывающего) · `S3-08` (чужой ключ повтора) · `S3-06` (чужие квитанции).
 * Все три чинятся ДО сборки, иначе сборка вносит их разом.
 */
import { LocalEnforcement } from "./local-enforcement";

// Брокер выдал квитанцию модели для РАЗБОРА ОТЧЁТА. Он помнит, что выдал её, — и только.
const брокер = { issuedHere: (id: string) => id === "model-для-отчёта" };
// Ревьюер проверял ОТЧЁТ. Порт отдаёт его личность — и только.
const ревью = { identityOf: (id: string) =>
  id === "rev-для-отчёта" ? { reviewerId: "r1", reviewerModel: "иная-модель" } : null };
// Надзор знает, ЧТО именно разрешил.
const надзор = { permittedAction: (id: string) =>
  id === "ovr-для-платежа" ? "payment.send" : "report.explain" };
const сделать = () => new LocalEnforcement(брокер as never, надзор as never,
                                           () => "2026-09-11T00:00:00Z", ревью as never);

const запрос = (over: Record<string, unknown>) => ({
  actionKey: `k-${Math.random()}`, functionId: "FN-1", authorityRef: "env-1",
  dataClasses: ["PSEUDONYMISED"], permittedDataClasses: ["PSEUDONYMISED"],
  authorIdentity: { agentId: "a1", model: "модель-автора" }, evidenceRefs: ["ev-1"],
  requiresModel: true, requiresReview: true, requiresOversight: true,
  ...over,
});

describe("S3-06 · связаны ли квитанции с ТЕМ ЖЕ действием", () => {
  it("квитанция НАДЗОРА связана: чужая даёт MLRO_DECISION_NOT_PERMITTING", () => {
    const o = сделать().enforce(запрос({
      action: "payment.send", allowedActions: ["payment.send"], prohibitedActions: [],
      modelReceiptId: "model-для-отчёта", reviewReceiptId: "rev-для-отчёта",
      oversightReceiptId: "ovr-для-отчёта",
    }) as never);
    expect(o.refusal).toBe("MLRO_DECISION_NOT_PERMITTING");
  });

  it("ДЕФЕКТ: квитанции МОДЕЛИ и РЕВЬЮ от ЧУЖОГО действия проходят", () => {
    // Модель звали ради разбора отчёта. Ревьюер смотрел отчёт. Исполняется ПЕРЕВОД ДЕНЕГ.
    const o = сделать().enforce(запрос({
      action: "payment.send", allowedActions: ["payment.send"], prohibitedActions: [],
      modelReceiptId: "model-для-отчёта",   // ← выдана под ДРУГОЕ действие
      reviewReceiptId: "rev-для-отчёта",    // ← ревью ДРУГОГО действия
      oversightReceiptId: "ovr-для-платежа",
    }) as never);
    // eslint-disable-next-line no-console
    console.log("S3-06 чужие квитанции →", JSON.stringify({ enforced: o.enforced, refusal: o.refusal }));
    expect(o.enforced).toBe(true);   // ← ДЕФЕКТ
  });

  it("КОНТРОЛЬ: происхождение квитанций проверяется настояще", () => {
    const o = сделать().enforce(запрос({
      action: "payment.send", allowedActions: ["payment.send"], prohibitedActions: [],
      modelReceiptId: "выдумана", reviewReceiptId: "rev-для-отчёта",
      oversightReceiptId: "ovr-для-платежа",
    }) as never);
    expect(o.refusal).toBe("MODEL_RECEIPT_NOT_ISSUED_BY_BROKER");
  });

  it("КОНТРОЛЬ: ревьюер-автор отвергается", () => {
    const свой = { identityOf: () => ({ reviewerId: "a1", reviewerModel: "модель-автора" }) };
    const e = new LocalEnforcement(брокер as never, надзор as never,
                                   () => "2026-09-11T00:00:00Z", свой as never);
    const o = e.enforce(запрос({
      action: "payment.send", allowedActions: ["payment.send"], prohibitedActions: [],
      modelReceiptId: "model-для-отчёта", reviewReceiptId: "любая",
      oversightReceiptId: "ovr-для-платежа",
    }) as never);
    expect(o.refusal).toBe("REVIEWER_IS_AUTHOR");
  });
});
