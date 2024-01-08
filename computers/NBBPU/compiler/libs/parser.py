# Grammar Rules
# -------------
# Token : (Action)
#
# QUOTE: (Ignore)
# COMMENT: (Ignore)
# KEYWORD:
#   if INT:
#       if Next is ID:
#           if Next is ASSIGN:
#               if next is NUMBER:
#                   if next is SEMICOLON:
#                       (Generate Numeric Assignment code for ID)
#                   else:
#                       (SYNTAX ERROR: Expected ;)                   
#               else:
#                   (SYNTAX ERROR: Expected NUMBER)
#           else:
#               (SYNTAX ERROR: Expected ASSIGN)
#       else:
#           (SYNTAX ERROR: Expected ID)
#    
#    if FOR:
#       ?????         
#
# ID:
#   if Next is ASSIGN:
#       if (ID in symbol table):
#           if Next is NUMBER:
#               if Next is SEMICOLON:
#                   (Generate Numeric Assignment code for ID)
#               else:
#                   (SYNTAX ERROR: Expected ;)                   
#           if Next is ID or Expression?????: (need some recursion!)
#       else:
#           (SYNTAX ERROR: ID not initialized)
#   - next (++): ASSIGN (increment)

#
# I need RecursioN (and Treeish stuff) to deal with nested expressions...hmmm
#

#
# Parser should output SSA or TAC (three address codes)...and control flow stuff
#

#Program -> Block
#Block -> Statement


# Syntax Directed Translation
# - Build some kind of tree based on rules attached to each CFG (context-free-grammar) production


# Simple: Calc Parser

# Program
def Program(tokens, index):
    return Declarations(tokens, index)

# Declarations
def Declarations(tokens, index):
    current = tokens[index]
    declarations = []
    while current is not None:
        declarations.append(Declaration())
    return declarations

# Declaration
def Declaration(tokens, index):
    current = tokens[index]
    if current[1] = 'int':
    


    while current is not None:
        declarations.append(Declaration())
    return declarations


def parse(tokens):
    return Program(tokens, 0)

#FIN