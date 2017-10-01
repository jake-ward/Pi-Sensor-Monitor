from application import app, socketio
from flask import render_template
from flask_socketio import emit
from sensors import Sensors
import time
from random import randint



# Assign variables to class Sensors (timer, name)
tempobj = Sensors(interval=2, value="temp") # Set time interval
humidobj = Sensors(interval=4, value="humid") # Set time interval

# Home page
@app.route('/')
def index():
	return render_template('home.html')

# Connect to client
@socketio.on('connect', namespace='/')
def test_connect():
	emit('my response', {'data': 'Connected'})

# Disconnect from client
@socketio.on('disconnect', namespace='/')
def test_disconnect():
	print('Client disconnected')

# Send JSON message to client
@socketio.on('my_event', namespace='/')
def test_message(message):
	# Timer running for delay events
	global timer
	timer = time.time()
	# Retrieve sensor data from Sensors class.
	state = {
		"humid": humidobj.update_humid(timer),
		"temp": tempobj.update_temp(timer)
	}
	emit('message', state)


