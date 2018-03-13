from ezmatrix import *
import threading

red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)

matrix = EzMatrix()

t = threading.Thread(target=matrix.rotate_square, args=(1, red))
t2 = threading.Thread(target=matrix.rotate_subsquare, args=(Point(10, 10), 10, 3, blue))
        
arr = [t, t2]

for thread in arr:
     thread.start()
    
 for thread in arr:
     thread.join()