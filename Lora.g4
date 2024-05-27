grammar Lora;

IF : 'if' ;
FOR : 'for' ;
IN : 'in' ;
BREAK : 'break' ;
FUNCTION : 'function' ;
RETURN : 'return' ;
ELSE : 'else' ;
IMPORT : 'import' ;
AS : 'as' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

INTEGER_VALUE : [0-9]+ ;
FLOAT_VALUE : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING_VALUE : '"' (~["\r\n])* '"' ;
BOOL_VALUE : 'True' | 'False' ;

NONE : 'None' ;

BLOCK_START : '{' ;
BLOCK_END: '}' ;

LPAREN : '(' ;
RPAREN : ')' ;
LSQUARE : '[' ;
RSQUARE : ']' ;

PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
LTE : '<=' ;
GT : '>' ;
GTE : '>=' ;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

ASSIGN : '=' ;

COMMA : ',';
SEMI : ';' ;
COLON: ':' ;
DOT: '.' ;
INTEND: '\t';

WS : [ \t\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;

program : (import_statement SEMI)* statement+ ;

import_statement : IMPORT ID (AS ID)? ;

typed_variable : ID COLON ID ;

value :
    INTEGER_VALUE |
    FLOAT_VALUE |
    STRING_VALUE |
    BOOL_VALUE |
    NONE ;

variable_reference : ID ;

tuple : expression (COMMA expression)*;

function_call : ID LPAREN tuple? RPAREN ;

index_operator : LSQUARE expression (COMMA expression)* RSQUARE ;

array : LSQUARE (expression (COMMA expression)*)? RSQUARE ;

object_field : ID COLON expression ;

object : BLOCK_START (object_field (COMMA object_field)*)? BLOCK_END ;

attribute_operator : DOT ID ;

expression : 
    value |
    array |
    object |
    variable_reference |
    function_call |
    expression index_operator |
    expression attribute_operator |
    expression op=(MULT | DIV) expression |
    expression op=(PLUS | MINUS) expression |
    expression op=(EQ | NEQ | LT | LTE | GT | GTE | AND | OR | NOT) expression |
    LPAREN expression RPAREN ;

typed_assignment : typed_variable ASSIGN expression ;

assignment : ID ASSIGN expression ;

function_parameter :
    ID |
    typed_variable ;

function_parameters_list : LPAREN ( function_parameter (COMMA function_parameter)* )? RPAREN ;

function_declaration : FUNCTION ID function_parameters_list (COLON ID)? BLOCK_START base_statement+ BLOCK_END ;

return_statement : RETURN expression ;

break_statement : BREAK ;

for_loop_statement : FOR LPAREN ID IN expression RPAREN BLOCK_START base_statement+ BLOCK_END ;

if_statement : IF LPAREN expression RPAREN BLOCK_START base_statement+ BLOCK_END else_statement? ;

else_statement : ELSE BLOCK_START base_statement+ BLOCK_END ;

simple_statement :
    typed_assignment |
    assignment |
    break_statement |
    return_statement |
    expression ;

base_statement : if_statement | simple_statement SEMI | for_loop_statement ;

statement : base_statement | function_declaration ;