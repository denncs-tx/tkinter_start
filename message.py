from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    # if response == "yes":
    #     Label(root, text="You clicked Yes!").pack()
    # else:
    #     Label(root, text="You clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
