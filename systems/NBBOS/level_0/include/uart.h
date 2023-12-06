#pragma once
#include "defs.h"

// Definitions
#define AUX_BASE            PERIPHERAL_BASE + 0x215000
#define AUX_IRQ             UAX_BASE + 0x00
#define AUX_ENABLES         UAX_BASE + 0x04
#define AUX_MU_IO_REG       UAX_BASE + 0x40
#define AUX_MU_IER_REG      UAX_BASE + 0x44
#define AUX_MU_IIR_REG      UAX_BASE + 0x48
#define AUX_MU_LCR_REG      UAX_BASE + 0x4c
#define AUX_MU_MCR_REG      UAX_BASE + 0x50
#define AUX_MU_LSR_REG      UAX_BASE + 0x54
#define AUX_MU_MSR_REG      UAX_BASE + 0x58
#define AUX_MU_SCRATCH      UAX_BASE + 0x5c
#define AUX_MU_CNTL_REG     UAX_BASE + 0x60
#define AUX_MU_STAT_REG     UAX_BASE + 0x64
#define AUX_MU_BAUD_REG     UAX_BASE + 0x68

#define UART_TXD            14
#define UART_RXD            15
#define UART_CLOCK          500000000
#define UART_MAX_QUEUE      16 * 1024
#define UART_BAUD(baud)     ((UART_CLOCK/(baud*8))-1)

// Declarations
void uart_init();
char uart_recv();
void uart_send(char c);
void uart_send_string(char *str);

void uart_init_2();
void uart_writeText(char *buffer);