// Controller (RV32I)
module controller(opcode, funct3, funct7b5, zero, result_select, mem_write, PC_select, ALU_select, reg_write, jump, immediate_select, ALU_control);

    // Declarations
    input [6:0] opcode;
    input [2:0] funct3;  
    input funct7b5;
    input zero;
    output [1:0] result_select;
    output mem_write;
    output PC_select;
    output ALU_select;
    output reg_write;
    output jump;
    output [1:0] immediate_select;
    output [2:0] ALU_control;
    
    // Intermediates
    wire [1:0] ALU_op;
    wire branch;
    
    // Main Decoder Sub-module
    main_decoder main_decoder
    (
        opcode,             // (input)
        reg_write,          // (output)
        immediate_select,   // (output)
        ALU_select,         // (output)
        mem_write,          // (output)
        result_select,      // (output)
        branch,             // (output)
        ALU_op,             // (output)
        jump                // (output)
    );
    
    // ALU Decoder Sub-module
    alu_decoder alu_decoder
    (
        opcode[5],      // (input) opcode_b5
        funct3,         // (input)
        funct7b5,       // (input)
        ALU_op,         // (input)
        ALU_control     // (output)
    );

    // Program Counter update (?)   
    assign PC_select = branch & zero | jump;
    
endmodule