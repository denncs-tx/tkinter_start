from denncs import DennCSApp, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        frame = ttk.LabelFrame(self, text="Choose", padding="10")
        frame.pack(padx=10, pady=10)
        ttk.Button(frame, text="Don't Click Here!").grid(row=0, column=0)
        ttk.Button(frame, text="...or here!").grid(row=1, column=1)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
