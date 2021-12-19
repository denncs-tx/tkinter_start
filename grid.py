from denncs import DennCSApp, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        ttk.Label(self, text="Hello World!").grid(row=0, column=0)
        ttk.Label(self, text="My Name is Theodore Dennis").grid(row=1, column=5)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
