<#list 0..(HarmonyCore.GEN_APP_TASK_COUNT - 1) as i>
    <#assign GEN_APP_TASK_NAME_STR = "HarmonyCore.GEN_APP_TASK_NAME_" + i>
    <#assign GEN_APP_TASK_NAME = GEN_APP_TASK_NAME_STR?eval>
    <#assign GEN_APP_RTOS_TASK_SIZE_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_SIZE">
    <#assign GEN_APP_RTOS_TASK_SIZE = GEN_APP_RTOS_TASK_SIZE_STR?eval>
    <#assign GEN_APP_RTOS_TASK_PRIO_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_PRIO">
    <#assign GEN_APP_RTOS_TASK_PRIO = GEN_APP_RTOS_TASK_PRIO_STR?eval>
    <#assign GEN_APP_RTOS_TASK_MSG_QTY_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_MSG_QTY">
    <#assign GEN_APP_RTOS_TASK_MSG_QTY = GEN_APP_RTOS_TASK_MSG_QTY_STR?eval>
    <#assign GEN_APP_RTOS_TASK_TIME_QUANTA_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_TIME_QUANTA">
    <#assign GEN_APP_RTOS_TASK_TIME_QUANTA = GEN_APP_RTOS_TASK_TIME_QUANTA_STR?eval>
    <#assign GEN_APP_RTOS_TASK_OPT_NONE_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_OPT_NONE">
    <#assign GEN_APP_RTOS_TASK_OPT_NONE = GEN_APP_RTOS_TASK_OPT_NONE_STR?eval>
    <#assign GEN_APP_RTOS_TASK_OPT_STK_CHK_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_OPT_STK_CHK">
    <#assign GEN_APP_RTOS_TASK_OPT_STK_CHK = GEN_APP_RTOS_TASK_OPT_STK_CHK_STR?eval>
    <#assign GEN_APP_RTOS_TASK_OPT_STK_CLR_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_OPT_STK_CLR">
    <#assign GEN_APP_RTOS_TASK_OPT_STK_CLR = GEN_APP_RTOS_TASK_OPT_STK_CLR_STR?eval>
    <#assign GEN_APP_RTOS_TASK_OPT_SAVE_FP_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_OPT_SAVE_FP">
    <#assign GEN_APP_RTOS_TASK_OPT_SAVE_FP = GEN_APP_RTOS_TASK_OPT_SAVE_FP_STR?eval>
    <#assign GEN_APP_RTOS_TASK_OPT_NO_TLS_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_OPT_NO_TLS">
    <#assign GEN_APP_RTOS_TASK_OPT_NO_TLS = GEN_APP_RTOS_TASK_OPT_NO_TLS_STR?eval>
    <#assign GEN_APP_RTOS_TASK_OPTIONS = "OS_OPT_TASK_NONE" + GEN_APP_RTOS_TASK_OPT_STK_CHK?then(' | OS_OPT_TASK_STK_CHK', '') + GEN_APP_RTOS_TASK_OPT_STK_CLR?then(' | OS_OPT_TASK_STK_CLR', '') + GEN_APP_RTOS_TASK_OPT_SAVE_FP?then(' | OS_OPT_TASK_SAVE_FP', '') + GEN_APP_RTOS_TASK_OPT_NO_TLS?then(' | OS_OPT_TASK_NO_TLS', '')>

    <#if HarmonyCore.SELECT_RTOS == "MicriumOSIII">
    <#lt>    /* Create OS Thread for ${GEN_APP_TASK_NAME?upper_case}_Tasks. */
    <#lt>    OSTaskCreate((OS_TCB      *)&_${GEN_APP_TASK_NAME?upper_case}_Tasks_TCB,
    <#lt>                 (CPU_CHAR    *)"${GEN_APP_TASK_NAME?upper_case}_Tasks",
    <#lt>                 (OS_TASK_PTR  )_${GEN_APP_TASK_NAME?upper_case}_Tasks,
    <#lt>                 (void        *)0,
    <#lt>                 (OS_PRIO      )${GEN_APP_RTOS_TASK_PRIO},
    <#lt>                 (CPU_STK     *)&_${GEN_APP_TASK_NAME?upper_case}_TasksStk[0],
    <#lt>                 (CPU_STK_SIZE )0u,
    <#lt>                 (CPU_STK_SIZE )${GEN_APP_RTOS_TASK_SIZE},
    <#if UCOSIII_CFG_TASK_Q_EN == true>
    <#lt>                 (OS_MSG_QTY   )${GEN_APP_RTOS_TASK_MSG_QTY}u,
    <#else>
    <#lt>                 (OS_MSG_QTY   )0u,
    </#if>
    <#if UCOSIII_CFG_SCHED_ROUND_ROBIN_EN == true>
    <#lt>                 (OS_TICK      )${GEN_APP_RTOS_TASK_TIME_QUANTA}u,
    <#else>
    <#lt>                 (OS_TICK      )0u,
    </#if>
    <#lt>                 (void        *)0,
    <#lt>                 (OS_OPT       )(${GEN_APP_RTOS_TASK_OPTIONS}),
    <#lt>                 (OS_ERR      *)&os_err);
    </#if>
</#list>