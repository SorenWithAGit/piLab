"""
#######################################################################
functions.py is a submodule within the schantzLab folder as part of the
pyLab package. 
This module contains the functions that are supplied to the lambda 
statements within the frames.py within the schantzLab.
#######################################################################
"""


import tkinter as tk
from ..smithLab import control as ctrl
from ..smithLab import procedure as pr
from src.schantzLab import frames as fr

class frames:

    def piLab_Home_Frame(frame):
        ctrl.window.clear_frame(frame)
        pr.mainFrames.piLab_home()

    def schantz_Home_Frame(frame):
        ctrl.window.clear_frame(frame)
        fr.homeFrames.schantz_lab_home()

    def schantz_instruments(frame):
        ctrl.window.clear_frame(frame)
        fr.homeFrames.instuments_frame()
    
    def elementar(frame):
        ctrl.window.clear_frame(frame)
        fr.instrumentFrames.elementar_frame()
    
    def rootScanner_Frame(frame):
        ctrl.window.clear_frame(frame)
        fr.instrumentFrames.root_scanner_frame()

class laiMeter:
    def sop(frame):
        ctrl.window.clear_frame(frame)
        fr.instrumentFrames.lai_frame()

class elementarSOPs:

    def step1(frame):
        ctrl.window.clear_frame(frame)
        fr.elementarSteps.step1()

    def step2(frame):
        ctrl.window.clear_frame(frame)
        fr.elementarSteps.step2()

    def step3(frame):
        ctrl.window.clear_frame(frame)
        fr.elementarSteps.step3()

class rootScannerSOPs:
    
    def step1(frame):
        ctrl.window.clear_frame(frame)
        fr.rootScannerSteps.step1()
    
    def step2(frame):
        ctrl.window.clear_frame(frame)
        fr.rootScannerSteps.step2()

    def step3(frame):
        ctrl.window.clear_frame(frame)
        fr.rootScannerSteps.step3()
        
    def step4(frame):
        ctrl.window.clear_frame(frame)
        fr.rootScannerSteps.step4()