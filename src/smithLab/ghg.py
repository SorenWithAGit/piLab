"""
########################################################################
ghg.py defines the classes and functions for the different
frames that are related to the SCION456 Greenhouse Gas Gas Chromatograph
and are being constructed through the operation of the piLab.
########################################################################
"""
import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

class ghg_window:
    def steps():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smtith Lab: SCION456 GHG SOP",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        stds_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "GHG Standards",
                               font = ("Arial", 20),
                               command = lambda: ctrl.ghgWindowControl.stds_click(frame)).grid(row = 4, column = 0,
                                                                                    padx = 20, 
                                                                                    pady = 20)
        step1_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: ctrl.ghgWindowControl.step1_click(frame)).grid(row = 4, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: ctrl.ghgWindowControl.step2_click(frame)).grid(row = 4, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: ctrl.ghgWindowControl.step3_click(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: ctrl.ghgWindowControl.step4_click(frame)).grid(row = 5, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        for i in range(7, 10):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "piLab Home",
                                    font = ("Arial", 20),
                                    command  = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 10,
                                                                                              column = 0,
                                                                                              padx = 20,
                                                                                              pady = 20)
        smtih_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 11,
                                                                        column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                         font = ("Arial", 20),
                                         text = "Analytical Instruments",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 10, 
                                                                                                                  column = 2,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)
class operating_procedure:

    def stds():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: SCION456 GHG SOP: Standards",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        stds = ins.ghg_stds
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = stds.stds
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "piLab Home",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                 padx = 5  , 
                                                                                                 pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 5  ,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Analytical Instruments",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                    column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 5  ,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "GHG SOP Steps",
                                     command = lambda: [ctrl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 5  ,
                                                                                      pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step1()]).grid(row = 5, column = 2)

    def step1():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: SCION456 GHG SOP: Step 1",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = ghg_op.step1
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "piLab Home",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                 padx = 5  , 
                                                                                                 pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 5  ,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Analytical Instruments",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                    column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 5  ,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "GHG SOP Steps",
                                     command = lambda: [ctrl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 5  ,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    font = ("Arial", 20),
                                    text = "Standards",
                                    command = lambda: [ctrl.window.clear_frame(frame),
                                                       operating_procedure.stds()]).grid(row = 5, column = 0,
                                                                                         padx = 5,
                                                                                         pady = 5)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step2()]).grid(row = 5, column = 2,
                                                                                padx = 5  ,
                                                                                pady = 20)
    

    def step2():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: SCION456 GHG SOP: Step 2",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = ghg_op.step2
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "piLab Home",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                 padx = 5  , 
                                                                                                 pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 5  ,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Analytical Instruments",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                    column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 5  ,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "GHG SOP Steps",
                                     command = lambda: [ctrl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 5  ,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step1()]).grid(row = 5, column = 0,
                                                                                padx = 5  ,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step3()]).grid(row = 5, column = 2,
                                                                                padx = 5  ,
                                                                                pady = 20)

    def step3():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: SCION456 GHG SOP: Step 3",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = ghg_op.step3
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "piLab Home",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                 padx = 5  , 
                                                                                                 pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 5  ,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Analytical Instruments",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                    column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 5  ,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "GHG SOP Steps",
                                     command = lambda: [ctrl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 5  ,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step2()]).grid(row = 5, column = 0,
                                                                                padx = 5  ,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step4()]).grid(row = 5, column = 2,
                                                                                padx = 5  ,
                                                                                pady = 20)
    
    def step4():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: SCION456 GHG SOP: Step 4",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = ghg_op.step4
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "piLab Home",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                                 padx = 5  , 
                                                                                                 pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 5  ,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Analytical Instruments",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, 
                                                                                                    column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 5  ,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "GHG SOP Steps",
                                     command = lambda: [ctrl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 5  ,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   operating_procedure.step3()]).grid(row = 5, column = 0,
                                                                                padx = 5  ,
                                                                                pady = 20)