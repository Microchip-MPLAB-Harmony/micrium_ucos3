<#list 0..(HarmonyCore.GEN_APP_TASK_COUNT - 1) as i>
    <#assign GEN_APP_TASK_NAME_STR = "HarmonyCore.GEN_APP_TASK_NAME_" + i>
    <#assign GEN_APP_TASK_NAME = GEN_APP_TASK_NAME_STR?eval>
    <#assign GEN_APP_RTOS_TASK_USE_DELAY_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_USE_DELAY">
    <#assign GEN_APP_RTOS_TASK_USE_DELAY = GEN_APP_RTOS_TASK_USE_DELAY_STR?eval>
    <#assign GEN_APP_RTOS_TASK_DELAY_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_DELAY">
    <#assign GEN_APP_RTOS_TASK_DELAY = GEN_APP_RTOS_TASK_DELAY_STR?eval>
    <#assign GEN_APP_RTOS_TASK_SIZE_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_SIZE">
    <#assign GEN_APP_RTOS_TASK_SIZE = GEN_APP_RTOS_TASK_SIZE_STR?eval>
    <#if HarmonyCore.SELECT_RTOS == "MicriumOSIII">
        <#lt>/* Handle for the ${GEN_APP_TASK_NAME?upper_case}_Tasks. */
        <#lt>OS_TCB  _${GEN_APP_TASK_NAME?upper_case}_Tasks_TCB;
        <#lt>CPU_STK _${GEN_APP_TASK_NAME?upper_case}_TasksStk[${GEN_APP_RTOS_TASK_SIZE}];

        <#lt>void _${GEN_APP_TASK_NAME?upper_case}_Tasks(  void *pvParameters  )
        <#lt>{
        <#if GEN_APP_RTOS_TASK_USE_DELAY == true>
        <#lt>    OS_ERR os_err;
        </#if>
        <#lt>    while(1)
        <#lt>    {
        <#lt>        ${GEN_APP_TASK_NAME?upper_case}_Tasks();
        <#if GEN_APP_RTOS_TASK_USE_DELAY == true>
        <#lt>        OSTimeDly(${GEN_APP_RTOS_TASK_DELAY} , OS_OPT_TIME_DLY, &os_err);
        </#if>
        <#lt>    }
        <#lt>}
    </#if>
</#list>