"""
window.py adds the .clear_frame function to destroy a frame to be 
rebuilt by the click of another tk button.
piLab_home will rebuild the home window
"""


import tkinter as tk
from src import procedure as pr
from src import instructions as ins

class window:

    def piLab_home():
         welcome = ins.welcome.welcome_statment
         welcome_frame = tk.Frame()
         welcome_frame.pack()
         icp_op = ins.icp_operation
         text = tk.Text(welcome_frame,
                           height = 10,
                           width = 52,
                           font = ("Arial", 20))
         text.grid(row = 0, column = 1)
         text.insert(tk.END, welcome)
         smith_lab = tk.Button(welcome_frame,
                               text = "Smith Lab",
                               font = ("Arial", 20),
                               command = lambda: [window.clear_frame(welcome_frame),
                                                  window.Smith_lab_home()]).grid(row = 1, column = 1,
                                                                                 padx = 20,
                                                                                 pady = 20)
         yost_lab = tk.Button(welcome_frame,
                              text = "Yost Lab?",
                              font = ("Arial", 20),
                              ).grid(row = 2, column = 1,
                                     padx = 20,
                                     pady = 20)
         Schantz_lab = tk.Button(welcome_frame,
                              text = "Schantz Lab?",
                              font = ("Arial", 20),
                              ).grid(row = 3, column = 1,
                                     padx = 20,
                                     pady = 20)

    def clear_frame(frame):
        frame.destroy()
    
    def Smith_lab_home():
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

        instrument_recipies = tk.Button(home,
                                text = "Instrument Recipes",
                                font = ("Arial", 20),
                                command = lambda: [window.clear_frame(home),
                                                   pr.procedure_selection.instruments_click()]).grid(row = 7, column = 3, padx = 20, pady = 20)
        extraction_protocols = tk.Button(home,
                              text = "Extraction Protocols",
                              font = ("Arial", 20),
                              command = lambda: [window.clear_frame(home),
                                                 pr.procedure_selection.extraction_protocol()]).grid(row = 8, column = 1, padx = 20, pady = 20)
        analytical_instruments = tk.Button(home,
                                text = "Analytical Instrumentation",
                                font = ("Arial", 20),
                                command = lambda: [window.clear_frame(home),
                                                   pr.procedure_selection.analytical_instruments()]).grid(row = 8, column = 3, padx = 20, pady = 20)
        piLab_home = tk.Button(home,
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: [window.clear_frame(home),
                                                  window.piLab_home()]).grid(row = 9, column = 0,
                                                                             padx = 20,
                                                                             pady = 20)