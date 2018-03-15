from ezmatrix import *

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
##    top_l = Point(0, 0)
##    top_r = Point(31, 0)
##    bot_l = Point(0, 31)
##    bot_r = Point(31, 31)
##    
##    cvs = matrix.draw_line_canvas(top_l, bot_r, Color(255,0,0), Canvas())
##    cvs = matrix.draw_line_canvas(top_r, bot_l, Color(0,255,0), cvs)
##    
##    matrix.draw_canvas(cvs)
    
    matrix.draw_anim(anim, 1)