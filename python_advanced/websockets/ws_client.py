#!/usr/bin/env python3
"""Minimal WebSocket client — task 1."""

import asyncio

import websockets

URI = "ws://localhost:8765"
MESSAGE = "Hello WebSocket"


async def main():
    async with websockets.connect(URI) as websocket:
        await websocket.send(MESSAGE)
        response = await websocket.recv()
        print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
