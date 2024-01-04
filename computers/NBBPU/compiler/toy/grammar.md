Program
└── DeclarationString
    ├── Declaration
    │   ├── VariableDeclaration
    │   │   └── int ID ;
    │   └── FunctionDeclaration
    │       ├── void ID ( Parameters ) StatementBlock
    │       └── int ID ( Parameters ) StatementBlock
    └── DeclarationString Declaration

Parameters
├── ParameterList
│   ├── Parameter
│   │   └── int ID
│   └── ParameterList , Parameter
└── void

StatementBlock
├── { InternalDeclaration StatementString }
└── { }

InternalDeclaration
├── NULL
└── InternalDeclaration InternalVariableDeclaration ;

InternalVariableDeclaration
├── int ID
└── double ID

StatementString
├── Statement
├── StatementString Statement
└── NULL

Statement
├── ifStatement
├── whileStatement
├── returnStatement
└── AssignmentStatement

ifStatement
├── if ( Expression ) StatementBlock elseStatement
└── if ( Expression ) StatementBlock

elseStatement
├── else StatementBlock
└── NULL

whileStatement
└── while ( Expression ) StatementBlock

returnStatement
├── return ReturnValue
└── return ;

ReturnValue
├── Expression ;
└── ;

AssignmentStatement
└── ID = Expression ;

Expression
├── AdditiveExpression
└── Expression relop AdditiveExpression

--------------

1. **Program**: This is the top-level non-terminal in the grammar. It represents the entire code of a program in this language. It typically consists of a series of declarations, which can be either variable declarations or function declarations.

2. **DeclarationString**: This non-terminal represents a sequence of declarations. It can be a single declaration or multiple declarations. It's used to define the global scope of the program, where variables and functions are declared.

3. **Declaration**: A declaration is a statement where a variable or a function is declared. In the context of your grammar, a declaration can either be a variable declaration or a function declaration.

4. **VariableDeclaration**: This represents the declaration of a variable. It typically includes a type specification (like `int` or `double`) and an identifier (variable name). For instance, `int x;` is a variable declaration.

5. **FunctionDeclaration**: This is the declaration of a function. It includes the return type (`void` or `int`), the function name (identifier), parameters (enclosed in parentheses), and the function's body (enclosed in curly braces).

6. **Parameters**: This non-terminal represents the list of parameters that a function takes. Parameters can be a list of typed variables, or it can be `void` to signify that the function takes no parameters.

7. **StatementBlock**: A statement block is a compound statement enclosed in curly braces `{}`. It represents a scope and contains a sequence of statements and/or internal declarations.

8. **InternalDeclaration**: These are declarations that occur inside a function or a block. They are typically variable declarations.

9. **StatementString**: This non-terminal represents a sequence of statements. It can be a single statement or multiple statements.

10. **Statement**: A statement is the smallest standalone element of the language that expresses some action to be carried out. Statements include control flow statements (`if`, `while`), return statements, and assignment statements.

11. **Expression**: An expression is a combination of one or more constants, variables, operators, and functions that the programming language interprets (according to its particular rules of precedence and of association) and computes to produce another value. Expressions include arithmetic expressions, boolean expressions, and more.

12. **ifStatement**, **whileStatement**, **returnStatement**, **AssignmentStatement**: These are specific types of statements. `ifStatement` represents conditional execution, `whileStatement` denotes a loop, `returnStatement` is used for returning a value from a function, and `AssignmentStatement` is used for assigning a value to a variable.

These non-terminals form the backbone of the programming language's syntax as defined by your grammar. Each non-terminal encapsulates a specific aspect of the language's structure, and together, they define how valid programs are constructed in the language.