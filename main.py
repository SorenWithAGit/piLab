#!/usr/bin/env python3

import tkinter as tk
from src.smithLab import procedure as pr


class MainGUI(tk.Tk):
    def __init__(self):
        # Main Setup
        super().__init__()
        self.title("piLab By John Sorensen")
        self.geometry("1280x800")
        self.resizable(width = False, height = False)


        # Ribbon Menu
        piLab_menu = tk.Menu(self)
        self.config(menu = piLab_menu)

        home_menu = tk.Menu(piLab_menu)
        piLab_menu.add_cascade(label = "Home", menu = home_menu)
        home_menu.add_command(label = "piLab Home", command = lambda: self.temp_command())
        home_menu.add_command(label = "Exit", command = self.quit)
    
        smith_menu  = tk.Menu(piLab_menu)
        piLab_menu.add_cascade(label = "Smith Lab", menu = smith_menu)
        smith_menu.add_command(label = "Smith Lab Home", command = lambda: self.temp_command())
        smith_menu.add_separator()
        smith_menu.add_command(label = "Extraction Recipes", command = lambda: self.temp_command())
        smith_menu.add_command(label = "Instrument Recipes", command = lambda: self.temp_command())
        smith_menu.add_command(label = "Extraction Protocols", command = lambda: self.temp_command())
        smith_menu.add_command(label = "Analytical Instrumentation", command = lambda: self.temp_command())

        yost_menu = tk.Menu(piLab_menu)
        piLab_menu.add_cascade(label = "Yost Lab", menu = yost_menu)

        schantz_menu = tk.Menu(piLab_menu)
        piLab_menu.add_cascade(label = "Schantz Lab", menu = schantz_menu)


        # Home Frame
        self.home = homeFrame(self)

        # Run
        self.mainloop()

    def temp_command():
        pass

class homeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pr.mainFrames.piLab_home()

MainGUI()