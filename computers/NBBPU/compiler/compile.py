import sys
import libs.lexer as lexer

# Check for program to compile
if len(sys.argv) != 2:
    print("Usage: python compile.py <program.nbb>")
    exit()

# Extract program file to compile
program_path = sys.argv[1]

# Load program
with open(program_path) as f:
    program = f.read()

# Lex program
tokens = lexer.tokenize(program)

# Report tokens
for t in tokens:
    print(t)
#    if t[0] == 'KEYWORD':
#        print(t)

# Debug
#print(program)
#print(tokens)

