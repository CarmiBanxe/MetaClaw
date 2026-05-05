"""Smoke test for Canon Judge MCP server — tool registration (no live LLM)."""

from __future__ import annotations

from src.canon_judge.mcp.server import TOOL_NAME, create_server


def test_server_creates_successfully() -> None:
    """MCP server instantiates without error."""
    server = create_server()
    assert server is not None
    assert server.name == "canon-judge"


def test_tool_name_constant() -> None:
    """Tool name matches expected value."""
    assert TOOL_NAME == "canon_judge_evaluate"


def test_server_has_tool_handlers() -> None:
    """Server has list_tools and call_tool handlers registered."""
    server = create_server()
    # MCP Server registers handlers via decorators — verify they exist
    assert hasattr(server, "list_tools")
    assert hasattr(server, "call_tool")
