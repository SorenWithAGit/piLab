from src.smithLab import procedure as pr
from src.smithLab import ghg
from src.smithLab import icp
from src.smithLab import skalar as sk
from src.smithLab import procedure as pr
from src.smithLab import extractions as ex
from src.smithLab import microwaveDigestor as md
from src.smithLab import pHandEC as phec
from src.smithLab import formacs as fm

current_frame = None

class window:

     def clear_frame(frame):
          frame.destroy()
          
     def smith_lab_click(frame):
          window.clear_frame(frame)
          pr.mainFrames.Smith_lab_home()

     def instruments_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.instruments_click()
     
     def analytical_instrumentation_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.analytical_instruments()

     def piLab_home_click(frame):
          window.clear_frame(frame)
          pr.mainFrames.piLab_home()


class procedureControl:

     def m3_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.m3_click()

     def h3a_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.h3a_click()

     def olsen_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.olsen_click()

     def kcl_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.kcl_click()

     def extract_home_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.extracts_click()

     def extraction_proto_click(frame):
          window.clear_frame(frame)
          pr.procedure_selection.extraction_protocol()

     def stock_click(frame):
          window.clear_frame(frame)
          ex.recipes.m3_stock_click()

     def m3_1_click(frame):
          window.clear_frame(frame)
          ex.recipes.m3_1L_click()

     def m3_2_click(frame):
          window.clear_frame(frame)
          ex.recipes.m3_2L_click()
     
     def h3a_1_click(frame):
          window.clear_frame(frame)
          ex.recipes.h3a_1L_click()

     def h3a_2_click(frame):
          window.clear_frame(frame)
          ex.recipes.h3a_2L_click()

     def olsen_1_click(frame):
          window.clear_frame(frame)
          ex.recipes.olsen_1L_click()
     
     def olsen_2_click(frame):
          window.clear_frame(frame)
          ex.recipes.olsen_2L_click()

     def kcl_1N_1L(frame):
          window.clear_frame(frame)
          ex.recipes.kcl_1N_1L_click()

     def kcl_1N_2L(frame):
          window.clear_frame(frame)
          ex.recipes.kcl_1N_2L_click()

     def kcl_2N_1L(frame):
          window.clear_frame(frame)
          ex.recipes.kcl_2N_1L_click()

     def kcl_2N_2L(frame):
          window.clear_frame(frame)
          ex.recipes.kcl_2N_2L_click()

     def m3_proto_click(frame):
          window.clear_frame(frame)
          ex.extract_protocol.mehlich3_pro_click()

     def kcl_proto_click(frame):
          window.clear_frame(frame)
          ex.extract_protocol.potassium_chloride_click()

     def olsen_proto_click(frame):
          window.clear_frame(frame)
          ex.extract_protocol.olsenP_click()
     
     def h3a_proto_click(frame):
          window.clear_frame(frame)
          ex.extract_protocol.h3a_click()

     def hcl_proto_click(frame):
          window.clear_frame(frame)
          ex.extract_protocol.hcl_click()

class icpWindowControl:

     def icp_home(frame):
          window.clear_frame(frame)
          icp.icp_cookbook.icp_home_frame()

     def icp_step_home(frame):
          window.clear_frame(frame)
          icp.icp_step_window.steps()

     def std4_click(frame):
         window.clear_frame(frame)
         icp.icp_cookbook.icp_element_frame()

     def std3_click(frame):
         window.clear_frame(frame)
         icp.icp_control.std_3_proto()
    
     def std2_click(frame):
         window.clear_frame(frame)
         icp.icp_control.std_2_proto()

     def std1_click(frame):
         window.clear_frame(frame)
         icp.icp_control.std_2_proto()
     
     def al_click(frame):
         window.clear_frame(frame)
         icp.icp_control.stock_solutions("Aluminium")
      
     def ca_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Calcium")
     
     def cu_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Copper")

     def fe_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Iron")

     def k_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Potassium")

     def mg_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Magnesium")

     def mn_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Manganese")
     
     def na_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Sodium")

     def p_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Phosphorus")

     def s_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Sulfur")

     def zn_click(frame):
          window.clear_frame(frame)
          icp.icp_control.stock_solutions("Zinc")

     def icp_step1(frame):
          window.clear_frame(frame)
          icp.icp_operation.step1()

     def icp_step2(frame):
          window.clear_frame(frame)
          icp.icp_operation.step2()

     def icp_step3(frame):
          window.clear_frame(frame)
          icp.icp_operation.step3()

     def icp_step4(frame):
          window.clear_frame(frame)
          icp.icp_operation.step4()
     
     def icp_step5(frame):
          window.clear_frame(frame)
          icp.icp_operation.step5()

     def icp_step6(frame):
          window.clear_frame(frame)
          icp.icp_operation.step6()

     def icp_step7(frame):
          window.clear_frame(frame)
          icp.icp_operation.step7()

     def icp_step8(frame):
          window.clear_frame(frame)
          icp.icp_operation.step8()
     
     def icp_step9(frame):
          window.clear_frame(frame)
          icp.icp_operation.step9()

