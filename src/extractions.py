import tkinter as tk
from src import window as mw
from src import procedure as pr
from src import instructions as ins

class recipes:

    def m3_stock_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Mehclich 3 Stock Solution Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        m3stock = ins.extractant_recipes.mehlich3Stock
        text.insert(tk.END, m3stock)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        m3_recipes_button = tk.Button(frame,
                                      text = "Mehlich 3 Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.m3_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def m3_1L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Mehlich 3 Protocol 2.5 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 11,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        m3_2 = ins.extractant_recipes.mehlich3["2.5 L"]
        text.insert(tk.END, m3_2)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        m3_recipes_button = tk.Button(frame,
                                      text = "Mehlich 3 Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.m3_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)
        
    def m3_2L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Mehlich 3 Protocol 5 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        m3_3 = ins.extractant_recipes.mehlich3["5.0 L"]
        text.insert(tk.END, m3_3)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        m3_recipes_button = tk.Button(frame,
                                      text = "Mehlich 3 Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.m3_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def h3a_1L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Haney 3 Acids Protocol 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        h3a1L = ins.extractant_recipes.H3A["1 L"]
        text.insert(tk.END, h3a1L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        h3a_recipes_button = tk.Button(frame,
                                      text = "Haney 3 Acids Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.h3a_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)
        
    def h3a_2L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Haney 3 Acids Protocol 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        h3a2L = ins.extractant_recipes.H3A["2 L"]
        text.insert(tk.END, h3a2L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        h3a_recipes_button = tk.Button(frame,
                                      text = "Haney 3 Acids Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.h3a_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def olsen_1L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Olsen P Protocol 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        olsen1L = ins.extractant_recipes.olsenP["1 L"]
        text.insert(tk.END, olsen1L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        olsen_recipes_button = tk.Button(frame,
                                      text = "Olsen P Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.olsen_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def olsen_2L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Olsen P Protocol 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        olsen2L = ins.extractant_recipes.olsenP["2 L"]
        text.insert(tk.END, olsen2L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        olsen_recipes_button = tk.Button(frame,
                                      text = "Olsen P Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.olsen_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)
        
    def kcl_1N_1L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Potassium Chloride Protocol 1N 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        kcl1N1L = ins.extractant_recipes.potassiumChloride["1 L 1 N"]
        text.insert(tk.END, kcl1N1L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame,
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.kcl_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def kcl_1N_2L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Potassium Chloride Protocol 1N 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        kcl1N2L = ins.extractant_recipes.potassiumChloride["1 L 2 N"]
        text.insert(tk.END, kcl1N2L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame,
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.kcl_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def kcl_2N_1L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Potassium Chloride Protocol 2N 1 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        kcl2N1L = ins.extractant_recipes.potassiumChloride["1 L 2 N"]
        text.insert(tk.END, kcl2N1L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame,
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.kcl_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

    def kcl_2N_2L_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Potassium Chloride Protocol 2N 2 L",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        kcl2N2L = ins.extractant_recipes.potassiumChloride["2 L 2 N"]
        text.insert(tk.END, kcl2N2L)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extract_home_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
        kcl_recipes_Button = tk.Button(frame,
                                      text = "Potassium Chloride Recipes",
                                      font = ("Arial", 20),
                                      command = lambda: mw.procedureControl.kcl_click(frame)).grid(row = 5, column = 2,
                                                                                                  padx = 20, 
                                                                                                  pady = 20)

class extract_protocol:

    def mehlich3_pro_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Mehlich 3 Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        m3_ex_pro = ins.extract_protocols.mehlich3
        text.insert(tk.END, m3_ex_pro)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.Smith_lab_home(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                 text = "Extraction Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def potassium_chloride_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Potassium Chloride Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        kcl_pro = ins.extract_protocols.potassiumChloride
        text.insert(tk.END, kcl_pro)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                 text = "Extraction Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: mw.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def olsenP_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Olsen P Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        text = tk.Text(frame,
                    height = 10,
                    width = 52,
                    font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        olsen_pro = ins.extract_protocols.olsenP
        text.insert(tk.END, olsen_pro)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                text = "Extraction Protocols",
                                font = ("Arial", 20),
                                command = lambda: mw.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 1,
                                                                                                padx = 20,
                                                                                                pady = 20)
    def h3a_click():
            frame = tk.Frame()
            frame.pack()
            main_label = tk.Label(frame,
                        text = "Haney 3 Acids Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
            for i in range(1,4):
                label = tk.Label(frame,
                                text = "").grid(row = i)
            text = tk.Text(frame,
                        height = 10,
                        width = 52,
                        font = ("Arial", 20))
            text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
            h3a = ins.extract_protocols.h3a
            text.insert(tk.END, h3a)
            smith_lab_home = tk.Button(frame,
                                    text = "Smith Lab Home",
                                    font = ("Arial", 20),
                                    command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
            extraction_protocols= tk.Button(frame,
                                    text = "Extraction Protocols",
                                    font = ("Arial", 20),
                                    command = lambda: mw.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 1,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
    def hcl_click():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                        text = "Hydrochloric Acid Extraction Protocol",
                        font = ("Arial", 25)).grid(row = 0, columnspan = 4)
        for i in range(1,4):
            label = tk.Label(frame,
                            text = "").grid(row = i)
        text = tk.Text(frame,
                    height = 10,
                    width = 52,
                    font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        hcl = ins.extract_protocols.hcl
        text.insert(tk.END, hcl)
        smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: mw.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                text = "Extraction Protocols",
                                font = ("Arial", 20),
                                command = lambda: mw.procedureControl.extraction_proto_click(frame)).grid(row = 5, column = 1,
                                                                                                padx = 20,
                                                                                                pady = 20)