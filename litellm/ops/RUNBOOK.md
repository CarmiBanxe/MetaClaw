# RUNBOOK — LiteLLM Director (:8000, direct process)

## What
User-level systemd service `litellm-director` running `litellm` directly
(no docker) on 127.0.0.1:8000 with `litellm-config.v2.yaml`.
Separate from the docker-compose LiteLLM on :4000 — do not confuse them.

## Required files (all in ~/MetaClaw/litellm/ops/)
- `litellm-director.service` — unit template (review EDIT-ME lines).
- `litellm-director.env` — runtime env; fill CHANGE_ME, keep chmod 600.
- `check-litellm-director.sh` — read-only healthcheck.
- `install-systemd-artifacts.sh` — copies unit, prints next commands.

## Install
1. Review the unit: binary path in `ExecStart`, `WorkingDirectory`.
2. Fill `litellm-director.env` (no CHANGE_ME left), `chmod 600` it.
3. `./install-systemd-artifacts.sh` (user mode; `--system` prints sudo variant).

## Validate BEFORE first start
- `./check-litellm-director.sh` — expect PASS on config/unit, WARN on HTTP
  (not listening yet is normal).
- Dry-run in foreground: `cd ~/MetaClaw/litellm && litellm --config
  litellm-config.v2.yaml --host 127.0.0.1 --port 8000` → Ctrl-C when clean.

## Start manually
`systemctl --user daemon-reload && systemctl --user start litellm-director`

## Enable autostart (after a good manual start)
`systemctl --user enable litellm-director`
`loginctl enable-linger $USER`  # required so it starts at boot, not at login

## Logs
`journalctl --user -u litellm-director -f` (follow)
`journalctl --user -u litellm-director -n 200 --no-pager` (recent)

## Verify :8000 and tools
`./check-litellm-director.sh` — all PASS/WARN explained inline;
key probes: `/health/liveliness` (no auth), `/health` and `/v1/models`
(master key from env).

## Roll back safely
1. `systemctl --user stop litellm-director`
2. `systemctl --user disable litellm-director` (removes autostart)
3. `rm ~/.config/systemd/user/litellm-director.service && systemctl --user daemon-reload`
4. Config rollback: restore the newest known-good
   `litellm-config.v2.yaml.bak-*` over `litellm-config.v2.yaml`, re-run
   the healthcheck, then start again. Templates in ops/ stay untouched.
