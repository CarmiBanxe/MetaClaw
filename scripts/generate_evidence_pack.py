#!/usr/bin/env python3
"""P5 Evidence Pack Generator — Software Factory Canon Section 9.

Usage: python3 scripts/generate_evidence_pack.py --branch <name> --verdict <PASS|WARN|BLOCK>
"""
import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def git(cmd: str) -> str:
    return subprocess.check_output(f"git {cmd}", shell=True, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description="Generate P5 Evidence Pack")
    parser.add_argument("--branch", required=True)
    parser.add_argument("--verdict", default="PASS", choices=["PASS", "WARN", "BLOCK"])
    parser.add_argument("--il-ref", default="UNKNOWN")
    parser.add_argument("--signer", default="system")
    parser.add_argument("--output-dir", default="docs/evidence-packs")
    args = parser.parse_args()

    pack_id = str(uuid4())[:8]
    ts = datetime.now(timezone.utc).isoformat()
    commit = git("rev-parse HEAD")
    files = git("diff --name-only HEAD~1").split("\n")

    pack = {
        "pack_id": pack_id,
        "timestamp": ts,
        "instruction_ref": args.il_ref,
        "branch": args.branch,
        "commit_sha": commit,
        "evaluation_verdict": args.verdict,
        "final_verdict": "APPROVED" if args.verdict == "PASS" else "PENDING",
        "signer": args.signer,
        "files_changed": files,
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")

    # JSON sidecar
    json_path = out_dir / f"{date_str}-{pack_id}.json"
    json_path.write_text(json.dumps(pack, indent=2))

    # Markdown
    md_path = out_dir / f"{date_str}-{pack_id}.md"
    md_path.write_text(f"""# P5 — Evidence Pack
- pack_id: {pack_id}
- timestamp: {ts}
- instruction_ref: {args.il_ref}
- branch: {args.branch}
- commit: {commit}
- verdict: {args.verdict}
- signer: {args.signer}
- files: {', '.join(files)}
""")

    print(f"P5 pack generated: {json_path} + {md_path}")


if __name__ == "__main__":
    main()
