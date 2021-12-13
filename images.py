# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')

my_img = ImageTk.PhotoImage(Image.open("images/0030.png").resize((500, 500), Image.ANTIALIAS))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
