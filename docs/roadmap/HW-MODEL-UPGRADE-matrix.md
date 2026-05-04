# BANXE Hardware × Model Upgrade Matrix
Last updated: 2026-05-03 · Source of truth for: hardware tiers, deployed models, upgrade triggers, expected throughput deltas.

## 1. Hardware tiers
| Node | CPU | RAM | iGPU/dGPU | NPU | Storage | Role |
|---|---|---|---|---|---|---|
| Legion (mark-legion, 192.168.0.75 NAT, Tailscale 100.101.218.26) | i9-14900HX (28 vCPU) | 64 GiB DDR5 | RTX 4070 Laptop 8 GiB | — | C:952 GiB + D:3.7 TiB | LiteLLM v2 gateway, factory ops, Claude Code, Aider client |
| EVO-X2 #1 (evo1, banxe-NucBox-EVO-X2, 192.168.0.72) | Ryzen AI Max+ 395 (32T) | 128 GiB LPDDR5X (BIOS UMA: 96 iGPU / 32 CPU) | Radeon 8060S 40 CU (gfx1151) | XDNA 2 NPU — 50 TOPS (system AI total ~126 TOPS incl. iGPU+CPU) | nvme1 931G (/) + nvme0 1.9T (/data) | Prod Ollama, llama.cpp glm-master :8081, banxe-compliance-api :8194, deep-search :8088, banxe-api :8093, prometheus-node-exporter :9100 |
| EVO-X2 #2 (evo2, banxe-NucBox-EVO-X2-2, 192.168.0.15) | Ryzen AI Max+ 395 (32T) | 128 GiB LPDDR5X (BIOS UMA: 64 iGPU / 64 CPU) | Radeon 8060S 40 CU (gfx1151) | XDNA 2 NPU — 50 TOPS (system AI total ~126 TOPS incl. iGPU+CPU) | nvme0 1.9T | Prod Ollama, llama.cpp RPC worker :50052, monitoring stack (prometheus :9090, grafana :3000, blackbox :9115), node_exporter :9100 |

USB4 RPC link: 10.0.0.1/30 ↔ 10.0.0.2/30, 9.12 Gbit/s, 0.49 ms RTT.

## 2. Deployed models per node (from `ollama list` 2026-05-03)

### evo1 (8 models, ~176 GiB)
```
NAME                                          ID              SIZE      MODIFIED
llama3.3:70b                                  a6eb4748fd29    42 GB     14 hours ago
qwen3.5:35b                                   3460ffeede54    23 GB     16 hours ago
qwen3:4b                                      359d7dd4bcda    2.5 GB    2 weeks ago
qwen3:30b-a3b                                 ad815644918f    18 GB     2 weeks ago
qwen3.5:latest                                6488c96fa5fa    6.6 GB    2 weeks ago
qwen3-coder-next:q4_K_M                       ca06e9e4087c    51 GB     2 weeks ago
gurubot/gpt-oss-derestricted:20b              d64366c49522    15 GB     5 weeks ago
huihui_ai/glm-4.7-flash-abliterated:latest    998f411fc8eb    18 GB     5 weeks ago
```

### evo2 (10 models, ~460 GiB)
```
NAME                                          ID              SIZE      MODIFIED
qwen3:235b-a22b-banxe                         3161844859cd    142 GB    3 hours ago
qwen3:235b-a22b                               754a872f1290    142 GB    9 hours ago
llama3.3:70b                                  a6eb4748fd29    42 GB     14 hours ago
qwen3.5:35b                                   3460ffeede54    23 GB     15 hours ago
qwen3:4b                                      359d7dd4bcda    2.5 GB    2 weeks ago
qwen3:30b-a3b                                 ad815644918f    18 GB     2 weeks ago
qwen3.5:latest                                6488c96fa5fa    6.6 GB    2 weeks ago
qwen3-coder-next:q4_K_M                       ca06e9e4087c    51 GB     2 weeks ago
huihui_ai/glm-4.7-flash-abliterated:latest    998f411fc8eb    18 GB     5 weeks ago
gurubot/gpt-oss-derestricted:20b              d64366c49522    15 GB     5 weeks ago
```

Plus llama.cpp distributed (glm-master on evo1):
- GLM-4.5-Air-Q4_K_M-00001-of-00002.gguf 47 GiB + 00002-of-00002.gguf 22 GiB (total ~73 GiB) → 110.5 B params, 21.4 tok/s gen via USB4 RPC.

## 3. Active aliases in LiteLLM v2 (legion:4000)
- ai = qwen3.5:35b LB (evo1+evo2)
- ai-heavy = llama3.3:70b LB (evo1+evo2)
- reasoning = llama3.3:70b LB (evo1+evo2) — degraded; qwen3:235b-a22b BLOCKED on UMA
- banxe-general / qwen3-30b / qwen3-banxe = qwen3:30b-a3b
- fast / glm-4-flash = glm-4.7-flash-abliterated (LB)
- coding = qwen3-coder-next:q4_K_M (evo1)
- gpt-oss-20b = gurubot/gpt-oss-derestricted:20b (evo1)
- large / glm-air / glm-4.5-air-distributed = GLM-4.5-Air via llama.cpp on evo1:8081

