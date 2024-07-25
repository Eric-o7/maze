import unittest
from maze import Maze

#reference to constructor
#class Maze():
    # def __init__(self, x1, y1, num_rows,
                #  num_cols, cell_size_x,
                #  cell_size_y, win=None):

class Tests(unittest.TestCase):
    def test_maze_create_cells_1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells_2(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(10,10, num_rows, num_cols, 100,100)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_break_walls(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(10,10,num_rows,num_cols,100,100)
        #using != to represent an XOR condition between the two walls to validate
        #the random nature of either of the walls being False, but not both
        self.assertEqual(
            m1._cells[0][0].has_top_wall 
            != m1._cells[0][0].has_left_wall,
            True
        )
        self.assertEqual(
            m1._cells[num_cols -1][num_rows-1].has_bottom_wall 
            != m1._cells[num_cols -1][num_rows-1].has_right_wall,
            True
        )
        
if __name__ == "__main__":
    unittest.main()