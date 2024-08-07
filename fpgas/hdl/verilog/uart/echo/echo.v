// UART (Echo)
module uart (clock, reset, rx_pin, tx_pin, left_leds, right_leds);

    // Declarations
    input  clock;                   // Clock Input
    input  reset;                   // Asynchronous Reset
    input  rx_pin;                  // Receive Pin
    output tx_pin;                  // Transmit Pin
    output [7:0] left_leds;         // Reporter LEDs
    output [4:0] right_leds;        // Idle LEDs

    // Parameters
    parameter CLK_HZ = 12000000;    // Clock frequency in Hz
    parameter BIT_RATE =   9600;    // Bits per second

    wire rx_valid;
    wire rx_break;
    wire [7:0] rx_byte;
    wire tx_busy;
    wire tx_enable;
    wire [7:0] tx_byte;

    // Report
    assign right_leds = 0;
    assign left_leds = rx_byte;

    // Echo
    assign tx_byte = rx_byte;
    assign tx_enable = rx_valid;

    // UART Receiver module
    rx #(
        .BIT_RATE(BIT_RATE),
        .PAYLOAD_BITS(PAYLOAD_BITS),
        .CLK_HZ  (CLK_HZ)
        ) i_uart_rx(
        .clk          (clock        ), // Top level system clock input.
        .resetn       (resetn       ), // Asynchronous active low reset.
        .uart_rxd     (rx_pin       ), // UART Recieve pin.
        .uart_rx_en   (1'b1         ), // Recieve enable
        .uart_rx_break(uart_rx_break), // Did we get a BREAK message?
        .uart_rx_valid(uart_rx_valid), // Valid data recieved and available.
        .uart_rx_data (uart_rx_data )  // The recieved data.
    );

    // UART Transmitter module
    tx #(
        .BIT_RATE(BIT_RATE),
        .PAYLOAD_BITS(PAYLOAD_BITS),
        .CLK_HZ  (CLK_HZ  )
        ) i_uart_tx(
        .clk          (clock        ),
        .resetn       (resetn       ),
        .uart_txd     (uart_txd     ),
        .uart_tx_en   (uart_tx_en   ),
        .uart_tx_busy (uart_tx_busy ),
        .uart_tx_data (uart_tx_data ) 
    );

endmodule