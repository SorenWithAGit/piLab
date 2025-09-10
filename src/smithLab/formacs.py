"""
########################################################################
formacs.py defines the classes and functions for the different
frames that are related to the Formacs TOC/TN Analyzer and are
being constructed through the operation of the piLab.
########################################################################
"""


import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

def tocHome():
    frame = tk.Frame(bg = "#055942", width = 1920, height = 1080)
    frame.pack()
    main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                          text = "Smith Lab: TOC Home",
                          font = ("Arial", 30)).grid(row = 0, columnspan = 3)
    for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
    standards = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                          text = "Formacs Standards and PO4 Acid",
                          font = ("Arial", 25),
                          command = lambda: ctrl.toc.stds(frame)).grid(row = 4, column = 0,
                                                     padx = 40,
                                                     pady = 40)
    steps = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                      text = "Formacs TOC Steps",
                      font = ("Arial", 25),
                      command = lambda: ctrl.toc.steps(frame)).grid(row = 4, column = 2,
                                                  padx = 40,
                                                  pady = 40)
    for i in range(5, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
    piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 40,
                                                                                        pady = 40)
    smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "Smith Lab Home",
                            command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10,
                                                                column = 0,
                                                                padx = 40,
                                                                pady = 40)
    instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 25),
                                    text = "Instrumentation SOPs",
                                    command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                            column = 2,
                                                                                                            rowspan = 2,
                                                                                                            padx = 40,
                                                                                                            pady = 40)

