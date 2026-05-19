#!/usr/bin/env python3
"""WebSocket unicast server — task 3."""

import asyncio

import websockets

CONNECTED = set()


async def connection_handler(websocket):
    """Reply only to the client that sent the message."""
    CONNECTED.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        CONNECTED.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
