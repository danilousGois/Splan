from flask_sqlalchemy import SQLAlchemy
import sqlite3

db = SQLAlchemy()

banco = sqlite3.connect('splan.db')