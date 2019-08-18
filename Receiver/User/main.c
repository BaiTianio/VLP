#include "sys.h"
#include "usart.h"
#include "delay.h"
#include "adc.h"
#include "gpio.h"
#include "dma.h"
#include "exti.h"

void Get_ADC(u8 *data_storge);//��ȡADC��Ϣ�������浽Data_storge	
int *Data_storge=NULL;
Data_storge=(int *)malloc(2000 * sizeof(u16));//���ݴ洢
memset(Data_storge,0,2000 * sizeof(u16))
int main(void)
{	
//	int i;//������

	uart_init(115200);
	delay_init();
	Adc_Init(); 
	gpio_Init();
	// dma_Init(DMA1_Channel4,(uint32_t)&USART1->DR,(uint32_t)Data_storge,(uint32_t)72);
	// exti_init();
	
	// Get_ADC(Data_storge);//�ɼ�����
	// dma_usart_Start(DMA1_Channel4, 72);//����DMA����
	while(1)
	{
		Get_ADC(Data_storge);//�ɼ�����
		// while(((DMA1->ISR)&(0x01<<13))==0);//�ȴ�DMA�������
		// DMA1->IFCR |=0x01<<13;//���������ɱ�־
		// dma_usart_Start(DMA1_Channel4, 72);//����DMA����
		// EXTI->IMR |=EXTI_Line12;//�����ⲿ�ж�
	}
}

void Get_ADC(u8 *data_storge)//��ȡADC��Ϣ�������浽data_storge
{
	u16 temp;//��ʱ�洢ADC����
	int Channel=0;
	u8 Sensor_g;
	u8 Data[8];
	
	for(Sensor_g=0;Sensor_g<8;Sensor_g++)
		{       
			GPIO_Write(GPIOB,Sensor_g<<3);//����ģ��ѡ����
			delay_us(5);
			for(Channel=0;Channel<=3;Channel++)
				{
					temp=Get_Adc_Average(Channel,5);//ÿ��ͨ��ת��5�����ֵ	
					switch(Channel)
					{
						case 0:	{
										Data[0]=temp>>8;
										Data[1]=temp;
										}
						case 1:	{
										Data[2]=temp>>8;
										Data[3]=temp;
										}
						case 2:	{									//Ϊ�˾���PCB���ִ���ABDC����ADC_Channel2���ݷ���Data[7]��Data[8]
										Data[6]=temp>>8;
										Data[7]=temp;
										}
						case 3:	{										//Ϊ�˾���PCB���ִ���ABDC����ADC_Channel3���ݷ���Data[5]��Data[6]
										Data[4]=temp>>8;
										Data[5]=temp;
										}
					}
				}
				*data_storge=Sensor_g;
				data_storge++;
				for(int i=0;i<8;i++)
					{
						*(data_storge)=Data[i];
						data_storge++;				
					}
	}
}
