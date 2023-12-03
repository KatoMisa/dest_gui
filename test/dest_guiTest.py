#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file dest_guiTest.py
 @brief RTC for specifying destination using GUI
 @date $Date$


"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

import dest_gui

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
dest_guitest_spec = ["implementation_id", "dest_guiTest", 
         "type_name",         "dest_guiTest", 
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
# @class dest_guiTest
# @brief RTC for specifying destination using GUI
# 
# 
# </rtc-template>
class dest_guiTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_gui_out = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_outIn = OpenRTM_aist.InPort("gui_out", self._d_gui_out)
        self._d_gui_in = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_inOut = OpenRTM_aist.OutPort("gui_in", self._d_gui_in)


        


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
        self.addInPort("gui_out",self._gui_outIn)
        
        # Set OutPort buffers
        self.addOutPort("gui_in",self._gui_inOut)
        
        # Set service provider to Ports
        
        # Set service consumers to Ports
        
        # Set CORBA Service Ports
        
        return RTC.RTC_OK
    
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #
    #    return RTC.RTC_OK
    
    #    ##
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
    
        ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
    
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
    
        return RTC.RTC_OK
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("dest_guiTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def dest_guiTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=dest_guitest_spec)
    manager.registerFactory(profile,
                            dest_guiTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    dest_guiTestInit(manager)
    dest_gui.dest_guiInit(manager)

    # Create a component
    comp = manager.createComponent("dest_guiTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

