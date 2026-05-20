#!/usr/bin/env python3
"""Programming Learning MCP Server — FastMCP."""

import json
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP("Programming Learning Server")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "topics.json"


def _load_topics() -> list[dict]:
    with DATA_PATH.open(encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, list):
        return data
    return data.get("topics", [])


def _normalize(text: str) -> str:
    return text.casefold().strip()


def _topic_matches(topic: dict, query: str) -> bool:
    q = _normalize(query)
    if not q:
        return False
    if q in _normalize(topic.get("title", "")):
        return True
    if q in _normalize(topic.get("id", "").replace("-", " ")):
        return True
    if q in _normalize(topic.get("summary", "")):
        return True
    for concept in topic.get("key_concepts", []):
        if q in _normalize(str(concept)):
            return True
    return False


def _topic_result(topic: dict) -> dict:
    """Return fields useful for choosing a relevant topic."""
    return {
        "id": topic["id"],
        "title": topic["title"],
        "summary": topic["summary"],
        "prerequisites": topic.get("prerequisites", []),
        "key_concepts": topic.get("key_concepts", []),
    }


@mcp.tool
def search_topics(query: str) -> list[dict]:
    """Search programming topics by title or keyword in key concepts."""
    topics = _load_topics()
    return [_topic_result(t) for t in topics if _topic_matches(t, query)]


if __name__ == "__main__":
    mcp.run()
