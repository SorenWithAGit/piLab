import tkinter as tk
from src.schantzLab import functions as fn
from src.schantzLab import schantzInstructions as si

class homeFrames:
        
    def schantz_lab_home():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Schantz Lab Home",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "").grid(row = i)
        instuments = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Instrument SOPs",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                        padx = 20,
                                        pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
    def instuments_frame():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Schantz Lab Home",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "").grid(row = i)
        lai = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                        text = "Leaf Area Index Meter",
                        font = ("Arial", 20),
                        ).grid(row = 8, column = 0,
                               padx = 20,
                               pady = 20)
        elementar = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "ELEMENTAR SOP",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.elementar(frame)).grid(row = 8, column = 1,
                                        padx = 20,
                                        pady = 20)
        rootScanner = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Root Scanner SOP",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.rootScanner_Frame(frame)).grid(row = 8, column = 2,
                                       padx = 20,
                                       pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 10, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        
class instrumentFrames:
      
    def elementar_frame():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Elementar Vario Max Cube",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "").grid(row = i)
        step1 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "SOP Step 1",
                            font = ("Arial", 20),
                            command = lambda: fn.elementarSOPs.step1(frame)).grid(row = 6, column = 0,
                                    padx = 20,
                                    pady = 20)
        step2 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "SOP Step 2",
                            font = ("Arial", 20),
                            command = lambda: fn.elementarSOPs.step2(frame)).grid(row = 6, column = 1,
                                    padx = 20,
                                    pady = 20)
        step3 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                            text = "SOP Step 3",
                            font = ("Arial", 20),
                            command = lambda: fn.elementarSOPs.step3(frame)).grid(row = 6, column = 2,
                                    padx = 20,
                                    pady = 20)
        for i in range(7,10):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 10, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 11, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     text = "Schantz Instrument SOPs",
                                     font = ("Arial", 20),
                                     command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 10, column = 1,
                                                                                                  rowspan = 2,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
    
    def root_scanner_frame():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Root Scanner",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "").grid(row = i)
        step1 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                        text = "SOP Step 1",
                        font = ("Arial", 20),
                        command = lambda: fn.rootScannerSOPs.step1(frame)).grid(row = 6, column = 0,
                                padx = 20,
                                pady = 20)
        step2 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                        text = "SOP Step 2",
                        font = ("Arial", 20),
                        command = lambda: fn.rootScannerSOPs.step2(frame)).grid(row = 6, column = 2,
                                padx = 20,
                                pady = 20)
        step3 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                        text = "SOP Step 3",
                        font = ("Arial", 20),
                        command = lambda: fn.rootScannerSOPs.step3(frame)).grid(row = 7, column = 0,
                                padx = 20,
                                pady = 20)
        step4 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                          text = "SOP Step 4",
                          font = ("Arial", 20),
                          command = lambda: fn.rootScannerSOPs.step4(frame)).grid(row = 7, column = 2,
                                 padx = 20,
                                 pady = 20)
        for i in range(8,10):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 10, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 11, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     text = "Schantz Instrument SOPs",
                                     font = ("Arial", 20),
                                     command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 10, column = 1,
                                                                                                  rowspan = 2,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        
class elementarSteps:
      
    def step1():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "Schantz Lab: Elementar Step 1",
                                font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        step1_INS = si.VarioMax.sop["Startup"]
        text = tk.Text(frame, borderwidth = 0,
                            height = 13,
                            width = 48,
                            font = ("Arial", 18),
                            bd = 5,
                            relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: fn.elementarSOPs.step2(frame)).grid(row = 5, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        text = "Schantz Instrument SOPs",
                                        font = ("Arial", 20),
                                        command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        elementar_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Elementar SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.elementar(frame)).grid(row = 8, column = 2,
                                                                                        rowspan = 2,
                                                                                        padx = 20,
                                                                                        pady = 20)
    def step2():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Schantz Lab: Elementar Step 2",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step1_INS = si.VarioMax.sop["Sequence"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 18),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Step 2",
                                    font = ("Arial", 20),
                                    command = lambda: fn.elementarSOPs.step1(frame)).grid(row = 5, column = 0)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: fn.elementarSOPs.step3(frame)).grid(row = 5, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     text = "Schantz Instrument SOPs",
                                     font = ("Arial", 20),
                                     command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                  rowspan = 2,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        elementar_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Elementar SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.elementar(frame)).grid(row = 8, column = 2,
                                                                                       rowspan = 2,
                                                                                       padx = 20,
                                                                                       pady = 20)
    def step3():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Schantz Lab: Elementar Step 3",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step1_INS = si.VarioMax.sop["Analysis"]
        text = tk.Text(frame, borderwidth = 0,
                           height = 13,
                           width = 48,
                           font = ("Arial", 18),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Step 2",
                                    font = ("Arial", 20),
                                    command = lambda: fn.elementarSOPs.step2(frame)).grid(row = 5, column = 0,
                                                                                          padx = 20,
                                                                                          pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 20)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     text = "Schantz Instrument SOPs",
                                     font = ("Arial", 20),
                                     command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                  rowspan = 2,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        elementar_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Elementar SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.elementar(frame)).grid(row = 8, column = 2,
                                                                                       rowspan = 2,
                                                                                       padx = 20,
                                                                                       pady = 20)

