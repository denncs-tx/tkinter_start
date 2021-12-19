from denncs import DennCSApp, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        ttk.Button(self, text="Click Me!", command=self._my_click).pack()

    def _my_click(self):
        ttk.Label(self, text="Look! I clicked a Button!!").pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
