#include "sys.h"
#include "usart.h"
#include "delay.h"
#include "adc.h"
#include "gpio.h"
#include "exti.h"

u16 Data_storge[40]={0};//���ݴ洢

void Get_ADC(u16 *data_point)//��ȡADC��Ϣ�������浽data_storge
{
	u16 temp;//��ʱ�洢ADC����
	int Channel=0;
	u8 Sensor_g;
	//u8 Data[8];
	
	for(Sensor_g=0;Sensor_g<8;Sensor_g++)
		{       
			GPIO_Write(GPIOB,Sensor_g<<3);//����ģ��ѡ����
			delay_us(5);
			*data_point=Sensor_g;
			for(Channel=0;Channel<=3;Channel++)
				{
					temp=Get_Adc_Average(Channel,5);//ÿ��ͨ��ת��5�����ֵ	
				  *(++data_point)=temp;
				}
			data_point++;//Ϊsensor_g���ӵ�ַ
		}
}

int main(void)
{	
	uart_init(1500000);
	delay_init();
	Adc_Init(); 
	gpio_Init();
	exti_init();
	while(1)
	{
		Get_ADC(Data_storge);//�ɼ�����	
		for (int i=0;i<40;i++)
			{
				while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=1);
				USART_SendData(USART1,Data_storge[i]);
			}
	}
}
