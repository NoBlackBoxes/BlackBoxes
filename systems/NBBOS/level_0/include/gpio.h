#pragma once

#include "defs.h"

// Definitions
#define GPIO_BASE       (PERIPHERAL_BASE + 0x00200000)
#define GPIO_MAXPIN     58
#define GPIO_LEDPIN     42

#define GPIO_GPSET0     7
#define GPIO_GPSET1     8
#define GPIO_GPCLR0     10
#define GPIO_GPCLR1     11
#define GPIO_GPLEV0     13
#define GPIO_GPLEV1     14
#define GPIO_GPEDS0     16
#define GPIO_GPEDS1     17
#define GPIO_GPREN0     19
#define GPIO_GPREN1     20
#define GPIO_GPFEN0     22
#define GPIO_GPFEN1     23
#define GPIO_GPHEN0     25
#define GPIO_GPHEN1     26
#define GPIO_GPLEN0     28
#define GPIO_GPLEN1     29
#define GPIO_GPAREN0    31
#define GPIO_GPAREN1    32
#define GPIO_GPAFEN0    34
#define GPIO_GPAFEN1    35
#define GPIO_GPPUDREG0  37
#define GPIO_GPPUDREG1  38
#define GPIO_GPPUDREG2  39
#define GPIO_GPPUDREG3  40

typedef enum _GPIO_Function {
    GPIO_Function_Input     = 0,
    GPIO_Function_Output    = 1,
    GPIO_Function_Alt0      = 4,
    GPIO_Function_Alt1      = 5,
    GPIO_Function_Alt2      = 6,
    GPIO_Function_Alt3      = 7,
    GPIO_Function_Alt4      = 3,
    GPIO_Function_Alt5      = 2
} GPIO_Function;

typedef enum _GPIO_Pull {
    GPIO_Pull_None          = 0,
    GPIO_Pull_Up            = 1,
    GPIO_Pull_Down          = 2,
    GPIO_Pull_Reserved      = 3,
} GPIO_Pull;

// Declarations
void gpio_set_function(unsigned int pin, GPIO_Function function);
void gpio_set_pull(unsigned int pin, GPIO_Pull pull);
void gpio_pin_set(unsigned int pin);
void gpio_pin_clear(unsigned int pin);
