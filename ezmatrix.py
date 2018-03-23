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
                
    def run_anim(self, anim, sleep):
        sleep = float(sleep) / float(self.matrix.height)
        for canvas in anim:
            self.draw_canvas(canvas)
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
    
    @classmethod
    def red(cls):
        return cls(255, 0, 0)
    
    @classmethod
    def green(cls):
        return cls(0, 255, 0)
    
    @classmethod
    def blue(cls):
        return cls(0, 0, 255)
    
    @classmethod
    def gray(cls):
        return cls(128, 128, 128)
    
    @classmethod
    def white(cls):
        return cls(255, 255, 255)
    
    @classmethod
    def off(cls):
        return cls(0, 0, 0)

class Canvas(list):
    def __init__(self, width=32, height=32):
        lst = []
        for row in range(height):
            color_row = []
            for col in range(width):
                color_row.append(Color.off())
            self.append(color_row)
        self = lst
    
    def add_subcanvas(self, subcanvas, translation=Point(0, 0)):
        # adding a translation of Point(3, 3) would move the
        # subcanvas right 3 and down 3
        # translation: must be a Point
        for y in range(len(subcanvas)):
            for x in range(len(subcanvas[y])):
                self[y + translation.y][x + translation.x] = subcanvas[y][x]
                
        return self
    
    def draw_line(self, start, end, color):
        points = Geometry.get_points_in_line(start, end)

        for point in points:
            x = int(round(point.x, 0))
            y = int(round(point.y, 0))
            
            #print('({}, {})'.format(x, y))
            
            self[y][x] = color
        
        return self
    
    def draw_rectangle(self, top_l, top_r, bot_l, bot_r, color):
        self.draw_line(top_l, bot_l, color)
        self.draw_line(bot_l, bot_r, color)
        self.draw_line(bot_r, top_r, color)
        self.draw_line(top_r, top_l, color)
        
        return self
    
class Animation(list):
    def __init__(self, length=32):
        lst = []
        
        for i in range(length):
            self.append(Canvas())
            
        self = lst
        
    def rect_rotation(self, point, size, color):
        point_left = point
        point_bottom = Point(point_left.x, point_left.y + size)
        point_right = Point(point_bottom.x + size, point_bottom.y)
        point_top = Point(point_right.x, point_right.y - size)
        
        for i, canvas in enumerate(self):
            wait = float(1/float(size)) * float(len(self))
            
            if i != 0 and i % wait < 1:
                point_left.y += 1
                point_bottom.x += 1
                point_right.y -= 1
                point_top.x -= 1
                
            self[i] = canvas.draw_line(point_left, point_bottom, color)
            self[i] = canvas.draw_line(point_bottom, point_right, color)
            self[i] = canvas.draw_line(point_right, point_top, color)
            self[i] = canvas.draw_line(point_top, point_left, color)
            
        return self