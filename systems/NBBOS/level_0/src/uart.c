#include "gpio.h"
#include "uart.h"

/* UART (AUX - minuart) Register set */
volatile unsigned int* aux = (unsigned int*)AUX_BASE;

void uart_init_2() {
    mmio_write(AUX_BASE + 4, 1); //enable UART1
    mmio_write(AUX_BASE + 68, 0);
    mmio_write(AUX_BASE + 96, 0);
    mmio_write(AUX_BASE + 76, 3); //8 bits
    mmio_write(AUX_BASE + 80, 0);
    mmio_write(AUX_BASE + 68, 0);
    mmio_write(AUX_BASE + 72, 0xC6); //disable interrupts
    mmio_write(AUX_BASE + 104, UART_BAUD(115200));
    gpio_useAsAlt5(14);
    gpio_useAsAlt5(15);
    mmio_write(AUX_BASE + 96, 3); //enable RX/TX
}


unsigned int uart_isWriteByteReady() { return mmio_read(AUX_BASE + 84) & 0x20; }

void uart_writeByteBlockingActual(unsigned char ch) {
    while (!uart_isWriteByteReady());

    // THESE ARE NOT THE SAME!!!!! WHYYYY!YY!Y!Y!Y!
    //aux[16] = (unsigned int)ch;

    *(volatile unsigned int *)(AUX_BASE + 64) = (unsigned int)ch;
    //mmio_write(AUX_BASE + AUX_MU_IO_REG, (unsigned int)ch);
}

void uart_writeText(char *buffer) {
    while (*buffer) {
       if (*buffer == '\n') uart_writeByteBlockingActual('\r');
       uart_writeByteBlockingActual(*buffer++);
    }
}

void uart_init() {
    
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