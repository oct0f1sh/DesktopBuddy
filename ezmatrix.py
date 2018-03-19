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

    def add_subcavas(self, canvas, subcanvas):
        cvs = canvas
        for y in range(len(subcanvas)):
            for x in range(len(subcanvas[y])):
                cvs[y][x] = subcanvas[y][x]

        return cvs
                
    def run_anim(self, anim, sleep):
        sleep = float(sleep) / float(self.matrix.height)
        for canvas in anim:
            self.draw_canvas(canvas)
            time.sleep(sleep)
            self.matrix.Clear()

    def draw_line_canvas(self, start, end, color, canvas):
        points = Geometry.get_points_in_line(start, end)

        for point in points:
            x = int(round(point.x, 0))
            y = int(round(point.y, 0))
            
            #print('({}, {})'.format(x, y))
            
            canvas[y][x] = color
        
        return canvas
            
    def rotate_square_canvas(self, color, canvas):
        cvs = canvas
        point_left = Point(0, 0)
        point_bottom = Point(0, 31)
        point_right = Point(31, 31)
        point_top = Point(31, 0)
        
        anim = []
        
        for _ in range(self.matrix.height - 1):
            cvs = self.draw_line_canvas(point_left, point_bottom, color, cvs)
            cvs = self.draw_line_canvas(point_bottom, point_right, color, cvs)
            cvs = self.draw_line_canvas(point_right, point_top, color, cvs)
            cvs = self.draw_line_canvas(point_top, point_left, color, cvs)
            
            point_left.y += 1
            point_bottom.x += 1
            point_right.y -= 1
            point_top.x -= 1
        
            anim.append(cvs)
            
            cvs = Canvas()
            
        return anim
        
    def rotate_subsquare_on_anim(self, point, size, color, anim):
        point_left = point
        point_bottom = Point(point_left.x, point_left.y + size)
        point_right = Point(point_bottom.x + size, point_bottom.y)
        point_top = Point(point_right.x, point_right.y - size)
        
        for i, canvas in enumerate(anim):
            wait = float(1/float(size)) * float(len(anim))
            
            if i != 0 and i % wait < 1:
                point_left.y += 1
                point_bottom.x += 1
                point_right.y -= 1
                point_top.x -= 1
            #else:
            anim[i] = self.draw_line_canvas(point_left, point_bottom, color, anim[i])
            anim[i] = self.draw_line_canvas(point_bottom, point_right, color, anim[i])
            anim[i] = self.draw_line_canvas(point_right, point_top, color, anim[i])
            anim[i] = self.draw_line_canvas(point_top, point_left, color, anim[i])
            
        return anim
    
    def draw_numer(self, number, point, color):
        cvs = Canvas()

        
        
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