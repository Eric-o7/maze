from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(50, 50, 150, 150)
    c2 = Cell(win)
    c2.has_top_wall = False
    c2.has_right_wall = False
    c2.draw(50, 150, 150, 250)
    c.draw_move(c2)
    c3 = Cell(win)
    c3.has_left_wall = False
    c3.draw(150, 150, 250, 250)
    c2.draw_move(c3)
    win.wait_for_close()

main()

