from flask import Flask, render_template, request, redirect, session, jsonify
from register import register_user
from login import login_user

app = Flask(__name__, static_folder='static')
app.secret_key = 'BigBrewsIsAwesome'


@app.route('/')
def index():
    return ('Hello, world!')


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


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
