import json

json_text = '''
{
    "model": "AI助手",
    "question": "什么是人工智能？",
    "answer": "人工智能是让计算机执行需要智能能力任务的技术。"
}
'''

data = json.loads(json_text)

print("模型：", data["model"])
print("问题：", data["question"])
print("回答：", data["answer"])