"""
main.py initializes the tkinter window to navigate the piLab package
"""


import tkinter as tk
import window

class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("piLab By John Sorensen")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("piLab By John Sorensen")
    root.geometry("1024x600")
    root.resizable(width = False, height = False)
    app = MainWindow(root)
    window.window.Smith_lab_home()
    root.mainloop()