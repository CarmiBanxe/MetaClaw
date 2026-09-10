/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `CASE_NOT_FOUND` и `CASE_SUBJECT_UNREADABLE` (`libraries/banksy-hitl/src/queue.ts`) —
 * оба не назывались ни одной пробой дерева. Второй сторожит ЧТЕНИЕ ДОНОРСКОЙ ФОРМЫ: запись без
 * `subject` и без `amountMinor` — «форма дела не определена».
 *
 * Третья проба нужна затем, чтобы отличить отказ от НЕЧИТАЕМОСТИ: старая запись, у которой сумма
 * ЕСТЬ, читается и форма выводится (`{kind:"money", amountMinor:150000n, currency:"GBP"}`).
 * Мера, отвергающая обе, была бы не строже, а слепее.
 *
 * КАНАРЕЙКА: `legacy.amountMinor` → `legacy.amountMinor ?? "0"` — недостающая сумма подменяется
 * нулём. `Tests: 1 failed, 2 passed`, ответ `НЕ БРОСИЛ`; третья проба остаётся зелёной.
 *
 * ЧЕМ ЭТО ГРОЗИТ БЕЗ СТРАЖА, и это стоит назвать прямо: дело с НЕЧИТАЕМЫМ предметом стало бы
 * делом НА НОЛЬ ФУНТОВ. Ноль проходит любой порог — и порог расширенной проверки, и порог
 * эскалации к MLRO. Подмена умолчанием здесь не теряет запись, она делает её безобидной на вид.
 *
 * Библиотека вне карантина переноса.
 */
import { ReviewQueue, type StoredCase } from "./queue";
import { VolatileRecords, VolatileLog } from "@bank-tree/banksy-durable";
import { SandboxHolders } from "./holders";
import type { OrgRole } from "./roles";

const HOLDERS = new SandboxHolders(new Map([
  ["MLRO", "sim://sandbox/MLRO"], ["CEO", "sim://sandbox/CEO"], ["CFO", "sim://sandbox/CFO"],
  ["CRO", "sim://sandbox/CRO"], ["CTO", "sim://sandbox/CTO"], ["COO", "sim://sandbox/COO"],
  ["COMPLIANCE_OFFICER", "sim://sandbox/CO"], ["OPERATOR", "sim://sandbox/OP"],
  ["INTERNAL_AUDITOR", "sim://sandbox/IA"],
] as [OrgRole, string][]));

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? String(e); }
};
const очередь = () => {
  const rows = new VolatileRecords<StoredCase>();
  return { q: new ReviewQueue(rows, new VolatileLog(), HOLDERS), rows };
};

describe("очередь надзора: дела нет и дело нечитаемо суть РАЗНЫЕ отказы", () => {
  it("CASE_NOT_FOUND — решение по делу, которого нет", () => {
    const { q } = очередь();
    expect(код(() => q.decide("нет-такого", "APPROVED" as never, "sim://sandbox/MLRO",
                              ["MLRO"] as never, new Date()))).toBe("CASE_NOT_FOUND");
  });

  it("CASE_SUBJECT_UNREADABLE — старая запись без предмета И без суммы", () => {
    const { q, rows } = очередь();
    // Запись донорской формы: ни `subject`, ни `amountMinor`. Форма дела не определена.
    const старая = { caseId: "case_legacy", status: "PENDING" } as unknown as StoredCase;
    rows.put("review_case", "case_legacy", старая);
    expect(код(() => q.get("case_legacy"))).toBe("CASE_SUBJECT_UNREADABLE");
  });

  it("старая запись С суммой читается: форма выводится, а не отвергается", () => {
    const { q, rows } = очередь();
    const с_суммой = { caseId: "case_old", status: "PENDING",
                       amountMinor: "150000", currency: "GBP" } as unknown as StoredCase;
    rows.put("review_case", "case_old", с_суммой);
    const c = q.get("case_old");
    expect(c?.subject).toEqual({ kind: "money", amountMinor: 150000n, currency: "GBP" });
  });
});
