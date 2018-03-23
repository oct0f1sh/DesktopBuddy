from weather import Weather, Unit
from ezmatrix import *
from pixnum import *
import time
from datetime import datetime
import pytz

green = Color(0, 255, 0)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
gray = Color(128, 128, 128)
white = Color(255, 255, 255)
off = Color(0, 0, 0)

class Module():
    @staticmethod
    def get_temperature(unit, location):
        if unit == 'c':
            weather = Weather(unit=Unit.CELSIUS)
        else:
            weather = Weather(unit=Unit.FAHRENHEIT)
        
        location = weather.lookup_by_location(location)
        
        temp = location.condition().temp()
        
        return temp
    
    @staticmethod
    def get_temperature_canvas():
        temp = str(Modules.get_temperature('f', 'san francisco'))
    
        if len(temp) == 3:
            pass
        else:
            temp_pos1 = NumCanvas.small_num(int(temp[0]), red)
            temp_pos2 = NumCanvas.small_num(int(temp[1]), red)
            deg = NumCanvas.small_num('deg', red)
        
        cvs = Canvas(11, 5)
    
        cvs.add_subcanvas(temp_pos1).add_subcanvas(temp_pos2, Point(4, 0)).add_subcanvas(deg, Point(8, 0))
    
        return cvs
    
    @staticmethod
    def get_time_canvas():
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
    
        hr_pos1 = NumCanvas.big_num(int(time_hr[0]), red)
        hr_pos2 = NumCanvas.big_num(int(time_hr[1]), red)
        
        if time_sec % 2 == 0:
            colon = NumCanvas.big_num(':', red)
        else:
            colon = Canvas(0,7)
        
        mn_pos1 = NumCanvas.big_num(int(time_mn[0]), blue)
        mn_pos2 = NumCanvas.big_num(int(time_mn[1]), blue)
        
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
        
##        # rectangle points
##        top_l = Point(2, 8)
##        bot_l = Point(2, 22)
##        bot_r = Point(28, 22)
##        top_r = Point(28, 8)
##        
##        canvas = Canvas().add_subcanvas(cvs, Point(3, 9)).draw_rectangle(top_l, top_r, bot_l, bot_r, off)
##        canvas.add_subcanvas(temperature_cvs)
    
        return cvs