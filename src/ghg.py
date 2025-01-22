import tkinter as tk
from src import control as cl
from src import instructions as ins

class ghg_window:
    def steps():
        frame = tk.Frame()
        frame.pack()
        
        main_label = tk.Label(frame,
                              text = "SCION456 GHG SOP",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        stds_click = tk.Button(frame,
                               text = "GHG Standards",
                               font = ("Arial", 20),
                               command = lambda: cl.ghgWindowControl.stds_click(frame)).grid(row = 4, column = 0,
                                                                                    padx = 20, 
                                                                                    pady = 20)
        step1_click = tk.Button(frame,
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: cl.ghgWindowControl.step1_click(frame)).grid(row = 4, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(frame,
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: cl.ghgWindowControl.step2_click(frame)).grid(row = 4, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(frame,
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: cl.ghgWindowControl.step3_click(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(frame,
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: cl.ghgWindowControl.step4_click(frame)).grid(row = 5, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        for i in range(7, 10):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smtih_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: cl.window.smith_lab_click(frame)).grid(row = 10,
                                                                        column = 0,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame,
                                         font = ("Arial", 20),
                                         text = "Instrumentation Home",
                                         command = lambda: cl.window.analytical_instrumentation_click(frame)).grid(row = 10, 
                                                                                                                  column = 2)
class operating_procedure:

    def stds():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "SCION456 GHG SOP: Standards",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        stds = ins.ghg_stds
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        step = stds.stds
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [cl.window.clear_frame(frame),
                                    cl.window.Smith_lab_home()]).grid(row = 6, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [cl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 6, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step1()]).grid(row = 7, column = 2)

    def step1():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "SCION456 GHG SOP: Step 1",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        step = ghg_op.step1
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [cl.window.clear_frame(frame),
                                    cl.window.Smith_lab_home()]).grid(row = 6, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [cl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 6, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step2()]).grid(row = 7, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    

    def step2():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "SCION456 GHG SOP: Step 2",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        step = ghg_op.step2
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [cl.window.clear_frame(frame),
                                    cl.window.Smith_lab_home()]).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [cl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 6, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step1()]).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step3()]).grid(row = 7, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)

    def step3():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "SCION456 GHG SOP: Step 3",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        step = ghg_op.step3
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [cl.window.clear_frame(frame),
                                    cl.window.Smith_lab_home()]).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [cl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 6, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step2()]).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step4()]).grid(row = 7, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step4():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "SCION456 GHG SOP: Step 4",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        ghg_op = ins.ghg_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 1)
        step = ghg_op.step4
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [cl.window.clear_frame(frame),
                                    cl.window.Smith_lab_home()]).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [cl.window.clear_frame(frame),
                                                        ghg_window.steps()]).grid(row = 6, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [cl.window.clear_frame(frame),
                                                   operating_procedure.step3()]).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)