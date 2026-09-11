/**
 * ПРОБА ЦЕНТРАЛЬНОГО ТЕРМИНАЛА — X-03, 2026-09-11, снимок b87a9041.
 *
 * ПРЕДМЕТ. `postJournalEntry(description, postings, highValueApproved = false)` — третий довод
 * есть ПОЛЕ ВЫЗЫВАЮЩЕГО. Удержание записи высокой величины (I-04/I-27) обходится подстановкой
 * `true`, и ничто не связывает это `true` с записью одобрения, которую `approveHighValue`
 * требует от НАЗВАННОГО человека (`gl-service.ts:397` — «requires a named human approver (I-27)»).
 *
 * ЧТО ИЗМЕРЯЕТСЯ. Не «параметр существует» — это видно чтением. Измеряется ПОСЛЕДСТВИЕ: проходит
 * ли запись выше порога и появляется ли строка одобрения в хранилище.
 *
 * КАНАРЕЙКА — вторая проба: та же запись при `false` УДЕРЖИВАЕТСЯ. Без неё зелёный первой был бы
 * неотличим от «удержание не работает вовсе».
 */
import { GLService, InMemoryGLAuditPort, isHighValueProposal } from "./gl-service";
import { InMemoryLedger } from "./inmemory-ledger";
import {
  Account, AccountType, HIGH_VALUE_THRESHOLD_MINOR, PostingDirection,
} from "./ledger.models";
import { InMemoryApprovalStore } from "./approval.models";

const СВЕРХ = HIGH_VALUE_THRESHOLD_MINOR + 100n;

interface Опора {
  gl: GLService;
  approvals: InMemoryApprovalStore;
  debit: Account;
  credit: Account;
}

async function опора(): Promise<Опора> {
  const approvals = new InMemoryApprovalStore();
  const gl = new GLService(new InMemoryLedger(), new InMemoryGLAuditPort(), approvals);
  const debit = await gl.createAccount("Customer Funds", AccountType.ASSET, "GBP");
  const credit = await gl.createAccount("Settlement Pending", AccountType.LIABILITY, "GBP");
  return { gl, approvals, debit, credit };
}

function ноги(o: Опора, amountMinor: bigint) {
  return [
    { accountId: o.debit.accountId, direction: PostingDirection.DEBIT, amountMinor, currency: "GBP" },
    { accountId: o.credit.accountId, direction: PostingDirection.CREDIT, amountMinor, currency: "GBP" },
  ];
}

describe("X-03: highValueApproved есть поле вызывающего", () => {
  it("подставленное true проводит запись выше порога БЕЗ одобрения", async () => {
    const o = await опора();
    const r = await o.gl.postJournalEntry("перевод", ноги(o, СВЕРХ), true);
    const удержано = isHighValueProposal(r);
    console.log("X-03 подставлено true →", JSON.stringify({
      удержано, сумма: String(СВЕРХ), порог: String(HIGH_VALUE_THRESHOLD_MINOR),
      вид: удержано ? "HighValueHITLProposal" : "ЗАПИСЬ ПРОВЕДЕНА",
    }));
    expect(удержано).toBe(false);
  });

  it("КАНАРЕЙКА: та же запись при false УДЕРЖИВАЕТСЯ — мера работает", async () => {
    const o = await опора();
    const r = await o.gl.postJournalEntry("перевод", ноги(o, СВЕРХ), false);
    expect(isHighValueProposal(r)).toBe(true);
  });

  it("КОНТРОЛЬ: безымянный одобряющий отвергается — I-27 держится", async () => {
    const o = await опора();
    const r = await o.gl.postJournalEntry("перевод", ноги(o, СВЕРХ), false);
    if (!isHighValueProposal(r)) throw new Error("канарейка уже сказала бы об этом");
    await expect(o.gl.approveHighValue(r.entryId, "")).rejects.toThrow(/named human/);
  });
});

