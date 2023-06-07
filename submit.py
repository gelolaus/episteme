import mysql.connector


def submit_to_database(form_data):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigBrews-23",
        auth_plugin="mysql_native_password",
        database="episteme_db"
    )

    cursor = db.cursor()

    # Insert the data into the database
    query = "INSERT INTO submissions (thesis_title, submission_type, full_name, group_name, member_name1, member_name2, member_name3, professor_name, submission_date, abstract, school"

    # Optional fields
    if 'github_repository' in form_data:
        query += ", github_repository"

    if 'keywords' in form_data:
        query += ", keywords"

    query += ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"

    # Optional field placeholders
    if 'github_repository' in form_data:
        query += ", %s"

    if 'keywords' in form_data:
        query += ", %s"

    query += ")"

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
        form_data['school']
    )

    # Optional field values
    if 'github_repository' in form_data:
        values += (form_data['github_repository'],)

    if 'keywords' in form_data:
        # Get the keywords as a list
        keywords = form_data['keywords']

        # Convert the keywords into a format suitable for database storage
        keywords_str = ', '.join(keywords)

        values += (keywords_str,)

    cursor.execute(query, values)
    db.commit()

    cursor.close()
    db.close()
