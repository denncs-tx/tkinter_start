# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *


def slide():
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")

vertical = Scale(root, from_=0, to=600)
vertical.pack()

horizontal = Scale(root, from_=100, to=800, orient=HORIZONTAL)
horizontal.pack()

Label(root, text=horizontal.get()).pack()
Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