## 4. Model upgrade triggers (carryover)
| Model | Status | Blocker | Resolves with | Deadline / Trigger |
|---|---|---|---|---|
| qwen3:235b-a22b | DOWNLOADED 142 GiB on evo2 | requires 134 GiB system memory > 64 GiB CPU on evo2 | P4.3 BIOS UMA rebalance evo2 (96 CPU / 32 iGPU) OR llama.cpp RPC like glm-master | post FCA CASS 15 (after 7 May 2026) |
| qwen3:235b-a22b-banxe | DOWNLOADED 142 GiB on evo2 (variant, 3h old) | same UMA blocker | same as above | same |
| GLM-4.5-Air | LIVE 21.4 tok/s gen | none | active baseline | — |
| llama3.3:70b LB | LIVE | none | active reasoning fallback | — |
| qwen3.5:35b LB | LIVE | none | active ai alias | — |
| qwen3-coder-next:q4_K_M | LIVE on evo1 | none | active coding alias | — |
| qwen3:30b-a3b LB | LIVE | none | active general alias | — |
| glm-4.7-flash-abliterated LB | LIVE | none | active fast alias | — |
| gpt-oss-derestricted:20b | LIVE on evo1 | none | active | — |
| qwen3:4b | LIVE | none | low-latency utility | — |
| qwen3.5:latest | LIVE | none | small utility | — |
| Qwen2.5-Coder-14B-Instruct (Legion) | LIVE local | none | Legion-side coding context | — |

## 5. Hardware upgrade path (from §15 Phase 4 backlog)
| Item | Action | Expected delta | Trigger | Risk |
|---|---|---|---|---|
| P4.2 ROCm 6.4 migration | Replace Vulkan path on both evo nodes | +30-50% throughput on gfx1151 | post FCA CASS 15 (≥ 8 May 2026) | medium — может потребоваться kernel/firmware update |
| P4.3 BIOS UMA evo2 rebalance | 64/64 → 96 iGPU / 32 CPU split (consistent with evo1) | НЕ для qwen3:235b-a22b unblock (тот наоборот хочет CPU‑side, см. note) | manual BIOS step + reboot | low |
| P4.3-alt BIOS UMA evo2 rebalance (alt) | 64/64 → 32 iGPU / 96 CPU | unlock qwen3:235b-a22b (134 GiB needs CPU side) | manual BIOS step + reboot, ~15 min | low |
| P4.4 XDNA 2 NPU | Enable ~100 TOPS aggregate NPU (50 per node × 2) via AMD Ryzen AI SDK + onnxruntime-vitis-ai | sub-10W inference path для small models | research sprint, 4h | high — SDK мало‑известен |
| USB4 RPC link | Already up (10.0.0.1/30 ↔ 10.0.0.2/30, 9.12 Gbit/s, 0.49 ms RTT) | distributed inference enabled | DONE (Phase 3 S5) | — |
| qwen3:235b-a22b via llama.cpp RPC | Skip Ollama, use llama-server master/worker like glm-master | unblock БЕЗ BIOS rebalance | required GGUF conversion (~2-3h) | medium — separate model artifact |

## 6. Cross-link к плоскостям
- Factory: см. INDEX.md §1.2.
- Project (FCA CASS 15 + EMI): см. INDEX.md §1.1 → ~/banxe-architecture/docs/ROADMAP-MATRIX.md.
- Cluster carryover: см. ~/MetaClaw/docs/roadmap/banxe-cluster-v2.3-phaseN.md §FINAL.
- Связанные ADRs: ADR-016 (AI plane PII/AML routing) и ADR-021 (banxe-emi-stack ai-plane-pii-aml-routing).

## 7. Throughput KPIs (baseline 2026-05-03)
- GLM-4.5-Air distributed (evo1+evo2 RPC): prompt 32.5 tok/s, gen 21.4 tok/s (50‑token bench).
- llama3.3:70b LB cold load: ~1m 13s first request, sub-second warm.
- qwen3.5:35b LB warm: 5-10 s on 100‑token completion.
- LiteLLM v2 :4000 overhead: ~20-40 ms (router+retry config).

## 8. Canonical target architecture (5-layer hybrid) — LOCKED 2026-05-03T18:29:18+02:00

Per ADR-018 (banxe-architecture/decisions/ADR-018-hybrid-5-layer-ai-compute.md):

| Layer | Scope | Hardware | Throughput target |
|---|---|---|---|
| 1 — Reasoning | 70B–235B via llama.cpp RPC | evo1 master + evo2 worker (USB4) | 5–25 t/s gen |
| 2 — Mid-size | 10B–70B Ollama LB | evo1 + evo2 iGPU | 15–35 t/s gen |
| 3 — Small specialized | ≤7B via XDNA 2 NPU | evo1 + evo2 NPU (~100 TOPS aggregate, 50 per node) | sub-10ms latency |
| 4 — Cloud meta | PR review, scaffolding | Claude Code (cloud), deny_paths enforced | ~1 s |
| 5 — Routing | All traffic | LiteLLM v2 :4000 (Legion systemd) | <40 ms overhead |

### BIOS UMA (asymmetric, canonical)
- **evo1**: 96 GiB iGPU / 32 GiB CPU (AI heavy).
- **evo2**: 32 GiB iGPU / 96 GiB CPU (CPU + DB heavy).

### Required sprints to reach 100%
1. **P4.3-evo2** — BIOS rebalance evo2 to 32/96 (15 min + reboot).
2. **P4.3-Q235** — convert qwen3:235b-a22b to Q4_K_M GGUF, second llama.cpp RPC master :8082 (~3-4 h).
3. **P4.4-NPU** — AMD Ryzen AI SDK install on both evo nodes, deploy 2-3 small ONNX models, wire LiteLLM aliases (~4 h research + setup).
4. **P4.2-ROCm** (optional) — Ollama Vulkan → ROCm 6.4, +30-50% throughput (~2 h).

### Reusability
Canonical target reusable for any future project (regtech, AI products, personal R&D). Models swap, Layers stay.
