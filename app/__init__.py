from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SECRET_KEY'] = 'testtesttest'
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import register_views
    app.register_blueprint(register_views.bp)

    return app