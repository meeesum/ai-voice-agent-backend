# test_env.py
from app.config import settings

print("OpenAI Key:", settings.OPENAI_API_KEY[:5] + "...")
print("Retell Key:", settings.RETELL_API_KEY[:5] + "...")
