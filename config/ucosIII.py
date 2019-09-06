# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

###############################################################################
########################## MicriumOSIII Configurations ########################
###############################################################################

def micriumOSFeatConf(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
        symbol.setValue(True, 1)
    else :
        symbol.setVisible(False)
        symbol.setValue(False, 1)

def micriumSymbolViibility(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def deactivateActiveRtos():
    activeComponents = Database.getActiveComponentIDs()

    for i in range(0, len(activeComponents)):
        if (activeComponents[i] == "FreeRTOS"):
            res = Database.deactivateComponents(["FreeRTOS"])
        if (activeComponents[i] == "ThreadX"):
            res = Database.deactivateComponents(["ThreadX"])

# Instatntiate Micrium OS III Component
def instantiateComponent(thirdPartyMicriumOSIII):
    Log.writeInfoMessage("Running MicriumOSIII")

    # Deactivate the active RTOS if any.
    deactivateActiveRtos()

    #MicriumOSIII Interrupt Handlers configurations
    SysTickInterruptEnable      = "SysTick_INTERRUPT_ENABLE"
    SysTickInterruptHandler     = "SysTick_INTERRUPT_HANDLER"
    SysTickInterruptHandlerLock = "SysTick_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", SysTickInterruptEnable)
    Database.setSymbolValue("core", SysTickInterruptEnable, True, 2)
    Database.clearSymbolValue("core", SysTickInterruptHandler)
    Database.setSymbolValue("core", SysTickInterruptHandler, "OS_CPU_SysTickHandler", 2)
    Database.clearSymbolValue("core", SysTickInterruptHandlerLock)
    Database.setSymbolValue("core", SysTickInterruptHandlerLock, True, 2)

    PendSVInterruptEnable       = "PendSV_INTERRUPT_ENABLE"
    PendSVInterruptHandler      = "PendSV_INTERRUPT_HANDLER"
    PendSVInterruptHandlerLock  = "PendSV_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", PendSVInterruptEnable)
    Database.setSymbolValue("core", PendSVInterruptEnable, True, 2)
    Database.clearSymbolValue("core", PendSVInterruptHandler)
    Database.setSymbolValue("core", PendSVInterruptHandler, "OS_CPU_PendSVHandler", 2)
    Database.clearSymbolValue("core", PendSVInterruptHandlerLock)
    Database.setSymbolValue("core", PendSVInterruptHandlerLock, True, 2)

    SVCallInterruptEnable       = "SVCall_INTERRUPT_ENABLE"
    SVCallInterruptHandler      = "SVCall_INTERRUPT_HANDLER"
    SVCallInterruptHandlerLock  = "SVCall_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", SVCallInterruptEnable)
    Database.setSymbolValue("core", SVCallInterruptEnable, True, 2)
    Database.clearSymbolValue("core", SVCallInterruptHandler)
    Database.setSymbolValue("core", SVCallInterruptHandler, "SVCall_Handler", 2)
    Database.clearSymbolValue("core", SVCallInterruptHandlerLock)
    Database.setSymbolValue("core", SVCallInterruptHandlerLock, True, 2)

    #MicriumOSIII Configuration Menu
    micriumSym_RtosMenu = thirdPartyMicriumOSIII.createMenuSymbol("UCOSIII_RTOS_MENU", None)
    micriumSym_RtosMenu.setLabel("RTOS Configuration")
    micriumSym_RtosMenu.setDescription("Configure uC/OS-III, Library and Port Library")

    micriumSym_FeatMenu = thirdPartyMicriumOSIII.createMenuSymbol("UCOSIII_FEATURE_MENU", micriumSym_RtosMenu)
    micriumSym_FeatMenu.setLabel("uC/OS-III Features")
    micriumSym_FeatMenu.setDescription("Compile-time configuration allows users to determine which features to enable and those features that are not needed. With compile-time configuration, the code and data sizes of uC/OS-III (i.e., its footprint) can be reduced by enabling only the desired functionality. MHC generates the uC/OS-III os_cfg.h file from this compile-time configuration. For more information, refer to http://www.micrium.com/rtos/ucosiii/overview/")

    micriumSym_AppHooks = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_APP_HOOKS_EN", micriumSym_FeatMenu)
    micriumSym_AppHooks.setLabel("Use application specific hooks")
    micriumSym_AppHooks.setDefaultValue(True)
    micriumSym_AppHooks.setDescription("uC/OS-III - Use application specific hooks. Specifies that application-defined hooks can be called from uC/OS-III's hooks. This allows the application code to extend the functionality of uC/OS-III. It's also up to a user to set pointer values to point to the appropriate application-defined hook functions. The pointers do not have to be set in main() but, you can set them after calling OSInit(). Note that not every hook function need to be defined, only the ones the user wants to place in the application code. Also, if you don't intend to extend uC/OS-III's hook through these application hooks, you can disable this setting to save RAM (i.e., the pointers). MHC sets the uC/OS-III preprocessor variable OS_CFG_APP_HOOKS_EN to 1/0 to enable/disable application specific hooks.")

    micriumSym_ArgCheck = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_ARG_CHK_EN", micriumSym_FeatMenu)
    micriumSym_ArgCheck.setLabel("Use argument checking")
    micriumSym_ArgCheck.setDefaultValue(True)
    micriumSym_ArgCheck.setDescription("uC/OS-III - Use argument checking. Determines whether the user wants most of uC/OS-III functions to perform argument checking. When selected, uC/OS-III ensures that pointers passed to functions are non-NULL, that arguments passed are within allowable range, that options are valid, and more. When disabled, those arguments are not checked and the amount of code space and processing time required by uC/OS-III is reduced. You would disable this option only if you are certain that the arguments are correct. uC/OS-III performs argument checking in over 40 functions. Therefore, you can save a few hundred bytes of code space by disabling this check. However, you should always enable argument checking until you are certain the code can be trusted. MHC sets the uC/OS-III preprocessor variable OS_CFG_ARG_CHK_EN to 1/0 to enable/disable argument checking.")

    micriumSym_CallFromIsr = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_CALLED_FROM_ISR_CHK_EN", micriumSym_FeatMenu)
    micriumSym_CallFromIsr.setLabel("Use check for called from ISR")
    micriumSym_CallFromIsr.setDefaultValue(True)
    micriumSym_CallFromIsr.setDescription("uC/OS-III - Use check for called from ISR. Determines whether most of uC/OS-III functions are to confirm that the function is not called from an ISR. In other words, most of the functions from uC/OS-III should be called by task-level code except \"post\" type functions (which can also be called from ISRs). By setting this option, uC/OS-III is told to make sure that functions that are only supposed to be called by tasks are not called by ISRs. It's highly recommended to select this option until you are absolutely certain that the code is behaving correctly and that task-level functions are always called from tasks. You can disable this option to save code space and, of course, processing time. uC/OS-III performs this check in approximately 50 functions. Therefore, you can save a few hundred bytes of code space by disabling this check. MHC sets the uC/OS-III preprocessor variable OS_CFG_CALLED_FROM_ISR_CHK_EN to 1/0 to enable/disable confirming that functions are not called from an ISR.")

    micriumSym_DebugCodeVar = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_DBG_EN", micriumSym_FeatMenu)
    micriumSym_DebugCodeVar.setLabel("Use debug code/variables")
    micriumSym_DebugCodeVar.setDefaultValue(True)
    micriumSym_DebugCodeVar.setDescription("uC/OS-III - Use debug code/variables. Adds ROM constants located in os_dbg.c to help support kernel aware debuggers. Specifically, a number of named ROM variables can be queried by a debugger to find out about compiled-in options. For example, a debugger can find out the size of an OS_TCB, uC/OS-III's version number, the size of an event flag group (OS_FLAG_GRP), and much more. MHC sets the uC/OS-III preprocessor variable OS_CFG_DBG_EN to 1/0 to enable/disable using debug code/variables.")

    micriumSym_KernelTickEnable = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TICK_EN", micriumSym_FeatMenu)
    micriumSym_KernelTickEnable.setLabel("Enable the Kernel tick")
    micriumSym_KernelTickEnable.setDefaultValue(True)
    micriumSym_KernelTickEnable.setDescription("Enable the Kernel tick.")

    micriumSym_DynTickEnable = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_DYN_TICK_EN", micriumSym_FeatMenu)
    micriumSym_DynTickEnable.setLabel("Enable the Dynamic tick")
    micriumSym_DynTickEnable.setDefaultValue(False)
    micriumSym_DynTickEnable.setDescription("Enable the Dynamic tick.")

    micriumSym_InvalidOsCallsCheck = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_INVALID_OS_CALLS_CHK_EN", micriumSym_FeatMenu)
    micriumSym_InvalidOsCallsCheck.setLabel("Enable checks for invalid kernel calls")
    micriumSym_InvalidOsCallsCheck.setDefaultValue(True)
    micriumSym_InvalidOsCallsCheck.setDescription("Enable checks for invalid kernel calls.")

    micriumSym_ObjTypeCheck = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_OBJ_TYPE_CHK_EN", micriumSym_FeatMenu)
    micriumSym_ObjTypeCheck.setLabel("Use object type checking")
    micriumSym_ObjTypeCheck.setDefaultValue(False)
    micriumSym_ObjTypeCheck.setDescription("uC/OS-III - Use argument checking. Determines whether the user wants most of uC/OS-III functions to perform argument checking. When selected, uC/OS-III ensures that pointers passed to functions are non-NULL, that arguments passed are within allowable range, that options are valid, and more. When disabled, those arguments are not checked and the amount of code space and processing time required by uC/OS-III is reduced. You would disable this option only if you are certain that the arguments are correct. uC/OS-III performs argument checking in over 40 functions. Therefore, you can save a few hundred bytes of code space by disabling this check. However, you should always enable argument checking until you are certain the code can be trusted. MHC sets the uC/OS-III preprocessor variable OS_CFG_ARG_CHK_EN to 1/0 to enable/disable argument checking.")

    micriumSym_TimeStamp = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TS_EN", micriumSym_FeatMenu)
    micriumSym_TimeStamp.setLabel("Use time stamping")
    micriumSym_TimeStamp.setDefaultValue(False)
    micriumSym_TimeStamp.setDescription("uC/OS-III - Use time stamping. Controls use of time-stamping. MHC sets the uC/OS-III preprocessor variable OS_CFG_TS_EN to 1/0 to enable/disable time-stamping.")

    micriumSym_MaxTaskPrio = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_PRIO_MAX", micriumSym_FeatMenu)
    micriumSym_MaxTaskPrio.setLabel("The maximum number of task priorities")
    micriumSym_MaxTaskPrio.setDefaultValue(8)
    micriumSym_MaxTaskPrio.setDescription("uC/OS-III - The maximum number of task priorities. Specifies the maximum number of priorities available in the application. Setting this option to just the number of priorities the user intends to use, reduces the amount of RAM needed by uC/OS-III. In uC/OS-III, task priorities can range from 0 (highest priority) to a maximum of 255 (lowest possible priority) when the data type OS_PRIO is defined as a CPU_INT08U. However, in uC/OS-III, there is no practical limit to the number of available priorities. Specifically, if defining OS_PRIO as a CPU_INT16U, there can be up to 65536 priority levels. It is recommended to leave OS_PRIO defined as a CPU_INT08U and use only 256 different priority levels (i.e., 0..255), which is generally sufficient for every application. You should always set the maximum number of task priorities to even multiples of 8 (8, 16, 32, 64, 128, 256, etc.). The higher the number of different priorities, the more RAM uC/OS-III will consume. MHC sets the uC/OS-III preprocessor variable OS_CFG_PRIO_MAX to the maximum number of task priorities. An application cannot create tasks with a priority number higher than or equal to OS_CFG_PRIO_MAX. In fact, uC/OS-III reserves priority OS_CFG_PRIO_MAX-2 and OS_CFG_PRIO_MAX-1 for itself; OS_CFG_PRIO_MAX-1 is reserved for the idle task OS_IdleTask(). Additionally, do not use priority 0 for an application since it is reserved by uC/OS-III's ISR handler task. The priorities of the application tasks can therefore take a value between 2 and OS_CFG_PRIO_MAX – 3 (inclusive).")

    micriumSym_MeasSchedlockTime = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_SCHED_LOCK_TIME_MEAS_EN", micriumSym_FeatMenu)
    micriumSym_MeasSchedlockTime.setLabel("Include code to measure scheduler lock time")
    micriumSym_MeasSchedlockTime.setDefaultValue(False)
    micriumSym_MeasSchedlockTime.setDescription("uC/OS-III - Include code to measure scheduler lock time. Controls code generation of code to measure the amount of time the scheduler is locked. This is useful when determining task latency. MHC sets the uC/OS-III preprocessor variable OS_CFG_SCHED_LOCK_TIME_MEAS_EN to 1/0 to include/exclude code to measure the amount of time the scheduler is locked.")

    micriumSym_RoundRobinSched = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_SCHED_ROUND_ROBIN_EN", micriumSym_FeatMenu)
    micriumSym_RoundRobinSched.setLabel("Include code for Round-Robin scheduling")
    micriumSym_RoundRobinSched.setDefaultValue(False)
    micriumSym_RoundRobinSched.setDescription("uC/OS-III - Include code for Round-Robin scheduling. Controls code generation of code for the round-robin feature of uC/OS-III. MHC sets the uC/OS-III preprocessor variable OS_CFG_SCHED_ROUND_ROBIN_EN to 1/0 to include/exclude code for the round-robin feature.")

    micriumSym_MinTaskStkSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_STK_SIZE_MIN", micriumSym_FeatMenu)
    micriumSym_MinTaskStkSize.setLabel("Minimum allowable task stack size")
    micriumSym_MinTaskStkSize.setDefaultValue(64)
    micriumSym_MinTaskStkSize.setDescription("uC/OS-III - Minimum allowable task stack size. This value specifies the minimum stack size (in CPU_STK elements) for each task. This is used by uC/OS-III to verify that sufficient stack space is provided for when each task is created. Suppose the full context of a processor consists of 16 registers of 32 bits. Also, suppose CPU_STK is declared as being of type CPU_INT32U, at a bare minimum, set OS_CFG_STK_SIZE_MIN to 16. However, it would be quite unwise to not accommodate for storage of local variables, function call returns, and possibly nested ISRs. Refer to the \"port\" of the processor used to see how to set this minimum. Again, this is a safeguard to make sure task stacks have sufficient stack space. MHC sets the uC/OS-III preprocessor variable OS_CFG_STK_SIZE_MIN to the specified value.")

    micriumSym_EventFlags = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_FLAG_EN", micriumSym_FeatMenu)
    micriumSym_EventFlags.setLabel("Use Event Flags")
    micriumSym_EventFlags.setDefaultValue(True)
    micriumSym_EventFlags.setDescription("uC/OS-III - Use EVENT FLAGS. Controls code generation of event flag services and data structures. This reduces the amount of code and data space needed when an application does not require event flags. MHC sets the uC/OS-III preprocessor variable OS_CFG_FLAG_EN to 1/0 to enable/disable using EVENT FLAGS.")

    micriumSym_OSFlagDel = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_FLAG_DEL_EN", micriumSym_EventFlags)
    micriumSym_OSFlagDel.setLabel("Include code for OSFlagDel()")
    micriumSym_OSFlagDel.setDefaultValue(True)
    micriumSym_OSFlagDel.setDescription("uC/OS-III - Include code for OSFlagDel. Controls code generation of function OSFlagDel(). MHC sets the uC/OS-III preprocessor variable OS_CFG_FLAG_DEL_EN to 1/0 to include/exclude OSFlagDel().")
    micriumSym_OSFlagDel.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_FLAG_EN"])

    micriumSym_WaitOnClearEventFlags = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_FLAG_MODE_CLR_EN", micriumSym_EventFlags)
    micriumSym_WaitOnClearEventFlags.setLabel("Include code for Wait on Clear Event Flags")
    micriumSym_WaitOnClearEventFlags.setDefaultValue(True)
    micriumSym_WaitOnClearEventFlags.setDescription("uC/OS-III - Include code for Wait on Clear EVENT FLAGS. Enables or disables code generation used to wait for event flags to be 0 instead of 1. Generally, you would wait for event flags to be set. However, the user may also want to wait for event flags to be clear and in this case, enable this option. MHC sets the uC/OS-III preprocessor variable OS_CFG_FLAG_MODE_CLR_EN to 1/0 to include/exclude code to wait for event flags to be 0.")
    micriumSym_WaitOnClearEventFlags.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_FLAG_EN"])

    micriumSym_OSFlagPendAbort = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_FLAG_PEND_ABORT_EN", micriumSym_EventFlags)
    micriumSym_OSFlagPendAbort.setLabel("Include code for OSFlagPendAbort()")
    micriumSym_OSFlagPendAbort.setDefaultValue(True)
    micriumSym_OSFlagPendAbort.setDescription("uC/OS-III - Include code for OSFlagPendAbort(). Controls code generation of function OSFlagPendAbort(). MHC sets the uC/OS-III preprocessor variable OS_CFG_FLAG_PEND_ABORT_EN to 1/0 to include/exclude OSFlagPendAbort().")
    micriumSym_OSFlagPendAbort.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_FLAG_EN"])

    micriumSym_MemManager = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_MEM_EN", micriumSym_FeatMenu)
    micriumSym_MemManager.setLabel("Use Memory Manager")
    micriumSym_MemManager.setDefaultValue(True)
    micriumSym_MemManager.setDescription("uC/OS-III - Use MEMORY MANAGER. Enables or disables code generation of the uC/OS-III partition memory manager and its associated data structures. This feature allows users to reduce the amount of code and data space needed when an application does not require the use of memory partitions. MHC sets the uC/OS-III preprocessor variable OS_CFG_MEM_EN to 1/0 to enable or disable the uC/OS-III partition memory manager.")

    micriumSym_UseMutex = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_MUTEX_EN", micriumSym_FeatMenu)
    micriumSym_UseMutex.setLabel("Use Mutex")
    micriumSym_UseMutex.setDefaultValue(True)
    micriumSym_UseMutex.setDescription("uC/OS-III - Use MUTEX. Enables or disables the code generation of all mutual exclusion semaphore services and data structures. This feature allows users to reduce the amount of code and data space needed when an application does not require the use of mutexes. MHC sets the uC/OS-III preprocessor variable OS_CFG_MUTEX_EN to 1/0 to enable or disable the code generation of all mutual exclusion semaphore services and data structures.")

    micriumSym_OSMutexDel = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_MUTEX_DEL_EN", micriumSym_UseMutex)
    micriumSym_OSMutexDel.setLabel("Include code for OSMutexDel()")
    micriumSym_OSMutexDel.setDefaultValue(True)
    micriumSym_OSMutexDel.setDescription("uC/OS-III - Include code for OSMutexDel(). Controls code generation of function OSMutexDel().MHC sets the uC/OS-III preprocessor variable OS_CFG_MUTEX_DEL_EN to 1/0 to include/exclude OSMutexDel().")
    micriumSym_OSMutexDel.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_MUTEX_EN"])

    micriumSym_OSMutexPendAbort = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_MUTEX_PEND_ABORT_EN", micriumSym_UseMutex)
    micriumSym_OSMutexPendAbort.setLabel("Include code for OSMutexPendAbort()")
    micriumSym_OSMutexPendAbort.setDefaultValue(True)
    micriumSym_OSMutexPendAbort.setDescription("uC/OS-III - Include code for OSMutexPendAbort(). Controls code generation of function OSMutexPendAbort(). MHC sets the uC/OS-III preprocessor variable OS_CFG_MUTEX_PEND_ABORT_EN to 1/0 to include/exclude OSMutexPendAbort().")
    micriumSym_OSMutexPendAbort.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_MUTEX_EN"])

    micriumSym_UseQueues = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_Q_EN", micriumSym_FeatMenu)
    micriumSym_UseQueues.setLabel("Use Queues")
    micriumSym_UseQueues.setDefaultValue(True)
    micriumSym_UseQueues.setDescription("uC/OS-III - Use QUEUES. Enables or disables all message queue services and data structures. This reduces the amount of code space needed when an application does not require the use of message queues. MHC sets the uC/OS-III preprocessor variable OS_CFG_Q_EN to 1/0 to enable or disable all message queue services and data structures.")

    micriumSym_OSQDel = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_Q_DEL_EN", micriumSym_UseQueues)
    micriumSym_OSQDel.setLabel("Include code for OSQDel()")
    micriumSym_OSQDel.setDefaultValue(True)
    micriumSym_OSQDel.setDescription("uC/OS-III - Include code for OSQDel(). Controls code generation of function OSQDel(). MHC sets the uC/OS-III preprocessor variable OS_CFG_Q_DEL_EN to 1/0 to include/exclude OSQDel().")
    micriumSym_OSQDel.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_Q_EN"])

    micriumSym_OSQFlush = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_Q_FLUSH_EN", micriumSym_UseQueues)
    micriumSym_OSQFlush.setLabel("Include code for OSQFlush()")
    micriumSym_OSQFlush.setDefaultValue(True)
    micriumSym_OSQFlush.setDescription("uC/OS-III - Include code for OSQFlush(). Controls code generation of function OSQFlush(). MHC sets the uC/OS-III preprocessor variable OS_CFG_Q_FLUSH_EN to 1/0 to include/exclude OSQFlush().")
    micriumSym_OSQFlush.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_Q_EN"])

    micriumSym_OSQPendAbort = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_Q_PEND_ABORT_EN", micriumSym_UseQueues)
    micriumSym_OSQPendAbort.setLabel("Include code for OSQPendAbort()")
    micriumSym_OSQPendAbort.setDefaultValue(True)
    micriumSym_OSQPendAbort.setDescription("uC/OS-III - Include code for OSQPendAbort(). Controls code generation of function OSQPendAbort(). MHC sets the uC/OS-III preprocessor variable OS_CFG_Q_PEND_ABORT_EN to 1/0 to include/exclude OSQPendAbort().")
    micriumSym_OSQPendAbort.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_Q_EN"])

    micriumSym_UseSem = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_SEM_EN", micriumSym_FeatMenu)
    micriumSym_UseSem.setLabel("Use Semaphores")
    micriumSym_UseSem.setDefaultValue(True)
    micriumSym_UseSem.setDescription("uC/OS-III - Use SEMAPHORES. Controls code generation of the semaphore manager and associated data structures. This reduces the amount of code and data space needed when an application does not require the use of semaphores. MHC sets the uC/OS-III preprocessor variable OS_CFG_SEM_EN to 1/0 to include/exclude code for the semaphore manager and associated data structures.")

    micriumSym_OSSemDel = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_SEM_DEL_EN", micriumSym_UseSem)
    micriumSym_OSSemDel.setLabel("Include code for OSSemDel()")
    micriumSym_OSSemDel.setDefaultValue(True)
    micriumSym_OSSemDel.setDescription("uC/OS-III - Include code for OSSemDel(). Controls code generation of function OSSemDel(). MHC sets the uC/OS-III preprocessor variable OS_CFG_SEM_DEL_EN to 1/0 to include/exclude OSSemDel().")
    micriumSym_OSSemDel.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_SEM_EN"])

    micriumSym_OSSemPendAbort = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_SEM_PEND_ABORT_EN", micriumSym_UseSem)
    micriumSym_OSSemPendAbort.setLabel("Include code for OSSemPendAbort()")
    micriumSym_OSSemPendAbort.setDefaultValue(True)
    micriumSym_OSSemPendAbort.setDescription("uC/OS-III - Include code for OSSemPendAbort(). Controls code generation of function OSSemPendAbort(). MHC sets the uC/OS-III preprocessor variable OS_CFG_SEM_PEND_ABORT_EN to 1/0 to include/exclude OSSemPendAbort().")
    micriumSym_OSSemPendAbort.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_SEM_EN"])

    micriumSym_OSSemSet = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_SEM_SET_EN", micriumSym_UseSem)
    micriumSym_OSSemSet.setLabel("Include code for OSSemSet()")
    micriumSym_OSSemSet.setDefaultValue(True)
    micriumSym_OSSemSet.setDescription("uC/OS-III - Include code for OSSemSet(). Controls code generation of function OSSemSet(). MHC sets the uC/OS-III preprocessor variable OS_CFG_SEM_SET_EN to 1/0 to include/exclude OSSemSet().")
    micriumSym_OSSemSet.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_SEM_EN"])

    micriumSym_UseTaskStat = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_STAT_TASK_EN", micriumSym_FeatMenu)
    micriumSym_UseTaskStat.setLabel("Use the statistics task")
    micriumSym_UseTaskStat.setDefaultValue(True)
    micriumSym_UseTaskStat.setDescription("uC/OS-III - Use the statistics task. Specifies whether or not to enable uC/OS-III's statistic task, as well as its initialization function. When selected, the statistic task OS_StatTask() and statistic task initialization function are enabled. OS_StatTask() computes the CPU usage of an application, stack usage of each task, the CPU usage of each task at run time and more. When enabled, OS_StatTask() executes at a rate of OS_CFG_STAT_TASK_RATE_HZ (see os_cfg_app.h), and computes the value of OSStatTaskCPUUsage, which is a variable that contains the percentage of CPU used by the application. OS_StatTask() calls OSStatTaskHook() every time it executes so that the user can add their own statistics as needed. See os_stat.c for details on the statistic task. The priority of OS_StatTask() is configurable by the application code (see os_cfg_app.h).OS_StatTask() also computes stack usage of each task created. In this case, OS_StatTask() calls OSTaskStkChk() for each task and the result is placed in the task's TCB. The .StkFree and .StkUsed field of the task's TCB represents the amount of free space (in bytes) and amount of used space, respectively. When this option is disabled, all variables used by the statistic task are not declared (see os.h). This, of course, reduces the amount of RAM needed by uC/OS-III when not enabling the statistic task. When this option is enabled, statistics will be determined at a rate of OS_CFG_STAT_TASK_RATE_HZ (see os_cfg_app.h). MHC sets the uC/OS-III preprocessor variable OS_CFG_STAT_TASK_EN  to 1/0 to include/exclude the statistics task.")

    micriumSym_CheckTaskStkStat = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_STAT_TASK_STK_CHK_EN", micriumSym_UseTaskStat)
    micriumSym_CheckTaskStkStat.setLabel("Check task stacks from statistic task")
    micriumSym_CheckTaskStkStat.setDefaultValue(True)
    micriumSym_CheckTaskStkStat.setDescription("uC/OS-III - Check task stacks from statistic task. Allows the statistic task to call OSTaskStkChk() for each task created. MHC sets the uC/OS-III preprocessor variable OS_CFG_STAT_TASK_STK_CHK_EN to 1/0 to check task stacks from statistic task.")
    micriumSym_CheckTaskStkStat.setDependencies(micriumOSFeatConf, ["UCOSIII_CFG_STAT_TASK_EN"])

    micriumSym_OSTaskChangePrio = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_CHANGE_PRIO_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskChangePrio.setLabel("Include code for OSTaskChangePrio()")
    micriumSym_OSTaskChangePrio.setDefaultValue(True)
    micriumSym_OSTaskChangePrio.setDescription("uC/OS-III - Include code for OSTaskChangePrio(). Controls code generation of function OSTaskChangePrio(). MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_CHANGE_PRIO_EN to 1/0 to include/exclude OSTaskChangePrio().")

    micriumSym_OSTaskDel = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_DEL_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskDel.setLabel("Include code for OSTaskDel()")
    micriumSym_OSTaskDel.setDefaultValue(True)
    micriumSym_OSTaskDel.setDescription("uC/OS-III - Include code for OSTaskDel(). Controls code generation of function OSTaskDel(). MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_DEL_EN to 1/0 to include/exclude OSTaskDel().")

    micriumSym_OSTasIdleEnable = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_IDLE_EN", micriumSym_FeatMenu)
    micriumSym_OSTasIdleEnable.setLabel("Include code the idle task")
    micriumSym_OSTasIdleEnable.setDefaultValue(True)
    micriumSym_OSTasIdleEnable.setDescription("uC/OS-III - Include code the idle task.")

    micriumSym_OSTaskQXXXX = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_Q_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskQXXXX.setLabel("Include code for OSTaskQXXXX()")
    micriumSym_OSTaskQXXXX.setDefaultValue(True)
    micriumSym_OSTaskQXXXX.setDescription("uC/OS-III - Include code for OSTaskQXXXX(). Controls code generation of the OSTaskQXXX() functions used to send and receive messages directly to/from tasks and ISRs. Sending messages directly to a task is more efficient than sending messages using a message queue because there is no pend list associated with messages sent to a task. MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_Q_EN to 1/0 to include/exclude the OSTaskQXXX() functions.")

    micriumSym_OSTaskQPendAbort = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_Q_PEND_ABORT_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskQPendAbort.setLabel("Include code for OSTaskQPendAbort()")
    micriumSym_OSTaskQPendAbort.setDefaultValue(True)
    micriumSym_OSTaskQPendAbort.setDescription("MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_Q_PEND_ABORT_EN to 1/0 to include/exclude OSTaskQPendAbort()")

    micriumSym_TaskProf = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_PROFILE_EN", micriumSym_FeatMenu)
    micriumSym_TaskProf.setLabel("Include variables in OS_TCB for profiling")
    micriumSym_TaskProf.setDefaultValue(True)
    micriumSym_TaskProf.setDescription("uC/OS-III - Include variables in OS_TCB for profiling. This options allows variables to be allocated in each task's OS_TCB to hold performance data about each task. If enabled, each task will have a variable to keep track of the number of times a task is switched to, the task execution time, the percent CPU usage of the task relative to the other tasks and more. The information made available with this feature is highly useful when debugging, but requires extra RAM. MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_PROFILE_EN to 1/0 to include/exclude variables in OS_TCB for profiling.")

    micriumSym_TaskSpecReg = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TASK_REG_TBL_SIZE", micriumSym_FeatMenu)
    micriumSym_TaskSpecReg.setLabel("Number of task specific registers")
    micriumSym_TaskSpecReg.setDefaultValue(1)
    micriumSym_TaskSpecReg.setDescription("uC/OS-III - Number of task specific registers. This value allows each task to have task context variables. Use task variables to store such elements as \"errno\", task identifiers and other task-specific values. The number of variables that a task contains is set by this constant. Each variable is identified by a unique identifier from 0 to the number of task specific registers - 1. Also, each variable is declared as having an OS_REG data type (see os_type.h). If OS_REG is a CPU_INT32U, all variables in this table are of this type. MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_REG_TBL_SIZE to the specified number of task specific registers.")

    micriumSym_OSTaskStkRedzone = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_STK_REDZONE_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskStkRedzone.setLabel("Enable stack redzone")
    micriumSym_OSTaskStkRedzone.setDefaultValue(False)
    micriumSym_OSTaskStkRedzone.setDescription("uC/OS-III - Enable stack redzone")

    micriumSym_OSTaskTaskStkRedzoneDepth = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TASK_STK_REDZONE_DEPTH", micriumSym_OSTaskStkRedzone)
    micriumSym_OSTaskTaskStkRedzoneDepth.setLabel("Depth of the stack redzone")
    micriumSym_OSTaskTaskStkRedzoneDepth.setDefaultValue(8)
    micriumSym_OSTaskTaskStkRedzoneDepth.setDescription("uC/OS-III - Depth of the stack redzone")
    micriumSym_OSTaskTaskStkRedzoneDepth.setVisible(False)
    micriumSym_OSTaskTaskStkRedzoneDepth.setDependencies(micriumSymbolViibility, ["UCOSIII_CFG_TASK_STK_REDZONE_EN"])

    micriumSym_OSTaskSemPendAbort = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_SEM_PEND_ABORT_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskSemPendAbort.setLabel("Include code for OSTaskSemPendAbort()")
    micriumSym_OSTaskSemPendAbort.setDefaultValue(True)
    micriumSym_OSTaskSemPendAbort.setDescription("uC/OS-III - Include code for OSTaskSemPendAbort(). Controls code generation of function OSTaskSemPendAbort(). MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_SEM_PEND_ABORT_EN to 1/0 to include/exclude OSTaskSemPendAbort().")

    micriumSym_OSTaskSuspend = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TASK_SUSPEND_EN", micriumSym_FeatMenu)
    micriumSym_OSTaskSuspend.setLabel("Include code for OSTaskSuspend()")
    micriumSym_OSTaskSuspend.setDefaultValue(True)
    micriumSym_OSTaskSuspend.setDescription("uC/OS-III - Include code for OSTaskSuspend() and OSTaskResume(). Controls code generation of functions OSTaskSuspend() and OSTaskResume(), which allows the application to explicitly suspend and resume tasks, respectively. Suspending and resuming a task is useful when debugging, especially if calling these functions via a terminal interface at run time. MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_SUSPEND_EN to 1/0 to include/exclude OSTaskSuspend() and OSTaskResume().")

    micriumSym_OSTaskTlsTblSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TLS_TBL_SIZE", micriumSym_FeatMenu)
    micriumSym_OSTaskTlsTblSize.setLabel("Include code for Task Local Storage (TLS) registers")
    micriumSym_OSTaskTlsTblSize.setDefaultValue(0)
    micriumSym_OSTaskTlsTblSize.setDescription("uC/OS-III - Include (DEF_ENABLED) code for Task Local Storage (TLS) registers")

    micriumSym_OSTimeDlyHMSM = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TIME_DLY_HMSM_EN", micriumSym_FeatMenu)
    micriumSym_OSTimeDlyHMSM.setLabel("Include code for OSTimeDlyHMSM()")
    micriumSym_OSTimeDlyHMSM.setDefaultValue(True)
    micriumSym_OSTimeDlyHMSM.setDescription("uC/OS-III - Include code for OSTimeDlyHMSM(). Controls code generation of function OSTimeDlyHMSM(), which is used to delay a task for a specified number of hours, minutes, seconds, and milliseconds. MHC sets the uC/OS-III preprocessor variable OS_CFG_TIME_DLY_HMSM_EN to 1/0 to include/exclude OSTimeDlyHMSM().")

    micriumSym_OSTimeDlyResume = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TIME_DLY_RESUME_EN", micriumSym_FeatMenu)
    micriumSym_OSTimeDlyResume.setLabel("Include code for OSTimeDlyResume()")
    micriumSym_OSTimeDlyResume.setDefaultValue(True)
    micriumSym_OSTimeDlyResume.setDescription("uC/OS-III - Include code for OSTimeDlyResume(). Controls code generation of function OSTimeDlyResume(). MHC sets the uC/OS-III preprocessor variable OS_CFG_TIME_DLY_HMSM_EN to 1/0 to include/exclude OSTimeDlyResume().")

    micriumSym_UseTimers = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TMR_EN", micriumSym_FeatMenu)
    micriumSym_UseTimers.setLabel("Use Timers")
    micriumSym_UseTimers.setDefaultValue(True)
    micriumSym_UseTimers.setDescription("uC/OS-III - Use TIMERS. Controls code generation of timer management functions. MHC sets the uC/OS-III preprocessor variable OS_CFG_TMR_EN to 1/0 to include/exclude timer management functions.")

    micriumSym_OSTmrDel = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TMR_DEL_EN", micriumSym_FeatMenu)
    micriumSym_OSTmrDel.setLabel("Use OSTmrDel()")
    micriumSym_OSTmrDel.setDefaultValue(True)
    micriumSym_OSTmrDel.setDescription("uC/OS-III - Include code for OSTmrDel(). Controls code generation of function OSTmrDel(). MHC sets the uC/OS-III preprocessor variable OS_CFG_TMR_DEL_EN to 1/0 to include/exclude OSTmrDel().")

    micriumSym_OSTraceEnable = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TRACE_EN", micriumSym_FeatMenu)
    micriumSym_OSTraceEnable.setLabel("Enable uC/OS-III Trace instrumentation")
    micriumSym_OSTraceEnable.setDefaultValue(False)
    micriumSym_OSTraceEnable.setDescription("uC/OS-III - Enable uC/OS-III Trace instrumentation")

    micriumSym_OSTraceApiEnterEnable = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TRACE_API_ENTER_EN", micriumSym_FeatMenu)
    micriumSym_OSTraceApiEnterEnable.setLabel("Enable uC/OS-III Trace API enter instrumentation")
    micriumSym_OSTraceApiEnterEnable.setDefaultValue(False)
    micriumSym_OSTraceApiEnterEnable.setDescription("uC/OS-III - Enable uC/OS-III Trace API enter instrumentation")

    micriumSym_OSTraceApiExitEnable = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_CFG_TRACE_API_EXIT_EN", micriumSym_FeatMenu)
    micriumSym_OSTraceApiExitEnable.setLabel("Enable uC/OS-III Trace API exit  instrumentation")
    micriumSym_OSTraceApiExitEnable.setDefaultValue(False)
    micriumSym_OSTraceApiExitEnable.setDescription("uC/OS-III - Enable uC/OS-III Trace API exit  instrumentation")

    micriumSym_StkPoolMenu = thirdPartyMicriumOSIII.createMenuSymbol("UCOSIII_STACK_POOLS_MENU", micriumSym_RtosMenu)
    micriumSym_StkPoolMenu.setLabel("uC/OS-III Stacks, Pools, and Other")
    micriumSym_StkPoolMenu.setDescription("uC/OS-III - Stacks, Pools, and Other. uC/OS-III allows the user to configure the sizes of the idle task stack, statistic task stack, message pool, and more. MHC generates the uC/OS-III os_cfg_app.h file from this compile-time configuration.")

    micriumSym_MaxMsgSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_MSG_POOL_SIZE", micriumSym_StkPoolMenu)
    micriumSym_MaxMsgSize.setLabel("Maximum number of messages")
    micriumSym_MaxMsgSize.setDefaultValue(100)
    micriumSym_MaxMsgSize.setDescription("uC/OS-III - Maximum number of messages. This entry specifies the number of OS_MSGs available in the pool of OS_MSGs. The size is specified in number of OS_MSG elements. MHC sets the uC/OS-III preprocessor variable OS_CFG_MSG_POOL_SIZE to the specified value.")

    micriumSym_IsrStkSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_ISR_STK_SIZE", micriumSym_StkPoolMenu)
    micriumSym_IsrStkSize.setLabel("ISR stack size")
    micriumSym_IsrStkSize.setDefaultValue(512)
    micriumSym_IsrStkSize.setDescription("uC/OS-III - ISR stack size. This specifies the size of uC/OS-III's interrupt stack (in CPU_STK elements). Note that the stack size needs to accommodate for worst case interrupt nesting. MHC sets the uC/OS-III preprocessor variable OS_CFG_ISR_STK_SIZE to the specified value.")

    micriumSym_StkLimPos = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TASK_STK_LIMIT_PCT_EMPTY", micriumSym_StkPoolMenu)
    micriumSym_StkLimPos.setLabel("Stack limit position in percentage to empty")
    micriumSym_StkLimPos.setDefaultValue(10)
    micriumSym_StkLimPos.setDescription("uC/OS-III - Stack limit position in percentage to empty. Sets the position (as a percentage to empty) of the stack limit for the idle, statistic, tick, interrupt queue handler, and timer tasks stacks. In other words, the amount of space to leave before the stack is empty. For example if the stack contains 1000 CPU_STK entries and the user sets percent to empty to 10, the stack limit will be set when the stack reaches 90% full, or 10% empty. MHC sets the uC/OS-III preprocessor variable OS_CFG_TASK_STK_LIMIT_PCT_EMPTY to the specified value.")

    micriumSym_IdleStkSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_IDLE_TASK_STK_SIZE", micriumSym_StkPoolMenu)
    micriumSym_IdleStkSize.setLabel("Idle stack size")
    micriumSym_IdleStkSize.setMin(micriumSym_MinTaskStkSize.getValue())
    micriumSym_IdleStkSize.setMax(99999)
    micriumSym_IdleStkSize.setDescription("uC/OS-III - Idle stack size. This #define sets the size of the idle task's stack (in CPU_STK elements).  Note that the stack size needs to be at least greater than OS_CFG_STK_SIZE_MIN. MHC sets the uC/OS-III preprocessor variable OS_CFG_IDLE_TASK_STK_SIZE to the specified value.")

    micriumSym_StatTaskRateHz = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_STAT_TASK_RATE_HZ", micriumSym_StkPoolMenu)
    micriumSym_StatTaskRateHz.setLabel("Statistics task rate of execution in Hz")
    micriumSym_StatTaskRateHz.setDefaultValue(10)
    micriumSym_StatTaskRateHz.setDescription("uC/OS-III - Statistics task rate of execution in Hz. Defines the execution rate (in Hz) of the statistic task. It is recommended to make this rate an even multiple of the tick rate (OS_CFG_TICK_RATE_HZ). MHC sets the uC/OS-III preprocessor variable OS_CFG_STAT_TASK_RATE_HZ to the specified value.")
    micriumSym_StatTaskRateHz.setDependencies(micriumSymbolViibility, ["UCOSIII_CFG_STAT_TASK_EN"])

    micriumSym_StatTaskStkSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_STAT_TASK_STK_SIZE", micriumSym_StkPoolMenu)
    micriumSym_StatTaskStkSize.setLabel("Statistics task stack size")
    micriumSym_StatTaskStkSize.setMin(micriumSym_MinTaskStkSize.getValue())
    micriumSym_StatTaskStkSize.setMax(99999)
    micriumSym_StatTaskStkSize.setDefaultValue(512)
    micriumSym_StatTaskStkSize.setDescription("uC/OS-III - Statistics task stack size. Sets the size of the statistic task's stack (in CPU_STK elements).  Note that the stack size needs to be at least greater than OS_CFG_STK_SIZE_MIN. MHC sets the uC/OS-III preprocessor variable OS_CFG_STAT_TASK_STK_SIZE to the specified value.")
    micriumSym_StatTaskStkSize.setDependencies(micriumSymbolViibility, ["UCOSIII_CFG_STAT_TASK_EN"])

    micriumSym_UseTickInt = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_TICK_INTERRUPT", micriumSym_StkPoolMenu)
    micriumSym_UseTickInt.setLabel("Tick interrupt")
    micriumSym_UseTickInt.setDefaultValue(True)
    micriumSym_UseTickInt.setReadOnly(True)
    micriumSym_UseTickInt.setDescription("uC/OS-III - Tick Interrupt. Enables (when set to 1) or disables (when set to 0) the code generation of the system interrupt services. MHC sets the system service preprocessor variable SYS_INT to TRUE.")

    micriumSym_TickIntHz = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TICK_RATE_HZ", micriumSym_StkPoolMenu)
    micriumSym_TickIntHz.setLabel("Tick rate in Hz")
    micriumSym_TickIntHz.setDefaultValue(1000)
    micriumSym_TickIntHz.setDescription("uC/OS-III - Tick rate in Hz. Specifies the rate in Hertz of uC/OS-III's tick interrupt. The tick rate should be set between 10 and 1000 Hz. The higher the rate, the more overhead it will impose on the processor. The desired rate depends on the granularity required for time delays and timeouts. MHC sets the uC/OS-III preprocessor variable OS_CFG_TICK_RATE_HZ to the specified value.")

    micriumSym_TmrTaskRateHz = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TMR_TASK_RATE_HZ", micriumSym_StkPoolMenu)
    micriumSym_TmrTaskRateHz.setLabel("Timer rate in Hz")
    micriumSym_TmrTaskRateHz.setDefaultValue(10)
    micriumSym_TmrTaskRateHz.setDescription("uC/OS-III - Timer rate in Hz. Specifies the rate in Hertz of uC/OS-III's timer task. The timer task rate should typically be set to 10 Hz. However, timers can run at a faster rate at the price of higher processor overhead. Note that OS_CFG_TMR_TASK_RATE_HZ MUST be an integer multiple of OS_CFG_TICK_TASK_RATE_HZ. In other words, if setting OS_CFG_TICK_TASK_RATE_HZ to 1000, do not set OS_CFG_TMR_TASK_RATE_HZ to 11 since 90.91 ticks would be required for every timer update, and 90.91 is not an integer multiple. Use approximately 10 Hz in this example. MHC sets the uC/OS-III preprocessor variable OS_CFG_TMR_TASK_RATE_HZ to the specified value.")

    micriumSym_TmrTaskStkSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_CFG_TMR_TASK_STK_SIZE", micriumSym_StkPoolMenu)
    micriumSym_TmrTaskStkSize.setLabel("Timer task stack size")
    micriumSym_TmrTaskStkSize.setMin(micriumSym_MinTaskStkSize.getValue())
    micriumSym_TmrTaskStkSize.setMax(99999)
    micriumSym_TmrTaskStkSize.setDefaultValue(512)
    micriumSym_TmrTaskStkSize.setDescription("uC/OS-III - Timer task stack size. Sets the size of the timer task's stack (in CPU_STK elements).  Note that the stack size needs to be at least greater than OS_CFG_STK_SIZE_MIN. MHC sets the uC/OS-III preprocessor variable OS_CFG_TMR_TASK_STK_SIZE to the specified value.")

    micriumSym_PortableLibMenu = thirdPartyMicriumOSIII.createMenuSymbol("UCOSIII_PORTABLE_LIBRARY_MENU", micriumSym_RtosMenu)
    micriumSym_PortableLibMenu.setLabel("uC/OS-III Portable Library Functions")
    micriumSym_PortableLibMenu.setDescription("uC/OS-III - Portable Library Functions. uC/LIB consists of library functions meant to be highly portable and not tied to any specific compiler. This facilitates third-party certification of Micrium products. uC/OS-III does not use any uC/LIB functions, however uC/OS-III and uC/CPU assumes the presence of lib_def.h for such definitions as: DEF_YES, DEF_NO, DEF_TRUE, DEF_FALSE, DEF_ON, DEF_OFF and more.")

    micriumSym_PortableLibFunc = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_USE_PORTABLE_LIBRARY_FUNCTIONS", micriumSym_PortableLibMenu)
    micriumSym_PortableLibFunc.setLabel("Use portable library functions?")
    micriumSym_PortableLibFunc.setDefaultValue(False)
    micriumSym_PortableLibFunc.setDescription("uC/OS-III - Use portable library functions?. MHC includes the portable library functions in the project when this option is selected.")

    micriumSym_LibMemCfgArgCheck = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_LIB_MEM_CFG_ARG_CHK_EXT_EN", micriumSym_PortableLibFunc)
    micriumSym_LibMemCfgArgCheck.setLabel("Enable argument check feature")
    micriumSym_LibMemCfgArgCheck.setDefaultValue(False)
    micriumSym_LibMemCfgArgCheck.setDescription("uC/OS-III - Enable argument check feature. MHC sets the uC/OS-III preprocessor variable LIB_MEM_CFG_ARG_CHK_EXT_EN to the specified value.")
    micriumSym_LibMemCfgArgCheck.setDependencies(micriumSymbolViibility, ["UCOSIII_USE_PORTABLE_LIBRARY_FUNCTIONS"])
    micriumSym_LibMemCfgArgCheck.setVisible(False)

    micriumSym_LibMemCfgOptAsm = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_LIB_MEM_CFG_OPTIMIZE_ASM_EN", micriumSym_PortableLibFunc)
    micriumSym_LibMemCfgOptAsm.setLabel("Configure assembly-optimized function(s)")
    micriumSym_LibMemCfgOptAsm.setDefaultValue(False)
    micriumSym_LibMemCfgOptAsm.setDescription("uC/OS-III - Configure assembly-optimized function(s). MHC sets the uC/OS-III preprocessor variable LIB_MEM_CFG_OPTIMIZE_ASM_EN to the specified value.")
    micriumSym_LibMemCfgOptAsm.setDependencies(micriumSymbolViibility, ["UCOSIII_USE_PORTABLE_LIBRARY_FUNCTIONS"])
    micriumSym_LibMemCfgOptAsm.setVisible(False)

    micriumSym_LibMemCfgAlloc = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_LIB_MEM_CFG_ALLOC_EN", micriumSym_PortableLibFunc)
    micriumSym_LibMemCfgAlloc.setLabel("Enable memory allocation functions")
    micriumSym_LibMemCfgAlloc.setDefaultValue(False)
    micriumSym_LibMemCfgAlloc.setDescription("uC/OS-III - Enable memory allocation functions. MHC sets the uC/OS-III preprocessor variable LIB_MEM_CFG_ALLOC_EN to the specified value.")
    micriumSym_LibMemCfgAlloc.setDependencies(micriumSymbolViibility, ["UCOSIII_USE_PORTABLE_LIBRARY_FUNCTIONS"])
    micriumSym_LibMemCfgAlloc.setVisible(False)

    micriumSym_LibMemCfgHeadSize = thirdPartyMicriumOSIII.createIntegerSymbol("UCOSIII_LIB_MEM_CFG_HEAP_SIZE", micriumSym_LibMemCfgAlloc)
    micriumSym_LibMemCfgHeadSize.setLabel("Heap Size")
    micriumSym_LibMemCfgHeadSize.setDefaultValue(0)
    micriumSym_LibMemCfgHeadSize.setDescription("uC/OS-III - Heap Size. MHC sets the uC/OS-III preprocessor variable LIB_MEM_CFG_HEAP_SIZE to the specified value.")
    micriumSym_LibMemCfgHeadSize.setDependencies(micriumSymbolViibility, ["UCOSIII_LIB_MEM_CFG_ALLOC_EN"])
    micriumSym_LibMemCfgHeadSize.setVisible(False)

    micriumSym_LibStrCfgFloatPoint = thirdPartyMicriumOSIII.createBooleanSymbol("UCOSIII_LIB_STR_CFG_FP_EN", micriumSym_PortableLibFunc)
    micriumSym_LibStrCfgFloatPoint.setLabel("Enable floating point string functions")
    micriumSym_LibStrCfgFloatPoint.setDefaultValue(False)
    micriumSym_LibStrCfgFloatPoint.setDescription("uC/OS-III - Enable floating point string functions. MHC sets the uC/OS-III preprocessor variable LIB_STR_CFG_FP_EN to the specified value.")
    micriumSym_LibStrCfgFloatPoint.setDependencies(micriumSymbolViibility, ["UCOSIII_USE_PORTABLE_LIBRARY_FUNCTIONS"])
    micriumSym_LibStrCfgFloatPoint.setVisible(False)


