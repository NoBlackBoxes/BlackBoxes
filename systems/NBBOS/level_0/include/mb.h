extern volatile unsigned int mbox[36];

enum {
    MBOX_REQUEST  = 0
};

enum {
    MBOX_CH_POWER = 0,
    MBOX_CH_FB    = 1,
    MBOX_CH_VUART = 2,
    MBOX_CH_VCHIQ = 3,
    MBOX_CH_LEDS  = 4,
    MBOX_CH_BTNS  = 5,
    MBOX_CH_TOUCH = 6,
    MBOX_CH_COUNT = 7,
    MBOX_CH_PROP  = 8 // Request from ARM for response by VideoCore
};

enum {
    /* Frame buffer */
    MBOX_TAG_SETPHYWH   = 0x48003,
    MBOX_TAG_SETVIRTWH  = 0x48004,
    MBOX_TAG_SETVIRTOFF = 0x48009,
    MBOX_TAG_SETDEPTH   = 0x48005,
    MBOX_TAG_SETPXLORDR = 0x48006,
    MBOX_TAG_GETFB      = 0x40001,
    MBOX_TAG_GETPITCH   = 0x40008,

    /* Clocks */
    MBOX_TAG_GET_CLOCK_STATE = 0x30001,
    MBOX_TAG_SET_CLOCK_STATE = 0x38001,
    MBOX_TAG_GET_CLOCK_RATE = 0x30002,
    MBOX_TAG_SET_CLOCK_RATE = 0x38002,
    MBOX_TAG_GET_MAX_CLOCK_RATE = 0x30004,
    MBOX_TAG_GET_MIN_CLOCK_RATE = 0x30007,
    MBOX_TAG_GET_TURBO = 0x30009,
    MBOX_TAG_SET_TURBO = 0x38009,
    
    MBOX_TAG_LAST       = 0
};

void mmio_write(long reg, unsigned int val);
unsigned int mmio_read(long reg);

unsigned int mbox_call(unsigned char ch);
