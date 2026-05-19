#!/usr/bin/env python3
"""Minimal WebSocket client — task 1."""

import asyncio
import os

import websockets

DEFAULT_URI = "ws://localhost:8765"
DEFAULT_MESSAGE = "Hello WebSocket"


async def connect_and_send(uri: str, text: str) -> str:
    """Connect, send one message, return the server response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    uri = os.environ.get("WS_URI", DEFAULT_URI)
    message = "demo" if "WS_URI" in os.environ else DEFAULT_MESSAGE
    print(await connect_and_send(uri, message), end="")


if __name__ == "__main__":
    asyncio.run(main())
