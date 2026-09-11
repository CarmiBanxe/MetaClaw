#!/usr/bin/env python3
"""Сплошной прогон проб центрального терминала в снимке.

ЗАЧЕМ ОТДЕЛЬНАЯ МЕРА. Число «31 проба, 142 зелены» полезно ровно настолько, насколько его можно
переснять. Число, которое нельзя переснять, есть воспоминание.

ЧТО МЕРА ДЕЛАЕТ И ЧЕГО НЕ ДЕЛАЕТ. Она размещает пробы в снимке, удаляет прежние копии и гоняет
каждый проект его собственной конфигурацией. Она НЕ судит о том, верны ли пробы: зелёная проба
может измерять ноль, и это ловится обходом по тексту, а не прогоном. Два приёма находят разное.

ПРЕЖНИЕ КОПИИ УДАЛЯЮТСЯ ОБЯЗАТЕЛЬНО. Двадцать семь копий `zz-*`, оставшихся от прежних прогонов,
складывали число из двух файлов: «8 passed» оказалось четырьмя пробами дважды, причём старая
половина несла утверждение `expect(true).toBe(true)`.
"""

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys

ПРЕФИКС = "cc-"
ЧУЖИЕ = ("zz-", "cc-")

# Размещение проб по проектам. Ключ — имя файла пробы, значение — каталог в снимке.
РАЗМЕЩЕНИЕ = {
    "append-only-reachability": "libraries/banksy-mlro-boundary/src",
    "timeout-never-approves": "libraries/banksy-mlro-boundary/src",
    "s3-06-receipt-binding-protection": "libraries/banksy-mlro-boundary/src",
    "s3-07-server-policy-protection": "libraries/banksy-mlro-boundary/src",
    "s3-08-replay-bound-to-content-protection": "libraries/banksy-mlro-boundary/src",
    "central-restore-dual-control-probe-2026-09-10": "libraries/banksy-durable/src",
    "manifest-guards": "libraries/banksy-org/src",
    "memory-idempotence": "libraries/banksy-memory/src",
    "plan-executor-guards": "libraries/banksy-plan/src",
    "queue-legacy-subject": "libraries/banksy-hitl/src",
    "s1-03-role-self-appointment": "libraries/banksy-hitl/src",
    "s1-07-egress-bypass-map": "libraries/banksy-data-class/src",
    "central-x03-approval-flag-2026-09-11": "services/ledger/ledger/src",
    "s2-05-kyc-port-characterisation": "services/onboarding/kyc/src",
    "conversation-customer-isolation": "services/banksy/customer-gateway/src",
    "gateway-origin-and-facts": "services/banksy/customer-gateway/src",
    "s1-04-context-gap-demo": "services/banksy/customer-gateway/src",
    "tool-context-unreachable": "services/banksy/customer-gateway/src",
    "s1-01-admission-layers": "services/banksy/conductor/src",
    "instruction-outcome": "services/banksy/conductor/src/adapters",
    "conductor-three-guards": "services/banksy/conductor/src/orchestrator",
    "cost-construction": "services/banksy/conductor/src/orchestrator",
    "plan-graph-cycles": "services/banksy/conductor/src/orchestrator",
    "shadow-run-asymmetry": "services/banksy/conductor/src/substrate",
    "substrate-five-guards": "services/banksy/conductor/src/substrate",
    "central-a12-end-to-end-probe-2026-09-10": "services/banksy/conductor/src/http",
    "central-authority-substitution-probe-2026-09-10": "services/banksy/conductor/src/http",
    "enforcement-slot-fail-closed": "services/banksy/conductor/src/http",
    "s1-08-interruption-identity-gap": "services/banksy/conductor/src/http",
    "s1-09-handoff-chain-measure": "services/banksy/conductor/src/http",
    "s1-10-decision-trace": "services/banksy/conductor/src/http",
}


def проекты(снимок: pathlib.Path) -> list[str]:
    """Проекты, в которых оказались пробы, — по размещению, а не по догадке."""
    из_путей = set()
    for каталог in РАЗМЕЩЕНИЕ.values():
        части = каталог.split("/")
        # проект есть тот каталог вверх по пути, где лежит jest.config.ts
        for глубина in range(len(части), 0, -1):
            кандидат = "/".join(части[:глубина])
            if (снимок / кандидат / "jest.config.ts").exists():
                из_путей.add(кандидат)
                break
    return sorted(из_путей)


