import csv
import psycopg2
import asyncio

from colorama import Fore
from config import CONNECT


async def create_tables():
    try:
        connection = psycopg2.connect(
            host=CONNECT['host'],
            user=CONNECT['user'],
            password=CONNECT['password'],
            database=CONNECT['database']
        )
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE translations (
            id BIGSERIAL NOT NULL PRIMARY KEY,
            language_code VARCHAR(5) NOT NULL,
            key VARCHAR(50) NOT NULL,
            value TEXT NOT NULL);"""
                       )

        try:
            cursor.execute("""CREATE TABLE users (
                id BIGSERIAL NOT NULL PRIMARY KEY,
                first_name VARCHAR(64) NOT NULL,
                last_name VARCHAR(64) DEFAULT NULL,
                language_code VARCHAR(5) DEFAULT 'en',
                id_telegram BIGSERIAL NOT NULL);"""
                           )
            print(Fore.GREEN + '[+] creation of the users table was successfull')
        except psycopg2.Error as error:
            print(Fore.RED + '[-] error when creating table users', error)

        with open('translations.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cursor.execute(
                    f"INSERT INTO translations(language_code, key, value) VALUES('{row[1]}', '{row[2]}', '{row[3]}');")
        print(Fore.GREEN + '[+] creation of the translations table was successfull')

    except psycopg2.Error as error:
        print(Fore.RED + '[-] error failed to create table:', error)

    finally:
        if connection:
            connection.commit()
            connection.close()
            connection.close()


if __name__ == "__main__":
    asyncio.run(create_tables())
