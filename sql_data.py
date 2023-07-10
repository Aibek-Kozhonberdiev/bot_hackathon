# Libraries Imported
import datetime
import psycopg2
from config import CONNECT

class SqlConnect:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=CONNECT['host'],
            user=CONNECT['user'],
            password=CONNECT['password'],
            database=CONNECT['database']   
        )

class SqlData(SqlConnect):
    def __init__(self, message):
        super().__init__()  # Calling the constructor of the outgoing class
        self.date = datetime.datetime.now().date()
        self.first_name = message.from_user.first_name
        self.last_name = message.from_user.last_name
        self.id_telegram = message.from_user.id
    
    async def insert_users(self):
        try:
            self.connection.autocommit = True
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO users(first_name, last_name, date, id_telegram) VALUES
                    ('{self.first_name}', '{self.last_name}', '{self.date}', {self.id_telegram});"""
                )

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if self.connection:
                self.connection.close()
                print("[INFO] PostgreSQL connection closed")
                
class UserLanguage(SqlConnect):
    def __init__(self, user_id: str, new_language: str):
        super().__init__() # Calling the constructor of the outgoing class
        self.user_id = user_id
        self.new_language = new_language

    async def change_user_language(self):
        try:
            cursor = self.connection.cursor()

            create_table_query = f"""UPDATE users SET user_language = '{self.new_language}' WHERE id_telegram = '{self.user_id}';"""

            cursor.execute(create_table_query)
            self.connection.commit()
            print("Table created successfully")

        except (Exception, psycopg2.Error) as error:
            print("Error while creating table in PostgreSQL", error)

        finally:
            if cursor:
                cursor.close()
            if self.connection:
                self.connection.close()
                print("PostgreSQL connection closed")

class Conclusion(SqlConnect): 
    async def admin(self):
        try:
            cursor = self.connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM users"

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
        
            print("[INFO] Output of each article and its columns")
            for_me = []
            for row in mobile_records:
                for_me.append(row)
            return for_me[0]

        except (psycopg2.Error) as error:
            print("[INFO] Error while working with PostgreSQL:", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("[INFO] PostgreSQL connection closed") 
        
class ResultText(SqlConnect):
    def __init__(self, user_id: int, text: str):
        super().__init__() # Calling the constructor of the outgoing class
        self.user_id = user_id
        self.text = text

    async def lang_text(self):
        try:
            lang = await self.get_user_language()
            cursor = self.connection.cursor()
            postgreSQL_select_Query = f"""
            SELECT value
            FROM translations
            WHERE language_code = '{lang}'
            AND key = '{self.text}';
            """

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()

            print("[INFO] Output of each article and its columns")
            return mobile_records[0][0]

        except (psycopg2.Error) as error:
            print("[INFO] Error while working with PostgreSQL:", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("[INFO] PostgreSQL connection closed")

    async def get_user_language(self):
        try:
            cursor = self.connection.cursor()
            postgreSQL_select_Query = f"""
            SELECT user_language
            FROM users
            WHERE id_telegram = {self.user_id};
            """

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()

            print("[INFO] Output of each article and its columns")
            return mobile_records[0][0]

        except (psycopg2.Error) as error:
            print("[INFO] Error while working with PostgreSQL:", error)
        finally:
            if cursor:
                cursor.close()

async def sqldata(message):
    creator = SqlData(message)
    response = await creator.insert_users()
    return response

async def userlanguage(user_id: str, new_language: str):
    creator = UserLanguage(user_id, new_language)
    response = await creator.change_user_language()
    return response

async def conclusion():
    creator = Conclusion()
    response = await creator.admin()
    return response

async def resulttext(user_id: int, text: str):
    creator = ResultText(user_id, text)
    response = await creator.lang_text()
    return response
