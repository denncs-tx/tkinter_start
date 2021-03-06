# NOTE: This is not being converted to DennCSApp framework because "status.py" encompasses this functionality
from tkinter import *
from PIL import ImageTk, Image

global button_back
global button_forward
global my_label


def back(image_number):
    global button_back
    global button_forward
    global my_label

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    else:
        button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global button_back
    global button_forward
    global my_label

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)


root = Tk()
root.title("Dennis Creative Solutions Image Viewer")
root.iconbitmap('file.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/0001.png").resize((500, 500), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage(Image.open("images/0002.png").resize((500, 500), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage(Image.open("images/0003.png").resize((500, 500), Image.ANTIALIAS))
my_img4 = ImageTk.PhotoImage(Image.open("images/0004.png").resize((500, 500), Image.ANTIALIAS))
my_img5 = ImageTk.PhotoImage(Image.open("images/0005.png").resize((500, 500), Image.ANTIALIAS))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
