from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
# banco = sqlite3.connect('splan.db')