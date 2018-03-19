from ezmatrix import *

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
        
def disp_num():
    matrix = EzMatrix()
    
    cvs = PixNum.canvas_for_num(2, Color(0, 255, 0))
    
    cvs = matrix.add_subcavas(Canvas(), cvs)
    
    while True:
        
        matrix.draw_canvas(cvs)
        
disp_num()