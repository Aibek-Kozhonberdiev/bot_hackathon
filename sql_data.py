import datetime
import psycopg2
from bot_create import connect

class Sql_connect:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=connect['host'],
            user=connect['user'],
            password=connect['password'],
            database=connect['database']   
        )

class Sql_data(Sql_connect):
    def __init__(self, message):
        super().__init__()  # Вызов конструктора родительского класса
        self.date = datetime.datetime.now().date()
        self.first_name = message.from_user.first_name
        self.last_name = message.from_user.last_name
        self.id_telegram = message.from_user.id
    
    def insert_users(self):
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

class User_language(Sql_connect):
    def __init__(self, user_id: str, new_language: str):
        super().__init__()
        self.user_id = user_id
        self.new_language = new_language

    def change_user_language(self):
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

class Conclusion(Sql_connect):
    def result(self):
        try:
            cursor = self.connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM users"

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
        
            print("[INFO] Output of each article and its columns")
            for_me = []
            for row in mobile_records:
                for_me.append(f"Id: {row[0]}, first_name: {row[1]}, last_name: {row[2]}, id_telegram: {row[3]}, date: {row[4]}")
            return for_me[0]

        except (psycopg2.Error) as error:
            print("[INFO] Error while working with PostgreSQL:", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("[INFO] PostgreSQL connection closed") 
        
class ResultText(Sql_connect):
    def __init__(self, user_id: int, text: str):
        super().__init__()
        self.user_id = user_id
        self.text = text

    def lang_text(self):
        try:
            lang = self.get_user_language()
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

    def get_user_language(self):
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