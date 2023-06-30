# Libraries Imported
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

telegram_key = os.getenv('API_KEY') # Stores the API key for the Telegram bot.
ADMIN = os.getenv('ADMIN') # Stores the admin username or ID for the bot.
token = os.getenv("API_BARD") # Stores the API key for an external service called "Bard".
connect = { # Stores a dictionary of database connection details, including the host, user, password, and database name.
    "host": os.getenv('host'),
    "user": os.getenv('user'),
    "password": os.getenv('password'),
    "database": os.getenv('db_name') 
}

bot = Bot(token=telegram_key) # Bot Initialization
dp = Dispatcher(bot) # Dispatcher Initialization

# Welcome Message
welcome_message = """ 
Bard is a large language model from Google AI, trained on a massive dataset of text and code. I can generate text, translate languages, write different kinds of creative content, and answer your questions in an informative way. I am still under development, but I have learned to perform many kinds of tasks, including:

🤖 Following instructions and completing requests thoughtfully.
📚 Answering questions in a comprehensive and informative way, even if they are open ended, challenging, or strange.
🎭 Generating different creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.
I am a helpful and informative bot that can be used for a variety of purposes. I can be used to:

🏖️ Provide summaries of factual topics.
👫 Create stories.
🌎 Translate languages.
✍️ Write different kinds of creative content.
❓ Answer your questions in an informative way.
I am still under development, but I am learning new things every day. I am excited to see what the future holds for me, and I am eager to help people in any way that I can.

Here are some words that I would use to describe myself:

💡 Intelligent
💡 Creative
🤔 Curious
🤖 Helpful
ℹ️ Informative
🕵️ Eager to learn
I hope you will find me to be a helpful and informative bot. 😊

I hope you like the emojis!"""