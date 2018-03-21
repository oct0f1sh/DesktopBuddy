from ezmatrix import *
from pixnum import *
import time
import pytz
from datetime import datetime

def run_anim():
    matrix = EzMatrix()

    cvs = Canvas()

    anim = matrix.rotate_square_canvas(Color(0, 255, 0), cvs)
    anim = matrix.rotate_subsquare_on_anim(Point(2, 2), 27, Color(255, 0, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(4, 4), 23, Color(0, 0, 255), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(6, 6), 19, Color(0, 255, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(8, 8), 15, Color(255, 0, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(10, 10), 11, Color(0, 0, 255), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(12, 12), 7, Color(0, 255, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(14, 14), 3, Color(255, 0, 0), anim)

    while True:
    
        matrix.run_anim(anim, 1)

def test():
    matrix = EzMatrix()
    
    anim = Animation().rect_rotation(Point(8, 8), 15, Color(255, 0, 0))
    
    while True:
        matrix.run_anim(anim, 1)
        
def test_nums():
    matrix = EzMatrix()
    
    for i in range(10):
        cvs = Canvas()
        
        subcvs_0 = NumCanvas.small_num(i - 1, Color(255, 0, 0))
        cvs.add_subcanvas(subcvs_0)
        
        subcvs_1 = NumCanvas.small_num(i, Color(0, 0, 255))
        cvs.add_subcanvas(subcvs_1, Point(5, 5))
        
        matrix.draw_canvas(cvs)
        
        time.sleep(1)
        
def clock():
    matrix = EzMatrix()
    
    green = Color(0, 0, 255)
    red = Color(255, 0, 0)
    blue = Color(0, 255, 0)
    gray = Color(128, 128, 128)
    white = Color(255, 255, 255)
    
    while True:
        time = datetime.now(pytz.timezone('US/Pacific'))
        time_hr = time.strftime('%H')
        time_mn = time.strftime('%M')
        
        time_sec = int(time.strftime('%S'))
        
        date_mon = time.strftime('%m')
        date_day = time.strftime('%d')
        date_year = time.strftime('%y')
        
        if int(time_hr) > 12:
            time_hr = '0' + str(int(time_hr) - 12)
            
        month_pos1 = NumCanvas.small_num(int(date_mon[0]), white)
        month_pos2 = NumCanvas.small_num(int(date_mon[1]), white)
        
        day_pos1 = NumCanvas.small_num(int(date_day[0]), gray)
        day_pos2 = NumCanvas.small_num(int(date_day[1]), gray)
        
        year_pos1 = NumCanvas.small_num(int(date_year[0]), white)
        year_pos2 = NumCanvas.small_num(int(date_year[1]), white)
    
        hr_pos1 = NumCanvas.big_num(int(time_hr[0]), Color(255, 0, 0))
        hr_pos2 = NumCanvas.big_num(int(time_hr[1]), Color(255, 0, 0))
        
        if time_sec % 2 == 0:
            colon = NumCanvas.big_num(':', Color(255, 0, 0))
        else:
            colon = Canvas(0,7)
        
        mn_pos1 = NumCanvas.big_num(int(time_mn[0]), Color(0, 0, 255))
        mn_pos2 = NumCanvas.big_num(int(time_mn[1]), Color(0, 0, 255))
        
        date_cvs = Canvas(25, 5)
        date_cvs.add_subcanvas(month_pos1).add_subcanvas(month_pos2, Point(4, 0))
        date_cvs.add_subcanvas(day_pos1, Point(9, 0)).add_subcanvas(day_pos2, Point(13, 0))
        date_cvs.add_subcanvas(year_pos1, Point(18, 0)).add_subcanvas(year_pos2, Point(22, 0))
    
        time_cvs = Canvas(25, 7)
        time_cvs.add_subcanvas(hr_pos1).add_subcanvas(hr_pos2, Point(6, 0))
        time_cvs.add_subcanvas(colon, Point(12, 0))
        time_cvs.add_subcanvas(mn_pos1, Point(14, 0)).add_subcanvas(mn_pos2, Point(20, 0))
        
        cvs = Canvas(25, 13)
        cvs.add_subcanvas(date_cvs)
        cvs.add_subcanvas(time_cvs, Point(0, 6))
        
        canvas = Canvas().add_subcanvas(cvs, Point(3, 9))
    
        matrix.draw_canvas(canvas)
        
def num_cycle():
    matrix = EzMatrix()
    for i in range(10):
        b_cvs = NumCanvas.big_num(i, Color(255, 0, 0))
        s_cvs = NumCanvas.small_num(i, Color(255, 0, 0))
        
        cvs = Canvas().add_subcanvas(b_cvs).add_subcanvas(s_cvs, Point(6, 0))
        
        matrix.draw_canvas(cvs)
        
        time.sleep(1)
        
        
def draw_rect():
    top_l = Point(0, 0)
    top_r = Point(7, 0)
    bot_r = Point(7, 9)
    bot_l = Point(0, 9)
    
    matrix = EzMatrix()
    cvs = Canvas()
    blue = Color(0, 0, 255)
    
    cvs.draw_line(top_l, bot_l, blue)
    cvs.draw_line(bot_l, bot_r, blue)
    cvs.draw_line(bot_r, top_r, blue)
    cvs.draw_line(top_r, top_l, blue)
    
##    cvs = matrix.draw_line_canvas(top_l, bot_l, Color(0, 0, 255), Canvas())
##    cvs = matrix.draw_line_canvas(bot_l, bot_r, Color(0, 0, 255), cvs)
##    cvs = matrix.draw_line_canvas(bot_r, top_r, Color(0, 0, 255), cvs)
##    cvs = matrix.draw_line_canvas(top_r, top_l, Color(0, 0, 255), cvs)
##    
    while True:
        matrix.draw_canvas(cvs)
        
test()