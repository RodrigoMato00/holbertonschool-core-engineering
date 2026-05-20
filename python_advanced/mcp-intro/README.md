# MCP Servers in Python: Tools, Resources, and Agent Integration

Programming Learning MCP Server built with FastMCP.

## MCP Architecture Summary

**What is MCP?** The Model Context Protocol (MCP) is a standard way for AI applications to talk to external capabilities (files, APIs, local data) through a shared contract. Instead of wiring every tool directly into your agent code, you expose capabilities on an MCP server and let a client discover and call them.

**MCP host** — The application the user interacts with (for example, an IDE, a chat app, or our study assistant). The host runs the conversation, decides when help from external data is needed, and coordinates one or more connections to MCP servers.

**MCP client** — A connector inside the host (or in a small script like `client/mcp_client.py`) that speaks the protocol with **one** MCP server. If the host needs two servers, it typically uses two clients—one per server.

**MCP server** — A separate program (here, `server/learning_server.py`) that advertises what it can do: which **tools** it can run and which **resources** it can read. Our server wraps the local `topics.json` dataset and study helpers.

**Tools** — Actions the server can execute when the client asks (for example, search topics, return details, suggest a practice exercise). Tools are like functions with a name, inputs, and a result.

**Resources** — Read-only data the client can fetch (for example, a catalog of all topic names). Resources are useful when the model needs context without running an action.

**Expose only what you need** — A server should publish a small, clear set of tools and resources. Extra endpoints increase attack surface, confuse agents, and make maintenance harder. For this project, we only expose study-topic operations—not the whole filesystem or arbitrary code execution.

**Example in this project:** A student asks, *“I want to study Python decorators. What should I review first?”* The **host** runs our **agent**. The **client** calls the **server** tool that looks up “Python decorators” in `topics.json` and may read the topic catalog **resource**. The agent then turns that structured data into a short, friendly answer.

## Project layout

```text
mcp-intro/
├── server/learning_server.py   # MCP server
├── client/mcp_client.py        # MCP client
├── client/agent.py             # Agent using the server
├── data/topics.json            # Local topic dataset
└── output/                     # Generated agent responses
```

## Status

- **Task 0:** project structure.
- **Task 1:** MCP architecture summary (this README section).
- **Task 2:** minimal FastMCP server in `server/learning_server.py`.
- **Task 3:** local dataset in `data/topics.json` (6 topics).
- **Task 4:** MCP tool `search_topics` on the server.
- **Task 5:** MCP tool `get_topic_details` on the server.
- **Task 6:** read-only resource `topics://catalog`.
- **Task 7:** server tested with `client/mcp_client.py` (and optional MCP Inspector).

## Requirements

- Python **3.10+** (required by FastMCP)
- `pip install -r requirements.txt`

## Run the MCP server (Task 2+)

From the `mcp-intro` directory:

```bash
python3 server/learning_server.py
```

The server uses stdio transport by default. Do not print debug messages to stdout while it runs.

For **MCP Inspector** or HTTP clients:

```bash
python3 server/learning_server.py --http
# Server URL: http://localhost:8000/mcp
```

## Test the server (Task 7)

From `mcp-intro/` with dependencies installed:

```bash
python3 client/mcp_client.py
```

The script connects to the server in-process, lists tools and resources, calls both tools, reads `topics://catalog`, and checks invalid `topic_id` handling.

### Sample output (excerpt)

**Tools listed:**

```text
Tools: ['get_topic_details', 'search_topics']
```

**search_topics** with `query=decorator` returns at least:

```json
[
  {
    "id": "python-decorators",
    "title": "Python Decorators",
    "summary": "Decorators wrap functions or methods..."
  }
]
```

**get_topic_details** with invalid id returns:

```json
{
  "error": "Topic not found: 'not-a-real-topic'",
  "available_ids": ["python-decorators", "..."]
}
```

**topics://catalog** returns a JSON array of `id` and `title` for all six topics.

Agents and full README sections will be added in later tasks.
