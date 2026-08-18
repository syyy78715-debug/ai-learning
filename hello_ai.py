import requests

response = requests.get("https://api.github.com")

print("状态码：", response.status_code)

data = response.json()

print("GitHub API 返回的数据类型：", type(data))
print("GitHub API 数据类型：", type(data))
print("GitHub API 地址：", data["current_user_url"])