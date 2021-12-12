from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")

# Databases

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE table addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)""")


# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
