"""
########################################################################
icp.py defines the classes and functions for the different
frames that are related to Agilent 5110 ICP-OES and are being 
constructed through the operation of the piLab.
########################################################################
"""

import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

class icp_cookbook:
    def icp_home_frame():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab: ICP-OES Standard Recipes",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        std4_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 4 Elements and Concentrations",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std4_click(frame)).grid(row = 1, column = 0, padx = 50, pady = 50)
        std3_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 3 Protocol",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std3_click(frame)).grid(row = 1, column = 1, 
                                                                                                padx = 50, 
                                                                                                pady = 50)
        std2_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 2 protocol",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std2_click(frame)).grid(row = 2, column = 0, 
                                                                                                padx = 50, 
                                                                                                pady =50)
        std1_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 1 Protocol",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std1_click(frame)).grid(row = 2, column = 1, 
                                                                                                padx = 50, 
                                                                                                pady = 50)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 3, column = 0,
                                                                                           padx = 20,
                                                                                           pady =20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 4, column = 0, 
                                                                                    padx = 20, 
                                                                                    pady = 20)
        instrument_recipies = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                   text = "Instrument Recipes",
                                   font = ("Arial", 20),
                                   command = lambda: ctrl.window.instruments_click(frame)).grid(row = 3, column = 1,
                                                                                                rowspan = 2,
                                                                                                padx = 20, 
                                                                                                pady = 20)

    def icp_element_frame():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab: ICP-OES Standard Element Selection",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4,
                                                         padx = 20,
                                                         pady = 20)
        Al_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                    text = "Aluminium",
                                    font = ("Arial", 20),
                                    command = lambda: ctrl.icpWindowControl.al_click(frame)).grid(row = 1, column = 0,
                                                            padx = 50, pady = 40)
        Ca_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Calcium",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.ca_click(frame)).grid(row = 1,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 40)
        Cu_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Copper",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.cu_click(frame)).grid(row = 1,
                                                                                    column = 2,
                                                                                    padx = 50,
                                                                                    pady = 40)
        Fe_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Iron",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.fe_click(frame)).grid(row = 1,
                                                                                    column = 3,
                                                                                    padx = 50,
                                                                                    pady =40)
        K_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Potassium",
                                font = ("Arial", 20),
                                command = lambda:ctrl.icpWindowControl.k_click(frame)).grid(row = 2,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 40)
        Mg_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Magnesium",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.mg_click(frame)).grid(row = 2,
                                                                                        column = 2,
                                                                                        padx = 50,
                                                                                        pady = 40)
        Mn_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Manganese",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.mn_click(frame)).grid(row = 2,
                                                                                        column = 3,
                                                                                        padx = 50,
                                                                                        pady = 40)
        Na_Button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Sodium",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.na_click(frame)).grid(row = 3,
                                                                                    column = 0,
                                                                                    padx = 50,
                                                                                    pady = 40)
        P_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Phosphorus",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.p_click(frame)).grid(row = 3,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 40)
        S_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Sulfur",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.s_click(frame)).grid(row = 3,
                                                                                    column = 2,
                                                                                    padx = 50,
                                                                                    pady = 40)
        Zn_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Zinc",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.zn_click(frame)).grid(row = 3,
                                                                                    column = 3,
                                                                                    padx = 50,
                                                                                    pady = 40)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 4, column = 0,
                                                                                           padx = 50,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 5, column = 0, 
                                                                                    padx = 20, 
                                                                                    pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 4, column = 3, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)

