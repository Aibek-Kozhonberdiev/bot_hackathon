import os
import requests
import psycopg2
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class Connect:
    def __init__(self, url: str):
        self.url = url
        
    def req(self):
        try:
            self.r = requests.get(self.url)
            return self.r.content
        except requests.ConnectionError as e:
            print(e)

class Botrecord:
    def text_welcome(self):
        with open("~/bot_hackathon/text_bot/text_welcome.tex", "r") as f:
            self.start_text = f.read()
        return self.start_text
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

Botrecord().db_language()

# Здесь будет парсер