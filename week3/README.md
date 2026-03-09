# National House Pricing MCP Server

This is a Model Context Protocol (MCP) server that provides tools for fetching national real estate pricing data in China. It supports querying the current house price and the year-over-year (YoY) trend for major cities.

## Features
- Provides an MCP tool `get_current_price(city: str)`
- Provides an MCP tool `get_price_trend(city: str)`
- Simulated external HTTP request with resilience (handles timeouts and potential network failures).
- Mocked rate limit awareness.

## Prerequisites
- Python 3.10+
- `mcp` library from Anthropic
- `httpx` for HTTP request simulation

To install dependencies:
```bash
pip install mcp httpx
```

## Running the Server (Local STDIO Transport)
This server runs using the STDIO transport, making it compatible with MCP clients such as Claude Desktop and Cursor.

Run the server script:
```bash
python server/app.py
```

### Setup with Claude Desktop Client
To add this MCP server to a Claude Desktop installation, edit your `claude_desktop_config.json` file (typically located at `%APPDATA%\Claude\claude_desktop_config.json` on Windows):

```json
{
  "mcpServers": {
    "house-pricing-server": {
      "command": "python",
      "args": [
        "C:\\absolute\\path\\to\\week3\\server\\app.py"
      ]
    }
  }
}
```

### Usage Example
Once connected, you can ask Claude:
- *"What is the current house price in Beijing?"*
- *"Can you tell me the year-over-year pricing trend for Shanghai?"*

Claude will automatically execute the `get_current_price` or `get_price_trend` tool with your specified city, fetch the data, and incorporate it into the reply.
