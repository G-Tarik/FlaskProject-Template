#!/usr/bin/python3

from app import create_app, socketio
import app_config, db_config

if __name__ == '__main__':
    app =  create_app(app_config.DevConfig, db_config.PGSQL)
    socketio.run(app, app.config['HOST'], app.config['PORT'])
