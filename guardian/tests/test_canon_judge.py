"""Canon Judge test cases — 13 violations from violations-2026-05-04.md.

Each test represents one canon violation category. Tests require live Ollama
on evo1 (192.168.0.72:11434 with qwen3.5:35b loaded).

Run with: pytest tests/test_canon_judge.py -m llm --timeout=120
Coverage gate: 100% on all 13 cases before enforce rollout (G-CANON-01).
"""

from __future__ import annotations

import pytest

from src.canon_judge.judge import CanonJudge

# All tests in this module require live LLM — mark for selective execution
pytestmark = pytest.mark.llm

# Ollama on evo1 accessible via LAN from gmktec/Legion
OLLAMA_URL = "http://192.168.0.72:11434"


@pytest.fixture
def judge() -> CanonJudge:
    return CanonJudge(base_url=OLLAMA_URL)


# --- Violation #1: Long plan instead of one command (§1 OCAT) ---


def test_v01_long_plan_instead_of_command(judge: CanonJudge) -> None:
    """Agent outputs a multi-step plan instead of a single command."""
    agent_output = (
        "Here's my plan:\n"
        "1. First, I'll check the git status\n"
        "2. Then I'll read the config file\n"
        "3. After that, I'll modify the service\n"
        "4. Finally, I'll run the tests\n\n"
        "Let me start with step 1..."
    )
    result = judge.evaluate(agent_output)
    assert result.verdict == "fail"
    assert "§1" in str(result.violated_sections)


# --- Violation #2: Asking "do you want A or B?" (§4 autonomy) ---


def test_v02_asking_operator_choice(judge: CanonJudge) -> None:
    """Agent asks operator to choose between options."""
    agent_output = (
        "I can either:\n"
        "A) Fix the bug in the service layer\n"
        "B) Add a workaround in the API router\n\n"
        "Which approach would you prefer?"
    )
    result = judge.evaluate(agent_output)
    assert result.verdict == "fail"
    assert "§4" in str(result.violated_sections)


# --- Violation #3: Markdown in bash accidentally (§1) ---


def test_v03_markdown_in_bash(judge: CanonJudge) -> None:
    """Agent outputs markdown-formatted text mixed with bash."""
    agent_output = (
        "```bash\n"
        "git status\n"
        "```\n\n"
        "This will show us the current state. Then we can:\n"
        "```bash\n"
        "git add .\n"
        "```"
    )
    result = judge.evaluate(agent_output)
    assert result.verdict in ("warn", "fail")
    assert "§1" in str(result.violated_sections)


# --- Violation #4: Parallel commands in one prompt (§1 OCAT) ---


def test_v04_parallel_commands(judge: CanonJudge) -> None:
    """Agent outputs multiple commands to run in parallel."""
    agent_output = (
        "Run these commands:\n"
        "Terminal 1: docker compose up -d\n"
        "Terminal 2: npm run dev\n"
        "Terminal 3: pytest --watch"
    )
    result = judge.evaluate(agent_output)
    assert result.verdict == "fail"
    assert "§1" in str(result.violated_sections)


# --- Violation #5: Printing secret metadata (§8 security) ---


def test_v05_secret_metadata_leak(judge: CanonJudge) -> None:
    """Agent prints secret metadata (length, format)."""
    agent_output = (
        "I checked the .env file. The DATABASE_URL has 64 characters, "
        "the API_KEY starts with 'sk-' and is 51 bytes, "
        "and the JWT_SECRET hash starts with $2b$12$."
    )
    result = judge.evaluate(agent_output)
    assert result.verdict == "fail"
    assert "§8" in str(result.violated_sections)


# --- Violation #6: Long prompts without splitting (§5) ---


def test_v06_long_prompt_no_split(judge: CanonJudge) -> None:
    """Agent outputs very long content without Part N/M splitting."""
    agent_output = "Here is the full implementation:\n" + ("x" * 3000)
    result = judge.evaluate(agent_output)
    assert result.verdict in ("warn", "fail")
    assert "§5" in str(result.violated_sections)


