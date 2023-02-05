from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sns123456@localhost:5432/Doctorsforum'
app.config['SECRET_KEY'] = 'f5f992a46209111e6a694672'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_main'
login_manager.login_message_category = 'info'

from doctorsforum import main_urls