def разместить(снимок: pathlib.Path, источник: pathlib.Path) -> tuple[int, int, list[str]]:
    убрано = 0
    for шаблон in ("libraries/**/*.spec.ts", "services/**/*.spec.ts"):
        for f in снимок.glob(шаблон):
            if f.name.startswith(ЧУЖИЕ):
                f.unlink()
                убрано += 1
    размещено, неразмещённые = 0, []
    for p in sorted(источник.glob("*.spec.ts")):
        имя = p.name.removesuffix(".spec.ts")
        каталог = РАЗМЕЩЕНИЕ.get(имя)
        if каталог is None:
            неразмещённые.append(p.name)
            continue
        цель = снимок / каталог / (ПРЕФИКС + p.name)
        цель.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(p, цель)
        размещено += 1
    return размещено, убрано, неразмещённые


def убрать(снимок: pathlib.Path) -> int:
    """Снять СВОИ пробы с дерева после прогона. Возвращает число снятых.

    ЗАЧЕМ. 2026-09-11 обход оставил 31 пробу в ОБЩЕМ дереве интеграции, и они были взяты jest
    наравне с деревом: `conductor` показал 493 вместо 435, `mlro-boundary` 311 вместо 292,
    и четыре набора числились КРАСНЫМИ. Чужая линия сведения потратила такт на объяснение
    чисел, которые я же и сдвинула.

    ПРОБЫ ЦЕНТРАЛЬНОГО ТЕРМИНАЛА СУТЬ ПРИБОР, А НЕ ДЕРЕВО. Прибор, оставленный внутри
    измеряемого, меряет себя вместе с предметом.
    """
    снято = 0
    for f in снимок.rglob("cc-*.spec.ts"):
        if "node_modules" in f.parts:
            continue
        f.unlink()
        снято += 1
    return снято


def прогнать(снимок: pathlib.Path, проект: str) -> dict:
    файлов = len(list((снимок / проект).rglob(ПРЕФИКС + "*.spec.ts")))
    if файлов == 0:
        return {"проект": проект, "файлов": 0, "зелёных": 0, "красных": 0}
    r = subprocess.run(
        ["npx", "jest", "--config", f"{проект}/jest.config.ts", "--testPathPattern", ПРЕФИКС],
        cwd=снимок,
        capture_output=True,
        text=True,
    )
    чисто = re.sub(r"\x1b\[[0-9;]*m", "", r.stderr + r.stdout)
    строка = next((s for s in чисто.splitlines() if s.startswith("Tests:")), "")
    зел = int(m.group(1)) if (m := re.search(r"(\d+) passed", строка)) else 0
    кр = int(m.group(1)) if (m := re.search(r"(\d+) failed", строка)) else 0
    return {"проект": проект, "файлов": файлов, "зелёных": зел, "красных": кр}


def главное() -> int:
    p = argparse.ArgumentParser(description="сплошной прогон проб центрального терминала")
    p.add_argument("--снимок", required=True)
    p.add_argument("--пробы", default="/home/mmber/MetaClaw/evidence/probes")
    p.add_argument("--json")
    a = p.parse_args()
    снимок, источник = pathlib.Path(a.снимок), pathlib.Path(a.пробы)
    if not (снимок / "package.json").exists():
        raise SystemExit(f"снимок не похож на дерево: {снимок}")

    размещено, убрано, нет = разместить(снимок, источник)
    print(f"размещено проб: {размещено} | убрано прежних копий: {убрано}")
    if нет:
        print(f"НЕ РАЗМЕЩЕНЫ ({len(нет)}) — размещение не знает, куда их класть:")
        for n in нет:
            print("   ", n)

    # УБОРКА ОБЯЗАТЕЛЬНА И ПРИ ОТКАЗЕ ПРОГОНА: иначе прибор остаётся внутри измеряемого.
    try:
        строки = [прогнать(снимок, пр) for пр in проекты(снимок)]
    finally:
        снято = убрать(снимок)
        print(f"убрано проб после прогона: {снято} — прибор не остаётся в дереве")
    строки = [s for s in строки if s["файлов"]]
    print(f"\n{'проект':34s} {'файлов':>6} {'зелёных':>8} {'красных':>8}")
    for s in строки:
        print(f"{s['проект']:34s} {s['файлов']:>6} {s['зелёных']:>8} {s['красных']:>8}")
    ф = sum(s["файлов"] for s in строки)
    з = sum(s["зелёных"] for s in строки)
    к = sum(s["красных"] for s in строки)
    print(f"\nИТОГО: файлов {ф} | зелёных {з} | КРАСНЫХ {к}")
    if нет:
        print(f"и ещё {len(нет)} проб НЕ ПРОГНАНЫ — они в число не входят и молчанием не считаются")
    if a.json:
        pathlib.Path(a.json).write_text(
            json.dumps(
                {"проекты": строки, "файлов": ф, "зелёных": з, "красных": к, "не_размещены": нет},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
    # Красная проба — сигнал, а не отказ меры: причина может быть в пробе, а не в дереве.
    return 0


if __name__ == "__main__":
    sys.exit(главное())
