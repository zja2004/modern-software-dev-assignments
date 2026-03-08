import os
import re
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

# TODO: 填在这里！
YOUR_SYSTEM_PROMPT = ""


USER_PROMPT = """
解决这个问题，然后在最后一行给出最终答案，格式为 "Answer: <number>"。

3^{12345} (mod 100) 是多少？
"""


# 对于这个简单的例子，我们只期待最终的数字答案
EXPECTED_OUTPUT = "Answer: 43"


def extract_final_answer(text: str) -> str:
    """从详细的推理轨迹中提取最后的 'Answer: ...' 行。

    - 查找以 'Answer:' 开头的最后一行（不区分大小写）
    - 当存在数字时，规范化为 'Answer: <number>'
    - 如果未检测到数字，则退回返回匹配的内容
    """
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    if matches:
        value = matches[-1].strip()
        # 尽可能倾向于数字标准化（支持整数/小数）
        num_match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
        if num_match:
            return f"Answer: {num_match.group(0)}"
        return f"Answer: {value}"
    return text.strip()


def test_your_prompt(system_prompt: str) -> bool:
    """运行最多 NUM_RUNS_TIMES 次，如果任何输出与 EXPECTED_OUTPUT 匹配，则返回 True。

    找到匹配项时打印 "SUCCESS"。
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.3},
        )
        output_text = response.message.content
        final_answer = extract_final_answer(output_text)
        if final_answer.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {final_answer}")
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)


