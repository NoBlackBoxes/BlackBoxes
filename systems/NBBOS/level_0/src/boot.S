.section ".text.boot"

.globl _start
_start:
    mrs x0, mpidr_el1       // Load the core ID
    and x0, x0, #0xFF       // Isolate lowest byte
    cbz x0, master          // If Zero, then we are on the main core
    b hang

master:
    ldr     x1, =_start
    mov     sp, x1

    adr x0, bss_begin       // Setup stack
    adr x1, bss_end
    sub x1, x1, x0          // Measure size of BSS section
    bl memzero              // Clear

    mov sp, #LOW_MEMORY     // Set stack pointer

    bl kernel_main          // Start kernel
    b  hang                 // Hang if code retruns

hang:
    wfe                     // Hang
    b hang
