from denncs import DennCSApp, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        my_label = ttk.Label(self, text="Hello World!")
        my_label.grid(column=0, row=0)


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
