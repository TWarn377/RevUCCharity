# -*- coding: utf-8 -*-
import os
import json

from flask import Flask, render_template, request
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

    app.config.from_mapping(
        SECRET_KEY='dev',
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

    @app.route('/charities', methods=['GET' ,])
    def charities_page():
        return render_template('charities.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
