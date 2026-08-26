# CLOUD-FIRST FCC POLICY

## Canonical direction
The primary target is cloud-first routing through Free Claude Code.
Ollama must not be the strategic focus.
Ollama is optional only as a last-resort local fallback.

## Approved primary provider focus
1. NVIDIA NIM
2. OpenRouter
3. DeepSeek
4. Kimi / Moonshot (through supported FCC provider path)

## Operational rule
- Claude Code stays the client interface.
- FCC stays the local proxy gateway.
- Strong cloud models become the main execution layer.
- Local weak models must not remain the default path.

## Required operator intent in FCC Admin UI
- Configure a cloud provider API key.
- Select a strong cloud coding or reasoning model.
- Validate and apply the provider.
- Configure fallback to another cloud provider.
- Move local Ollama to last fallback or disable it.

## Environment invariants
Keep:
- ANTHROPIC_BASE_URL=http://127.0.0.1:8082
- ANTHROPIC_AUTH_TOKEN=freecc

Change:
- FCC internal provider/model routing to cloud-first only.

## Hard rule
Any wording or config that makes Ollama the implied default is incorrect for this project direction.

> **Smart Model Routing:** `docs/canon/smart-model-routing-protocol-v1.md` is the governing role, trust-tier, preflight, and independent-review protocol for this document.