class skalarWindowControl:

     def skalar_home(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.home_frame()
     
     def nitr_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.nitrate_frame()
     
     def phos_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.phosphate_frame()
     
     def ammo_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.ammonium_frame()

     def rins_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("rinsing")

     def cal_stds_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.standards_frame()

     def nitr_buff_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.buffer_volume_frame("nitrate_buffer")

     def color_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("color_reagent")

     def ffd6_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("ffd6")

     def sulf_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("sulfuric_acid")

     def hept_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("ammonium_heptamolybdate")

     def lplus_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("l_plus_ascorbic")

     def ammo_buff_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.buffer_volume_frame("ammonium_buffer")

     def sali_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("salicyalite")

     def nitro_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("nitroprusside")

     def dichlor_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.volume_frame("dichlorocyanurite")
     
     def std1_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe("std1", 100)[0],
                                            sk.skalar_recipes.get_recipe("std1", 100)[1])

     def std2_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe("std2", 100)[0],
                                            sk.skalar_recipes.get_recipe("std2", 100)[1])

     def std3_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe("std3", 100)[0],
                                            sk.skalar_recipes.get_recipe("std3", 100)[1])

     def std4_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe("std4", 100)[0],
                                            sk.skalar_recipes.get_recipe("std5", 100)[1])

     def std5_click(frame):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe("std5", 100)[0],
                                            sk.skalar_recipes.get_recipe("std5", 100)[1])

     def buff_vol1_click(frame, reagent):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe(reagent, 500)[0],
                                            sk.skalar_recipes.get_recipe(reagent, 500)[1])

     def buff_vol2_click(frame, reagent):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe(reagent, 1000)[0],
                                            sk.skalar_recipes.get_recipe(reagent, 1000)[1])

     def buff_vol3_click(frame, reagent):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe(reagent, 2000)[0],
                                            sk.skalar_recipes.get_recipe(reagent, 2000)[1])

     def reag_vol1_click(frame, reagent):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe(reagent, 500)[0],
                                            sk.skalar_recipes.get_recipe(reagent, 500)[1])

     def reag_vol2_click(frame, reagent):
          window.clear_frame(frame)
          sk.skalar_cookbook.instruct_frame(sk.skalar_recipes.get_recipe(reagent, 1000)[0],
                                            sk.skalar_recipes.get_recipe(reagent, 1000)[1])

     def step_home(frame):
          window.clear_frame(frame)
          sk.skalar_window.steps()

     def sop_step1(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step1()

     def sop_step2(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step2()

     def sop_step3(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step3()
     
     def sop_step4(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step4()

     def sop_step5(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step5()

     def sop_step6(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step6()
     
     def sop_step7(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step7()

     def sop_step8(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step8()

     def sop_step9(frame):
          window.clear_frame(frame)
          sk.operating_procedure.step9()

class ghgWindowControl:

     def steps_home(frame):
          window.clear_frame(frame)
          ghg.ghg_window.steps()

     def stds_click(frame):
          window.clear_frame(frame)
          ghg.operating_procedure.stds()

     def step1_click(frame):
          window.clear_frame(frame)
          ghg.operating_procedure.step1()

     def step2_click(frame):
          window.clear_frame(frame)
          ghg.operating_procedure.step2()

     def step3_click(frame):
          window.clear_frame(frame)
          ghg.operating_procedure.step3()

     def step4_click(frame):
          window.clear_frame(frame)
          ghg.operating_procedure.step4()

class microwaveDigest:

     def digestHome(frame):
          window.clear_frame(frame)
          md.microwave_frame()

     def totalP(frame):
          window.clear_frame(frame)
          md.totalP_frame()

class pHEC:

     def phec_home(frame):
          window.clear_frame(frame)
          phec.phec_frame()

     def ec_click(frame):
          window.clear_frame(frame)
          phec.ecMeter.ec_steps()
     
     def ec_cal_click(frame):
          window.clear_frame(frame)
          phec.ecMeter.cal_click()

     def ec_mode_click(frame):
          window.clear_frame(frame)
          phec.ecMeter.mode_click()
     
     def ec_measure_click(frame):
          window.clear_frame(frame)
          phec.ecMeter.measure_click()

     def ph_click(frame):
          window.clear_frame(frame)
          phec.phMeter.ph_steps()

     def ph_cal_check(frame):
          window.clear_frame(frame)
          phec.phMeter.ph_cal_check()
     
     def ph_cal(frame):
          window.clear_frame(frame)
          phec.phMeter.ph_cal()

     def ph_measure_click(frame):
          window.clear_frame(frame)
          phec.phMeter.ph_measure_click()

class toc:

     def toc_home(frame):
          window.clear_frame(frame)
          fm.tocHome()
     
     def stds(frame):
          window.clear_frame(frame)
          fm.formacsOperation.standardFrame()
     
     def steps(frame):
          window.clear_frame(frame)
          fm.formacsOperation.stepsHome()
     
     def std1(frame):
          window.clear_frame(frame)
          fm.formacsOperation.std1_click()
     
     def std2(frame):
          window.clear_frame(frame)
          fm.formacsOperation.std2_click()
     
     def std3(frame):
          window.clear_frame(frame)
          fm.formacsOperation.std3_click()
     
     def phos(frame):
          window.clear_frame(frame)
          fm.formacsOperation.phos_click()
     
     def step1(frame):
          window.clear_frame(frame)
          fm.formacsOperation.step1()

     def step2(frame):
          window.clear_frame(frame)
          fm.formacsOperation.step2()
     
     def step3(frame):
          window.clear_frame(frame)
          fm.formacsOperation.step3()

     def step4(frame):
          window.clear_frame(frame)
          fm.formacsOperation.step4()
     
     def step5(frame):
          window.clear_frame(frame)
          fm.formacsOperation.step5()
     
     def step6(frame):
          window.clear_frame(frame)
          fm.formacsOperation.step6()
     