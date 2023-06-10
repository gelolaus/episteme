import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BigBrews-23",
    auth_plugin="mysql_native_password",
    database="episteme_db"
)
cursor = db.cursor()

# Function to insert a new submission into the database


def insert_submission(data):
    sql = """INSERT INTO submissions (thesis_title, submission_type, full_name, group_name,
             member_name1, member_name2, member_name3, professor_name, submission_date,
             abstract, soft_copy, github_repository, keywords, school, status)
             VALUES (%(thesis_title)s, %(submission_type)s, %(full_name)s, %(group_name)s,
             %(member_name1)s, %(member_name2)s, %(member_name3)s, %(professor_name)s,
             %(submission_date)s, %(abstract)s, %(soft_copy)s, %(github_repository)s,
             %(keywords)s, %(school)s, %(status)s)"""
    cursor.execute(sql, data)
    db.commit()
    print("Submission inserted successfully!")

# Retrieve submission data from the MySQL database


def get_submission_data():
    sql = "SELECT * FROM submissions WHERE status = 'Submitted'"
    cursor.execute(sql)
    return cursor.fetchall()


# Process each submission and insert into the database
submissions = get_submission_data()
for submission in submissions:
    insert_submission(submission)

# Close the database connection
cursor.close()
db.close()
