# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
# TODO: Make functionally equivalent to old MS Windows calculator including the look & feel
# from tkinter import *
#
# global f_num
# global math
#
#
# def button_add():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "addition"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# def button_clear():
#     e.delete(0, END)
#
#
# def button_click(number):
#     current = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + str(number))
#
#
# def button_divide():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "division"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)
#
#     if math == 'addition':
#         e.insert(0, f_num + int(second_number))
#     if math == 'subtraction':
#         e.insert(0, f_num - int(second_number))
#     if math == 'multiplication':
#         e.insert(0, f_num * int(second_number))
#     if math == 'division':
#         e.insert(0, f_num / int(second_number))
#
#
# def button_multiply():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "multiplication"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# def button_subtract():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "subtraction"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# root = Tk()
# root.title("Simple Calculator")
#
# # Define the controls
# e = Entry(root, width=35, borderwidth=5)
# button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
# button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
# button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
# button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
# button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
# button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
# button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
# button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
# button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
# button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
# button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
# button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear)
# button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
# button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
# button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
#
# # Put the controls on the main application window
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
# button_0.grid(row=4, column=0)
# button_clear.grid(row=4, column=1, columnspan=2)
# button_add.grid(row=5, column=0)
# button_equal.grid(row=5, column=1, columnspan=2)
# button_subtract.grid(row=6, column=0)
# button_multiply.grid(row=6, column=1)
# button_divide.grid(row=6, column=2)
#
# root.mainloop()
import tkinter

import fontTools.fontBuilder

from denncs import DennCSApp, tk, ttk
from tkinter import messagebox


class CalcFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._calc_frame = ttk.Frame(parent, width=190, height=50, border=1, borderwidth=2)
        self._label1 = ttk.Label(self, background="red", foreground="white", text="Hello")
        self._label1.place(x=1, y=1)


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("214x284")
        self.iconbitmap("calc.ico")
        self.resizable(width=False, height=False)
        # hue: 143, sat: 160, lum: 229
        self['background'] = f'#{235:02x}{242:02x}{251:02x}'
        s = ttk.Style()
        s.theme_use("xpnative")
        self._set_bindings()
        self['menu'] = self._build_menu()
        # self._calc_frame = ttk.Frame(self, width=190, height=50, border=1)
        # self._label1 = ttk.Label(self._calc_frame, background="red", foreground="white", text="Hello")
        # self._label1.place(x=1, y=1)
        self._calc_frame = CalcFrame(self)
        self._calc_frame.place(x=10, y=10, width=50, height=50)
        # self._e = ttk.Label(self, width=35, text="0", justify=tk.RIGHT, font=("Segoe UI", 12, "bold"))
        # self._e.place(x=10, y=10, width=50)

    def _build_menu(self):
        self.menuBar = tk.Menu(self)
        self.viewMenu = tk.Menu(self.menuBar, tearoff=0)
        self.viewMenu.add_command(label="Standard", accelerator="Alt+1", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_command(label="Scientific", accelerator="Alt+2", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_command(label="Programmer", accelerator="Alt+3", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_command(label="Statistics", accelerator="Alt+4", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_separator()
        self.viewMenu.add_command(label="History", accelerator="Ctrl+H", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_command(label="Digit grouping", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_separator()
        self.viewMenu.add_command(label="Basic", accelerator="Ctrl+F4", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_command(label="Unit conversion", accelerator="Ctrl+U", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_command(label="Date calculation", accelerator="Ctrl+E", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewWorksheetsMenu = tk.Menu(self.viewMenu, tearoff=0)
        self.viewWorksheetsMenu.add_command(label="Mortgage", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewWorksheetsMenu.add_command(label="Vehicle lease", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewWorksheetsMenu.add_command(label="Fuel economy (mpg)", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewWorksheetsMenu.add_command(label="Fuel economy (L/100 km)", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.viewMenu.add_cascade(label="Worksheets", menu=self.viewWorksheetsMenu)
        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.editMenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.editMenu.add_separator()
        self.editHistoryMenu = tk.Menu(self.editMenu, tearoff=0)
        self.editHistoryMenu.add_command(label="Copy history", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.editHistoryMenu.add_command(label="Edit", accelerator="F2", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.editHistoryMenu.add_command(label="Cancel edit", accelerator="Esc", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.editHistoryMenu.add_command(label="Clear", accelerator="Ctrl+Shift+D", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.editMenu.add_cascade(label="History", menu=self.editHistoryMenu)
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="View Help", accelerator="F1", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label="About", command=lambda: messagebox.showinfo(self.title(), "Not implemented yet."))
        self.menuBar.add_cascade(label="View", menu=self.viewMenu)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
        return self.menuBar

    def _set_bindings(self):
        self.bind("<Alt-KeyPress-1>", func=lambda event: messagebox.showinfo(self.title(), "Change mode to Standard."))
        self.bind("<Alt-KeyPress-2>", func=lambda event: messagebox.showinfo(self.title(), "Change mode to Scientific."))
        self.bind("<Alt-KeyPress-3>", func=lambda event: messagebox.showinfo(self.title(), "Change mode to Programmer."))
        self.bind("<Alt-KeyPress-4>", func=lambda event: messagebox.showinfo(self.title(), "Change mode to Statistics."))
        self.bind("<Control-h>", func=lambda event: messagebox.showinfo(self.title(), "Show calculation history."))
        self.bind("<Control-H>", func=lambda event: messagebox.showinfo(self.title(), "Show Calculation history."))
        self.bind("<Control-F4>", func=lambda event: messagebox.showinfo(self.title(), "Basic - No Worksheets"))
        self.bind("<Control-u>", func=lambda event: messagebox.showinfo(self.title(), "Unit Conversion worksheet."))
        self.bind("<Control-U>", func=lambda event: messagebox.showinfo(self.title(), "Unit Conversion worksheet."))
        self.bind("<Control-e>", func=lambda event: messagebox.showinfo(self.title(), "Date Calculation worksheet."))
        self.bind("<Control-E>", func=lambda event: messagebox.showinfo(self.title(), "Date Calculation worksheet."))
        self.bind("<Control-c>", func=lambda event: messagebox.showinfo(self.title(), "Copy to Windows Clipboard."))
        self.bind("<Control-C>", func=lambda event: messagebox.showinfo(self.title(), "Copy to Windows Clipboard."))
        self.bind("<Control-v>", func=lambda event: messagebox.showinfo(self.title(), "Paste from Windows Clipboard."))
        self.bind("<Control-V>", func=lambda event: messagebox.showinfo(self.title(), "Paste from Windows Clipboard."))
        self.bind("<F2>", func=lambda event: messagebox.showinfo(self.title(), "Edit History entry."))
        self.bind("<Escape>", func=lambda event: messagebox.showinfo(self.title(), "Cancel Edit History entry."))
        self.bind("<Control-Shift-d>", func=lambda event: messagebox.showinfo(self.title(), "Clear History."))
        self.bind("<Control-Shift-D>", func=lambda event: messagebox.showinfo(self.title(), "Clear History."))
        self.bind("<F1>", func=lambda event: messagebox.showinfo(self.title(), "Show Interactive Help."))


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
