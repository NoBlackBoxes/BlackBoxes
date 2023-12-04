#include "mm.h"

.section ".text.boot"

.globl _start
    _start:
        mrs x0, mpidr_el1   // Check that we are on the mmain core
    and x0, x0, #0xFF
    cbz x0, master
    b proc_hang

master:
    //// Define memory attributes
    //// Attr0 = Normal, Inner/Outer Write-back, Write-allocate, Cacheable
    //LDR X0, =0xFF               // Set Attr0=0xFF (Normal Memory)
    //MSR MAIR_EL3, X0            // Write to MAIR_EL1
//
    //LDR X0, =translation_table   // Load address of translation table
    //MSR TTBR0_EL3, X0            // Set TTBR0_EL3
//
    //// Assuming translation tables and MAIR are already set up
    //LDR X0, = translation_table  // Load the address of the translation table
    //MSR TTBR0_EL3, X0            // Set Translation Table Base Register 0
//
    //// Example values: T0SZ=22 for 4GB address space, Inner/Outer Write-back, no allocation on write miss
    //LDR X0, =0x80000000 | (22 << 16) 
    //MSR TCR_EL3, X0             // Write to TCR_EL3
//
    //// Set up MAIR, TCR registers
    //MRS X0, SCTLR_EL3            // Read SCTLR
    //ORR X0, X0, #1               // Set M bit to enable MMU
    //MSR SCTLR_EL3, X0            // Write back to SCTLR
//
    //DSB SY                       // Data Synchronization Barrier
    //ISB                          // Instruction Synchronization Barrier
//
    //mrs X0, SCTLR_EL3      // Read SCTLR
    //orr X0, X0, #(1 << 2)  // Set C bit for D-cache
    //orr X0, X0, #(1 << 12) // Set I bit for I-cache
    //msr SCTLR_EL3, X0      // Write back to SCTLR
    //dsb SY                 // Data Synchronization Barrier
    //isb                    // Instruction Synchronization Barrier
//
    adr x0, bss_begin       // Setup stack
    adr x1, bss_end
    sub x1, x1, x0          // Measure size of BSS section
    bl memzero              // Clear

    mov sp, #LOW_MEMORY     // Set stack pointer


    bl kernel_main          // Start kernel
    b  proc_hang            // Hang if code retruns

proc_hang:
    wfe                     // Hang
    b proc_hang

//.section .data
//    .align 12                    // 4KB aligned
//translation_table:
//    .rept 512                    // Repeat 512 times for 1GB of memory
//    // Each entry: Output address | AttrIdx (bits 2-4) | Access Flag, Shareable, Valid, and Type Flags
//    .word 0x40000000 | (0 << 2) | 0x403         // Normal Memory, Read-Write, Outer Shareable
//.endr