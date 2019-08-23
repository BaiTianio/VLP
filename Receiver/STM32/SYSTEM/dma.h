#ifndef __DMA_H
#define __DMA_H

#include "stm32f10x.h"


// //临时使用
// #include "..\SourceCode\stm32f10x_conf.h"

// //


void dma_Init(DMA_Channel_TypeDef *DMA_CHx, uint32_t Periph_Addr,uint32_t Memory_Addr,uint32_t data_num);
void dma_usart_Start(DMA_Channel_TypeDef * DMA_CHx, uint32_t data_num);
#endif
