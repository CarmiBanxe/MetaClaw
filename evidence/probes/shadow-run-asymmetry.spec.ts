/**
 * ДОКАЗАННАЯ ПРОБА — прогон и ДВЕ канарейки 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `SHADOW_SIDE_EFFECT` и `SAMPLE_TOO_SMALL` (`conductor/src/substrate/shadow.ts`) —
 * оба не назывались ни одной пробой дерева. Довод носителя: «тень, изменившая состояние, тенью
 * не является».
 *
 * ГЛАВНОЕ ЗДЕСЬ — АСИММЕТРИЯ, которую легко потерять правкой:
 *   малая выборка И НОЛЬ расхождений  → ОТКАЗ («ноль расхождений здесь означает, что мало
 *                                       смотрели»)
 *   малая выборка И ЕСТЬ расхождение  → НЕ отказ (нашли — значит смотрели не зря), но
 *                                       `conclusive: false`
 *
 * КАНАРЕЙКА 1 — защита. `run.sideEffects.length` → `> 1_000_000`: побочное действие перестаёт
 * ловиться. `Tests: 2 failed, 3 passed` — покраснели обе пробы побочного действия.
 *
 * КАНАРЕЙКА 2 — асимметрия. `divergences.length === 0` → `>= 0`: малая выборка отказывает
 * ВСЕГДА. `Tests: 1 failed, 4 passed` — покраснела РОВНО четвёртая.
 *
 * И вот довод, ради которого четвёртая проба написана: под второй канарейкой третья остаётся
 * ЗЕЛЁНОЙ. Набор без четвёртой пробы принял бы потерю асимметрии за исправную работу —
 * а потеря эта превращает «мало смотрели» в «смотреть незачем».
 *
 * Служба вне карантина переноса.
 */
import { assess, type ShadowRun } from "./shadow";

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? String(e); }
};
const ход = (o: Partial<ShadowRun>): ShadowRun =>
  ({ sideEffects: [], divergences: [], sampleSize: 100, minSample: 10, ...o }) as ShadowRun;

describe("теневой прогон: тень, изменившая состояние, тенью не является", () => {
  it("SHADOW_SIDE_EFFECT — хоть одно побочное действие есть отказ", () => {
    expect(код(() => assess(ход({ sideEffects: ["записал строку"] })))).toBe("SHADOW_SIDE_EFFECT");
  });

  it("побочное действие важнее малой выборки: проверяется ПЕРВЫМ", () => {
    expect(код(() => assess(ход({ sideEffects: ["x"], sampleSize: 1, minSample: 10 }))))
      .toBe("SHADOW_SIDE_EFFECT");
  });

  it("SAMPLE_TOO_SMALL — мало смотрели И НИ ОДНОГО расхождения", () => {
    expect(код(() => assess(ход({ sampleSize: 3, minSample: 10 })))).toBe("SAMPLE_TOO_SMALL");
  });

  it("малая выборка С расхождением отказом НЕ является: нашли — значит смотрели не зря", () => {
    const r = assess(ход({ sampleSize: 3, minSample: 10, divergences: ["d1"] as never }));
    expect(r.divergences).toHaveLength(1);
    expect(r.conclusive).toBe(false);   // и всё же вывод НЕ окончателен
  });

  it("достаточная выборка без расхождений проходит и объявляется окончательной", () => {
    const r = assess(ход({ sampleSize: 100, minSample: 10 }));
    expect(r.conclusive).toBe(true);
    expect(r.divergences).toHaveLength(0);
  });
});
