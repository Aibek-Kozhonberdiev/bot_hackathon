# Libraries Imported
from aiogram import executor, types 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, bot, welcome_message, ADMIN
from bard_create import bard_chat
from sql_data import sqldata, userlanguage, conclusion, resulttext

# This function is a message handler for the /start command. When users send /start to the bot, this function will be triggered.
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('/help - Instruction'))
    await sqldata(message)
    await message.answer(text=welcome_message, reply_markup=kb)

# This function is a message handler for the /help command. When users send /help to the bot, this function will be triggered.
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    result = await resulttext(message.from_user.id, "help")
    await message.answer(result)

# This function is a message handler for the /instruction command. When users send /instruction to the bot, this function will be triggered.
@dp.message_handler(commands=['instruction'])
async def send_instruction(message: types.Message):
    result = await resulttext(message.from_user.id, "instruction")
    await message.answer(result)

# This function is a message handler for the /language command. When users send /language to the bot, this function will be triggered.
@dp.message_handler(commands=['language'])
async def weather_in(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text='English🇺🇸', callback_data='en')
    btn2 = InlineKeyboardButton(text='Русский🇷🇺', callback_data='ru')
    btn3 = InlineKeyboardButton(text='Кыргызча🇰🇬', callback_data='kg')
    kb.add(btn1, btn2, btn3)
    result = await resulttext(message.from_user.id, "Choose")
    await message.answer(result, reply_markup=kb)

# This function is a callback query handler. It handles the user's response to the language selection keyboard.
@dp.callback_query_handler()
async def check_callback_data(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await userlanguage(user_id, callback.data)
    if callback.data == "en":
        await callback.answer("Language changed successfully")
    elif callback.data == "ru":
        await callback.answer("Язык успешно изменен")
    else:
        await callback.answer("Тил ийгиликтүү өзгөртүлдү")

# It sends the bot's conclusion message to the admin user.
@dp.message_handler(commands=['bot'])
async def send_bot(message: types.Message):
    if message.from_user.id == int(ADMIN):
        result = await conclusion()
        await message.answer(result)

# It sends a loading message to the user, processes the user's text input using the Bard_create module, and sends the result back to the user.
@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    loading = await resulttext(message.from_user.id, 'loading')
    sent_message = await message.answer(f"⌛️{loading}⌛️")
    result = await bard_chat(message.text)
    await message.answer(result)
    await bot.delete_message(message.chat.id, sent_message.message_id)

# It sends an error message to the user based on their preferred language.
@dp.message_handler(content_types=ContentTypes.ANY)
async def send_all(message: types.Message):
    result = await resulttext(message.from_user.id, 'error')
    await message.answer(f"💤{result}💤")

# This block is executed only if the script is run directly (not imported as a module).
# skip_updates=True indicates that the bot should skip any pending updates when it starts.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)