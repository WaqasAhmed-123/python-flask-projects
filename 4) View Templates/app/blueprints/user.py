from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("user", __name__)

@bp.route("/user/create", methods=["GET"])
def create():
    return render_template("user/create.html")


@bp.route("/user/create", methods=["POST"])
def post_create():
    # getting form data
    # return request.form

    # "user" is the name of blue print while "create" is the function
    # where we want to redirect
    return redirect(url_for("user.create"))


@bp.route("/user/list", methods=["GET"])
def list():
    return render_template("user/list.html")


@bp.route("/user/details/<int:id>", methods=["GET"])
def detail(id):
    return render_template("user/details.html", id = id)