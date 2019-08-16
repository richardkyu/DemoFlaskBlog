from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f2efa08a181e856e3251026e42da759'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#Need this line for the login_required functionality to work. Pass in the def associated with login.
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes