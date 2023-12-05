#include "gpio.h"
#include "uart.h"

#define UART_TXD 14
#define UART_RXD 15

#define UART_CLOCK  500000000
#define UART_BAUD(baud) ((UART_CLOCK/(baud*8))-1)

void uart_init() {

    // Set GPIO pin alternate functions
    gpio_set_function(UART_TXD, GPIO_Function_Alt5);
    gpio_set_function(UART_RXD, GPIO_Function_Alt5);
    
    // Set UART (miniuart, UART1) registers
    UART_REGS->enables = 1;
    UART_REGS->mu_control = 0;
    UART_REGS->mu_lcr = 3;
    UART_REGS->mu_mcr = 0;
    UART_REGS->mu_ier = 0;
    UART_REGS->mu_iir = 0xc6;
    UART_REGS->mu_baud_rate = 541; // = 115200 @ 500 Mhz

    // Disable pull resistors on TXD/RXD
    gpio_set_pull(UART_TXD, GPIO_Pull_None);
    int r=150; while(r--) { asm volatile("nop"); }
    gpio_set_pull(UART_RXD, GPIO_Pull_None);
    r=150; while(r--) { asm volatile("nop"); }

    //int r=150; while(r--) { asm volatile("nop"); }
    //*GPPUDCLK0 = (1<<14)|(1<<15);
    //r=150; while(r--) { asm volatile("nop"); }
    //*GPPUDCLK0 = 0;        // flush GPIO setup

    // Enable UART
    //UART_REGS->mu_control = 3;

    //// Offset screen
    //uart_send('\r');
    //uart_send('\n');
    //uart_send('\n');
    //uart_send('\n');
    //uart_send('\n');
}

void uart_send(char c) {
    while(!(UART_REGS->mu_lsr & 0x20));

    UART_REGS->mu_io = c;
}

char uart_recv() {
    while(!(UART_REGS->mu_lsr & 1));

    return UART_REGS->mu_io & 0xFF;
}

void uart_send_string(char *str) {
    while(*str) {
        if (*str == '\n') {
            uart_send('\r');
        }

        uart_send(*str);
        str++;
    }
}