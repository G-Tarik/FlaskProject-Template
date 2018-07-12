#!/usr/bin/python3

from app import create_app, socketio

if __name__ == '__main__':
    app =  create_app('config')
    socketio.run(app, '0.0.0.0', 5000)
