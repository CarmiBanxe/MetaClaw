#!/usr/bin/env python3
"""Карта «служба дерева → донорский набор проб», выведенная ПО ИМПОРТАМ.

ЗАЧЕМ НЕ ПО ИМЕНИ. Соответствие по имени каталога в этой линии ошиблось шесть раз подряд, и
каждый раз в одну сторону — занижало. Уклады донора:

  1. `tests/test_<служба>/`                  центральный
  2. `tests/emi-stack/test_<служба>/`        центральный, второй репозиторий
  3. `services/<домен>/<служба>/tests/`      рядом со службой
  4. имя через ДЕФИС вместо подчёркивания    `payment-orchestration`, `trading-gateway`
  5. имя по СОДЕРЖАНИЮ, а не по службе       `test_fin060_reporting` есть набор службы `reporting`

Пятый уклад именем не ловится ни при каком образце: имя описывает предмет проб, а не службу.
Надёжен только один признак — ЧТО набор импортирует. `from services.reporting.report_models import …`
называет службу прямо, и ошибиться в нём нельзя.

ЧЕГО МЕРА НЕ ДЕЛАЕТ. Она не утверждает, что набор зелен, и не заменяет условие 5 реестра
карантина: два зелёных прогона суть отдельная работа. Она отвечает на один вопрос — ЕСТЬ ЛИ у
службы донорский набор и где он лежит.
"""

import argparse
import collections
import json
import pathlib
import re
import sys

ИМПОРТ = re.compile(r"^\s*(?:from|import)\s+(?:services|src)\.([A-Za-z0-9_]+)", re.M)
ИМПОРТ2 = re.compile(r"^\s*from\s+(?:services|src)\.[A-Za-z0-9_]+\.([A-Za-z0-9_]+)", re.M)


def службы_набора(файл: pathlib.Path) -> set[str]:
    """Какие службы донора набор импортирует. Возвращает оба уровня: домен и службу."""
    try:
        текст = файл.read_text(errors="ignore")
    except OSError:
        return set()
    имена = set(ИМПОРТ.findall(текст)) | set(ИМПОРТ2.findall(текст))
    return {и.replace("-", "_") for и in имена}


def собрать(корни: list[pathlib.Path]) -> dict[str, set[str]]:
    """служба → пути наборов. ДВА прибора, и ни один в одиночку не полон.

    ПРИБОР 1 — ИМПОРТЫ. Центральный набор называет службу прямо:
    `from services.reporting.report_models import …`. Ловит и пятый уклад, где имя каталога
    описывает предмет проб (`test_fin060_reporting`), а не службу.

    ПРИБОР 2 — РАСПОЛОЖЕНИЕ. Набор, лежащий ВНУТРИ службы (`services/<домен>/<служба>/tests/`),
    её НЕ НАЗЫВАЕТ: ему незачем — он импортирует `src.…` либо имя пакета
    (`banxe_trading_backend`). Импортами такой набор не находится ни при каком образце.

    Ни один прибор в одиночку не полон, и это не тонкость: счёт в этой линии двигался
    9 → 205 → 187 → 213 → 221 → 225, шесть раз, и каждый сдвиг был сменой прибора, а не предмета.
    """
    карта: dict[str, set[str]] = collections.defaultdict(set)
    for корень in корни:
        for ф in корень.rglob("test_*.py"):
            if any(ч in (".venv", "node_modules", ".git") for ч in ф.parts):
                continue
            for служба in службы_набора(ф):
                карта[служба].add(str(ф))
        # ПРИБОР 2: набор внутри службы приписывается ей по месту.
        for тесты in корень.glob("services/*/*/tests"):
            if not тесты.is_dir():
                continue
            служба = тесты.parent.name.replace("-", "_")
            for ф in тесты.rglob("test_*.py"):
                карта[служба].add(str(ф))
    return карта


def главное() -> int:
    p = argparse.ArgumentParser(description="карта донорских наборов по импортам")
    p.add_argument("--доноры", nargs="+", required=True)
    p.add_argument("--покрытие", required=True, help="governance/org/function-coverage.json дерева")
    p.add_argument("--json", help="куда сложить карту")
    a = p.parse_args()

    карта = собрать([pathlib.Path(д) for д in a.доноры])
    cov = json.loads(pathlib.Path(a.покрытие).read_text(encoding="utf-8"))
    заперты = [b for b in cov["blocked"] if "QUARANTINE" in str(b.get("blocked_by"))]
    по_службе: collections.Counter = collections.Counter()
    for b in заперты:
        части = ((b.get("carrier_seen") or {}).get("path") or "").split("/")
        по_службе[части[2] if len(части) > 2 else "?"] += 1

    есть, нет = [], []
    for служба, функций in по_службе.items():
        (есть if карта.get(служба) else нет).append((служба, функций, len(карта.get(служба, ()))))

    print(f"донорских служб, названных импортами: {len(карта)}")
    print(f"служб с запертыми функциями: {len(по_службе)} | функций: {sum(по_службе.values())}")
    print(f"  донорский набор НАЙДЕН: служб {len(есть):3d}  функций {sum(n for _, n, _ in есть):3d}")
    print(f"  НЕ найден:              служб {len(нет):3d}  функций {sum(n for _, n, _ in нет):3d}")
    for с, n, _ in sorted(нет, key=lambda x: -x[1]):
        print(f"      {n:3d} функц.  {с}")
    print("\nкрупнейшие, с числом файлов набора:")
    for с, n, ф in sorted(есть, key=lambda x: -x[1])[:10]:
        print(f"      {n:3d} функц.  {с:28s} файлов {ф}")
    if a.json:
        pathlib.Path(a.json).write_text(
            json.dumps({с: sorted(п) for с, п in карта.items()}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    sys.exit(главное())
