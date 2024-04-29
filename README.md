# Lora

## Tokens
```
IF : 'if' ;
WHILE : 'while' ;
DEF : 'function' ;
RETURN : 'return' ;
BLOCK_START : ':' ;
ELIF : 'elif';
ELSE : 'else';
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;
BOOL : 'True' | 'False' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LSQUARE : '[' ;
RSQUARE : ']' ;
PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
POW : '**' ;
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
LTE : '<=' ;
GT : '>' ;
GTE : '>=' ;
ASSIGN : '=' ;
COMMA : ',';
SEMI : ';' ;
```

## Grammar
```
program : statement+ ;

statement : simple_statement
          | if_statement
          | while_statement
          | function_definition
          ;

simple_statement : assignment_statement
                 | expression_statement
                 | return_statement
                 ;

assignment_statement : ID '=' expression ';' ;

expression_statement : expression ';' ;

tuple : expression (COMMA expression)*;

function_call : ID '(' tuple ')';

expression : ID
           | function_call
           | INT |
           | '(' expression ')'
           | expression op=('*' | '/' | '+' | '-' | '==' | '!=' | '<' | '<=' | '>' | '>=' ) expression
           ;
           
if_statement : IF expression BLOCK_START statement ( ELIF expression BLOCK_START statement )* ( ELSE BLOCK_START statement )? ;

while_statement : WHILE expression BLOCK_START statement ;

function_definition : DEF ID '(' parameters ')' BLOCK_START statement ;

parameters : ID (COMMA ID)* ;

return_statement : RETURN expression ';' ;
```

## Example code
```
function add(a, b):
    return a + b;

x = 13;
a = 23;
if a == 23:
    a = 32;
    
while a < 100:
    if a > 40:
        a = 100;
    else:
        a = a + 1;

c = add(a, add(x, 20));
```
