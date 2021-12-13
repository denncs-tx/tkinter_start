# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()


def my_click():
    hello = f"Hello {e.get()}"
    my_label = Label(root, text=hello)
    my_label.pack()


myButton = Button(root, text="Enter Your Name", command=my_click)
myButton.pack()

root.mainloop()
