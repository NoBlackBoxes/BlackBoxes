#pragma once

// Definitions (Peripheral base address)
#define PERIPHERAL_BASE 0xFE000000

// Definitions (Type names)
#define uint8_t     unsigned char
#define int8_t      signed char
#define uint16_t    unsigned short
#define int16_t     signed short
#define uint32_t    unsigned long
#define int32_t     signed long
#define uint64_t    unsigned long long
#define int64_t     signed long long

// External declarations
extern void PUT32 (uint64_t address, uint32_t value);
extern uint32_t GET32 (uint64_t address);
extern void TICK (uint64_t count);
