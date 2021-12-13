# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *


def my_click():
    my_label = Label(root, text="Look! I clicked a Button!!")
    my_label.pack()


root = Tk()
myButton = Button(root, text="Click Me!", command=my_click)
myButton.pack()
root.mainloop()
