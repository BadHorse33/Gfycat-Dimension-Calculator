import tkinter as tk
from tkinter import ttk
from Rectangle import Rectangle

#=================
# Methods
#=================

def calculate_enter(event):
    calculate_clicked()

def calculate_clicked():
    if txtHeight != "" and txtWidth != "":
        w = txtWidth.get()
        h = txtHeight.get()
        if(not w.isdigit() or not h.isdigit):
            result.delete(0, 'end')
            result.insert(0, "width or height not a number")
            return
        r = Rectangle(int(w), int(h))
        newDimensions = "x".join([str(x) for x in r.getNearestDivisibleWidth()])
        result.delete(0, 'end')
        result.insert(0, newDimensions)

#=================
# Setup
#=================

win = tk.Tk()

field_frame = ttk.LabelFrame(win, text='dimensions')
field_frame.grid(column=0, row=0, padx=5)

win.title("GfyCat Dimension Calculator")
win.resizable(True, True)

width = tk.IntVar
ttk.Label(field_frame, text="Width: ").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
txtWidth = ttk.Entry(field_frame, textvariable=width)
txtWidth.grid(column=1, row=0, padx=5, pady=5)
height = tk.IntVar
ttk.Label(field_frame, text="Height: ").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
txtHeight = ttk.Entry(field_frame, textvariable=height)
txtHeight.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
action = ttk.Button(win, text="Calculate", command=calculate_clicked)
action.grid(column=1, row=0, sticky=tk.N+tk.S+tk.W, columnspan=1, rowspan=1, pady=10)

result_frame = ttk.LabelFrame(win, text='result')
result_frame.grid(column=0, row=1, padx=5, pady=5, columnspan=2)
result = ttk.Entry(result_frame, width=50)
result.grid(column=0, row=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

txtWidth.focus()
win.bind('<Return>', calculate_enter)


#=================
# Start GUI
#=================
if __name__ == '__main__':
    win.mainloop()