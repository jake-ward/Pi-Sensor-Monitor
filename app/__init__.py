#from eventlet import monkey_patch
#monkey_patch()


from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
socketio = SocketIO(app)


import app.views
