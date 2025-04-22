from app.blueprints import home, user
from flask import Flask

app = Flask(__name__)

app.register_blueprint(home.bp)
app.register_blueprint(user.bp)

