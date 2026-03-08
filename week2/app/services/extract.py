from __future__ import annotations

import os
import re
from typing import Any
import json
from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

BULLET_PREFIX_PATTERN = re.compile(r"^\s*([-*•]|\d+\.)\s+")
KEYWORD_PREFIXES = (
    "todo:",
    "action:",
    "next:",
)


def _is_action_line(line: str) -> bool:
    stripped = line.strip().lower()
    if not stripped:
        return False
    if BULLET_PREFIX_PATTERN.match(stripped):
        return True
    if any(stripped.startswith(prefix) for prefix in KEYWORD_PREFIXES):
        return True
    if "[ ]" in stripped or "[todo]" in stripped:
        return True
    return False


def extract_action_items(text: str) -> List[str]:
    lines = text.splitlines()
    extracted: List[str] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if _is_action_line(line):
            cleaned = BULLET_PREFIX_PATTERN.sub("", line)
            cleaned = cleaned.strip()
            # Trim common checkbox markers
            # 移除常见的复选框标记
            cleaned = cleaned.removeprefix("[ ]").strip()
            cleaned = cleaned.removeprefix("[todo]").strip()
            extracted.append(cleaned)
    # Fallback: if nothing matched, heuristically split into sentences and pick imperative-like ones
    # 退回方案：如果没有任何匹配项，基于启发式算法切割为句子，并挑选出类似祈使句的句子
    if not extracted:
        sentences = re.split(r"(?<=[.!?])\s+", text.strip())
        for sentence in sentences:
            s = sentence.strip()
            if not s:
                continue
            if _looks_imperative(s):
                extracted.append(s)
    # Deduplicate while preserving order
    # 在保留顺序的同时去重
    seen: set[str] = set()
    unique: List[str] = []
    for item in extracted:
        lowered = item.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        unique.append(item)
    return unique


class ActionItemsSchema(BaseModel):
    items: List[str]


def extract_action_items_llm(text: str) -> List[str]:
    """
    TODO 1: Extract action items using a Large Language Model (Gemini).
    """
    if not text.strip():
        return []

    system_prompt = """
You are an expert action item extractor.
Given the following meeting notes or text, extract all actionable tasks, to-dos, or assignments.
Ignore general narrative sentences.
Return ONLY a strictly formatted JSON object with a single key "items" that maps to a list of strings.
Example output format:
{
  "items": [
    "Set up the database",
    "Email the client for feedback"
  ]
}
"""
    
    # Use API key directly from user request, or fallback to environment variable
    api_key = os.environ.get("MOONSHOT_API_KEY", "sk-WDqyiDQEfroOwfEfDlIyMCf4mpIyFzGQtuZYyz2bjifP8J43") 
    
    try:
        # Initialize the client using Moonshot API settings
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.moonshot.cn/v1",
        )
        
        response = client.chat.completions.create(
            model='kimi-k2-turbo-preview',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )

        content = response.choices[0].message.content
        if not content:
            return []
            
        data = json.loads(content)
        return data.get("items", [])
    except Exception as e:
        print(f"LLM extraction error: {e}")
        # Fallback to the heuristic rules if LLM fails
        return extract_action_items(text)



def _looks_imperative(sentence: str) -> bool:
    words = re.findall(r"[A-Za-z']+", sentence)
    if not words:
        return False
    first = words[0]
    # Crude heuristic: treat these as imperative starters
    # 粗略的启发式：将这些词视作祈使句的开头
    imperative_starters = {
        "add",
        "create",
        "implement",
        "fix",
        "update",
        "write",
        "check",
        "verify",
        "refactor",
        "document",
        "design",
        "investigate",
    }
    return first.lower() in imperative_starters
