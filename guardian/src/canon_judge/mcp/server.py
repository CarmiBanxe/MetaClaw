"""MCP server exposing canon_judge.evaluate as a tool.

Transport: stdio (for Claude Code integration).
Mode: audit (log-only, does not block output).

Usage:
    python -m src.canon_judge.mcp.server

Or via Claude Code MCP config:
    {"command": "python", "args": ["-m", "src.canon_judge.mcp.server"], "cwd": "/path/to/guardian"}
"""

from __future__ import annotations

import json
import os
import logging
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from ..judge import CanonJudge, JudgeVerdict

logger = logging.getLogger(__name__)

TOOL_NAME = "canon_judge_evaluate"
TOOL_DESCRIPTION = (
    "Evaluate AI agent output against ADR-025 Agent Interaction Canon (15 sections). "
    "Returns verdict (pass/warn/fail), violated sections, and correction suggestion. "
    "Mode: audit (log-only, informational)."
)


def create_server(
    ollama_url: str = "http://127.0.0.1:11434",
    model: str = "qwen3.5:35b",
    mode: str | None = None,
) -> Server:
    """Create MCP server with canon_judge.evaluate tool."""
    _mode = mode or os.environ.get("CANON_JUDGE_MODE", "enforce")
    logger.info("Canon Judge mode: %s", _mode)
    server = Server("canon-judge")
    judge = CanonJudge(base_url=ollama_url, model=model)

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name=TOOL_NAME,
                description=TOOL_DESCRIPTION,
                inputSchema={
                    "type": "object",
                    "properties": {
                        "agent_output": {
                            "type": "string",
                            "description": "The agent output text to evaluate against canon.",
                        },
                        "last_messages": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "role": {"type": "string"},
                                    "content": {"type": "string"},
                                },
                            },
                            "description": "Last 10 chat messages for context (optional).",
                            "default": [],
                        },
                    },
                    "required": ["agent_output"],
                },
            )
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
        if name != TOOL_NAME:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

        agent_output = arguments.get("agent_output", "")
        last_messages = arguments.get("last_messages", [])

        verdict: JudgeVerdict = judge.evaluate(
            agent_output=agent_output,
            chat_history=last_messages,
        )

        result = {
            "verdict": verdict.verdict,
            "violated_sections": verdict.violated_sections,
            "correction": verdict.correction,
            "mode": "audit",
        }

        if verdict.error:
            result["error"] = verdict.error

        logger.info(
            "canon-judge audit: verdict=%s sections=%s",
            verdict.verdict,
            verdict.violated_sections,
        )

        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False))]

    return server


async def main() -> None:
    """Run MCP server on stdio transport."""
    server = create_server()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
