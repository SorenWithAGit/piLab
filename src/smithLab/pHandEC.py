"""
########################################################################
pHandEC.py defines the classes and functions for the different
frames that are related to the SOPs for the pH meter and Electrical 
Conductivity meters and are being constructed through the operation 
of the piLab.
########################################################################
"""


import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

def phec_frame():
    frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
    frame.pack()
    main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                          text = "Smith Lab: pH and Electrical Conductivity",
                          font = ("Arial", 25)).grid(row = 0, columnspan = 3,
                                                     padx = 20,
                                                     pady = 20)
    for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
    ec_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                          text = "Electrical Conductivity",
                          font = ("Arial", 20),
                          command = lambda: ctrl.pHEC.ec_click(frame)).grid(row = 4, column = 1,
                                                             padx = 20,
                                                             pady = 20)
    ph_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                          text = "pH Meter",
                          font = ("Arial", 20),
                          command = lambda: ctrl.pHEC.ph_click(frame)).grid(row = 4, column =2,
                                                             padx = 20,
                                                             pady = 20)
    for i in range(5, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
    piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                  font = ("Arial", 20),
                                  text = "piLab Home",
                                  command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                              padx = 20,
                                                                                              pady = 20)
    smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                        column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
    instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Analytical Instruments",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                  column = 2,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
class ecMeter:

    def ec_steps():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab EC Meter SOP",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        
        cal_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "Calibration",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ec_cal_click(frame)).grid(row = 4, column = 0,
                                    padx = 20,
                                    pady = 20)
        step1_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Mode Selection",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.pHEC.ec_mode_click(frame)).grid(row = 4, column = 1,
                                        padx = 20,
                                        pady = 20)
        step2_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Measurement",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.pHEC.ec_measure_click(frame)).grid(row = 4, column = 2,
                                        padx = 20,
                                        pady = 20)
        for i in range(5, 8):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "piLab Home",
                                    command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                padx = 20,
                                                                                                pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        font = ("Arial", 20),
                                        text = "Smith Lab Home",
                                        command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                            column = 0,
                                                                            padx = 20,
                                                                            pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                            font = ("Arial", 20),
                                            text = "Analytical Instruments",
                                            command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                    column = 1,
                                                                                                                    rowspan = 2,
                                                                                                                    padx = 20,
                                                                                                                    pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                        rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
    def cal_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab EC Meter SOP: Calibration",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 5)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        cal = ins.ecph.ecMeter["Calibration"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 8,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, columnspan = 2)
        text.insert(tk.END, cal)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "piLab Home",
                                    command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                padx = 20,
                                                                                                pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        font = ("Arial", 20),
                                        text = "Smith Lab Home",
                                        command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                            column = 0,
                                                                            padx = 20,
                                                                            pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                            font = ("Arial", 20),
                                            text = "Analytical Instruments",
                                            command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                    column = 1,
                                                                                                                    rowspan = 2,
                                                                                                                    padx = 20,
                                                                                                                    pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                        rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        steps_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "EC Steps",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.ec_click(frame)).grid(row = 8, column = 3,
                                                                         rowspan = 2,
                                                                         padx = 10,
                                                                         pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "Mode Selection",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ec_mode_click(frame)).grid(row = 5, column = 3,
                                                                                   padx = 10,
                                                                                   pady = 20)
        
    def mode_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab EC Meter SOP: Measurement Mode",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        cal = ins.ecph.ecMeter["Measurement Mode"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 8,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, columnspan = 2, rowspan = 2)
        text.insert(tk.END, cal)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "piLab Home",
                                    command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                padx = 20,
                                                                                                pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        font = ("Arial", 20),
                                        text = "Smith Lab Home",
                                        command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                            column = 0,
                                                                            padx = 20,
                                                                            pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                            font = ("Arial", 20),
                                            text = "Analytical Instruments",
                                            command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                    column = 1,
                                                                                                                    rowspan = 2,
                                                                                                                    padx = 20,
                                                                                                                    pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                        rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        steps_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "EC Steps",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.ec_click(frame)).grid(row = 8, column = 3,
                                                                         rowspan = 2,
                                                                         padx = 10,
                                                                         pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Calibration",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.pHEC.ec_cal_click(frame)).grid(row = 5, column = 0,
                                                                                          padx = 20,
                                                                                          pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Measurement",
                                font = ("Arial", 20),
                                command = lambda: ctrl.pHEC.ec_measure_click(frame)).grid(row = 5, column = 3,
                                                                                          padx = 20,
                                                                                          pady = 20)
    
    def measure_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab EC Meter SOP: Measurement",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        cal = ins.ecph.ecMeter["Measurement"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 8,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, columnspan = 2, rowspan = 2)
        text.insert(tk.END, cal)
        for i in range(7, 9):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "piLab Home",
                                    command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                padx = 20,
                                                                                                pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        font = ("Arial", 20),
                                        text = "Smith Lab Home",
                                        command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                            column = 0,
                                                                            padx = 20,
                                                                            pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                            font = ("Arial", 20),
                                            text = "Analytical Instruments",
                                            command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                    column = 1,
                                                                                                                    rowspan = 2,
                                                                                                                    padx = 20,
                                                                                                                    pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                        rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        steps_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "EC Steps",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.ec_click(frame)).grid(row = 8, column = 3,
                                                                         rowspan = 2,
                                                                         padx = 10,
                                                                         pady = 20)        
        cal_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Calibration",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.pHEC.ec_cal_click(frame)).grid(row = 5, column = 0,
                                                                                          padx = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Measurement Mode",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.pHEC.ec_mode_click(frame)).grid(row = 6, column = 0,
                                                                                           padx = 20)
        
