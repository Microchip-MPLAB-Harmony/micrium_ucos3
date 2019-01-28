/*
*********************************************************************************************************
*                                               uC/OS-III
*                                          The Real-Time Kernel
*
*                         (c) Copyright 2009-2018; Silicon Laboratories Inc.,
*                                400 W. Cesar Chavez, Austin, TX 78701
*
*                   All rights reserved. Protected by international copyright laws.
*
*                  Your use of this software is subject to your acceptance of the terms
*                  of a Silicon Labs Micrium software license, which can be obtained by
*                  contacting info@micrium.com. If you do not agree to the terms of this
*                  license, you may not use this software.
*
*                  Please help us continue to provide the Embedded community with the finest
*                  software available. Your honesty is greatly appreciated.
*
*                    You can find our product's documentation at: doc.micrium.com
*
*                          For more information visit us at: www.micrium.com
*********************************************************************************************************
*/

/*
*********************************************************************************************************
*
*                               OS CONFIGURATION (APPLICATION SPECIFICS)
*
* Filename : os_cfg_app.h
* Version  : V3.07.03
*********************************************************************************************************
*/

#ifndef OS_CFG_APP_H
#define OS_CFG_APP_H

/*
************************************************************************************************************************
*                                                      CONSTANTS
************************************************************************************************************************
*/

                                          /* --------------------- MISCELLANEOUS ------------------ */
#define  OS_CFG_MSG_POOL_SIZE             ${UCOSIII_CFG_MSG_POOL_SIZE}u              <#lt>   /* Maximum number of messages                             */

#define  OS_CFG_ISR_STK_SIZE              ${UCOSIII_CFG_ISR_STK_SIZE}u               <#lt>   /* Stack size of ISR stack (number of CPU_STK elements)   */

#define  OS_CFG_TASK_STK_LIMIT_PCT_EMPTY  ${UCOSIII_CFG_TASK_STK_LIMIT_PCT_EMPTY}u   <#lt>   /* Stack limit position in percentage to empty            */


                                          /* ---------------------- IDLE TASK --------------------- */
#define  OS_CFG_IDLE_TASK_STK_SIZE        ${UCOSIII_CFG_IDLE_TASK_STK_SIZE}u         <#lt>   /* Stack size (number of CPU_STK elements)                */


                                          /* ------------------- STATISTIC TASK ------------------- */
#define  OS_CFG_STAT_TASK_PRIO            ${UCOSIII_CFG_PRIO_MAX}-2u                 <#lt>   /* Priority                                               */
#define  OS_CFG_STAT_TASK_RATE_HZ         ${UCOSIII_CFG_STAT_TASK_RATE_HZ}u          <#lt>   /* Rate of execution (10 Hz Typ.)                         */
#define  OS_CFG_STAT_TASK_STK_SIZE        ${UCOSIII_CFG_STAT_TASK_STK_SIZE}u         <#lt>   /* Stack size (number of CPU_STK elements)                */


                                          /* ------------------------ TICKS ----------------------- */
#define  OS_CFG_TICK_RATE_HZ              ${UCOSIII_CFG_TICK_RATE_HZ}u               <#lt>   /* Tick rate in Hertz (10 to 1000 Hz)                     */


                                          /* ----------------------- TIMERS ----------------------- */
#define  OS_CFG_TMR_TASK_PRIO             ${UCOSIII_CFG_PRIO_MAX}-3u                 <#lt>   /* Priority of 'Timer Task'                               */
#define  OS_CFG_TMR_TASK_STK_SIZE         ${UCOSIII_CFG_TMR_TASK_STK_SIZE}u          <#lt>   /* Stack size (number of CPU_STK elements)                */

#define  OS_CFG_TMR_TASK_RATE_HZ          ${UCOSIII_CFG_TMR_TASK_RATE_HZ}u           <#lt>   /* DEPRECATED - Rate for timers (10 Hz Typ.)              */
                                                                                             /* The timer task now calculates its timeouts based       */
                                                                                             /* on the timers in the list. It no longer runs at a      */
                                                                                             /* static frequency.                                      */
                                                                                             /* This define is included for compatibility reasons.     */
                                                                                             /* It will determine the period of a timer tick.          */
                                                                                             /* We recommend setting it to OS_CFG_TICK_RATE_HZ         */
                                                                                             /* for new projects.                                      */
#endif

