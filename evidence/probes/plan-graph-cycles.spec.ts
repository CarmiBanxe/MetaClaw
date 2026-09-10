/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `CYCLIC_PLAN` и `UNKNOWN_DEPENDENCY` (`conductor/src/orchestrator/graph-sandbox.ts`) —
 * оба не назывались ни одной пробой дерева. Довод носителя: «обнаруженный цикл — отказ, а не
 * „разрулим на исполнении“».
 *
 * КАК ЭТА ПРОБА НАШЛА СВОЙ СОБСТВЕННЫЙ ДЕФЕКТ. Первая редакция ставила `counterpartyCheck: true`
 * и «годный план» упал с `ORDER_VIOLATION`: при проверке контрагента санкционный скрининг обязан
 * быть ПЕРВЫМ шагом (I-01). Ошибка была моя, а не предмета — и предмет её поймал. Заодно нашёлся
 * третий страж, и он добавлен шестой пробой, с обеими сторонами: не первый — отказ, первый —
 * проходит.
 *
 * КАНАРЕЙКА: `ordered.length !== names.length` → `ordered.length !== ordered.length`. Цикл
 * перестаёт обнаруживаться. `Tests: 3 failed, 3 passed` — покраснели ровно три цикловые; «годный
 * план», `UNKNOWN_DEPENDENCY` и `ORDER_VIOLATION` остались зелёными. Различает.
 *
 * ПОЧЕМУ ТРИ РАЗНЫХ ЦИКЛА, А НЕ ОДИН: пара, тройка и цикл В ЧАСТИ плана при ацикличном остатке.
 * Обход, ловящий только пару, прошёл бы первую и провалил третью — а с одной пробой это было бы
 * незаметно.
 *
 * Служба вне карантина переноса.
 */
import { buildPlan, type PlanRequest } from "./graph-sandbox";

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? String(e); }
};
const запрос = (nodes: PlanRequest["nodes"]): PlanRequest =>
  ({ nodes, ceiling: "L4", counterpartyCheck: false });

describe("построение плана: цикл и неизвестная зависимость суть ОТКАЗЫ, а не забота исполнения", () => {
  it("годный план строится и упорядочивается", () => {
    const p = buildPlan(запрос([
      { module: "a", dependsOn: [] },
      { module: "b", dependsOn: ["a"] },
      { module: "c", dependsOn: ["a"] },
    ]));
    expect(p.nodes).toHaveLength(3);
  });

  it("UNKNOWN_DEPENDENCY — зависимость на модуль, которого в плане нет", () => {
    expect(код(() => buildPlan(запрос([
      { module: "a", dependsOn: ["нет-такого"] },
    ])))).toBe("UNKNOWN_DEPENDENCY");
  });

  it("CYCLIC_PLAN — двучленный цикл", () => {
    expect(код(() => buildPlan(запрос([
      { module: "a", dependsOn: ["b"] },
      { module: "b", dependsOn: ["a"] },
    ])))).toBe("CYCLIC_PLAN");
  });

  it("CYCLIC_PLAN — цикл длиной три, а не только пара", () => {
    expect(код(() => buildPlan(запрос([
      { module: "a", dependsOn: ["c"] },
      { module: "b", dependsOn: ["a"] },
      { module: "c", dependsOn: ["b"] },
    ])))).toBe("CYCLIC_PLAN");
  });

  it("цикл В ЧАСТИ плана ловится, даже если остальное ациклично", () => {
    expect(код(() => buildPlan(запрос([
      { module: "s", dependsOn: [] },
      { module: "a", dependsOn: ["b"] },
      { module: "b", dependsOn: ["a"] },
    ])))).toBe("CYCLIC_PLAN");
  });

  it("ORDER_VIOLATION — при проверке контрагента санкции обязаны быть ПЕРВЫМ шагом (I-01)", () => {
    const с_проверкой = (nodes: PlanRequest["nodes"]): PlanRequest =>
      ({ nodes, ceiling: "L4", counterpartyCheck: true });
    // санкции есть, но не первые: сперва идёт независимый узел
    expect(код(() => buildPlan(с_проверкой([
      { module: "a", dependsOn: [] },
      { module: "A.sanctions", dependsOn: ["a"] },
    ])))).toBe("ORDER_VIOLATION");
    // санкции первые — проходит
    expect(код(() => buildPlan(с_проверкой([
      { module: "A.sanctions", dependsOn: [] },
      { module: "b", dependsOn: ["A.sanctions"] },
    ])))).toBe("НЕ БРОСИЛ");
  });
});
