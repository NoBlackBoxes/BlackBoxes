// Main Decoder
module main_decoder(opcode, reg_write, ALU_select, memory_control, result_select, branch, ALU_op, jump);

    // Declarations
    input [6:0] opcode;
    output reg_write;
    output ALU_select;
    output [3:0] memory_control;
    output [2:0] result_select;
    output branch;
    output [1:0] ALU_op;
    output jump;
    
    // Intermediates
    reg [12:0] controls;
    assign {reg_write, ALU_select, memory_control, result_select, branch, ALU_op, jump} = controls;   
    
    // Logic
    always @*
        case(opcode)      
            // reg_write - ALU_select - memory_control - result_select - branch - ALU_op - jump
            7'b0000011: controls = 13'b1_1_0000_001_0_00_0; // lw
            7'b0100011: controls = 13'b0_1_0001_000_0_00_0; // sw
            7'b0110011: controls = 13'b1_0_0000_000_0_10_0; // R–type
            7'b0010111: controls = 13'b1_0_0000_100_0_00_0; // auipc
            7'b0110111: controls = 13'b1_0_0000_011_0_00_0; // lui
            7'b1100011: controls = 13'b0_0_0000_000_1_01_0; // beq, bne, blt, bge, bgeu, bltu
            7'b0010011: controls = 13'b1_1_0000_000_0_10_0; // I–type ALU
            7'b1100111: controls = 13'b1_1_0000_010_0_00_1; // jalr
            7'b1101111: controls = 13'b1_0_0000_010_0_00_1; // jal
            default:    controls = 13'bx_x_xxxx_xxx_x_xx_x; // ???   
        endcase

endmodule