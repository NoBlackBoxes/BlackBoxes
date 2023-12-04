#include "uart.h"
#include "fb.h"
#include "gpio.h"

void kernel_main()
{
    uart_init();
    fb_init();
	
	gpio_pin_set_func(16, GFOutput);

    // Get processor speed
    uart_send_string("TEST TEST");

    char r,g,b;
    r = 0;
    g = 55;
    b = 77;

    int rg = 0;
    while (1)
    {
        if(rg == 1)
        {
            gpio_pin_set(16);
			fill(r,g,b);
			r += 2;
			g += 5;
			b += 9;
            rg = 0;
        }
        else
        {
            gpio_pin_clear(16);
			clear();
            rg = 1;
        }
    }
}
