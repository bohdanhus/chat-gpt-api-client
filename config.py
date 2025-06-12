from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not all([OPENAI_API_KEY, GEMINI_API_KEY, BOT_TOKEN]):
    raise EnvironmentError("Missing one or more environment variables: OPENAI_API_KEY, GEMINI_API_KEY, BOT_TOKEN")
