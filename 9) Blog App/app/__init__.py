import os
from dotenv import load_dotenv
from flask import Flask, render_template
from datetime import timedelta
from app.database import init_db
from app.routes.auth_routes import auth_routes
from app.routes.user_routes import user_routes
from app.routes.blog_routes import blog_routes
from app.routes.home_routes import home_routes
from app.utils.encryption import encrypt_id

load_dotenv()

#static folder path setup
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
static_folder = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, static_folder=static_folder)

#required for session login
app.secret_key = os.getenv('APP_SECRET_KEY')
app.permanent_session_lifetime = timedelta(days=7) #making session persistent
#required for session login

#static folder path setup, only required when folder is outside of app folder
app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')

init_db()

#to make the encrypt_id() function inside jinja template
app.jinja_env.globals['encrypt_id'] = encrypt_id


@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/notFound.html'), 404

#global exception handling
@app.errorhandler(Exception)
def handle_global_exception(e):
    print(f"[ERROR] {str(e)}")

    return render_template('home/notFound.html'), 404

app.register_blueprint(auth_routes)
app.register_blueprint(home_routes)
app.register_blueprint(user_routes)
app.register_blueprint(blog_routes)
