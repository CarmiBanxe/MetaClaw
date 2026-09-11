/**
 * ДОКАЗАННАЯ ПРОБА — прогон и ДВЕ канарейки 2026-09-11 на снимке `b87a9041`. Пункт `S1-10`.
 *
 * Предмет решения 9: «сбой записи не должен оставлять **неподтверждённое успешное решение**».
 *
 * ИЗМЕРЕНО: требование исполнено, и исполнено тремя разными ответами на три разных состояния.
 *
 *   исправный журнал      → 200  ok                          decided: true
 *   отказ записи НАМЕРЕНИЯ → 503 EVIDENCE_STORE_UNAVAILABLE  decided: false, дело PENDING
 *   отказ записи ИСХОДА    → 500 DECISION_WITHOUT_EVIDENCE   decided: true
 *
 * УСТРОЙСТВО: намерение пишется ДО решения, исход — ПОСЛЕ. Отказ первой записи означает, что
 * решения не было; отказ второй — что решение состоялось, а следа нет.
 *
 * ТРЕТИЙ СЛУЧАЙ И ЕСТЬ ПРЕДМЕТ. Дверь не притворяется ни в одну сторону: она НАЗЫВАЕТ оба факта
 * сразу — «решение принято» и «доказательства нет». Единственный честный ответ, когда произошло
 * и то, и другое.
 *
 * ── КАНАРЕЙКИ ──
 *   запись намерения убрана          →  2 failed, 1 passed
 *   отсутствие следа СКРЫТО (200 ok) →  1 failed, 2 passed  ← ровно третья проба
 *
 * Вторая канарейка и есть доказательство, что проба меряет НАЗВАННОСТЬ состояния, а не сам факт
 * отказа: скрыть отсутствие следа значит вернуть ту самую тихую зелёную строку.
 *
 * Журнал-подсадка отказывает на N-й записи. Отказ носителя — не выдумка: диск кончается.
 */
import type { AddressInfo } from "node:net";
import { VolatileLog, VolatileRecords } from "@bank-tree/banksy-durable";
import { ReviewQueue, SandboxHolders, type OrgRole, type StoredCase } from "@bank-tree/banksy-hitl";
import { assertMay } from "@bank-tree/banksy-mlro-boundary";
import { buildDirectorServer } from "./server";

const HOLDERS = new SandboxHolders(new Map([["MLRO", "sim://sandbox/MLRO"]] as [OrgRole, string][]));

/** Журнал, отказывающий на N-й записи. Отказ носителя — не выдумка: диск кончается. */
class ЛомкийЖурнал extends VolatileLog {
  private n = 0;
  constructor(private readonly ломается_на: number) { super(); }
  append(stream: string, entry: unknown): never | ReturnType<VolatileLog["append"]> {
    this.n += 1;
    if (this.n === this.ломается_на) throw new Error("носитель отказал");
    return super.append(stream, entry as never);
  }
}

