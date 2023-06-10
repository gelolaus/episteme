from flask import Flask, render_template, request, redirect, session, jsonify
from register import register_user
from login import login_user
from admin import fetch_submissions
from personal import get_user_submissions, get_user_id
import submit

app = Flask(__name__, static_folder='static')
app.secret_key = 'BigBrewsIsAwesome'

# Define a list of routes that require authentication
authenticated_routes = ['/homepage', '/submission', '/admin', '/update_status']


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
                       "student.apc.edu.ph", "bigbrews", "tester"]
    domain = email_address.split("@")[-1]
    if domain not in allowed_domains:
        return "Invalid email domain. Please use an email address from the allowed domains."

    # Call the register_user function from register.py
    result = register_user(first_name, last_name, email_address, password)

    # Process the result and return a response
    if result:
        return redirect('/landing')
    else:
        return 'Error registering user'


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
    submissions = get_user_submissions(user_id)

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

    # Call submit function to handle MySQL database operations
    submit.submit_to_database(form_data, user_id)

    return "Form submitted successfully!"


# ADMIN and VERIFIER pages
@app.route('/admin')
def admin():
    submissions = fetch_submissions()
    return render_template('admin.html', submissions=submissions)


if __name__ == '__main__':
    app.run(debug=True)
