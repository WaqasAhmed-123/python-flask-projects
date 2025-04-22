from flask import Blueprint, render_template, session
from app.services.user_service import get_user_count
from app.services.blog_service import get_blog_count
from app.utils.auth_guard import login_required

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/home')
#@login_required([1, 2]) #only allowed roles
@login_required() #all roles
def home():
    user_count = get_user_count()
    blog_count = get_blog_count(session['user_id'] if session['user_role'] == 2 else None)
    return render_template('home/index.html', user_count=user_count, blog_count=blog_count)
