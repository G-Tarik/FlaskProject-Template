#!/usr/bin/python3

from app import create_app, socketio

if __name__ == '__main__':
    app =  create_app('config.DevConfig')
    socketio.run(app, app.config['HOST'], app.config['PORT'])
