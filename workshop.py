from tkinter import Tk, BOTH, Canvas
import tkinter as tk

root = tk.Tk() #initializes Tk

root.geometry("500x500") #size of window
root.title("Button Grid") #text that appear as a part of the window

label = tk.Label(root, text="Button Grid Example", font=('Arial', 18))#text inside the window
label.pack(padx=20, pady=20)#pack method

textbox = tk.Text(root, height=3, font=('Arial, 16'))#creates a bottomless text box
textbox.pack(padx=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill=tk.X)

root.mainloop()#runs the program

