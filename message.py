from denncs import DennCSApp, ttk
from tkinter import messagebox


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._resp_lbl = ttk.Label(self, text="")
        ttk.Button(self, text="Popup", command=self._popup).pack()
        self._resp_lbl.pack()

    def _popup(self):
        self._resp_lbl.configure(text="")
        response = messagebox.showinfo("This is my Popup!", "Hello World!")
        self._resp_lbl.configure(text=response)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
