/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: четыре условия `openReviewedRun` (`libraries/banksy-plan/src/executor.ts`). Три из
 * четырёх отказов — `REVIEW_FOR_ANOTHER_PLAN`, `PLAN_NOT_ACCEPTED`, `AUTHORITY_NOT_HELD_AT_OPEN`
 * — не назывались ни одной пробой дерева.
 *
 * Носитель сам объясняет, почему третье и четвёртое условия ДУБЛИРУЮТ находки проверки: «бюджет
 * подаётся здесь отдельным числом и мог быть уменьшен, а конверт полномочий мог быть отозван —
 * оба между проверкой и запуском». Пробы построены ровно на этих двух зазорах во времени.
 *
 * ШЕСТАЯ ПРОБА — не отказ, а УСТРОЙСТВО: полномочие спрашивается на КАЖДЫЙ шаг, и это доказано
 * записью вызовов (`["a.read", "a.write"]`), а не чтением цикла.
 *
 * КАНАРЕЙКА: `plan.steps` → `plan.steps.slice(0, 1)` — полномочие спрашивается только у первого
 * шага. `Tests: 2 failed, 4 passed`: покраснели ровно две полномочные пробы.
 *
 * И ГЛАВНОЕ О НЕЙ: проба «годный случай открывается» под канарейкой осталась **ЗЕЛЁНОЙ**. То есть
 * дефект «проверяем только первый шаг» невидим для всякой пробы, которая смотрит лишь на успех.
 * Именно это и делает шестую пробу необходимой, а не избыточной.
 *
 * Библиотека вне карантина переноса.
 */
import { openReviewedRun } from "./executor";

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? String(e); }
};
const шаг = (id: string, to: string) => ({ id, to }) as never;
const план = { planId: "P-1", stepsRequired: 2, steps: [шаг("s1", "a.read"), шаг("s2", "a.write")] } as never;
const вердикт = { planId: "P-1", findings: [] } as never;
const опции = { runId: "R-1", startedAt: "2026-09-10T00:00:00.000Z",
                dueBy: "2026-09-10T01:00:00.000Z", stepBudget: 2 };
const бегун = { open: (x: unknown) => ({ opened: true, ...(x as object) }) } as never;
const всё_можно = { permits: () => true };

describe("открытие хода по проверенному плану: четыре условия, каждое поимённо", () => {
  it("годный случай открывается", () => {
    expect(код(() => openReviewedRun(бегун, план, вердикт, опции, всё_можно))).toBe("НЕ БРОСИЛ");
  });

  it("REVIEW_FOR_ANOTHER_PLAN — вердикт выдан другому плану", () => {
    expect(код(() => openReviewedRun(бегун, план, { ...(вердикт as object), planId: "P-2" } as never,
                                     опции, всё_можно))).toBe("REVIEW_FOR_ANOTHER_PLAN");
  });

  it("PLAN_NOT_ACCEPTED — вердикт с находкой", () => {
    const плохой = { planId: "P-1", findings: [{ code: "X1" }] } as never;
    expect(код(() => openReviewedRun(бегун, план, плохой, опции, всё_можно))).toBe("PLAN_NOT_ACCEPTED");
  });

  it("STEP_BUDGET_INSUFFICIENT — бюджет уменьшили ПОСЛЕ проверки", () => {
    expect(код(() => openReviewedRun(бегун, план, вердикт, { ...опции, stepBudget: 1 }, всё_можно)))
      .toBe("STEP_BUDGET_INSUFFICIENT");
  });

  it("AUTHORITY_NOT_HELD_AT_OPEN — конверт отозван между проверкой и запуском", () => {
    const только_чтение = { permits: (s: { to: string }) => s.to.endsWith(".read") };
    expect(код(() => openReviewedRun(бегун, план, вердикт, опции, только_чтение as never)))
      .toBe("AUTHORITY_NOT_HELD_AT_OPEN");
  });

  it("полномочие спрашивается на КАЖДЫЙ шаг, а не на первый", () => {
    const спрошено: string[] = [];
    const учёт = { permits: (s: { to: string }) => { спрошено.push(s.to); return true; } };
    openReviewedRun(бегун, план, вердикт, опции, учёт as never);
    expect(спрошено).toEqual(["a.read", "a.write"]);
  });
});
