import logging
from openai import OpenAI
from config import OPENAI_API_KEY

logging.basicConfig(level=logging.DEBUG)

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_chatgpt(prompt: str) -> str:
    logging.debug(f"Запрос к GPT: {prompt}")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=700,
        )
        logging.debug(f"Ответ от GPT: {response}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Ошибка GPT: {e}", exc_info=True)
        return f"❌ Ошибка GPT: {e}"
