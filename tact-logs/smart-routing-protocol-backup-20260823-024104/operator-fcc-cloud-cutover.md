# OPERATOR CUTOVER — FCC CLOUD-ONLY STACK

## Decision
Primary runtime for Claude Code must use strong cloud models through Free Claude Code.
Local weak server models must not be used as the main coding/reasoning layer.
Allowed role for local models: emergency fallback only, or fully disabled.

## Why
- FCC is a public open-source proxy project that routes Claude Code-compatible traffic to alternative providers while keeping the Claude Code interface. 
- Claude Code supports gateway routing through ANTHROPIC_BASE_URL and gateway credentials through ANTHROPIC_AUTH_TOKEN.
- The current local weak models are not acceptable for the required engineering quality.
- Therefore the correct target architecture is cloud-first via FCC, documented at project level and applied consistently across terminals.

## Required target providers
Priority order for evaluation and rollout:
1. OpenRouter — broad model choice, easy cloud routing.
2. NVIDIA NIM — strong free/cheap options, including hosted reasoning/coding models.
3. Kimi/Moonshot — strong reasoning candidate if exposed through FCC/NIM/OpenRouter path.
4. DeepSeek — cheap fallback / factory tier.
5. Ollama — emergency-only fallback, not primary.

## Required target policy
- Central terminal (BRAIN): strongest cloud reasoning/coding model.
- Left terminal (FACTORY): cheaper but still capable cloud coding model.
- Right terminal (ASSISTANT): fast cloud helper model.
- No local weak model may remain as default primary model.

## Operator actions
1. Open FCC Admin UI.
2. Replace current primary local Ollama model with a strong cloud model.
3. Configure fallback chain using cloud providers only.
4. Move Ollama to last-resort fallback or remove it.
5. Keep project docs and settings aligned with the cloud-first policy.

## Required project standard
The project must reflect:
- cloud-first AI routing
- no weak local primary models
- terminal role separation
- documented gateway policy
- operator-controlled rollout

## Exact config intent
Project env must continue using:
- ANTHROPIC_BASE_URL=http://127.0.0.1:8082
- ANTHROPIC_AUTH_TOKEN=freecc

But FCC internal provider/model routing must be changed to cloud-first.

## Rollout sequence
1. Set primary cloud model for Central.
2. Set cheaper cloud model for Factory.
3. Set fast helper cloud model for Assistant.
4. Add cloud-only fallback chain.
5. Demote/remove Ollama.
6. Verify via /status and /model in each terminal.
7. Update docs if the chosen provider/model names differ from current assumptions.

## Hard rule
Do not spend more operator time trying to improve weak local models.
The strategic direction is cloud-first through FCC.

