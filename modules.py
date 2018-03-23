from weather import Weather, Unit
from ezmatrix import *
from pixnum import *

class Modules():
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
        red = Color(255, 0, 0)
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