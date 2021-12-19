from denncs import DennCSApp, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._entry = ttk.Entry(self, width=50)
        self._entry.pack()
        self._entry.focus()
        ttk.Button(self, text="Enter Your Name", command=self._my_click).pack()

    def _my_click(self):
        hello = f"Hello {self._entry.get()}"
        ttk.Label(self, text=hello).pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
