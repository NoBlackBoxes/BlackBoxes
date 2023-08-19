// NBBPU
// -----------------------------------------
// This is the top module of the NBBPU (CPU)
// -----------------------------------------
module nbbpu(
                clock, 
                reset, 
                instruction, 
                read_data, 
                instruction_enable, 
                read_enable, 
                write_enable, 
                address, 
                write_data, 
                PC, 
                debug_RGB
            );
    
    // Declarations
    input clock;
    input reset;
    input [15:0] instruction;
    input [15:0] read_data;
    output instruction_enable;
    output read_enable;
    output write_enable;
    output [15:0] address;
    output [15:0] write_data;
    output reg [15:0] PC;
    output [2:0] debug_RGB;

    // Parameters (Cycle States)
    parameter FETCH     = 2'b00;    // Fetch next instruction from ROM
    parameter DECODE    = 2'b01;    // Decode instruction and generate control signals
    parameter EXECUTE   = 2'b10;    // Execute instruction inside ALU
    parameter STORE     = 2'b11;    // Store results in memory (register file or RAM)

    // Intermediates
    reg [1:0] current_state;
    reg [1:0] next_state;
    wire [3:0] opcode, _x, x, y, z;
    wire reg_write;
    wire reg_set;
    wire jump_PC;
    wire branch_PC;
    wire branch_or_jump_PC;
    wire [15:0] X;
    wire [15:0] Y;
    wire [15:0] Z;
    reg [15:0] PC_next;

    // Assignments
    assign opcode = instruction[15:12];
    //assign _x = instruction[11:8];
    //assign y = instruction[7:4];
    //assign z = instruction[3:0];
    //assign address = X;             // ??
    //assign write_data = Z;          // ??

    // Sub-module: Controller
    controller controller
    (
        current_state,          // (input) Cycle state
        opcode,                 // (input) Op Code
        instruction_enable,     // (output) Instruction read enable
        read_enable,            // (output) Data read enable
        reg_write,              // (output) Register write enable
        reg_set,                // (output) Register set enable
        write_enable,           // (output) Data write enable
        jump_PC,                // (output) jump PC signal
        branch_PC               // (output) branch PC signal
    );

    // Debug
    //assign instruction_enable = 1'b1;
    reg [31:0] counter; // 32-bit counter
    //assign debug_RGB = {counter[23], counter[23], counter[23]};
    assign debug_RGB = instruction[2:0];

    //// Logic (register set)
    //mux2 #(4) x_mux(_x, z, reg_set, x);
    //
    //// Logic (register file)
    //regfile regfile(clock, reg_write, z, Z, x, y, X, Y);
    //
    //// Logic (branch)
    //assign branch_or_jump_PC = (jump_PC | (Z[0] & branch_PC));
    //
    //// Logic (ALU)
    //alu alu(X, Y, instruction, read_data, PC, Z);

    // Cycle State Machine
    initial 
        begin
            PC = 16'd0;
            counter = 32'd0;
            current_state = FETCH;
        end
    always @(current_state)
        begin
            case(current_state)
                FETCH:
                    begin
                        next_state = DECODE;
                    end
                DECODE:
                    begin
                        next_state = EXECUTE;
                    end
                EXECUTE:
                    begin
                        next_state = STORE;
                    end
                STORE:
                    begin
                        next_state <= FETCH;
                    end
            endcase
        end

    // Update State
    always @(posedge clock, posedge reset)
        begin
            if(reset)
                begin
                    PC <= 16'd0;
                    counter <= 32'd0;
                    current_state <= FETCH;
                end
            else
                begin
                    counter <= counter + 32'd1;
                    if(counter >= 32'h00FFFFFF)
                        begin
                            counter <= 32'd0;
                            PC <= PC + 1;
                            current_state = next_state;
                        end
                end
        end

endmodule