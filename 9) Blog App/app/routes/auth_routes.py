from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt

from app.forms.form_models import ResetPasswordForm, SignupForm, UpdateUserForm
from app.services.user_service import *
from app.utils.auth_guard import *
from app.utils.encryption import *
from app.utils.mail_sender import send_reset_email

bcrypt = Bcrypt()
auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/')
def index():
    return redirect(url_for('auth_routes.login'))


@auth_routes.route('/login', methods=['GET', 'POST'])
@login_not_required()
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = get_user_by_email(email)

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            session['user_profile'] = user['profile_path']
            session.permanent = True

            return redirect(url_for('home_routes.home'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('auth/login.html')


@auth_routes.route('/forgot-password', methods=['GET', 'POST'])
@login_not_required()
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        if not email.strip():
            flash("Email is required.", "danger")
            return redirect(url_for('auth_routes.forgot_password')) 
        
        user = get_user_by_email(email)

        if not user:
            flash("Email does not belongs to us.", "danger")
            return redirect(url_for('auth_routes.forgot_password'))

        reset_url = f"{request.url_root}reset-password/{encrypt_id(user['id'])}"

        if send_reset_email(email, user['name'], reset_url):
            flash("Reset link sent to your email.", "success")
        else:
            flash("Failed to send email. Try again later.", "danger")

        return redirect(url_for('auth_routes.forgot_password'))

    return render_template('auth/forgot.html')


@auth_routes.route('/reset-password/<string:id>', methods=['GET', 'POST'])
@login_not_required()
def reset_password(id):
    form = ResetPasswordForm()
    user = get_user_by_id(decrypt_id(id))

    if not user:
        flash("Invalid reset link or user not found.", "danger")
        return redirect(url_for('auth_routes.login'))

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        update_user_password(decrypt_id(id), hashed_password)
        flash("Password updated successfully. You can now log in.", "success")
        return redirect(url_for('auth_routes.login'))

    return render_template('auth/reset.html', form=form, id=id)


@auth_routes.route('/signup', methods=['GET', 'POST'])
@login_not_required()
def signup():
    form = SignupForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data

            existing_user = get_user_by_email(email)
            if existing_user:
                flash("Email is already registered.", "danger")
                return render_template('auth/signup.html', form=form)

            add_user(name, email, password)
            flash("Signup successful! You can now log in.", "success")

            return redirect(url_for('auth_routes.login'))
    
    return render_template('auth/signup.html', form=form)


@auth_routes.route('/update-profile', methods=['GET', 'POST'])
@login_required() #for all users
def profile():
    form = UpdateUserForm()
    user_id = session['user_id']
    user = get_user_by_id(user_id)

    if not user:
        return "User not found", 404

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data.strip()
            email = form.email.data.strip()

            existing_user = get_user_by_email(email, user_id)
            if existing_user:
                flash("Email is already registered.", "danger")
                return redirect(url_for('auth_routes.profile'))

            update_user(user_id, name, email)

            updated_user = get_user_by_id(user_id)
            session['user_name'] = updated_user['name']
            session['user_email'] = updated_user['email']

            flash("Profile updated successfully.", "success")
            return redirect(url_for('auth_routes.profile'))
    else:
        form.name.data = user['name']
        form.email.data = user['email']

    return render_template('auth/update-profile.html', form=form)

@auth_routes.route('/update_password', methods=['GET', 'POST'])
@login_required() #for all users
def update_password():
    form = ResetPasswordForm()
    user_id = session['user_id']
    user = get_user_by_id(user_id)

    if not user:
        return "User not found", 404

    if form.validate_on_submit():
        old_password = request.form['old_password']
        if not bcrypt.check_password_hash(user['password'], old_password.strip()):
            flash("Old password not matched.", "danger")
            return redirect(url_for('auth_routes.update_password'))
        
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        update_user_password(user_id, hashed_password)
        flash("Password updated successfully.", "success")
        return redirect(url_for('auth_routes.update_password'))

    return render_template('auth/update-password.html', form=form)


@auth_routes.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_routes.login'))
