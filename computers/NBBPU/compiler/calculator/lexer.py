class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_char = None
        self.pos = -1
        self.next_char()

    def next_char(self):
        self.pos += 1
        if self.pos >= len(self.source_code):
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.source_code[self.pos]

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.next_char()
            elif self.current_char.isdigit():
                self.tokens.append(self.number())
            elif self.current_char == '+':
                self.tokens.append(Token('ADD', self.current_char))
                self.next_char()
            elif self.current_char == '-':
                self.tokens.append(Token('SUB', self.current_char))
                self.next_char()
            elif self.current_char == '*':
                self.tokens.append(Token('MUL', self.current_char))
                self.next_char()
            elif self.current_char == '/':
                self.tokens.append(Token('DIV', self.current_char))
                self.next_char()
            elif self.current_char == '(':
                self.tokens.append(Token('LPAREN', self.current_char))
                self.next_char()
            elif self.current_char == ')':
                self.tokens.append(Token('RPAREN', self.current_char))
                self.next_char()
            else:
                raise Exception(f"Unknown character: {self.current_char}")

    def number(self):
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.next_char()
        if self.current_char == '.':
            num_str += self.current_char
            self.next_char()
            while self.current_char is not None and self.current_char.isdigit():
                num_str += self.current_char
                self.next_char()
        return Token('NUMBER', float(num_str) if '.' in num_str else int(num_str))

def main():
    expression = "12 + 24 / (3 - 1)"
    lexer = Lexer(expression)
    lexer.tokenize()
    print(lexer.tokens)

if __name__ == "__main__":
    main()
