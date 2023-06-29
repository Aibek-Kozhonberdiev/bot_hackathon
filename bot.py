from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentTypes, InlineKeyboardMarkup, InlineKeyboardButton
from main import admin, bot, dp, welcome_message, instruction_text, sql_data, Bard_create

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton('/help - Instruction'))
    await message.answer(text=welcome_message, reply_markup=kb)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("🤖/start - Welcome🤖\n📥/help - teams📥\n🌐/language - language🌐\n🆘/instruction - instruction🆘")

@dp.message_handler(commands=['instruction'])
async def send_instruction(message: types.Message):
    await message.answer(instruction_text)

@dp.message_handler(commands=['language'])
async def weather_in(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text='English🇺🇸', callback_data='us')
    btn2 = InlineKeyboardButton(text='Русский🇷🇺', callback_data='ru')
    btn3 = InlineKeyboardButton(text='Кыргызча🇰🇬', callback_data='kg')
    kb.add(btn1, btn2, btn3)
    await message.answer('🌐Choose language:🌐', reply_markup=kb)

@dp.callback_query_handler()
async def check_callback_data(callback: types.CallbackQuery):
    if callback.data == "us":
        await callback.answer(text="aaa")
    print(callback)

@dp.message_handler(commands=['bot'])
async def send_bot(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text=sql_data().db_language())
    print(message.chat.id)

@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    sent_message = await message.answer("⌛️The request will take some time to process.⌛️")
    await message.answer(Bard_create(message.text).aibek_kk())
    await bot.delete_message(message.chat.id, sent_message.message_id)

@dp.message_handler(content_types=ContentTypes.ANY)
async def send_all(message: types.Message):
    await message.answer("💤The bot does not process such a message!💤")
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)