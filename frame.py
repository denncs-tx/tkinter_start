# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *

root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
