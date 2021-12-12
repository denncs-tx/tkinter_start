from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
# from PIL import ImageTk, Image


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()


my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()
