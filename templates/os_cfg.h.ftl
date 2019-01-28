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
*                                          CONFIGURATION FILE
*
* Filename : os_cfg.h
* Version  : V3.07.03
*********************************************************************************************************
*/

#ifndef OS_CFG_H
#define OS_CFG_H

                                          /* ---------------------------- MISCELLANEOUS -------------------------- */
#define OS_CFG_APP_HOOKS_EN               <#if UCOSIII_CFG_APP_HOOKS_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>            <#lt>   /* Enable (DEF_ENABLED) application specific hooks                        */
#define OS_CFG_ARG_CHK_EN                 <#if UCOSIII_CFG_ARG_CHK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>              <#lt>   /* Enable (DEF_ENABLED) argument checking                                 */
#define OS_CFG_CALLED_FROM_ISR_CHK_EN     <#if UCOSIII_CFG_CALLED_FROM_ISR_CHK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>  <#lt>   /* Enable (DEF_ENABLED) check for called from ISR                         */
#define OS_CFG_DBG_EN                     <#if UCOSIII_CFG_DBG_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                  <#lt>   /* Enable (DEF_ENABLED) debug code/variables                              */
#define OS_CFG_TICK_EN                    <#if UCOSIII_CFG_TICK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                 <#lt>   /* Enable (DEF_ENABLED) the kernel tick                                   */
#define OS_CFG_DYN_TICK_EN                <#if UCOSIII_CFG_DYN_TICK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>             <#lt>   /* Enable (DEF_ENABLED) the Dynamic Tick                                  */
#define OS_CFG_INVALID_OS_CALLS_CHK_EN    <#if UCOSIII_CFG_INVALID_OS_CALLS_CHK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if> <#lt>   /* Enable (DEF_ENABLED) checks for invalid kernel calls                   */
#define OS_CFG_OBJ_TYPE_CHK_EN            <#if UCOSIII_CFG_OBJ_TYPE_CHK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>         <#lt>   /* Enable (DEF_ENABLED) object type checking                              */
#define OS_CFG_TS_EN                      <#if UCOSIII_CFG_TS_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                   <#lt>   /* Enable (DEF_ENABLED) time stamping                                     */

#define OS_CFG_PRIO_MAX                   ${UCOSIII_CFG_PRIO_MAX}u                                                              <#lt>   /* Defines the maximum number of task priorities (see OS_PRIO data type)  */

#define OS_CFG_SCHED_LOCK_TIME_MEAS_EN    <#if UCOSIII_CFG_SCHED_LOCK_TIME_MEAS_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if> <#lt>   /* Include (DEF_ENABLED) code to measure scheduler lock time              */
#define OS_CFG_SCHED_ROUND_ROBIN_EN       <#if UCOSIII_CFG_SCHED_ROUND_ROBIN_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>    <#lt>   /* Include (DEF_ENABLED) code for Round-Robin scheduling                  */

#define OS_CFG_STK_SIZE_MIN               ${UCOSIII_CFG_STK_SIZE_MIN}u                                                          <#lt>   /* Minimum allowable task stack size                                      */


                                          /* ----------------------------- EVENT FLAGS --------------------------- */
#define OS_CFG_FLAG_EN                    <#if UCOSIII_CFG_FLAG_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                 <#lt>   /* Enable (DEF_ENABLED) code generation for EVENT FLAGS                   */
#define OS_CFG_FLAG_DEL_EN                <#if UCOSIII_CFG_FLAG_DEL_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>             <#lt>   /*     Include (DEF_ENABLED) code for OSFlagDel()                         */
#define OS_CFG_FLAG_MODE_CLR_EN           <#if UCOSIII_CFG_FLAG_MODE_CLR_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>        <#lt>   /*     Include (DEF_ENABLED) code for Wait on Clear EVENT FLAGS           */
#define OS_CFG_FLAG_PEND_ABORT_EN         <#if UCOSIII_CFG_FLAG_PEND_ABORT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>      <#lt>   /*     Include (DEF_ENABLED) code for OSFlagPendAbort()                   */


                                          /* -------------------------- MEMORY MANAGEMENT ------------------------ */
