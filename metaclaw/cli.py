"""
MetaClaw CLI entry point.

Usage:
    metaclaw setup          — interactive first-time configuration wizard
    metaclaw start          — one-click start (proxy + optional RL training)
    metaclaw stop           — stop a running MetaClaw instance
    metaclaw status         — check whether MetaClaw is running
    metaclaw config KEY VAL — set a config value (e.g. rl.enabled true)
    metaclaw config show    — show current config
"""

from __future__ import annotations

import sys

try:
    import click
except ImportError:
    print("MetaClaw requires 'click'. Install it with: pip install click")
    sys.exit(1)

from .config_store import CONFIG_FILE, ConfigStore


@click.group()
def metaclaw():
    """MetaClaw — OpenClaw skill injection and RL training."""


@metaclaw.command()
def setup():
    """Interactive first-time configuration wizard."""
    from .setup_wizard import SetupWizard
    SetupWizard().run()


@metaclaw.command()
@click.option(
    "--mode",
    type=click.Choice(["skills_only", "rl"]),
    default=None,
    help="Override operating mode for this session.",
)
@click.option(
    "--port",
    type=int,
    default=None,
    help="Override proxy port for this session.",
)
def start(mode: str | None, port: int | None):
    """Start MetaClaw (proxy + optional RL training)."""
    import asyncio
    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )

    cs = ConfigStore()
    if not cs.exists():
        click.echo(
            "No config found. Run 'metaclaw setup' first.",
            err=True,
        )
        sys.exit(1)

    # Session-level overrides (don't persist)
    if mode or port:
        data = cs.load()
        if mode:
            data["mode"] = mode
        if port:
            data.setdefault("proxy", {})["port"] = port
        # Use an in-memory store for this session
        from .config_store import ConfigStore as _CS
        import tempfile, os, yaml
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False, encoding="utf-8"
        )
        yaml.dump(data, tmp)
        tmp.close()
        cs = _CS(config_file=__import__("pathlib").Path(tmp.name))

    from .launcher import MetaClawLauncher
    launcher = MetaClawLauncher(cs)
    try:
        asyncio.run(launcher.start())
    except KeyboardInterrupt:
        click.echo("\nInterrupted — stopping MetaClaw.")
        launcher.stop()


@metaclaw.command()
def stop():
    """Stop a running MetaClaw instance."""
    import os
    import signal
    from pathlib import Path

    pid_file = Path.home() / ".metaclaw" / "metaclaw.pid"
    if not pid_file.exists():
        click.echo("MetaClaw is not running (no PID file found).")
        return
    try:
        pid = int(pid_file.read_text().strip())
        os.kill(pid, signal.SIGTERM)
        pid_file.unlink(missing_ok=True)
        click.echo(f"Sent SIGTERM to PID {pid}.")
    except ProcessLookupError:
        click.echo("Process not found — cleaning up stale PID file.")
        pid_file.unlink(missing_ok=True)
    except Exception as e:
        click.echo(f"Error stopping MetaClaw: {e}", err=True)


@metaclaw.command()
def status():
    """Check whether MetaClaw is running."""
    import os
    from pathlib import Path

    pid_file = Path.home() / ".metaclaw" / "metaclaw.pid"
    if not pid_file.exists():
        click.echo("MetaClaw: not running")
        return

    try:
        pid = int(pid_file.read_text().strip())
        os.kill(pid, 0)  # check if process exists
    except (ProcessLookupError, ValueError):
        click.echo("MetaClaw: not running (stale PID file)")
        pid_file.unlink(missing_ok=True)
        return

    # Try health check
    cs = ConfigStore()
    port = cs.get("proxy.port") or 30000
    try:
        import urllib.request
        with urllib.request.urlopen(
            f"http://localhost:{port}/healthz", timeout=2
        ) as resp:
            healthy = resp.status == 200
    except Exception:
        healthy = False

    mode = cs.get("mode") or "?"
    if healthy:
        click.echo(f"MetaClaw: running  (PID={pid}, mode={mode}, proxy=:{port})")
    else:
        click.echo(f"MetaClaw: starting (PID={pid}, mode={mode}, proxy=:{port})")

    # Show scheduler state if available.
    state_file = Path.home() / ".metaclaw" / "scheduler_state.json"
    if state_file.exists():
        try:
            import json
            sched = json.loads(state_file.read_text())
            state_val  = sched.get("state", "?")
            sleep_win  = sched.get("sleep_window", "?")
            idle_min   = sched.get("idle_threshold_minutes", "?")
            updated_at = sched.get("updated_at", "?")
            click.echo(
                f"scheduler:  state={state_val}  "
                f"sleep={sleep_win}  idle≥{idle_min}min  "
                f"(updated {updated_at})"
            )
        except Exception:
            pass


