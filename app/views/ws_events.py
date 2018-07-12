from .. import socketio
import eventlet
from random import randint

# for sleep method
eventlet.monkey_patch()


def updateData():
    rnumber =randint(1,1000)
    resp = {'response': rnumber}
    return resp


def sendUpdateData():
    while True:
        emit_data = updateData()
        if emit_data:
            socketio.emit('UpdateData', emit_data)
        eventlet.sleep(2) # in seconds


@socketio.on('client_connected')
def ws_connect(cldata):
    socketio.emit('UpdateData', updateData())


# using eventlet for asynchronous websocket communication
eventlet.spawn_n(sendUpdateData)
