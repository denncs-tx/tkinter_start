from denncs import DennCSApp, ttk
import sqlite3


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._conn = None
        ttk.Button(self, text="Create database", command=self._create_tables).pack()
        self._status_lbl = ttk.Label(self, text="Waiting for action...")
        self._status_lbl.pack()
        self._connect_db()

    def __del__(self):
        self._close_db()

    def _close_db(self):
        self._conn.close()

    def _connect_db(self):
        self._conn = sqlite3.connect("address_book.db")

    def _create_tables(self):
        try:
            c = self._conn.cursor()
            c.execute("""CREATE table addresses(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)""")
            self._conn.commit()
            self._status_lbl.configure(text="Table addresses successfully created!")
        except sqlite3.OperationalError as soe:
            print(soe.__str__())
            self._status_lbl.configure(text=soe.__str__())


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
