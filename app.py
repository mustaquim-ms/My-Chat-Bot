# pip install flask flask-socketio eventlet


from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from chatbot import Chatbot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

chatbot = Chatbot()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    response = chatbot.respond(msg)
    emit('response', response)

if __name__ == '__main__':
    socketio.run(app, debug=True)
