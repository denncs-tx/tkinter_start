from denncs import DennCSApp, ttk
from PIL import ImageTk, Image
from tkinter import filedialog


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._my_img = None
        self._img_lbl = ttk.Label(self, image=self._my_img)
        self._file_lbl = ttk.Label(self, text="")
        ttk.Button(self, text="Open File", command=self._open_file).pack()
        self._img_lbl.pack()
        self._file_lbl.pack()

    def _open_file(self):
        filename = filedialog.askopenfilename(initialdir="images", title="Select A File",
                                              filetypes=(("PNG File", "*.png"), ("Any File", "*.*")))
        self._my_img = ImageTk.PhotoImage(Image.open(filename).resize((500, 500), Image.ANTIALIAS))
        self._img_lbl.configure(image=self._my_img)
        self._file_lbl.configure(text=filename)


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
