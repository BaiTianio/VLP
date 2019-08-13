#include"dma.h"




void dma_Init(DMA_Channel_TypeDef *DMA_CHx, uint32_t Periph_Addr,uint32_t Memory_Addr,uint32_t data_num)
{
    DMA_InitTypeDef DMA_InitSturcture;
	
	//开启dma时钟
    RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1,ENABLE);


    DMA_InitSturcture.DMA_PeripheralBaseAddr=Periph_Addr;
    DMA_InitSturcture.DMA_MemoryBaseAddr=Memory_Addr;
    DMA_InitSturcture.DMA_DIR=DMA_DIR_PeripheralDST;//从内存读取数据发送到外设
    DMA_InitSturcture.DMA_BufferSize=data_num;
    DMA_InitSturcture.DMA_PeripheralInc=DMA_PeripheralInc_Disable;
    DMA_InitSturcture.DMA_MemoryInc=DMA_MemoryInc_Enable;
	  DMA_InitSturcture.DMA_PeripheralDataSize=DMA_PeripheralDataSize_Byte;//外设接收数据Size：字节
    DMA_InitSturcture.DMA_MemoryDataSize=DMA_MemoryDataSize_Byte;//内存发送数据Size：字节
    DMA_InitSturcture.DMA_Mode=DMA_Mode_Normal;
    DMA_InitSturcture.DMA_Priority=DMA_Priority_Medium;
    DMA_InitSturcture.DMA_M2M=DMA_M2M_Disable;
    DMA_Init(DMA_CHx,&DMA_InitSturcture);
    
}

//开始一次DMA传输
void dma_usart_Start(DMA_Channel_TypeDef * DMA_CHx, uint32_t data_num)
{  
    DMA_Cmd(DMA_CHx,DISABLE);
    DMA_CHx->CNDTR=data_num;//设置传输量大小
    DMA_Cmd(DMA_CHx,ENABLE);
}

