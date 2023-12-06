#include "gpio.h"
#include "uart.h"

// Initialize UART
void uart_init()
{    
    // Set UART (miniuart, UART1) registers
    PUT32(AUX_ENABLES, 1);
    PUT32(AUX_MU_IER_REG, 0);
    PUT32(AUX_MU_CNTL_REG, 0);
    PUT32(AUX_MU_LCR_REG, 3);
    PUT32(AUX_MU_MCR_REG, 0);
    PUT32(AUX_MU_IER_REG, 0);
    PUT32(AUX_MU_IIR_REG, 0xC6);
    PUT32(AUX_MU_BAUD_REG, UART_BAUD(115200));

    // Set GPIO pin alternate functions and pull resistors
    gpio_set_pull(UART_TXD, GPIO_Pull_None);
    gpio_set_function(UART_TXD, GPIO_Function_Alt5);
    gpio_set_pull(UART_RXD, GPIO_Pull_None);
    gpio_set_function(UART_RXD, GPIO_Function_Alt5);

    // Enable UART
    PUT32(AUX_MU_CNTL_REG, 3);

    // Offset screen
    uart_send('\r');
    uart_send('\n');
}

void uart_send(char c) 
{
    while(!(GET32(AUX_MU_LSR_REG) & 0x20));

    PUT32(AUX_MU_IO_REG, c);
}

char uart_recv() {
    while(!(GET32(AUX_MU_LSR_REG) & 1));

    return GET32(AUX_MU_IO_REG) & 0xFF;
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