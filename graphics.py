from tkinter import Tk, BOTH, Canvas

def Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.operating = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw():
        self.root.update_idletasks()
        self.root.update()
        
        
    def wait_for_close():
        self.operating = True
        while self.operating:
            self.redraw()
        print("window closed...")
            
    def close():
        self.operating = False