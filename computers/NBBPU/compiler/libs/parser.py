from languages.nbbc import *
from libs.token import Token

# Parser Class
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = None
        self.next()

    def next(self):
        self.current = self.tokens.pop(0) if self.tokens else None
        if self.current.type == 'COMMENT':
            self.next()
        return

    def eat_type(self, token_type):
        if self.current.type == token_type:
            self.next()
        else:
            print(f"Syntax Error: Unexpected token type ({self.current}, expected: {token_type}) at {self.current.line}")
            exit(-1)
        return

    def eat_name(self, token_name):
        if self.current.name == token_name:
            self.next()
        else:
            print(f"Syntax Error: Unexpected token name ({self.current}, expected: {token_name}) at {self.current.line}")
            exit(-1)
        return

    def parse(self):
        return self.program()

    # Semantic Analysis
    # ------------------

    # Program
    def program(self):
        return self.declarations()

    # Declarations
    def declarations(self):
        declarations = []
        while self.current is not None:
            declarations.append(self.declaration())
        return declarations

    # Declaration
    def declaration(self):
        if self.current.name in ['int', 'void']:
            declaration_name = self.current.name
            self.eat_name(self.current.name)
            identifier = self.current.name
            self.eat_type('ID')
            if declaration_name == 'int':
                return self.declaration_type(identifier)
            elif declaration_name == 'void':
                return self.function_declaration(identifier)
        else:
            print(self.current)
            print(f"Syntax Error: Invalid Declaration at {self.current.line}")
            exit(-1)
            
    # Declaration Type
    def declaration_type(self, identifier):
        if self.current.value == '=':
            self.eat_name('ASSIGN')
            if self.current.type == 'NUMBER':
                print(f"{identifier} = {self.current.value}")                
                self.eat_type('NUMBER')
            elif self.current.type == 'ID':
                print(f"{identifier} = {self.current.name}")                
                self.eat_type('ID')
            self.eat_name('SEMICOLON')
        else:
            self.eat_name('SEMICOLON')
        return {'type': 'VariableDeclaration', 'identifier': identifier}

    # Function Declaration
    def function_declaration(self, identifier):
        # Implement 'FunctionDeclaration' -> '(' 'Parameters' ')' 'StatementBlock'
        self.eat_name('LEFT_PARENT')
        # Add parsing for 'Parameters' and 'StatementBlock'
        self.eat_name('RIGHT_PARENT')
        print(f"function ({identifier})")
        return {'type': 'FunctionDeclaration', 'identifier': identifier}

#FIN