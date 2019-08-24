
#include "exti.h"

void exti_io_init(void)
{
    GPIO_InitTypeDef GPIO_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE);
    
    GPIO_InitStructure.GPIO_Pin=GPIO_Pin_12;
    GPIO_InitStructure.GPIO_Mode=GPIO_Mode_IPD;//下拉输入
    GPIO_InitStructure.GPIO_Speed=GPIO_Speed_50MHz;
    GPIO_Init(GPIOB,&GPIO_InitStructure);
}

void exti_NVIC_init(void)
{
    EXTI_InitTypeDef EXTI_InitStructure;
	
	  GPIO_EXTILineConfig(GPIO_PortSourceGPIOB,GPIO_PinSource12);
    EXTI_InitStructure.EXTI_Line=EXTI_Line12;	
  	EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;	
		EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;//上降沿触发
  	EXTI_InitStructure.EXTI_LineCmd = ENABLE;
  	EXTI_Init(&EXTI_InitStructure);	 

	  NVIC_InitTypeDef NVIC_InitStructure;
    NVIC_InitStructure.NVIC_IRQChannel = EXTI15_10_IRQn;			
  	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0x00;	//设置优先级到最高
  	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0x00;			
  	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;					//使能外部中断通道
  	NVIC_Init(&NVIC_InitStructure); 
}

void exti_init(void)
{
    exti_io_init();
    exti_NVIC_init();
}
