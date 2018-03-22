from ezmatrix import *

class NumCanvas():
    @staticmethod
    def small_num(number, color):
        o = Color(0,0,0)
        c = color
        # numbers have a sub-canvas size of 3x5 pixels
        cvs = Canvas(3, 5)
        if number == 1:
            cvs = [[o, c, o], #  X
                   [c, c, o], # XX
                   [o, c, o], #  X 
                   [o, c, o], #  X 
                   [c, c, c]] # XXX
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
        return cvs

    @staticmethod
    def big_num(number, color):
        o = Color(0,0,0)
        c = color
        if number == 1:
            cvs = [[o, o, c, o, o], #   X  
                   [o, c, c, o, o], #  XX
                   [c, o, c, o, o], # X X
                   [o, o, c, o, o], #   X
                   [o, o, c, o, o], #   X
                   [o, o, c, o, o], #   X
                   [c, c, c, c, c]] # XXXXX
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