from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    id = db.Columns(db.Integer, primary_key=True)
    username = db.Columns(db.String, primary_key=True, unique)
