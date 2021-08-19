# -*- coding: utf-8 -*-
import sys

# Convert HEX dump text to machine code text

# Parse command line input
if(len(sys.argv) == 2):
    input_path = sys.argv[1]
    output_path = input_path[:-4] + 'txt'
else:
    exit("Fail: dump2machine - incorrect input arg count")

# Open input (dump) and output (machine code) files
input_file = open(input_path, "r")
output_file = open(output_path, "w")

# Load input HEX dump (text) file
lines = input_file.readlines()

# Parse input HEX dump file
instruction_count = 0
for line in lines:
    tokens = line.split(' ')
    num_tokens = len(tokens)
    if(num_tokens > 1):
        has_lower = False
        lower = ''
        for token in tokens[1:]:
            if (len(token) == 4) or (len(token) == 5): # with and without newline
                token = token[:4] # Remove newline
                if has_lower:
                    output_file.write((token + lower + '\n').upper())                    
                    has_lower = False
                    instruction_count += 1
                else:
                    lower = token # Store lower byte
                    has_lower = True

# Report
#print("{0} instructions (32-bit words) written to HEX text file.".format(instruction_count))

# Pad memory file with zeros
memory_size = 4096
for i in range(memory_size - instruction_count):
    output_file.write('00000000\n')

# Cleanup
input_file.close()
output_file.close()

#FIN