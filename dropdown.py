from denncs import DennCSApp, tk, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self._clicked = tk.StringVar()
        ttk.OptionMenu(self, self._clicked, options[0], *options).pack()
        ttk.Button(self, text="Show Selection", command=self._show).pack()

    def _show(self):
        ttk.Label(self, text=self._clicked.get()).pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
