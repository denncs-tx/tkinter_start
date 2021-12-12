from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")

# Databases

# Create a database or connect to one
# conn = sqlite3.connect("address_book.db")

# Create cursor
# c = conn.cursor()

# Create table
'''
c.execute("""CREATE table addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)""")
'''


# Create Function to Delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Create Edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title("Update a record")
    editor.iconbitmap('file.ico')
    editor.geometry("400x400")

    record_id = delete_box.get()
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zip")
    zipcode_label.grid(row=5, column=0)

    # Create a Save Button to Save edited Record
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Create Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()
    # Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()
    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create function to update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first_name,
        last_name = :last_name,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid
    """,
              {'first_name': f_name_editor.get(),
               'last_name': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id}
              )
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    editor.destroy()


# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zip")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# Commit Changes
# conn.commit()

# Close Connection
# conn.close()

root.mainloop()
