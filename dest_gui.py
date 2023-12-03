#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file dest_gui.py
 @brief RTC for specifying destination using GUI
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import tkinter as tk
from tkinter import StringVar


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
dest_gui_spec = ["implementation_id", "dest_gui", 
         "type_name",         "dest_gui", 
         "description",       "RTC for specifying destination using GUI", 
         "version",           "1.0.0", 
         "vendor",            "rsdlab", 
         "category",          "User Interface", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",

         "conf.default.place1", "Home",
         "conf.default.place2", "Reception desk",
         "conf.default.place3", "Room1",
         "conf.default.place4", "Room2",
         "conf.default.place5", "Room3",

         "conf.__widget__.place1", "text",
         "conf.__widget__.place2", "text",
         "conf.__widget__.place3", "text",
         "conf.__widget__.place4", "text",
         "conf.__widget__.place5", "text",

         "conf.__type__.place1", "string",
         "conf.__type__.place2", "string",
         "conf.__type__.place3", "string",
         "conf.__type__.place4", "string",
         "conf.__type__.place5", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class dest_gui
# @brief RTC for specifying destination using GUI
# 
# 
# </rtc-template>
class dest_gui(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_gui_in = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_inIn = OpenRTM_aist.InPort("gui_in", self._d_gui_in)
        self._d_gui_out = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_outOut = OpenRTM_aist.OutPort("gui_out", self._d_gui_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">      
        """
        
         - Name:  place1
         - DefaultValue: Home
        """
        self._place1 = ['Home']
        """
        
         - Name:  place2
         - DefaultValue: Reception desk
        """
        self._place2 = ['Reception desk']
        """
        
         - Name:  place3
         - DefaultValue: Room1
        """
        self._place3 = ['Room1']
        """
        
         - Name:  place4
         - DefaultValue: Room2
        """
        self._place4 = ['Room2']
        """
        
         - Name:  place5
         - DefaultValue: Room3
        """
        self._place5 = ['Room3']
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("place1", self._place1, "Home")
        self.bindParameter("place2", self._place2, "Reception desk")
        self.bindParameter("place3", self._place3, "Room1")
        self.bindParameter("place4", self._place4, "Room2")
        self.bindParameter("place5", self._place5, "Room3")
		
        # Set InPort buffers
        self.addInPort("gui_in",self._gui_inIn)
		
        # Set OutPort buffers
        self.addOutPort("gui_out",self._gui_outOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK

    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	

    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK

    #
    def onExecute(self, ec_id):
        root=tk.Tk()

        root.title("Guidance")

        root.geometry("500x400")

        def button_click0():
            self._d_gui_out.data = 0
            self._gui_outOut.write()
        
        def button_click1():
            self._d_gui_out.data = 1
            self._gui_outOut.write()

        def button_click2():
            self._d_gui_out.data = 2
            self._gui_outOut.write()      

        # def button_click3():
        #     self._d_gui_out.data = 3
        #     self._gui_outOut.write()

        button0 = tk.Button(
            text=self._place1,
            font=10,
            width=40,
            height=4,
            command = button_click0
        )
        button0.place(x=60, y=20) #ボタンを配置する位置の設定

        button1 = tk.Button(
            text=self._place2,
            font=10,
            width=40,
            height=4,
            command=button_click1,
        )
        button1.place(x=60, y=150) #ボタンを配置する位置の設定

        button2 = tk.Button(
            text=self._place3,
            font=10,
            width=40,
            height=4,
            command=button_click2,
        )
        button2.place(x=60, y=280) #ボタンを配置する位置の設定

        # button3 = tk.Button(
        #     text="Examination room2",
        #     width=50,
        #     height=3,
        #     command=button_click3,
        # )
        # button3.place(x=40, y=260)

        root.mainloop()      
    
        return RTC.RTC_OK




def dest_guiInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=dest_gui_spec)
    manager.registerFactory(profile,
                            dest_gui,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    dest_guiInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("dest_gui" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