async function дверь(журнал: VolatileLog) {
  const queue = new ReviewQueue(new VolatileRecords<StoredCase>(), new VolatileLog(), HOLDERS);
  queue.open({ caseId: "case_1", subjectRef: "tx_1", customerRef: "cust_1",
               subject: { kind: "money", amountMinor: 5_000_00n, currency: "GBP" },
               trigger: "SAR_REQUIRED", reasons: ["structuring"],
               openedAt: new Date().toISOString() });
  const built = buildDirectorServer({} as never, {
    reviewQueue: queue, holders: HOLDERS,
    subjects: { resolve: () => "sim://sandbox/MLRO" },
    mlroJournal: журнал,
    mlroBoundary: { assertMay: (a: string, act: string) => assertMay(a as never, act as never) },
  } as never);
  await new Promise<void>((ok) => built.server.listen(0, "127.0.0.1", ok));
  const port = (built.server.address() as AddressInfo).port;
  return {
    queue, close: () => new Promise<void>((ok) => built.server.close(() => ok())),
    async decide() {
      const r = await fetch(`http://127.0.0.1:${port}/v0/hitl/decisions`, {
        method: "POST", headers: { "content-type": "application/json" },
        // ОСНАСТКА ПЕРЕПИСАНА 2026-09-11, И ЭТО САМО ПО СЕБЕ ЗАМЕР.
        //
        // Прежняя подавала `{caseId, decidedBy, decision: "APPROVE", roles, reason}` — и этого
        // хватало. Сегодня дверь отвергает такое трижды подряд, и каждый отказ есть исполненное
        // требование:
        //
        //   409 DECISION_CONTEXT_MISMATCH   ← решение связано с ДЕЛОМ и КЛИЕНТОМ (решение 9)
        //   400 CONTRACT_VERSION_MISMATCH   ← контракт handoff ПОДКЛЮЧЁН к пути решений (S1-09)
        //   улики без провенанса          ← EVIDENCE_WITHOUT_PROVENANCE
        //
        // КРАСНЫЙ КОНТРОЛЬ ЗДЕСЬ ЕСТЬ ДОКАЗАТЕЛЬСТВО ЧУЖОЙ ПОЧИНКИ: щель S1-09 («контракт
        // handoff не подключён к пути решений») закрыта ровно тем, что дверь теперь требует
        // контракт и отвергает всё, что его не несёт.
        //
        // СЛОВАРИ: дверь берёт `decision` в словаре ОЧЕРЕДИ (`APPROVE`) и переводит его в
        // словарь контракта (`PROCEED`) отображением `СТАТУС_ГРАНИЦЫ`. То есть отображение
        // ЕСТЬ и оно явное — требование решения 4 исполнено. Остальные поля контракта дверь
        // строит САМА из дела, и потому здесь не подаются: подать их значило бы позволить
        // обратившемуся назначить себе полномочие.
        body: JSON.stringify({
          caseId: "case_1", customerReference: "cust_1",
          decidedBy: "sim://sandbox/MLRO", roles: ["MLRO"],
          reason: "основание названо словами",
          decision: "APPROVE",              // ← словарь ОЧЕРЕДИ; дверь сама переводит в PROCEED
          contractVersion: "dmi-1.0.0-draft",
          requestId: "tx_1",
          evidenceReferences: [{ evidenceId: "ev-1", provenance: "hitl.case.case_1",
                                 recordedAt: "2026-09-11T00:00:00Z" }],
        }),
      });
      return { status: r.status, body: (await r.json()) as Record<string, unknown> };
    },
  };
}

describe("S1-10 · решение и долговечный след", () => {
  it("КОНТРОЛЬ: исправный журнал — решение принято и записано", async () => {
    const d = await дверь(new VolatileLog());
    try {
      const r = await d.decide();
      // eslint-disable-next-line no-console
      console.log("S1-10 исправный →", r.status, r.body["code"] ?? "ok", "decided:", r.body["decided"]);
      expect(r.status).toBe(200);
      expect(d.queue.get("case_1")?.status).not.toBe("PENDING");
    } finally { await d.close(); }
  });

  it("отказ записи НАМЕРЕНИЯ — решение НЕ принимается", async () => {
    const d = await дверь(new ЛомкийЖурнал(1));
    try {
      const r = await d.decide();
      // eslint-disable-next-line no-console
      console.log("S1-10 отказ намерения →", r.status, r.body["code"], "decided:", r.body["decided"]);
      expect(r.body["decided"]).toBe(false);
      expect(d.queue.get("case_1")?.status).toBe("PENDING");   // состояние не изменено
    } finally { await d.close(); }
  });

  it("отказ записи ИСХОДА — решение принято, и это СКАЗАНО, а не скрыто", async () => {
    const d = await дверь(new ЛомкийЖурнал(2));
    try {
      const r = await d.decide();
      // eslint-disable-next-line no-console
      console.log("S1-10 отказ исхода →", r.status, r.body["code"], "decided:", r.body["decided"]);
      expect(r.body["code"]).toBe("DECISION_WITHOUT_EVIDENCE");
      expect(r.body["decided"]).toBe(true);      // молчаливого успеха нет
      expect(r.status).toBeGreaterThanOrEqual(500);
    } finally { await d.close(); }
  });
});