#define OS_CFG_MEM_EN                     <#if UCOSIII_CFG_MEM_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                  <#lt>   /* Enable (DEF_ENABLED) code generation for MEMORY MANAGER                */


                                          /* --------------------- MUTUAL EXCLUSION SEMAPHORES ------------------- */
#define OS_CFG_MUTEX_EN                   <#if UCOSIII_CFG_MUTEX_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                <#lt>   /* Enable (DEF_ENABLED) code generation for MUTEX                         */
#define OS_CFG_MUTEX_DEL_EN               <#if UCOSIII_CFG_MUTEX_DEL_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>            <#lt>   /*     Include (DEF_ENABLED) code for OSMutexDel()                        */
#define OS_CFG_MUTEX_PEND_ABORT_EN        <#if UCOSIII_CFG_MUTEX_PEND_ABORT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>     <#lt>   /*     Include (DEF_ENABLED) code for OSMutexPendAbort()                  */


                                          /* --------------------------- MESSAGE QUEUES -------------------------- */
#define OS_CFG_Q_EN                       <#if UCOSIII_CFG_Q_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                    <#lt>   /* Enable (DEF_ENABLED) code generation for QUEUES                        */
#define OS_CFG_Q_DEL_EN                   <#if UCOSIII_CFG_Q_DEL_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                <#lt>   /*     Include (DEF_ENABLED) code for OSQDel()                            */
#define OS_CFG_Q_FLUSH_EN                 <#if UCOSIII_CFG_Q_FLUSH_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>              <#lt>   /*     Include (DEF_ENABLED) code for OSQFlush()                          */
#define OS_CFG_Q_PEND_ABORT_EN            <#if UCOSIII_CFG_Q_PEND_ABORT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>         <#lt>   /*     Include (DEF_ENABLED) code for OSQPendAbort()                      */


                                          /* ----------------------------- SEMAPHORES ---------------------------- */
#define OS_CFG_SEM_EN                     <#if UCOSIII_CFG_SEM_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                  <#lt>   /* Enable (DEF_ENABLED) code generation for SEMAPHORES                    */
#define OS_CFG_SEM_DEL_EN                 <#if UCOSIII_CFG_SEM_DEL_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>              <#lt>   /*    Include code (DEF_ENABLED) for OSSemDel()                           */
#define OS_CFG_SEM_PEND_ABORT_EN          <#if UCOSIII_CFG_SEM_PEND_ABORT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>       <#lt>   /*    Include code (DEF_ENABLED) for OSSemPendAbort()                     */
#define OS_CFG_SEM_SET_EN                 <#if UCOSIII_CFG_SEM_SET_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>              <#lt>   /*    Include code (DEF_ENABLED) for OSSemSet()                           */


                                          /* -------------------------- TASK MANAGEMENT -------------------------- */
#define OS_CFG_STAT_TASK_EN               <#if UCOSIII_CFG_STAT_TASK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>            <#lt>   /* Enable (DEF_ENABLED) the statistics task                               */
#define OS_CFG_STAT_TASK_STK_CHK_EN       <#if UCOSIII_CFG_STAT_TASK_STK_CHK_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>    <#lt>   /*    Check task stacks from statistic task                               */

