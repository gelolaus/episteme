import mysql.connector


def submit_to_database(form_data, user_id):
    # Get the file from the form_data
    file = form_data['file']

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigBrews-23",
        auth_plugin="mysql_native_password",
        database="episteme_db"
    )

    cursor = db.cursor()

    # Insert the data into the database
    query = "INSERT INTO submissions (thesis_title, submission_type, full_name, group_name, member_name1, member_name2, member_name3, professor_name, submission_date, abstract, school, soft_copy"

    # Optional fields
    if 'github_repository' in form_data:
        query += ", github_repository"

    if 'keywords' in form_data:
        query += ", keywords"

    # Add the user_id column to the query
    query += ", user_id)"

    query += " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"

    # Optional field placeholders
    if 'github_repository' in form_data:
        query += ", %s"

    if 'keywords' in form_data:
        query += ", %s"

    # Add the placeholder for user_id
    query += ", %s)"

    values = (
        form_data['thesis_title'],
        form_data['submission_type'],
        form_data['full_name'],
        form_data['group_name'],
        form_data['member_name1'],
        form_data['member_name2'],
        form_data['member_name3'],
        form_data['professor_name'],
        form_data['submission_date'],
        form_data['abstract'],
        form_data['school'],
        file.read(),  # Read the file content as bytes
    )

    # Optional field values
    if 'github_repository' in form_data:
        values += (form_data['github_repository'],)

    if 'keywords' in form_data:
        keywords = form_data['keywords'].split(", ")
        keywords_str = ', '.join(keywords)
        values += (keywords_str,)

    # Add the user_id to the values tuple
    values += (user_id,)

    cursor.execute(query, values)

    db.commit()

    cursor.close()
    db.close()
