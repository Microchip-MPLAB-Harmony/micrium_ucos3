
# Microchip MPLAB Harmony configurations and applications for Micrium OS-III Release Notes
## Release v3.2.0
### NEW FEATURES
- **New part support** - This release introduces initial support for [SAM E54](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus), [SAM E70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus) families of 32-bit microcontrollers.
- Supports **Micrium OS-III Version** - v3.07.03 (not included and must be downloaded separately)
- **Development kit and demo application support** - The following table provides number of Micrium OS-III demo application available for different development kits.

| Development kits | Applications |
| --- | --- |
| [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsame54-xpro) | 1 |
| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | 1 |

### KNOWN ISSUES

The current known issues are as follows:

- Programming and debugging through EDBG is not supported for SAM E54, need to use external debugger (ICD4).
- Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).  Please see the &quot;Configuring the Library&quot; section in the help documentation in the doc folder for this module instead.  Help is available in both CHM and PDF formats.

### DEVELOPMENT TOOLS

- [MPLAB X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
- MPLAB X IDE plug-ins: MPLAB Harmony Configurator (MHC) v3.2.0.0
