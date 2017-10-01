from app import app, socketio
from flask import render_template
from flask_socketio import emit
#from sensors import Sensors, t1
import time
from random import randint




class Sensors:
    
    def __init__(self, timer, name):
        self.tw = time.time()
        self.th = time.time()
        self.timer = timer
        self.name = name
    
    def get_humid(self):
        #print("update_humid: ")
        if (t1 - self.tw >= self.timer):
            global humid
            humid = randint(70,79)
            #print("newHumid: %s\nDelay: %s" % (humid, (t1 -self.tw)))
            self.tw = time.time()
            return humid

        else:
            #print("Humid: %s" % humid)
            return humid
    
    def get_temp(self):
        #print("update_temp: ")
        if (t1 - self.th >= self.timer):
            global temp
            temp = randint(70,79)
            #print("newTemp: %s\nDelay: %s" % (temp, (t1 -self.th)))
            self.th = time.time()
            return temp
            
        else:
            #print("Temp: %s\nDelay: %s\nT1: %s\nTh: %s" % (temp, (t1 -self.th), t1, self.th))
            return temp


# Initialise sensor values
humid = "Calibrating"
temp = "Calibrating"
t1 = time.time()


# Assign variables to class Sensors (timer, name)
tempobj = Sensors(timer=2, name="temp") # Set time interval (4 seconds)
humidobj = Sensors(timer=2, name="humid") # Set time interval (2 seconds)

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
	global t1
	t1 = time.time()
	#print('t1: ')
	state = {
		"humid": humidobj.get_humid(),
		"temp": tempobj.get_temp()
	}
	emit('message', state)


