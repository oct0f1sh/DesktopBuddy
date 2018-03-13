from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import random

class DoSomething():
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        options.cols = 32
        
        self.matrix = RGBMatrix(options = options)
        
    def run(self):
        for y in range(0, self.matrix.height):
            for x in range(0, self.matrix.width):
                self.matrix.SetPixel(x, y, random.randint(0,255), random.randint(0,255), random.randint(0,255))
                time.sleep(0.0001)
        
if __name__ == "__main__":
    thing = DoSomething()
    while True:
        thing.run()