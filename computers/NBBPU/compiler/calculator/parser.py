# Make sure to import the Lexer and Token classes from lexer.py
from lexer import Lexer, Token

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.next_token()

    def pretty_print(self, node, prefix="", is_left=True):
            if node is not None:
                # Determine the line connector and the next prefix
                if is_left:
                    line_connector = "└── "
                    next_prefix = prefix + "    "
                else:
                    line_connector = "┌── "
                    next_prefix = prefix + "|   "

                # Print the current node
                print(prefix + line_connector + str(node.value))

                # Recursively print the left and right children
                if node.left is not None or node.right is not None:
                    if node.right is not None:
                        self.pretty_print(node.right, next_prefix, False)
                    if node.left is not None:
                        self.pretty_print(node.left, next_prefix, True)

    def next_token(self):
        self.current_token = self.lexer.tokens.pop(0) if self.lexer.tokens else None

    def parse(self):
        return self.expression()

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.next_token()
            return Node(token.value)
        elif token.type == 'LPAREN':
            self.next_token()
            node = self.expression()
            if self.current_token.type != 'RPAREN':
                raise Exception("Missing closing parenthesis")
            self.next_token()
            return node
        else:
            raise Exception(f"Invalid syntax")

    def term(self):
        node = self.factor()
        while self.current_token is not None and self.current_token.type in ['MUL', 'DIV']:
            token = self.current_token
            self.next_token()
            node = Node(token.type, left=node, right=self.factor())
        return node

    def expression(self):
        node = self.term()
        while self.current_token is not None and self.current_token.type in ['ADD', 'SUB']:
            token = self.current_token
            self.next_token()
            node = Node(token.type, left=node, right=self.term())
        return node

    def evaluate(self, node):
        if node is None:
            return 0

        if node.value == 'ADD':
            return self.evaluate(node.left) + self.evaluate(node.right)
        elif node.value == 'SUB':
            return self.evaluate(node.left) - self.evaluate(node.right)
        elif node.value == 'MUL':
            return self.evaluate(node.left) * self.evaluate(node.right)
        elif node.value == 'DIV':
            return self.evaluate(node.left) / self.evaluate(node.right)
        else:
            # Assume the node is a number
            return node.value

def main():
    expression = "120 * 24 / ((30*2) - (100-50))"
    lexer = Lexer(expression)
    lexer.tokenize()
    parser = Parser(lexer)
    ast = parser.parse()

    print("Abstract Syntax Tree:")
    parser.pretty_print(ast)

    result = parser.evaluate(ast)
    print("\nResult of the expression:", result)

if __name__ == "__main__":
    main()
