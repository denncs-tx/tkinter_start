# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *

options = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]


# Dropdown Boxes
def show():
    Label(root, text=clicked.get()).pack()


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

Button(root, text="Show Selection", command=show).pack()

root.mainloop()
