import tkinter as tk
import window as mw
import skalar as sk
import icp as ic

class procedure_selection:

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
                                             protocols.m3_stock_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        m3_1L = tk.Button(m3_frame,
                          text = "M3 Solution 1 L",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(m3_frame),
                                             protocols.m3_1L_click(protocols.open_protocols())]).grid(row = 7, column = 3, padx = 20, pady = 20)
        m3_2L = tk.Button(m3_frame,
                          text = "M3 Solution 2 L",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(m3_frame),
                                             protocols.m3_2L_click(protocols.open_protocols())]).grid(row = 8, column =2, padx = 20, pady = 20)
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
                                              protocols.h3a_1L_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        h3a_2L = tk.Button(h3a_frame,
                           text = "H3A 2 L",
                           font = ("Arial", 20),
                           command = lambda: [mw.window.clear_frame(h3a_frame),
                                              protocols.h3a_2L_click(protocols.open_protocols())]).grid(row = 7, column = 2, padx = 20, pady = 20)
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
                                                protocols.olsen_1L_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        olsen_2L = tk.Button(olsen_frame,
                             text = "Olsen P 2 L",
                             font = ("Arial", 20),
                             command = lambda: [mw.window.clear_frame(olsen_frame),
                                                protocols.olsen_2L_click(protocols.open_protocols())]).grid(row = 7, column = 2, padx = 20, pady = 20)
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
                                                 protocols.kcl_1N_1L_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        kcl_1N_2L = tk.Button(kcl_frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 protocols.kcl_1N_2L_click(protocols.open_protocols())]).grid(row = 7, column =2, padx = 20, pady = 20)
        kcl_2N_1L = tk.Button(kcl_frame,
                              text = "2N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 protocols.kcl_2N_1L_click(protocols.open_protocols())]).grid(row = 8, column =1, padx = 20, pady = 20)
        kcl_2N_2L = tk.Button(kcl_frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: [mw.window.clear_frame(kcl_frame),
                                                 protocols.kcl_2N_2L_click(protocols.open_protocols())]).grid(row = 8, column =2, padx = 20, pady = 20)
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
        
class protocols:
    def open_protocols():
        with open(r"C:\Users\john.sorensen\Box\programming\python\pi_lab\src\protocols.txt", mode = "r") as file:
            proto = file.readlines()
            return proto

    def m3_stock_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[2:7]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def m3_1L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 11,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[8:17]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def m3_2L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[18:26]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def h3a_1L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[29:36]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def h3a_2L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[37:44]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def olsen_1L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[47:54]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def olsen_2L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[55:62]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def kcl_1N_1L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[65:70]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_1N_2L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[71:76]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_2N_1L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[77:82]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_2N_2L_click(proto):
        frame = tk.Frame()
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[83:88]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)