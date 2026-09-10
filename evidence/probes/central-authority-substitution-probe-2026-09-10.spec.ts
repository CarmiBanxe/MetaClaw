/** ПРОБА ЦЕНТРАЛЬНОГО ТЕРМИНАЛА — независимая, в изолированном снимке. РЕДАКЦИЯ 2. */
import { NamedIssuers, VolatileRevocations, verifyEnvelope } from "./authority-envelope";
import { admit } from "../action-admission";
import { SandboxHolders, assertHolders, type OrgRole } from "@bank-tree/banksy-hitl";

const ISSUER = "оператор";
const issuers = () => { const i = new NamedIssuers([ISSUER]); i.issue("env-1", ISSUER); return i; };

describe("central: недоверенное заявление как основание полномочий", () => {
  it("A3: предъявитель меняет allowed у ВЫДАННОГО конверта", () => {
    const подделка = { allowed: ["write:/etc/shadow"], grantedBy: ISSUER, envelopeId: "env-1",
                       scope: { workId: "работа-1" }, issuedAt: "2026-09-10T00:00:00Z" };
    const v = verifyEnvelope(подделка, { workId: "работа-1" }, issuers(), new VolatileRevocations());
    const a = admit({ subject: "write:/etc/shadow", allowed: подделка.allowed, envelopeId: "env-1" });
    console.log("A3 allowed →", JSON.stringify({ verify: v.ok, admit: a.permitted }));
    expect({ v: v.ok, a: a.permitted }).toEqual({ v: false, a: false });
  });

  it("A2: предъявитель СТИРАЕТ prohibited пустым массивом (образец содержателен)", () => {
    // Договор запрещает исход в сеть; предъявитель прислал prohibited: [].
    const из_конверта: readonly string[] = [];
    const действующий = из_конверта ?? ["network:egress"];   // ровно строка engineering-intake
    const a = admit({ subject: "network:egress", allowed: ["write:src/", "network:egress"],
                      prohibited: [...действующий], envelopeId: "env-1" });
    console.log("A2 prohibited=[] →", JSON.stringify(a), "| действующий запрет:", JSON.stringify(действующий));
    expect(a.permitted).toBe(false);
  });

  it("КОНТРОЛЬ: тот же вызов с настоящим запретом обязан отказать", () => {
    const a = admit({ subject: "network:egress", allowed: ["write:src/", "network:egress"],
                      prohibited: ["network:egress"], envelopeId: "env-1" });
    console.log("КОНТРОЛЬ →", JSON.stringify(a));
    expect(a.permitted).toBe(false);
  });

  it("Держатель: посторонний проходит как MLRO в песочнице", () => {
    const reg = new SandboxHolders(new Map([["MLRO", "sim://sandbox/MLRO"]] as [OrgRole, string][]));
    const got = assertHolders(reg, "посторонний-вызывающий", ["MLRO"], "sandbox");
    console.log("ДЕРЖАТЕЛЬ →", JSON.stringify(got));
    expect(() => assertHolders(reg, "посторонний-вызывающий", ["MLRO"], "sandbox")).toThrow();
  });
});
