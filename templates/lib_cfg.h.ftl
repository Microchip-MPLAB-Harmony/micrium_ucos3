/*
*********************************************************************************************************
*                                            EXAMPLE CODE
*
*               This file is provided as an example on how to use Micrium products.
*
*               Please feel free to use any application code labeled as 'EXAMPLE CODE' in
*               your application products.  Example code may be used as is, in whole or in
*               part, or may be used as a reference only. This file can be modified as
*               required to meet the end-product requirements.
*
*               Please help us continue to provide the Embedded community with the finest
*               software available.  Your honesty is greatly appreciated.
*
*               You can find information about uC/LIB by visiting doc.micrium.com.
*               You can contact us at: www.micrium.com
*********************************************************************************************************
*/

/*
*********************************************************************************************************
*
*                                  CUSTOM LIBRARY CONFIGURATION FILE
*
*                                              TEMPLATE
*
* Filename      : lib_cfg.h
* Version       : V1.38.02.00
* Programmer(s) : FBJ
*                 JFD
*********************************************************************************************************
*/


/*
*********************************************************************************************************
*                                               MODULE
*********************************************************************************************************
*/

#ifndef  LIB_CFG_MODULE_PRESENT
#define  LIB_CFG_MODULE_PRESENT


/*
*********************************************************************************************************
*********************************************************************************************************
*                                    MEMORY LIBRARY CONFIGURATION
*********************************************************************************************************
*********************************************************************************************************
*/

/*
*********************************************************************************************************
*                             MEMORY LIBRARY ARGUMENT CHECK CONFIGURATION
*
* Note(s) : (1) Configure LIB_MEM_CFG_ARG_CHK_EXT_EN to enable/disable the memory library suite external
*               argument check feature :
*
*               (a) When ENABLED,      arguments received from any port interface provided by the developer
*                   or application are checked/validated.
*
*               (b) When DISABLED, NO  arguments received from any port interface provided by the developer
*                   or application are checked/validated.
*********************************************************************************************************
*/

                                                        /* Configure external argument check feature (see Note #1) :    */
#define  LIB_MEM_CFG_ARG_CHK_EXT_EN     <#if UCOSIII_LIB_MEM_CFG_ARG_CHK_EXT_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>
                                                        /*   DEF_DISABLED     Argument check DISABLED                   */
                                                        /*   DEF_ENABLED      Argument check ENABLED                    */


/*
*********************************************************************************************************
*                         MEMORY LIBRARY ASSEMBLY OPTIMIZATION CONFIGURATION
*
* Note(s) : (1) Configure LIB_MEM_CFG_OPTIMIZE_ASM_EN to enable/disable assembly-optimized memory function(s).
*********************************************************************************************************
*/

                                                        /* Configure assembly-optimized function(s) [see Note #1] :     */
#define  LIB_MEM_CFG_OPTIMIZE_ASM_EN    <#if UCOSIII_LIB_MEM_CFG_OPTIMIZE_ASM_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>
                                                        /*   DEF_DISABLED     Assembly-optimized function(s) DISABLED   */
                                                        /*   DEF_ENABLED      Assembly-optimized function(s) ENABLED    */


/*
*********************************************************************************************************
*                                   MEMORY ALLOCATION CONFIGURATION
*
* Note(s) : (1) Configure LIB_MEM_CFG_ALLOC_EN to enable/disable memory allocation functions.
*
*           (2) (a) Configure LIB_MEM_CFG_HEAP_SIZE with the desired size of heap memory (in octets).
*
*               (b) Configure LIB_MEM_CFG_HEAP_BASE_ADDR to specify a base address for heap memory :
*
*                   (a) Heap initialized to specified application memory,  if LIB_MEM_CFG_HEAP_BASE_ADDR
*                                                                                 #define'd in 'app_cfg.h'
*
*                   (b) Heap declared in 'lib_mem.c',                      if LIB_MEM_CFG_HEAP_BASE_ADDR
*                                                                             NOT #define'd in 'app_cfg.h'
*********************************************************************************************************
*/

                                                        /* Configure memory allocation feature (see Note #1) :          */
#define  LIB_MEM_CFG_ALLOC_EN           <#if UCOSIII_LIB_MEM_CFG_ALLOC_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>
                                                        /*   DEF_DISABLED     Memory allocation DISABLED                */
                                                        /*   DEF_ENABLED      Memory allocation ENABLED                 */


#define  LIB_MEM_CFG_HEAP_SIZE           ${UCOSIII_LIB_MEM_CFG_HEAP_SIZE}   /* Configure heap memory size         [see Note #2a].           */



/*
*********************************************************************************************************
*                                 STRING FLOATING POINT CONFIGURATION
*
* Note(s) : (1) Configure LIB_STR_CFG_FP_EN to enable/disable floating point string function(s).
*********************************************************************************************************
*/

                                                        /* Configure floating point feature(s) [see Note #1] :          */
#define  LIB_STR_CFG_FP_EN              <#if UCOSIII_LIB_STR_CFG_FP_EN == true>DEF_ENABLED<#else>DEF_DISABLED</#if>
                                                        /*   DEF_DISABLED     Floating point functions DISABLED         */
                                                        /*   DEF_ENABLED      Floating point functions ENABLED          */



#endif                                                  /* End of lib cfg module include.                               */

