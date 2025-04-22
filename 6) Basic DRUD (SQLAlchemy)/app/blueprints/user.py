from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import User as UserModel
from app.extentions import db

bp = Blueprint("user", __name__)

@bp.route("/user/create", methods=["GET"])
def create():
    return render_template("user/create.html")


@bp.route("/user/create", methods=["POST"])
def post_create():
    # getting form data
    # return request.form
    new_user = UserModel(
        name = request.form["name"],
        email = request.form["email"]
    )

    db.session.add(new_user)
    db.session.commit()
    # "user" is the name of blue print while "list" is the function
    # where we want to redirect
    return redirect(url_for("user.list"))


@bp.route("/user/list", methods=["GET"])
def list():
    users = UserModel.query.all()
    return render_template("user/list.html", users=users)


@bp.route("/user/details/<int:id>", methods=["GET"])
def detail(id):
    user = UserModel.query.get(id)
    return render_template("user/details.html", user = user)


@bp.route("/user/update/<int:id>", methods=["GET"])
def update(id):
    user = UserModel.query.get(id)
    return render_template("user/update.html", user=user)


@bp.route("/user/update", methods=["POST"])
def post_update():

    user = UserModel.query.get(request.form["id"])
    user.name = request.form["name"]
    user.email = request.form["email"]
    
    db.session.commit()
    return redirect(url_for("user.list"))



@bp.route("/user/delete/<int:id>", methods=["DELETE"])
def delete(id):
    user = UserModel.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return True