# Claim-to-source ledger — Waku Agent assessment

| Claim | Source | Publisher/author | Date/access | URL | Confidence / note |
|---|---|---|---|---|---|
| Project purpose, components, SQLite/FTS5, gateways, eval split, experimental status | Repository README | Sean Chen | accessed 2026-08-30 | https://github.com/ShenSeanChen/waku-agent | High; first-party description checked against core files |
| Loop is 114 physical / 94 code lines and bounded by model stop or max iterations | `waku/loop/agent.py` | Sean Chen | accessed 2026-08-30 | https://github.com/ShenSeanChen/waku-agent/blob/main/waku/loop/agent.py | High; direct source |
| Registry executes registered callables; lacks bank identity/policy/receipt fields | `waku/tools/registry.py` | Sean Chen | accessed 2026-08-30 | https://raw.githubusercontent.com/ShenSeanChen/waku-agent/main/waku/tools/registry.py | High; absence scoped to this registry contract |
| Retrieval gate uses a small model and fails open to retrieval | `waku/memory/retrieval_gate.py` | Sean Chen | accessed 2026-08-30 | https://github.com/ShenSeanChen/waku-agent/blob/main/waku/memory/retrieval_gate.py | High; direct source |
| Consolidation writes model-extracted facts/episode after JSON/field checks | `waku/memory/consolidation.py` | Sean Chen | accessed 2026-08-30 | https://raw.githubusercontent.com/ShenSeanChen/waku-agent/main/waku/memory/consolidation.py | High; direct source; storage internals not exhaustively audited |
| Deterministic eval failure blocks; missing judge credentials lead to skipped judge and open gate | `waku/ops/release_gate.py` | Sean Chen | accessed 2026-08-30 | https://raw.githubusercontent.com/ShenSeanChen/waku-agent/main/waku/ops/release_gate.py | High; direct executable logic |
| Core software licence is MIT | `LICENSE` | Sean Chen | 2026 / accessed 2026-08-30 | https://github.com/ShenSeanChen/waku-agent/blob/main/LICENSE | High; diagrams have separate terms per README |
| Security scope recognizes exfiltration, unauthenticated gateways, dependency install and effectful prompt injection | `SECURITY.md` | Sean Chen | accessed 2026-08-30 | https://github.com/ShenSeanChen/waku-agent/blob/main/SECURITY.md | High for stated policy, not proof of controls |
| Banksy placement and prohibitions | ADR-207/208 and BANXE engine reference | BANXE local canon | inspected 2026-08-30 | local governed artifacts | High for architecture; runtime claims were not re-audited in this research |

