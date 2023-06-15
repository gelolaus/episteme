import os
import submit
import mysql.connector

from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from register import register_user
from login import login_user
from admin import fetch_submissions_admin
from verify import fetch_submissions_verify
from publish import fetch_submissions_publish
from view import fetch_submissions_view
from update import update_submission_mysql
from verify_update import update_verify_mysql
from home import fetch_submissions_homepage
from homepage_view import fetch_submissions_homeview
from verify_view import fetch_submissions_verifyview
from personal import get_user_submissions, get_user_id

UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
ALLOWED_EXTENSIONS = {'pdf'}  # Allowed file extensions

app = Flask(__name__, static_folder='static')
app.secret_key = 'BigBrewsIsAwesome'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Define a list of routes that require authentication
authenticated_routes = ['/homepage', '/submission',
                        '/admin', '/update_status', '/verify', '/publish', '/view', '/homeview', '/personal', '/hompage_view', '/verify_view', '/publish_view']


@app.before_request
def check_authentication():
    # Check if the requested route requires authentication
    if request.path in authenticated_routes and 'email_address' not in session:
        # User is not logged in, redirect to landing
        return redirect('/landing')

    # Check if the user is trying to access the /admin page
    if request.path == '/admin' and 'email_address' in session:
        allowed_email_addresses = [
            'dev@bigbrews'  # Modify this with the actual allowed email addresses
        ]
        if session['email_address'] not in allowed_email_addresses:
            return redirect('/')

    # Check if the user is trying to access the /verify page
    if request.path == '/verify' and 'email_address' in session:
        allowed_email_addresses = [
            'dev@bigbrews'  # Modify this with the actual allowed email addresses
        ]
        if session['email_address'] not in allowed_email_addresses:
            return redirect('/')

            # Check if the user is trying to access the /publish page
    if request.path == '/publish' and 'email_address' in session:
        allowed_email_addresses = [
            'dev@bigbrews'  # Modify this with the actual allowed email addresses
        ]
        if session['email_address'] not in allowed_email_addresses:
            return redirect('/')


def get_pdf_data(submission_id):
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigBrews-23",
        auth_plugin="mysql_native_password",
        database="episteme_db"
    )

    # Create a cursor object
    cursor = connection.cursor()


@app.route('/')
def index():
    if 'email_address' in session:
        # User is logged in, redirect to homepage
        return redirect('/homepage')
    else:
        # User is not logged in, redirect to landing
        return redirect('/landing')


# LANDING, REGISTER, and LOGIN pages
@app.route('/landing')
def landing():
    if 'email_address' in session:
        # User is logged in, redirect to homepage
        return redirect('/homepage')
    else:
        # User is not logged in, render the landing page
        return render_template('landing.html')


@app.route('/register', methods=['POST'])
def register_route():
    # Get the form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email_address = request.form['email_address']
    password = request.form['password']

    # Perform domain validation
    allowed_domains = ["apc.edu.ph",
                       "student.apc.edu.ph", "bigbrews"]
    domain = email_address.split("@")[-1]
    if domain not in allowed_domains:
        registration_message = 'This form only accepts \"apc.edu.ph\" and \"student.apc.edu.ph\" email addresses.'
        return render_template('landing.html', registration_message=registration_message)

    # Call the register_user function from register.py
    result = register_user(first_name, last_name, email_address, password)

    # Process the result and return a response
    if result:

        success_message = 'Registered successfully!'
        return render_template('landing.html', success_message=success_message)
    else:
        errorreg_message = 'Error registering user'
        return render_template('landing.html', errorreg_message=errorreg_message)


@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']

        # Call the login_user function from login.py
        result = login_user(email_address, password)

        if result:
            session['email_address'] = email_address
            return redirect('/homepage')  # Redirect to /homepage route
        else:
            error_message = 'Invalid email/password combination'
            return render_template('landing.html', error_message=error_message)
    else:
        return render_template('landing.html')


@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()
    return redirect('/landing')

# HOMEPAGE and SUBMISSION pages


