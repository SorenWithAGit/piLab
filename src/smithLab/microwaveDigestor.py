"""
########################################################################
microwaveDigestor.py defines the classes and functions for the different
frames that are related to SOPs for the operation of the Mars6 Microwave
Digestor and are being constructed through the operation of the piLab.
########################################################################
"""


import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

def microwave_frame():
    frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
    frame.pack()
    main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                          text = "Smith Lab: Microwave Digestor Protocols",
                          font = ("Arial", 25)).grid(row = 0, columnspan = 5)
    for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
    wq_digest = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "Water Quality Total P",
                            font = ("Arial", 20),
                            command = lambda: ctrl.microwaveDigest.totalP(frame)).grid(row = 4, column = 0,
                                                                        columnspan = 3,
                                                                        padx = 20,
                                                                        pady = 20)
    for i in range(9,12):
          label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                           text = "").grid(row = i)
    piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "piLab Home",
                                    command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 12, column = 0,
                                                                                                padx = 50,
                                                                                                pady = 20)
    smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "Smith Lab Home",
                            command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 13, column = 0,
                                                                    padx = 50,
                                                                    pady = 20)
    instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Instrumentation SOPs",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 12, 
                                                                                                                  column = 2,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 50,
                                                                                                                  pady = 20)

    
def totalP_frame():
    frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
    frame.pack()
    main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                          text = "Smith Lab: Total P Water Digest",
                          font = ("Arial", 25)).grid(row = 0, columnspan = 3)
    for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
    text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20),
                       bd = 5,
                       relief = "sunken")
    text.configure(bg = "#055942", fg = "#67aae6")
    text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
    totalP_digestion = ins.microwaveDigestor.MDprotocols["WQ Total P"]
    text.insert(tk.END, totalP_digestion)
    for i in range(5, 8):
          label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                           text = "").grid(row = i)
    piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "piLab Home",
                                    command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                padx = 20,
                                                                                                pady = 20)
    smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "Smith Lab Home",
                            command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
    instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Instrumentation SOPs",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                  column = 1,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
    mdHome = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Microwave Digestor Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.microwaveDigest.digestHome(frame)).grid(row = 8, column = 2,
                                                                                                   rowspan = 2,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    
