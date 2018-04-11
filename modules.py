from weather import Weather, Unit
from ezmatrix import *
from pixnum import *
import time
from datetime import datetime
import pytz
from PIL import Image
from operator import itemgetter

class Module():
    @staticmethod
    def get_temperature(unit, location):
        if unit == 'c':
            weather = Weather(unit=Unit.CELSIUS)
        else:
            weather = Weather(unit=Unit.FAHRENHEIT)
        
        location = weather.lookup_by_location(location)
        
        temp = location.condition().temp()
        
        print('got temperature as {} {} in {}'.format(temp, unit, location.location().city()))
        
        return temp
    
    @staticmethod
    def temperature_canvas(unit, location, color):
        temp = str(Module.get_temperature(unit, location))
    
        if len(temp) == 3:
            pass
        else:
            temp_pos1 = NumCanvas.small_num(int(temp[0]), color)
            temp_pos2 = NumCanvas.small_num(int(temp[1]), color)
            deg = NumCanvas.small_num('deg', color)
        
        cvs = Canvas(10, 5)
    
        cvs.add_subcanvas(temp_pos1).add_subcanvas(temp_pos2, Point(4, 0)).add_subcanvas(deg, Point(8, 0))
    
        return cvs
    
    @staticmethod
    def time_canvas(timezone, mon_color=Color.white(), day_color=Color.gray(), yr_color=Color.white(), hr_color=Color.red(), col_color=Color.red(), min_color=Color.red()):
        time = datetime.now(pytz.timezone(timezone))
        time_hr = time.strftime('%H')
        time_mn = time.strftime('%M')
        
        time_sec = int(time.strftime('%S'))
        
        date_mon = time.strftime('%m')
        date_day = time.strftime('%d')
        date_year = time.strftime('%y')
        
        if int(time_hr) > 12:
            if int(time_hr) - 12 >= 10:
                time_hr = str(int(time_hr) - 12)
            else:
                time_hr = '0' + str(int(time_hr) - 12)
            
##        month_pos1 = NumCanvas.small_num(int(date_mon[0]), mon_color)
##        month_pos2 = NumCanvas.small_num(int(date_mon[1]), mon_color)
##        
        day_pos1 = NumCanvas.small_num(int(date_day[0]), day_color)
        day_pos2 = NumCanvas.small_num(int(date_day[1]), day_color)
##        
##        year_pos1 = NumCanvas.small_num(int(date_year[0]), yr_color)
##        year_pos2 = NumCanvas.small_num(int(date_year[1]), yr_color)
            
        day_cvs = NumCanvas.day_of_week(datetime.today().weekday(), Color.white())
    
        hr_pos1 = NumCanvas.big_num(int(time_hr[0]), hr_color)
        hr_pos2 = NumCanvas.big_num(int(time_hr[1]), hr_color)
        
        if time_sec % 2 == 0:
            colon = NumCanvas.big_num(':', col_color)
        else:
            colon = Canvas(0,7)
        
        mn_pos1 = NumCanvas.big_num(int(time_mn[0]), min_color)
        mn_pos2 = NumCanvas.big_num(int(time_mn[1]), min_color)
        
        date_cvs = Canvas(25, 5)
        #date_cvs.add_subcanvas(month_pos1).add_subcanvas(month_pos2, Point(4, 0))
        #date_cvs.add_subcanvas(day_pos1, Point(9, 0)).add_subcanvas(day_pos2, Point(13, 0))
        #date_cvs.add_subcanvas(year_pos1, Point(18, 0)).add_subcanvas(year_pos2, Point(22, 0))
        date_cvs.add_subcanvas(day_cvs)
        date_cvs.add_subcanvas(day_pos1, Point(18, 0)).add_subcanvas(day_pos2, Point(22, 0))
    
        time_cvs = Canvas(25, 7)
        time_cvs.add_subcanvas(hr_pos1).add_subcanvas(hr_pos2, Point(6, 0))
        time_cvs.add_subcanvas(colon, Point(12, 0))
        time_cvs.add_subcanvas(mn_pos1, Point(14, 0)).add_subcanvas(mn_pos2, Point(20, 0))
        
        cvs = Canvas(25, 13)
        cvs.add_subcanvas(date_cvs)
        cvs.add_subcanvas(time_cvs, Point(0, 6))
    
        return cvs
    
    @staticmethod
    def image_canvas(img):
        remove_background = False
        
        width, height = img.size
        
        if width > 32 or height > 32:
            img = Module.resize_image(img)
            width, height = img.size
            
        cvs = Canvas(width, height)
        
        colors = img.getcolors(1000)
        
        common_color = max(colors, key=itemgetter(0))[1]
        
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x,y))
                if (r, g, b) == common_color and remove_background:
                    cvs[y][x] = Color.off()
                else:
                    cvs[y][x] = Color(r, g, b)
                
        return cvs
    
    @staticmethod
    def image_canvas_from_path(image_path):
        try:
            img = Image.open(image_path)
        except IOError:
            print('ERROR: FILE NOT FOUND')
            return Canvas()
        
        cvs = Module.image_canvas(img)
        
        return cvs
    
    @staticmethod
    def resize_image(img, new_width=32, new_height=32):
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        
        return img
    
    @staticmethod
    def gif_anim(gif_path):
        print('COMPILING GIF...')
        
        try:
            frame = Image.open(gif_path)
        except IOError:
            print('ERROR: FILE NOT FOUND')
            return []
        
        frames = 0
        
        anim = []
        
        while frame:
            cvs = Module.image_canvas(frame.convert('RGB'))
            anim.append(cvs)
            
            frames += 1
            
            print('frame {} compiled'.format(frames))
            
            try:
                frame.seek(frames)
            except EOFError:
                print('GIF COMPILED, LENGTH: {}'.format(frames))
                break
            
        return anim