from ezmatrix import *
from pixnum import *
import time
import pytz
from datetime import datetime
import sys
from modules import Module
    
green = Color(0, 255, 0)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
gray = Color(128, 128, 128)
white = Color(255, 255, 255)
off = Color(0, 0, 0)

def run_anim():
    matrix = EzMatrix()
    
    anim = Animation().rect_rotation(Point(0, 0), 31, red)
    anim.rect_rotation(Point(2, 2), 27, green)
    anim.rect_rotation(Point(4, 4), 23, blue)
    anim.rect_rotation(Point(6, 6), 19, red)
    anim.rect_rotation(Point(8, 8), 15, green)
    anim.rect_rotation(Point(10, 10), 11, blue)
    anim.rect_rotation(Point(12, 12), 7, red)
    anim.rect_rotation(Point(14, 14), 3, green)
    
    while True:
        matrix.run_anim(anim, 1)
        
def test_nums():
    matrix = EzMatrix()
    
    for i in range(10):
        cvs = Canvas()
        
        subcvs_0 = NumCanvas.small_num(i - 1, white)
        cvs.add_subcanvas(subcvs_0)
        
        subcvs_1 = NumCanvas.small_num(i, white)
        cvs.add_subcanvas(subcvs_1, Point(5, 5))
        
        matrix.draw_canvas(cvs)
        
        time.sleep(1)
        
def num_cycle():
    matrix = EzMatrix()
    for i in range(10):
        b_cvs = NumCanvas.big_num(i, red)
        s_cvs = NumCanvas.small_num(i, red)
        
        cvs = Canvas().add_subcanvas(b_cvs).add_subcanvas(s_cvs, Point(6, 0))
        
        matrix.draw_canvas(cvs)
        
        time.sleep(1)
        
def clock():
    matrix = EzMatrix()
    
    while True:
        matrix.draw_canvas(Canvas().add_subcanvas(Module.time_canvas('US/Pacific'), Point(3, 9)))
        
        
def draw_rect():
    top_l = Point(0, 0)
    top_r = Point(7, 0)
    bot_r = Point(7, 9)
    bot_l = Point(0, 9)
    
    matrix = EzMatrix()
    cvs = Canvas()
    
    cvs.draw_line(top_l, bot_l, blue)
    cvs.draw_line(bot_l, bot_r, blue)
    cvs.draw_line(bot_r, top_r, blue)
    cvs.draw_line(top_r, top_l, blue)
    
    while True:
        matrix.draw_canvas(cvs)
        

def draw_temp(ref_rate=3):
    temp_cvs = Module.temperature_canvas('f', 'san francisco', Color.red())
    
    ref_rate = ref_rate * 60
    
    tme = int(time.time())
    
    matrix = EzMatrix()
    
    while True:
        if int(time.time()) - tme == ref_rate:
            print('get temp')
            
            temp_cvs = Module.temperature_canvas('f', 'san francisco', Color.red())
            tme = int(time.time())
            
        time_cvs = Canvas().add_subcanvas(Module.time_canvas('US/Pacific'), Point(3, 9))
        
        time_cvs.add_subcanvas(temp_cvs, Point(18, 3))
        
        matrix.draw_canvas(time_cvs)
        
    

if sys.argv[1] == 'clock':
    clock()
elif sys.argv[1] == 'rect':
    run_anim()
elif sys.argv[1] == 'temp':
    draw_temp(1)