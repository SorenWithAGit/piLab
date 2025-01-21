#!/usr/bin/env python3

import tkinter as tk
from src import window
from src import instructions as ins

class MainWindow(tk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("piLab By John Sorensen")
        window.window.piLab_home()

def temp_command():
     pass

def main():
    root = tk.Tk()
    root.title("piLab By John Sorensen")
    root.geometry("1280x800")
    root.resizable(width = False, height = False)

    piLab_menu = tk.Menu(root)
    root.config(menu = piLab_menu)

    home_menu = tk.Menu(piLab_menu)
    piLab_menu.add_cascade(label = "Home", menu = home_menu)
    home_menu.add_command(label = "piLab Home", command = lambda: temp_command())
    home_menu.add_command(label = "Exit", command = root.quit)
   
    smith_menu  = tk.Menu(piLab_menu)
    piLab_menu.add_cascade(label = "Smith Lab", menu = smith_menu)
    smith_menu.add_command(label = "Smith Lab Home", command = lambda: temp_command()())
    smith_menu.add_separator()
    smith_menu.add_command(label = "Extraction Recipes", command = lambda: temp_command())
    smith_menu.add_command(label = "Instrument Recipes", command = lambda: temp_command())
    smith_menu.add_command(label = "Extraction Protocols", command = lambda: temp_command())
    smith_menu.add_command(label = "Analytical Instrumentation", command = lambda: temp_command())

    yost_menu = tk.Menu(piLab_menu)
    piLab_menu.add_cascade(label = "Yost Lab", menu = yost_menu)

    schantz_menu = tk.Menu(piLab_menu)
    piLab_menu.add_cascade(label = "Schantz Lab", menu = schantz_menu)

    app = MainWindow()
    root.mainloop()


if __name__ == "__main__":
    main()