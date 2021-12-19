from denncs import DennCSApp, tk, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._pizza = tk.StringVar(self, "Pepperoni")
        self._toppings = [
            ("Pepperoni", "Pepperoni"),
            ("Cheese", "Cheese"),
            ("Mushroom", "Mushroom"),
            ("Onion", "Onion"),
        ]
        for text, topping in self._toppings:
            ttk.Radiobutton(self, text=text, variable=self._pizza, value=topping).pack(anchor=tk.W)
        ttk.Button(self, text="Click Me!", command=lambda: self._clicked(self._pizza.get())).pack()

    def _clicked(self, value):
        ttk.Label(self, text=value).pack()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
