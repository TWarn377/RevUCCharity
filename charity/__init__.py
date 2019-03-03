# -*- coding: utf-8 -*-
import os
import json

from flask import Flask, render_template
from flask_migrate import Migrate

from charity.models import db, Donation

config = {
    'default': 'charity.config.DevelopmentConfig',
    'development': 'charity.config.DevelopmentConfig',
    'production': 'charity.config.ProductionConfig',
}

def create_app():
    app = Flask(__name__,
        static_url_path='/static'
    )

    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from charity.models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import api
    app.register_blueprint(api.bp)

    # Views.
    @app.route('/')
    def index():
        # Query data form database.
        result = Donation.query.all()

        return render_template('index.html', donations=result)

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'GET':
            # Redner the page.
            return render_template('login.html')
        else:
            pass

    @app.route('/signup', methods=['POST', 'GET'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')

        elif request.method == 'POST':

            c = usercon.cursor()

            c.execute('''CREATE TABLE users (nvarchar(319) email, nvarchar(32) pswrd)''')


    @app.route('/charities', methods=['GET' ,])
    def charities_page():
        return render_template('Charities.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
