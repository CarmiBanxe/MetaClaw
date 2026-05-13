"""Memory pull contract per ADR-020.

Loads all memory artefacts that any Guardian audit MUST consult before rule checks.
Cache TTL: 60s (mitigates per-audit IO cost noted in ADR-020 §Consequences).
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

HOME = Path.home()
ARCH = HOME / "banxe-architecture"
EMI_STACK_ADR = HOME / "banxe-emi-stack" / "docs" / "adr"
METACLAW_ROADMAP = HOME / "MetaClaw" / "docs" / "roadmap"
PASSPORTS_DIR = ARCH / "docs" / "canon" / "passports"

CACHE_TTL_SECONDS = 60.0


@dataclass
class MemorySnapshot:
    memory: str = ""
    ledger: str = ""
    gap_register: str = ""
    canon: str = ""
    hitl: str = ""
    passports: dict = field(default_factory=dict)
    constitution: str = ""
    adrs: list[str] = field(default_factory=list)
    roadmap: str = ""

    def as_dict(self) -> dict[str, str | list[str]]:
        return {
            "memory": self.memory,
            "ledger": self.ledger,
            "gap_register": self.gap_register,
            "canon": self.canon,
            "hitl": self.hitl,
            "constitution": self.constitution,
            "adrs": self.adrs,
            "roadmap": self.roadmap,
        }


class MemoryLoader:
    def __init__(self) -> None:
        self._cache: MemorySnapshot | None = None
        self._cache_ts: float = 0.0

    def load_all(self, force: bool = False) -> dict[str, str | list[str]]:
        if not force and self._cache and (time.time() - self._cache_ts) < CACHE_TTL_SECONDS:
            return self._cache.as_dict()

        snap = MemorySnapshot(
            memory=self._read(ARCH / "MEMORY.md"),
            ledger=self._read(ARCH / "INSTRUCTION-LEDGER.md"),
            gap_register=self._read(ARCH / "GAP-REGISTER.md"),
            canon=self._read(ARCH / "PROMPT-CANON-PROJECT.md"),
            hitl=self._read(ARCH / "HITL-MATRIX.yaml"),
            passports=self._load_passports(),
            constitution=self._collect_constitution(),
            adrs=self._collect_adrs(),
            roadmap=self._collect_roadmap(),
        )
        self._cache = snap
        self._cache_ts = time.time()
        return snap.as_dict()

    @staticmethod

    def _load_passports(self) -> dict:
        """Load all YAML passports from docs/canon/passports/."""
        import yaml
        result = {}
        if PASSPORTS_DIR.is_dir():
            for f in sorted(PASSPORTS_DIR.glob("*.yaml")):
                if f.name == "schema.yaml":
                    continue
                try:
                    data = yaml.safe_load(f.read_text())
                    if data and "role_id" in data:
                        result[data["role_id"]] = data
                except Exception as e:
                    logger.warning("Failed to load passport %s: %s", f.name, e)
        return result

    def _read(path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8")
        except FileNotFoundError:
            logger.warning("memory file missing: %s", path)
            return ""
        except OSError as exc:
            logger.warning("memory file unreadable %s: %s", path, exc)
            return ""

    def _collect_constitution(self) -> str:
        parts: list[str] = []
        readme = ARCH / "constitution" / "README.md"
        if readme.exists():
            parts.append(f"# {readme}\n{self._read(readme)}")
        amend_dir = ARCH / "constitution" / "amendments"
        if amend_dir.is_dir():
            for f in sorted(amend_dir.glob("*.md")):
                parts.append(f"# {f}\n{self._read(f)}")
        if not parts:
            logger.warning("constitution corpus empty")
        return "\n\n".join(parts)

    def _collect_adrs(self) -> list[str]:
        files: list[Path] = []
        for d in (ARCH / "decisions", ARCH / "adrs", EMI_STACK_ADR):
            if d.is_dir():
                files.extend(sorted(d.glob("*.md")))
        if not files:
            logger.warning("no ADR files discovered across 3 catalogues")
        return [f.read_text(encoding="utf-8") for f in files]

    def _collect_roadmap(self) -> str:
        parts: list[str] = []
        if METACLAW_ROADMAP.is_dir():
            for f in sorted(METACLAW_ROADMAP.glob("banxe-cluster-v*.md")):
                parts.append(f"# {f}\n{self._read(f)}")
        matrix = ARCH / "docs" / "ROADMAP-MATRIX.md"
        if matrix.exists():
            parts.append(f"# {matrix}\n{self._read(matrix)}")
        if not parts:
            logger.warning("roadmap corpus empty")
        return "\n\n".join(parts)
