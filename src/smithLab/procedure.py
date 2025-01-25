import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

class mainFrames:

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
                              font = ("Arial", 20)).grid(row = 1, columnspan = 3)
          smith_lab = tk.Button(frame,
                                   text = "Smith Lab",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 2, column = 1,
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


    def Smith_lab_home():
          frame = tk.Frame()
          frame.pack()
          label = tk.Label(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 25)).grid(row = 0, columnspan = 4)
          for i in range(1,6):
                    label = tk.Label(frame,
                                   text = "").grid(row = i)
          extracts = tk.Button(frame,
                              text = "Extractant Recipes",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)

          instrument_recipies = tk.Button(frame,
                                   text = "Instrument Recipes",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.instruments_click(frame)).grid(row = 7, column = 3, padx = 20, pady = 20)
          extraction_protocols = tk.Button(frame,
                              text = "Extraction Protocols",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 8, column = 1, padx = 20, pady = 20)
          analytical_instruments = tk.Button(frame,
                                   text = "Analytical Instrumentation",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, column = 3, padx = 20, pady = 20)
          piLab_home = tk.Button(frame,
                                   text = "piLab Home",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)

class procedure_selection:

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
                              font = ("Arial", 20)).grid(row = 1, columnspan = 3)
          smith_lab = tk.Button(frame,
                                   text = "Smith Lab",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 2, column = 1,
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


    def Smith_lab_home():
          frame = tk.Frame()
          frame.pack()
          label = tk.Label(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 25)).grid(row = 0, columnspan = 4)
          for i in range(1,6):
                    label = tk.Label(frame,
                                   text = "").grid(row = i)
          extracts = tk.Button(frame,
                              text = "Extractant Recipes",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)

          instrument_recipies = tk.Button(frame,
                                   text = "Instrument Recipes",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.instruments_click(frame)).grid(row = 7, column = 3, padx = 20, pady = 20)
          extraction_protocols = tk.Button(frame,
                              text = "Extraction Protocols",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 8, column = 1, padx = 20, pady = 20)
          analytical_instruments = tk.Button(frame,
                                   text = "Analytical Instrumentation",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 8, column = 3, padx = 20, pady = 20)
          piLab_home = tk.Button(frame,
                                   text = "piLab Home",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)

    def instruments_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Instrument Recipes Selection",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        icp = tk.Button(frame,
                        text = "ICP-OES",
                        font = ("Arial", 25),
                        command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 7, column = 0, padx = 20, pady = 20)
        cfa = tk.Button(frame,
                        text = "Skalar San ++",
                        font = ("Arial", 25),
                        command = lambda: ctrl.skalarWindowControl.skalar_home(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)
        for i in range(9,12):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 12, column = 0, padx = 20, pady = 20)
    def extracts_click():     
         frame = tk.Frame()
         frame.pack()
         main_label = tk.Label(frame,
                               text = "Smith Lab: Extraction Recipes",
                               font = ("Arial", 25)).grid(row = 0, columnspan = 3)
         for i in range(1,6):
             label = tk.Label(frame,
                              text = "").grid(row = i)
         m3 = tk.Button(frame,
                       text = "Mehlich 3",
                       font = ("Arial", 20),
                       command = lambda: ctrl.procedureControl.m3_click(frame)).grid(row = 7, column = 0, padx = 20, pady = 20)
         h3a = tk.Button(frame,
                        text = "H3A: Haney 3 Acids",
                        font = ("Arial", 20),
                        command = lambda: ctrl.procedureControl.h3a_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 20)
         olsen = tk.Button(frame,
                          text = "Olsen P",
                          font = ("Arial", 20),
                          command = lambda: ctrl.procedureControl.olsen_click(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)
         kcl = tk.Button(frame,
                        text = "KCl: Potassium Chloride",
                        font = ("Arial", 20),
                        command = lambda: ctrl.procedureControl.kcl_click(frame)).grid(row = 8, column = 2, padx = 20, pady = 20)
         for i in range(9,12):
            label = tk.Label(frame,
                             text = "").grid(row = i)
         smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 12, column = 0, padx = 20, pady = 20)
    
    
    def m3_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Mehlich 3 Recipes",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        stock = tk.Button(frame,
                          text = "M3 Stock Solution",
                          font = ("Arial", 20),
                          command = lambda: ctrl.procedureControl.stock_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        m3_1L = tk.Button(frame,
                          text = "M3 Solution 2.5 L",
                          font = ("Arial", 20),
                          command = lambda: ctrl.procedureControl.m3_1_click(frame)).grid(row = 7, column = 3, padx = 20, pady = 20)
        m3_2L = tk.Button(frame,
                          text = "M3 Solution 5 L",
                          font = ("Arial", 20),
                          command = lambda: ctrl.procedureControl.m3_2_click(frame)).grid(row = 8, column =2, padx = 20, pady = 20)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 9, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def h3a_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Haney 3 Acids Recipes",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        h3a_1L = tk.Button(frame,
                           text = "H3A 1 L",
                           font = ("Arial", 20),
                           command = lambda: ctrl.procedureControl.h3a_1_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        h3a_2L = tk.Button(frame,
                           text = "H3A 2 L",
                           font = ("Arial", 20),
                           command = lambda: ctrl.procedureControl.h3a_2_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 20)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 8, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def olsen_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Olsen P Recipes",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        olsen_1L = tk.Button(frame,
                             text = "Olsen P 1 L",
                             font = ("Arial", 20),
                             command = lambda: ctrl.procedureControl.olsen_1_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        olsen_2L = tk.Button(frame,
                             text = "Olsen P 2 L",
                             font = ("Arial", 20),
                             command = lambda: ctrl.procedureControl.olsen_2_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 20)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 8, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Potassium Chloride Recipes",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        kcl_1N_1L = tk.Button(frame,
                              text = "1N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.kcl_1N_1L(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        kcl_1N_2L = tk.Button(frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.kcl_1N_2L(frame)).grid(row = 7, column =2, padx = 20, pady = 20)
        kcl_2N_1L = tk.Button(frame,
                              text = "2N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.kcl_2N_1L(frame)).grid(row = 8, column =1, padx = 20, pady = 20)
        kcl_2N_2L = tk.Button(frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: ctrl.procedureControl.kcl_2N_2L(frame)).grid(row = 8, column =2, padx = 20, pady = 20)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 9, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        
    def extraction_protocol():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Extraction Protocols",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        mehlich3 = tk.Button(frame,
                             text = "M3 Extraction",
                             font = ("Arial", 20),
                             command = lambda: ctrl.procedureControl.m3_proto_click(frame)).grid(row = 7, column = 1,
                                                                                              padx = 20,
                                                                                              pady = 20)
        potassiumChloride = tk.Button(frame,
                            text = "KCl Extraction",
                            font = ("Arial", 20),
                            command = lambda: ctrl.procedureControl.kcl_proto_click(frame)).grid(row = 7, column = 2,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        olsenP = tk.Button(frame,
                           text = "Olsen P Extraction",
                           font = ("Arial", 20),
                           command = lambda: ctrl.procedureControl.olsen_proto_click(frame)).grid(row = 7, column = 3,
                                                                                        padx = 20,
                                                                                        pady = 20)
        h3a = tk.Button(frame,
                        text = ("H3A Extraction"),
                        font = ("Arial", 20),
                        command = lambda: ctrl.procedureControl.h3a_proto_click(frame)).grid(row = 8, column = 1,
                                                                                  padx = 20,
                                                                                  pady = 20)
        hcl = tk.Button(frame,
                        text = "HCl Extraction",
                        font = ("Arial", 20),
                        command = lambda: ctrl.procedureControl.hcl_proto_click(frame)).grid(row = 8, column = 3,
                                                                                  padx = 20,
                                                                                  pady = 20)
        for i in range(9,12):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 12, column = 0, padx = 20, pady = 20)

    def analytical_instruments():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Smith Lab: Analytical Instrumentation Protocols",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        icp_button = tk.Button(frame,
                               text = "ICP-OES",
                               font = ("Arial", 20),
                               command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 7, column = 0,
                                                                                    padx = 20,
                                                                                    pady = 20)
        skalar_button = tk.Button(frame,
                                  text = "Skalar CFA",
                                  font = ("Arial", 20),
                                  command = lambda: ctrl.skalarWindowControl.step_home(frame)).grid(row = 7, column = 1,
                                                                               padx = 20,
                                                                               pady = 20)
        scion456 = tk.Button(frame,
                             text = "SCION 456 GHG",
                             font = ("Arial", 20),
                             command = lambda: ctrl.ghgWindowControl.steps_home(frame)).grid(row = 7, column = 2,
                                                                             padx = 20,
                                                                             pady = 20)
        mars6 = tk.Button(frame,
                          text = "Microwave Digestor",
                          font = ("Arial", 20),
                          command = lambda: ctrl.microwaveDigest.digestHome(frame)).grid(row = 8, column = 0,
                                                                                         padx = 20,
                                                                                         pady = 20)
        phec = tk.Button(frame,
                         text = "pH and Conductivity Meters",
                         font = ("Arial", 20),
                         command = lambda: ctrl.pHEC.phec_home(frame)).grid(row = 8, column = 1,
                                                                            padx = 20,
                                                                            pady = 20)
        toc = tk.Button(frame,
                        text = "Formacs TOC",
                        font = ("Arial", 20),
                        command = lambda: ctrl.toc.toc_home(frame)).grid(row = 8, column = 2,
                                                                         padx = 20,
                                                                         pady = 20)
        for i in range(9,12):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 12, column = 0, padx = 20, pady = 20)