class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.next_token()
        else:
            raise Exception(f"Unexpected token: {self.current_token}, expected: {token_type}")

    def parse(self):
        # Start the parsing process
        return self.program()

    def program(self):
        # Assuming 'Program' -> 'DeclarationString'
        return self.declaration_string()

    def declaration_string(self):
        # Implement 'DeclarationString' -> 'Declaration'
        # or 'DeclarationString' -> 'DeclarationString' 'Declaration'
        declarations = []
        while self.current_token is not None:
            declarations.append(self.declaration())
        return declarations

    def declaration(self):
        # Implement 'Declaration' -> 'int' 'ID' 'DeclarationType'
        # or 'Declaration' -> 'void' 'ID' 'FunctionDeclaration'
        if self.current_token.type in ['int', 'void']:
            decl_type = self.current_token.value
            self.eat(self.current_token.type)
            identifier = self.current_token.value
            self.eat('ID')
            if decl_type == 'int':
                return self.declaration_type(identifier)
            elif decl_type == 'void':
                return self.function_declaration(identifier)

    def declaration_type(self, identifier):
        # Implement 'DeclarationType' -> 'VariableDeclaration'
        self.eat('END')
        return {'type': 'VariableDeclaration', 'identifier': identifier}

    def function_declaration(self, identifier):
        # Implement 'FunctionDeclaration' -> '(' 'Parameters' ')' 'StatementBlock'
        self.eat('(')
        # Add parsing for 'Parameters' and 'StatementBlock'
        self.eat(')')
        return {'type': 'FunctionDeclaration', 'identifier': identifier}

    # Add methods for other non-terminals in your grammar
    # ...

def main():
    source_code = """
    int x;
    void myFunction()
    """
    lexer = Lexer(source_code)
    tokens = lexer.get_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)

if __name__ == "__main__":
    main()
