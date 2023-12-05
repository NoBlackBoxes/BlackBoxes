#pragma once

struct AUX_REGS {
    unsigned int irq_status;
    unsigned int enables;
    unsigned int reserved[14];
    unsigned int mu_io;
    unsigned int mu_ier;
    unsigned int mu_iir;
    unsigned int mu_lcr;
    unsigned int mu_mcr;
    unsigned int mu_lsr;
    unsigned int mu_msr;
    unsigned int mu_scratch;
    unsigned int mu_control;
    unsigned int mu_status;
    unsigned int mu_baud_rate;
};

#define UART_REGS ((struct AUX_REGS *)(PERIPHERAL_BASE + 0x00215000))

void uart_init();
char uart_recv();
void uart_send(char c);
void uart_send_string(char *str);