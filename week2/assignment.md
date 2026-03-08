# Week 2 – Action Item Extractor
# 第二周 – 行动项提取器

This week, we will be expanding upon a minimal FastAPI + SQLite app that converts free‑form notes into enumerated action items.
本周，我们将对一个简易的 FastAPI + SQLite 应用程序进行扩展，该程序能将自由格式的笔记转换为逐条列出的行动项。

***We recommend reading this entire document before getting started.***
***我们建议在开始之前阅读整份文档。***

Tip: To preview this markdown file
提示：要预览此 Markdown 文件
- On Mac, press `Command (⌘) + Shift + V`
- 在 Mac 上，按 `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`
- 在 Windows/Linux 上，按 `Ctrl + Shift + V`

## Getting Started
## 准备开始

### Cursor Set Up
### Cursor 设置
Follow these instructions to set up Cursor and open your project:
按照以下说明设置 Cursor 并打开你的项目：
1. Redeem your free year of Cursor Pro: https://cursor.com/students
1. 兑换你的 Cursor Pro 一年免费试用：https://cursor.com/students
2. Download Cursor: https://cursor.com/download
2. 下载 Cursor：https://cursor.com/download
3. To enable the Cursor command line tool, open Cursor and press `Command (⌘) + Shift+ P` for Mac users (or `Ctrl + Shift + P` for non-Mac users) to open the Command Palette. Type: `Shell Command: Install 'cursor' command`. Select it and hit Enter.
3. 要启用 Cursor 命令行工具，请打开 Cursor，Mac 用户按 `Command (⌘) + Shift+ P`（非 Mac 用户按 `Ctrl + Shift + P`）打开命令面板。输入：`Shell Command: Install 'cursor' command`。选择它并按回车 (Enter)。
4. Open a new terminal window, navigate to your project root, and run: `cursor .`
4. 打开一个新的终端窗口，进入你的项目根目录，然后运行：`cursor .`

### Current Application
### 当前的应用程序
Here's how you can start running the current starter application: 
下面是启动运行当前初始应用程序的方法：
1. Activate your conda environment.
1. 激活你的 conda 环境。
```bash
conda activate cs146s 
```
2. From the project root, run the server:
2. 在项目根目录下，运行服务器：
```bash
poetry run uvicorn week2.app.main:app --reload
```
3. Open a web browser and navigate to http://127.0.0.1:8000/.
3. 打开 Web 浏览器并访问 http://127.0.0.1:8000/。
4. Familiarize yourself with the current state of the application. Make sure you can successfully input notes and produce the extracted action item checklist. 
4. 熟悉应用程序的当前状态。确保你能够成功地输入笔记，并生成提取出的行动项检查表。

## Exercises
## 练习
For each exercise, use Cursor to help you implement the specified improvements to the current action item extractor application.
对于每一个练习，请使用 Cursor 协助你对当前的行动项提取器应用程序实现指定的改进。

As you work through the assignment, use `writeup.md` to document your progress. Be sure to include the prompts you use, as well as any changes made by you or Cursor. We will be grading based on the contents of the write-up. Please also include comments throughout your code to document your changes. 
在完成作业的过程中，请使用 `writeup.md` 记录你的进度。确保包含你所使用的提示词 (prompts)，以及由你或 Cursor 所做的任何更改。我们将根据 write-up (实验报告) 的内容进行评分。也请在整个代码中包含注释以记录你的更改。

### TODO 1: Scaffold a New Feature
### 练习 1：搭建一个新功能框架

Analyze the existing `extract_action_items()` function in `week2/app/services/extract.py`, which currently extracts action items using predefined heuristics.
分析 `week2/app/services/extract.py` 中现有的 `extract_action_items()` 函数，该函数当前使用预定义的启发式规则提取行动项。

