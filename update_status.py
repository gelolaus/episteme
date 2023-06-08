import mysql.connector


def update_submission_status(submission_id, new_status):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigBrews-23",
        auth_plugin="mysql_native_password",
        database="episteme_db"
    )
    cursor = connection.cursor()

    # Update the status in the database
    update_query = 'UPDATE submissions SET status = %s WHERE submission_id = %s'
    cursor.execute(update_query, (new_status, submission_id))
    connection.commit()

    # Close the cursor and database connection
    cursor.close()
    connection.close()
