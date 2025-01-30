"""
########################################################################
extractions.py defines the classes and functions for the different
frames that are related to the extractions for sample analysis in house
and are being constructed through the operation of the piLab.
########################################################################
"""
import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

class recipes:

    def m3_stock_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Mehclich 3 Stock Solution Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        m3stock = ins.extractant_recipes.mehlich3Stock
        text.insert(tk.END, m3stock)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        m3_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Mehlich 3 Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.m3_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def m3_1L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Mehlich 3 Protocol 2.5 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 11,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        m3_2 = ins.extractant_recipes.mehlich3["2.5 L"]
        text.insert(tk.END, m3_2)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        m3_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Mehlich 3 Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.m3_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)
        
    def m3_2L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Mehlich 3 Protocol 5 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        m3_3 = ins.extractant_recipes.mehlich3["5.0 L"]
        text.insert(tk.END, m3_3)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        m3_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Mehlich 3 Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.m3_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def h3a_1L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Haney 3 Acids Protocol 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        h3a1L = ins.extractant_recipes.H3A["1 L"]
        text.insert(tk.END, h3a1L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        h3a_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Haney 3 Acids Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.h3a_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)
        
    def h3a_2L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Haney 3 Acids Protocol 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        h3a2L = ins.extractant_recipes.H3A["2 L"]
        text.insert(tk.END, h3a2L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        h3a_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Haney 3 Acids Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.h3a_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def olsen_1L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Olsen P Protocol 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        olsen1L = ins.extractant_recipes.olsenP["1 L"]
        text.insert(tk.END, olsen1L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        olsen_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Olsen P Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.olsen_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def olsen_2L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Olsen P Protocol 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        olsen2L = ins.extractant_recipes.olsenP["2 L"]
        text.insert(tk.END, olsen2L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        olsen_recipes_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Olsen P Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.olsen_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)
        
    def kcl_1N_1L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Potassium Chloride Protocol 1N 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        kcl1N1L = ins.extractant_recipes.potassiumChloride["1 L 1 N"]
        text.insert(tk.END, kcl1N1L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.kcl_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def kcl_1N_2L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Potassium Chloride Protocol 1N 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        kcl1N2L = ins.extractant_recipes.potassiumChloride["1 L 2 N"]
        text.insert(tk.END, kcl1N2L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.kcl_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def kcl_2N_1L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Potassium Chloride Protocol 2N 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        kcl2N1L = ins.extractant_recipes.potassiumChloride["1 L 2 N"]
        text.insert(tk.END, kcl2N1L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.kcl_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

    def kcl_2N_2L_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Potassium Chloride Protocol 2N 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        kcl2N2L = ins.extractant_recipes.potassiumChloride["2 L 2 N"]
        text.insert(tk.END, kcl2N2L)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extract_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extract_home_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: ctrl.procedureControl.kcl_click(frame)).grid(row = 5, column = 3, rowspan = 2,
                                                                                                  padx = 8, 
                                                                                                  pady = 20)

class extract_protocol:

    def mehlich3_pro_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Mehlich 3 Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        m3_ex_pro = ins.extract_protocols.mehlich3
        text.insert(tk.END, m3_ex_pro)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extraction_protocols= tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extraction Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
    def potassium_chloride_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Potassium Chloride Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        kcl_pro = ins.extract_protocols.potassiumChloride
        text.insert(tk.END, kcl_pro)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extraction_protocols= tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Extraction Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                   padx = 8,
                                                                                                   pady = 20)
    def olsenP_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Olsen P Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                    height = 10,
                    width = 52,
                    font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        olsen_pro = ins.extract_protocols.olsenP
        text.insert(tk.END, olsen_pro)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extraction_protocols= tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Extraction Protocols",
                                font = ("Arial", 20),
                                command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                padx = 8,
                                                                                                pady = 20)
    def h3a_click():
            frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
            frame.pack()
            main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Haney 3 Acids Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
            for i in range(1,4):
                label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "").grid(row = i)
            text = tk.Text(frame, borderwidth = 0,
                        height = 10,
                        width = 52,
                        font = ("Arial", 20))
            text.configure(bg = "#055942", fg = "#67aae6")
            text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
            h3a = ins.extract_protocols.h3a
            text.insert(tk.END, h3a)
            piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
            smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Smith Lab Home",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                               padx = 8, 
                                                                                               pady = 20)
            extraction_protocols= tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Extraction Protocols",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                    padx = 8,
                                                                                                    pady = 20)
    def hcl_click():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                        text = "Smith Lab: Hydrochloric Acid Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                            text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                    height = 10,
                    width = 52,
                    font = ("Arial", 20))
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, columnspan = 2, padx = 8, pady = 35)
        hcl = ins.extract_protocols.hcl
        text.insert(tk.END, hcl)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                    padx = 8,
                                                                                    pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, 
                                                                                           padx = 8, 
                                                                                           pady = 20)
        extraction_protocols= tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Extraction Protocols",
                                font = ("Arial", 20),
                                command = lambda: ctrl.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 2, rowspan = 2,
                                                                                                padx = 8,
                                                                                                pady = 20)