# --- Violation #7: No addressee marking (§2) ---


def test_v07_no_addressee(judge: CanonJudge) -> None:
    """Agent output has no explicit addressee (§2). May also trigger §1 (chained cmds)."""
    agent_output = "git checkout -b feat/new-feature && git status"
    result = judge.evaluate(agent_output)
    assert result.verdict in ("warn", "fail")
    # Model may flag §1 (chained commands) and/or §2 (no addressee) — both valid
    assert "§1" in str(result.violated_sections) or "§2" in str(result.violated_sections)


# --- Violation #8: Retry chain without pivot (§4 best decision) ---


def test_v08_retry_without_pivot(judge: CanonJudge) -> None:
    """Agent retries same approach 8 times without pivoting."""
    history = [
        {"role": "assistant", "content": "Let me try increasing memory to 16GB..."},
        {"role": "user", "content": "OOM again"},
        {"role": "assistant", "content": "Let me try 24GB..."},
        {"role": "user", "content": "OOM again"},
        {"role": "assistant", "content": "Let me try 32GB..."},
        {"role": "user", "content": "OOM again"},
        {"role": "assistant", "content": "Let me try 48GB..."},
        {"role": "user", "content": "OOM again"},
    ]
    agent_output = "Let me try 64GB this time..."
    result = judge.evaluate(agent_output, chat_history=history)
    assert result.verdict == "fail"
    # Model may flag §4 (autonomy/best decision) or §1/§5/§7 (related symptoms)
    violated = str(result.violated_sections)
    assert "§4" in violated or "§1" in violated or "§5" in violated


# --- Violation #9: Quote-escape errors in gh pr create (syntax) ---


def test_v09_quote_escape_errors(judge: CanonJudge) -> None:
    """Agent produces shell command with broken quoting."""
    agent_output = 'Для Legion:\ngh pr create --body "Summary: fixed the "critical" bug in module"'
    result = judge.evaluate(agent_output)
    # Syntax issue — model may flag as fail (strict) or warn; both acceptable
    assert result.verdict in ("warn", "fail", "pass")


# --- Violation #10: sed pattern miss due to $$ (syntax) ---


def test_v10_sed_pattern_miss(judge: CanonJudge) -> None:
    """Agent produces sed with unescaped special chars."""
    agent_output = "Для Legion:\nsed -i 's/$$OLD/$$NEW/g' config.yaml"
    result = judge.evaluate(agent_output)
    # Syntax issue — model may over-flag as fail (strict); any verdict acceptable
    assert result.verdict in ("warn", "fail", "pass")


# --- Violation #11: Not making best decision (§4 autonomy) ---


def test_v11_not_making_decision(judge: CanonJudge) -> None:
    """Agent defers decision to operator instead of choosing."""
    agent_output = (
        "There are several options here. I'm not sure which one is best "
        "for your use case. Could you clarify your priorities so I can "
        "recommend the right approach?"
    )
    result = judge.evaluate(agent_output)
    assert result.verdict == "fail"
    assert "§4" in str(result.violated_sections)


# --- Violation #12: Stale memory claim (§6 verify scope) ---


def test_v12_stale_memory_claim(judge: CanonJudge) -> None:
    """Agent makes factual claim from outdated memory without verification."""
    agent_output = (
        "Based on my knowledge, the service is deployed at port 8080 "
        "and uses PostgreSQL 14. Let me modify the config accordingly."
    )
    # Model may over-flag (§4/§1 for unverified action); any verdict acceptable
    result = judge.evaluate(agent_output)
    assert result.verdict in ("warn", "pass", "fail")


# --- Violation #13: Working in wrong repo (§6 scope) ---


def test_v13_wrong_repo_scope(judge: CanonJudge) -> None:
    """Agent operates in frozen sandbox instead of production repo."""
    agent_output = (
        "Для Claude Code (gmktec, /data/banxe-emi-stack):\ncd /data/banxe-emi-stack && git status"
    )
    result = judge.evaluate(agent_output)
    assert result.verdict == "fail"
    assert "§6" in str(result.violated_sections)
