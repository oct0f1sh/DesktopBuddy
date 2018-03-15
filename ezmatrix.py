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
                self.matrix.SetPixel(x, y, pixel.r, pixel.g, pixel.b)
        
    def draw_line(self, start, end, color):
        points = Geometry.get_points_in_line(start, end)
        
        for point in points:
            self.matrix.SetPixel(int(point.x), int(point.y), color.r, color.g, color.b)

    def draw_line_canvas(self, start, end, color, canvas):
        points = Geometry.get_points_in_line(start, end)

        for point in points:
            x = int(round(point.x, 0))
            y = int(round(point.y, 0))
            
            canvas[y][x] = color
        
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
        for pixel in range(self.matrix.width):
            canvas = self.draw_line_canvas(Point(0, pixel), Point(32, 31 - pixel), color, Canvas())
            self.draw_canvas(canvas)
            #print('({}, {}) ({}, {})'.format(0, pixel, 32, 32 - pixel))
            time.sleep(sleep)
            self.matrix.Clear()

    def test_rows(self):
        canvas = Canvas()
        for y in range(len(canvas)):
            if y % 3 == 0:
                color = Color(255, 0, 0)
            elif y % 3 == 1:
                color = Color(0, 255, 0)
            else:
                color = Color(0, 0, 255)
    
            for x in range(len(canvas[y])):
                canvas[y][x] = color

        return canvas

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
        points.append(end)
        
        return points
        
        
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return ('({}, {})'.format(self.x, self.y))
        
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
    top_l = Point(0, 0)
    top_r = Point(31, 0)
    bot_l = Point(0, 31)
    bot_r = Point(31, 31)
    
##    matrix.matrix.SetPixel(31, 0, 0, 0, 255)
##    matrix.matrix.SetPixel(0, 31, 0, 0, 255)
##    matrix.matrix.SetPixel(31, 31, 0, 0, 255)
##    matrix.matrix.SetPixel(0, 0, 0, 0, 255)
    
    #cvs = matrix.draw_line_canvas(Point(1, 1), Point(5, 5), Color(255, 0, 0), Canvas())
    
    cvs = matrix.draw_line_canvas(top_l, bot_r, Color(255,0,0), Canvas())
    cvs = matrix.draw_line_canvas(top_r, bot_l, Color(0,255,0), cvs)
    
    matrix.draw_canvas(cvs)