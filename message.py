# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *
from tkinter import messagebox


def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')

Button(root, text="Popup", command=popup).pack()

root.mainloop()
