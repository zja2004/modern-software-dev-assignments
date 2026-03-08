# Week 2 Write-up
# 第二周 实验报告 (Write-up)

Tip: To preview this markdown file
提示：要预览此 Markdown 文件
- On Mac, press `Command (⌘) + Shift + V`
- 在 Mac 上，按 `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`
- 在 Windows/Linux 上，按 `Ctrl + Shift + V`

## INSTRUCTIONS
## 说明

Fill out all of the `TODO`s in this file.
填写此文件中的所有 `TODO` 项。

## SUBMISSION DETAILS
## 提交详情

Name: **<Your Name>** \
姓名：**<你的名字>** \
SUNet ID: **<Your SUNet ID>** \
学号/SUNet ID: **<你的学号>** \
Citations: **None (Completed via Agent)**
引用：**无（由智能体协助完成）**
引用：**TODO**

This assignment took me about **1** hours to do. 
完成这项作业大约花了我 **1** 个小时。


## YOUR RESPONSES
## 你的回答
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.
对于每个练习，除了说明生成的代码所在位置之外，请包含你用来生成答案的提示词 (prompts)。确保在你的代码中清楚地添加注释，以记录哪些部分是由 AI 生成的。

### Exercise 1: Scaffold a New Feature
### 练习 1：搭建一个新功能框架

Prompt: 
提示词：
```
"Please implement an extract_action_items_llm function in app/services/extract.py using the google-genai library and Gemini 2.5 Flash model instead of Ollama. It should take the text and return a List[str] containing extracted items using Structured Outputs."
``` 

Generated Code Snippets:
生成的代码片段：
```
app/services/extract.py: 
Lines 68-115 (Added ActionItemsSchema and extract_action_items_llm)
```

### Exercise 2: Add Unit Tests
### 练习 2：添加单元测试

Prompt: 
提示词：
```
"Write unit tests for the new extract_action_items_llm function using pytest in tests/test_extract.py. Mock the genai.Client so it doesn't make real API calls, and cover cases for bullet points, empty input, and fallback mechanism."
``` 

Generated Code Snippets:
生成的代码片段：
```
tests/test_extract.py:
Lines 23-64 (Added mock tests for success, empty input, and exception fallback)
```

### Exercise 3: Refactor Existing Code for Clarity
### 练习 3：重构现有代码以提高清晰度

Prompt: 
提示词：
```
"Refactor the app/db.py to add Pydantic schemas (Note and ActionItem). Update notes.py and action_items.py routers to use these explicit Pydantic response models instead of returning raw Dicts, improving clarity and API contract."
``` 

Generated/Modified Code Snippets:
生成/修改的代码片段：
```
app/db.py: Lines 14-25 (Added Pydantic Schemas), Lines 80-123 (Updated return types to Schema models)
app/routers/notes.py: Lines 9-16 (Added Pydantic schemas), Lines 20-43 (Updated endpoints to use response_model)
app/routers/action_items.py: Lines 6-27 (Added Pydantic schemas), Lines 33-66 (Refactored payload requests and router response models)
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
### 练习 4：使用智能体模式自动执行小任务

Prompt: 
提示词：
```
"Create a new endpoint `/action-items/extract-llm` in action_items.py. Then, edit frontend/index.html to add an 'Extract LLM' button and a 'List Notes' button. Hook them up to fetch and display data using Vanilla JS."
``` 

Generated Code Snippets:
生成的代码片段：
```
app/routers/notes.py: Lines 33-36 (Added /notes GET endpoint)
app/routers/action_items.py: Lines 47-59 (Added /action-items/extract-llm endpoint)
frontend/index.html: Lines 27-28 (Added LLM button), Lines 31-35 (Added List Notes UI), Lines 69-128 (Added JS listeners for the two new buttons)
```


### Exercise 5: Generate a README from the Codebase
### 练习 5：从代码库生成说明文件 (README)

Prompt: 
提示词：
```
"Generate a README.md explaining the Action Item Extractor project, describing its features, how to set it up (including setting up GEMINI_API_KEY), the API endpoints (including the new LLM extraction), and how to run pytest."
``` 

Generated Code Snippets:
生成的代码片段：
```
README.md:
Lines 1-61 (Entire file generated)
```


## SUBMISSION INSTRUCTIONS
## 提交说明
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
1. 按下 `Command (⌘) + F`（或 `Ctrl + F`）来查找此文件中是否还有遗留下来的 `TODO`。如果没有找到结果，恭喜你——你已经完成了所有必填项。
2. Make sure you have all changes pushed to your remote repository for grading.
2. 确保你已将所有更改推送到你的远程仓库以供评分。
3. Submit via Gradescope. 
3. 通过 Gradescope 进行提交。