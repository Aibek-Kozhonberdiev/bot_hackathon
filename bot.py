from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton
from bot_create import dp, bot, welcome_message, ADMIN
from bard_create import Bard_create
from sql_data import Sql_data, Conclusion, User_language, Result_text

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('/help - Instruction'))
    await message.answer(text=welcome_message, reply_markup=kb)
    Sql_data(message).insert_users()

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("🤖/start - Welcome🤖\n📥/help - teams📥\n🆘/instruction - instruction🆘\n🌐/language - language🌐")

@dp.message_handler(commands=['instruction'])
async def send_instruction(message: types.Message):
    await message.answer(text=Result_text(message.from_user.id).result())

@dp.message_handler(commands=['language'])
async def weather_in(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text='English🇺🇸', callback_data='en')
    btn2 = InlineKeyboardButton(text='Русский🇷🇺', callback_data='ru')
    btn3 = InlineKeyboardButton(text='Кыргызча🇰🇬', callback_data='kg')
    kb.add(btn1, btn2, btn3)
    await message.answer('🌐Choose language:🌐', reply_markup=kb)

@dp.callback_query_handler()
async def check_callback_data(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    User_language(user_id, callback.data).change_user_language()
    if callback.data == "en":
        await callback.answer("Language changed successfully")
    elif callback.data == "ru":
        await callback.answer("Язык успешно изменен")
    else:
        await callback.answer("Тил ийгиликтүү өзгөртүлдү")

@dp.message_handler(commands=['bot'])
async def send_bot(message: types.Message):
    if message.from_user.id == int(ADMIN):
        await message.answer(text=Conclusion().result())

@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    sent_message = await message.answer("⌛️The request will take some time to process.⌛️")
    await message.answer(Bard_create(message.text).chat())
    await bot.delete_message(message.chat.id, sent_message.message_id)

@dp.message_handler(content_types=ContentTypes.ANY)
async def send_all(message: types.Message):
    await message.answer("💤The bot does not process such a message!💤")
   
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)