class phMeter:
     
    def ph_steps():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab pH Meter SOP",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        
        cal_check = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "Calibration Check",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ph_cal_check(frame)).grid(row = 4, column = 0,
                                    padx = 20,
                                    pady = 20)
        cal = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Calibration",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.pHEC.ph_cal(frame)).grid(row = 4, column = 1,
                                        padx = 20,
                                        pady = 20)
        meas = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Measurement",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.pHEC.ph_measure_click(frame)).grid(row = 4, column = 2,
                                        padx = 20,
                                        pady = 20)
        for i in range(5, 8):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Analytical Instruments",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                  column = 1,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                         rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
    def ph_cal_check():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab pH Meter SOP: Calibration Check",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        check = ins.ecph.ph_meter["CalCheck"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 9,
                        width = 48,
                        font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, rowspan = 2)
        text.insert(tk.END, check)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Analytical Instruments",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                  column = 1,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                         rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        steps_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "pH Steps",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ph_click(frame)).grid(row = 8, column = 3,
                                                                        rowspan = 2,
                                                                        padx = 20,
                                                                        pady = 20)
        cal_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "Calibration Mode",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ph_cal(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        measure_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                   text = "Measurement",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.pHEC.ph_measure_click(frame)).grid(row = 6, column = 2,
                                                                                             padx = 20,
                                                                                             pady = 20)
        
    def ph_cal():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab pH Meter SOP: Calibration Mode",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        cal = ins.ecph.ph_meter["Calibration"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 9,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, cal)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Analytical Instruments",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                  column = 1,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                         rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        steps_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "pH Steps",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ph_click(frame)).grid(row = 8, column = 3,
                                                                        rowspan = 2,
                                                                        padx = 20,
                                                                        pady = 20)
        cal_check_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Calibration Check",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.pHEC.ph_cal_check(frame)).grid(row = 5, column = 0,
                                                                                          padx = 20,
                                                                                          pady = 20)
        meas_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Measurement",
                                font = ("Arial", 20),
                                command = lambda: ctrl.pHEC.ph_measure_click(frame)).grid(row = 5, column = 2,
                                                                                          padx = 20,
                                                                                          pady = 20)
        
    def ph_measure_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab pH Meter SOP: Measurement",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        measure = ins.ecph.ph_meter["Measurement"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 9,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, rowspan = 2, columnspan = 2)
        text.insert(tk.END, measure)
        for i in range(7, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Analytical Instruments",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, 
                                                                                                                  column = 1,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
        phec_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                              text = "pH and EC Home",
                              font = ("Arial", 20),
                              command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 2,
                                                                         rowspan = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        steps_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "pH Steps",
                            font = ("Arial", 20),
                            command = lambda: ctrl.pHEC.ph_click(frame)).grid(row = 8, column = 3,
                                                                        rowspan = 2,
                                                                        padx = 20,
                                                                        pady = 20)
        cal_check_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     text = "Calibration Check",
                                     font = ("Arial", 20),
                                     command = lambda: ctrl.pHEC.ph_cal(frame)).grid(row = 5, column = 0,
                                                                                     pady = 20)
        cal_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Calibration Mode",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.pHEC.ph_cal(frame)).grid(row = 6, column = 0,
                                                                                          pady = 20)
        
