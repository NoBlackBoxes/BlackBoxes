import sys
import libs.lexer

# Check for program to compile
if len(sys.argv) != 2:
    print("Usage: python compile.py <program.nbb>")
    exit()

# Extract input file to compile
input_path = sys.argv[1]

# Open file
input_file = open(input_path, 'r')

# Load program
lines = input_file.readlines()

# Debug
print(lines)

