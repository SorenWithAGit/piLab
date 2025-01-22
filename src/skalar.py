import tkinter as tk
from src import control as cl
from src import instructions as ins

class skalar_cookbook:
    def home_frame():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar Recipies Home",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1, 6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        channel = tk.Label(frame,
                              text = "Select Channel",
                              font = ("Arial", 20)).grid(row = 6, columnspan = 3, padx = 20, pady = 20)
        nitr_button = tk.Button(frame,
                                text = "Nitrate/Nitrite Channel",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.nitr_click(frame)).grid(row = 7, column = 0, padx = 20, pady = 20)
        phos_button = tk.Button(frame,
                                text = "Phosphate Channel",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.phos_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        ammo_button = tk.Button(frame,
                                text = "Ammonium Channel",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.ammo_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 20)
        rins_button = tk.Button(frame,
                                text = "Rinsing Liquid",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.rins_click(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)
        stds_button = tk.Button(frame,
                                text = "Calibration Standards",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.cal_stds_click(frame)).grid(row = 8, column = 2, padx = 20, pady = 20)
        smith_lab_home = tk.Button(frame,
                         text = "Smith Lab Home",
                         font = ("Arial", 20),
                         command = lambda: cl.window.smith_lab_click(frame)).grid(row = 9, column = 0, padx = 20, pady = 20)
        instrument_recipies = tk.Button(frame,
                                   text = "Instrument Recipes",
                                   font = ("Arial", 20),
                                   command = lambda: cl.window.instruments_click(frame)).grid(row = 9, column = 2, padx = 20, pady = 20)

    def nitrate_frame():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar: Nitrate/Nitrite Reagents",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)

        nitr_buffer = tk.Button(frame,
                                text = "Nitrate/Nitrite Buffer",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.nitr_buff_click(frame)).grid(row = 6, column = 1, padx = 20, pady = 20)
        color_reag = tk.Button(frame,
                               text = "Color Reagent",
                               font = ("Arial", 20),
                               command = lambda: cl.skalarWindowControl.color_click(frame)).grid(row = 6, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 7, column =0, padx = 20, pady = 20)

    def phosphate_frame():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar: Phosphate Reagents",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        ffd6_button = tk.Button(frame,
                                text = "FFD6 Solution",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.ffd6_click(frame)).grid(row = 6, column = 1, padx = 20, pady = 20)
        sulf_button = tk.Button(frame,
                                text = "Sulfuric Acid Solution",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sulf_click(frame)).grid(row = 6, column = 2, padx = 20, pady = 20)
        hept_button = tk.Button(frame,
                                text = "Ammonium Heptamolybdate",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.hept_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        lplus_button = tk.Button(frame,
                                 text = "L+ Ascorbic Acid",
                                 font = ("Arial", 20),
                                 command = lambda: cl.skalarWindowControl.lplus_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)

    def ammonium_frame():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar: Ammonium Reagents",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        ammo_buffer = tk.Button(frame,
                                text = "Ammonium Buffer",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.ammo_buff_click(frame)).grid(row = 6, column = 1, padx = 20, pady = 20)
        sali_button = tk.Button(frame,
                                  text = "Sodium Salicyalite Solution",
                                  font = ("Arial", 20),
                                  command = lambda: cl.skalarWindowControl.sali_click(frame)).grid(row = 6, column = 2, padx = 20, pady = 20)
        nitro_button = tk.Button(frame,
                                 text = "Nitroprusside Solution",
                                 font = ("Arial", 20),
                                 command = lambda: cl.skalarWindowControl.nitro_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 20)
        dichlo_button = tk.Button(frame,
                                  text = "Dichlorocyanurite Solution",
                                  font = ("Arial", 20),
                                  command = lambda: cl.skalarWindowControl.dichlor_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)
    def standards_frame():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar: Standards Recipes",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = 1)
        std1 = tk.Button(frame,
                         font = ("Arial", 20),
                         text = "Standard 1",
                         command = lambda: cl.skalarWindowControl.std1_click(frame)).grid(row = 6, column = 0, padx = 20, pady = 40)
        std2 = tk.Button(frame,
                         text = "Standard 2",
                         font = ("Arial", 20),
                         command = lambda: cl.skalarWindowControl.std2_click(frame)).grid(row = 6, column = 1, padx = 20, pady = 40)
        std3 = tk.Button(frame,
                         text = "Standard 3",
                         font = ("Arial", 20),
                         command = lambda: cl.skalarWindowControl.std3_click(frame)).grid(row = 6, column = 2, padx = 20, pady = 40)
        std4 = tk.Button(frame,
                         text = "Standard 4",
                         font = ("Arial", 20),
                         command = lambda: cl.skalarWindowControl.std4_click(frame)).grid(row = 7, column = 1, padx = 20, pady = 40)
        std5 = tk.Button(frame,
                         text = "Standard 5",
                         font = ("Arial", 20),
                         command = lambda: cl.skalarWindowControl.std5_click(frame)).grid(row = 7, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)

    def buffer_volume_frame(reagent):
        reagent = reagent
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = ("Skalar: " + str(reagent).replace("_", " ") + " Volume Frame"),
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        vol_1 = tk.Button(frame,
                          text = "500 mL",
                          font = ("Arial", 20),
                          command = lambda: cl.skalarWindowControl.buff_vol1_click(frame, reagent)).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(frame,
                          text = "1,000 mL",
                          font = ("Arial", 20),
                          command = lambda: cl.skalarWindowControl.buff_vol2_click(frame, reagent)).grid( row = 6, column = 2, padx = 20, pady = 40)
        vol_3 = tk.Button(frame,
                          text = "2,000 mL",
                          font = ("Arial", 20),
                          command = lambda: cl.skalarWindowControl.buff_vol3_click(frame, reagent)).grid(row = 7, column = 1, padx = 20, pady = 40)

        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)

    def volume_frame(reagent):
        reagent = reagent
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = ("Skalar: " + str(reagent).replace("_", " ") + " Volume Frame"),
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,6):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        vol_1 = tk.Button(frame,
                          text = "500 mL",
                          font = ("Arial", 20),
                          command = lambda: cl.skalarWindowControl.reag_vol1_click(frame, reagent)).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(frame,
                          text = "1,000 mL",
                          font = ("Arial", 20),
                          command = lambda: cl.skalarWindowControl.reag_vol2_click(frame, reagent)).grid( row = 6, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 8, column = 0, padx = 20, pady = 20)

    def instruct_frame(label, recipe):
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = str(label),
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1,4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 48,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.skalar_home(frame)).grid(row = 5, column = 0, padx = 20, pady = 20)
class skalar_recipes:
    def get_recipe(reagent, volume):
        nitrb = ins.skalar_recipes.nitrateNitriteBuffer
        nitrc = ins.skalar_recipes.nitrateNitriteColor
        ffd6 = ins.skalar_recipes.phosphateFFD6
        sulf = ins.skalar_recipes.phosphateSulfuric
        hept = ins.skalar_recipes.phosphateAmmoniumHeptamolybdate
        lplus = ins.skalar_recipes.phosphateLAscorbicAcid
        ammob = ins.skalar_recipes.ammoniaBuffer
        sali = ins.skalar_recipes.ammoniaSalicyalite
        nitr = ins.skalar_recipes.ammoniaNitroprusside
        dich = ins.skalar_recipes.ammoniaDichlorocyanurite
        rins = ins.skalar_recipes.rinsingLiquid
        skastd = ins.skalar_recipes.skalarSTD
        if reagent == "nitrate_buffer" and volume == 500:
            label = "Nitrate/Nitrite: Buffer 500 mL"
            recipe = nitrb["500 mL"]
            return [label, recipe]
        if reagent == "nitrate_buffer" and volume == 1000:
            label = "Nitrate/Nitrite: Buffer 1 L"
            recipe = nitrb["1 L"]
            return [label, recipe]
        if reagent == "nitrate_buffer" and volume == 2000:
            label = "Nitrate/Nitrite: Buffer 2 L"
            recipe = nitrb["2 L"]
            return [label, recipe]
        if reagent == "color_reagent" and volume == 500:
            label = "Nitrate/Nitrite: Color Reagent 500 mL"
            recipe = nitrc["500 mL"]
            return [label, recipe]
        if reagent == "color_reagent" and volume == 1000:
            label = "Nitrate/Nitrite: Color Reagent 1 L"
            recipe = nitrc["1 L"]
            return [label, recipe]
        if reagent == "ffd6" and volume == 500:
            label = "Phosphate: FFD6 500 mL"
            recipe = ffd6["500 mL"]
            return [label, recipe]
        if reagent == "ffd6" and volume == 1000:
            label = "Phosphate: FFD6 1 L"
            recipe = ffd6["1 L"]
            return [label, recipe]
        if reagent == "sulfuric_acid" and volume == 500:
            label = "Phosphate: Sulfuric Acid 500 mL"
            recipe = sulf["500 mL"]
            return [label, recipe]
        if reagent == "sulfuric_acid" and volume == 1000:
            label = "Phosphate: Sulfuric Acid 1 L"
            recipe = sulf["1 L"]
            return [label, recipe]
        if reagent == "ammonium_heptamolybdate" and volume == 500:
            label = "Phosphate: Ammonium Heptamolybdate 500 mL"
            recipe = hept["500 mL"]
            return [label, recipe]
        if reagent == "ammonium_heptamolybdate" and volume == 1000:
            label = "Phosphate: Ammonium HeptaMolybdate 1 L"
            recipe = hept["1 L"]
            return [label, recipe]
        if reagent == "l_plus_ascorbic" and volume == 500:
            label = "Phosphate: L+ Ascorbic Acid 500 mL"
            recipe = lplus["500 mL"]
            return [label, recipe]
        if reagent == "l_plus_ascorbic" and volume == 1000:
            label = "Phosphate: L+ Ascorbic acid 1 L"
            recipe = lplus["1 L"]
            return [label, recipe]
        if reagent == "ammonium_buffer" and volume == 500:
            label = "Ammonium: Buffer 500 mL"
            recipe = ammob["500 mL"]
            return [label, recipe]
        if reagent == "ammonium_buffer" and volume == 1000:
            label = "Ammonium: Buffer 1 L"
            recipe = ammob["1 L"]
            return [label, recipe]
        if reagent == "ammonium_buffer" and volume == 2000:
            label = "Ammonium: Buffer 2 L"
            recipe = ammob["2 L"]
            return [label, recipe]
        if reagent == "salicyalite" and volume == 500:
            label = "Ammonium: Salicyalite 500 mL"
            recipe = sali["500 mL"]
            return [label, recipe]
        if reagent == "salicyalite" and volume == 1000:
            label = "Ammonium: Salicyalite 1 L"
            recipe = sali["1 L"]
            return [label, recipe]
        if reagent == "nitroprusside" and volume == 500:
            label = "Ammonium: Nitroprusside 500 mL"
            recipe = nitr["500 mL"]
            return [label, recipe]
        if reagent == "nitroprusside" and volume == 1000:
            label = "Ammonium: Nitroprusside 1 L"
            recipe = nitr["1 L"]
            return [label, recipe]
        if reagent == "dichlorocyanurite" and volume == 500:
            label = "Ammonium: Dichlorocyanurite 500 mL"
            recipe = dich["500 mL"]
            return [label, recipe]
        if reagent == "dichlorocyanurite" and volume == 1000:
            label = "Ammonium Dichlorocyanurite 1 L"
            recipe = dich["1 L"]
            return [label, recipe]
        if reagent == "rinsing" and volume == 500:
            label = "Rinsing Liquid 500 mL"
            recipe = rins["500 mL"]
            return [label, recipe]
        if reagent == "rinsing" and volume == 1000:
            label = "Rinsing Liquid 1 L"
            recipe = rins["1 L"]
            return [label, recipe]
        if reagent == "rinsing" and volume == 2000:
            label = "Rinsing Liquid 2 L"
            recipe = rins["2 L"]
            return [label, recipe]
        if reagent == "std1":
            label = "Standard 1: 0.25 ppm"
            recipe = skastd["STD 1"]
            return [label, recipe]
        if reagent == "std2":
            label = "Standard 2: 0.75 ppm"
            recipe = skastd["STD 2"]
            return [label, recipe]
        if reagent == "std3":
            label = "Standard 3: 1.0 ppm"
            recipe = skastd["STD 3"]
            return [label, recipe]
        if reagent == "std4":
            label = "Standard 4: 2.0 ppm"
            recipe = skastd["STD 4"]
            return [label, recipe]
        if reagent == "std5":
            label = "Standard 5: 4.0 ppm"
            recipe = skastd["STD 5"]
            return [label, recipe]
        