class rootScannerSteps:
     
    def step1():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "Schantz Lab: Root Scanner Step 1",
                                font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        step1_INS = si.rootScanner.sop["Root Processing"]
        text = tk.Text(frame, borderwidth = 0,
                            height = 18,
                            width = 48,
                            font = ("Arial", 17),
                            bd = 5,
                            relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: fn.rootScannerSOPs.step2(frame)).grid(row = 5, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        text = "Schantz Instrument SOPs",
                                        font = ("Arial", 20),
                                        command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 10)
        root_scanner_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Root Scanner SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.rootScanner_Frame(frame)).grid(row = 8, column = 2,
                                                                                        rowspan = 2,
                                                                                        padx = 20,
                                                                                        pady = 10)
    def step2():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "Schantz Lab: Root Scanner Step 2",
                                font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        step1_INS = si.rootScanner.sop["Setup"]
        text = tk.Text(frame, borderwidth = 0,
                            height = 18,
                            width = 48,
                            font = ("Arial", 17),
                            bd = 5,
                            relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Step 1",
                                    font = ("Arial", 20,),
                                    command = lambda: fn.rootScannerSOPs.step1(frame)).grid(row = 5, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: fn.rootScannerSOPs.step3(frame)).grid(row = 5, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        text = "Schantz Instrument SOPs",
                                        font = ("Arial", 20),
                                        command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 10)
        root_scanner_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Root Scanner SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.rootScanner_Frame(frame)).grid(row = 8, column = 2,
                                                                                        rowspan = 2,
                                                                                        padx = 20,
                                                                                        pady = 10)
    def step3():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "Schantz Lab: Root Scanner Step 3",
                                font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        step1_INS = si.rootScanner.sop["Scanning"]
        text = tk.Text(frame, borderwidth = 0,
                            height = 18,
                            width = 48,
                            font = ("Arial", 17),
                            bd = 5,
                            relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Step 2",
                                    font = ("Arial", 20,),
                                    command = lambda: fn.rootScannerSOPs.step2(frame)).grid(row = 5, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: fn.rootScannerSOPs.step4(frame)).grid(row = 5, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        text = "Schantz Instrument SOPs",
                                        font = ("Arial", 20),
                                        command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 10)
        root_scanner_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Root Scanner SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.rootScanner_Frame(frame)).grid(row = 8, column = 2,
                                                                                        rowspan = 2,
                                                                                        padx = 20,
                                                                                        pady = 10)
    def step4():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "Schantz Lab: Root Scanner Step 4",
                                font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        step1_INS = si.rootScanner.sop["XLRhizo"]
        text = tk.Text(frame, borderwidth = 0,
                            height = 18,
                            width = 48,
                            font = ("Arial", 17),
                            bd = 5,
                            relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        text.insert(tk.END, step1_INS)
        for i in range(6, 7):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Step 3",
                                    font = ("Arial", 20,),
                                    command = lambda: fn.rootScannerSOPs.step3(frame)).grid(row = 5, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "piLab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.piLab_Home_Frame(frame)).grid(row = 8, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        schantz_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Schantz Lab Home",
                                font = ("Arial", 20),
                                command = lambda: fn.frames.schantz_Home_Frame(frame)).grid(row = 9, column = 0,
                                                                    padx = 20,
                                                                    pady = 10)
        instuments_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                        text = "Schantz Instrument SOPs",
                                        font = ("Arial", 20),
                                        command = lambda: fn.frames.schantz_instruments(frame)).grid(row = 8, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 10)
        root_scanner_frame = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Root Scanner SOP",
                                    font = ("Arial", 20),
                                    command = lambda: fn.frames.rootScanner_Frame(frame)).grid(row = 8, column = 2,
                                                                                        rowspan = 2,
                                                                                        padx = 20,
                                                                                        pady = 10)