#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error

def main():
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if connection.is_connected():
            print("✅ Successfully connected to MySQL Server")

            cursor = connection.cursor()

            
            with open("alx_book_store.sql", "r") as file:
                sql_script = file.read()

            
            for result in cursor.execute(sql_script, multi=True):
                pass

            print("🎉 Database and tables created successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

    finally:
        
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL connection closed.")

if __name__ == "__main__":
    main()