from graphics import *

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        #broken cell walls are redrawn in white
        #removing the walls in memory does not update the canvas
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill = "red"
        else:
            fill = "gray"
        center_self = Point(((self._x1+self._x2)/2),((self._y1+self._y2)/2))
        center_to_cell = Point(((to_cell._x1+to_cell._x2)/2),((to_cell._y1+to_cell._y2)/2))
        line = Line(center_self, center_to_cell)
        if self.has_bottom_wall == False and to_cell.has_top_wall == False:
            self._win.draw_line(line, fill)
        elif self.has_top_wall == False and to_cell.has_bottom_wall == False:
            self._win.draw_line(line, fill)
        elif self.has_right_wall == False and to_cell.has_left_wall == False:
            self._win.draw_line(line, fill)
        elif self.has_left_wall == False and to_cell.has_right_wall == False:
            self._win.draw_line(line, fill)