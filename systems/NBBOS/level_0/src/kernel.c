#include "defs.h"
#include "uart.h"
#include "gpio.h"

void kernel_main()
{
    // Initialize UART
    uart_init();

    // Say hello
    uart_send_string("Hello Everybody!\n");

    // Select GPIO functions
	gpio_set_function(GPIO_LEDPIN, GPIO_Function_Output);
	gpio_set_function(16, GPIO_Function_Output);

    // Blink super fast
    int rg = 0;
    while (1)
    {
        if(rg == 1)
        {
            gpio_pin_set(GPIO_LEDPIN);
            gpio_pin_set(16);
            rg = 0;
        }
        else
        {
            gpio_pin_clear(GPIO_LEDPIN);
            gpio_pin_clear(16);
            rg = 1;
        }
        TICK(10000);
    }
}