############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    # RTOS Configurations: MicriumOSIII OS, App and Library Configurations
    micriumAppConfHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_APP_CONFIG_H", None)
    micriumAppConfHeaderFile.setSourcePath("templates/app_cfg.h.ftl")
    micriumAppConfHeaderFile.setOutputName("app_cfg.h")
    micriumAppConfHeaderFile.setDestPath("micrium_config/")
    micriumAppConfHeaderFile.setProjectPath("config/" + configName + "/micrium_config/")
    micriumAppConfHeaderFile.setType("HEADER")
    micriumAppConfHeaderFile.setMarkup(True)

    micriumCpuConfHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_CONFIG_H", None)
    micriumCpuConfHeaderFile.setSourcePath("templates/cpu_cfg.h.ftl")
    micriumCpuConfHeaderFile.setOutputName("cpu_cfg.h")
    micriumCpuConfHeaderFile.setDestPath("micrium_config/")
    micriumCpuConfHeaderFile.setProjectPath("config/" + configName + "/micrium_config/")
    micriumCpuConfHeaderFile.setType("HEADER")
    micriumCpuConfHeaderFile.setMarkup(True)

    micriumLibConfHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_CONFIG_H", None)
    micriumLibConfHeaderFile.setSourcePath("templates/lib_cfg.h.ftl")
    micriumLibConfHeaderFile.setOutputName("lib_cfg.h")
    micriumLibConfHeaderFile.setDestPath("micrium_config/")
    micriumLibConfHeaderFile.setProjectPath("config/" + configName + "/micrium_config/")
    micriumLibConfHeaderFile.setType("HEADER")
    micriumLibConfHeaderFile.setMarkup(True)

    micriumOsConfHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_CONFIG_H", None)
    micriumOsConfHeaderFile.setSourcePath("templates/os_cfg.h.ftl")
    micriumOsConfHeaderFile.setOutputName("os_cfg.h")
    micriumOsConfHeaderFile.setDestPath("micrium_config/")
    micriumOsConfHeaderFile.setProjectPath("config/" + configName + "/micrium_config/")
    micriumOsConfHeaderFile.setType("HEADER")
    micriumOsConfHeaderFile.setMarkup(True)

    micriumOsAppConfHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_APP_CONFIG_H", None)
    micriumOsAppConfHeaderFile.setSourcePath("templates/os_cfg_app.h.ftl")
    micriumOsAppConfHeaderFile.setOutputName("os_cfg_app.h")
    micriumOsAppConfHeaderFile.setDestPath("micrium_config/")
    micriumOsAppConfHeaderFile.setProjectPath("config/" + configName + "/micrium_config/")
    micriumOsAppConfHeaderFile.setType("HEADER")
    micriumOsAppConfHeaderFile.setMarkup(True)

    # Source: MicriumOSIII/Software/uC-CPU/
    micriumCpuCoreSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_CORE_C", None)
    micriumCpuCoreSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/cpu_core.c")
    micriumCpuCoreSourceFile.setOutputName("cpu_core.c")
    micriumCpuCoreSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/")
    micriumCpuCoreSourceFile.setProjectPath("MicriumOSIII/Software/uC-CPU/")
    micriumCpuCoreSourceFile.setType("SOURCE")
    micriumCpuCoreSourceFile.setMarkup(False)

    # Header: MicriumOSIII/Software/uC-CPU/
    micriumCpuCacheHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_CACHE_H", None)
    micriumCpuCacheHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/cpu_cache.h")
    micriumCpuCacheHeaderFile.setOutputName("cpu_cache.h")
    micriumCpuCacheHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/")
    micriumCpuCacheHeaderFile.setProjectPath("MicriumOSIII/Software/uC-CPU/")
    micriumCpuCacheHeaderFile.setType("HEADER")
    micriumCpuCacheHeaderFile.setMarkup(False)

    micriumCpuCoreHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_CORE_H", None)
    micriumCpuCoreHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/cpu_core.h")
    micriumCpuCoreHeaderFile.setOutputName("cpu_core.h")
    micriumCpuCoreHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/")
    micriumCpuCoreHeaderFile.setProjectPath("MicriumOSIII/Software/uC-CPU/")
    micriumCpuCoreHeaderFile.setType("HEADER")
    micriumCpuCoreHeaderFile.setMarkup(False)

    micriumCpuDefHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_DEF_H", None)
    micriumCpuDefHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/cpu_def.h")
    micriumCpuDefHeaderFile.setOutputName("cpu_def.h")
    micriumCpuDefHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/")
    micriumCpuDefHeaderFile.setProjectPath("MicriumOSIII/Software/uC-CPU/")
    micriumCpuDefHeaderFile.setType("HEADER")
    micriumCpuDefHeaderFile.setMarkup(False)

    # Source: MicriumOSIII/Software/uC-LIB/
    micriumLibAsciiSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_ASCII_C", None)
    micriumLibAsciiSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_ascii.c")
    micriumLibAsciiSourceFile.setOutputName("lib_ascii.c")
    micriumLibAsciiSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibAsciiSourceFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibAsciiSourceFile.setType("SOURCE")
    micriumLibAsciiSourceFile.setMarkup(False)

    micriumLibMathSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_MATH_C", None)
    micriumLibMathSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_math.c")
    micriumLibMathSourceFile.setOutputName("lib_math.c")
    micriumLibMathSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibMathSourceFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibMathSourceFile.setType("SOURCE")
    micriumLibMathSourceFile.setMarkup(False)

    micriumLibStrSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_STR_C", None)
    micriumLibStrSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_str.c")
    micriumLibStrSourceFile.setOutputName("lib_str.c")
    micriumLibStrSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibStrSourceFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibStrSourceFile.setType("SOURCE")
    micriumLibStrSourceFile.setMarkup(False)

    micriumLibMemSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_MEM_C", None)
    micriumLibMemSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_mem.c")
    micriumLibMemSourceFile.setOutputName("lib_mem.c")
    micriumLibMemSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibMemSourceFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibMemSourceFile.setType("SOURCE")
    micriumLibMemSourceFile.setMarkup(False)

    # Header: MicriumOSIII/Software/uC-LIB/
    micriumLibAsciiHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_ASCII_H", None)
    micriumLibAsciiHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_ascii.h")
    micriumLibAsciiHeaderFile.setOutputName("lib_ascii.h")
    micriumLibAsciiHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibAsciiHeaderFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibAsciiHeaderFile.setType("HEADER")
    micriumLibAsciiHeaderFile.setMarkup(False)

    micriumLibDefHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_DEF_H", None)
    micriumLibDefHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_def.h")
    micriumLibDefHeaderFile.setOutputName("lib_def.h")
    micriumLibDefHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibDefHeaderFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibDefHeaderFile.setType("HEADER")
    micriumLibDefHeaderFile.setMarkup(False)

    micriumLibMathHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_MATH_H", None)
    micriumLibMathHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_math.h")
    micriumLibMathHeaderFile.setOutputName("lib_math.h")
    micriumLibMathHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibMathHeaderFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibMathHeaderFile.setType("HEADER")
    micriumLibMathHeaderFile.setMarkup(False)

    micriumLibMemHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_MEM_H", None)
    micriumLibMemHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_mem.h")
    micriumLibMemHeaderFile.setOutputName("lib_mem.h")
    micriumLibMemHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibMemHeaderFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibMemHeaderFile.setType("HEADER")
    micriumLibMemHeaderFile.setMarkup(False)

    micriumLibStrHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_STR_H", None)
    micriumLibStrHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/lib_str.h")
    micriumLibStrHeaderFile.setOutputName("lib_str.h")
    micriumLibStrHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB")
    micriumLibStrHeaderFile.setProjectPath("MicriumOSIII/Software/uC-LIB")
    micriumLibStrHeaderFile.setType("HEADER")
    micriumLibStrHeaderFile.setMarkup(False)

    # Source: MicriumOSIII/Software/uCOS-III/Source
    micriumOsCfgAppSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_CFG_APP_C", None)
    micriumOsCfgAppSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_cfg_app.c")
    micriumOsCfgAppSourceFile.setOutputName("os_cfg_app.c")
    micriumOsCfgAppSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsCfgAppSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsCfgAppSourceFile.setType("SOURCE")
    micriumOsCfgAppSourceFile.setMarkup(False)

    micriumOsCoreSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_CORE_C", None)
    micriumOsCoreSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_core.c")
    micriumOsCoreSourceFile.setOutputName("os_core.c")
    micriumOsCoreSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsCoreSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsCoreSourceFile.setType("SOURCE")
    micriumOsCoreSourceFile.setMarkup(False)

    micriumOsDbgSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_DBG_C", None)
    micriumOsDbgSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_dbg.c")
    micriumOsDbgSourceFile.setOutputName("os_dbg.c")
    micriumOsDbgSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsDbgSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsDbgSourceFile.setType("SOURCE")
    micriumOsDbgSourceFile.setMarkup(False)

    micriumOsFlagSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_FLAG_C", None)
    micriumOsFlagSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_flag.c")
    micriumOsFlagSourceFile.setOutputName("os_flag.c")
    micriumOsFlagSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsFlagSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsFlagSourceFile.setType("SOURCE")
    micriumOsFlagSourceFile.setMarkup(False)

    micriumOsMemSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_MEM_C", None)
    micriumOsMemSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_mem.c")
    micriumOsMemSourceFile.setOutputName("os_mem.c")
    micriumOsMemSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsMemSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsMemSourceFile.setType("SOURCE")
    micriumOsMemSourceFile.setMarkup(False)

    micriumOsMsgSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_MSG_C", None)
    micriumOsMsgSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_msg.c")
    micriumOsMsgSourceFile.setOutputName("os_msg.c")
    micriumOsMsgSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsMsgSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsMsgSourceFile.setType("SOURCE")
    micriumOsMsgSourceFile.setMarkup(False)

    micriumOsMutexSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_MUTEX_C", None)
    micriumOsMutexSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_mutex.c")
    micriumOsMutexSourceFile.setOutputName("os_mutex.c")
    micriumOsMutexSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsMutexSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsMutexSourceFile.setType("SOURCE")
    micriumOsMutexSourceFile.setMarkup(False)

    micriumOsPrioSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_PRIO_C", None)
    micriumOsPrioSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_prio.c")
    micriumOsPrioSourceFile.setOutputName("os_prio.c")
    micriumOsPrioSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsPrioSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsPrioSourceFile.setType("SOURCE")
    micriumOsPrioSourceFile.setMarkup(False)

    micriumOsQSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_Q_C", None)
    micriumOsQSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_q.c")
    micriumOsQSourceFile.setOutputName("os_q.c")
    micriumOsQSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsQSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsQSourceFile.setType("SOURCE")
    micriumOsQSourceFile.setMarkup(False)

    micriumOsSemSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_SEM_C", None)
    micriumOsSemSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_sem.c")
    micriumOsSemSourceFile.setOutputName("os_sem.c")
    micriumOsSemSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsSemSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsSemSourceFile.setType("SOURCE")
    micriumOsSemSourceFile.setMarkup(False)

    micriumOsStatSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_STAT_C", None)
    micriumOsStatSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_stat.c")
    micriumOsStatSourceFile.setOutputName("os_stat.c")
    micriumOsStatSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsStatSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsStatSourceFile.setType("SOURCE")
    micriumOsStatSourceFile.setMarkup(False)

    micriumOsTaskSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_TASK_C", None)
    micriumOsTaskSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_task.c")
    micriumOsTaskSourceFile.setOutputName("os_task.c")
    micriumOsTaskSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTaskSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTaskSourceFile.setType("SOURCE")
    micriumOsTaskSourceFile.setMarkup(False)

    micriumOsTickSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_TICK_C", None)
    micriumOsTickSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_tick.c")
    micriumOsTickSourceFile.setOutputName("os_tick.c")
    micriumOsTickSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTickSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTickSourceFile.setType("SOURCE")
    micriumOsTickSourceFile.setMarkup(False)

    micriumOsTimeSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_TIME_C", None)
    micriumOsTimeSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_time.c")
    micriumOsTimeSourceFile.setOutputName("os_time.c")
    micriumOsTimeSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTimeSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTimeSourceFile.setType("SOURCE")
    micriumOsTimeSourceFile.setMarkup(False)

    micriumOsTmrSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_TMR_C", None)
    micriumOsTmrSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_tmr.c")
    micriumOsTmrSourceFile.setOutputName("os_tmr.c")
    micriumOsTmrSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTmrSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTmrSourceFile.setType("SOURCE")
    micriumOsTmrSourceFile.setMarkup(False)

    micriumOsVarSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_VAR_C", None)
    micriumOsVarSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_var.c")
    micriumOsVarSourceFile.setOutputName("os_var.c")
    micriumOsVarSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsVarSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsVarSourceFile.setType("SOURCE")
    micriumOsVarSourceFile.setMarkup(False)

    # Header: MicriumOSIII/Software/uCOS-III/Source
    micriumOsHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_H", None)
    micriumOsHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os.h")
    micriumOsHeaderFile.setOutputName("os.h")
    micriumOsHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsHeaderFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsHeaderFile.setType("HEADER")
    micriumOsHeaderFile.setMarkup(False)

    micriumOsTraceHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_TRACE_H", None)
    micriumOsTraceHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_trace.h")
    micriumOsTraceHeaderFile.setOutputName("os_trace.h")
    micriumOsTraceHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTraceHeaderFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTraceHeaderFile.setType("HEADER")
    micriumOsTraceHeaderFile.setMarkup(False)

    micriumOsTypeHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_TYPE_H", None)
    micriumOsTypeHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Source/os_type.h")
    micriumOsTypeHeaderFile.setOutputName("os_type.h")
    micriumOsTypeHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTypeHeaderFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Source")
    micriumOsTypeHeaderFile.setType("HEADER")
    micriumOsTypeHeaderFile.setMarkup(False)

    micriumSystemDefFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_SYS_DEF", None)
    micriumSystemDefFile.setType("STRING")
    micriumSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    micriumSystemDefFile.setSourcePath("templates/system/definitions.h.ftl")
    micriumSystemDefFile.setMarkup(True)

    micriumSystemInit = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_INIT", None)
    micriumSystemInit.setType("STRING")
    micriumSystemInit.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    micriumSystemInit.setSourcePath("templates/system/initialization.c.ftl")
    micriumSystemInit.setMarkup(True)

    micriumSystemInitDef = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_INIT_DEF", None)
    micriumSystemInitDef.setType("STRING")
    micriumSystemInitDef.setOutputName("core.LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION")
    micriumSystemInitDef.setSourcePath("templates/system/initialization_definitions.c.ftl")
    micriumSystemInitDef.setMarkup(True)

    micriumSystemTasksFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_SYS_START_SCHED", None)
    micriumSystemTasksFile.setType("STRING")
    micriumSystemTasksFile.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_CALL_SCHEDULAR")
    micriumSystemTasksFile.setSourcePath("templates/system/start_rtos.c.ftl")
    micriumSystemTasksFile.setMarkup(True)

    micriumSystemTasks = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_SYS_TASKS", None)
    micriumSystemTasks.setType("STRING")
    micriumSystemTasks.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_GEN_APP")
    micriumSystemTasks.setSourcePath("templates/system/create_tasks.c.ftl")
    micriumSystemTasks.setMarkup(True)

    micriumSystemTasksDef = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_SYS_TASKS_DEF", None)
    micriumSystemTasksDef.setType("STRING")
    micriumSystemTasksDef.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS")
    micriumSystemTasksDef.setSourcePath("templates/system/tasks_macros.c.ftl")
    micriumSystemTasksDef.setMarkup(True)

    armArch     = Database.getSymbolValue("core", "CoreArchitecture")

    # load family specific configuration
    execfile(Module.getPath() + "config/arch/arm/devices_" + armArch.replace("-", "_").replace("PLUS", "").lower() + "/ucosIII_config.py")
