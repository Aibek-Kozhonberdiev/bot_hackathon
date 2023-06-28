import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from main import Botrecord

load_dotenv()

telegram_key = os.getenv('API_KEY') 
admin = os.getenv('ADMIN')
bot = Bot(token=telegram_key)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('/help - 🆘Instruction🆘'))
    await message.answer(text=Botrecord().text_welcome(), reply_markup=kb)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("🤖/start - Welcome🤖\n🆘/help - Instruction🆘\n🌐/language - language🌐")

@dp.message_handler(commands=['language'])
async def weather_in(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text='English🇺🇸', callback_data='btn1')
    btn2 = InlineKeyboardButton(text='Русский🇷🇺', callback_data='btn2')
    btn3 = InlineKeyboardButton(text='Кыргызча🇰🇬', callback_data='btn3')
    kb.add(btn1, btn2, btn3)
    await message.answer('🌐Choose language:🌐', reply_markup=kb)

@dp.callback_query_handler()
async def check_callback_data(callback: types.CallbackQuery):
    await callback.answer(text="aaa")
    print(callback.data)

@dp.message_handler(commands=['bot'])
async def send_bot(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text=Botrecord())

@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    sent_message = await message.answer("⌛️The request will take some time to process.⌛️")
    await message.answer()
    await bot.delete_message(message.chat.id, sent_message.message_id)

@dp.message_handler(content_types=ContentTypes.ANY)
async def send_all(message: types.Message):
    await message.answer("💤The bot does not process such a message!💤")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)