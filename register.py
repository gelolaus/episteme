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


def register_user(first_name, last_name, email_address, password):
    db_connection = create_connection()
    cursor = db_connection.cursor()

    try:
        query = "INSERT INTO user (first_name, last_name, email_address, password) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, email_address, password)
        cursor.execute(query, values)
        db_connection.commit()
        print("Data inserted successfully")
        return True
    except Error as e:
        print(f"The error '{e}' occurred while inserting data into the table")
        return False
    finally:
        cursor.close()
        db_connection.close()
