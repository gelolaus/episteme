'''
import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BigBrews-23",
            auth_plugin="mysql_native_password",
            database="episteme_db"
        )
        print("Connected to MySQL database")
    except Error as e:
        print(f"The error '{e}' occurred while connecting to MySQL database")
    return connection


def login_user(email_address, password):
    db_connection = create_connection()
    cursor = db_connection.cursor()

    try:
        query = "SELECT * FROM user WHERE email_address = %s AND password = %s"
        values = (email_address, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            return True
        else:
            return False
    except Error as e:
        print(f"The error '{e}' occurred while executing the SQL query")
        return False
    finally:
        cursor.close()
        db_connection.close()
'''

import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BigBrews-23",
            auth_plugin="mysql_native_password",
            database="episteme_db"
        )
        print("Connected to MySQL database")
    except Error as e:
        print(f"The error '{e}' occurred while connecting to MySQL database")
    return connection


def login_user(email_address, password):
    db_connection = create_connection()
    cursor = db_connection.cursor()

    try:
        query = "SELECT user_id, first_name, last_name, email_address FROM user WHERE email_address = %s AND password = %s"
        values = (email_address, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            user_object = {
                'user_id': user[0],
                'first_name': user[1],
                'last_name': user[2],
                'email_address': user[3]
            }
            return user_object
        else:
            return None
    except Error as e:
        print(f"The error '{e}' occurred while executing the SQL query")
        return None
    finally:
        cursor.close()
        db_connection.close()
