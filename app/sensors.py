from random import randint
import time


#def get_humid():
#	while True:
#		sleep(1)
#		humid = randint(70,79)
#		return humid

#def get_temp():
#	temp = randint(70,79)
#	return temp


class Sensors:
    timer = 0
    def __init__(self):
        self.tw = time.time()
        self.th = time.time()
    
    def get_humid(self, t1):
        if (t1 - self.tw >= self.timer):
			humid = randint(70,79)
			self.tw = time.time()
			return humid

    def get_temp(self, t1):
        if (t1 - self.th >= self.timer):
			temp = randint(70,79)
			self.th = time.time()
			return temp
        else:
            return 4

t1 = time.time()