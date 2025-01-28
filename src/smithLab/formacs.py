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
    frame = tk.Frame()
    frame.pack()
    main_label = tk.Label(frame,
                          text = "Smith Lab: TOC Home",
                          font = ("Arial", 25)).grid(row = 0, columnspan = 3)
    for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
    standards = tk.Button(frame,
                          text = "Formacs Standards and PO4 Acid",
                          font = ("Arial", 20),
                          command = lambda: ctrl.toc.stds(frame)).grid(row = 4, column = 0,
                                                     padx = 20,
                                                     pady = 20)
    steps = tk.Button(frame,
                      text = "Formacs TOC Steps",
                      font = ("Arial", 20),
                      command = lambda: ctrl.toc.steps(frame)).grid(row = 4, column = 2,
                                                  padx = 20,
                                                  pady = 20)
    for i in range(5, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
    smtih_home_button = tk.Button(frame,
                            font = ("Arial", 20),
                            text = "Smith Lab Home",
                            command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                column = 0,
                                                                pady = 20)
    instrumentation_home = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "Instrumentation Home",
                                    command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                            column = 2)

class formacsOperation:
    
    def standardFrame():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                            text = "Smith Lab: TOC Standards",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                                text = "").grid(row = i)
        std1 = tk.Button(frame,
                         text = "TC Standard",
                         font = ("Arial", 20),
                         command = lambda: ctrl.toc.std1(frame)).grid(row = 4, column = 0,
                                                     padx = 20,
                                                     pady = 20)
        std2 = tk.Button(frame,
                         text = "IC Standard",
                         font = ("Arial", 20),
                         command = lambda: ctrl.toc.std2(frame)).grid(row = 4, column = 1,
                                                     padx = 20,
                                                     pady = 20)
        std3 = tk.Button(frame,
                         text = "TN Standard",
                         font = ("Arial", 20),
                         command = lambda: ctrl.toc.std3(frame)).grid(row = 4, column = 2,
                                                     padx = 20,
                                                     pady = 20)
        phos = tk.Button(frame,
                         text = "Phosphoric Acid Protocol",
                         font = ("Arial", 20,),
                         command = lambda: ctrl.toc.phos(frame)).grid(row = 4, column = 3,
                                                     padx = 20,
                                                     pady = 20)
        for i in range(5, 8):
                label = tk.Label(frame,
                                text = "").grid(row = i)
        smtih_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                    column = 0,
                                                                    pady = 20)
        instrumentation_home = tk.Button(frame,
                                        font = ("Arial", 20),
                                        text = "Instrumentation Home",
                                        command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                                column = 1,
                                                                                                                columnspan = 2)
        toc_home = tk.Button(frame,
                             text = "TOC Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 3,
                                                                              padx = 20,
                                                                              pady = 20)
    
    def std1_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                            text = "Smith Lab TOC SOP: TC Standard",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        tcSTD = ins.formacsTOC.standard_prep["TC Stock"]
        text = tk.Text(frame,
                        height = 10,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, tcSTD)
        for i in range(6, 8):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instructions_home = tk.Button(frame,
                                      font = ("Arial", 20),
                                      text = "Instrumentation Home",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        TOC_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        icSTD_button = tk.Button(frame,
                                text = "IC Standard",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.std2(frame)).grid(row = 10, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        tnSTD_button = tk.Button(frame,
                                text = "TN Standard",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.std3(frame)).grid(row = 10, column = 2,
                                        padx = 20,
                                        pady = 20)
            
    def std2_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                            text = "Smith Lab TOC SOP: IC Standard",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        icSTD = ins.formacsTOC.standard_prep["IC Stock"]
        text = tk.Text(frame,
                        height = 10,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, icSTD)
        for i in range(6, 8):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instructions_home = tk.Button(frame,
                                      font = ("Arial", 20),
                                      text = "Instrumentation Home",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        TOC_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        tcSTD_button = tk.Button(frame,
                                text = "TC Standard",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.std1(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        tnSTD_button = tk.Button(frame,
                                text = "TN Standard",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.std3(frame)).grid(row = 10, column = 2,
                                        padx = 20,
                                        pady = 20)

    def std3_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                            text = "Smith Lab TOC SOP: TN Standard",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        tnSTD = ins.formacsTOC.standard_prep["TN Stock"]
        text = tk.Text(frame,
                        height = 10,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, tnSTD)
        for i in range(6, 8):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instructions_home = tk.Button(frame,
                                      font = ("Arial", 20),
                                      text = "Instrumentation Home",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        TOC_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        tcSTD_button = tk.Button(frame,
                                text = "TC Standard",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.std1(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        icSTD_button = tk.Button(frame,
                                text = "IC Standard",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.std2(frame)).grid(row = 10, column = 1,
                                        padx = 20,
                                        pady = 20)
        
    def phos_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                            text = "Smith Lab TOC SOP: Phosphoric Acid",
                            font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        phos = ins.formacsTOC.phosphoricAcid
        text = tk.Text(frame,
                        height = 10,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, phos)
        for i in range(6, 8):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instructions_home = tk.Button(frame,
                                      font = ("Arial", 20),
                                      text = "Instrumentation Home",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        TOC_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)

    def stepsHome():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Steps",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step1_click = tk.Button(frame,
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step1(frame)).grid(row = 4, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(frame,
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step2(frame)).grid(row = 4, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(frame,
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step3(frame)).grid(row = 4, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(frame,
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step4(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step5_click = tk.Button(frame,
                                text = "Step 5",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step5(frame)).grid(row = 5, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step6_click = tk.Button(frame,
                                text = "Step 6",
                                font = ("Arial", 20),
                                command = lambda: ctrl.toc.step6(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)  

        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smtih_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9,
                                                                        column = 0,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame,
                                         font = ("Arial", 20),
                                         text = "Instrumentation Home",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                                     padx = 20,
                                                                                                                     pady = 20)
        TOC_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Home",
                                    command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
    def step1():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Step 1",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step1"]
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        toc_home = tk.Button(frame,
                             text = "TOC Home",
                             font = ("Arial", 20),
                             command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 1,
                                                                               padx = 20,
                                                                               pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "TOC Step Home",
                                     command = lambda: ctrl.toc.steps(frame)).grid(row = 9, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.toc.step2(frame)).grid(row = 10, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step2():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Step 2",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step2"]
        text = tk.Text(frame,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        toc_home = tk.Button(frame,
                            text = "TOC Home",
                            font = ("Arial", 20),
                            command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 1,
                                                                            padx = 20,
                                                                            pady = 20) 
        step_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Step Home",
                                    command = lambda: ctrl.toc.steps(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.toc.step1(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: ctrl.toc.step3(frame)).grid(row = 10, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)    
        
    def step3():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Step 3",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step3"]
        text = tk.Text(frame,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        toc_home = tk.Button(frame,
                            text = "TOC Home",
                            font = ("Arial", 20),
                            command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 1,
                                                                            padx = 20,
                                                                            pady = 20) 
        step_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Step Home",
                                    command = lambda: ctrl.toc.steps(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.toc.step2(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: ctrl.toc.step4(frame)).grid(row = 10, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)    
    def step4():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Step 4",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step4"]
        text = tk.Text(frame,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        toc_home = tk.Button(frame,
                            text = "TOC Home",
                            font = ("Arial", 20),
                            command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 1,
                                                                            padx = 20,
                                                                            pady = 20) 
        step_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Step Home",
                                    command = lambda: ctrl.toc.steps(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: ctrl.toc.step3(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: ctrl.toc.step5(frame)).grid(row = 10, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    def step5():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Step 5",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step5"]
        text = tk.Text(frame,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        toc_home = tk.Button(frame,
                            text = "TOC Home",
                            font = ("Arial", 20),
                            command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 1,
                                                                            padx = 20,
                                                                            pady = 20) 
        step_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Step Home",
                                    command = lambda: ctrl.toc.steps(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: ctrl.toc.step4(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: ctrl.toc.step6(frame)).grid(row = 10, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    def step6():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab TOC SOP: Step 6",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 3):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step = ins.formacsTOC.formacsOperation["Step6"]
        text = tk.Text(frame,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        toc_home = tk.Button(frame,
                            text = "TOC Home",
                            font = ("Arial", 20),
                            command = lambda: ctrl.toc.toc_home(frame)).grid(row = 9, column = 1,
                                                                            padx = 20,
                                                                            pady = 20) 
        step_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "TOC Step Home",
                                    command = lambda: ctrl.toc.steps(frame)).grid(row = 9, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: ctrl.toc.step5(frame)).grid(row = 10, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
