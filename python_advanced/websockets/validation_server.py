#!/usr/bin/env python3
"""WebSocket server with message validation — task 2."""

import asyncio

import websockets


async def connection_handler(websocket):
    """Validate each message; reply OK:{text} or ERR:EMPTY."""
    async for message in websocket:
        trimmed = message.strip()
        if trimmed == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{trimmed}")


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
