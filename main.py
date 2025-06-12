import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN
from gpt_client import ask_chatgpt
from gemini_client import ask_gemini  # Предполагается, что тоже async

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Я бот с поддержкой GPT и Gemini.\n"
        "Используй команды:\n"
        "/gpt Текст запроса — для ChatGPT (GPT-3.5 бесплатно)\n"
        "/gemini Текст запроса — для Gemini (имитация ответа)\n"
        "Пример:\n/gpt Расскажи анекдот"
    )



async def process_prompt(message: types.Message, model_func, model_name):
    prompt = message.text.partition(' ')[2].strip()
    if not prompt:
        await message.answer(f"❌ Пожалуйста, введите текст после команды /{model_name.lower()}.")
        return
    await message.answer(f"⏳ Обрабатываю запрос через {model_name}...")
    try:
        reply = await model_func(prompt)
    except Exception as e:
        logging.error(f"Ошибка при запросе к {model_name}: {e}")
        await message.answer(f"❌ Ошибка при обработке запроса к {model_name}. Попробуйте позже.")
        return

    # Разбиваем очень длинный ответ на части по 4000 символов
    for i in range(0, len(reply), 4000):
        await message.answer(f"💬 Ответ от {model_name}:\n\n{reply[i:i + 4000]}")


@dp.message(Command("gpt"))
async def gpt_cmd(message: types.Message):
    await process_prompt(message, ask_chatgpt, "GPT")


@dp.message(Command("gemini"))
async def gemini_cmd(message: types.Message):
    await process_prompt(message, ask_gemini, "Gemini")


@dp.message()
async def fallback(message: types.Message):
    await message.answer(
        "Используйте команды /gpt или /gemini перед сообщением.\n"
        "Например:\n/gpt Что ты умеешь?\n/gemini Привет!"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