@app.route('/homepage')
def homepage():
    if 'email_address' not in session:
        # User is not logged in, redirect to landing
        return redirect('/landing')

    # Get the email address from the session
    email_address = session['email_address']

    # Retrieve the user ID associated with the logged-in email address
    user_id = get_user_id(email_address)

    if user_id is None:
        # User ID not found, redirect to landing
        return redirect('/landing')

    # Retrieve user-specific submissions based on the user ID
    submissions = fetch_submissions_homepage()

    return render_template('homepage.html', submissions=submissions)


@app.route('/submission')
def submission():
    if 'email_address' in session:
        email_address = session['email_address']
        user_id = get_user_id(email_address)
        submissions = get_user_submissions(user_id)
        return render_template('submission.html', submissions=submissions)
    else:
        return redirect('/landing')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Get the form data
    form_data = {
        'thesis_title': request.form['thesis_title'],
        'submission_type': request.form['answer'],
        'full_name': request.form.get('full_name'),
        'group_name': request.form.get('group_name'),
        'member_name1': request.form.get('member_name1'),
        'member_name2': request.form.get('member_name2'),
        'member_name3': request.form.get('member_name3'),
        'professor_name': request.form['professor_name'],
        'submission_date': request.form['submission_date'],
        'abstract': request.form['abstract'],
        'school': request.form['school']
    }

    # Optional form fields
    if 'github_repository' in request.form:
        form_data['github_repository'] = request.form['github_repository']

    if 'keywords' in request.form:
        form_data['keywords'] = request.form.getlist('keywords[]')

    if 'email_address' not in session:
        # User is not logged in, redirect to landing
        return redirect('/landing')

    # Get the email address from the session
    email_address = session['email_address']

    # Retrieve the user ID associated with the logged-in email address
    user_id = get_user_id(email_address)

    if user_id is None:
        # User ID not found, redirect to landing
        return redirect('/landing')

    # Save the uploaded PDF file
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Append the file to the form_data dictionary
        form_data['file'] = file

        # Call submit function to handle MySQL database operations
        submit.submit_to_database(form_data, user_id)

        return redirect('/submission')

    return "Error submitting form. Please check your file."


@app.route('/update', methods=['POST'])
def update_submission():
    # Get the form data from the request
    form_data = request.form

    # Get the submission ID from the form data
    submission_id = form_data['submission_id']

    # Get the user ID (you may have your own way of retrieving it)
    email_address = session['email_address']
    user_id = get_user_id(email_address)

    # Call the update_submission_mysql function to update the submission in the database
    update_submission_mysql(form_data, user_id, submission_id)

    return redirect('/submission')


@app.route('/update_verify', methods=['POST'])
def update_verify():
    # Get the form data from the request
    form_data = request.form

    # Get the submission ID from the form data
    submission_id = form_data['submission_id']

    # Call the update_submission_mysql function to update the submission in the database
    update_verify_mysql(form_data, submission_id)

    return redirect('/verify')


'''
@app.route('/view_submission', methods=['POST'])
def view_submission():
    submission_id = request.form['submission_id']
    # Fetch the submission details from the MySQL table based on submission_id

    # Pass the details to the view_submission.html template
    return render_template('view_submission.html', submission=submission_details)
'''


# ADMIN and VERIFIER pages


@app.route('/verify')
def verify():
    submissions = fetch_submissions_verify()
    return render_template('verify.html', submissions=submissions)


@app.route('/publish')
def publish():
    submissions = fetch_submissions_publish()
    return render_template('publish.html', submissions=submissions)


@app.route('/admin')
def admin():
    submissions = fetch_submissions_admin()
    return render_template('admin.html', submissions=submissions)


@app.route('/view', methods=['GET'])
def view_submission():
    submission_id = request.args.get('submission_id')
    submission = fetch_submissions_view(submission_id)
    return render_template('view.html', submission=submission)


@app.route('/homepage_view', methods=['GET'])
def homepage_view():
    submission_id = request.args.get('submission_id')
    submission = fetch_submissions_homeview(submission_id)
    return render_template('homepage_view.html', submission=submission)


@app.route('/verify_view', methods=['GET'])
def verify_view():
    submission_id = request.args.get('submission_id')
    submission = fetch_submissions_verifyview(submission_id)
    return render_template('verify_view.html', submission=submission)


if __name__ == '__main__':
    app.run(debug=True)
