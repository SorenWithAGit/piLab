import tkinter as tk
from src.smithLab import control as ctrl
from src.smithLab import instructions as ins

def microwave_frame():
    frame = tk.Frame()
    frame.pack()
    main_label = tk.Label(frame,
                          text = "Microwave Digestor Protocols",
                          font = ("Arial", 25)).grid(row = 0, columnspan = 3)
    for i in range(1,4):
            label = tk.Label(frame,
                                text = "").grid(row = i)
    wq_digest = tk.Button(frame,
                            text = "Water Quality Total P",
                            font = ("Arial", 20),
                            command = lambda: ctrl.microwaveDigest.totalP(frame)).grid(row = 4, column = 0,
                                                                        padx = 20,
                                                                        pady = 20)
    
def totalP_frame():
    frame = tk.Frame()
    frame.pack()
    main_label = tk.Label(frame,
                          text = "Microwave Digestor Total P Water Digest",
                          font = ("Arial", 25)).grid(row = 0, columnspan = 3)
    for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
    text = tk.Text(frame,
                       height = 10,
                       width = 52,
                       font = ("Arial", 20))
    text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
    totalP_digestion = ins.microwaveDigestor.MDprotocols["WQ Total P"]
    text.insert(tk.END, totalP_digestion)
    smith_lab_home = tk.Button(frame,
                                text = "Smith Lab Home",
                                font = ("Arial", 20),
                                command = lambda: ctrl.window.smith_lab_click(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
    mdHome = tk.Button(frame,
                                 text = "Microwave Digestor Protocols",
                                 font = ("Arial", 20),
                                 command = lambda: ctrl.microwaveDigest.digestHome(frame)).grid(row = 5, column = 1,
                                                                                                   padx = 20,
                                                                                                   pady = 20)
