from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

class Even_Odd_Flash():
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        options.cols = 32
        
        self.matrix = RGBMatrix(options = options)
        
    def set_color(self, r, g, b):
        for y in range(self.matrix.height):
            for x in range(self.matrix.width):
                if y % 2 == 0:
                    self.matrix.SetPixel(x, y, r, g, b)
        
    def run(self):
        for y in range(self.matrix.height):
            for x in range(self.matrix.width):
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.matrix.SetPixel(x, y, 0, 0, 255)
                else:
                    if x % 2 == 1:
                        self.matrix.SetPixel(x, y, 0, 255, 0)
                        
    def run_inv(self):
        for y in range(self.matrix.height):
            for x in range(self.matrix.width):
                if y % 2 == 1:
                    if x % 2 != 0:
                        self.matrix.SetPixel(x, y, 0, 0, 255)
                else:
                    if x % 2 != 1:
                        self.matrix.SetPixel(x, y, 0, 255, 0)
                        
    def run_anim(self):
        while True:
            self.run()
            time.sleep(1)
            self.set_color(0, 0, 0)
            self.run_inv()
            time.sleep(1)
            self.set_color(0, 0, 0)
            
    def snake(self):
        pass
            
if __name__ == "__main__":
    nice = Even_Odd_Flash()
    nice.run_anim()
    