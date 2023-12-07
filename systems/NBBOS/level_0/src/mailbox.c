#include "defs.h"
#include "mailbox.h"

// The buffer must be 16-byte aligned as only the upper 28 bits of the address can be passed via the mailbox
volatile uint32_t __attribute__((aligned(16))) mailbox[36];

// Declarations
uint32_t mailbox_call(unsigned char ch)
{
    // 28-bit address (MSB) and 4-bit value (LSB)
    uint32_t r = ((uint32_t)((long) &mailbox) &~ 0xF) | (ch & 0xF);

    // Wait until we can write
    while (GET32(MBOX_STATUS) & MBOX_FULL);
    
    // Write the address of our buffer to the mailbox with the channel appended
    PUT32(MBOX_WRITE, r);

    while (1) {
        // Is there a reply?
        while (GET32(MBOX_STATUS) & MBOX_EMPTY);

        // Is it a reply to our message?
        if (r == GET32(MBOX_READ)) return mailbox[1]==MBOX_RESPONSE; // Is it successful?
    }
    return 0;
}
