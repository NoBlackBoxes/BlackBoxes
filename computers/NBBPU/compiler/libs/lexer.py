from languages.nbbc import *
from libs.token import Token

# Lexer FSM States
SEEK = 0
TOKEN = 1
LINE_COMMENT = 2
BLOCK_COMMENT = 3

# Lexer Class
class Lexer:
    def __init__(self, characters):
        self.characters = characters
        self.num_characters = len(characters)
        self.tokens = []

        # Build "line number" array for debugging
        self.lines = []
        count = 1
        for c in self.characters:
            self.lines.append(count)
            if c == '\n':
                count += 1
        
        # Append '#' character to avoid out-of-bounds
        self.characters += '#'

    def tokenize(self):
        lexeme = ''
        index = 0
        state = SEEK

        # Lexer FSM
        while(True):

            # Check for end of characters
            if index >= self.num_characters:
                break

            # Get current character and next doublet
            c = self.characters[index]
            cc = c + self.characters[index + 1]

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
                            self.tokens.append(Token('KEYWORD', lexeme, None, self.lines[index]))
                        elif (lexeme[0] in Digits) or (lexeme[0] == '-'):
                            for l in lexeme[1:]:
                                if l in Digits:
                                    continue
                                else:
                                    print(f"Lexer Error: Invalid ID ({lexeme} at Line: {self.lines[index]})")
                                    exit(-1)
                            self.tokens.append(Token('NUMBER', 'integer', int(lexeme), self.lines[index]))
                        else:
                            self.tokens.append(Token('ID', lexeme, None, self.lines[index]))
                    lexeme = ''
                    state = SEEK
                # ...otherwise concat character and continue
                else:
                    lexeme += c
                    index += 1
                    continue
                # Handle Seperators and Operators
                if c in Single_Seperators:
                    self.tokens.append(Token('SEPERATOR', Single_Seperators[c], c, self.lines[index]))
                    index += 1
                    state = SEEK
                elif c in Single_Operators:
                    if (c == '-') and (cc[1] in Digits):
                        lexeme += c
                        index += 1
                        continue                 
                    else:
                        self.tokens.append(Token('OPERATOR', Single_Operators[c], c, self.lines[index]))
                        index += 1
                        state = SEEK
                elif cc in Double_Seperators:
                    if cc == '//':
                        lexeme = ''
                        index += 2
                        state = LINE_COMMENT
                    elif cc == '/*':
                        lexeme = ''
                        index += 2
                        state = BLOCK_COMMENT
                    else:
                        lexeme = ''                   

#                elif cc in Double_Seperators:
#                    if cc == '//':
#                        lexeme = ''
#                        index += 2
#                        state = LINE_COMMENT
#                    elif cc == '/*':
#                        lexeme = ''
#                        index += 2
#                        state = BLOCK_COMMENT
#                    else:
#                        lexeme = ''                   

            # LINE_COMMENT State
            elif LINE_COMMENT == state:
                if c == '\n':
                    self.tokens.append(Token('COMMENT', 'LINE', lexeme, self.lines[index]))
                    lexeme = ''
                    index += 1
                    state = SEEK
                else:
                    lexeme += c
                    index += 1

            # BLOCK_COMMENT State
            elif BLOCK_COMMENT == state:
                if cc == '*/':
                    self.tokens.append(Token('COMMENT', 'BLOCK', lexeme, self.lines[index]))
                    lexeme = ''
                    index += 2
                    state = SEEK
                else:
                    lexeme += c
                    index += 1

        return self.tokens

