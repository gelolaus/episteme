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


def get_user_submissions(user_id):
    db_connection = create_connection()
    cursor = db_connection.cursor()
    try:
        query = "SELECT * FROM submissions WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        submissions = cursor.fetchall()
        return submissions
    except Error as e:
        print(f"The error '{e}' occurred while executing the SQL query")
        return []
    finally:
        cursor.close()
        db_connection.close()


def get_user_id(email_address):
    db_connection = create_connection()
    cursor = db_connection.cursor()

    try:
        query = "SELECT user_id FROM user WHERE email_address = %s"
        values = (email_address,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            user_id = result[0]
            return user_id
        else:
            return None
    except Error as e:
        print(f"The error '{e}' occurred while executing the SQL query")
        return None
    finally:
        cursor.close()
        db_connection.close()


def get_user_submissions(user_id):
    db_connection = create_connection()
    cursor = db_connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM submissions WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(query, values)
        submissions = cursor.fetchall()

        return submissions
    except Error as e:
        print(f"The error '{e}' occurred while executing the SQL query")
        return []
    finally:
        cursor.close()
        db_connection.close()
