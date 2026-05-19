# Real-time communication with WebSockets

WebSocket servers and clients using the `websockets` library and `async` / `await`.

## Requirements

- Ubuntu 20.04
- Python 3.x
- `websockets` library

## Tasks

- **0. Server** — `echo_server.py`: WebSocket server on `localhost:8765` that echoes each text message back to the sender and keeps the connection open for continuous communication.
- **1. Client** — `ws_client.py`: connects to the echo server, sends `Hello WebSocket`, prints the server response exactly as received, then closes the connection.
- **2. Validation** — `validation_server.py`: validates each message (`OK:{text}` or `ERR:EMPTY`); keeps the connection open after invalid messages.
- **3. Unicast** — `unicast_server.py`: tracks active connections; replies with `U:{message}` only to the sender.
- **4. Broadcast** — `broadcast_server.py`: sends `B:{message}` to every connected client.
