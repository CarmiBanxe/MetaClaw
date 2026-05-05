"""Tests for claude.bash scope rules — ADR-025 canon violations (bash subset)."""

from __future__ import annotations

import pytest

from src.rules import AuditContext
from src.rules.claude_bash_rules import ClaudeBashRules


@pytest.fixture
def rules() -> ClaudeBashRules:
    return ClaudeBashRules()


# --- §10 deny-paths (CB1) ---


def test_cb1_block_env_file(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="cat /home/user/project/.env.production")
    results = rules.evaluate_all(ctx, {})
    r1 = next(r for r in results if r.rule_id == "CB1-deny-path")
    assert r1.status == "BLOCK"


def test_cb1_block_secrets_dir(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="ls secrets/keycloak-admin.json")
    results = rules.evaluate_all(ctx, {})
    r1 = next(r for r in results if r.rule_id == "CB1-deny-path")
    assert r1.status == "BLOCK"


def test_cb1_block_pem(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="cat /etc/ssl/private/server.pem")
    results = rules.evaluate_all(ctx, {})
    r1 = next(r for r in results if r.rule_id == "CB1-deny-path")
    assert r1.status == "BLOCK"


def test_cb1_pass_safe_path(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="cat README.md")
    results = rules.evaluate_all(ctx, {})
    r1 = next(r for r in results if r.rule_id == "CB1-deny-path")
    assert r1.status == "PASS"


# --- §8 secret leak (CB2) ---


def test_cb2_block_cat_env(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="cat .env")
    results = rules.evaluate_all(ctx, {})
    r2 = next(r for r in results if r.rule_id == "CB2-secret-leak")
    assert r2.status == "BLOCK"


def test_cb2_block_printenv(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="printenv | head")
    results = rules.evaluate_all(ctx, {})
    r2 = next(r for r in results if r.rule_id == "CB2-secret-leak")
    assert r2.status == "BLOCK"


def test_cb2_pass_normal_cmd(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="git status -sb")
    results = rules.evaluate_all(ctx, {})
    r2 = next(r for r in results if r.rule_id == "CB2-secret-leak")
    assert r2.status == "PASS"


# --- §6 frozen sandbox (CB3) ---


def test_cb3_warn_frozen_sandbox(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="cd /data/banxe-emi-stack && git log")
    results = rules.evaluate_all(ctx, {})
    r3 = next(r for r in results if r.rule_id == "CB3-frozen-sandbox")
    assert r3.status == "WARN"


def test_cb3_pass_production_repo(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="cd /home/mmber/banxe-emi-stack && git log")
    results = rules.evaluate_all(ctx, {})
    r3 = next(r for r in results if r.rule_id == "CB3-frozen-sandbox")
    assert r3.status == "PASS"


# --- dangerous commands (CB4) ---


def test_cb4_block_rm_rf_root(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="rm -rf /var/data")
    results = rules.evaluate_all(ctx, {})
    r4 = next(r for r in results if r.rule_id == "CB4-dangerous-cmd")
    assert r4.status == "BLOCK"


def test_cb4_block_force_push(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="git push --force origin main")
    results = rules.evaluate_all(ctx, {})
    r4 = next(r for r in results if r.rule_id == "CB4-dangerous-cmd")
    assert r4.status == "BLOCK"


def test_cb4_pass_safe_git(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="git push origin feat/new-branch")
    results = rules.evaluate_all(ctx, {})
    r4 = next(r for r in results if r.rule_id == "CB4-dangerous-cmd")
    assert r4.status == "PASS"


# --- integration: full evaluate_all returns 4 results ---


def test_evaluate_all_returns_four_results(rules: ClaudeBashRules) -> None:
    ctx = AuditContext(prompt="echo hello")
    results = rules.evaluate_all(ctx, {})
    assert len(results) == 4
    assert all(r.status == "PASS" for r in results)
