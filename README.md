Telegram GPT+Gemini Bot

Описание:
Телеграм-бот, который принимает сообщения с командами /gpt или /gemini, отправляет их в соответствующие модели и возвращает ответ.

Запуск:

1. Создай и активируй виртуальное окружение:
   python -m venv venv
   source venv/bin/activate  # или venv\Scripts\activate для Windows

2. Установи зависимости:
   pip install -r requirements.txt

3. Внеси свои ключи в config.py:
   - OPENAI_API_KEY
   - GEMINI_API_KEY
   - BOT_TOKEN

4. Запусти бота:
   python main.py

5. Пиши в Telegram /gpt Текст или /gemini Текст

Стек:
- Python 3.10+
- aiogram
- openai
- google-generativeai

---

Что можно добавить позже:
- Логирование сообщений в базу или CSV
- Выбор модели через inline-кнопки
- Ответы обоих моделей сразу
- Рейтинг ответов ("что понравилось больше?")
