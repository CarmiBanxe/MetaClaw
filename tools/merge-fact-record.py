#!/usr/bin/env python3
"""X-02 · Проверяемая запись факта слияния — выводится ИЗ РЕПОЗИТОРИЯ.

РЕШЕНИЕ 6 (оператор, 2026-09-10): «Для последующих слияний вести проверяемую запись факта:
исходные и итоговый SHA, источник события, связанные результаты CI и review, если они
существуют. Запись о слиянии сама по себе не доказывает качество или санкционирование.
Новый разрешительный барьер этим поручением не вводится.»

ПОЧЕМУ НЕ ДОПИСЫВАТЬ В СУЩЕСТВУЮЩИЙ ЖУРНАЛ. `governance/merge-readiness-verdicts.jsonl`
пишет сам `guarded-merge.py`. Запись, которую делает инструмент санкционированного пути,
может описать только санкционированный путь: слияние мимо него следа не оставляет. Это
запись ПУТИ, а не факта. Здесь запись выводится из самого `main`, и потому не зависит от
того, чем слияние сделано.

МЕРА НЕ ОТКАЗЫВАЕТ НИ ПРИ КАКОМ СОДЕРЖИМОМ ЗАПИСИ (R4). Код возврата всегда 0, кроме
случая, когда не удалось прочитать репозиторий. Мера, способная отказать по содержимому,
ввела бы разрешительный барьер, которого поручение прямо не вводит.
"""

import argparse
import json
import subprocess
import sys
from collections import Counter

НЕ_ДОКАЗЫВАЕТ = (
    "ЗАПИСЬ О СЛИЯНИИ НЕ ДОКАЗЫВАЕТ КАЧЕСТВА И НЕ ДОКАЗЫВАЕТ САНКЦИОНИРОВАНИЯ. "
    "Она фиксирует факт, что слияние состоялось, и ничего сверх того."
)
ЖУРНАЛ = "governance/merge-readiness-verdicts.jsonl"
НЕИЗВЕСТНО = "неизвестен"  # R3: отсутствие есть ЗНАЧЕНИЕ, а не пропуск поля
НЕТ = "нет"


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"не удалось прочитать репозиторий: git {' '.join(args)}\n{r.stderr}")
    return r.stdout


def прежний_журнал(repo):
    """Прежние записи — по итоговому SHA и по исходным SHA. Журнал НЕ переписывается (R7)."""
    по_итогу, по_исходному = {}, {}
    try:
        текст = open(f"{repo}/{ЖУРНАЛ}", encoding="utf-8").read()
    except OSError:
        return по_итогу, по_исходному
    for строка in текст.splitlines():
        if not строка.strip():
            continue
        try:
            r = json.loads(строка)
        except json.JSONDecodeError:
            continue
        if r.get("merge_commit"):
            по_итогу[r["merge_commit"][:12]] = r
        for k in ("branch_head_sha", "tested_sha"):
            if r.get(k):
                по_исходному.setdefault(r[k][:12], r)
    return по_итогу, по_исходному


def слияния(repo, ref, предел):
    поле = "%H%x1f%cI%x1f%P%x1f%an%x1f%cn%x1f%s"
    вывод = git(repo, "log", "--merges", f"-{предел}", f"--format={поле}", ref)
    for строка in вывод.splitlines():
        h, ci, родители, автор, коммиттер, тема = строка.split("\x1f")
        yield {
            "sha": h,
            "at": ci,
            "parents": родители.split(),
            "author": автор,
            "committer": коммиттер,
            "subject": тема,
        }


def источник_события(м, прежняя):
    """R2 — кем или чем слияние совершено. R3 — «неизвестен» есть значение."""
    if прежняя and прежняя.get("mr"):
        return f"guarded-merge, MR {прежняя['mr']}"
    тема = м["subject"]
    if тема.startswith("Merge branch") or тема.startswith("Merge remote"):
        return f"git merge, коммиттер {м['committer']}"
    if "See merge request" in тема or тема.startswith("Merge pull request"):
        return f"forge, коммиттер {м['committer']}"
    return f"{НЕИЗВЕСТНО} (коммиттер {м['committer']})"


def ci_результат(прежняя):
    """R3: отсутствие CI — значение «нет», а не отсутствующее поле."""
    if not прежняя:
        return НЕТ
    вывод = прежняя.get("merge_output") or ""
    if "Pipeline Succeeded" in вывод or "✓ Pipeline" in вывод:
        return "succeeded (из merge_output прежнего журнала)"
    if "Pipeline Failed" in вывод or "✗" in вывод:
        return "failed (из merge_output прежнего журнала)"
    if прежняя.get("ready") is not None:
        return f"ready={прежняя['ready']} (поле прежнего журнала, не результат CI)"
    return НЕТ


