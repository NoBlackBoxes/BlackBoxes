#include "io.h"
#include "gpio.h"

/** GPIO Register set */
volatile unsigned int* gpio = (unsigned int*)GPIO_BASE;

void kernel_main()
{
    uart_init();
    fb_init();
    gpio[LED_GPFSEL] |= (1 << LED_GPFBIT); // Set as output
    gpio[GPIO_GPFSEL1] |= (1 << 18); // Set as output

    // Get processor speed
    uart_writeText("TEST TEST");

    char r,g,b;
    r = 0;
    g = 55;
    b = 77;

    int rg = 0;
    while (1)
    {
        fill(r,g,b);
        r += 2;
        g += 5;
        b += 9;

        if(rg == 1)
        {
            gpio[LED_GPCLR] = (1 << LED_GPIO_BIT);
            gpio[GPIO_GPCLR0] = (1 << 16);
            rg = 0;
        }
        else
        {
            gpio[LED_GPSET] = (1 << LED_GPIO_BIT);
            gpio[GPIO_GPSET0] = (1 << 16);
            rg = 1;
        }
    }
}