class skalar_window:
    def steps():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar: SOP Steps",
                              font = ("Arial", 25)).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        step1_click = tk.Button(frame,
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step1(frame)).grid(row = 4, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(frame,
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step2(frame)).grid(row = 4, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(frame,
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step3(frame)).grid(row = 4, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(frame,
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step4(frame)).grid(row = 5, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step5_click = tk.Button(frame,
                                text = "Step 5",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step5(frame)).grid(row = 5, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step6_click = tk.Button(frame,
                                text = "Step 6",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step6(frame)).grid(row = 5, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step7_click = tk.Button(frame,
                                text = "Step 7",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step7(frame)).grid(row = 6, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step8_click = tk.Button(frame,
                                text = "Step 8",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step8(frame)).grid(row = 6, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step9_click = tk.Button(frame,
                                text = "Step 9",
                                font = ("Arial", 20),
                                command = lambda: cl.skalarWindowControl.sop_step9(frame)).grid(row = 6, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        for i in range(7, 10):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        smtih_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: cl.window.smith_lab_click(frame)).grid(row = 10,
                                                                        column = 0,
                                                                        pady = 20)
        instrumentation_home = tk.Button(frame,
                                         font = ("Arial", 20),
                                         text = "Instrumentation Home",
                                         command = lambda: cl.window.analytical_instrumentation_click(frame)).grid(row = 10, 
                                                                                                                  column = 2)
        
class operating_procedure:
    def step1():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 1",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        skal_op = ins.skalar_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step1
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: cl.skalarWindowControl.sop_step2(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
    

    def step2():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 2",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        skal_op = ins.skalar_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step2
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: cl.skalarWindowControl.sop_step1(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: cl.skalarWindowControl.sop_step3(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)

    def step3():
        frame = tk.Frame()
        frame.pack()
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 3",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        skal_op = ins.skalar_operation
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step3
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: cl.skalarWindowControl.sop_step2(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: cl.skalarWindowControl.sop_step4(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step4():
        frame = tk.Frame()
        frame.pack()
        skal_op = ins.skalar_operation
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 4",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step4
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: cl.skalarWindowControl.sop_step3(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: cl.skalarWindowControl.sop_step5(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step5():
        frame = tk.Frame()
        frame.pack()
        skal_op = ins.skalar_operation
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 5",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step5
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        step_home_button = tk.Button(frame,
                                    font = ("Arial", 20),
                                    text = "Skalar Step Home",
                                    command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: cl.skalarWindowControl.sop_step4(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: cl.skalarWindowControl.sop_step6(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step6():
        frame = tk.Frame()
        frame.pack()
        skal_op = ins.skalar_operation
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 6",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step6
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: cl.skalarWindowControl.sop_step5(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 7",
                                command = lambda: cl.skalarWindowControl.sop_step7(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step7():
        frame = tk.Frame()
        frame.pack()
        skal_op = ins.skalar_operation
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 7",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step7
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: cl.skalarWindowControl.sop_step6(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 8",
                                command = lambda: cl.skalarWindowControl.sop_step8(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step8():
        frame = tk.Frame()
        frame.pack()
        skal_op = ins.skalar_operation
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 8",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step8
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 7",
                                command = lambda: cl.skalarWindowControl.sop_step7(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 9",
                                command = lambda: cl.skalarWindowControl.sop_step9(frame)).grid(row = 7, column = 3,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step9():
        frame = tk.Frame()
        frame.pack()
        skal_op = ins.skalar_operation
        main_label = tk.Label(frame,
                              text = "Skalar SOP: Step 9",
                              font = ("Arial", 25),).grid(row = 0, columnspan = 3)
        for i in range(1, 4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 5, column = 2)
        step = skal_op.step9
        text.insert(tk.END, step)

        smith_home_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: cl.window.smith_lab_click(frame)).grid(row = 6, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: cl.skalarWindowControl.step_home(frame)).grid(row = 6, column = 3,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(frame,
                                font = ("Arial", 20),
                                text = "Step 8",
                                command = lambda: cl.skalarWindowControl.sop_step8(frame)).grid(row = 7, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)