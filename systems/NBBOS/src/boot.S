.section ".text.boot"  // Make sure the linker puts this at the start of the kernel image

.global _start  // Execution starts here

_start:
    // Check processor ID is zero (executing on main core), else hang
    mrs     x1, mpidr_el1
    and     x1, x1, #3
    cbz     x1, 2f
    // We're not on the main core, so hang in an infinite wait loop
1:  wfe
    b       1b
2:  // We're on the main core!

//"================================================================"
//  Initialize Generic Timers for Core0
//"================================================================"
	mrs	x0, cnthctl_el2
	orr	x0, x0, #0x3						/* Enable EL1 access to timers */
	msr	cnthctl_el2, x0
	msr	cntvoff_el2, xzr
	
	/* Not sure if I want this yet */
	mrs	x0, cntkctl_el1
	orr	x0, x0, #0x3						/* Enable EL0 access to timers */
	msr	cntkctl_el1, x0
    
//"================================================================"
//  Initilize MPID/MPIDR registers for all Cores
//"================================================================"
	mrs	x0, midr_el1
	mrs	x1, mpidr_el1
	msr	vpidr_el2, x0
	msr	vmpidr_el2, x1

//"================================================================"
//  Disable coprocessor traps for all Cores
//"================================================================"
	mov	x0, #0x33ff
	msr	cptr_el2, x0						// Disable coprocessor traps to EL2
	msr	hstr_el2, xzr						// Disable coprocessor traps to EL2
	mov	x0, #3 << 20
	msr	cpacr_el1, x0						// Enable FP/SIMD at EL1

//"================================================================"
//  Initialize HCR_EL2 so EL1 is 64 bits for all Cores
//"================================================================"
	mov	x0, #(1 << 31)						// 64bit EL1
	msr	hcr_el2, x0

//"================================================================"
//  Initialize SCTLR_EL1 for all Cores
//"================================================================"
    /*  RES1 bits (29,28,23,22,20,11) to 1
	 *  RES0 bits (31,30,27,21,17,13,10,6) +
	 *  UCI,EE,EOE,WXN,nTWE,nTWI,UCT,DZE,I,UMA,SED,ITD,
	 *  CP15BEN,SA0,SA,C,A,M to 0 */
	mov	x0, #0x0800
	movk	x0, #0x30d0, lsl #16
	orr    x0, x0, #(0x1 << 2)            // The C bit on (data cache). 
	orr    x0, x0, #(0x1 << 12)           // The I bit on (instruction cache)
    msr	sctlr_el1, x0

    // Set stack to start below our code
    ldr     x1, =_start
    mov     sp, x1

    // Clean the BSS section
    ldr     x1, =__bss_start     // Start address
    ldr     w2, =__bss_size      // Size of the section
3:  cbz     w2, 4f               // Quit loop if zero
    str     xzr, [x1], #8
    sub     w2, w2, #1
    cbnz    w2, 3b               // Loop if non-zero

    // Jump to our main() routine in C (make sure it doesn't return)
4:  bl      kernel_main
    // In case it does return, halt the master core too
    b       1b