Your task is to implement an **LLM-powered** alternative, `extract_action_items_llm()`, that utilizes Ollama to perform action item extraction via a large language model.
你的任务是实现一个由 **大语言模型 (LLM) 驱动** 的替代方案 `extract_action_items_llm()`，它利用 Ollama 通过大模型来进行行动项提取。

Some tips:
一些提示：
- To produce structured outputs (i.e. JSON array of strings), refer to this documentation: https://ollama.com/blog/structured-outputs 
- 要生成结构化的输出（即字符串的 JSON 数组），请参阅此文档：https://ollama.com/blog/structured-outputs 
- To browse available Ollama models, refer to this documentation: https://ollama.com/library. Note that larger models will be more resource-intensive, so start small. To pull and run a model: `ollama run {MODEL_NAME}`
- 若要浏览可用的 Ollama 模型，请参阅此文档：https://ollama.com/library。请注意，更大的模型将更加耗费资源，所以请从小的模型开始。拉取并运行命令：`ollama run {MODEL_NAME}`

### TODO 2: Add Unit Tests 
### 练习 2：添加单元测试

Write unit tests for `extract_action_items_llm()` covering multiple inputs (e.g., bullet lists, keyword-prefixed lines, empty input) in `week2/tests/test_extract.py`.
编写 `extract_action_items_llm()` 的单元测试，涵盖多种输入（例如，项目符号列表、关键字前缀行、空输入），并将其写在 `week2/tests/test_extract.py` 中。

### TODO 3: Refactor Existing Code for Clarity
### 练习 3：重构现有代码以提高清晰度

Perform a refactor of the code in the backend, focusing in particular on well-defined API contracts/schemas, database layer cleanup, app lifecycle/configuration, error handling. 
对后端代码进行重构，尤其要注意明确的 API 契约/模式 (contracts/schemas)、数据库层的清理、应用程序生命周期/配置，以及错误处理。

### TODO 4: Use Agentic Mode to Automate Small Tasks
### 练习 4：使用智能体模式 (Agentic Mode) 自动执行小任务

1. Integrate the LLM-powered extraction as a new endpoint. Update the frontend to include an "Extract LLM" button that, when clicked, triggers the extraction process via the new endpoint.
1. 将基于 LLM 的提取功能集成作为一个新的 API 端点 (endpoint)。更新前端以包含一个 "Extract LLM" 按钮，点击后将通过新端点触发提取进程。

2. Expose one final endpoint to retrieve all notes. Update the frontend to include a "List Notes" button that, when clicked, fetches and displays them.
2. 暴露最后一个端点用于检索所有的笔记。更新前端以包含一个 "List Notes" 按钮，点击后将抓取并显示它们。

### TODO 5: Generate a README from the Codebase
### 练习 5：从代码库生成说明文件 (README)

***Learning Goal:***
***学习目标：***
*Students learn how AI can introspect a codebase and produce documentation automatically, showcasing Cursor’s ability to parse code context and translate it into human‑readable form.*
*学生学习 AI 如何内省 (introspect) 代码库并自动生成文档，这展示了 Cursor 解析代码上下文并将其转换为人类可读形式的能力。*

Use Cursor to analyze the current codebase and generate a well-structured `README.md` file. The README should include, at a minimum:
使用 Cursor 分析当前的代码库，并生成一个结构良好的 `README.md` 文件。README 至少应包含：
- A brief overview of the project
- 项目的简要概述
- How to set up and run the project
- 如何设置和运行该项目
- API endpoints and functionality
- API 端点及其功能
- Instructions for running the test suite
- 运行测试套件的说明

## Deliverables
## 交付物
Fill out `week2/writeup.md` according to the instructions provided. Make sure all your changes are documented in your codebase. 
根据提供的说明填写 `week2/writeup.md`。确保代码库记录了你的所有修改。

## Evaluation rubric (100 pts total)
## 评分标准 (总分 100 分)
- 20 points per part 1-5 (10 for the generated code and 10 for each prompt).
- 第 1 到 5 部分各 20 分 (10 分给生成的代码，10 分给每一个提示词)。