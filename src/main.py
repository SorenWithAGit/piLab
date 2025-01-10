import tkinter as tk
import window
from procedure import procedure_selection

class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("piLab By John Sorensen")

    def open_extracts(self):
        procedure_selection(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("piLab By John Sorensen")
    root.geometry("1024x600")
    root.resizable(width = False, height = False)
    app = MainWindow(root)
    window.window.piLab_home()
    root.mainloop()