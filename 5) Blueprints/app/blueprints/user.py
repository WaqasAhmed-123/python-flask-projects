from flask import Blueprint, request

bp = Blueprint("user", __name__)

@bp.route("/user/", methods=["GET", "POST", "PUT", "DELETE"])
def user():
    if request.method == "GET":
        return "<h3>Get request called.</h3>"
    elif request.method == "POST":
        return "<h3>Post request called.</h3>"
    elif request.method == "PUT":
        return "<h3>PUT request called.</h3>"
    else:
        return "<h3>Delete request called.</h3>"