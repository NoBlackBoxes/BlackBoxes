// NBBPU
// -----------------------------------------
// This is the top module of the NBBPU (CPU). It receives a clock, reset signal, and 16-bit instruction.
// It also receives "read_data" coming from RAM.
// It outputs a control signal for memory ("write_enable"), the address to write to ("wrtie_address"),
// and the value to write ("write_data").
// It also updates the the value of the program counter (PC) to retrieve the next instruction.
//
// Not all of the outputs (or inputs) are used for every instruction,
// but the connections always exist and the logic decides what gets used and what is ignored.
//
// The nbbpu module invokes two sub-modules (controller and datapath)
// -----------------------------------------
module nbbpu(clock, reset, instruction, read_data, write_enable, address, write_data, PC);
    
    // Declarations
    input clock;
    input reset;
    input [15:0] instruction;
    input [15:0] read_data;
    output write_enable;
    output [15:0] address;
    output [15:0] write_data;
    output [15:0] PC;


    // Need to set address and write data somewhere in datapath!


    // Intermediates
    wire reg_write_lower;
    wire reg_write_upper;
    wire reg_set;
    wire write_enable;
    wire PC_select;

    // Sub-module: Controller
    controller controller
    (
        instruction[15:12],     // (input) Opcode
        reg_write_lower,        // (output) Register write (lower byte) enable
        reg_write_upper,        // (output) Register write (upper byte) enable
        reg_set,                // (output) Register set enable
        write_enable,           // (output) Data write enable
        PC_select               // (output) PC select signal
    );

    // Sub-module: Datapath
    datapath datapath
    (
        clock,                  // (input) clock
        reset,                  // (input) reset
        instruction,            // (input) instruction
        reg_write_lower,        // (input) reg_write_lower
        reg_write_upper,        // (input) reg_write_upper
        reg_set,                // (input) reg_set
        PC_select,              // (input) PC select signal
        read_data,              // (input) read_data
        write_data,             // (output) write_data
        PC                      // (output) PC
    );

endmodule