# Action Item Extractor (Week 2)

这个项目是 Stanford 现代软件开发课程的第二周作业：**Action Item Extractor**。
它是一个基于 FastAPI + SQLite 搭建的轻量级 Web 服务，主要功能是将用户提供的任意长文本（例如会议记录、头脑风暴笔记）提取为结构化的待办事项（Action Items）清单。

## 项目概述
本项目在原有（基于正则表达式的启发式提取）实现的基础之上，集成了大语言模型能力（默认使用了 Gemini API），使其能够进行具有上下文语义理解能力的智能行动项提取。

包含的主要功能有：
- **存入笔记**：接收任意长文本作为笔记并保存。
- **列出笔记**：可以拉取查看过往存储在 SQLite 数据库中的所有历史笔记。
- **启发式提取**（可选）：通过简单的关键字规则（例如以 `- [ ]` 或 `TODO:` 开头）来摘取笔记中的任务。
- **LLM 智能提取**：集成 Google GenAI (Gemini) API，能够自动识别笔记中的叙述并在忽略它们的基础上，只抽出核心待办任务并结构化输出。
- **任务状态追踪**：对提取出来的任务可以直接进行勾选完成操作。

## 如何设置与运行

由于本项目集成了 Google Gemini 的大模型能力，你需要先准备好对应的 API Key。

1. **环境准备**
建议你使用 `conda` 创建隔离环境，或者直接通过项目的 `poetry` 进行依赖安装：
```bash
pip install -r requirements.txt
# 或者如果你有诗歌环境：
poetry install
```
确保你也安装了以下运行时所需的关键库：
```bash
pip install fastapi uvicorn sqlite3 pydantic google-genai python-dotenv pytest
```

2. **配置环境变量**
在项目的根目录下创建一个 `.env` 文件，并填入你的 Gemini API Key：
```bash
GEMINI_API_KEY="your-api-key-here"
```

3. **启动服务**
在项目根目录运行以下命令来启动后端 FastAPI 服务器：
```bash
poetry run uvicorn week2.app.main:app --reload
# 如果没装 poetry：
python -m uvicorn week2.app.main:app --reload
```
服务将在 `http://127.0.0.1:8000/` 本地启动。你可以直接打开浏览器访问该地址，即可看到并测试我们准备好的 HTML 测试前端页。

## API 端点及其功能

### `GET /`
- 渲染根路径，返回一个简洁的 HTML 界面供用户交互。

### 注意：`/notes` 组
主要负责处理用户的原始笔记文本记录。
- **`POST /notes`**
    - 创建一条新的文本笔记存储到数据库。
- **`GET /notes`**
    - `[新增功能]` 拉取全量的过往笔记列表。
- **`GET /notes/{note_id}`**
    - 根据指定的 `note_id` 拉取单独某条笔记。

### 注意：`/action-items` 组
主要负责“提取待办任务”逻辑以及“勾选”逻辑。
- **`GET /action-items`**
    - 拉取所有待办任务，也可以传入 `note_id` 查询具体某条笔记关联的 Action Items。
- **`POST /action-items/{action_item_id}/done`**
    - 变更某个指定的 action item 的完成状态。
- **`POST /action-items/extract`**
    - 【旧版入口】使用启发式规则提取传入的文本，如果有必要可以一拍保存。
- **`POST /action-items/extract-llm`**
    - `[新增功能]` 这次重构作业的新入口。调用 Gemini API 大语言模型能力智能分析文本并提取 Action Items，返回结构化 JSON 格式数据。

## 运行测试套件的说明

测试全部被包含在 `week2/tests/` 文件夹内，你可以直接通过内置的 `pytest` 命令执行测试以验证包括大模型 Fallback 情况在内的业务逻辑是否健壮：

```bash
python -m pytest week2/tests/
```
如果能够打印 `PASSED` 便说明单元测试运行通过。
