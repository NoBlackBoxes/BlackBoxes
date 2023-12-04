#include "gpio.h"
#include "utils.h"

#define GPIO_GPSET0     7
#define GPIO_GPSET1     8

#define GPIO_GPCLR0     10
#define GPIO_GPCLR1     11

/** GPIO Register set */
volatile unsigned int* gpio = (unsigned int*)REGS_GPIO;

void gpio_pin_set_func(u8 pinNumber, GpioFunc func) {
    u8 bitStart = (pinNumber * 3) % 30;
    u8 reg = pinNumber / 10;

    u32 selector = REGS_GPIO->func_select[reg];
    selector &= ~(7 << bitStart);
    selector |= (func << bitStart);

    REGS_GPIO->func_select[reg] = selector;
}

void gpio_pin_enable(u8 pinNumber) {
    REGS_GPIO->pupd_enable = 0;
    delay(150);
    REGS_GPIO->pupd_enable_clocks[pinNumber / 32] = 1 << (pinNumber % 32);
    delay(150);
    REGS_GPIO->pupd_enable = 0;
    REGS_GPIO->pupd_enable_clocks[pinNumber / 32] = 0;
}

void gpio_pin_set(u8 pinNumber) 
{
    gpio[GPIO_GPSET0] = (1 << pinNumber);
}

void gpio_pin_clear(u8 pinNumber) 
{
    gpio[GPIO_GPCLR0] = (1 << pinNumber);
}