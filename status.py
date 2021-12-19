from denncs import DennCSApp, tk, ttk
from PIL import ImageTk, Image


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._image_list = []
        for i in range(10):
            self._image_list.append(f"images/{i+1:04}.png")
        self._status = ttk.Label(self, text="Image 1 of " + str(len(self._image_list)), border=1, relief=tk.SUNKEN,
                                 anchor=tk.E)
        self._image_src = ImageTk.PhotoImage(Image.open(self._image_list[0]).resize((500, 500), Image.ANTIALIAS))
        self._image = ttk.Label(self, image=self._image_src)
        self._button_back = ttk.Button(self, text="<<", command=lambda: self._back(0))
        self._button_back.state(["disabled"])
        self._button_forward = ttk.Button(self, text=">>", command=lambda: self._forward(2))
        self._image.grid(row=0, column=0, columnspan=3)
        self._button_back.grid(row=1, column=0)
        ttk.Button(self, text="Exit Program", command=self.quit).grid(row=1, column=1)
        self._button_forward.grid(row=1, column=2, pady=10)
        self._status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

    def _back(self, image_number):
        self._display_image(image_number - 1)
        self._button_forward.configure(command=lambda: self._forward(image_number+1))
        self._status.configure(text="Image " + str(image_number) + " of " + str(len(self._image_list)))

        if image_number == 1:
            self._button_back.state(["disabled"])
        else:
            self._button_back.configure(command=lambda: self._back(image_number-1))
            self._button_forward.state(["!disabled"])

    def _display_image(self, image_number):
        self._image_src = ImageTk.PhotoImage(
            Image.open(self._image_list[image_number]).resize((500, 500), Image.ANTIALIAS))
        self._image.configure(image=self._image_src)

    def _forward(self, image_number):
        self._display_image(image_number - 1)
        self._button_back.configure(command=lambda: self._back(image_number-1))
        self._status.configure(text="Image " + str(image_number) + " of " + str(len(self._image_list)))

        if image_number == len(self._image_list):
            self._button_forward.state(["disabled"])
        else:
            self._button_forward.configure(command=lambda: self._forward(image_number+1))
            self._button_back.state(["!disabled"])


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
