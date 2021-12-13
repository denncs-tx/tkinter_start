# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Theodore Dennis")

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()
