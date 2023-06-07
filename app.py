from flask import Flask, render_template, request, redirect, session, jsonify
from register import register_user
from login import login_user
import submit

app = Flask(__name__, static_folder='static')
app.secret_key = 'BigBrewsIsAwesome'


@app.route('/')
def index():
    return ('Hello, world!')


'''
This is for the LANDING, REGISTER, and LOGIN page
This is for the LANDING, REGISTER, and LOGIN page
This is for the LANDING, REGISTER, and LOGIN page
'''


@app.route('/landing')
def landing():
    return render_template('landing.html')


@app.route('/register', methods=['POST'])
def register_route():
    # Get the form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email_address = request.form['email_address']
    password = request.form['password']

    # Call the register_user function from register.py
    result = register_user(first_name, last_name, email_address, password)

    # Process the result and return a response
    if result:
        response = {'message': 'Registration successful'}
    else:
        response = {'message': 'Registration failed'}

    return jsonify(response)


@app.route('/login', methods=['POST'])
def login_route():
    email_address = request.form['email_address']
    password = request.form['password']

    # Call the login_user function from login.py
    result = login_user(email_address, password)

    if result:
        session['email_address'] = email_address
        return redirect('/homepage')
    else:
        return 'Invalid email/password combination'


'''
This is for the HOMEPAGE and SUBMISSION page
This is for the HOMEPAGE and SUBMISSION page
This is for the HOMEPAGE and SUBMISSION page
'''


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/submission')
def submission():
    return render_template('submission.html')


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

    # Call submit function to handle MySQL database operations
    submit.submit_to_database(form_data)

    return "Form submitted successfully!"


'''
This is for the ADMIN and VERIFIER page
This is for the ADMIN and VERIFIER page
This is for the ADMIN and VERIFIER page
'''


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
