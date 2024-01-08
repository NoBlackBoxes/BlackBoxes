# Keyword (reserved) list
Keywords = {
    "int",
    "for",
    "return",
}

# Single Operator dictionary
Single_Operators = {
    '='             : "ASSIGN",
    '+'             : "BINARY",
    '-'             : "BINARY",
    '!'             : "UNARY",
    '<'             : "BINARY",
    '>'             : "BINARY",
}

# Double Operator dictionary
Double_Operators = {
    '--'            : "ASSIGN",
    '++'            : "ASSIGN",
    '+='            : "ASSIGN",
    '-='            : "ASSIGN",
    '=='            : "BINARY",
    '!='            : "BINARY",
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

# Sets
Operators = Single_Operators | Double_Operators
Seperators = Single_Seperators | Double_Seperators

# Letters
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
_Letters = ['_'] + lower_case + upper_case

# Digits
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
