/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: стражи `acceptManifest` (`libraries/banksy-org/src/manifest.ts`) — те самые, что
 * стерегут ПРИНЯТУЮ КАРТУ, которой меряется вся миссия: 324 функции, две независимые ветви,
 * происхождение из коммита research.
 *
 * Семь из тринадцати отказов этого модуля не назывались НИ ОДНОЙ пробой дерева; проба закрывает
 * ДЕВЯТЬ стражей из десяти проверяемых. Она ведётся
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
 *
 * РАСШИРЕНО тем же тактом до десяти проб. Вторая канарейка — на самый доктринальный страж:
 * `MANIFEST_INDEPENDENT_BRANCH_SUBSTITUTED`. Ветвь MLRO переименована в `OVERSIGHT_TWO`, тип
 * оставлен: ветвей по-прежнему ДВЕ, **счётчик удовлетворён, независимость — нет**. Носитель
 * говорит это сам: «ветвь, переименованная в третью, независимость не создаёт, а лишь
 * удовлетворяет счётчику».
 *
 * Ослепление проверки имён (`joined + " MLRO AUDIT"`) даёт `Tests: 1 failed, 9 passed` —
 * покраснела ровно она.
 *
 * ОДИННАДЦАТАЯ ПРОБА — и главное доказательство этого файла. Она проверяет `MANIFEST_TAMPERED`
 * **КОДОМ**, тогда как проба дерева (`accepted-manifest.spec.ts:81`) проверяет только
 * `toThrow(OrgRefusal)`.
 *
 * ПАРА ПРОГОНОВ, СДЕЛАННАЯ 2026-09-10, — подмена отказа на СОСЕДНИЙ ТОГО ЖЕ КЛАССА
 * (`MANIFEST_TAMPERED` → `MANIFEST_WITHOUT_PROVENANCE`):
 *
 *     набор дерева (класс):   18 passed → 18 passed     ← СЛЕП
 *     эта проба (код):        11 passed → 1 failed      ← ловит
 *
 * То есть страж целостности принятой карты начал бы сообщать «манифест без происхождения» вместо
 * «манифест подделан», оператор искал бы не ту причину, а набор из восемнадцати проб сказал бы,
 * что всё хорошо. Класс `OrgRefusal` несёт тринадцать отказов; одна проба зачлась за все.
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { acceptManifest, type Manifest } from "./manifest";

// ПУТЬ ПЕЧАТАЕТСЯ (правило R5, `specs/gap-probe-must-name-its-reddening.md`). Проба-читатель,
// молчащая о прочитанном пути, неотличима от пробы, читающей соседа: в этой же линии
// `require.resolve` по имени пакета увёл пробу из снимка в живое дерево, и вскрыла это только
// непокрасневшая канарейка. Здесь путь берётся от `__dirname` и объявляется вслух.
const ПУТЬ_МАНИФЕСТА = join(__dirname, "../../../governance/org/accepted-org-manifest.json");
console.log("manifest-guards читает →", ПУТЬ_МАНИФЕСТА);
const ЖИВОЙ = JSON.parse(readFileSync(ПУТЬ_МАНИФЕСТА, "utf8")) as Manifest;
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

  it("MANIFEST_SUPERSESSION_WITHOUT_SUCCESSOR — замещён, преемник не назван", () => {
    const m = копия();
    const ps = (m.payload.passports as unknown as { status?: string; superseded_by?: string }[])[0]!;
    ps.status = "SUPERSEDED"; delete ps.superseded_by;
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_SUPERSESSION_WITHOUT_SUCCESSOR");
  });

  it("MANIFEST_AGENT_UNKNOWN — действующий паспорт без agent_id", () => {
    const m = копия();
    (m.payload.passports as unknown as { agent_id: string }[])[0]!.agent_id = "  ";
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_AGENT_UNKNOWN");
  });

  it("MANIFEST_AGENT_DUPLICATED — два действующих паспорта под одним агентом", () => {
    const m = копия();
    const ps = m.payload.passports as unknown as { agent_id: string; status?: string }[];
    const первый = ps.find((x) => (x.status ?? "").toUpperCase() !== "SUPERSEDED")!;
    const второй = ps.find((x) => x !== первый && (x.status ?? "").toUpperCase() !== "SUPERSEDED")!;
    второй.agent_id = первый.agent_id;
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_AGENT_DUPLICATED");
  });

  it("MANIFEST_INDEPENDENT_BRANCH_SUBSTITUTED — ветвей две, но имя подменено", () => {
    const m = копия();
    const n = m.payload.nodes as unknown as Record<string, { node_type: string }>;
    const мlro = Object.keys(n).find((k) => k.toUpperCase().includes("MLRO")
                                          && n[k]!.node_type === "INDEPENDENT_BRANCH")!;
    n["OVERSIGHT_TWO"] = n[мlro]!; delete n[мlro];
    // ветвей по-прежнему ДВЕ: счётчик удовлетворён, независимость — нет
    expect(код(() => acceptManifest(m, свой))).toBe("MANIFEST_INDEPENDENT_BRANCH_SUBSTITUTED");
  });

  it("MANIFEST_TAMPERED называется КОДОМ: класс отказа предмета не различает", () => {
    const m = копия();
    (m.payload.functions as unknown as { organisational_owner: string }[])[0]!
      .organisational_owner = "COO";
    // ВАЖНО: здесь проверяется КОД, а не класс. Соседняя проба дерева
    // (`accepted-manifest.spec.ts:81`) проверяет только `toThrow(OrgRefusal)` — и остаётся
    // ЗЕЛЁНОЙ, если этот страж начнёт сообщать любой другой из тринадцати отказов класса.
    // Доказано прогоном 2026-09-10: подмена MANIFEST_TAMPERED → MANIFEST_WITHOUT_PROVENANCE
    // оставила весь набор 18/18 зелёным.
    expect(код(() => acceptManifest(m, () => "чужой-хеш"))).toBe("MANIFEST_TAMPERED");
  });
});
