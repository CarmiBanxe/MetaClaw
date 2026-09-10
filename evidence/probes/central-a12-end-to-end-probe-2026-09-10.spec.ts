/**
 * ПРОБА ЦЕНТРАЛЬНОГО ТЕРМИНАЛА — A12 сквозь ВЕСЬ ПУТЬ, с замером СОСТОЯНИЯ ДЕЛА.
 *
 * Оператор: «Он присылает точное имя зарегистрированного двойника и roles=["MLRO"] — подмена
 * также отвергается» и «Знание строки sim://… не должно позволять другому вызывающему
 * действовать от имени двойника».
 *
 * Проверяется НЕ код ответа: сравнивается состояние дела ДО и ПОСЛЕ.
 */
import type { AddressInfo } from "node:net";
import { VolatileLog, VolatileRecords } from "@bank-tree/banksy-durable";
import { ReviewQueue, SandboxHolders, assertHolders,
         type OrgRole, type StoredCase } from "@bank-tree/banksy-hitl";
import { assertMay } from "@bank-tree/banksy-mlro-boundary";
import { buildDirectorServer } from "./server";

const HOLDERS = new SandboxHolders(new Map([
  ["MLRO", "sim://sandbox/MLRO"], ["CEO", "sim://sandbox/CEO"],
] as [OrgRole, string][]));

describe("central A12: посторонний, знающий строку двойника", () => {
  it("проходит ВЕСЬ путь и меняет решение по делу", async () => {
    const store = new VolatileRecords<StoredCase>();
    const queue = new ReviewQueue(store, new VolatileLog(), HOLDERS);
    queue.open({ caseId: "case_1", subjectRef: "tx_1", customerRef: "cust_1",
                 subject: { kind: "money", amountMinor: 5_000_00n, currency: "GBP" },
                 trigger: "SAR_REQUIRED", reasons: ["structuring"],
                 openedAt: new Date().toISOString() });
    const до = queue.get("case_1")?.status;

    const built = buildDirectorServer({} as never, {
      reviewQueue: queue, holders: HOLDERS,
      mlroBoundary: { assertMay: (a: string, act: string) => assertMay(a as never, act as never) },
    } as never);
    await new Promise<void>((ok) => built.server.listen(0, "127.0.0.1", ok));
    const port = (built.server.address() as AddressInfo).port;
    let r: { status: number; body: Record<string, unknown> };
    try {
      const resp = await fetch(`http://127.0.0.1:${port}/v0/hitl/decisions`, {
        method: "POST", headers: { "content-type": "application/json" },
        // ПОСТОРОННИЙ. Никакого удостоверения — только знание строки из реестра.
        body: JSON.stringify({ caseId: "case_1", decidedBy: "sim://sandbox/MLRO",
                               decision: "APPROVE", roles: ["MLRO"],
                               reason: "основание названо словами" }),
      });
      r = { status: resp.status, body: (await resp.json()) as Record<string, unknown> };
    } finally { await new Promise<void>((ok) => { built.server.close(() => ok()); }); }

    const после = queue.get("case_1")?.status;
    console.log("A12 сквозной →", JSON.stringify({ http: r.status, до, после,
                                                   решил: queue.get("case_1")?.decidedBy }));
    expect({ до, после }).toEqual({ до: "PENDING", после: "PENDING" });
  });

  it("R12 нижний слой: assertHolders не сравнивает держателя с decidedBy в песочнице", () => {
    const got = assertHolders(HOLDERS, "кто-угодно-и-даже-не-ссылка", ["MLRO"], "sandbox");
    console.log("R12 нижний слой →", JSON.stringify(got));
    expect(() => assertHolders(HOLDERS, "кто-угодно-и-даже-не-ссылка", ["MLRO"], "sandbox"))
      .toThrow();
  });
});
