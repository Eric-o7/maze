from cell import Cell
import time
from graphics import *
import random

class Maze():
    def __init__(self, x1, y1, num_rows,
                 num_cols, cell_size_x,
                 cell_size_y, win=None, seed=None):
        #x1 and y1 are where maze generation begins on the Canvas
        #top left of Canvas is x=0, y=0
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column_cells = []
            for row in range(self.num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.00055)
    
    def _break_entrance_and_exit(self):
        break_wall = random.randint(1, 2)
        if break_wall == 1: 
            self._cells[0][0].has_top_wall = False
            self._cells[self.num_cols -1][self.num_rows-1].has_bottom_wall = False
        else:
            self._cells[0][0].has_left_wall = False
            self._cells[self.num_cols -1][self.num_rows-1].has_right_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols-1, self.num_rows-1)
        