import tkinter as tk
import window as mw
import skalar as sk
import icp as ic
import instructions as ins
import extractions as ex

class procedure_selection:

    def instruments_click():
        instrument_frame = tk.Frame()
        instrument_frame.pack()
        for i in range(6):
            label = tk.Label(instrument_frame,
                             text = "").grid(row = i)
        icp = tk.Button(instrument_frame,
                        text = "ICP-OES",
                        font = ("Arial", 25),
                        command = lambda: [mw.window.clear_frame(instrument_frame),
                                           ic.icp_cookbook.icp_home_frame()]).grid(row = 7, column = 0, padx = 20, pady = 20)
        cfa = tk.Button(instrument_frame,
                        text = "Skalar San ++",
                        font = ("Arial", 25),
                        command = lambda: [mw.window.clear_frame(instrument_frame),
                                           sk.skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)
        piLab_home = tk.Button(instrument_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(instrument_frame),
                                            mw.window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)
    def extracts_click():     
         extract_frame = tk.Frame()
         extract_frame.pack()
         for i in range(6):
             label = tk.Label(extract_frame,
                              text = "").grid(row = i)
         m3 = tk.Button(extract_frame,
                       text = "Mehlich 3",
                       font = ("Arial", 20),
                       command = lambda: [mw.window.clear_frame(extract_frame),
                                           procedure_selection.m3_click()]).grid(row = 7, column = 0, padx = 20, pady = 20)
         h3a = tk.Button(extract_frame,
                        text = "H3A: Haney 3 Acids",
                        font = ("Arial", 20),
                        command = lambda: [mw.window.clear_frame(extract_frame),
                                           procedure_selection.h3a_click()]).grid(row = 7, column = 2, padx = 20, pady = 20)
         olsen = tk.Button(extract_frame,
                          text = "Olsen P",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(extract_frame),
                                             procedure_selection.olsen_click()]).grid(row = 8, column = 0, padx = 20, pady = 20)
         kcl = tk.Button(extract_frame,
                        text = "KCl: Potassium Chloride",
                        font = ("Arial", 20),
                        command = lambda: [mw.window.clear_frame(extract_frame),
                                          procedure_selection.kcl_click()]).grid(row = 8, column = 2, padx = 20, pady = 20)
         piLab_home = tk.Button(extract_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(extract_frame),
                                            mw.window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)
    
    
    def m3_click():
        m3_frame = tk.Frame()
        m3_frame.pack()
        for i in range(6):
            label = tk.Label(m3_frame,
                             text = "").grid(row = i)
        stock = tk.Button(m3_frame,
                          text = "M3 Stock Solution",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(m3_frame),
                                             ex.recipes.m3_stock_click()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        m3_1L = tk.Button(m3_frame,
                          text = "M3 Solution 2.5 L",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(m3_frame),
                                             ex.recipes.m3_1L_click()]).grid(row = 7, column = 3, padx = 20, pady = 20)
        m3_2L = tk.Button(m3_frame,
                          text = "M3 Solution 5 L",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(m3_frame),
                                             ex.recipes.m3_2L_click()]).grid(row = 8, column =2, padx = 20, pady = 20)
        piLab_home = tk.Button(m3_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(m3_frame),
                                            mw.mw.window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(m3_frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(m3_frame),
                                                    procedure_selection.extracts_click()]).grid(row = 9, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def h3a_click():
        h3a_frame = tk.Frame()
        h3a_frame.pack()
        for i in range(6):
            label = tk.Label(h3a_frame,
                             text = "").grid(row = i)
        h3a_1L = tk.Button(h3a_frame,
                           text = "H3A 1 L",
                           font = ("Arial", 20),
                           command = lambda: [mw.window.clear_frame(h3a_frame),
                                              ex.recipes.h3a_1L_click()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        h3a_2L = tk.Button(h3a_frame,
                           text = "H3A 2 L",
                           font = ("Arial", 20),
                           command = lambda: [mw.window.clear_frame(h3a_frame),
                                              ex.recipes.h3a_2L_click()]).grid(row = 7, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(h3a_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(h3a_frame),
                                            mw.window.piLab_home()]).grid(row = 8, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(h3a_frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(h3a_frame),
                                                    procedure_selection.extracts_click()]).grid(row = 8, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def olsen_click():
        olsen_frame = tk.Frame()
        olsen_frame.pack()
        for i in range(6):
            label = tk.Label(olsen_frame,
                             text = "").grid(row = i)
        olsen_1L = tk.Button(olsen_frame,
                             text = "Olsen P 1 L",
                             font = ("Arial", 20),
                             command = lambda: [mw.window.clear_frame(olsen_frame),
                                                ex.recipes.olsen_1L_click()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        olsen_2L = tk.Button(olsen_frame,
                             text = "Olsen P 2 L",
                             font = ("Arial", 20),
                             command = lambda: [mw.window.clear_frame(olsen_frame),
                                                ex.recipes.olsen_2L_click()]).grid(row = 7, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(olsen_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(olsen_frame),
                                            mw.window.piLab_home()]).grid(row = 8, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(olsen_frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(olsen_frame),
                                                    procedure_selection.extracts_click()]).grid(row = 8, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_click():
        kcl_frame = tk.Frame()
        kcl_frame.pack()
        for i in range(6):
            label = tk.Label(kcl_frame,
                             text = "").grid(row = i)
        kcl_1N_1L = tk.Button(kcl_frame,
                              text = "1N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 ex.recipes.kcl_1N_1L_click()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        kcl_1N_2L = tk.Button(kcl_frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 ex.recipes.kcl_1N_2L_click()]).grid(row = 7, column =2, padx = 20, pady = 20)
        kcl_2N_1L = tk.Button(kcl_frame,
                              text = "2N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 ex.recipes.kcl_2N_1L_click()]).grid(row = 8, column =1, padx = 20, pady = 20)
        kcl_2N_2L = tk.Button(kcl_frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 ex.recipes.kcl_2N_2L_click()]).grid(row = 8, column =2, padx = 20, pady = 20)
        piLab_home = tk.Button(kcl_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(kcl_frame),
                                            mw.window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(kcl_frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(kcl_frame),
                                                    procedure_selection.extracts_click()]).grid(row = 9, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        
    def extraction_protocol():
        ex_pro_frame = tk.Frame()
        ex_pro_frame.pack()
        for i in range(6):
            label = tk.Label(ex_pro_frame,
                             text = "").grid(row = i)
        mehlich3 = tk.Button(ex_pro_frame,
                             text = "M3 Extraction",
                             font = ("Arial", 20),
                             command = lambda: [mw.window.clear_frame(ex_pro_frame),
                                                ex.extract_protocol.mehlich3_pro_click()]).grid(row = 7, column = 1,
                                                                                              padx = 20,
                                                                                              pady = 20)
        potassiumChloride = tk.Button(ex_pro_frame,
                            text = "KCl Extraction",
                            font = ("Arial", 20),
                            command = lambda: [mw.window.clear_frame(ex_pro_frame),
                                             ex.extract_protocol.potassium_chloride_click()]).grid(row = 7, column = 2,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        olsenP = tk.Button(ex_pro_frame,
                           text = "Olsen P Extraction",
                           font = ("Arial", 20),
                           command = lambda: [mw.window.clear_frame(ex_pro_frame),
                                              ex.extract_protocol.olsenP_click()]).grid(row = 7, column = 3,
                                                                                        padx = 20,
                                                                                        pady = 20)
        h3a = tk.Button(ex_pro_frame,
                        text = ("H3A Extraction"),
                        font = ("Arial", 20),
                        command = lambda: [mw.window.clear_frame(ex_pro_frame),
                                           ex.extract_protocol.h3a_click()]).grid(row = 8, column = 1,
                                                                                  padx = 20,
                                                                                  pady = 20)
        hcl = tk.Button(ex_pro_frame,
                        text = "HCl Extraction",
                        font = ("Arial", 20),
                        command = lambda: [mw.window.clear_frame(ex_pro_frame),
                                           ex.extract_protocol.hcl_click()]).grid(row = 8, column = 3,
                                                                                  padx = 20,
                                                                                  pady = 20)
        piLab_home = tk.Button(ex_pro_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(ex_pro_frame),
                                            mw.window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)
