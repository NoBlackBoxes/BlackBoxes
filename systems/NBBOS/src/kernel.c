#include "io.h"
#include "fb.h"

void main()
{
    uart_init();
    fb_init();

    int x = 150;
    while (1)
    {
        drawRect(x,150,400,400,0x03,0);
        drawRect(300,300,350,350,0x2e,1);

        drawCircle(960,540,250,0x0e,0);
        drawCircle(960,540,50,0x13,1);

        drawPixel(250,250,0x0e);

        drawChar('O',500,500,0x05);
        drawString(100,100,"Hello world!",0x0f);

        drawLine(100,500,350,700,0x0c);

        x = x + 1;

        if(x > 1500)
        {
            x = 0;
        }

    }
}
