# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
from tkinter import *

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
