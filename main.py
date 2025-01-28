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

        home_menu = tk.Menu(piLab_menu, tearoff = 0)
        piLab_menu.add_cascade(label = "Home", menu = home_menu)
        home_menu.add_command(label = "piLab Home",
                              font = ("Arial", 24),
                              command = lambda: [self.clear(),
                                                 pr.mainFrames.piLab_home()])
        home_menu.add_separator()
        home_menu.add_command(label = "Exit",
                              font = ("arial", 24),
                              command = self.quit)
    
        smith_menu  = tk.Menu(piLab_menu, tearoff = 0)
        piLab_menu.add_cascade(label = "Smith Lab", menu = smith_menu)
        smith_menu.add_separator()
        smith_menu.add_command(label = "Smith Lab Home",
                               font = ("Arial", 24),
                               command = lambda: [self.clear(),
                                                  pr.mainFrames.Smith_lab_home()])
        smith_menu.add_separator()
        smith_menu.add_command(label = "Extraction Recipes",
                               font = ("Arial", 24),
                               command = lambda: [self.clear(),
                                                  pr.procedure_selection.extracts_click()])
        smith_menu.add_separator()
        smith_menu.add_command(label = "Instrument Recipes",
                               font = ("Arial", 24),
                               command = lambda: [self.clear(),
                                                  pr.procedure_selection.instruments_click()])
        smith_menu.add_separator()
        smith_menu.add_command(label = "Extraction Protocols",
                               font = ("Arial", 24),
                               command = lambda: [self.clear(),
                                                  pr.procedure_selection.extraction_protocol()])
        smith_menu.add_separator()
        smith_menu.add_command(label = "Analytical Instrumentation",
                               font = ("Arial", 24),
                               command = lambda: [self.clear(),
                                                  pr.procedure_selection.analytical_instruments()])
        smith_menu.add_separator()

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

    def clear(self):
        for widget in self.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()


class homeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pr.mainFrames.piLab_home()

MainGUI()