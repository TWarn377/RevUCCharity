# -*- coding: utf-8 -*-
from datetime import datetime

from charity import create_app
from charity.models import db, User

if __name__ == '__main__':
    # Create app and push context.
    app = create_app()
    with app.app_context():
        u = User(username='krerkkiat', password='1234')
        db.session.add(u)
        db.session.commit()