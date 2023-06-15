import mysql.connector


def update_submission_mysql(form_data, user_id, submission_id):

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigBrews-23",
        auth_plugin="mysql_native_password",
        database="episteme_db"
    )

    cursor = db.cursor()

    # Update the data in the database
    query = """
        UPDATE submissions
        SET thesis_title = %s,
            submission_type = %s,
            full_name = %s,
            group_name = %s,
            member_name1 = %s,
            member_name2 = %s,
            member_name3 = %s,
            professor_name = %s,
            submission_date = %s,
            abstract = %s,
            school = %s,
            status = %s,
            comments = %s
    """

    # Optional fields
    if 'github_repository' in form_data:
        query += ", github_repository = %s"

    if 'keywords' in form_data:
        query += ", keywords = %s"

    # Add the PDF file update code
    if 'pdf_file' in form_data:
        query += ", pdf_file = %s"
        # Assuming you have the PDF file object
        pdf_file = form_data['pdf_file'].read()

    query += " WHERE submission_id = %s AND user_id = %s"

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
        form_data['status'],
        form_data['comments']
    )

    # Optional field values
    if 'github_repository' in form_data:
        values += (form_data['github_repository'],)

    if 'keywords' in form_data:
        keywords = form_data['keywords'].split(", ")
        keywords_str = ', '.join(keywords)
        values += (keywords_str,)

    # Add the PDF file value to the values tuple
    if 'pdf_file' in form_data:
        values += (pdf_file,)

    # Add submission_id and user_id to the values tuple
    values += (submission_id, user_id)

    cursor.execute(query, values)

    db.commit()

    cursor.close()
    db.close()
