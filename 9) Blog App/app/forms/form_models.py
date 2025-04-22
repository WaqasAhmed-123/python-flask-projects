# need to install following library
# pip install flask-wtf
#pip install email-validator

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileAllowed

class SignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Name is required."), Length(min=3, message="Name must be at least 3 characters.")])
    email = StringField("Email", validators=[DataRequired(message="Email is required."), Email(message="Invalid email format.")])
    password = PasswordField("Password", validators=[
        DataRequired(message="Password is required."),
        Length(min=6, message="Password must be at least 6 characters.")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(message="Please confirm your password."),
        EqualTo('password', message="Passwords must match.")
    ])


class ResetPasswordForm(FlaskForm):
    password = PasswordField("New Password", validators=[
        DataRequired(message="New Password is required."),
        Length(min=6, message="Password must be at least 6 characters.")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(message="Please confirm your password."),
        EqualTo('password', message="Passwords must match.")
    ])


class AddUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Name is required."), Length(min=3, message="Name must be at least 3 characters.")])
    email = StringField("Email", validators=[DataRequired(message="Email is required."), Email(message="Invalid email format.")])
    password = PasswordField("Password", validators=[
        DataRequired(message="Password is required."),
        Length(min=3, message="Password must be at least 3 characters.")
    ])


class UpdateUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Name is required."), Length(min=3, message="Name must be at least 3 characters.")])
    email = StringField("Email", validators=[DataRequired(message="Email is required."), Email(message="Invalid email format.")])
    

class BlogForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(message="Title is required."), Length(min=3, message="Title must be at least 3 characters.")])
    content = TextAreaField("Content", validators=[DataRequired(message="Content is required."), Length(min=5, message="Content must be at least 5 characters.")])
    image = FileField("Upload Image", validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message = "Only Images allowed!")])

