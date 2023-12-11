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
1:  cbz w2, mmu             // Check if w2 is zero, if so setup the MMU (and cache)
    str xzr, [x1], #8       // Store zero (the xzr register, 64-bits/8-bytes) at address in x1 and then increment x1 by 8
    sub w2, w2, #1          // Decrement w2
    cbnz w2, 1b             // Loop (go to backward reference 1, 1b) if result w2 not zero

// Setup MMU and cache (we are in exception level 2)
mmu:
//    // Disable L1 Caches
//    mrs x0, SCTLR_EL2       // Read SCTLR_EL2
//    bic X0, X0, #(0x1 << 2) // Disable D Cache
//    msr SCTLR_EL2, X0       // Write SCTLR_EL2
//
//    // Invalidate Data cache
//    //  - Calculate the cache size first and loop through each set + way.
//    mov X0, #0x0            // X0 = Cache level
//    msr CSSELR_EL1, x0      // 0x0 for L1 Dcache 0x2 for L2 Dcache.
//    mrs X4, CCSIDR_EL1      // Read Cache Size ID.
//    and X1, X4, #0x7
//    add X1, X1, #0x4        // X1 = Cache Line Size.
//    ldr X3, =0x7FFF
//    and X2, X3, X4, lsr #13 // X2 = Cache Set Number – 1.
//    ldr X3, =0x3FF
//    and X3, X3, X4, lsr #3  // X3 = Cache Associativity Number – 1.
//    clz W4, W3              // X4 = way position in the CISW instruction.
//    mov X5, #0              // X5 = way counter way_loop.
//way_loop:
//    mov X6, #0              // X6 = set counter set_loop.
//set_loop:
//    lsl X7, X5, X4
//    orr X7, X0, X7          // Set way.
//    lsl X8, X6, X1
//    orr X7, X7, X8          // Set set.
//    DC cisw, X7             // Clean and Invalidate cache line.
//    add X6, X6, #1          // Increment set counter.
//    cmp X6, X2              // Last set reached yet?
//    ble set_loop            // If not, iterate set_loop,
//    add X5, X5, #1          // else, next way.
//    cmp X5, X3              // Last way reached yet?
//    ble way_loop            // If not, iterate way_loop
//
//    // Initialize translation table control registers
//    ldr x1, =0x3520         // 4GB space 4KB granularity
//    // Inner-shareable.
//    msr TCR_EL2, x1         // Normal Inner and Outer Cacheable
//    ldr X1, =0xFF440400     // ATTR0 Device-nGnRnE ATTR1 Device
//    msr MAIR_EL2, X1        // ATTR2 Normal Non-Cacheable
//                            // ATTR3 Normal Cacheable.
//    ADR X0, ttb0_base       // ttb0_base must be a 4KB-aligned address.
//    MSR TTBR0_EL2, X0
//    
//    // Set up translation table entries in memory with looped store instructions.
//    // Set the level 1 translation table.
//    // The first entry points to level2_pagetable.
//    LDR X1, = level2_pagetable // Must be a 4KB align address.
//    LDR X2, =0xFFFFF000
//    AND X2, X1, X2 // NSTable=0 APTable=0 XNTable=0 PXNTable=0.
//    ORR X2, X2, 0x3
//    STR X2, [X0], #8
//    // The second entry is 512MB block from 0x20000000 to 0x3FFFFFFF
//    LDR X2, =0x20000741 // Executable Inner and Outer Shareable.
//    STR X2, [X0], #8 // R/W at all ELs secure memory
//    // AttrIdx=000 Device-nGnRnE.
//    //// The third entry is 1GB block from 0x80000000 to 0xBFFFFFFF.
//    //LDR X2, =0x80000741
//    //STR X2, [X0], #8
//    //// The fourth entry is 1GB block from 0xC0000000 to 0xFFFFFFFF.
//    //LDR X2, =0xC0000741
//    //STR X2, [X0], #8
//    // Set level 2 translation table.
//    LDR X0, =level2_pagetable // Base address of level2_pagetable.
//    LDR X2, =0x0000074D // Executable Inner and Outer Shareable.
//    // R/W at all ELs secure memory.
//    // AttrIdx=011 Normal Cacheable.
//    MOV X4, #256 // Set 256 level2 block entries.
//    LDR X5, =0x00200000 // Increase 2MB address each time.
//loop:
//    STR X2, [X0], #8 // Each entry occupies 2 words.
//    ADD X2, X2, X5
//    SUBS X4, X4, #1
//    BNE loop
//
//    // It is implemented in the CPUECTLR register.
//    MRS X0, S3_1_C15_C2_1
//    ORR X0, X0, #(0x1 << 6) // The SMP bit.
//    MSR S3_1_C15_C2_1, X0
//    
//    // Enable caches and the MMU.
//    MRS X0, SCTLR_EL2
//    ORR X0, X0, #(0x1 << 2) // The C bit (data cache).
//    ORR X0, X0, #(0x1 << 12) // The I bit (instruction cache).
//    ORR X0, X0, #0x1 // The M bit (MMU).
//    MSR SCTLR_EL2, X0
//    DSB SY
//    ISB
    b code

// Jump to code entry point
code:
    bl kernel_main

    // Hang if our code returns
    b  hang

// Hang (infinite loop)
hang:
    wfe                     // Wait for event (low-power)
    b hang

//    // Put a 64-bit value with little endianness.
//    .macro PUT_64B high, low
//    .word \low
//    .word \high
//    .endm
//    // Create an entry pointing to a next-level table.
//    .macro TABLE_ENTRY PA, ATTR
//    PUT_64B \ATTR, (\PA) + 0x3
//    .endm
//    // Create an entry for a 512MB block
//    .macro BLOCK_512MB PA, ATTR_HI, ATTR_LO
//    PUT_64B \ATTR_HI, ((\PA) & 0xC0000000) | \ATTR_LO | 0x1
//    .endm
//    // Create an entry for a 2MB block
//    .macro BLOCK_2MB PA, ATTR_HI, ATTR_LO
//    PUT_64B \ATTR_HI, ((\PA) & 0xFFE00000) | \ATTR_LO | 0x1
//    .endm
//.align 12 // 12 for 4KB granule.
//ttb0_base:
//    TABLE_ENTRY level2_pagetable, 0
//    BLOCK_512MB 0x20000000, 0, 0x740
//.align 12 // 12 for 4KB granule.
//level2_pagetable:
//    .set ADDR, 0x000 // The current page address.
//    .rept 0x200
//    BLOCK_2MB (ADDR << 20), 0, 0x74C
//    .set ADDR, ADDR+2
//    .endr