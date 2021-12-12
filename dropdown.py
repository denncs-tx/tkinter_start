from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")


# Drop Down Boxes
def show():
    Label(root, text=clicked.get()).pack()


options = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

Button(root, text="Show Selection", command=show).pack()

root.mainloop()
