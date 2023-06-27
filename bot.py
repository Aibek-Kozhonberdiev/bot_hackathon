import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentTypes
from dotenv import load_dotenv
from main import BotText

load_dotenv()

telegram_key = os.getenv('API_KEY') 
bot = Bot(token=telegram_key)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('/help - Instruction'))
    await message.answer(text=BotText().text_welcome(), reply_markup=kb)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("/start - Welcome\n/help - Instruction\n/language - language")

@dp.message_handler(commands=['language'])
async def send_language(message: types.Message):
    pass

@dp.message_handler(content_types=['voice'])
async def send_audio(message: types.Message):
    pass

@dp.message_handler(content_types=['photo'])
async def send_photo(message: types.Message):
    pass

@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    pass

@dp.message_handler(content_types=ContentTypes.ANY)
async def send_all(message: types.Message):
    await message.answer("The bot does not process such a message!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)