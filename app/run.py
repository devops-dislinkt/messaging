import eventlet

eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO

flask_app = create_app()
socketio = SocketIO(flask_app, engineio_logger=False, async_mode="eventlet")


if __name__ == "__main__":
    socketio.start_background_task(emit_notif)
    socketio.run(flask_app, host="0.0.0.0", port=8092)
