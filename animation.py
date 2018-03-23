from ezmatrix import *
from pixnum import *
import time
import pytz
from datetime import datetime
import sys
from modules import Module

def run_anim():
    matrix = EzMatrix()
    
    anim = Animation().rect_rotation(Point(0, 0), 31, Color.red())
    anim.rect_rotation(Point(2, 2), 27, Color.green())
    anim.rect_rotation(Point(4, 4), 23, Color.blue())
    anim.rect_rotation(Point(6, 6), 19, Color.red())
    anim.rect_rotation(Point(8, 8), 15, Color.green())
    anim.rect_rotation(Point(10, 10), 11, Color.blue())
    anim.rect_rotation(Point(12, 12), 7, Color.red())
    anim.rect_rotation(Point(14, 14), 3, Color.green())
    
    while True:
        matrix.run_anim(anim, 1)
        
def test_nums():
    matrix = EzMatrix()
    
    for i in range(10):
        cvs = Canvas()
        
        subcvs_0 = NumCanvas.small_num(i - 1, Color.white())
        cvs.add_subcanvas(subcvs_0)
        
        subcvs_1 = NumCanvas.small_num(i, Color.white())
        cvs.add_subcanvas(subcvs_1, Point(5, 5))
        
        matrix.draw_canvas(cvs)
        
        time.sleep(1)
        
def num_cycle():
    matrix = EzMatrix()
    for i in range(10):
        b_cvs = NumCanvas.big_num(i, Color.red())
        s_cvs = NumCanvas.small_num(i, Color.red())
        
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
    
    cvs.draw_line(top_l, bot_l, Color.blue())
    cvs.draw_line(bot_l, bot_r, Color.blue())
    cvs.draw_line(bot_r, top_r, Color.blue())
    cvs.draw_line(top_r, top_l, Color.blue())
    
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