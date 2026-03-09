# Week 3 — Build a Custom MCP Server
# 第三周 — 构建自定义的 MCP 服务器

Design and implement a Model Context Protocol (MCP) server that wraps a real external API. You may:
设计并实现一个模型上下文协议 (MCP) 服务器，用于包装（包裹）一个真实的外部 API。你可以：
- Run it **locally** (STDIO transport) and integrate with an MCP client (like Claude Desktop).
- 在本地运行它 (使用 STDIO 标准输入输出流传输)，并与一个 MCP 客户端（如 Claude Desktop）集成。
- Or run it **remotely** (HTTP transport) and call it from a model agent or client. This is harder but earns extra credit.
- 或者远程运行它 (使用 HTTP 传输)，并从模型智能体或客户端调用它。这会更难，但可以获得额外加分。

Bonus points for adding authentication (API keys or OAuth2) aligned with the MCP Authorization spec.
如果添加了符合 MCP 授权规范的身份验证（API 密钥或 OAuth2），将获得加分。

## Learning goals
## 学习目标
- Understand core MCP capabilities: tools, resources, prompts.
- 理解核心的 MCP 能力：工具 (tools)、资源 (resources)、提示词 (prompts)。
- Implement tool definitions with typed parameters and robust error handling.
- 实现带有类型化参数和健壮的错误处理的工具定义。
- Follow logging and transport best practices (no stdout for STDIO servers).
- 遵循日志记录和传输的最佳实践（对于 STDIO 服务器，不能使用标准输出 `stdout` 打印日志）。
- Optionally implement authorization flows for HTTP transports.
- （可选）为 HTTP 传输实现授权流程。

## Requirements
## 要求
1. Choose an external API and document which endpoints you’ll use. Examples: weather, GitHub issues, Notion pages, movie/TV databases, calendar, task managers, finance/crypto, travel, sports stats.
1. 选择一个外部 API 并记录你将使用哪些端点 (endpoints)。例如：天气、GitHub Issues、Notion 页面、电影/电视数据库、日历、任务管理器、金融/加密货币、旅游、体育统计数据。
2. Expose at least two MCP tools
2. 暴露（提供）至少两个 MCP 工具。
3. Implement basic resilience:
3. 实现基本的弹性（健壮性）：
   - Graceful errors for HTTP failures, timeouts, and empty results.
   - 针对 HTTP 失败、超时和空结果的优雅错误处理。
   - Respect API rate limits (e.g., simple backoff or user-facing warning).
   - 遵守 API 的速率限制（例如，简单的退避重试机制或面向用户的警告）。
4. Packaging and docs:
4. 打包和文档：
   - Provide clear setup instructions, environment variables, and run commands.
   - 提供清晰的设置说明、环境变量和运行命令。
   - Include an example invocation flow (what to type/click in the client to trigger the tools).
   - 包含一个示例调用流程（在客户端中输入/点击什么来触发这些工具）。
5. Choose one deployment mode:
5. 选择一种部署模式：
   - Local: STDIO server, runnable from your machine and discoverable by Claude Desktop or an AI IDE like Cursor.
   - 本地：STDIO 服务器，可从你的机器上运行，并可被 Claude Desktop 或类似的 AI IDE（如 Cursor）发现和调用。
   - Remote: HTTP server accessible over the network, callable by an MCP-aware client or an agent runtime. Extra credit if deployed and reachable.
   - 远程：可以通过网络访问的 HTTP 服务器，可以被支持 MCP 的客户端或智能体运行环境调用。如果部署并可访问，则获得额外加分。
6. (Optional) Bonus: Authentication
6. （可选）加分项：身份验证
   - API key support via environment variable and client configuration; or
   - 通过环境变量和客户端配置支持 API 密钥；或者
   - OAuth2-style bearer tokens for HTTP transport, validating token audience and never passing tokens through to upstream APIs.
   - 为 HTTP 传输提供类似 OAuth2 的 bearer 令牌，验证令牌的 audience (受众)，并且永远不将这些令牌传递给上游 API。

## Deliverables
## 交付物
- Source code under `week3/` (suggested: `week3/server/` with a clear entrypoint like `main.py` or `app.py`).
- 源代码放在 `week3/` 目录下（建议放在 `week3/server/` 中，并有一个清晰的入口点，如 `main.py` 或 `app.py`）。
- `week3/README.md` with:
- `week3/README.md` 需包含：
  - Prerequisites, environment setup, and run instructions (local and/or remote).
  - 前置要求、环境设置和运行说明（本地和/或远程）。
  - How to configure the MCP client (Claude Desktop example for local) or agent runtime for remote.
  - 如何配置 MCP 客户端（本地模式以 Claude Desktop 为例）或远程模式的智能体运行环境。
  - Tool reference: names, parameters, example inputs/outputs, and expected behaviors.
  - 工具参考指南：名称、参数、示例输入/输出以及预期行为。

## Evaluation rubric (90 pts total)
## 评估标准（总分 90 分）
- Functionality (35): Implements 2+ tools, correct API integration, meaningful outputs.
- 功能性 (35分)：实现 2 个以上工具，正确的 API 集成，有意义的输出。
- Reliability (20): Input validation, error handling, logging, rate-limit awareness.
- 可靠性 (20分)：输入验证、错误处理、日志记录、速率限制意识。
- Developer experience (20): Clear setup/docs, easy to run locally; sensible folder structure.
- 开发者体验 (20分)：清晰的设置/文档，在本地容易运行；合理的文件夹结构。
- Code quality (15): Readable code, descriptive names, minimal complexity, type hints where applicable.
- 代码质量 (15分)：可读的代码，描述性的命名，最小化复杂性，在适用处使用类型提示。
- Extra credit (10):
- 额外加分 (10分)：
  - +5 Remote HTTP MCP server, callable by an agent/client such as the OpenAI/Claude SDK.
  - +5分：远程 HTTP MCP 服务器，可被诸如 OpenAI/Claude SDK 之类的智能体/客户端调用。
  - +5 Auth implemented correctly (API key or OAuth2 with audience validation).
  - +5分：正确实现了身份验证（API 密钥或带有受众验证的 OAuth2）。

## Helpful references
## 有用的参考资料
- MCP Server Quickstart: [modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server). 
- MCP 服务器快速入门：[modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)。
*NOTE: You may not submit this exact example.*
*注意：你不可以直接提交这个完全一样的示例代码。*
- MCP Authorization (HTTP): [modelcontextprotocol.io/specification/2025-06-18/basic/authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- MCP 授权 (HTTP)：[modelcontextprotocol.io/specification/2025-06-18/basic/authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- Remote MCP on Cloudflare (Agents): [developers.cloudflare.com/agents/guides/remote-mcp-server/](https://developers.cloudflare.com/agents/guides/remote-mcp-server/). Use the modelcontextprotocol inspector tool to debug your server locally before deploying.
- Cloudflare 上的远程 MCP (Agents)：[developers.cloudflare.com/agents/guides/remote-mcp-server/](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)。在部署之前，使用 modelcontextprotocol 的检查器工具在本地调试你的服务器。
- https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel If you choose to do a remote MCP deployment, Vercel is a good option with a free tier. 
- https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel 如果你选择进行远程 MCP 部署，Vercel 是一个很好的选择，它提供免费套餐。