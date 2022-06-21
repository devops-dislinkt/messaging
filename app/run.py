import eventlet

eventlet.monkey_patch()
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from create_app import create_app
from flask_cors import CORS, cross_origin

flask_app = create_app()
cors = CORS(flask_app)
flask_app.config['CORS_HEADERS'] = 'Content-Type'

socketio = SocketIO(flask_app, engineio_logger=False, async_mode="eventlet", cors_allowed_origins='*', path="messages")


username_to_sid = {}
sid_to_username = {}


@flask_app.route("/user1")
def user1():
    return render_template("user1.html")


@flask_app.route("/user2")
def user2():
    return render_template("user2.html")


@socketio.on("connect")
def connect():
    print("User connected", request.sid)


@socketio.on("username")
def add_user_connection(username):
    username_to_sid[username] = request.sid
    sid_to_username[request.sid] = username


@socketio.on("new-message")
def add_user_connection(data):
    message = {"value": data["message"], "from": sid_to_username[request.sid]}
    socketio.emit("response", to=username_to_sid[data["to_whom"]], data=message)


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    socketio.run(flask_app, host="0.0.0.0", port=8092)
