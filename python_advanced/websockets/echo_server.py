#!/usr/bin/env python3
"""Minimal WebSocket echo server — task 0."""

import asyncio

import websockets


async def connection_handler(websocket):
    """Echo each text message back to the same client."""
    async for message in websocket:
        await websocket.send(f"ECO:{message}")


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
