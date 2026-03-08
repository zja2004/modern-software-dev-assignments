# 第一周 — 提示词技巧 (Prompting Techniques)

你将通过编写提示词来完成特定任务，以此练习多种提示词技巧。每个任务的说明都位于其对应源文件的顶部。

## 安装指南
确保你已经首先完成了顶层 `README.md` 中描述的安装步骤。

## Ollama 安装
我们将使用一个名为 [Ollama](https://ollama.com/) 的工具，在你的本地机器上运行不同的最先进的大语言模型 (LLMs)。请使用以下方法之一进行安装：

- macOS (Homebrew):
  ```bash
  brew install --cask ollama 
  ollama serve
  ```

- Linux (推荐):
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- Windows:
  从 [ollama.com/download](https://ollama.com/download) 下载并运行安装程序。

验证安装：
```bash
ollama -v
```

在运行测试脚本之前，请确保你已经拉取了以下模型。你只需要执行一次此操作即可（除非你之后删除了这些模型）：
```bash
ollama run mistral-nemo:12b
ollama run llama3.1:8b
```

## 技巧与源文件
- K-shot 提示词 (K-shot prompting) — `week1/k_shot_prompting.py`
- 思维链 (Chain-of-thought) — `week1/chain_of_thought.py`
- 工具调用 (Tool calling) — `week1/tool_calling.py`
- 自洽性提示词 (Self-consistency prompting) — `week1/self_consistency_prompting.py`
- RAG (检索增强生成) — `week1/rag.py`
- 反思 (Reflexion) — `week1/reflexion.py`

## 交付物
- 阅读每份文件中的任务描述。
- 设计并运行提示词（寻找代码中所有标记为 `TODO` 的地方）。那应该是你唯一需要修改的地方（即不要改动模型本身）。
- 迭代改进结果，直到测试脚本通过。
- 保存你为每种技巧最终确定的提示词和输出结果。
- 请确保在提交的作业中包含每种提示词技巧文件已完成代码。***务必仔细检查所有的 `TODO` 都已解决。***

## 评分标准 (总分 60 分)
- 6 种不同的提示词技巧，每个完成的提示词 10 分