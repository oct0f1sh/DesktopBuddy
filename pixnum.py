from ezmatrix import *

class NumCanvas():
    @staticmethod
    def small_num(number, color):
        o = Color.off()
        c = color
        
        if number == 1:
            cvs = [[o, c, o], #  X
                   [c, c, o], # XX
                   [o, c, o], #  X 
                   [o, c, o], #  X 
                   [o, c, o]] #  X
        if number == 2:
            cvs = [[c, c, c], # XXX
                   [o, o, c], #   X
                   [c, c, c], # XXX
                   [c, o, o], # X  
                   [c, c, c]] # XXX
        if number == 3:
            cvs = [[c, c, c], # XXX
                   [o, o, c], #   X
                   [c, c, c], # XXX
                   [o, o, c], #   X
                   [c, c, c]] # XXX
        if number == 4:
            cvs = [[c, o, c], # X X
                   [c, o, c], # X X
                   [c, c, c], # XXX
                   [o, o, c], #   X
                   [o, o, c]] #   X
        if number == 5:
            cvs = [[c, c, c], # XXX
                   [c, o, o], # X 
                   [c, c, c], # XXX
                   [o, o, c], #   X
                   [c, c, c]] # XXX
        if number == 6:
            cvs = [[c, c, c], # XXX
                   [c, o, o], # X  
                   [c, c, c], # XXX
                   [c, o, c], # X X
                   [c, c, c]] # XXX
        if number == 7:
            cvs = [[c, c, c], # XXX
                   [o, o, c], #   X
                   [o, o, c], #   X
                   [o, o, c], #   X
                   [o, o, c]] #   X
        if number == 8:
            cvs = [[c, c, c], # XXX
                   [c, o, c], # X X
                   [c, c, c], # XXX
                   [c, o, c], # X X
                   [c, c, c]] # XXX
        if number == 9:
            cvs = [[c, c, c], # XXX
                   [c, o, c], # X X
                   [c, c, c], # XXX
                   [o, o, c], #   X
                   [o, o, c]] #   X
        if number == 0:
            cvs = [[c, c, c], # XXX
                   [c, o, c], # X X
                   [c, o, c], # X X
                   [c, o, c], # X X
                   [c, c, c]] # XXX
        if number == 'deg':
            cvs = [[c, c], # XX
                   [c, c], # XX
                   [o, o], # 
                   [o, o], #
                   [o, o]] # 
        return cvs

    @staticmethod
    def big_num(number, color):
        o = Color.off()
        c = color
        
        if number == 1:
            cvs = [[o, o, o, c, o], #    X  
                   [o, o, c, c, o], #   XX
                   [o, o, o, c, o], #    X
                   [o, o, o, c, o], #    X
                   [o, o, o, c, o], #    X
                   [o, o, o, c, o], #    X
                   [o, o, o, c, o]] #    X
        if number == 2:
            cvs = [[c, c, c, c, c], # XXXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [c, c, c, c, c], # XXXXX
                   [c, o, o, o, o], # X    
                   [c, o, o, o, o], # X
                   [c, c, c, c, c]] # XXXXX
        if number == 3:
            cvs = [[c, c, c, c, c], # XXXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, c, c, c, c], #  XXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [c, c, c, c, c]] # XXXXX
        if number == 4:
            cvs = [[c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, c, c, c, c], # XXXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c]] #     X
        if number == 5:
            cvs = [[c, c, c, c, c], # XXXXX
                   [c, o, o, o, o], # X    
                   [c, o, o, o, o], # X    
                   [c, c, c, c, c], # XXXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [c, c, c, c, c]] # XXXXX
        if number == 6:
            cvs = [[c, c, c, c, c], # XXXXX
                   [c, o, o, o, o], # X    
                   [c, o, o, o, o], # X    
                   [c, c, c, c, c], # XXXXX
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, c, c, c, c]] # XXXXX
        if number == 7:
            cvs = [[c, c, c, c, c], # XXXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c]] #     X
        if number == 8:
            cvs = [[c, c, c, c, c], # XXXXX
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, c, c, c, c], # XXXXX
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, c, c, c, c]] # XXXXX
        if number == 9:
            cvs = [[c, c, c, c, c], # XXXXX
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, c, c, c, c], # XXXXX
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c], #     X
                   [o, o, o, o, c]] #     X
        if number == 0:
            cvs = [[c, c, c, c, c], # XXXXX
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, o, o, o, c], # X   X
                   [c, c, c, c, c]] # XXXXX
        if number == ':':
            cvs = [[o],             #
                   [o],             #
                   [c],             # X
                   [o],             # 
                   [c],             # X
                   [o],             #
                   [o]]             #
        return cvs
    
    @staticmethod
    def day_of_week(day, color):
        o = Color.off()
        c = color
        
        if day == 6:
            cvs = [[c, c, c, o, c, o, c, o, c, o, o, c],
                   [c, o, o, o, c, o, c, o, c, c, o, c],
                   [c, c, c, o, c, o, c, o, c, c, c, c],
                   [o, o, c, o, c, o, c, o, c, o, c, c],
                   [c, c, c, o, c, c, c, o, c, o, o, c]]
        if day == 0:
            cvs = [[c, o, o, c, o, c, c, c, o, c, o, o, c],
                   [c, c, c, c, o, c, o, c, o, c, c, o, c],
                   [c, c, c, c, o, c, o, c, o, c, c, c, c],
                   [c, o, o, c, o, c, o, c, o, c, o, c, c],
                   [c, o, o, c, o, c, c, c, o, c, o, o, c]]
        if day == 1:
            cvs = [[c, c, c, o, c, o, c, o, c, c, c],
                   [o, c, o, o, c, o, c, o, c, o, o],
                   [o, c, o, o, c, o, c, o, c, c, c],
                   [o, c, o, o, c, o, c, o, c, o, o],
                   [o, c, o, o, c, c, c, o, c, c, c]]
        if day == 2:
            cvs = [[c, o, o, c, o, c, c, c, o, c, c, o],
                   [c, o, o, c, o, c, o, o, o, c, o, c],
                   [c, c, c, c, o, c, c, c, o, c, o, c],
                   [c, c, c, c, o, c, o, o, o, c, o, c],
                   [c, o, o, c, o, c, c, c, o, c, c, o]]
        if day == 3:
            cvs = [[c, c, c, o, c, o, c, o, c, o, c],
                   [o, c, o, o, c, o, c, o, c, o, c],
                   [o, c, o, o, c, c, c, o, c, o, c],
                   [o, c, o, o, c, o, c, o, c, o, c],
                   [o, c, o, o, c, o, c, o, c, c, c]]
        if day == 4:
            cvs = [[c, c, c, o, c, c, c, o, c, c, c],
                   [c, o, o, o, c, o, c, o, o, c, o],
                   [c, c, o, o, c, c, c, o, o, c, o],
                   [c, o, o, o, c, c, o, o, o, c, o],
                   [c, o, o, o, c, o, c, o, c, c, c]]
        if day == 5:
            cvs = [[c, c, c, o, c, c, c, o, c, c, c],
                   [c, o, o, o, c, o, c, o, o, c, o],
                   [c, c, c, o, c, c, c, o, o, c, o],
                   [o, o, c, o, c, o, c, o, o, c, o],
                   [c, c, c, o, c, o, c, o, o, c, o]]
            
        return cvs