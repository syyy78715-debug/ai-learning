from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("AI_API_KEY")

print("API Key 已读取：", api_key)