def запись(м, по_итогу, по_исходному):
    прежняя = по_итогу.get(м["sha"][:12])
    if прежняя is None:
        for p in м["parents"]:
            if p[:12] in по_исходному:
                прежняя = по_исходному[p[:12]]
                break
    return {
        "merge_sha": м["sha"],  # итоговый SHA
        "parent_shas": м["parents"],  # исходные SHA
        "at": м["at"],
        "event_source": источник_события(м, прежняя),
        "ci_result": ci_результат(прежняя),
        "review_result": (
            f"MR {прежняя['mr']} state={прежняя.get('mr_state', НЕИЗВЕСТНО)}" if прежняя and прежняя.get("mr") else НЕТ
        ),
        "prior_journal_entry": (
            прежняя.get("merge_commit") or прежняя.get("branch_head_sha") if прежняя else None
        ),  # ССЫЛКА на прежний журнал, не копия (E4)
        "proves": "nothing",  # R5, машиночитаемо
    }


def главное():
    p = argparse.ArgumentParser(description="запись факта слияния, выведенная из репозитория")
    p.add_argument("--repo", default=".")
    p.add_argument("--ref", default="HEAD")
    p.add_argument("--limit", type=int, default=400)
    p.add_argument("--since", help="ISO-час; по умолчанию — час первой записи прежнего журнала")
    p.add_argument("--jsonl", help="куда писать записи; без него печатается только сводка")
    p.add_argument(
        "--самопроверка", action="store_true", help="A4: показать, что мера не отказывает ни при каком содержимом"
    )
    a = p.parse_args()

    по_итогу, по_исходному = прежний_журнал(a.repo)
    начало = a.since
    if начало is None:
        часы = []
        try:
            for строка in open(f"{a.repo}/{ЖУРНАЛ}", encoding="utf-8"):
                if строка.strip():
                    ч = json.loads(строка).get("at")
                    if ч:
                        часы.append(ч)
        except (OSError, json.JSONDecodeError):
            pass
        начало = min(часы) if часы else "0000"

    все = list(слияния(a.repo, a.ref, a.limit))
    после = [м for м in все if м["at"] >= начало]
    записи = [запись(м, по_итогу, по_исходному) for м in после]

    без_прежней = [z for z in записи if z["prior_journal_entry"] is None]
    неизвестен = [z for z in записи if z["event_source"].startswith(НЕИЗВЕСТНО)]
    по_коммиттеру = Counter(м["committer"] for м in после)
    без_по_коммиттеру = Counter(м["committer"] for м, z in zip(после, записи) if z["prior_journal_entry"] is None)

    if a.jsonl:
        with open(a.jsonl, "w", encoding="utf-8") as f:
            f.write(f"# {НЕ_ДОКАЗЫВАЕТ}\n")
            for z in записи:
                f.write(json.dumps(z, ensure_ascii=False) + "\n")

    print(НЕ_ДОКАЗЫВАЕТ)
    print(f"\nграница отсчёта: {начало}")
    print(f"слияний в {a.ref} после границы: {len(после)}   записей выведено: {len(записи)}")
    print(f"расхождение (R6): {len(после) - len(записи)}")
    print(
        f"\nиз них БЕЗ записи в прежнем журнале: {len(без_прежней)}"
        f"  — это не дефект записи факта, а мера охвата прежнего журнала"
    )
    print(f"источник события «{НЕИЗВЕСТНО}»: {len(неизвестен)} (R3: значение, а не пропуск)")
    print("\nохват прежнего журнала по коммиттеру:")
    for кто, всего in по_коммиттеру.most_common():
        нет = без_по_коммиттеру.get(кто, 0)
        print(f"   {кто:28s} слияний {всего:4d}   без записи {нет:4d}   охват {100 * (всего - нет) / всего:5.1f}%")

    if a.самопроверка:
        print("\nA4 — самопроверка: мера не отказывает по содержимому")
        for имя, м in [
            (
                "слияние без родителей",
                {
                    "sha": "0" * 40,
                    "at": "2026-01-01T00:00:00Z",
                    "parents": [],
                    "author": "x",
                    "committer": "x",
                    "subject": "",
                },
            ),
            (
                "пустая тема и нет прежней",
                {
                    "sha": "1" * 40,
                    "at": "2026-01-01T00:00:00Z",
                    "parents": ["2" * 40],
                    "author": "",
                    "committer": "",
                    "subject": "",
                },
            ),
        ]:
            z = запись(м, {}, {})
            print(
                f"   {имя:32s} → источник={z['event_source']!r} ci={z['ci_result']!r} "
                f"review={z['review_result']!r}  ОТКАЗА НЕТ"
            )
    return 0  # R4: всегда 0


if __name__ == "__main__":
    sys.exit(главное())
