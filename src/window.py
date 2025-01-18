import tkinter as tk
from src import procedure as pr
from src import instructions as ins
from src import ghg
from src import icp

class window:

    def piLab_home():
         welcome = ins.welcome.welcome_statment
         frame = tk.Frame()
         frame.pack()
         icp_op = ins.icp_operation
         label = tk.Label(frame,
                          text = "piLab Home",
                          font = ("Arial", 25)).grid(row = 0, column = 1)
         welcome_label = tk.Label(frame,
                          text = welcome,
                           height = 10,
                           width = 52,
                           font = ("Arial", 20)).grid(row = 1, column = 1)
         smith_lab = tk.Button(frame,
                               text = "Smith Lab",
                               font = ("Arial", 20),
                               command = lambda: window.smith_lab_click(frame)).grid(row = 2, column = 1,
                                                                                 padx = 20,
                                                                                 pady = 20)
         yost_lab = tk.Button(frame,
                              text = "Yost Lab?",
                              font = ("Arial", 20),
                              ).grid(row = 3, column = 1,
                                     padx = 20,
                                     pady = 20)
         Schantz_lab = tk.Button(frame,
                              text = "Schantz Lab?",
                              font = ("Arial", 20),
                              ).grid(row = 4, column = 1,
                                     padx = 20,
                                     pady = 20)

    def clear_frame(frame):
        frame.destroy()
    
    def Smith_lab_home():
        frame = tk.Frame()
        frame.pack()
        label = tk.Label(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 25)).grid(row = 0, column = 1)
        for i in range(1,6):
                label = tk.Label(frame,
                                text = "").grid(row = i)
        extracts = tk.Button(frame,
                             text = "Extractant Recipes",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(frame),
                                               pr.procedure_selection.extracts_click()] ).grid(row = 7, column = 1, padx = 20, pady = 20)

        instrument_recipies = tk.Button(frame,
                                text = "Instrument Recipes",
                                font = ("Arial", 20),
                                command = lambda: [window.clear_frame(frame),
                                                   pr.procedure_selection.instruments_click()]).grid(row = 7, column = 3, padx = 20, pady = 20)
        extraction_protocols = tk.Button(frame,
                              text = "Extraction Protocols",
                              font = ("Arial", 20),
                              command = lambda: [window.clear_frame(frame),
                                                 pr.procedure_selection.extraction_protocol()]).grid(row = 8, column = 1, padx = 20, pady = 20)
        analytical_instruments = tk.Button(frame,
                                text = "Analytical Instrumentation",
                                font = ("Arial", 20),
                                command = lambda: [window.clear_frame(frame),
                                                   pr.procedure_selection.analytical_instruments()]).grid(row = 8, column = 3, padx = 20, pady = 20)
        piLab_home = tk.Button(frame,
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: [window.clear_frame(frame),
                                                  window.piLab_home()]).grid(row = 9, column = 0,
                                                                     padx = 20,
                                                                     pady = 20)
        
    def smith_lab_click(frame):
         window.clear_frame(frame)
         window.Smith_lab_home()

class icpWindowControl:

    def std4_click(frame):
         window.clear_frame(frame)
         icp.icp_cookbook.icp_element_frame()

    def std3_click(frame):
         window.clear_frame(frame)
         icp.icp_control.std_3_proto()
    
    def std2_click(frame):
         window.clear_frame(frame)
         icp.icp_control.std_2_proto()

    def std1_click(frame):
         window.clear_frame(frame)
         icp.icp_control.std_2_proto()

    


class ghgWindowControl:

    def stds_click(frame):
          window.clear_frame(frame)
          ghg.operating_procedure.stds()
    
    def step1_click(frame):
        window.clear_frame(frame)
        ghg.operating_procedure.step1()

    def step2_click(frame):
         window.clear_frame(frame)
         ghg.operating_procedure.step2()
    
    def step3_click(frame):
         window.clear_frame(frame)
         ghg.operating_procedure.step3()
    
    def step4_click(frame):
         window.clear_frame(frame)
         ghg.operating_procedure.step4()
