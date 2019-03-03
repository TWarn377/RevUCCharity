from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    created = db.Column(db.DateTime, server_default=func.now())
    modified = db.Column(db.DateTime, onupdate=func.now())
    username = db.Column(db.String, primary_key=True, unique=True)
    password = db.Column(db.String)

    donations = relationship('Donation', back_populates='user')

class Donation(db.Model):
    __tablename__ = 'donation'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('User', back_populates='donations')

    created = db.Column(db.DateTime, server_default=func.now())
    amount = db.Column(db.Float)

class Organization(db.Model):
    __tablename__ = 'organization'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    created = db.Column(db.DateTime, server_default=func.now())
    
    name = db.Column(db.String)
    url = db.Column(db.String)