@metaclaw.command(name="config")
@click.argument("key_or_action")
@click.argument("value", required=False)
def config_cmd(key_or_action: str, value: str | None):
    """Get or set a config value.

    Examples:\n
      metaclaw config show\n
      metaclaw config rl.enabled true\n
      metaclaw config proxy.port 30001
    """
    cs = ConfigStore()
    if key_or_action == "show":
        if not cs.exists():
            click.echo("No config file found. Run 'metaclaw setup' first.")
            return
        click.echo(f"Config file: {CONFIG_FILE}\n")
        click.echo(cs.describe())
        return

    if value is None:
        # Get mode
        result = cs.get(key_or_action)
        if result is None:
            click.echo(f"{key_or_action}: (not set)")
        else:
            click.echo(f"{key_or_action}: {result}")
        return

    cs.set(key_or_action, value)
    click.echo(f"Set {key_or_action} = {cs.get(key_or_action)}")


@metaclaw.group()
def scheduler():
    """Scheduler management commands."""


@scheduler.command(name="status")
def scheduler_status():
    """Show the current slow-update scheduler state."""
    import json
    from pathlib import Path

    state_file = Path.home() / ".metaclaw" / "scheduler_state.json"
    if not state_file.exists():
        click.echo("Scheduler not running or not enabled.")
        return
    try:
        data = json.loads(state_file.read_text())
        click.echo(f"state:              {data.get('state', '?')}")
        click.echo(f"sleep window:       {data.get('sleep_window', '?')}")
        click.echo(f"idle threshold:     {data.get('idle_threshold_minutes', '?')} min")
        click.echo(f"last updated:       {data.get('updated_at', '?')}")
    except Exception as exc:
        click.echo(f"Error reading scheduler state: {exc}", err=True)


@scheduler.command(name="next-window")
def scheduler_next_window():
    """Estimate when the next slow-update window will open.

    Reads live scheduler state and configuration to give an approximate
    time until the next eligible idle/sleep/calendar window.
    """
    import json
    from pathlib import Path

    state_file = Path.home() / ".metaclaw" / "scheduler_state.json"
    if not state_file.exists():
        click.echo("Scheduler not running or not enabled.")
        return

    try:
        data = json.loads(state_file.read_text())
    except Exception as exc:
        click.echo(f"Error reading scheduler state: {exc}", err=True)
        return

    state = data.get("state", "?")
    click.echo(f"Current state:   {state}")
    click.echo(f"Sleep window:    {data.get('sleep_window', '?')}")
    click.echo(f"Idle threshold:  {data.get('idle_threshold_minutes', '?')} min")

    if state in ("window_open", "updating"):
        click.echo("→ A window is OPEN right now — RL update may be in progress.")
    elif state == "pausing":
        click.echo("→ Pausing current update (user became active).")
    else:
        click.echo(
            "→ Waiting for next idle/sleep/calendar window.\n"
            "  The scheduler checks every 60 seconds.\n"
            "  Next window opens when: sleep hours begin, "
            "or idle exceeds threshold, or a calendar event starts."
        )
