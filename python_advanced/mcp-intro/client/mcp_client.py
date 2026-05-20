#!/usr/bin/env python3
"""Test the Programming Learning MCP server (Task 7)."""

import asyncio
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "server"))

from learning_server import mcp  # noqa: E402


def _step(title: str) -> None:
    print(f"\n=== {title} ===")


async def run_tests() -> int:
    from fastmcp import Client

    _step("Connect to server (in-process)")
    async with Client(mcp) as client:
        _step("List tools")
        tools = await client.list_tools()
        tool_names = sorted(t.name for t in tools)
        print("Tools:", tool_names)
        for required in ("search_topics", "get_topic_details"):
            if required not in tool_names:
                print(f"Missing tool: {required}", file=sys.stderr)
                return 1

        _step("search_topics(query='decorator')")
        search = await client.call_tool("search_topics", {"query": "decorator"})
        print(json.dumps(search.data, indent=2))

        _step("get_topic_details(topic_id='python-decorators')")
        details = await client.call_tool(
            "get_topic_details",
            {"topic_id": "python-decorators"},
        )
        print(json.dumps(details.data, indent=2))

        _step("get_topic_details(invalid id)")
        invalid = await client.call_tool(
            "get_topic_details",
            {"topic_id": "not-a-real-topic"},
        )
        print(json.dumps(invalid.data, indent=2))
        if "error" not in invalid.data:
            print("Expected error key for invalid topic id", file=sys.stderr)
            return 1

        _step("Read resource topics://catalog")
        resources = await client.list_resources()
        resource_uris = [r.uri for r in resources]
        print("Resources:", resource_uris)
        if "topics://catalog" not in resource_uris:
            print("Missing resource topics://catalog", file=sys.stderr)
            return 1
        catalog = await client.read_resource("topics://catalog")
        print(catalog[0].text)

    print("\nAll Task 7 checks passed.")
    return 0


def main() -> None:
    try:
        raise SystemExit(asyncio.run(run_tests()))
    except ImportError as exc:
        print(
            "fastmcp is required (Python 3.10+). "
            "Install with: pip install -r requirements.txt",
            file=sys.stderr,
        )
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
