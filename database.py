import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


class Database:

    def __init__(self):

        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )


    def execute_select(self, sql, params=None):

        cursor = self.connection.cursor(
            dictionary=True
        )

        try:
            cursor.execute(
                sql,
                params or ()
            )

            return cursor.fetchall()

        finally:
            cursor.close()



    def execute(self, sql, params=None):

        """
        Pour les requêtes INSERT/UPDATE/DELETE
        """

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                sql,
                params or ()
            )

            self.connection.commit()

            return cursor.rowcount

        finally:
            cursor.close()



    def close(self):

        if self.connection.is_connected():
            self.connection.close()