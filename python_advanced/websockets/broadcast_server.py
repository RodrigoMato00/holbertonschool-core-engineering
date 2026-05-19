#!/usr/bin/env python3
"""WebSocket broadcast server — task 4."""

import asyncio

import websockets

CONNECTED = set()


async def connection_handler(websocket):
    """Broadcast each message to every connected client."""
    CONNECTED.add(websocket)
    try:
        async for message in websocket:
            payload = f"B:{message}"
            for client in list(CONNECTED):
                await client.send(payload)
    finally:
        CONNECTED.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
