# -*- coding: utf-8 -*-
import sys

# Convert HEX (text) dump of .data section to machine data file

# Parse command line input
if(len(sys.argv) == 2):
    input_path = sys.argv[1]
    output_path = input_path[:-9] + 'text_data'
else:
    exit("Fail: dump2machine_data - incorrect input arg count")

# Open input (dump) and output (machine data) file
input_file = open(input_path, "r")
output_file = open(output_path, "w")

# Load input HEX dump (text) file
lines = input_file.readlines()

# Parse input HEX dump file
data_count = 0
for line in lines:
    tokens = line.split(' ')
    num_tokens = len(tokens)
    if(num_tokens > 1):
        for token in tokens[1:]:
            if (len(token) == 4) or (len(token) == 5): # with and without newline
                token = token[:4] # Remove newline
                output_file.write((token[2:4] + '\n').upper())                    
                output_file.write((token[0:2] + '\n').upper())                    
                data_count += 2

# Report
#print("{0} data (32-bit words) written to HEX text file.".format(data_count))

# Pad memory file with zeros
memory_size = 4096
for i in range(memory_size - data_count):
    output_file.write('00\n')

# Cleanup
input_file.close()
output_file.close()

#FIN