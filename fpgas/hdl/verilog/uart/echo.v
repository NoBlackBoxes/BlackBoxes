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
    input   wire        uart_rxd,   // UART Recieve pin.
    output  wire        uart_txd,   // UART transmit pin.
    output wire[7:0]    left_leds,
    output wire[4:0]    right_leds
);

// Clock frequency in hertz.
parameter CLK_HZ = 12000000;
parameter BIT_RATE =   9600;
parameter PAYLOAD_BITS = 8;

wire [PAYLOAD_BITS-1:0]  uart_rx_data;
wire        uart_rx_valid;
wire        uart_rx_break;

wire        uart_tx_busy;
wire [PAYLOAD_BITS-1:0]  uart_tx_data;
wire        uart_tx_en;

assign right_leds = 0;

// ------------------------------------------------------------------------- 

// Report
assign left_leds = uart_rx_data;

// Echo
assign uart_tx_data = uart_rx_data;
assign uart_tx_en   = uart_rx_valid;

// ------------------------------------------------------------------------- 

//
// UART RX
rx #(
    .BIT_RATE(BIT_RATE),
    .PAYLOAD_BITS(PAYLOAD_BITS),
    .CLK_HZ  (CLK_HZ)
    ) i_uart_rx(
    .clk          (clock        ), // Top level system clock input.
    .resetn       (resetn       ), // Asynchronous active low reset.
    .uart_rxd     (uart_rxd     ), // UART Recieve pin.
    .uart_rx_en   (1'b1         ), // Recieve enable
    .uart_rx_break(uart_rx_break), // Did we get a BREAK message?
    .uart_rx_valid(uart_rx_valid), // Valid data recieved and available.
    .uart_rx_data (uart_rx_data )  // The recieved data.
);

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