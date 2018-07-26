# -*- coding: utf-8 -*-
from os import urandom
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(app_config, db_config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    app.config.update(SECRET_KEY=urandom(16),
                      SQLALCHEMY_DATABASE_URI=db_config.URI)

    from .views.pages import blue_view
    app.register_blueprint(blue_view)

    from app.models import db
    db.init_app(app)

    socketio.init_app(app, logger=True, engineio_logger=True)
    return app
