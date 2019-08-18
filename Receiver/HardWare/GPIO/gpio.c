#include"gpio.h"
//stm32f103c8t6 复用引脚的初始化需要先把主要功能关闭，再初始化GPIO

void DisableMainFunc(void)
{

	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO,ENABLE);
	
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);
	
}



void gpio_Init(void)
{
    GPIO_InitTypeDef GPIO_InitStructure;
	
		DisableMainFunc();//禁用主要功能JTAG
	
		RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE);
    
    GPIO_InitStructure.GPIO_Pin=GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5;
    GPIO_InitStructure.GPIO_Mode=GPIO_Mode_Out_PP;
    GPIO_InitStructure.GPIO_Speed=GPIO_Speed_50MHz;
    GPIO_Init(GPIOB,&GPIO_InitStructure);
}
