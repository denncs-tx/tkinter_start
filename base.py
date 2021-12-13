# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *
from PIL import ImageTk, Image

global my_img


def window_open():
    global my_img
    top = Toplevel()
    top.title("Dennis Creative Solutions - Photo")
    top.iconbitmap('file.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/0030.png").resize((500, 500), Image.ANTIALIAS))
    Label(top, image=my_img).pack()
    Button(top, text="Close Window", command=top.destroy).pack()


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
Button(root, text="Open Second Window", command=window_open).pack()
root.mainloop()