class formacsOperation:
    
    def standardFrame():
        frame = tk.Frame(bg = "#055942", width = 1920, height = 1080)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab: TOC Standards",
                            font = ("Arial", 30)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        std1 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "TC Standard",
                         font = ("Arial", 25),
                         command = lambda: ctrl.toc.std1(frame)).grid(row = 4, column = 0,
                                                     padx = 40,
                                                     pady = 40)
        std2 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "IC Standard",
                         font = ("Arial", 25),
                         command = lambda: ctrl.toc.std2(frame)).grid(row = 4, column = 1,
                                                     padx = 40,
                                                     pady = 40)
        std3 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "TN Standard",
                         font = ("Arial", 25),
                         command = lambda: ctrl.toc.std3(frame)).grid(row = 4, column = 2,
                                                     padx = 40,
                                                     pady = 40)
        phos = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Phosphoric Acid Protocol",
                         font = ("Arial", 25),
                         command = lambda: ctrl.toc.phos(frame)).grid(row = 4, column = 3,
                                                     padx = 40,
                                                     pady = 40)
        for i in range(5, 8):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 40,
                                                                                        pady = 40)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 25),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10,
                                                                    column = 0,
                                                                    padx = 40,
                                                                    pady = 40)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        font = ("Arial", 25),
                                        text = "Instrumentation SOPs",
                                        command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                                column = 2,
                                                                                                                rowspan = 2,
                                                                                                                padx = 40,
                                                                                                                pady = 40)
        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 25),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 3, rowspan = 2,
                                                                              padx = 40,
                                                                              pady = 40)
    
    def std1_click():
        frame = tk.Frame(bg = "#055942", width = 1920, height = 1080)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab TOC SOP: TC Standard",
                            font = ("Arial", 30)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        tcSTD = ins.formacsTOC.standard_prep["TC Stock"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 10,
                        width = 48,
                        font = ("Arial", 25),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, rowspan = 2)
        text.insert(tk.END, tcSTD)
        for i in range(7, 9):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 40,
                                                                                        pady = 40)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 25),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                    padx = 40,
                                                                    pady = 40)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 25),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 40,
                                                                                                    pady = 40)
        TOC_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 25),
                                    text = "TOC SOP Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    rowspan = 2,
                                                                                    padx = 40,
                                                                                    pady = 40)
        icSTD_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "IC Standard",
                                font = ("Arial", 25),
                                command = lambda: ctrl.toc.std2(frame)).grid(row = 5, column = 2,
                                                                                padx = 40,
                                                                                pady = 40)
        tnSTD_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "TN Standard",
                                font = ("Arial", 25),
                                command = lambda: ctrl.toc.std3(frame)).grid(row = 6, column = 2,
                                        padx = 40,
                                        pady = 40)
            
    def std2_click():
        frame = tk.Frame(bg = "#055942", width = 1920, height = 1080)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab TOC SOP: IC Standard",
                            font = ("Arial", 30)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        icSTD = ins.formacsTOC.standard_prep["IC Stock"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 10,
                        width = 48,
                        font = ("Arial", 25),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, icSTD)
        for i in range(6, 9):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 40,
                                                                                        pady = 40)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 25),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                    padx = 40,
                                                                    pady = 40)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 25),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 40,
                                                                                                    pady = 40)
        TOC_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 25),
                                    text = "TOC SOP Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    rowspan = 2,
                                                                                    padx = 40,
                                                                                    pady = 40)
        tcSTD_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "TC Standard",
                                font = ("Arial", 25),
                                command = lambda: ctrl.toc.std1(frame)).grid(row = 5, column = 0,
                                                                                padx = 40,
                                                                                pady = 40)
        tnSTD_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "TN Standard",
                                font = ("Arial", 25),
                                command = lambda: ctrl.toc.std3(frame)).grid(row = 5, column = 2,
                                        padx = 40,
                                        pady = 40)

    def std3_click():
        frame = tk.Frame(bg = "#055942", width = 1920, height = 1080)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab TOC SOP: TN Standard",
                            font = ("Arial", 30)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        tnSTD = ins.formacsTOC.standard_prep["TN Stock"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 10,
                        width = 48,
                        font = ("Arial", 25),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1, columnspan = 4, rowspan = 2)
        text.insert(tk.END, tnSTD)
        for i in range(6, 9):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 40,
                                                                                        pady = 40)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 25),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                    padx = 40,
                                                                    pady = 40)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 25),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                    column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 40,
                                                                                                    pady = 40)
        TOC_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 25),
                                    text = "TOC SOP Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    rowspan = 2,
                                                                                    padx = 40,
                                                                                    pady = 40)
        tcSTD_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "TC Standard",
                                font = ("Arial", 25),
                                command = lambda: ctrl.toc.std1(frame)).grid(row = 5, column = 0,
                                                                                padx = 40,
                                                                                pady = 40)
        icSTD_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "IC Standard",
                                font = ("Arial", 25),
                                command = lambda: ctrl.toc.std2(frame)).grid(row = 6, column = 0,
                                        padx = 40,
                                        pady = 40)
        
    def phos_click():
        frame = tk.Frame(bg = "#055942", width = 1920, height = 1080)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "Smith Lab TOC SOP: Phosphoric Acid",
                            font = ("Arial", 30)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        phos = ins.formacsTOC.phosphoricAcid
        text = tk.Text(frame, borderwidth = 0,
                        height = 10,
                        width = 48,
                        font = ("Arial", 25),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, phos)
        for i in range(6, 9):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 25),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 40,
                                                                                        pady = 40)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 25),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                    padx = 40,
                                                                    pady = 40)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 25),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 40,
                                                                                                    pady = 40)
        TOC_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 25),
                                    text = "TOC SOP Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    rowspan = 2,
                                                                                    padx = 40,
                                                                                    pady = 40)

    def stepsHome():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Steps",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step1_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step1(frame)).grid(row = 4, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step2(frame)).grid(row = 4, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step3(frame)).grid(row = 4, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step4(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step5_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 5",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step5(frame)).grid(row = 5, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step6_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 6",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step6(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)  

        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 30 ,
                                                                                        pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10,
                                                                        column = 0,
                                                                        padx = 30 ,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Instrumentation SOPs",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                                     column = 1,
                                                                                                                     rowspan = 2,
                                                                                                                     padx = 30 ,
                                                                                                                     pady = 20)
        TOC_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "TOC SOP Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    rowspan = 2,
                                                                                    padx = 30 ,
                                                                                    pady = 20)
    def step1():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Step 1",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step1"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)

        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "TOC SOP Steps",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 10, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        instrumentationSOP = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Instrumentation SOPs",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                             rowspan = 2,
                                                                                             padx = 20, 
                                                                                             pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.toc.step2(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step2():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Step 2",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step2"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "TOC SOP Steps",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 10, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        instrumentationSOP = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Instrumentation SOPs",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                             rowspan = 2,
                                                                                             padx = 20, 
                                                                                             pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.toc.step1(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: ctrl.toc.step3(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)    
        
    def step3():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Step 3",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step3"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "TOC SOP Steps",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 10, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        instrumentationSOP = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Instrumentation SOPs",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                             rowspan = 2,
                                                                                             padx = 20, 
                                                                                             pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.toc.step2(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: ctrl.toc.step4(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)    
    def step4():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Step 4",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step4"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "TOC SOP Steps",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 10, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        instrumentationSOP = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Instrumentation SOPs",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                             rowspan = 2,
                                                                                             padx = 20, 
                                                                                             pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: ctrl.toc.step3(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: ctrl.toc.step5(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    def step5():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Step 5",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step5"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "TOC SOP Steps",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 10, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        instrumentationSOP = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Instrumentation SOPs",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                             rowspan = 2,
                                                                                             padx = 20, 
                                                                                             pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: ctrl.toc.step4(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: ctrl.toc.step6(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    def step6():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab TOC SOP: Step 6",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step6"]
        text = tk.Text(frame, borderwidth = 0,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            font = ("Arial", 20),
                            text = "piLab Home",
                            command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        toc_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "TOC SOP Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "TOC SOP Steps",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 10, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        instrumentationSOP = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Instrumentation SOPs",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                             rowspan = 2,
                                                                                             padx = 20, 
                                                                                             pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: ctrl.toc.step5(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
