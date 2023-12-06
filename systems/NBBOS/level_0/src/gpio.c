#include "gpio.h"

// Set GPIO pin function
void gpio_set_function(unsigned int pin, unsigned int function)
{
    int selection_bank = pin / 10;                      // Determine function selection bank (groups of 10 pins)
    int bit_offset = (pin * 3) % 30;                    // Determine bit offset of pin within bank
    
    unsigned int current_value = GET32(selection_bank); // Retrieve current register value
    current_value &= ~(7 << bit_offset);                // Clear 3 bits at offset
    current_value |= (function << bit_offset);          // Store new bits at offset
    PUT32(selection_bank, current_value);               // Set selection register

    return;
}

// Set GPIO pin pull resistor
void gpio_set_pull(unsigned int pin, unsigned int pull)
{
    int selection_bank = (pin / 16) + GPIO_PUP_PDN_CNTRL_REG0;  // Determine pull selection bank (groups of 16 pins)
    int bit_offset = (pin * 2) % 32;                            // Determine bit offset of pin within bank
    
    unsigned int current_value = GET32(selection_bank);         // Retrieve current register value
    current_value &= ~(3 << bit_offset);                        // Clear 2 bits at offset
    current_value |= (pull << bit_offset);                      // Store new bits at offset
    PUT32(selection_bank, current_value);                       // Set selection register

    return;
}

// Set (True)
void gpio_pin_set(unsigned int pin) 
{
    if(pin < 32)
    {
        PUT32(GPSET0, (1 << pin));    
    }
    else if(pin < GPIO_MAXPIN)
    {
        PUT32(GPSET1, (1 << (pin - 32)));    
    }    
    return;
}

// Clear (False)
void gpio_pin_clear(unsigned int pin) 
{
    if(pin < 32)
    {
        PUT32(GPCLR0, (1 << pin));    
    }
    else if(pin < GPIO_MAXPIN)
    {
        PUT32(GPCLR1, (1 << (pin - 32)));    
    }    
    return;
}
