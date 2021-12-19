from denncs import DennCSApp, tk, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._var = tk.IntVar()
        ttk.Checkbutton(self, text="Check this box, I dare you!", variable=self._var).pack()
        ttk.Button(self, text="Show Select", command=self._show).pack()

    def _show(self):
        ttk.Label(self, text=self._var.get()).pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
