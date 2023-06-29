import os
import psycopg2
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

telegram_key = os.getenv('API_KEY') 
admin = os.getenv('ADMIN')
bot = Bot(token=telegram_key)
token = os.getenv("API_BARD")
dp = Dispatcher(bot)
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

instruction_text = """
Who   ➡️ 🙋‍♂️ Assigns the role you need the model to play. A role like a teacher, developer, chef, and so on. 
What  ➡️ 🔬 Refers to the action you want the model to do. 
When  ➡️ 🕑 Your desired timeline to complete a particular task. 
Where ➡️ 📍 Refers to the location or context of a particular prompt. 
Why   ➡️ 🤔 Refers to the reasons, motivations, or goals for a particular prompt."""

class sql_data:
    def db_language(self):
        try:
            # connect to exist database
            connection = psycopg2.connect(
                host=os.getenv('host'),
                user=os.getenv('user'),
                password=os.getenv('password'),
                database=os.getenv('db_name')   
            )
            connection.autocommit = True
            
            # the cursor for perfoming database operations
            # cursor = connection.cursor()
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT version();"
                )
                
                print(f"Server version: {cursor.fetchone()}")
                
            # create a new table
            # with connection.cursor() as cursor:
            #     cursor.execute(
            #         """CREATE TABLE users(
            #             id serial PRIMARY KEY,
            #             first_name varchar(50) NOT NULL,
            #             nick_name varchar(50) NOT NULL);"""
            #     )
                
            #     # connection.commit()
            #     print("[INFO] Table created successfully")
                
            # insert data into a table
            # with connection.cursor() as cursor:
            #     cursor.execute(
            #         """INSERT INTO users (first_name, nick_name) VALUES
            #         ('Oleg', 'barracuda');"""
            #     )
                
            #     print("[INFO] Data was succefully inserted")
                
            # get data from a table
            # with connection.cursor() as cursor:
            #     cursor.execute(
            #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
            #     )
                
            #     print(cursor.fetchone())
                
            # delete a table
            # with connection.cursor() as cursor:
            #     cursor.execute(
            #         """DROP TABLE users;"""
            #     )
                
            #     print("[INFO] Table was deleted")
        
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")

class Bard_create:
    def __init__(self, message: str):
        self.message = message
    def aibek_kk(self):
        from bardapi import Bard
        Bard = Bard(token=token)
        return Bard.get_answer(f"{self.message}")['content']