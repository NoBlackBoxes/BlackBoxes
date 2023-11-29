#include "io.h"
#include "fb.h"

void main()
{
    uart_init();
    fb_init();

    int rg = 0;
    while (1)
    {
        if(rg == 1)
        {
            fillBackground(0x04);
            rg = 0;
        }
        else
        {
            fillBackground(0x02);
            rg = 1;
        }
    }
}
