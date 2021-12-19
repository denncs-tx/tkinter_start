import tkinter as tk
from tkinter import ttk


class DennCSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dennis Creative Solutions")
        self.iconbitmap("file.ico")
        self.geometry("800x600")
        self.Style = ttk.Style(self)
        self.Style.theme_use("winnative")
