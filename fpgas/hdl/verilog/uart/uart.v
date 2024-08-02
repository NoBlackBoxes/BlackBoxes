// Module: uart
// 
// Notes:
// - Top level module to be used in an implementation.
// - To be used in conjunction with the constraints/defaults.xdc file.
// - Ports can be (un)commented depending on whether they are being used.
// - The constraints file contains a complete list of the available ports
//   including the chipkit/Arduino pins.
//

module uart (
    input               clock,      // Top level system clock input.
    input               resetn,     // Active low reset
    output  wire        uart_txd,   // UART transmit pin.
    output wire[7:0]    left_leds,
    output wire[4:0]    right_leds
);

// Clock frequency in hertz.
parameter CLK_HZ = 12000000;
parameter BIT_RATE =   9600;
parameter PAYLOAD_BITS = 8;

wire        uart_tx_busy;
wire        uart_tx_en;
wire [PAYLOAD_BITS-1:0]  uart_tx_data;

reg[31:0] count;

assign right_leds = 0;
assign uart_tx_en = &count[22:0];

// ------------------------------------------------------------------------- 

// Initialize
initial
    begin
        count <= 0;
    end

    // Logic
    always @(posedge clock)
        begin
            if(!resetn)
                begin
                    count <= 0;
                end
            else
                begin
                    count <= count + 1;
                end
        end

// Report
assign left_leds = count[29:22];
assign uart_tx_data = count[30:23];


// ------------------------------------------------------------------------- 

//
// UART Transmitter module.
//
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