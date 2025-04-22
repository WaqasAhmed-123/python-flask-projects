from flask import Blueprint, render_template
from app.models.user import User as UserModel

bp = Blueprint("home", __name__)

# need to create "templates" named folder in app folder for rendering remplates
@bp.route("/")
def index_page():
    user_count = UserModel.query.count()
    return render_template("home/index.html", user_count=user_count)