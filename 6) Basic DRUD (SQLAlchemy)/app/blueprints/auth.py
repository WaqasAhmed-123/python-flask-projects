from flask import Blueprint, render_template
from app.models.user import User as UserModel

bp = Blueprint("auth", __name__)

@bp.route("/login")
def login():
    return render_template("auth/login.html")