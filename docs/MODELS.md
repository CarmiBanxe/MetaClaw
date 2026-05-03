# BANXE AI Cluster — Model Classification

**Updated:** 2026-05-03 (Sprint P3.8)
**Scope:** all LLMs deployed on evo1 + evo2 + Legion via Ollama / llama.cpp-RPC

---

## Tier 1 — Production-critical

Models the cluster cannot operate without; routed by LiteLLM gateway as defaults for
their respective roles.

| Model | Role | Backend | Host(s) | Notes |
|---|---|---|---|---|
| `qwen3:30b-a3b` | General-purpose default | Ollama (Vulkan) | evo1, evo2 | MoE 30B-A3B; primary default in LiteLLM router. |
| `huihui_ai/glm-4.7-flash-abliterated` | Fast/uncensored chat | Ollama (Vulkan) | evo1 | Used for low-latency assistant flows. |
| `qwen3-coder-next:q4_K_M` | Coding (default) | Ollama (Vulkan) | evo1, evo2 | Continue.dev autocomplete + Aider default. |
| `GLM-4.5-Air` (Q4_K_M, 67.97 GiB) | Large reasoning | llama.cpp + GGML_RPC + GGML_VULKAN | master: evo1; worker: evo2 (USB4 RPC) | Distributed inference path (Sprint S5). |

---

## Tier 2 — Useful

Models actively used for specific workflows but not blocking the cluster if absent.

| Model | Role | Backend | Host(s) | Notes |
|---|---|---|---|---|
| `gurubot/gpt-oss-derestricted:20b` | Unrestricted research | Ollama | evo1 | Used when guard-rails must be off (legal corpus exploration). |
| `qwen3.5:35b` | Aider `ai` command | Ollama | evo1 (present), evo2 (downloading) | Mid-tier reasoning. |
| `llama3.3:70b` | Aider `ai-heavy` command | Ollama | evo1 (downloading), evo2 (downloading) | Long-context reasoning; pull running in nohup. |

---

## Tier 3 — Auxiliary / test

Smoke-test models, kept for benchmarks and local sanity checks.

| Model | Role | Backend | Host(s) |
|---|---|---|---|
| `qwen3:4b` | Tiny smoke test | Ollama | evo1, evo2 |
| `qwen3.5:latest` (~6B, 6.6 GiB) | Lightweight chat | Ollama | evo2 |

---

## Pending downloads (in flight 2026-05-03)

| Model | Host | Status |
|---|---|---|
| `qwen3.5:35b` | evo2 | nohup pull in progress |
| `llama3.3:70b` | evo1 | nohup pull in progress |
| `llama3.3:70b` | evo2 | nohup pull in progress |

These pulls are tracked by `pgrep -fa "ollama.*pull"` on each node. Do **not** restart
ollama or kill the parent shell while these are running.

---

## Routing summary (LiteLLM gateway)

- `default` → `qwen3:30b-a3b`
- `fast` → `huihui_ai/glm-4.7-flash-abliterated`
- `code` → `qwen3-coder-next:q4_K_M`
- `reason-large` → GLM-4.5-Air via RPC master (evo1)
- `aider/ai` → `qwen3.5:35b`
- `aider/ai-heavy` → `llama3.3:70b`
- `unrestricted` → `gurubot/gpt-oss-derestricted:20b`
