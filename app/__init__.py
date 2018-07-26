# -*- coding: utf-8 -*-
from os import urandom
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.update(SECRET_KEY=urandom(16))

    from .views.pages import blue_view
    app.register_blueprint(blue_view)

    socketio.init_app(app, logger=True, engineio_logger=True)
    return app
