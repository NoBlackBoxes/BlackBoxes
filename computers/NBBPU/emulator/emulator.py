import os
import sys
import numpy as np
from libs.opcodes import OpCodes
from libs.operations import operation

# Define state
pc = 0
registers = np.zeros(16, dtype=np.int16)
ram = np.zeros(256, dtype=np.int16)
state  = {'pc' : pc, 'registers' : registers, 'ram' : ram}

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

    # Seperate instrution nibbles
    op = line[0]
    x = int(line[1], 16)
    y = int(line[2], 16)
    z = int(line[3], 16)

    # Run operation
    operation(OpCodes[op], x, y, z, state)

    # Report
    print("{0:03d}: {1} {2} {3} {4}".format(instruction_count, OpCodes[op], x, y, z))
    print("{0}".format(state['registers']))

    # Increment instruction count
    instruction_count = instruction_count + 1

    # DEBUG
    if instruction_count > 5:
        print(instruction_count)
        break

# Shutdown
input_file.close()

#FIN


