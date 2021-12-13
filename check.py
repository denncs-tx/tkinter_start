# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *


def show():
    Label(root, text=var.get()).pack()


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

Button(root, text="Show Select", command=show).pack()

root.mainloop()
