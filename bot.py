from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram import F
import logging

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен бота
BOT_TOKEN = "7776746101:AAGfbpUlNxF6ZAnyjXnXWiFZFxUPjeDoFZY"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создание кнопки для запуска мини-приложения
start_button = InlineKeyboardButton(
    text="Играть",
    web_app=types.WebAppInfo(url="http://127.0.0.1:5000")  # URL вашего мини-приложения
)

# Создание клавиатуры с кнопкой
start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[start_button]])

# Стартовая команда
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Привет! Добро пожаловать в KitHome.\nНажмите на кнопку ниже, чтобы начать игру.",
        reply_markup=start_keyboard
    )

# Асинхронный запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
