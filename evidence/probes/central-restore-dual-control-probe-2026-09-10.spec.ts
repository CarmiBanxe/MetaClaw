/**
 * ПРОБА ЦЕНТРАЛЬНОГО ТЕРМИНАЛА — §5, обход маршрутов.
 * Предмет: правило проверяет ФОРМУ заявления, написанного тем, кого оно ограничивает.
 */
import { assertDualControl } from "./restore-dual-control";

describe("central §5: двойной контроль восстановления", () => {
  it("вызывающий пишет одобрения сам и проходит все четыре проверки", () => {
    // Ровно то, что приходит из тела запроса на /v0/director/restore.
    const самописные = [
      { by: "sim://sandbox/CEO", reason: "восстановление согласовано", at: "2026-09-10T00:00:00Z" },
      { by: "sim://sandbox/CFO", reason: "восстановление согласовано", at: "2026-09-10T00:00:00Z" },
    ];
    let итог = "ПРИНЯТО";
    try { assertDualControl(самописные, { sandbox: true }); }
    catch (e) { итог = (e as { code?: string }).code ?? "ОТКАЗ"; }
    console.log("§5 restore самописные одобрения →", итог);
    expect(итог).not.toBe("ПРИНЯТО");
  });

  it("КОНТРОЛЬ: правило умеет отказывать — одно одобрение", () => {
    let итог = "ПРИНЯТО";
    try { assertDualControl([{ by: "sim://sandbox/CEO", reason: "одиночно", at: "x" }],
                            { sandbox: true }); }
    catch (e) { итог = (e as { code?: string }).code ?? "ОТКАЗ"; }
    console.log("§5 КОНТРОЛЬ одно одобрение →", итог);
    expect(итог).toBe("RESTORE_WITHOUT_DUAL_CONTROL");
  });
});
