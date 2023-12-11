#pragma once

// Include STD headers
#include <stdint.h>

// Definitions (Peripheral base address)
#define PERIPHERAL_BASE 0xFE000000

// External declarations (ASM utilities)
extern void PUT32 (uint64_t address, uint32_t value);
extern uint32_t GET32 (uint64_t address);
extern void TICK (uint64_t count);
extern uint32_t GETEL (void);
