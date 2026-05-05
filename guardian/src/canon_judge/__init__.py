"""Canon Judge — conversation-level canon enforcement (G-CANON-01).

Evaluates AI agent output against 14 sections of the Agent Interaction Canon
(ADR-025) using a local LLM judge (glm-air or qwen3.5:35b via LiteLLM).
"""

from .judge import CanonJudge, JudgeVerdict

__all__ = ["CanonJudge", "JudgeVerdict"]
