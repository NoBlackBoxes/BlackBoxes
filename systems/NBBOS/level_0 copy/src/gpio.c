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

enum {
    GPFSEL0         = PERIPHERAL_BASE + 0x200000,
    GPSET0          = PERIPHERAL_BASE + 0x20001C,
    GPCLR0          = PERIPHERAL_BASE + 0x200028,
    GPPUPPDN0       = PERIPHERAL_BASE + 0x2000E4
};

enum {
    GPIO_MAX_PIN       = 53,
    GPIO_FUNCTION_ALT5 = 2,
};

enum {
    Pull_None = 0,
};


void mmio_write(long reg, unsigned int val) { *(volatile unsigned int *)reg = val; }
unsigned int mmio_read(long reg) { return *(volatile unsigned int *)reg; }

unsigned int gpio_call(unsigned int pin_number, unsigned int value, unsigned int base, unsigned int field_size, unsigned int field_max) {
    unsigned int field_mask = (1 << field_size) - 1;
  
    if (pin_number > field_max) return 0;
    if (value > field_mask) return 0; 

    unsigned int num_fields = 32 / field_size;
    unsigned int reg = base + ((pin_number / num_fields) * 4);
    unsigned int shift = (pin_number % num_fields) * field_size;

    unsigned int curval = mmio_read(reg);
    curval &= ~(field_mask << shift);
    curval |= value << shift;
    mmio_write(reg, curval);

    return 1;
}

unsigned int gpio_set     (unsigned int pin_number, unsigned int value) { return gpio_call(pin_number, value, GPSET0, 1, GPIO_MAX_PIN); }
unsigned int gpio_clear   (unsigned int pin_number, unsigned int value) { return gpio_call(pin_number, value, GPCLR0, 1, GPIO_MAX_PIN); }
unsigned int gpio_pull    (unsigned int pin_number, unsigned int value) { return gpio_call(pin_number, value, GPPUPPDN0, 2, GPIO_MAX_PIN); }
unsigned int gpio_function(unsigned int pin_number, unsigned int value) { return gpio_call(pin_number, value, GPFSEL0, 3, GPIO_MAX_PIN); }

void gpio_useAsAlt5(unsigned int pin_number) {
    gpio_pull(pin_number, Pull_None);
    gpio_function(pin_number, GPIO_FUNCTION_ALT5);
}
