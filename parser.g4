parser grammar LoraParser;

program : statement+ ;

statement : simple_statement
          | if_statement
          | while_statement
          | function_definition
          ;

simple_statement : assignment_statement
                 | expression_statement
                 | return_statement
                 | print_statement
                 ;

assignment_statement : ID '=' expression ';' ;

expression_statement : expression ';' ;

expression : ID
           | INT |
           | '(' expression ')'
           | expression op=('*' | '/' | '+' | '-' | '==' | '!=' | '<' | '<=' | '>' | '>=' ) expression
           ;
           
if_statement : IF expression BLOCK_START statement ( ELIF expression BLOCK_START statement )* ( ELSE BLOCK_START statement )? ;

while_statement : WHILE expression BLOCK_START statement ;

function_definition : DEF ID '(' parameters ')' BLOCK_START statement ;

parameters : ID (COMMA ID)* ;

return_statement : RETURN expression ';' ;