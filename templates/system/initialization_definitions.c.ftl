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