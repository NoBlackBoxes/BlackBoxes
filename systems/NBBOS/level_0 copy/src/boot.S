.section ".text.boot"

// The "start" of NBBOS
.globl _start
_start:
    // Check that we are on the main core
    mrs x0, mpidr_el1       // Load the core ID into x0
    and x0, x0, #0xFF       // Isolate the lowest byte
    cbz x0, setup           // If zero, then we are on the main core (branch to setup)
    b hang                  // If not, then hang

// Setup and clear the stack
setup:
    // Set the stack pointer
    ldr x1, =_start         // Load the address of _start in x1
    mov sp, x1              // Set the stack pointer to this address (stack will grow down)

    // Clear the BSS (stack) region
    ldr x1, =__bss_start    // Load first address of BSS into x0
    ldr w2, =__bss_size     // Load size of BSS into w2
1:  cbz w2, code            // Check if w2 is zero, if so run our code
    str xzr, [x1], #8       // Store zero (the xzr register, 64-bits/8-bytes) at address in x1 and then increment x1 by 8
    sub w2, w2, #1          // Decrement w2
    cbnz w2, 1b             // Loop (go to backward reference 1, 1b) if result w2 not zero

// Jump to code entry point
code:
    bl kernel_main

    // Hang if our code returns
    b  hang

// Hang (infinite loop)
hang:
    wfe                     // Wait for event (low-power)
    b hang
