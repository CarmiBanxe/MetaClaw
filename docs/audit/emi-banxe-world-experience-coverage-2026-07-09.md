# EMI BANXE World-Experience — Coverage (BEN / CENTRAL)
Date: 2026-07-09
Provenance:
- Source: docs/sources/emi-banxe-world-experience-2026-07-09.md
  sha256: 08aff49982f7e7ba... (cp+sha zero-loss, R8 BEST)
Method: marker + code-context-verify over ROOTS (banxe-emi-stack, banxe-ai-infrastructure, MetaClaw),
excluding docs/rules/prompts/md/json/tests. Numbers = code-matches after context-verify, not feature counts.

## GROUP F — Compliance

### F1 — PSD2 / SCA
- Маркеры: PSD2, SCA, dynamic.linking, Art.97, RTS.
- Статус: IMPLEMENTED (135 code-matches).
- Доказательство: api/main.py (/v1/auth/sca/challenge, /sca/verify, /token/refresh); api/deps.py
  (SCAService, get_sca_service_di); open_banking + psd2_gateway routers (IL-OBK-01/PSD2GW-01);
  clickhouse_payments.sql (FCA PSR/PSD2/I-24 append-only).
- Рекомендация: привязать к I-24; новых задач не заводить.

### F2 — GDPR
- Маркеры: GDPR, consent, erasure, Art.(5|6|30).
- Статус: IMPLEMENTED (78 code-matches).
- Доказательство: user_preferences.py (consent-withdrawal + erasure -> HITL I-27, data-export);
  statements.py (UK GDPR Art.5, I-09); iam_port.py (access-restriction); gateway.py (Art.30 audit log);
  notification_port.py (Art.6 lawful-basis).
- Рекомендация: привязать к I-27/I-09; новых задач нет.

### F3 — HITL / approval gate
- Маркеры: HITL, hitl_threshold, human.in.the.loop, approval.
- Статус: IMPLEMENTED (557 code-matches).
- Доказательство: intent_dispatcher/dispatcher.py (I-27 "AI proposes, human decides", L2+ -> HITLProposal,
  никогда прямой bus.send, I-24); a2a_bus/chain_registry.py (L3 MLRO gate, risk_score>0.4, L4 SAR human-only);
  intent_dispatcher/models.py (hitl_threshold/hitl_proposal).
- Рекомендация: привязать к I-27; новых задач нет.

### F4 — Audit trail / lineage
- Маркеры: audit.trail, lineage, AuditEvent, correlation_id.
- Статус: IMPLEMENTED (172 code-matches).
- Доказательство: src.safeguarding.audit_trail (AuditTrail/AuditEvent); api/routers/intent.py (ADR-046 lineage,
  GET /v1/intent/decision/{correlation_id}, services.agents._lineage); transaction_monitor.py
  (alert.audit_trail.append); experiments.py (AuditEntry).
- Рекомендация: привязать к I-24/ADR-046. Оговорка: backlog #2/#7 держат lineage PARTIAL (полнота
  ClickHouse-записи / hash-chain) — не противоречие: контур IMPLEMENTED, полнота — отдельный пункт, не дублировать.

### F5 — EU AI Act (Art.12-17)
- Маркеры: EU AI Act, Art.1[2-7], Annex IV, high-risk.
- Статус: PARTIAL (84 code-matches, но в основном на high-risk risk-scoring, не на статьях).
- Доказательство: clickhouse_customers.sql (high-risk view, MLRO); sanctions_rescreen.py + api/main.py
  (/compliance/sanctions/rescreen/high-risk, IL-068). Явной имплементации Art.12-17 / Annex IV в коде нет.
- Рекомендация: NON-GATED compliance — рассмотреть явную имплементацию Art.12-17 (logging/transparency/
  human-oversight docs) отдельным backlog-пунктом; привязать к #1 (SHAP/LIME Art.15) и lineage #2/#7, без
  дублирования. Sanctions/high-risk = детект/эскалация, НЕ рекомендация к автономному кредит/платёж действию
  (B-EMI-CREDIT-GATE-001).

Summary F: IMPLEMENTED=4 PARTIAL=1 MISSING=0 GATED=0

## GROUP B — LLM-orchestration

### B1 — LangGraph / StateGraph
- Маркеры: LangGraph, StateGraph, GraphExecutor, graph.run.
- Статус: MISSING (planned P1 only, 3 файла — все планирующие комментарии).
- Доказательство: intent_dispatcher/adapters/logging_adapter.py, adapters/port.py,
  services/intent_dispatcher/app.py — текст "P1 will add CrewAI / LangGraph adapters ... DO NOT add them here".
  Кода нет.
- Рекомендация: NON-GATED, reliability — реализовать LangGraph-adapter за существующим adapter-port; привязать
  к P1-плану в port.py, не заводить дубль.

### B2 — LangSmith / LangChain
- Маркеры: LangSmith, LangChain.
- Статус: MISSING (0 файлов).
- Рекомендация: optional — рассматривать только если выбирается LangGraph-стек (B1). Не приоритет.

