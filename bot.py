import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from main import *

load_dotenv()

telegram_key = os.getenv('API_KEY')
bot = Bot(token=telegram_key)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton('/help - Инструкция'))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Приветствие', reply_markup=kb)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("/start - Приветствие\n/help - Инструкция\n/setting - Настройка")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)