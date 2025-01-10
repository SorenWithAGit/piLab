"""
window.py adds the .clear_frame function to destroy a frame to be 
rebuilt by the click of another tk button.
piLab_home will rebuild the home window
"""


import tkinter as tk
import procedure as pr

class window:

    def clear_frame(frame):
        frame.destroy()
    
    def piLab_home():
        home = tk.Frame()
        home.pack()
        for i in range(6):
                label = tk.Label(home,
                                text = "").grid(row = i)
        extracts = tk.Button(home,
                             text = "Extractant Recipes",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(home),
                                               pr.procedure_selection.extracts_click()] ).grid(row = 7, column = 1, padx = 20, pady = 20)

        instruments = tk.Button(home,
                                text = "Instrumentation",
                                font = ("Arial", 20),
                                command = lambda: [window.clear_frame(home),
                                                   pr.procedure_selection.instruments_click()]).grid(row = 7, column = 3, padx = 20, pady = 20)
        protocols = tk.Button(home,
                              text = "Protocols",
                              font = ("Arial", 20),
                              ).grid(row = 8, column = 2, padx = 20, pady = 20)