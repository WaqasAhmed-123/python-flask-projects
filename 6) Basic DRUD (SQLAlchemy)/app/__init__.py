# need to run following command in main folder through command prompt for sqlalchemy Db
# pip install -U Flask-SQLAlchemy

from flask import Flask
from app.blueprints import home, user, auth
from app.extentions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

app.register_blueprint(home.bp)
app.register_blueprint(user.bp)
app.register_blueprint(auth.bp)


with app.app_context():
    db.create_all()