# To Do:
# - Preserve line numbers (and columns?)
# - Refactor to make super clear
# - ASSIGN!

# Letters List
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
_Letters = ['_'] + lower_case + upper_case

# Digits
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Keyword (reserved) list
Keywords = {
    "int",
    "for",
    "return",
}

# Single Operator dictionary
Single_Operators = {
    '+'             : "BINARYOP",
    '-'             : "BINARYOP",
    '='             : "ASSIGN",
    '!'             : "BINARYOP",
    '<'             : "BINARYOP",
    '>'             : "BINARYOP",
}

# Double Operator dictionary
Double_Operators = {
    '++'            : "BINARYOP",
    '+='            : "BINARYOP",
    '=='            : "BINARYOP",
    '!='            : "BINARYOP",
}

# Single Seperator dictionary
Single_Seperators = {
    "("             : "LEFT_PARENT",
    ")"             : "RIGHT_PARENT",
    "["             : "LEFT_BRACKET",
    "]"             : "RIGHT_BRACKET",
    "{"             : "LEFT_BRACE",
    "}"             : "RIGHT_BRACE",
    ";"             : "SEMICOLON",
}

# Double Seperator dictionary
Double_Seperators = {
    "/*"            : "LEFT_COMMENT",
    "*/"            : "RIGHT_COMMENT",
    "//"            : "LINE_COMMENT",
}

# Whitspace dictionary
Whitespaces = {
    ' '             : "WHITESPACE",
    '\t'            : "WHITESPACE",
    '\n'            : "WHITESPACE",
}

# FSM States
SEEK = 0
TOKEN = 1
COMMENT = 2
QUOTE = 3

# Sets
Operators = Single_Operators | Double_Operators
Seperators = Single_Seperators | Double_Seperators

# Tokenize character array
def tokenize(characters):

    # Number of characters to tokenize
    num_characters = len(characters)

    # Append extra character to avoid out-of-bounds when checking "double-sized" patterns
    characters += '#'

    # Initialize
    tokens = []
    lexeme = ''
    index = 0
    state = SEEK

    # FSM
    while(True):

        # Check for end of characters
        if index >= num_characters:
            break

        # Get current character and next doublet
        c = characters[index]
        cc = c + characters[index + 1]

        # SEEK State
        if SEEK == state:
            if c in Whitespaces:
                index += 1
            else:
                state = TOKEN

        # TOKEN State
        elif TOKEN == state:
            # If lexeme is complete, then tokenize it...
            if (c in Whitespaces | Single_Seperators | Single_Operators) or (cc in Double_Seperators | Double_Operators):
                if lexeme:
                    # Tokenize lexeme (Keyword, Number, or Identifier?)
                    if lexeme in Keywords:
                        tokens.append(('KEYWORD', lexeme))
                    elif (lexeme[0] in Digits) or (lexeme[0] == '-'):
                        for l in lexeme[1:]:
                            if l in Digits:
                                continue
                            else:
                                print("Lex Error: Invalid ID ({0})".format(lexeme))
                                exit(-1)
                        tokens.append(('NUMBER', int(lexeme)))                              
                    else:
                        tokens.append(('ID', lexeme))
                lexeme = ''
                state = SEEK
            # ...otherwise concat character and continue
            else:
                lexeme += c
                index += 1
                continue

            # Handle Seperators and Operators
            if c in Single_Seperators:
                tokens.append((Single_Seperators[c], c))
                index += 1
                state = SEEK
            elif c in Single_Operators:
                if (c == '-') and (cc[1] in Digits):
                    lexeme += c
                    index += 1
                    continue                 
                else:
                    tokens.append((Single_Operators[c], c))
                    index += 1
                    state = SEEK
            elif cc in Double_Seperators:
                if cc == '//':
                    lexeme = ''
                    index += 2
                    state = COMMENT
                elif cc == '/*':
                    lexeme = ''
                    index += 2
                    state = QUOTE
                else:
                    lexeme = ''                   

        # COMMENT State
        elif COMMENT == state:
            if c == '\n':
                tokens.append(('COMMENT', lexeme))
                lexeme = ''
                index += 1
                state = SEEK
            else:
                lexeme += c
                index += 1

        # QUOTE State
        elif QUOTE == state:
            if cc == '*/':
                tokens.append(('QUOTE', lexeme))
                lexeme = ''
                index += 2
                state = SEEK
            else:
                lexeme += c
                index += 1

    return tokens