class icp_control:
    def std_3_proto():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab: ICP Standard 3 Protocol",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 6,
                       width = 48,
                       font = ("Arial", 20),
                       bd = 5,
                       relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, padx = 20, pady =20)
        std3 = ins.icp_recipes.icpSTD["STD 3"]
        text.insert(tk.END, std3)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 8, column = 2, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 2",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std2_click(frame)).grid(row = 4, column = 2,
                                                                                        padx = 20,
                                                                                        pady = 20)

    def std_2_proto():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab: ICP Standard 2 Protocol",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 6,
                       width = 48,
                       font = ("Arial", 20),
                       bd = 5,
                       relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, padx = 20, pady =20)
        std2 = ins.icp_recipes.icpSTD["STD 2"]
        text.insert(tk.END, std2)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 8, column = 2, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 3",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std3_click(frame)).grid(row = 4, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 1",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std1_click(frame)).grid(row = 4, column = 2,
                                                                                        padx = 20,
                                                                                        pady = 20)

    def std_1_proto():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab: ICP Standard 1 Protocol",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        text = tk.Text(frame, borderwidth = 0,
                       height = 6,
                       width = 48,
                       font = ("Arial", 20),
                       bd = 5,
                       relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 1, padx = 20, pady =20)
        std1 = ins.icp_recipes.icpSTD["STD 1"]
        text.insert(tk.END, std1)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 8, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 9, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 8, column = 2, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Standard 2",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.std2_click(frame)).grid(row = 4, column = 0,
                                                                                        padx = 20,
                                                                                        pady = 20)

    def stock_solutions(element):
        element = element
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        choose_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                                text = "Choose " + element + " Stock Standard",
                                font = ("Arial", 25)).grid(row = 0, column =0, columnspan = 5)
        ppm_1000 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             font = ("Arial", 20),
                             text = "1,000 ppm " + element,
                             command = lambda: [ctrl.window.clear_frame(frame),
                                                icp_control.desired_conc(1000, element)]).grid(row = 1,
                                                                              column = 1,
                                                                              pady = 50)
        ppm_10000 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             font = ("Arial", 20),
                             text = "10,000 ppm " + element,
                             command = lambda: [ctrl.window.clear_frame(frame),
                                                icp_control.desired_conc(10000, element),]).grid(row = 2,
                                                                              column = 1,
                                                                              pady = 50)
        for i in range(2, 5):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 5, column = 2, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)

    def desired_conc(stock_conc, element):
        element = element
        stock_conc = stock_conc
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        concentrations = []
        conc_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Select the desired concentration For Standard 4",
                              font = ("Arial", 20)).grid(row = 0, column = 0, columnspan = 4)
        conc_6 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                           text = "10.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(10.0),
                                              text.insert(tk.END, "10.0 ppm" + "\n")]).grid(row = 2, column = 0,
                                                                                            
                                                                                            padx = 10, pady = 20)
        conc_7 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                           text = "20.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(20.0),
                                              text.insert(tk.END, "20.0 ppm" + "\n")]).grid(row = 2, column = 2,
                                                                                            
                                                                                            padx = 10, pady = 20)
        conc_9 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                           text = "40.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(40.0),
                                              text.insert(tk.END, "40.0 ppm" + "\n")]).grid(row = 2, column = 3,
                                                                                            
                                                                                            padx = 10, pady = 20)

        conc_11 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                           text = "100.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(100.0),
                                              text.insert(tk.END, "100.0 ppm" + "\n")]).grid(row = 3, column = 0,
                                                                                             
                                                                                             padx = 10, pady = 20)
        conc_14 = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                           text = "800.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(800.0),
                                              text.insert(tk.END, "800.0 ppm" + "\n")]).grid(row = 3, column = 3,
                                                                                             
                                                                                             padx = 10, pady = 20)
        # blank_1 = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
        #                     text = "",
        #                     font = ("Arial", 15)).grid(row = 2, column = 1, padx = 25, pady = 20)
        # blank_2 = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
        #                     text = "",
        #                     font = ("Arial", 15)).grid(row = 2, column = 3, padx = 25, pady = 20)
        # blank_3 = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
        #                     text = "",
        #                     font = ("Arial", 15)).grid(row = 3, column = 1, padx = 25, pady = 20)
        # blank_4 = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
        #                     text = "",
        #                     font = ("Arial", 15)).grid(row = 3, column = 2, padx = 25, pady = 20)
        # blank_5 = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
        #                     text = "",
        #                     font = ("Arial", 15)).grid(row = 3, column = 3, padx = 25, pady = 20)
        text = tk.Text(frame, borderwidth = 0,
                       height = 5,
                       width = 40,
                       font = ("Arial", 20),
                       bd = 5,
                       relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 4, column = 0, columnspan = 4, padx = 25, pady = 15)

        clear_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                 text = "Clear Selection",
                                 font = ("Arial", 20),
                                 command = lambda: [concentrations.clear(),
                                                    text.delete("1.0", "end")]).grid(row = 5,
                                                                             column =2,
                                                                             rowspan = 2,
                                                                             padx = 20,
                                                                             pady = 10)
        conc_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Accept STD concentrations:",
                                font = ("Arial", 20),
                                command = lambda: [ctrl.window.clear_frame(frame),
                                                   icp_control.std_instructions(icp_math.calculate_conc(stock_conc, concentrations), element)]).grid(row =5,
                                                                                         column = 3,
                                                                                         rowspan = 2,
                                                                                         padx = 20,
                                                                                         pady = 10)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 5, column = 1, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)

    def std_instructions(concentrations, element):
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab: ICP Standard 4 Protocol",
                              font = ("Arial", 25)).grid(row = 0, column = 1,
                                                         padx = 20,
                                                         pady = 20)
        text = tk.Text(frame, borderwidth = 0,
                           height = 7,
                           width = 38,
                           font = ("Arial", 30),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 1, column = 1, padx = 20, pady = 20)
        for std in concentrations:
            text.insert(tk.END, str(std) + " uL " + " or " + str(std / 1000) + ' mL ' + "of " + element + "\n" + "to the 100 mL volumetric flask")
        for i in range(2, 5):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                               text = "piLab Home",
                               font = ("Arial", 20),
                               command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 5, column = 0,
                                                                                           padx = 20,
                                                                                           pady = 20)
        smith_lab_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 6, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                             text = "ICP Recipes",
                             font = ("Arial", 20),
                             command = lambda: ctrl.icpWindowControl.icp_home(frame)).grid(row = 5, column = 1, 
                                                                                           rowspan = 2,
                                                                                           padx = 20, 
                                                                                           pady = 20)

