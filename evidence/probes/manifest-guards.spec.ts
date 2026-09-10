/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: стражи `acceptManifest` (`libraries/banksy-org/src/manifest.ts`) — те самые, что
 * стерегут ПРИНЯТУЮ КАРТУ, которой меряется вся миссия: 324 функции, две независимые ветви,
 * происхождение из коммита research.
 *
 * Семь из тринадцати отказов этого модуля не назывались НИ ОДНОЙ пробой дерева. Проба ведётся
 * на НАСТОЯЩЕМ манифесте (`governance/org/accepted-org-manifest.json`), а не на игрушечном:
 * хеш подаётся снаружи, поэтому меряются проверки СОДЕРЖИМОГО, а не пересчёт хеша.
 *
 * КАНАРЕЙКА, ПРОВЕДЁННАЯ И ЗАПИСАННАЯ. Страж повторов ослеплён ИЗМЕНЕНИЕМ ВХОДА, а не вырезом
 * блока: `seenFn.has(f.function_id)` → `seenFn.has(f.function_id + "\u0000никогда")`. Тип цел,
 * число проверок цело, сборка цела. Результат: `Tests: 1 failed, 5 passed` — покраснела РОВНО
 * та проба, и ответ был `НЕ БРОСИЛ`.
 *
 * ПОЧЕМУ ВХОД, А НЕ ВЫРЕЗ. Первая попытка вырезала блок и уронила сборку: `Tests: 0 total`.
 * Канарейка, ломающая сборку, не измеряет ничего — она лишь показывает, что код перестал
 * компилироваться.
 *
 * ЧЕМ ЭТО ГРОЗИТ БЕЗ СТРАЖА: манифест с повторяющимся идентификатором принимается, и карта несёт
 * 323 различных функции, объявляя 324.
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { acceptManifest, type Manifest } from "./manifest";

const ЖИВОЙ = JSON.parse(
  readFileSync(join(__dirname, "../../../governance/org/accepted-org-manifest.json"), "utf8"),
) as Manifest;
// Хеш подаётся снаружи: проба меряет ПРОВЕРКИ СОДЕРЖИМОГО, а не пересчёт хеша.
const свой = () => ЖИВОЙ.integrity.digest;
const копия = (): Manifest => JSON.parse(JSON.stringify(ЖИВОЙ)) as Manifest;
const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? String(e); }
};

describe("стражи принятого манифеста карты", () => {
  it("настоящий манифест принимается", () => {
    const a = acceptManifest(ЖИВОЙ, свой);
    expect(a.functionsById.size).toBe(324);
    expect(a.independentBranches).toHaveLength(2);
  });

  it("MANIFEST_FUNCTION_INCOMPLETE — функция без имени", () => {
    const m = копия();
    (m.payload.functions as unknown as { name: string }[])[0]!.name = "  ";
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_FUNCTION_INCOMPLETE");
  });

  it("MANIFEST_FUNCTION_DUPLICATED — два одинаковых идентификатора", () => {
    const m = копия();
    const fs = m.payload.functions as unknown as { function_id: string }[];
    fs[1]!.function_id = fs[0]!.function_id;
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_FUNCTION_DUPLICATED");
  });

  it("MANIFEST_PASSPORT_WITHOUT_STATUS — паспорт без состояния", () => {
    const m = копия();
    delete (m.payload.passports as unknown as { status?: string }[])[0]!.status;
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_PASSPORT_WITHOUT_STATUS");
  });

  it("MANIFEST_LOST_AN_INDEPENDENT_BRANCH — потеря независимой ветви", () => {
    const m = копия();
    const n = m.payload.nodes as Record<string, { node_type: string }>;
    const ветвь = Object.entries(n).find(([, v]) => v.node_type === "INDEPENDENT_BRANCH")![0];
    n[ветвь]!.node_type = "EXECUTIVE_DEPARTMENT";
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_LOST_AN_INDEPENDENT_BRANCH");
  });

  it("MANIFEST_SOURCE_STALE — манифест из другого коммита research", () => {
    expect(код(() => acceptManifest(ЖИВОЙ, свой, { expectedResearchSha: "0".repeat(40) })))
      .toBe("MANIFEST_SOURCE_STALE");
  });
});
