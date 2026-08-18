assistant = {
    "name": "AI助手",
    "model": "DeepSeek",
    "language": "中文",
    "version": 1
}

print("助手名称：", assistant["name"])
print("使用模型：", assistant["model"])
print("语言：", assistant["language"])
print("版本：", assistant["version"])
assistant["version"] = 2

print("更新后的版本：", assistant["version"])