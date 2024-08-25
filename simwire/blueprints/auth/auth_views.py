from flask_login import login_required, current_user, logout_user, login_user
from flask import render_template, request, flash, url_for, redirect, jsonify
from werkzeug.exceptions import BadRequest


from . import verify_password
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates')


# renders the manual login page
@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('auth_login.html')

@auth_bp.route('/homepage')
def landing_page():
        return f"Welcome, [current_user.id-placeholder] w/ [username-placeholder]! This is " \
           f"a protected page." + str(url_for('auth.landing_page'))

@auth_bp.route('/login', methods=['POST'])
def login_validate():
    form_username = ''
    form_password = ''
    
    # logic for authentication goes here
    return redirect(url_for('auth.landing_page'))

@auth_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('auth_logout.html')
