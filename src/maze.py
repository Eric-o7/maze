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
        self.reset_cells_visited()
    
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
        time.sleep(0.009)
    
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
        self._break_walls_r(0, 0)
        
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # up
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # down
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # left
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # right
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]
            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
                
    def reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False

    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)
    
    # def _solve_r(self, i, j):
    #     self._animate()
    #     self._cells[i][j].visited = True
    #     # Check if current cell is the goal
    #     if i == self.num_cols - 1 and j == self.num_rows - 1:
    #         return True
    #     # Directions with corresponding movements
    #     directions = {
    #         "up": (-1, 0),
    #         "down": (1, 0),
    #         "left": (0, -1),
    #         "right": (0, 1)
    #     }
    #     # Shuffle directions to add randomness
    #     faces = ["up", "down", "left", "right"]
    #     random.shuffle(faces)
    #     for face in faces:
    #         di, dj = directions[face]
    #         ni, nj = i + di, j + dj
    #         # Boundary and movement checks
    #         if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
    #             if not self._cells[ni][nj].visited:
    #                 if face == "up" and not self._cells[ni][nj].has_bottom_wall and not self._cells[i][j].has_top_wall:
    #                     pass
    #                 elif face == "down" and not self._cells[ni][nj].has_top_wall and not self._cells[i][j].has_bottom_wall:
    #                     pass
    #                 elif face == "left" and not self._cells[ni][nj].has_right_wall and not self._cells[i][j].has_left_wall:
    #                     pass
    #                 elif face == "right" and not self._cells[ni][nj].has_left_wall and not self._cells[i][j].has_right_wall:
    #                     pass
    #                 else:
    #                     continue
                    
    #                 # If we can move to next cell
    #                 self._cells[i][j].draw_move(self._cells[ni][nj])
    #                 if self._solve_r(ni, nj):
    #                     return True
    #                 else:
    #                     # Undo the move
    #                     self._cells[i][j].draw_move(self._cells[ni][nj], undo=True) 
    #     return False
                        
    # def solve(self):
    #     return self._solve_r(0, 0)