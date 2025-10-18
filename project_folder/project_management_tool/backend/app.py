import os
from flask import Flask
from models import db

def create_app(config_name='default'):
    app = Flask(__name__)
    if config_name == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        db_user = os.environ.get('DB_USER', 'user')
        db_password = os.environ.get('DB_PASSWORD', 'password')
        db_host = os.environ.get('DB_HOST', 'localhost')
        db_name = os.environ.get('DB_NAME', 'pm_tool')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'

    db.init_app(app)

    from routes import api
    app.register_blueprint(api)

    return app
