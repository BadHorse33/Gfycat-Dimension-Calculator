import tkinter as tk
from tkinter import ttk
from Rectangle import Rectangle

#=================
# Methods
#=================

def calculate_clicked():
    if txtHeight != "" and txtWidth != "":
        w = txtWidth.get()
        h = txtHeight.get()
        r = Rectangle(int(w), int(h))
        newDimensions = "x".join([str(x) for x in r.getNearestDivisibleWidth()])
        result.delete(0)
        result.insert(0, newDimensions)

#=================
# Setup
#=================

win = tk.Tk()

win.title("GfyCat Dimension Calculator")
win.resizable(True, True)

ttk.Label(win, text="Enter dimensions: ").grid(column=0, row=0)

width = tk.IntVar
ttk.Label(win, text="Width: ").grid(column=0, row=1)
txtWidth = ttk.Entry(win, textvariable=width)
txtWidth.grid(column=1, row=1)
height = tk.IntVar
ttk.Label(win, text="Height: ").grid(column=0, row=2)
txtHeight = ttk.Entry(win, textvariable=height)
txtHeight.grid(column=1, row=2)
action = ttk.Button(win, text="Calculate", command=calculate_clicked)
action.grid(column=0, row=3)
result = ttk.Entry(win, text="result = ")
result.grid(column=1, row=3)


#=================
# Start GUI
#=================
if __name__ == '__main__':
    win.mainloop()