import mysql.connector


def connect_to_database():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigBrews-23",
        auth_plugin="mysql_native_password",
        database="episteme_db"
    )

    return connection


def fetch_submissions_verifyview(submission_id):
    # Connect to the database
    connection = connect_to_database()

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Fetch the data from the submissions table for the given submission_id
    cursor.execute(
        'SELECT * FROM submissions WHERE submission_id = %s', (submission_id,))
    submissions = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    return submissions


# You can define other functions for CRUD operations here
# For example: insert_submission(), update_status(), delete_submission()

if __name__ == '__main__':
    # Example usage of the fetch_submissions() function
    submissions = fetch_submissions_verifyview()
    for submission in submissions:
        print(submission)
