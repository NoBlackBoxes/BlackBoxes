# Expression Parser Grammar

The expression parser is designed to handle basic arithmetic expressions. The grammar is defined using a context-free grammar (CFG). The CFG for this parser is described below:

## Non-Terminals
- `Expression`: Represents an arithmetic expression.
- `Term`: Represents a term within an expression, handling multiplication and division.
- `Factor`: Represents a factor within a term, handling numbers and parenthesized expressions.

## Terminals
- `NUMBER`: A numeric value (integer or decimal).
- `ADD`: The addition operator (`+`).
- `SUB`: The subtraction operator (`-`).
- `MUL`: The multiplication operator (`*`).
- `DIV`: The division operator (`/`).
- `LPAREN`: Left parenthesis (`(`).
- `RPAREN`: Right parenthesis (`)`).

## Production Rules
```python
Expression -> Term (('ADD' | 'SUB') Term)*
Term -> Factor (('MUL' | 'DIV') Factor)*
Factor -> 'NUMBER' | 'LPAREN' Expression 'RPAREN'
```

### Explanation
1. **Expression**:
   - An `Expression` consists of one or more `Term`s.
   - `Term`s can be combined using addition (`ADD`) or subtraction (`SUB`) operators.
   - The use of `*` in the production rule indicates repetition (zero or more times).

2. **Term**:
   - A `Term` consists of one or more `Factor`s.
   - `Factor`s can be combined using multiplication (`MUL`) or division (`DIV`) operators.
   - Similar to `Expression`, the `*` in the production rule signifies repetition.

3. **Factor**:
   - A `Factor` is either a `NUMBER` or an `Expression` enclosed within parentheses.
   - This allows the grammar to handle basic numbers and nested expressions.

## Example Expressions
- `12 + 24 / (3 - 1)`
- `7 * (5 - 2)`
- `42 / 6 + 3.5`

The grammar supports arithmetic expressions with standard operator precedence and associativity. Parentheses can be used to group expressions and override the default precedence.

---