### B3 — DSPy
- Маркеры: DSPy, Teleprompter, dspy.Signature.
- Статус: MISSING — "49" файлов = FALSE POSITIVE (слово signature в services/ledger/production/paybis_* =
  webhook signature-verification, не DSPy Signature). Отсеян.
- Рекомендация: NON-GATED, low priority.

### B4 — LiteLLM
- Маркеры: LiteLLM, litellm, litellm_prod.
- Статус: PARTIAL (15 файлов — инфра/observability, не code-level lib).
- Доказательство: banxe-monitoring/prometheus/prometheus.yml (job litellm_prod, /metrics scrape);
  prometheus/rules/targets.yml (alert LiteLLMGatewayDown); deploy/docker-compose.yml (litellm gateway).
- Рекомендация: зафиксировать как принятый gateway (инфра IMPLEMENTED); code-level usage — по мере необходимости.

### B5 — Bedrock
- Маркеры: Bedrock, BedrockChatClient, bedrock_region.
- Статус: IMPLEMENTED (9 файлов, реальный код).
- Доказательство: MetaClaw/scripts/run_v03_benchmark.py (PRM scoring + skill-evolution via Bedrock Sonnet 4.6,
  prm_provider="bedrock", evolver_provider="bedrock", bedrock_region); metaclaw.bedrock_client.BedrockChatClient.
- Рекомендация: зафиксировать как основной LLM-провайдер MetaClaw benchmark/PRM.

### B6 — Azure OpenAI
- Маркеры: Azure.OpenAI, azure_openai_deployment.
- Статус: PARTIAL (1 файл, legacy).
- Доказательство: MetaClaw/metaclaw/config.py (azure_openai_deployment="o3" "# kept for backward compat").
- Рекомендация: держать как fallback provider, не расширять.

### B7 — Vertex AI / Gemini
- Маркеры: Vertex.?AI, Gemini, google/gemini.
- Статус: PARTIAL (1 файл, config-опция).
- Доказательство: MetaClaw/metaclaw/setup_wizard.py (model_id "google/gemini-2.5-pro"). Активная интеграция
  здесь не доказана.
- Рекомендация: активировать только при явном решении оператора.

### B8 — DeepSeek
- Маркеры: DeepSeek, deepseek.
- Статус: PARTIAL (2 файла, audit-only).
- Доказательство: deploy/config.yaml + docker-compose.yml — "DeepSeek V4 — READ-ONLY full-repo audit ONLY.
  NEVER for BANXE service traffic".
- Рекомендация: сохранить ограничение read-only audit; не подключать к service traffic.

Коррекция (честно, не конфликт): ранее LangGraph значился "IMPLEMENTED (via reuse)" по engine-doc coverage —
этот code-only context-verify показывает, что буквального LangGraph в коде НЕТ: реализован диспетчер/adapter-port
(intent_dispatcher), а LangGraph лишь запланирован (P1). Фиксируем как уточнение статуса предыдущего reuse
(marker dispatcher != LangGraph), не как противоречие.

Summary B: IMPLEMENTED=1 PARTIAL=4 MISSING=4 GATED=0

## GROUP C — Data / Observability
C1 ClickHouse (lineage/audit) | qdrant excluded here | Статус: IMPLEMENTED | Доказательство: infra/clickhouse/a2a_events.sql (ADR-145 a2a_events), config/aml_baselines.yaml (banxe.aml_alerts ClickHouse) | Рекомендация: зафиксировать как lineage-store, привязать к F4/I-24, backlog #2/#7 (полнота записи) — не дублировать.
C2 Qdrant vector DB | Маркеры: qdrant, vector_store | Статус: PARTIAL | Доказательство: deploy/docker-compose.yml (qdrant/qdrant:v1.14.0, ADR-136/137), prometheus.yml (qdrant_evo1 scrape, target DOWN until operator up) | Рекомендация: NON-GATED reliability — поднять и интегрировать по решению оператора (episode-substrate).
C3 Temporal durable engine | Маркеры: temporal, start_workflow | Статус: MISSING | Доказательство: только семантические совпадения (event_replayer.py "temporal query", custom start_workflow без Temporal SDK) | Рекомендация: NON-GATED reliability — дедуплицировать с backlog #9 (Temporal durable workflows).
C4 Langfuse | Статус: MISSING | Доказательство: 0 code-matches | Рекомендация: NON-GATED observability, опционально при выборе LLM-стека.
C5 Kafka event stream | Статус: MISSING | Доказательство: 0 code-matches | Рекомендация: NON-GATED reliability, отдельное решение оператора.
C6 OceanBase | Статус: MISSING | Доказательство: 0 code-matches | Рекомендация: не приоритет (ClickHouse уже покрывает audit-store).
C7 SOFAStack | Статус: MISSING | Доказательство: 0 code-matches | Рекомендация: не приоритет.
Summary C: IMPLEMENTED=1 PARTIAL=1 MISSING=5 GATED=0

