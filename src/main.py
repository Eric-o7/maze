from graphics import Window, Line, Point
from cell import *
from maze import *

def main():
    win = Window(800,600)
    m = Maze(20,20,28,38,20,20,win)
    m.solve()
    win.wait_for_close()

main()

