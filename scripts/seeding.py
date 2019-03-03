# -*- coding: utf-8 -*-
from datetime import datetime

from charity import create_app
from charity.models import db, User

app = create_app()

def add_first_user():
    with app.app_context():
        u = User(username='krerkkiat', password='1234')
        db.session.add(u)
        db.session.commit()