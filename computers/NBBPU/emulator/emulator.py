import os
import sys
from libs.opcodes import OpCodes

# Check for program to emulate
if len(sys.argv) != 2:
    print("Usage: python emmulator.py <executable.rom>")
    exit()

# Extract input file to emulate
input_path = sys.argv[1]

# Open files
input_file = open(input_path, 'r')

# Emulate
emulating = True
instruction_count = 0
while emulating:
    # Read line
    line = input_file.readline()

    # Is finished? Stop.
    if not line:
        emulating = False
        continue

    # Seperate code bytes
    op = line[0]
    x = line[1]
    y = line[2]
    z = line[3]

    # Report
    print("{0} {1} {2} {3}".format(OpCodes[op], x, y, z))

    # Increment instruction count
    instruction_count = instruction_count + 1

# Shutdown
input_file.close()

#FIN


