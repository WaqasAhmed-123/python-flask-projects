from flask import Blueprint

bp = Blueprint("home", __name__)

@bp.route("/")
def index_page():
    return "<h3>Welcome to homepage.</h3>"