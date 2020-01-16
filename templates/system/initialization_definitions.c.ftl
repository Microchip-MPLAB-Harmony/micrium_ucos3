<#if core.CoreArchitecture == "CORTEX-M0PLUS">
/*******************************************************************************
  Function:
    void  OS_CPU_SysTickInitFreq (CPU_INT32U cpuFrequency)

  Summary:
    Determine nbr SysTick increments and Init uC/OS periodic time src (SysTick).

  Remarks:
 */
void  OS_CPU_SysTickInitFreq (CPU_INT32U cpuFrequency)
{
    CPU_INT32U  cnts;

    cnts = cpuFrequency / (CPU_INT32U)OSCfg_TickRate_Hz;        /* Determine nbr SysTick increments. */

    OS_CPU_SysTickInit(cnts);                                   /* Init uC/OS periodic time src (SysTick). */
}
</#if>

/*******************************************************************************
  Function:
    void MICRIUM_UCOS3_Initialize ( void )

  Summary:
    Initializes the SysTick using CPU Clock Frequency, CPU module and the
    internals of uC/OS-III. This function MUST be called prior to creating any
    uC/OS-III object and, prior to calling OSStart().

  Remarks:
 */
void MICRIUM_UCOS3_Initialize( void )
{
    OS_ERR os_err;

    OS_CPU_SysTickInitFreq(${core.CPU_CLOCK_FREQUENCY});

    CPU_Init();

    OSInit(&os_err);
}