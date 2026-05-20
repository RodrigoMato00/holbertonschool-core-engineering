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


def _find_topic_by_id(topic_id: str) -> dict | None:
    tid = topic_id.strip()
    if not tid:
        return None
    for topic in _load_topics():
        if topic.get("id") == tid:
            return topic
    return None


@mcp.tool
def get_topic_details(topic_id: str) -> dict:
    """Return full information for a topic by id."""
    topic = _find_topic_by_id(topic_id)
    if topic is None:
        return {
            "error": f"Topic not found: {topic_id!r}",
            "available_ids": [t.get("id") for t in _load_topics()],
        }
    return dict(topic)


@mcp.resource("topics://catalog")
def get_topic_catalog() -> str:
    """Return the list of available topic ids and titles."""
    catalog = [
        {"id": topic["id"], "title": topic["title"]}
        for topic in _load_topics()
    ]
    return json.dumps(catalog)


if __name__ == "__main__":
    mcp.run()
