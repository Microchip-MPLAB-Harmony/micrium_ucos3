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

############################################################################
############### Cortex-M7 Architecture specific configuration ##############
############################################################################

#Set SysTick Priority and Lock the Priority
SysTickInterruptIndex        = Interrupt.getInterruptIndex("SysTick")
SysTickInterruptPriority     = "NVIC_"+ str(SysTickInterruptIndex) +"_0_PRIORITY"
SysTickInterruptPriorityLock = "NVIC_" + str(SysTickInterruptIndex) +"_0_PRIORITY_LOCK"

Database.clearSymbolValue("core", SysTickInterruptPriority)
Database.setSymbolValue("core", SysTickInterruptPriority, "7", 2)
Database.clearSymbolValue("core", SysTickInterruptPriorityLock)
Database.setSymbolValue("core", SysTickInterruptPriorityLock, True, 2)


############################################################################
#### Code Generation ####
############################################################################

configName  = Variables.get("__CONFIGURATION_NAME")

micriumCpuArmV7AsmSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_ARMV7_S", None)
micriumCpuArmV7AsmSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/GNU/cpu_a.S")
micriumCpuArmV7AsmSourceFile.setOutputName("cpu_a.S")
micriumCpuArmV7AsmSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M")
micriumCpuArmV7AsmSourceFile.setProjectPath("MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M")
micriumCpuArmV7AsmSourceFile.setType("SOURCE")
micriumCpuArmV7AsmSourceFile.setMarkup(False)

# Source: MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M
micriumCpuArmV7SourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_ARMV7_C", None)
micriumCpuArmV7SourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/cpu_c.c")
micriumCpuArmV7SourceFile.setOutputName("cpu_c.c")
micriumCpuArmV7SourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M")
micriumCpuArmV7SourceFile.setProjectPath("MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M")
micriumCpuArmV7SourceFile.setType("SOURCE")
micriumCpuArmV7SourceFile.setMarkup(False)

# Header: MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/GNU
micriumCpuArmV7HeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_CPU_ARMV7_H", None)
micriumCpuArmV7HeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/GNU/cpu.h")
micriumCpuArmV7HeaderFile.setOutputName("cpu.h")
micriumCpuArmV7HeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/GNU")
micriumCpuArmV7HeaderFile.setProjectPath("MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/GNU")
micriumCpuArmV7HeaderFile.setType("HEADER")
micriumCpuArmV7HeaderFile.setMarkup(False)

# Source: MicriumOSIII/Software/uC-LIB/Ports/ARM-Cortex-M4/
micriumLibMemAsmSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_LIB_ARM_CORTEX_M4_MEM_S", None)
micriumLibMemAsmSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uC-LIB/Ports/ARM-Cortex-M4/GNU/lib_mem_a.S")
micriumLibMemAsmSourceFile.setOutputName("lib_mem_a.S")
micriumLibMemAsmSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uC-LIB/Ports/ARM-Cortex-M4")
micriumLibMemAsmSourceFile.setProjectPath("MicriumOSIII/Software/uC-LIB/Ports/ARM-Cortex-M4")
micriumLibMemAsmSourceFile.setType("SOURCE")
micriumLibMemAsmSourceFile.setMarkup(False)
micriumLibMemAsmSourceFile.setEnabled(False)

# Source: MicriumOSIII/Software/uCOS-III/Source/Ports/ARM-Cortex-M/ARMv7-M
micriumOsCpuSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_CPU_C", None)
micriumOsCpuSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/os_cpu_c.c")
micriumOsCpuSourceFile.setOutputName("os_cpu_c.c")
micriumOsCpuSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/")
micriumOsCpuSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M")
micriumOsCpuSourceFile.setType("SOURCE")
micriumOsCpuSourceFile.setMarkup(False)

# Source: MicriumOSIII/Software/uCOS-III/Source/Ports/ARM-Cortex-M/ARMv7-M/GNU
micriumOsCpuAsmSourceFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_CPU_S", None)
micriumOsCpuAsmSourceFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU/os_cpu_a.S")
micriumOsCpuAsmSourceFile.setOutputName("os_cpu_a.S")
micriumOsCpuAsmSourceFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU")
micriumOsCpuAsmSourceFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU")
micriumOsCpuAsmSourceFile.setType("SOURCE")
micriumOsCpuAsmSourceFile.setMarkup(False)

# Header: MicriumOSIII/Software/uCOS-III/Source/Ports/ARM-Cortex-M/ARMv7-M/GNU
micriumOsCpuHeaderFile = thirdPartyMicriumOSIII.createFileSymbol("UCOSIII_OS_CPU_H", None)
micriumOsCpuHeaderFile.setSourcePath("../thirdparty_micrium/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU/os_cpu.h")
micriumOsCpuHeaderFile.setOutputName("os_cpu.h")
micriumOsCpuHeaderFile.setDestPath("../../third_party/rtos/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU")
micriumOsCpuHeaderFile.setProjectPath("MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU")
micriumOsCpuHeaderFile.setType("HEADER")
micriumOsCpuHeaderFile.setMarkup(False)

# Update C32 Include directories path
micriumOsXc32SettingSym = thirdPartyMicriumOSIII.createSettingSymbol("UCOSIII_OS_XC32_INCLUDE_DIRS", None)
micriumOsXc32SettingSym.setCategory("C32")
micriumOsXc32SettingSym.setKey("extra-include-directories")
micriumOsXc32SettingSym.setValue("../src/config/" + configName + "/micrium_config;../src/third_party/rtos/MicriumOSIII/Software/uC-CPU/;../src/third_party/rtos/MicriumOSIII/Software/uC-CPU/ARM-Cortex-M/ARMv7-M/GNU;../src/third_party/rtos/MicriumOSIII/Software/uC-LIB;../src/third_party/rtos/MicriumOSIII/Software/uCOS-III/Source;../src/third_party/rtos/MicriumOSIII/Software/uCOS-III/Ports/ARM-Cortex-M/ARMv7-M/GNU;")
micriumOsXc32SettingSym.setAppend(True, ";")
