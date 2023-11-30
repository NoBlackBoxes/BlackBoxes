#include "io.h"
#include "fb.h"
#include "gpio.h"

/** GPIO Register set */
volatile unsigned int* gpio = (unsigned int*)GPIO_BASE;

void main()
{
    uart_init();
    fb_init();
    gpio[LED_GPFSEL] |= (1 << LED_GPFBIT); // Set as output

    int rg = 0;
    while (1)
    {
        if(rg == 1)
        {
            gpio[LED_GPCLR] = (1 << LED_GPIO_BIT);
            fillBackground(0x04);
            rg = 0;
        }
        else
        {
            gpio[LED_GPSET] = (1 << LED_GPIO_BIT);
            fillBackground(0x02);
            rg = 1;
        }
    }
}
