from denncs import DennCSApp, tk, ttk


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._horizontal = ttk.Scale(self, from_=0, to=1024, orient=tk.HORIZONTAL, value=800, command=self._hslide)
        self._vertical = ttk.Scale(self, from_=0, to=768, orient=tk.VERTICAL, value=600, command=self._vslide)
        self._dim_lbl = ttk.Label(self, text="800x600")
        self._height_lbl = ttk.Label(self, text="0 - 768 (600)")
        self._width_lbl = ttk.Label(self, text="0 - 1024 (800)")
        self._width_lbl.pack()
        self._horizontal.pack()
        self._vertical.pack()
        self._height_lbl.pack()
        ttk.Button(self, text="Click Me!", command=self._slide).pack()
        self._dim_lbl.pack()

    def _hslide(self, value):
        lbl_txt = f"0 - 1024 ({int(float(value))})"
        self._width_lbl.configure(text=lbl_txt)

    def _slide(self):
        dim_str = f"{int(self._horizontal.get())}x{int(self._vertical.get())}"
        self._dim_lbl.configure(text=dim_str)
        self.geometry(dim_str)

    def _vslide(self, value):
        lbl_txt = f"0 - 768 ({int(float(value))})"
        self._height_lbl.configure(text=lbl_txt)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
