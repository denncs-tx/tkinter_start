# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *

root = Tk()

# Creating a label widget
myLabel = Label(root, text="Hello World!")
# Shoving it onto the screen
myLabel.pack()

root.mainloop()
