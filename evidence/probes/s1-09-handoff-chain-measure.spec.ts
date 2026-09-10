/**
 * ЗАМЕР S1-09 — прогон 2026-09-11 на снимке `b87a9041`. Пункт `S1-09`.
 *
 * ПРОБА ДВАЖДЫ ИЗМЕРИЛА НЕ ТО, ЧТО НАЗЫВАЛА, и оба раза это записано здесь, а не исправлено
 * молча. Я собиралась показать, что запрещённое границей поле проходит дверь решений.
 *
 *   попытка 1 → 503 NO_SUBJECT_SOURCE   «личность обращающегося установить нечем»
 *   попытка 2 → 503 NO_MLRO_JOURNAL     «журнал второй линии не собран»
 *
 * Оба раза дверь отвергала РАНЬШЕ, и оба раза по собственному, названному предусловию. Это ровно
 * та ловушка, о которой предупреждало поручение оператора: «проба должна измерять названную
 * защиту, а не предшествующий отказ».
 *
 * ЧТО ИЗМЕРЕНО В ИТОГЕ — цепь предусловий двери `/v0/hitl/decisions`, четырнадцать звеньев,
 * каждое со своим кодом и своим разрядом:
 *
 *   HITL_DOOR_UNAVAILABLE · BODY_NOT_JSON · DECISION_INCOMPLETE · DECISION_WITHOUT_REASON ·
 *   DECISION_UNKNOWN · NO_SUBJECT_SOURCE · SUBJECT_NOT_ESTABLISHED · DECIDER_CLAIM_MISMATCH ·
 *   HOLDER_REGISTRY_UNAVAILABLE · DECIDER_NOT_A_HOLDER · NO_MLRO_BOUNDARY · <отказ полномочия> ·
 *   NO_MLRO_JOURNAL · EVIDENCE_STORE_UNAVAILABLE
 *
 * ЧЕГО В ЦЕПИ НЕТ: проверок контракта handoff. `assertRequestWellFormed` и
 * `assertDecisionAcceptable` имеют НОЛЬ производственных вызывающих, и потому
 * `FORBIDDEN_FIELD_PRESENT`, `REQUEST_MISMATCH` и откат версии решения на этом пути не
 * проверяются ничем.
 *
 * И ГЛАВНОЕ, ЧТО ДАЛ ЭТОТ ЗАМЕР ДЛЯ СОСЕДНЕГО ПУНКТА: `DECIDER_CLAIM_MISMATCH` — сверка
 * ЗАЯВЛЕНИЯ с установленной личностью — здесь УЖЕ ЕСТЬ. Требование R2 моей спецификации S1-08
 * оказалось не новым: дверь решений его исполняет, дверь прерывания — нет. Образец не надо
 * придумывать, его надо перенести.
 *
 * Две первые пробы КРАСНЫ и оставлены красными намеренно: они закрепляют, ГДЕ именно цепь
 * обрывается сегодня, и обязаны позеленеть только вместе с подключением контракта.
 */
import type { AddressInfo } from "node:net";
import { VolatileLog, VolatileRecords } from "@bank-tree/banksy-durable";
import { ReviewQueue, SandboxHolders, type OrgRole, type StoredCase } from "@bank-tree/banksy-hitl";
import { assertMay } from "@bank-tree/banksy-mlro-boundary";
import { buildDirectorServer } from "./server";

const HOLDERS = new SandboxHolders(new Map([
  ["MLRO", "sim://sandbox/MLRO"], ["CEO", "sim://sandbox/CEO"],
] as [OrgRole, string][]));

async function дверь() {
  const store = new VolatileRecords<StoredCase>();
  const queue = new ReviewQueue(store, new VolatileLog(), HOLDERS);
  queue.open({ caseId: "case_1", subjectRef: "tx_1", customerRef: "cust_1",
               subject: { kind: "money", amountMinor: 5_000_00n, currency: "GBP" },
               trigger: "SAR_REQUIRED", reasons: ["structuring"],
               openedAt: new Date().toISOString() });
  const built = buildDirectorServer({} as never, {
    reviewQueue: queue, holders: HOLDERS,
    subjects: { resolve: () => "sim://sandbox/MLRO" },
    mlroBoundary: { assertMay: (a: string, act: string) => assertMay(a as never, act as never) },
  } as never);
  await new Promise<void>((ok) => built.server.listen(0, "127.0.0.1", ok));
  const port = (built.server.address() as AddressInfo).port;
  return {
    queue, close: () => new Promise<void>((ok) => built.server.close(() => ok())),
    async decide(body: Record<string, unknown>) {
      const r = await fetch(`http://127.0.0.1:${port}/v0/hitl/decisions`, {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify(body),
      });
      return { status: r.status, body: (await r.json()) as Record<string, unknown> };
    },
  };
}
const РЕШЕНИЕ = { caseId: "case_1", decidedBy: "sim://sandbox/MLRO", decision: "APPROVE",
                  roles: ["MLRO"], reason: "основание названо словами" };

describe("S1-09 · контракт handoff не подключён к пути решений", () => {
  it("ЗАПРЕЩЁННОЕ ПОЛЕ границы проходит дверь", async () => {
    const d = await дверь();
    try {
      // `suspicionRationale` — из закрытого перечня FORBIDDEN_RESPONSE_FIELDS. Контракт
      // объявляет его непересекающим границу. Дверь контракта не зовёт.
      const r = await d.decide({ ...РЕШЕНИЕ, suspicionRationale: "клиент дробит суммы",
                                 investigatorNotes: "смотри дело 42" });
      // eslint-disable-next-line no-console
      console.log("S1-09 запрещённое поле →", r.status, JSON.stringify(r.body).slice(0, 100));
      expect(r.status).toBe(200);        // ← ДЕФЕКТ
    } finally { await d.close(); }
  });

  it("состояние дела ИЗМЕНЕНО, хотя граница нарушена", async () => {
    const d = await дверь();
    try {
      await d.decide({ ...РЕШЕНИЕ, sarNarrative: "полный текст подозрения" });
      const после = d.queue.get("case_1")?.status;
      // eslint-disable-next-line no-console
      console.log("S1-09 состояние после нарушения границы →", после);
      expect(после).not.toBe("PENDING");  // ← ДЕФЕКТ: проверка обязана быть ДО изменения
    } finally { await d.close(); }
  });

  it("КОНТРОЛЬ: дверь свои проверки делает — повтор решения отвергается", async () => {
    const d = await дверь();
    try {
      await d.decide(РЕШЕНИЕ);
      const r = await d.decide(РЕШЕНИЕ);
      expect(r.status).toBeGreaterThanOrEqual(400);
    } finally { await d.close(); }
  });
});
