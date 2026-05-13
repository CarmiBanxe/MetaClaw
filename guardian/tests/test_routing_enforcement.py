"""Tests for Sprint 3 routing enforcement rules F9 and F10."""
import pytest
from guardian.src.rules import AuditContext, RuleResult
from guardian.src.rules.factory_rules import FactoryRules


@pytest.fixture
def rules():
    return FactoryRules()


@pytest.fixture
def base_ctx():
    return AuditContext(
        subject_type="prompt",
        subject_id="test-001",
        scope="claude.bash",
        prompt="",
        actor="claude-code",
        diff="",
        branch="feat/test",
    )


class TestF9RouteAliasValidation:
    def test_pass_no_ollama_ref(self, rules, base_ctx):
        base_ctx.prompt = "Use factory-mid for this task"
        result = rules.f9_route_alias_validation(base_ctx)
        assert result.verdict == "PASS"

    def test_warn_direct_ollama_call(self, rules, base_ctx):
        base_ctx.prompt = "ollama:chat:qwen3:30b-a3b directly"
        result = rules.f9_route_alias_validation(base_ctx)
        assert result.verdict == "WARN"
        assert "INV-02" in str(result.reasons)

    def test_pass_canonical_alias_in_ollama_format(self, rules, base_ctx):
        base_ctx.prompt = "using ollama:chat:factory-fast route"
        result = rules.f9_route_alias_validation(base_ctx)
        assert result.verdict == "PASS"


class TestF10RoleActionValidation:
    def test_pass_executor_writing_code(self, rules, base_ctx):
        base_ctx.actor = "aider-cli"
        base_ctx.prompt = "implement the function"
        result = rules.f10_role_action_validation(base_ctx)
        assert result.verdict == "PASS"

    def test_warn_executor_reviewing(self, rules, base_ctx):
        base_ctx.actor = "aider-cli"
        base_ctx.prompt = "review this PR and approve"
        result = rules.f10_role_action_validation(base_ctx)
        assert result.verdict == "WARN"
        assert "INV-01" in str(result.reasons)

    def test_warn_planner_writing_code(self, rules, base_ctx):
        base_ctx.actor = "claude-code"
        base_ctx.scope = "file-edit"
        result = rules.f10_role_action_validation(base_ctx)
        assert result.verdict == "WARN"

    def test_pass_planner_planning(self, rules, base_ctx):
        base_ctx.actor = "claude-code"
        base_ctx.scope = "plan-mode"
        base_ctx.prompt = "create a plan for the feature"
        result = rules.f10_role_action_validation(base_ctx)
        assert result.verdict == "PASS"
