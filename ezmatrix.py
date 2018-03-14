from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import math
import random

class EzMatrix(object):
    def __init__(self, rows=32, cols=32, chain_length=1):
        options = RGBMatrixOptions()
        options.rows = rows
        options.chain_length = chain_length
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        options.cols = cols
        
        self.matrix = RGBMatrix(options = options)
        
    def draw_canvas(self, canvas):
        for y in range(len(canvas)):
            for x in range(len(canvas[y])):
                pixel = canvas[y][x]
                self.matrix.SetPixel(x + 1, y + 1, pixel.r, pixel.g, pixel.b)
        
    def draw_line(self, start, end, color):
        points = Geometry.get_points_in_line(start, end)
        
        for point in points:
            self.matrix.SetPixel(int(point.x), int(point.y), color.r, color.g, color.b)

    def draw_line_canvas(self, start, end, color, canvas):
        points = Geometry.get_points_in_line(start, end)

        for point in points:
            x = int(point.x)
            y = int(point.y)
            
            canvas[y][x - 1] = color

        return canvas
            
    def test_line(self, sleep, color):
        i = 0
        for pixel in range(self.matrix.width):
            #print('({}, {}) ({}, {})'.format(0, i, 32, 32 - i))
            self.draw_line(Point(0, i), Point(33, 32 - i), color)
            time.sleep(sleep)
            i += 1
            self.matrix.Clear()

    def test_line_canvas(self, sleep, color):
        for pixel in range(self.matrix.width + 1):
            canvas = self.draw_line_canvas(Point(0, pixel), Point(32, 32 - pixel), color, Canvas())
            self.draw_canvas(canvas)
            print('({}, {}) ({}, {})'.format(0, pixel, 32, 32 - pixel))
            time.sleep(sleep)
            self.matrix.Clear()

    def rotate_square(self, sleep, color):
        sleep = float(sleep) / float(self.matrix.height)
        
        point_left = Point(0, 0)
        point_bottom = Point(0, 31)
        point_right = Point(31, 31)
        point_top = Point(31, 0)
        
        for _ in range(32):
            point_left.y += 1
            point_bottom.x += 1
            point_right.y -= 1
            point_top.x -= 1
            
            self.draw_line(point_left, point_bottom, color)
            self.draw_line(point_bottom, point_right, color)
            self.draw_line(point_right, point_top, color)
            self.draw_line(point_top, point_left, color)
            
            time.sleep(sleep)
            self.matrix.Clear()
            
    def rotate_subsquare(self, point, size, sleep, color):
        sleep = float(sleep) / float(self.matrix.height)
        
        point_left = point
        point_bottom = Point(point_left.x, point_left.y + size)
        point_right = Point(point_bottom.x + size, point_bottom.y)
        point_top = Point(point_right.x, point_right.y - size)
        
        for _ in range(size):
            point_left.y += 1
            point_bottom.x += 1
            point_right.y -= 1
            point_top.x -= 1
            
            self.draw_line(point_left, point_bottom, color)
            self.draw_line(point_bottom, point_right, color)
            self.draw_line(point_right, point_top, color)
            self.draw_line(point_top, point_left, color)
            
            time.sleep(sleep)
            self.matrix.Clear()
        
        
        
class Geometry():
    @staticmethod
    def distance(start, end):
        dx = end.x - start.x
        dy = end.y - start.y
        
        dx = dx ** 2
        dy = dy ** 2
        
        return math.sqrt(dx + dy)

    @staticmethod
    # linear interpolation
    # takes in single value integers, not points
    def lirp(start, end, t):
        return start + t * (end - start)
    
    @staticmethod
    def lirp_points(start, end, t):
        return Point(Geometry.lirp(start.x, end.x, t), Geometry.lirp(start.y, end.y, t))
    
    @staticmethod
    def get_points_in_line(start, end):
        num_points = Geometry.distance(start, end)
        points = []
        for i in range(int(num_points)):
            t = float(i) / float(num_points)
            points.append(Geometry.lirp_points(start, end, t))
        return points
        
        
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __repr__(self):
        return('(R:{} G:{} B:{})'.format(self.r, self.g, self.b))

class Canvas(list):
    def __init__(self, width=32, height=32):
        lst = []
        for row in range(height):
            color_row = []
            for col in range(width):
                color_row.append(Color(0,0,0))
            self.append(color_row)
        self = lst
        
        
matrix = EzMatrix()

# while True:
#     color = Color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
#     #matrix.rotate_square(0.5, color)
#     matrix.nice(0.01, color)

cvs = Canvas()
while True:
    matrix.test_line_canvas(0.5, Color(255, 0, 0))
    #cvs = matrix.draw_line_canvas(Point(0,0), Point(31, 31), Color(0, 255, 0), Canvas())
    #matrix.draw_canvas(cvs)
    #matrix.test_line(0.5, Color(255, 0, 0))