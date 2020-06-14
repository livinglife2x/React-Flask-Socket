from flask import Flask, jsonify
from flask_socketio import SocketIO, send
from task import some_method
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*")

app.host = 'localhost'


@socketIo.on("message")
def handleMessage(msg):
    some_method(msg)
    return None

if __name__ == '__main__':
    socketIo.run(app)