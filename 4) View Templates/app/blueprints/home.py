from flask import Blueprint, render_template

bp = Blueprint("home", __name__)

# need to create "templates" named folder in app folder for rendering remplates
@bp.route("/")
def index_page():
    return render_template("home/index.html")