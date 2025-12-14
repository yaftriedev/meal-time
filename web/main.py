from flask import Flask, request, redirect, url_for, render_template, session
from os import path
from util import *
from config import *
from datetime import datetime

# Create and Config Flask app
app = Flask(__name__)
app.secret_key = secret_key
app.jinja_env.globals.update(get_meal_time=get_meal_time)
app.jinja_env.globals.update(get_hour=get_hour)

# Check login status before each request
@app.before_request
def check_login():
    if request.endpoint not in not_logged_endpoints and not session.get('logged_in', False):
        return redirect(url_for('login'))

# Routes
@app.route('/', methods=['GET', 'POST'])
def main():

    if request.method == 'POST':
        
        if "password" in request.form and request.form.get("password").strip() != "":
            print("Changing password...")
            new_password = request.form.get("password").strip()
            
            if not new_password:
                return render_template('index.html', error="Password cannot be empty")
            
            if md5_hash(request.form.get('password', '')) == get_stored_password_md5():
                return render_template('index.html', error="New password cannot be the same as the old password")

            # Only for debugging purposes, not recommended in production
            # print(f"New password received: {new_password}")

            with open(password_md5_file, "w") as f:
                f.write(md5_hash(new_password))

        if "meal_time" in request.form:
            print("Updating meal times...")
            meal_time = request.form.get("meal_time", "").strip()
            result, valid = format_time(meal_time)

            if not valid:
                return render_template('index.html', error="Invalid time format")

            with open(meal_time_file, "w") as f:
                f.write(meal_time_separator.join(result))

    return render_template('index.html')

# Auxiliary routes
@app.route('/status', methods=['GET'])
def status():
    return "OK"

@app.route('/loged', methods=['GET'])
def loged():
    return str(session.get('logged_in', False))

# Login/Logout route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        if md5_hash(request.form.get('password', '')) == get_stored_password_md5():
            session['logged_in'] = True
            return redirect(url_for('main'))

        else:
            return render_template('login.html', error="Invalid password")
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

# Main entry point
if __name__ == "__main__":
    # Create password file with default credentials if it doesn't exist
    if not path.exists(password_md5_file):
        with open(password_md5_file, "w") as f:
            f.write(md5_hash(default_credentials))

    # Create meal time file with default times if it doesn't exist
    if not path.exists(meal_time_file):
        with open(meal_time_file, "w") as f:
            f.write(meal_time_separator.join(default_meal_times))

    # Run the Flask app
    app.run(debug=debug_mode, host="0.0.0.0", port=app_port)