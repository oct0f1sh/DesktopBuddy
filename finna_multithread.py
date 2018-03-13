from ezmatrix import *
import threading

red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)

matrix = EzMatrix()

#matrix.rotate_square(1, red)

##class BigSquare(threading.Thread):
##    def __init__(self, time, color):
##        super(BigSquare, self).__init__()
##        self.time = time
##        self.color = color
##        
##    def run(self):
##        while True:
##            matrix.rotate_square(1, self.color)
##        
##class SmallSquare(threading.Thread):
##    def __init__(self, time, point, size, color):
##        super(SmallSquare, self).__init__()
##        self.time = time
##        self.point = point
##        self.size = size
##        self.color = color
##        
##    def run(self):
##        while True:
##            matrix.rotate_subsquare(self.point, self.size, self.time, self.color)

t = threading.Thread(target=matrix.rotate_square, args=(1, red))
t2 = threading.Thread(target=matrix.rotate_subsquare, args=(Point(10, 10), 10, 3, blue))
        
arr = [t, t2]

def rep():
    for thread in arr:
        thread.start()
    
    for thraed in arr:
        thread.join()