## GROUP A — Federated / Privacy (EMI-GATED)
A1 FATE / federated learning | Маркеры: fate, federated_learning | Статус: MISSING | Доказательство: 0 code-matches | GATED (federated credit/cross-bank, B-EMI-CREDIT-GATE-001) | Рекомендация: post-licence; НЕ реализовывать сейчас; отдельный ADR (оператор/CTIO).
A2 FISCO BCOS / permissioned chain | Маркеры: fisco, bcos | Статус: MISSING | Доказательство: 0 code-matches | GATED | Рекомендация: post-licence; audit-trail уже покрыт ClickHouse (C1/F4), blockchain-ledger не требуется сейчас.
A3 WeIdentity / SSI | Маркеры: weidentity, verifiable_credential, did: | Статус: MISSING (false-positive VCALENDAR отсеян) | Доказательство: только iCal VERSION в calendar_reporter.py | GATED/optional | Рекомендация: post-licence; не приоритет.
A4 Differential privacy / PSI | Маркеры: differential_privacy, private_set_intersection | Статус: MISSING (false-positive "PSR/PSI 2017" отсеян) | Доказательство: payment-safeguards в card_agent.yaml, не PSI | GATED | Рекомендация: post-licence; связать с федеративным контуром A1.
Summary A: IMPLEMENTED=0 PARTIAL=0 MISSING=4 GATED=4 (все MISSING одновременно GATED)

## GROUP D — UX / Agentic Patterns (frontend/spec scope)
D1 Dual-track UI (conversational+classic) | Статус: MISSING (doc/spec-only) | Доказательство: только в source (world-experience, banxe-uxui-architecture); OVERRIDES.md "dual-track reasoning" нерелевантен | Рекомендация: NON-GATED UX; реализовать во фронтенде по banxe-uxui-architecture-2026-07-10.md, не backend-задача.
D2 Rich Cards (TransferCard/SpendingInsight/Exchange/LoanOffer) | Статус: MISSING (spec-only) | Доказательство: спецификация в banxe-uxui-architecture-2026-07-10.md (§ карточек), нет реализованных компонентов | Рекомендация: NON-GATED UX; frontend-компоненты; LoanOfferCard — при кредит-контуре пометить gated.
D3 Avatar banking | Статус: MISSING (citation-only) | Доказательство: только ссылки OCBC в References | Рекомендация: optional, не приоритет.
D4 Composite tools | Статус: MISSING | Доказательство: 0 matches | Рекомендация: NON-GATED reliability; связать с будущим tool-registry (если появится agent-стек).
D5 Evals-first (LLM-as-judge) | Статус: MISSING (false-positive infra-benchmarks отсеян) | Доказательство: совпадения — TPS/latency бенчмарки, не eval-pipeline | Рекомендация: NON-GATED safety/compliance; связать с backlog #4 (MetricsEngine Brier/ECE/Regret) — не дублировать.
D6 ReAct paradigm | Статус: MISSING (false-positive React-framework отсеян) | Доказательство: 3825 совпадений = React 19 фронтенд, не ReAct | Рекомендация: NON-GATED; рассматривать только с agent-orchestration стеком (связать с B LangGraph).
Summary D: IMPLEMENTED=0 PARTIAL=0 MISSING=6 GATED=0 (LoanOfferCard помечен gated-условно)

## GROUP E — Payments / Agentic Commerce (EMI-GATED)
E1 Visa Intelligent Commerce | Статус: MISSING | Доказательство: 0 code-matches | GATED (agentic payment, B-EMI-CREDIT-GATE-001) | Рекомендация: post-licence; НЕ реализовывать сейчас.
E2 M-Pesa MCP (mobile money) | Статус: MISSING | Доказательство: 0 code-matches | GATED | Рекомендация: post-licence; вне текущей EMI-лицензии.
E3 MCP infrastructure (agent tooling) | Статус: IMPLEMENTED (не платёжный) | Доказательство: safeguarding-engine/app/mcp/server.py (SafeguardingMCPServer), dbt mcp_tool_usage.sql (mcp_tool_events ClickHouse), semgrep mcp-tool rules | Рекомендация: NON-GATED — зафиксировать как agent-tooling MCP; НЕ расширять на платежи без лицензии.
E4 Payment confirmation gate / gateway | Статус: PARTIAL (payment-CDE контур существует) | Доказательство: merchant_acquiring/payment_gateway.py (+audit), open_banking.py / batch_payments (PaymentGatewayPort, InMemoryPaymentGateway) | GATED (payment-CDE) | Рекомендация: классический платёжный шлюз есть; agentic-payment слой поверх — post-licence, НЕ сейчас; HITL/Tier-4 остаются guard-rails.
Summary E: IMPLEMENTED=1 (MCP infra, off-purpose) PARTIAL=1 (payment gateway, gated) MISSING=2 GATED=3
