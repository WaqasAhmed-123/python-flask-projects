from flask import Blueprint, render_template, request, redirect, url_for
from app.services.user import *

user_routes = Blueprint('user_routes', __name__)

# Home page - List users
@user_routes.route('/')
def index():
    users = get_users()
    return render_template('index.html', users=users)

# Add a user
@user_routes.route('/add_user', methods=['POST'])
def add_user_route():
    name = request.form['name']
    age = request.form['age']
    add_user(name, age)
    return redirect(url_for('user_routes.index'))

# Update a user
@user_routes.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user_route(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        update_user(id, name, age)
        return redirect(url_for('user_routes.index'))

    users = get_users()
    user = next((u for u in users if u[0] == id), None)
    return render_template('update_user.html', user=user)

# Delete a user
@user_routes.route('/delete_user/<int:id>')
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for('user_routes.index'))