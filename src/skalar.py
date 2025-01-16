import tkinter as tk
from src import window as mw
from src import instructions as ins

class skalar_cookbook:
    def home_frame():
        home = tk.Frame()
        home.pack()
        for i in range(6):
            label = tk.Label(home,
                             text = "").grid(row = i)
        channel = tk.Label(home,
                              text = "Select Channel",
                              font = ("Arial", 20)).grid(row = 6, columnspan = 3, padx = 20, pady = 20)
        nitr_button = tk.Button(home,
                                text = "Nitrate/Nitrite Channel",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(home),
                                                   skalar_cookbook.nitrate_frame()]).grid(row = 7, column = 0, padx = 20, pady = 20)
        phos_button = tk.Button(home,
                                text = "Phosphate Channel",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(home),
                                                   skalar_cookbook.phosphate_frame()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        ammo_button = tk.Button(home,
                                text = "Ammonium Channel",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(home),
                                                   skalar_cookbook.ammonium_frame()]).grid(row = 7, column = 2, padx = 20, pady = 20)
        rins_button = tk.Button(home,
                                text = "Rinsing Liquid",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(home),
                                                   skalar_cookbook.volume_frame("rinsing")]).grid(row = 8, column = 0, padx = 20, pady = 20)
        stds_button = tk.Button(home,
                                text = "Calibration Standards",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(home),
                                                   skalar_cookbook.standards_frame()]).grid(row = 8, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(home,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(home),
                                            mw.window.Smith_lab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)

    def nitrate_frame():
        nitr_frame = tk.Frame()
        nitr_frame.pack()
        for i in range(6):
            label = tk.Label(nitr_frame,
                             text = "").grid(row = i)

        nitr_buffer = tk.Button(nitr_frame,
                                text = "Nitrate/Nitrite Buffer",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(nitr_frame),
                                                   skalar_cookbook.buffer_volume_frame("nitrate_buffer")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        color_reag = tk.Button(nitr_frame,
                               text = "Color Reagent",
                               font = ("Arial", 20),
                               command = lambda: [mw.window.clear_frame(nitr_frame),
                                                   skalar_cookbook.volume_frame("color_reagent")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(nitr_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(nitr_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 7, column =0, padx = 20, pady = 20)

    def phosphate_frame():
        phos_frame = tk.Frame()
        phos_frame.pack()
        for i in range(6):
            label = tk.Label(phos_frame,
                             text = "").grid(row = i)
        ffd6_button = tk.Button(phos_frame,
                                text = "FFD6 Solution",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("ffd6")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        sulf_button = tk.Button(phos_frame,
                                text = "Sulfuric Acid Solution",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("sulfuric_acid")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        hept_button = tk.Button(phos_frame,
                                text = "Ammonium Heptamolybdate",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("ammonium_heptamolybdate")]).grid(row = 7, column = 1, padx = 20, pady = 20)
        lplus_button = tk.Button(phos_frame,
                                 text = "L+ Ascorbic Acid",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("l_plus_ascorbic")]).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(phos_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(phos_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def ammonium_frame():
        ammo_frame = tk.Frame()
        ammo_frame.pack()
        for i in range(6):
            label = tk.Label(ammo_frame,
                             text = "").grid(row = i)
        ammo_buffer = tk.Button(ammo_frame,
                                text = "Ammonium Buffer",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(ammo_frame),
                                                   skalar_cookbook.buffer_volume_frame("ammonium_buffer")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        sali_button = tk.Button(ammo_frame,
                                  text = "Sodium Salicyalite Solution",
                                  font = ("Arial", 20),
                                  command = lambda: [mw.window.clear_frame(ammo_frame),
                                                   skalar_cookbook.volume_frame("salicyalite")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        nitro_button = tk.Button(ammo_frame,
                                 text = "Nitroprusside Solution",
                                 font = ("Arial", 20),
                                 command = lambda: [mw.window.clear_frame(ammo_frame),
                                                   skalar_cookbook.volume_frame("nitroprusside")]).grid(row = 7, column = 1, padx = 20, pady = 20)
        dichlo_button = tk.Button(ammo_frame,
                                  text = "Dichlorocyanurite Solution",
                                  font = ("Arial", 20),
                                  command = lambda: [mw.window.clear_frame(ammo_frame),
                                                   skalar_cookbook.volume_frame("dichlorocyanurite")]).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(ammo_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(ammo_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)
    def standards_frame():
        std_frame = tk.Frame()
        std_frame.pack()
        for i in range(6):
            label = tk.Label(std_frame,
                             text = "").grid(row = 1)
        std1 = tk.Button(std_frame,
                         font = ("Arial", 20),
                         text = "Standard 1",
                         command = lambda: [mw.window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std1", 100))]).grid(row = 6, column = 0, padx = 20, pady = 40)
        std2 = tk.Button(std_frame,
                         text = "Standard 2",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std2", 100))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        std3 = tk.Button(std_frame,
                         text = "Standard 3",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std3", 100))]).grid(row = 6, column = 2, padx = 20, pady = 40)
        std4 = tk.Button(std_frame,
                         text = "Standard 4",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std4", 100))]).grid(row = 7, column = 1, padx = 20, pady = 40)
        std5 = tk.Button(std_frame,
                         text = "Standard 5",
                         font = ("Arial", 20),
                         command = lambda: [mw.window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std5", 100))]).grid(row = 7, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(std_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(std_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def buffer_volume_frame(reagent):
        reagent = reagent
        vol_frame = tk.Frame()
        vol_frame.pack()
        for i in range(6):
            label = tk.Label(vol_frame,
                             text = "").grid(row = i)
        vol_1 = tk.Button(vol_frame,
                          text = "500 mL",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 500))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(vol_frame,
                          text = "1,000 mL",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 1000))]).grid( row = 6, column = 2, padx = 20, pady = 40)
        vol_3 = tk.Button(vol_frame,
                          text = "2,000 mL",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 2000))]).grid(row = 7, column = 1, padx = 20, pady = 40)

        home_button = tk.Button(vol_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(vol_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def volume_frame(reagent):
        reagent = reagent
        vol_frame = tk.Frame()
        vol_frame.pack()
        for i in range(6):
            label = tk.Label(vol_frame,
                             text = "").grid(row = i)
        vol_1 = tk.Button(vol_frame,
                          text = "500 mL",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 500))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(vol_frame,
                          text = "1,000 mL",
                          font = ("Arial", 20),
                          command = lambda: [mw.window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 1000))]).grid( row = 6, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(vol_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(vol_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def instruct_frame(recipe):
        inst_frame = tk.Frame()
        inst_frame.pack()
        for i in range(4):
            label = tk.Label(inst_frame,
                             text = "").grid(row = i)
        text = tk.Text(inst_frame,
                       height = 10,
                       width = 48,
                       font = ("Arial", 20))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(inst_frame,
                                text = "Skalar Home",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(inst_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 5, column = 0, padx = 20, pady = 20)
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
            recipe = nitrb["500 mL"]
            return recipe
        if reagent == "nitrate_buffer" and volume == 1000:
            recipe = nitrb["1 L"]
            return recipe
        if reagent == "nitrate_buffer" and volume == 2000:
            recipe = nitrb["2 L"]
            return recipe
        if reagent == "color_reagent" and volume == 500:
            recipe = nitrc["500 mL"]
            return recipe
        if reagent == "color_reagent" and volume == 1000:
            recipe = nitrc["1 L"]
            return recipe
        if reagent == "ffd6" and volume == 500:
            recipe = ffd6["500 mL"]
            return recipe
        if reagent == "ffd6" and volume == 1000:
            recipe = ffd6["1 L"]
            return recipe
        if reagent == "sulfuric_acid" and volume == 500:
            recipe = sulf["500 mL"]
            return recipe
        if reagent == "sulfuric_acid" and volume == 1000:
            recipe = sulf["1 L"]
            return recipe
        if reagent == "ammonium_heptamolybdate" and volume == 500:
            recipe = hept["500 mL"]
            return recipe
        if reagent == "ammonium_heptamolybdate" and volume == 1000:
            recipe = hept["1 L"]
            return recipe
        if reagent == "l_plus_ascorbic" and volume == 500:
            recipe = lplus["500 mL"]
            return recipe
        if reagent == "l_plus_ascorbic" and volume == 1000:
            recipe = lplus["1 L"]
            return recipe
        if reagent == "ammonium_buffer" and volume == 500:
            recipe = ammob["500 mL"]
            return recipe
        if reagent == "ammonium_buffer" and volume == 1000:
            recipe = ammob["1 L"]
            return recipe
        if reagent == "ammonium_buffer" and volume == 2000:
            recipe = ammob["2 L"]
            return recipe
        if reagent == "salicyalite" and volume == 500:
            recipe = sali["500 mL"]
            return recipe
        if reagent == "salicyalite" and volume == 1000:
            recipe = sali["1 L"]
            return recipe
        if reagent == "nitroprusside" and volume == 500:
            recipe = nitr["500 mL"]
            return recipe
        if reagent == "nitroprusside" and volume == 1000:
            recipe = nitr["1 L"]
            return recipe
        if reagent == "dichlorocyanurite" and volume == 500:
            recipe = dich["500 mL"]
            return recipe
        if reagent == "dichlorocyanurite" and volume == 1000:
            recipe = dich["1 L"]
            return recipe
        if reagent == "rinsing" and volume == 500:
            recipe = rins["500 mL"]
            return recipe
        if reagent == "rinsing" and volume == 1000:
            recipe = rins["1 L"]
            return recipe
        if reagent == "rinsing" and volume == 2000:
            recipe = rins["2 L"]
            return recipe
        if reagent == "std1":
            recipe = skastd["STD 1"]
            return recipe
        if reagent == "std2":
            recipe = skastd["STD 2"]
            return recipe
        if reagent == "std3":
            recipe = skastd["STD 3"]
            return recipe
        if reagent == "std4":
            recipe = skastd["STD 4"]
            return recipe
        if reagent == "std5":
            recipe = skastd["STD 5"]
            return recipe
        
class skalar_window:
    def steps():
        step_frame = tk.Frame()
        step_frame.pack()
        step1_click = tk.Button(step_frame,
                                text = "Step 1",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step1()]).grid(row = 0, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step2_click = tk.Button(step_frame,
                                text = "Step 2",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step2()]).grid(row = 0, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step3_click = tk.Button(step_frame,
                                text = "Step 3",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step3()]).grid(row = 0, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step4_click = tk.Button(step_frame,
                                text = "Step 4",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step4()]).grid(row = 1, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step5_click = tk.Button(step_frame,
                                text = "Step 5",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step5()]).grid(row = 1, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step6_click = tk.Button(step_frame,
                                text = "Step 6",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step6()]).grid(row = 1, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        step7_click = tk.Button(step_frame,
                                text = "Step 7",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step7()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        step8_click = tk.Button(step_frame,
                                text = "Step 8",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step8()]).grid(row = 2, column = 1,
                                                                                padx = 20,
                                                                                pady = 20)
        step9_click = tk.Button(step_frame,
                                text = "Step 9",
                                font = ("Arial", 20),
                                command = lambda: [mw.window.clear_frame(step_frame),
                                                   operating_procedure.step9()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        smtih_home_button = tk.Button(step_frame,
                                    font = ("Arial", 20),
                                    text = "Smith Lab Home",
                                    command = lambda: [mw.window.clear_frame(step_frame),
                                        mw.window.Smith_lab_home()]).grid(row = 5,
                                                                        column = 0,
                                                                        pady = 20)
        
class operating_procedure:
    def step1():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step1
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20,
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 1,
                                                                                      padx = 20,
                                                                                      pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step2()]).grid(row = 1, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    

    def step2():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step2
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 1",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step1()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step3()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)

    def step3():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step3
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 2",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step2()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step4()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step4():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step4
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 3",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step3()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step5()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step5():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                        height = 13,
                        width = 48,
                        font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step5
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                    padx = 20, 
                                                                    pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                    font = ("Arial", 20),
                                    text = "Skalar Step Home",
                                    command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                    padx = 20,
                                                                                    pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 4",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                operating_procedure.step4()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                operating_procedure.step6()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step6():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step6
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 5",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step5()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 7",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step7()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step7():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step7
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 6",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step6()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 8",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step8()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
    
    def step8():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step8
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 7",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step7()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)
        next_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 9",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step9()]).grid(row = 2, column = 2,
                                                                                padx = 20,
                                                                                pady = 20)
        
    def step9():
        instruct_frame = tk.Frame()
        instruct_frame.pack()
        skal_op = ins.skalar_operation
        text = tk.Text(instruct_frame,
                           height = 13,
                           width = 48,
                           font = ("Arial", 20))
        text.grid(row = 0, column = 1)
        step = skal_op.step9
        text.insert(tk.END, step)

        smith_home_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Smith Lab Home",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                    mw.window.Smith_lab_home()]).grid(row = 1, column = 0,
                                                                      padx = 20, 
                                                                      pady = 20)
        step_home_button = tk.Button(instruct_frame,
                                     font = ("Arial", 20),
                                     text = "Skalar Step Home",
                                     command = lambda: [mw.window.clear_frame(instruct_frame),
                                                        skalar_window.steps()]).grid(row = 1, column = 2,
                                                                                      padx = 20,
                                                                                      pady = 20)
        previous_button = tk.Button(instruct_frame,
                                font = ("Arial", 20),
                                text = "Step 8",
                                command = lambda: [mw.window.clear_frame(instruct_frame),
                                                   operating_procedure.step8()]).grid(row = 2, column = 0,
                                                                                padx = 20,
                                                                                pady = 20)