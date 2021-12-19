from denncs import DennCSApp, tk, ttk
from PIL import ImageTk, Image


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._my_img = None
        ttk.Button(self, text="Open Second Window", command=self._window_open).pack()

    def _window_open(self):
        self._my_img = ImageTk.PhotoImage(Image.open("images/0030.png").resize((500, 500), Image.ANTIALIAS))
        top = tk.Toplevel(self)
        top.title("Dennis Creative Solutions - Photo")
        top.iconbitmap("file.ico")
        ttk.Label(top, image=self._my_img).pack()
        ttk.Button(top, text="Close Window", command=top.destroy).pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
