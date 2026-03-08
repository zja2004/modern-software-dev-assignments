import os
import re
from typing import List, Callable
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

DATA_FILES: List[str] = [
    os.path.join(os.path.dirname(__file__), "data", "api_docs.txt"),
]


def load_corpus_from_files(paths: List[str]) -> List[str]:
    corpus: List[str] = []
    for p in paths:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    corpus.append(f.read())
            except Exception as exc:
                corpus.append(f"[load_error] {p}: {exc}")
        else:
            corpus.append(f"[missing_file] {p}")
    return corpus


# 从外部文件加载语料库（简单的 API 文档）。如果缺失，回退到内联片段
CORPUS: List[str] = load_corpus_from_files(DATA_FILES)

QUESTION = (
    "编写一个 Python 函数 `fetch_user_name(user_id: str, api_key: str) -> str`，调用文档中的 API "
    "通过 id 获取用户，并仅以字符串形式返回用户的名字。"
)


# TODO: 填在这里！
YOUR_SYSTEM_PROMPT = ""


# 对于这个简单例子
# 对于这个编码任务，通过必需的代码片段进行验证，而不是完全相同的字符串
REQUIRED_SNIPPETS = [
    "def fetch_user_name(",
    "requests.get",
    "/users/",
    "X-API-Key",
    "return",
]


def YOUR_CONTEXT_PROVIDER(corpus: List[str]) -> List[str]:
    """TODO: 从 CORPUS 中选择并返回与此任务相关的文档子集。

    例如，返回 [] 以模拟缺少上下文，或返回 [corpus[0]] 以包含 API 文档。
    """
    return []


def make_user_prompt(question: str, context_docs: List[str]) -> str:
    if context_docs:
        context_block = "\n".join(f"- {d}" for d in context_docs)
    else:
        context_block = "(no context provided)"
    return (
        f"Context (仅使用此信息):\n{context_block}\n\n"
        f"Task: {question}\n\n"
        "Requirements:\n"
        "- 使用文档中说明的 Base URL 和端点 (endpoint)。\n"
        "- 发送文档中说明的认证请求头 (authentication header)。\n"
        "- 如果响应不是 200，则抛出异常 (Raise)。\n"
        "- 只返回用户的名字字符串。\n\n"
        "Output: 一个包含函数和必要导入 (imports) 的单独的被代码块包围的 Python 代码块。\n"
    )


def extract_code_block(text: str) -> str:
    """提取最后一个带有围栏的 Python 代码块，或任何带有围栏的代码块，否则返回文本。"""
    # 首先尝试 ```python ... ```
    m = re.findall(r"```python\n([\s\S]*?)```", text, flags=re.IGNORECASE)
    if m:
        return m[-1].strip()
    # 回退到任何带有围栏的代码块
    m = re.findall(r"```\n([\s\S]*?)```", text)
    if m:
        return m[-1].strip()
    return text.strip()


def test_your_prompt(system_prompt: str, context_provider: Callable[[List[str]], List[str]]) -> bool:
    """运行最多 NUM_RUNS_TIMES 次，如果任何输出与 EXPECTED_OUTPUT 匹配，则返回 True。"""
    context_docs = context_provider(CORPUS)
    user_prompt = make_user_prompt(QUESTION, context_docs)

    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            options={"temperature": 0.0},
        )
        output_text = response.message.content
        code = extract_code_block(output_text)
        missing = [s for s in REQUIRED_SNIPPETS if s not in code]
        if not missing:
            print(output_text)
            print("SUCCESS")
            return True
        else:
            print("Missing required snippets:")
            for s in missing:
                print(f"  - {s}")
            print("Generated code:\n" + code)
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT, YOUR_CONTEXT_PROVIDER)
