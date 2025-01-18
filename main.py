#!/usr/bin/env python3

"""
main.py initializes the tkinter window to navigate the piLab package
"""


import tkinter as tk
from src import window

class MainWindow(tk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("piLab By John Sorensen")
        window.window.piLab_home()



def main():
    root = tk.Tk()
    root.title("piLab By John Sorensen")
    root.geometry("1280x800")
    root.resizable(width = False, height = False)
    app = MainWindow()
    root.mainloop()


if __name__ == "__main__":
    main()