class icp_math:
    def calculate_conc(stock_concentrations, final_concentrations):
        stock = stock_concentrations
        final = final_concentrations
        std_lst = []
        for i in range(len(final_concentrations)):
            std = (final[i] * 100) / stock * 1000
            std_lst.append(std)
        return std_lst
    
class icp_step_window():
    def steps():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Steps",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        step1_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step1(frame)).grid(row = 4, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step2(frame)).grid(row = 4, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step3(frame)).grid(row = 4, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step4(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step5_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 5",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step5(frame)).grid(row = 5, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step6_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 6",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step6(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step7_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 7",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step7(frame)).grid(row = 6, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step8_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 8",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step8(frame)).grid(row = 6, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step9_click = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                text = "Step 9",
                                font = ("Arial", 20),
                                command = lambda: ctrl.icpWindowControl.icp_step9(frame)).grid(row = 6, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        for i in range(7, 10):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 10, column = 0,
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
                                         text = "Instrumentation SOPs",
                                         command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 10, 
                                                                                                                  column = 2,
                                                                                                                  rowspan = 2,
                                                                                                                  padx = 20,
                                                                                                                  pady = 20)

class icp_operation:
    def step1():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 1",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step1
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.icpWindowControl.icp_step2(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    

    def step2():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 2",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step2
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: ctrl.icpWindowControl.icp_step1(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: ctrl.icpWindowControl.icp_step3(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)

    def step3():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 3",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step3
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: ctrl.icpWindowControl.icp_step2(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: ctrl.icpWindowControl.icp_step4(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step4():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 4",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step4
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: ctrl.icpWindowControl.icp_step3(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: ctrl.icpWindowControl.icp_step5(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step5():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 5",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                        height = 10,
                        width = 48,
                        font = ("Arial", 20),
                        bd = 5,
                        relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step5
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: ctrl.icpWindowControl.icp_step4(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: ctrl.icpWindowControl.icp_step6(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step6():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 6",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step6
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: ctrl.icpWindowControl.icp_step5(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 7",
                                command = lambda: ctrl.icpWindowControl.icp_step7(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step7():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 7",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step7
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: ctrl.icpWindowControl.icp_step6(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 8",
                                command = lambda: ctrl.icpWindowControl.icp_step8(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step8():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 8",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step8
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 7",
                                command = lambda: ctrl.icpWindowControl.icp_step7(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 9",
                                command = lambda: ctrl.icpWindowControl.icp_step9(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step9():
        frame = tk.Frame(bg = "#055942", width = 1280, height = 800)
        frame.pack()
        main_label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                              text = "Smith Lab ICP-OES SOP: Step 9",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1, 4):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        icp_op = ins.icp_operation
        text = tk.Text(frame, borderwidth = 0,
                           height = 10,
                           width = 48,
                           font = ("Arial", 20),
                           bd = 5,
                           relief = "sunken")
        text.configure(bg = "#055942", fg = "#67aae6")
        text.grid(row = 5, column = 1)
        step = icp_op.step9
        text.insert(tk.END, step)
        for i in range(6, 8):
            label = tk.label = tk.Label(frame, bg = "#055942", fg = "#67aae6",
                             text = "").grid(row = i)
        piLab_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "piLab Home",
                                      command = lambda: ctrl.window.piLab_home_click(frame)).grid(row = 9, column = 0,
                                                                                                  padx = 20,
                                                                                                  pady = 20)
        smith_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 10, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        instructions_home = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                      font = ("Arial", 20),
                                      text = "Instrumentation SOPs",
                                      command = lambda: ctrl.window.analytical_instrumentation_click(frame)).grid(row = 9, column = 1,
                                                                                                    rowspan = 2,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
        step_home_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                     font = ("Arial", 20),
                                     text = "ICP SOP Steps",
                                     command = lambda: ctrl.icpWindowControl.icp_step_home(frame)).grid(row = 9, column = 2,
                                                                                      rowspan = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame, bg = "#453f3f", fg = "#67aae6", bd = 5, relief = "raised",
                                font = ("Arial", 20),
                                text = "Step 8",
                                command = lambda: ctrl.icpWindowControl.icp_step8(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)