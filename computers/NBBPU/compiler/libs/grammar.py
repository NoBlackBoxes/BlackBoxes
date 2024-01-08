# Grammar for NBB language
# ------------------------
#
# Program
# └── Declarations
#     ├── Declaration
#     │   ├── "int ID"
#     │   │   └── Declaration_Type
#     │   │       ├── Variable_Declaration
#     │   │       │   └── ";"    
#     │   │       └── Function_Declaration
#     │   │           └── "(" Parameters ")" StatementBlock
#     │   └── "void ID"
#     │           └── Function_Declaration
#     │               └── "(" Parameters ") StatementBlock
#     └── Declarations, Declaration
#
# Parameters
# ├── ParameterList
# │   ├── Parameter
# │   │   └── "int ID"
# │   └── ParameterList, Parameter
# └── void

# Production dictionary
Productions = {
    'Program'               : [(['Declarations']                            , 'Program: Declarations')],
    'Declarations'          : [(['Declaration']                             , 'Declarations: -single-'),
                               (['Declarations', 'Declaration']             , 'Declarations: -multiple-')],
}

#    'Declaration'           : (['int', 'ID', 'Declaration_Type']            , print('Declaration: int ID Declation_Type')),
#    'Declaration'           : (['void', 'ID', 'Function_Declaration']       , print('Declaration: void ID Function_Declaration')),
#    'Declaration_Type'      : (['Variable_Declaration']                     , print('Declaration_Type: Variable_Declaration')),
#    'Declaration_Type'      : (['Function_Declaration']                     , print('Declaration_Type: Function_Declaration')),
#    'Variable_Declaration'  : ([';']                                        , print('Variable_Declaration: ;')),
#    'Function_Declaration'  : (['(', 'Parameters', ')', 'StatementBlock']   , print('Function_Declaration: (Parameters) StatementBlock')),
#    'Parameters'            : (['ParameterList']                            , print('Parameters: ParameterList')),
#    'Parameters'            : (['void']                                     , print('Parameters: void')),
#}
#
#    'ParameterList', ['Parameter']],
#    'ParameterList', ['ParameterList', ',', 'Parameter']],
#    'Parameter', ['int', 'ID']],
#    'StatementBlock', ['{', 'InternalDeclaration',  'StatementString', '}']],
#    'InternalDeclaration', ['NULL']],
#    'InternalDeclaration', ['InternalDeclaration',  'InternalVariableDeclaration', ';']],      # change
#    'InternalVariableDeclaration', ['int', 'ID']],
#    'InternalVariableDeclaration', ['double', 'ID']],     # add
#    'StatementString', ['Statement']],
#    'StatementString', ['StatementString', 'Statement']],
#    'Statement', ['ifStatement']],
#    'Statement', ['whileStatement']],
#    'Statement', ['returnStatement']],
#    'Statement', ['AssignmentStatement']],
#    'AssignmentStatement', ['ID', '=', 'Expression', ';']],
#    'returnStatement', ['return', 'ReturnValue']],
#    'ReturnValue', ['Expression', ';']],     # change
#    'ReturnValue', [';']],             # change
#    'whileStatement', ['while', '(', 'Expression', ')', 'StatementBlock']],
#    'ifStatement', ['if', '(', 'Expression', ')', 'StatementBlock', 'elseStatement']],
#    'elseStatement', ['else', 'StatementBlock']],
#    'elseStatement', ['NULL']],
#    'Expression', ['AdditiveExpression']],
#    'Expression', ['Expression', 'relop', 'AdditiveExpression']],
#    'relop', ['<']],
#    'relop', ['<=']],
#    'relop', ['>']],
#    'relop', ['>=']],
#    'relop', ['==']],
#    'relop', ['!=']],
#    'AdditiveExpression', ['Term']],
#    'AdditiveExpression', ['AdditiveExpression', '+', 'Term']],
#    'AdditiveExpression', ['AdditiveExpression', '-', 'Term']],
#    'Term', ['Factor']],
#    'Term', ['Term', '*', 'Factor']],
#    'Term', ['Term', '/', 'Factor']],
#    'Factor', ['num']],
#    'Factor', ['(', 'Expression', ')']],
#    'Factor', ['ID', 'FTYPE']],
#    'FTYPE', ['call']],
#    'FTYPE', ['NULL']],
#    'call', ['(', 'ActualParameterList', ')']],
#    'ActualParameter', ['ActualParameterList']],
#    'ActualParameter', ['NULL']],
#    'ActualParameterList', ['Expression']],
#    'ActualParameterList', ['ActualParameterList', ',', 'Expression']],
#    'ID', ['Identifier']]

