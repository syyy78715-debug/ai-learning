import json

messages = [
    {
        "role": "user",
        "content": "你好，请介绍一下人工智能。"
    },
    {
        "role": "assistant",
        "content": "人工智能是一种让计算机执行需要智能能力任务的技术。"
    }
]

json_data = json.dumps(messages, ensure_ascii=False, indent=2)

print(json_data)