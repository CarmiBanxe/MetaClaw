# LiteLLM LAN Gateway — runbook (FU-2 Phase 4)

The gateway is the single OpenAI-compatible entrypoint (`:4000`) in front of the
LAN model backends (Ollama GPU nodes + llama.cpp RPC). This directory makes its
cold-start reproducible. **This phase is infra/runbook only — it does not flip
`INTENT_LAYER_ENABLED` or route any client traffic.**

## Files

| File | Purpose |
|------|---------|
| `litellm-config.v2.yaml` | Live model routing/cache config (LAN-dev defaults). |
| `.env.example` | Template for every secret/endpoint. Copy → `.env`. |
| `docker-compose.yml` | Reproducible gateway on `:4000` (+ optional Postgres). |
| `../scripts/litellm-local-startup.sh` | Start + healthcheck helper. |

## Topology (as deployed)

- **Proxy:** `0.0.0.0:4000` (`litellm-lan-gateway.service`, master_key auth).
- **Ollama:** `192.168.0.72:11434` (evo1), `192.168.0.15:11434` (evo2),
  `127.0.0.1:11434` (legion).
- **RPC (llama.cpp, OpenAI API):** `192.168.0.72:8081` (GLM), `192.168.0.15:8082` (Q235).
- **Redis cache:** `192.168.0.72:6379`, namespace `banxe-litellm`.
- **Postgres (optional):** `litellm-db` on `:5435` — off by default.

## Quick start

```bash
cp litellm/.env.example litellm/.env   # then fill in real values
scripts/litellm-local-startup.sh       # compose up + healthcheck

# with optional Postgres persistence:
scripts/litellm-local-startup.sh --profile db

# use the existing systemd user unit instead of docker:
scripts/litellm-local-startup.sh --mode systemd

# only healthcheck an already-running gateway:
scripts/litellm-local-startup.sh --no-start
```

## Healthcheck (one-liner)

```bash
curl -fsS http://127.0.0.1:4000/health/liveliness && echo " gateway live"
# authenticated model list:
curl -fsS -H "Authorization: Bearer $LITELLM_MASTER_KEY" http://127.0.0.1:4000/v1/models
```

`/health/liveliness` and `/health/readiness` are unauthenticated; `/v1/models`
requires the master key.

## Secrets

- `.env` is gitignored — never commit it.
- The committed `litellm-config.v2.yaml` carries LAN-only dev keys for local use.
  For any non-LAN deployment, replace inline keys with `os.environ/<VAR>`
  references and source them from `.env` (var names in `.env.example`).
