"""
MetaClaw — OpenClaw skill injection and RL training, one-click deployment.

Integrates:
  - OpenClaw online dialogue data collection (FastAPI proxy)
  - Skill injection and auto-summarization (skills_only mode)
  - Tinker-compatible cloud LoRA RL training (rl mode, optional)

Quick start:
    metaclaw setup    # configure LLM, skills, RL toggle
    metaclaw start    # one-click launch
"""

from .api_server import MetaClawAPIServer
from .config import MetaClawConfig
from .config_store import ConfigStore
from .launcher import MetaClawLauncher
from .prm_scorer import PRMScorer
from .rollout import AsyncRolloutWorker
from .skill_evolver import SkillEvolver
from .skill_manager import SkillManager

# RL-only imports (guarded to avoid hard dep on torch/backend SDKs in skills_only mode)
try:
    from .data_formatter import ConversationSample, batch_to_datums, compute_advantages  # noqa: F401
    from .trainer import MetaClawTrainer  # noqa: F401
except ImportError:
    pass

__all__ = [
    "MetaClawConfig",
    "ConfigStore",
    "MetaClawAPIServer",
    "AsyncRolloutWorker",
    "PRMScorer",
    "SkillManager",
    "SkillEvolver",
    "MetaClawLauncher",
]
