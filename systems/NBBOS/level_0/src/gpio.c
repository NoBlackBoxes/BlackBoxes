#include "gpio.h"

/* GPIO Register set */
volatile unsigned int* gpio = (unsigned int*)GPIO_BASE;

// Set GPIO pin function
void gpio_set_function(unsigned int pin, GPIO_Function function)
{
    int selection_bank = pin / 10;                      // Determine function selection bank (groups of 10 pins)
    int bit_offset = (pin * 3) % 30;                    // Determine bit offset of pin within bank
    
    unsigned int current_value = gpio[selection_bank];  // Retrieve current register value
    current_value &= ~(7 << bit_offset);                // Clear 3 bits at offset
    current_value |= (function << bit_offset);          // Store new bits at offset
    gpio[selection_bank] = current_value;               // Set selection register

    return;
}

// Set GPIO pin pull resistor
void gpio_set_pull(unsigned int pin, GPIO_Pull pull)
{
    int selection_bank = (pin / 16) + GPIO_GPPUDREG0;   // Determine pull selection bank (groups of 16 pins)
    int bit_offset = (pin * 2) % 32;                    // Determine bit offset of pin within bank
    
    unsigned int current_value = gpio[selection_bank];  // Retrieve current register value
    current_value &= ~(3 << bit_offset);                // Clear 2 bits at offset
    current_value |= (pull << bit_offset);              // Store new bits at offset
    gpio[selection_bank] = current_value;               // Set selection register

    return;
}

// Set (True)
void gpio_pin_set(unsigned int pin) 
{
    if(pin < 32)
    {
        gpio[GPIO_GPSET0] = (1 << pin);    
    }
    else if(pin < GPIO_MAXPIN)
    {
        gpio[GPIO_GPSET1] = (1 << (pin - 32));    

    }    
    return;
}

// Clear (False)
void gpio_pin_clear(unsigned int pin) 
{
    if(pin < 32)
    {
        gpio[GPIO_GPCLR0] = (1 << pin);    
    }
    else if(pin < GPIO_MAXPIN)
    {
        gpio[GPIO_GPCLR1] = (1 << (pin - 32));    

    }    
    return;
}