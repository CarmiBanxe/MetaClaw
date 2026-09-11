"""Достижимость носителя от службы — по ВВОЗУ, не по имени и не по соседству.

Правило из `specs/coverage-counts-reachable-carriers.md`: «достижимость измеряется ввозом…
ввоз ТИПОМ достижимостью не является». Значит `import type { X }` не считается: при сборке он
стирается, и во время исполнения такого ввоза нет.

Корни обхода — точки входа служб: `services/*/*/src/main.ts`, `http/server.ts`, `index.ts`.
"""

import collections
import json
import pathlib
import re
import sys

КОРЕНЬ = pathlib.Path(sys.argv[1])
ТИПОВОЙ = re.compile(r"^\s*import\s+type\s", re.M)
ВВОЗ = re.compile(r"""^\s*(?:import|export)\s+(?!type\s)[^;]*?from\s+["']([^"']+)["']""", re.M)

import json as _json
import re as _re

_псев: dict[str, str] = {}
try:
    _т = (КОРЕНЬ / "tsconfig.base.json").read_text(errors="ignore")
    _т = _re.sub(r"//[^\n]*", "", _т)
    _т = _re.sub(r",(\s*[}\]])", r"\1", _т)
    for _k, _v in (_json.loads(_т).get("compilerOptions", {}).get("paths", {}) or {}).items():
        if _v:
            _псев[_k.rstrip("/*")] = _v[0]
except (OSError, ValueError):
    pass


def разрешить(откуда: pathlib.Path, цель: str) -> pathlib.Path | None:
    """Относительный ввоз И пакетный псевдоним. Без второго библиотеки выглядят недостижимыми."""
    if цель.startswith("."):
        p = (откуда.parent / цель).resolve()
        for к in (p.with_suffix(".ts"), p / "index.ts", p):
            if к.is_file():
                return к
        return None
    for имя, куда in _псев.items():
        if цель == имя or цель.startswith(имя + "/"):
            хвост = цель[len(имя) :].lstrip("/")
            корень_пс = (КОРЕНЬ / куда).resolve()
            if not хвост:
                return корень_пс if корень_пс.is_file() else None
            баз = корень_пс.parent / хвост
            for к in (баз.with_suffix(".ts"), баз / "index.ts", баз):
                if к.is_file():
                    return к
    return None


def ввозы(ф: pathlib.Path) -> list[str]:
    try:
        т = ф.read_text(errors="ignore")
    except OSError:
        return []
    строки = [s for s in т.split("\n") if not ТИПОВОЙ.match(s)]
    return ВВОЗ.findall("\n".join(строки))


входы = []
for шаб in ("services/*/*/src/main.ts", "services/*/*/src/http/server.ts", "services/*/*/src/index.ts"):
    входы += list(КОРЕНЬ.glob(шаб))
видел, очередь = set(), list(входы)
while очередь:
    ф = очередь.pop()
    if ф in видел:
        continue
    видел.add(ф)
    for ц in ввозы(ф):
        if (к := разрешить(ф, ц)) and к not in видел:
            очередь.append(к)

cov = json.loads((КОРЕНЬ / "governance/org/function-coverage.json").read_text(encoding="utf-8"))
дост, нед = [], []
for c in cov["covered"]:
    п = (c.get("carrier") or {}).get("path") or ""
    (дост if (КОРЕНЬ / п).resolve() in видел else нед).append((c["function_id"], п))
print(f"входов служб: {len(входы)} | достижимых файлов: {len(видел)}")
print(f"покрыто {len(cov['covered'])} | ДОСТИЖИМО ОТ СЛУЖБЫ {len(дост)} | недостижимо {len(нед)}")
print("недостижимые, поимённо:")
for f, p in sorted(нед):
    print(f"   {f:14s} {p}")
