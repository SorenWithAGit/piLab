import tkinter as tk
import window as mw
import procedure as pr
import instructions as ins

class recipes:

    def m3_stock_click():
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
        m3stock = ins.extractant_recipes.mehlich3Stock
        text.insert(tk.END, m3stock)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def m3_1L_click():
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
        m3_2 = ins.extractant_recipes.mehlich3["2.5 L"]
        text.insert(tk.END, m3_2)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def m3_2L_click():
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
        m3_3 = ins.extractant_recipes.mehlich3["5.0 L"]
        text.insert(tk.END, m3_3)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def h3a_1L_click():
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
        h3a1L = ins.extractant_recipes.H3A["1 L"]
        text.insert(tk.END, h3a1L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def h3a_2L_click():
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
        h3a2L = ins.extractant_recipes.H3A["2 L"]
        text.insert(tk.END, h3a2L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def olsen_1L_click():
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
        olsen1L = ins.extractant_recipes.olsenP["1 L"]
        text.insert(tk.END, olsen1L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def olsen_2L_click():
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
        olsen2L = ins.extractant_recipes.olsenP["2 L"]
        text.insert(tk.END, olsen2L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def kcl_1N_1L_click():
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
        kcl1N1L = ins.extractant_recipes.potassiumChloride["1 L 1 N"]
        text.insert(tk.END, kcl1N1L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_1N_2L_click():
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
        kcl1N2L = ins.extractant_recipes.potassiumChloride["1 L 2 N"]
        text.insert(tk.END, kcl1N2L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_2N_1L_click():
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
        kcl2N1L = ins.extractant_recipes.potassiumChloride["1 L 2 N"]
        text.insert(tk.END, kcl2N1L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

    def kcl_2N_2L_click():
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
        kcl2N2L = ins.extractant_recipes.potassiumChloride["2 L 2 N"]
        text.insert(tk.END, kcl2N2L)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extract_home = tk.Button(frame,
                                 text = "Extractants",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extracts_click()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)

class extract_protocol:

    def mehlich3_pro_click():
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
        m3_ex_pro = ins.extract_protocols.mehlich3
        text.insert(tk.END, m3_ex_pro)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                 text = "Extraction Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extraction_protocol()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def potassium_chloride_click():
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
        kcl_pro = ins.extract_protocols.potassiumChloride
        text.insert(tk.END, kcl_pro)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                   mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                 text = "Extraction Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extraction_protocol()]).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
    def olsenP_click():
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
        olsen_pro = ins.extract_protocols.olsenP
        text.insert(tk.END, olsen_pro)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                text = "Extraction Protocols",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extraction_protocol()]).grid(row = 5, column = 1,
                                                                                                padx = 20,
                                                                                                pady = 20)
    def h3a_click():
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
            h3a = ins.extract_protocols.h3a
            text.insert(tk.END, h3a)
            home_button = tk.Button(frame,
                                    text = "piLab Home",
                                    font = ("Arial", 18),
                                    command = lambda: [mw.window.clear_frame(frame),
                                                    mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
            extraction_protocols= tk.Button(frame,
                                    text = "Extraction Protocols",
                                    font = ("Arial", 20),
                                    command = lambda: [mw.window.clear_frame(frame),
                                                        pr.procedure_selection.extraction_protocol()]).grid(row = 5, column = 1,
                                                                                                    padx = 20,
                                                                                                    pady = 20)
    def hcl_click():
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
        hcl = ins.extract_protocols.hcl
        text.insert(tk.END, hcl)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [mw.window.clear_frame(frame),
                                                mw.window.Smith_lab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
        extraction_protocols= tk.Button(frame,
                                text = "Extraction Protocols",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(frame),
                                                    pr.procedure_selection.extraction_protocol()]).grid(row = 5, column = 1,
                                                                                                padx = 20,
                                                                                                pady = 20)