#pragma once

// Definitions
#define PERIPHERAL_BASE 0xFE000000

// External declarations
extern void PUT32 ( unsigned int, unsigned int );
extern unsigned int GET32 ( unsigned int );
extern void TICK ( unsigned int );
