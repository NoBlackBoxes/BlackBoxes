#include "common.h"
#include "utilities.h"
#include "mmu.h"
#include "uart.h"
#include "gpio.h"
#include "framebuffer.h"

void kernel_main()
{
    // Initialize UART
    uart_init();

    // MMU init
    mmu_init();

    // Say hello
    uart_send_string("Hello Everybody!\n");

    // Update CPU Clocks (this sequence breaks for O3 and O4 compiliation)
    uint32_t clock_rate = get_clock_rate();
    uart_report("Initial Clock Rate (Hz)", clock_rate);
    set_clock_rate(1500000000);
    clock_rate = get_clock_rate();
    uart_report("New Clock Rate (Hz)", clock_rate);

    // Get current exception level
    uint32_t el = GETEL();
    uart_report("Current Exception Level", el);

    // Initialize framebuffer
    framebuffer_init();

    // Select GPIO functions
	gpio_set_function(GPIO_LEDPIN, GPIO_Function_Output);
	gpio_set_function(16, GPIO_Function_Output);

    int rg = 0;
    char r,g,b;
    r = 0;
    g = 55;
    b = 77;

    while (1)
    {
        framebuffer_fill(r,g,b);
        r += 2;
        g += 5;
        b += 9;

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
        // TICK(10000);
    }
}
