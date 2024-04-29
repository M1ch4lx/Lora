
lexer grammar LoraLexer;

IF : 'if' ;
WHILE : 'while' ;
DEF : 'def' ;
RETURN : 'return' ;
PRINT : 'print' ;
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

WS : [ \t\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;