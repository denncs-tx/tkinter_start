from denncs import DennCSApp, tk, ttk
import sqlite3


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._conn = None
        self._editor = None
        self._f_name = ttk.Entry(self, width=30)
        self._l_name = ttk.Entry(self, width=30)
        self._address = ttk.Entry(self, width=30)
        self._city = ttk.Entry(self, width=30)
        self._state = ttk.Entry(self, width=30)
        self._zipcode = ttk.Entry(self, width=30)
        self._delete_box = ttk.Entry(self, width=30)
        self._f_name_label = ttk.Label(self, text="First Name")
        self._l_name_label = ttk.Label(self, text="Last Name")
        self._address_label = ttk.Label(self, text="Address")
        self._city_label = ttk.Label(self, text="City")
        self._state_label = ttk.Label(self, text="State")
        self._zipcode_label = ttk.Label(self, text="Zip")
        self._delete_box_label = ttk.Label(self, text="Select ID")
        self._submit_btn = ttk.Button(self, text="Add Record to Database", command=self._submit)
        self._query_btn = ttk.Button(self, text="Show Records", command=self._query)
        self._delete_btn = ttk.Button(self, text="Delete Record", command=self._delete)
        self._edit_btn = ttk.Button(self, text="Edit Record", command=self._edit)
        self._query_label = ttk.Label(self, text="")

        self._f_name_label.grid(row=0, column=0, pady=(10, 0))
        self._f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        self._l_name_label.grid(row=1, column=0)
        self._l_name.grid(row=1, column=1, padx=20)
        self._address_label.grid(row=2, column=0)
        self._address.grid(row=2, column=1, padx=20)
        self._city_label.grid(row=3, column=0)
        self._city.grid(row=3, column=1, padx=20)
        self._state_label.grid(row=4, column=0)
        self._state.grid(row=4, column=1, padx=20)
        self._zipcode_label.grid(row=5, column=0)
        self._zipcode.grid(row=5, column=1, padx=20)
        self._submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        self._query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        self._delete_box.grid(row=9, column=1, pady=5)
        self._delete_box_label.grid(row=9, column=0, pady=5)
        self._delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
        self._edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
        self._query_label.grid(row=12, column=0, columnspan=2)
        self._connect_db()

    def __del__(self):
        self._close_db()

    def _close_db(self):
        self._conn.close()

    def _connect_db(self):
        self._conn = sqlite3.connect("address_book.db")

    def _delete(self):
        c = self._conn.cursor()
        c.execute("DELETE FROM addresses WHERE oid = " + self._delete_box.get())
        self._conn.commit()

    def _edit(self):
        self._editor = tk.Toplevel(self)
        self._editor.title("Update a record")
        self._editor.iconbitmap('file.ico')
        self._editor.geometry("400x400")

        record_id = self._delete_box.get()
        c = self._conn.cursor()
        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = c.fetchall()
        f_name_editor = tk.Entry(self._editor, width=30)
        l_name_editor = tk.Entry(self._editor, width=30)
        address_editor = tk.Entry(self._editor, width=30)
        city_editor = tk.Entry(self._editor, width=30)
        state_editor = tk.Entry(self._editor, width=30)
        zipcode_editor = tk.Entry(self._editor, width=30)
        f_name_editor_label = tk.Label(self._editor, text="First Name")
        l_name_editor_label = tk.Label(self._editor, text="Last Name")
        address_editor_label = tk.Label(self._editor, text="Address")
        city_editor_label = tk.Label(self._editor, text="City")
        state_editor_label = tk.Label(self._editor, text="State")
        zipcode_editor_label = tk.Label(self._editor, text="Zip")

        f_name_editor_label.grid(row=0, column=0, pady=(10, 0))
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor_label.grid(row=1, column=0)
        l_name_editor.grid(row=1, column=1, padx=20)
        address_editor_label.grid(row=2, column=0)
        address_editor.grid(row=2, column=1, padx=20)
        city_editor_label.grid(row=3, column=0)
        city_editor.grid(row=3, column=1, padx=20)
        state_editor_label.grid(row=4, column=0)
        state_editor.grid(row=4, column=1, padx=20)
        zipcode_editor_label.grid(row=5, column=0)
        zipcode_editor.grid(row=5, column=1, padx=20)

        save_btn = tk.Button(self._editor, text="Save Record",
                             command=lambda: self._update(self._editor.winfo_children()))
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

    def _query(self):
        c = self._conn.cursor()
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print_records = ""
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"
        self._query_label.configure(text=print_records)
        self._conn.commit()

    def _submit(self):
        c = self._conn.cursor()
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                      'f_name': self._f_name.get(),
                      'l_name': self._l_name.get(),
                      'address': self._address.get(),
                      'city': self._city.get(),
                      'state': self._state.get(),
                      'zipcode': self._zipcode.get()
                  })
        self._conn.commit()
        self._f_name.delete(0, tk.END)
        self._l_name.delete(0, tk.END)
        self._address.delete(0, tk.END)
        self._city.delete(0, tk.END)
        self._state.delete(0, tk.END)
        self._zipcode.delete(0, tk.END)

    def _update(self, editor):
        db_values = []
        for item in editor:
            if type(item) is tk.Entry:
                db_values.append(item.get())
        c = self._conn.cursor()
        record_id = self._delete_box.get()
        c.execute("""UPDATE addresses SET
            first_name = :first_name,
            last_name = :last_name,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            WHERE oid = :oid
        """,
                  {'first_name': db_values[0],
                   'last_name': db_values[1],
                   'address': db_values[2],
                   'city': db_values[3],
                   'state': db_values[4],
                   'zipcode': db_values[5],
                   'oid': record_id}
                  )
        self._conn.commit()
        self._editor.destroy()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
