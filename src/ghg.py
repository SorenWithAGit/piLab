import tkinter as tk
import window as mw
import instructions as ins

class ghg_window:
    def steps():
        step_frame = tk.Frame()
        step_frame.pack()
        stds_click = tk.Button(step_frame,
                               text = "GHG Standards",
                               font = ("Arial", 20),
                               command = lambda: [mw.window.clear_frame(step_frame),
                                                  operating_procedure.stds()]).grid(row = 0, column = 0,
                                                                                    padx = 20, 
                                                                                    pady = 20)
        step1_click = tk.Button(step_frame,
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step1()]).grid(row = 0, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(step_frame,
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step2()]).grid(row = 0, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(step_frame,
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step3()]).grid(row = 1, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(step_frame,
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step4()]).grid(row = 1, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        smtih_home_button = tk.Button(step_frame,
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: [mw.window.clear_frame(step_frame),
                                        mw.window.Smith_lab_home()]).grid(row = 5,
                                                                        column = 0,
                                                                        pady = 20)
class operating_procedure:

    def stds():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        stds = ins.ghg_stds
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = stds.stds
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        ghg_window.steps()]).grid(row = 1, column = 1,
                                                                                      padx = 20,
                                                                                      pady = 20)

    def step1():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        ghg_op = ins.ghg_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = ghg_op.step1
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        ghg_window.steps()]).grid(row = 1, column = 1,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step2()]).grid(row = 1, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    

    def step2():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        ghg_op = ins.ghg_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = ghg_op.step2
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        ghg_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step1()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step3()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)

    def step3():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        ghg_op = ins.ghg_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = ghg_op.step3
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        ghg_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step2()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step4()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step4():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        ghg_op = ins.ghg_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = ghg_op.step4
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "GHG Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        ghg_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step3()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)