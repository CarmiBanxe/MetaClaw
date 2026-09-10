#!/usr/bin/env python3
"""Чем держится отказ: ТИПОМ или только пробой.

**Зачем.** 2026-09-10 канарейка на `FACTS_INCOMPLETE` не собралась: ослабление `||` до `&&`
дало `TS2322 — 'undefined' is not assignable`. Отказ СУЖАЕТ тип, и снять его молча нельзя.
В тот же час десятки других стражей — сравнение с слабейшим звеном, обнаружение цикла, различие
одобряющих, полнота выборки, роль происхождения — снимались **без единой жалобы компилятора**.

Разница существенна и до этого замера нигде не была названа числом:

  ДЕРЖИТ ТИП    — тихое удаление НЕВОЗМОЖНО: сборка падает по имени поля;
  ТОЛЬКО ПРОБА  — между мерой и её тихим удалением стоит ровно одна проба, и если проба
                  оказалась не такой, как о ней думали, не стоит ничего.

**Способ.** Ослепить страж (`if (X) {` → `if ((X) && false) {`) и собрать проект. Приём
типобезопасен по форме: он не меняет типов выражения, он лишь отнимает СУЖЕНИЕ. Падение сборки и
означает, что сужение было несущим.

**ПРЕДЕЛЫ, печатаемые при каждом прогоне:**
  1. Ослепляется БЛИЖАЙШИЙ предшествующий `if` в шести строках. Отказ, стоящий не за одиночным
     `if` — в `catch`, в `switch`, безусловный, — пропускается и считается отдельно.
  2. `if`, занимающий несколько строк, не разбирается: форма `if (...) {` на одной строке.
  3. Замер говорит о СУЖЕНИИ ТИПА, а не о полезности стража. Отказ, который держит тип, всё
     равно стоит пробы — но цена её отсутствия иная.
  4. Дерево восстанавливается после каждой подсадки, и в конце проверяется, что оно собирается.
     Прогон, оставивший дерево изменённым, есть неисправность замера.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import subprocess
import sys

ОТКАЗ = re.compile(r"new\s+[A-Za-z]*Refusal\(|refusalCode:")
КОД = re.compile(r'"([A-Z][A-Z0-9_]{3,})"')
IF = re.compile(r"^(\s*)if \((.*)\) \{\s*$")


def собирается(проект: str) -> bool:
    r = subprocess.run(["npx", "tsc", "-p", проект, "--noEmit"], capture_output=True, text=True)
    return r.returncode == 0


def места(строки: list[str]) -> list[tuple[int, str]]:
    """Отказы вместе с номером строки. Ловится и однострочная форма, и код строкой ниже."""
    out: list[tuple[int, str]] = []
    for i, с in enumerate(строки):
        if not ОТКАЗ.search(с):
            continue
        m = КОД.search(с)
        if m:
            out.append((i, m.group(1)))
        elif i + 1 < len(строки):
            m2 = re.match(r'^\s*"([A-Z][A-Z0-9_]{3,})"', строки[i + 1])
            if m2:
                out.append((i, m2.group(1)))
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--src", required=True, help="каталог исходников")
    p.add_argument("--project", required=True, help="tsconfig проекта")
    a = p.parse_args()

    print(__doc__.split("**Зачем.**")[0].strip())
    if not собирается(a.project):
        print("замер невозможен: дерево не собирается ДО подсадок")
        return 1

    файлы = []
    for корень, каталоги, имена in os.walk(a.src):
        каталоги[:] = [d for d in каталоги if d not in ("dist", "node_modules")]
        файлы += [os.path.join(корень, f) for f in имена if f.endswith(".ts") and ".spec." not in f]

    тип: list[str] = []
    проба: list[str] = []
    вне: list[str] = []
    for путь in файлы:
        исход = io.open(путь, encoding="utf-8").read()
        строки = исход.split("\n")
        for i, код in места(строки):
            j = next((k for k in range(i, max(-1, i - 7), -1) if re.match(r"\s*if \(", строки[k])), None)
            м = IF.match(строки[j]) if j is not None else None
            if м is None:
                вне.append(код)
                continue
            новые = строки[:]
            новые[j] = f"{м.group(1)}if (({м.group(2)}) && false) {{"
            io.open(путь, "w", encoding="utf-8").write("\n".join(новые))
            (проба if собирается(a.project) else тип).append(код)
            io.open(путь, "w", encoding="utf-8").write(исход)

    if not собирается(a.project):
        print("НЕИСПРАВНОСТЬ ЗАМЕРА: дерево не восстановлено")
        return 1

    всего = len(тип) + len(проба) + len(вне)
    print(f"\nмест отказа осмотрено: {всего}")
    print(f"  ДЕРЖИТ ТИП   {len(тип):>4}  — тихое удаление невозможно, сборка падает")
    print(f"  ТОЛЬКО ПРОБА {len(проба):>4}  — между мерой и её удалением стоит одна проба")
    print(f"  вне одиночного `if` {len(вне):>3}  — не осмотрено, см. предел 1")
    print("\nДЕРЖИТ ТИП, поимённо:")
    for к in sorted(set(тип)):
        print(f"  {к}")
    print(
        "\nПРЕДЕЛЫ, печатаются всегда: ослепляется ближайший `if` в шести строках, форма `if (…) {` "
        "на одной строке; замер говорит о СУЖЕНИИ ТИПА, а не о полезности стража."
    )
    json.dump(
        {"тип": sorted(set(тип)), "проба": sorted(set(проба)), "вне": sorted(set(вне))},
        io.open("type-vs-probe.json", "w", encoding="utf-8"),
        ensure_ascii=False,
        indent=1,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
