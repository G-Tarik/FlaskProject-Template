# -*- coding: utf-8 -*-

from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    from .views.pages import blue_view
    app.register_blueprint(blue_view)

    socketio.init_app(app, logger=True, engineio_logger=True)
    return app
