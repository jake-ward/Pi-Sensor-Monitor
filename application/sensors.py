from random import randint
import time



#t1 = time.time()

class Sensors:
    
    def __init__(self, interval, value):
        self.humid_timer = time.time()
        self.temp_timer = time.time()
        self.interval = interval
        self.value = "Calibrating..."

    def update_humid(self, timer):
        # Update humidity if time interval has passed
        if (timer - self.humid_timer >= self.interval):
            self.value = randint(10,19)
            # Restart humid timer
            self.humid_timer = time.time()
            return self.value

        else:
            return self.value
    
    def update_temp(self, timer):
        # Update temperature if time interval has passed
        if (timer - self.temp_timer >= self.interval):
            self.value = randint(10,19)
            # Restart interval timer
            self.temp_timer = time.time()
            return self.value

        else:
            return self.value
