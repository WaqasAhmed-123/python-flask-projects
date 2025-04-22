from flask import Flask
from app.database import init_db
from app.routes.user import user_routes

app = Flask(__name__)

init_db()

app.register_blueprint(user_routes)
