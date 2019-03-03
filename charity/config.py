# -*- config: utf-8 -*-
import os

class BaseConfig:
    SECRET = 'dev'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://{u}:{p}@ec2-18-235-225-4.compute-1.amazonaws.com:5432'.format(
        u=os.getenv('POSTGRES_USER', 'charity'),
        p=os.getenv('POSTGRES_PASSWORD', 'f0e92V0H3k64b8atxy0ysN1p')
    )

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False