// Debug (UART)
module debug (clock, tx_pin, leds, blank);

    // Declarations
    input wire  clock;          // System Clock
    input wire  reset;          // Signal Reset
    output wire tx_pin;         // UART transmit pin.
    output wire [7:0] leds;     // Reporter LEDs
    output wire [4:0] blank;    // Blanked LEDs

    // Parameters
    parameter CLOCK_HZ = 12_000_000;
    parameter BAUD_RATE = 9600;

    wire uart_tx_busy;
    wire uart_tx_en;
    wire [7:0] tx_byte;

    reg[31:0] count;

    assign blank = 0;
    assign uart_tx_en = &count[22:0];

    // Initialize
    initial
        begin
            count <= 0;
        end

    // Logic
    always @(posedge clock)
        begin
            if(reset)
                count <= 0;
            else
                count <= count + 1;
        end

    // Report
    assign leds = count[29:22];
    assign tx_byte = count[30:23];

    // UART Transmitter (Tx) module
    tx #(.BIT_RATE(BIT_RATE), .CLOCK_HZ(CLOCK_HZ)) uart_tx(
        .clk          (clock        ),
        .resetn       (resetn       ),
        .uart_txd     (uart_txd     ),
        .uart_tx_en   (uart_tx_en   ),
        .uart_tx_busy (uart_tx_busy ),
        .uart_tx_data (uart_tx_data ) 
    );

endmodule