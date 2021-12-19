from denncs import DennCSApp, ttk
from PIL import ImageTk, Image


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._my_img = ImageTk.PhotoImage(Image.open("images/0030.png").resize((500, 500), Image.ANTIALIAS))
        ttk.Label(image=self._my_img).pack()
        ttk.Button(self, text="Exit Program", command=self.quit).pack()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