#define OS_CFG_TASK_CHANGE_PRIO_EN        <#if UCOSIII_CFG_TASK_CHANGE_PRIO_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>     <#lt>   /* Include code (DEF_ENABLED) for OSTaskChangePrio()                      */
#define OS_CFG_TASK_DEL_EN                <#if UCOSIII_CFG_TASK_DEL_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>             <#lt>   /* Include code (DEF_ENABLED) for OSTaskDel()                             */
#define OS_CFG_TASK_IDLE_EN               <#if UCOSIII_CFG_TASK_IDLE_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>            <#lt>   /* Include code (DEF_ENABLED) the idle task                               */
#define OS_CFG_TASK_PROFILE_EN            <#if UCOSIII_CFG_TASK_PROFILE_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>         <#lt>   /* Include variables in OS_TCB for profiling                              */
#define OS_CFG_TASK_Q_EN                  <#if UCOSIII_CFG_TASK_Q_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>               <#lt>   /* Include code (DEF_ENABLED) for OSTaskQXXXX()                           */
#define OS_CFG_TASK_Q_PEND_ABORT_EN       <#if UCOSIII_CFG_TASK_Q_PEND_ABORT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>    <#lt>   /* Include code (DEF_ENABLED) for OSTaskQPendAbort()                      */
#define OS_CFG_TASK_REG_TBL_SIZE          ${UCOSIII_CFG_TASK_REG_TBL_SIZE}u                                                     <#lt>   /* Number of task specific registers                                      */
#define OS_CFG_TASK_STK_REDZONE_EN        <#if UCOSIII_CFG_TASK_STK_REDZONE_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>     <#lt>   /* Enable (DEF_ENABLED) stack redzone                                     */
#define OS_CFG_TASK_STK_REDZONE_DEPTH     ${UCOSIII_CFG_TASK_STK_REDZONE_DEPTH}u                                                <#lt>   /* Depth of the stack redzone                                             */
#define OS_CFG_TASK_SEM_PEND_ABORT_EN     <#if UCOSIII_CFG_TASK_SEM_PEND_ABORT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>  <#lt>   /* Include code (DEF_ENABLED) for OSTaskSemPendAbort()                    */
#define OS_CFG_TASK_SUSPEND_EN            <#if UCOSIII_CFG_TASK_SUSPEND_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>         <#lt>   /* Include code (DEF_ENABLED) for OSTaskSuspend() and OSTaskResume()      */


                                          /* ------------------ TASK LOCAL STORAGE MANAGEMENT -------------------  */
#define OS_CFG_TLS_TBL_SIZE               ${UCOSIII_CFG_TLS_TBL_SIZE}u                                                          <#lt>   /* Include (DEF_ENABLED) code for Task Local Storage (TLS) registers      */



                                          /* -------------------------- TIME MANAGEMENT -------------------------- */
#define OS_CFG_TIME_DLY_HMSM_EN           <#if UCOSIII_CFG_TIME_DLY_HMSM_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>        <#lt>   /*     Include code (DEF_ENABLED) for OSTimeDlyHMSM()                     */
#define OS_CFG_TIME_DLY_RESUME_EN         <#if UCOSIII_CFG_TIME_DLY_RESUME_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>      <#lt>   /*     Include code (DEF_ENABLED) for OSTimeDlyResume()                   */


                                          /* ------------------------- TIMER MANAGEMENT -------------------------- */
#define OS_CFG_TMR_EN                     <#if UCOSIII_CFG_TMR_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                  <#lt>   /* Enable (DEF_ENABLED) code generation for TIMERS                        */
#define OS_CFG_TMR_DEL_EN                 <#if UCOSIII_CFG_TMR_DEL_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>              <#lt>   /* Enable (DEF_ENABLED) code generation for OSTmrDel()                    */


                                          /* ------------------------- TRACE RECORDER ---------------------------- */
#define OS_CFG_TRACE_EN                   <#if UCOSIII_CFG_TRACE_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>                <#lt>   /* Enable (DEF_ENABLED) uC/OS-III Trace instrumentation                   */
#define OS_CFG_TRACE_API_ENTER_EN         <#if UCOSIII_CFG_TRACE_API_ENTER_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>      <#lt>   /* Enable (DEF_ENABLED) uC/OS-III Trace API enter instrumentation         */
#define OS_CFG_TRACE_API_EXIT_EN          <#if UCOSIII_CFG_TRACE_API_EXIT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>       <#lt>   /* Enable (DEF_ENABLED) uC/OS-III Trace API exit  instrumentation         */
#endif

