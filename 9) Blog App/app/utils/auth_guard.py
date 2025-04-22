from functools import wraps
from flask import session, redirect, url_for, flash


# login decorator
def login_required(allowed_roles=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if 'user_id' not in session:
                flash("Please log in to access this page.", "warning")
                return redirect(url_for('auth_routes.login'))

            if allowed_roles is not None:
                user_role = session.get('user_role')
                if user_role not in allowed_roles:
                    flash("Unauthorized access to this page.", "danger")
                    return redirect(url_for('home_routes.home'))

            return view_func(*args, **kwargs)
        return wrapper
    return decorator


def login_not_required():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if 'user_id' in session:
                flash("Already loggedin.", "warning")
                return redirect(url_for('home_routes.home'))

            return view_func(*args, **kwargs)
        return wrapper
    return decorator