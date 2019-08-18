#include"gpio.h"
//stm32f103c8t6 �������ŵĳ�ʼ����Ҫ�Ȱ���Ҫ���ܹرգ��ٳ�ʼ��GPIO

void DisableMainFunc(void)
{

	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO,ENABLE);
	
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);
	
}



void gpio_Init(void)
{
    GPIO_InitTypeDef GPIO_InitStructure;
	
		DisableMainFunc();//������Ҫ����JTAG
	
		RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE);
    
    GPIO_InitStructure.GPIO_Pin=GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5;
    GPIO_InitStructure.GPIO_Mode=GPIO_Mode_Out_PP;
    GPIO_InitStructure.GPIO_Speed=GPIO_Speed_50MHz;
    GPIO_Init(GPIOB,&GPIO_InitStructure);
}
