# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

global my_img


def open_file():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/Users/dennc/PycharmProjects/tkinter_start", title="Select "
                                                                                                              "A "
                                                                                                              "File",
                                               filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
    my_img = ImageTk.PhotoImage(Image.open(root.filename).resize((500, 500), Image.ANTIALIAS))
    my_label = Label(image=my_img)
    my_label.pack()


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')

Button(root, text="Open File", command=open_file).pack()

root.mainloop()
