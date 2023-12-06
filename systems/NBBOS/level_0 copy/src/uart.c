#include "gpio.h"
#include "uart.h"

void uart_init() {
    
    *(volatile unsigned int *)(AUX_BASE + AUX_ENABLES) = 1;

    // Set UART (miniuart, UART1) registers
    aux[AUX_ENABLES] = 1;
    aux[AUX_MU_IER_REG] = 0;
    aux[AUX_MU_CNTL_REG] = 0;
    aux[AUX_MU_LCR_REG] = 3;
    aux[AUX_MU_MCR_REG] = 0;
    aux[AUX_MU_IER_REG] = 0;
    aux[AUX_MU_IIR_REG] = 0xC6;
    aux[AUX_MU_BAUD_REG] = UART_BAUD(115200);


    gpio_useAsAlt5(14);
    gpio_useAsAlt5(15);

    // THIS IS BROKEN---->
    // Set GPIO pin alternate functions and pull resistors
    //gpio_set_pull(UART_TXD, GPIO_Pull_None);
    //gpio_set_function(UART_TXD, GPIO_Function_Alt5);
    //gpio_set_pull(UART_RXD, GPIO_Pull_None);
    //gpio_set_function(UART_RXD, GPIO_Function_Alt5);

    // Enable UART
    aux[AUX_MU_CNTL_REG] = 3;

    // Offset screen
    uart_send('\r');
    uart_send('\n');
    uart_send('\n');
    uart_send('\n');
    uart_send('\n');
}

void uart_send(char c) 
{
    while(!(aux[AUX_MU_LSR_REG] & 0x20));

    aux[AUX_MU_IO_REG] = c;
}

char uart_recv() {
    while(!(aux[AUX_MU_LSR_REG] & 1));

    return aux[AUX_MU_IO_REG] & 0xFF;
}

void uart_send_string(char *str) {
    while(*str)
    {
        if (*str == '\n') {
            uart_send('\r');
        }

        uart_send(*str);
        str++;
    }
}