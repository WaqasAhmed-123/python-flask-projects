from flask import Blueprint, flash, render_template, request, redirect, url_for
from app.forms.form_models import AddUserForm, UpdateUserForm
from app.services.user_service import *
from app.utils.auth_guard import login_required
from app.utils.encryption import *

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/user/list')
@login_required([1]) #only for admin access
def list():
    users = get_users()
    return render_template('user/list.html', users=users)


@user_routes.route('/user/add', methods=['GET', 'POST'])
@login_required([1]) #only for admin access
def add():
    form = AddUserForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data

            existing_user = get_user_by_email(email)
            if existing_user:
                flash("Email is already registered.", "danger")
                return render_template('user/add.html', form=form)

            add_user(name, email, password)
            flash("User created successfully.", "success")
            return redirect(url_for('user_routes.add'))
    
    return render_template('user/add.html', form=form)


@user_routes.route('/user/update/<string:id>', methods=['GET', 'POST'])
@login_required([1])
def update(id):
    form = UpdateUserForm()
    user = get_user_by_id(decrypt_id(id))

    if not user:
        return "User not found", 404

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data.strip()
            email = form.email.data.strip()

            existing_user = get_user_by_email(email, user['id'])
            if existing_user:
                flash("Email is already registered.", "danger")
                return redirect(url_for('user_routes.update', id=id))

            update_user(user['id'], name, email)
            flash("User updated successfully.", "success")
            return redirect(url_for('user_routes.list')) 
    else:
        form.name.data = user['name']
        form.email.data = user['email']

    return render_template('user/update.html', form=form, id=id)


@user_routes.route('/user/delete/<string:id>')
@login_required([1]) #only for admin access
def delete(id):
    delete_user(decrypt_id(id))
    flash("user deleted successfully.", "success")
    return redirect(url_for('user_routes.list'))