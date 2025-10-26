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

            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("🎉 Database 'alx_book_store' created or already exists.")

    except mysql.connector.Error as err:
      
        print(f"❌ Error: {err}")

    finally:
       
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL connection closed.")

if __name__ == "__main__":
    main()