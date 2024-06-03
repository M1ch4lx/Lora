# Lora

## Tokens
```
IF : 'if' ;
FOR : 'for' ;
WHILE : 'while' ;
IN : 'in' ;
BREAK : 'break' ;
FUNCTION : 'function' ;
RETURN : 'return' ;
ELSE : 'else' ;
IMPORT : 'import' ;
AS : 'as' ;

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

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
```

## Grammar
```
program : (import_statement SEMI)* (statement | function_declaration)+ ;

alias : AS ID ;

import_statement : IMPORT ID alias? ;

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

index_operator : LSQUARE tuple RSQUARE ;

array : LSQUARE (expression (COMMA expression)*)? RSQUARE ;

object_field : ID COLON expression ;

object : BLOCK_START (object_field (COMMA object_field)*)? BLOCK_END ;

attribute_operator : DOT ID ;

expression
    : boolean_expression
    ;

boolean_expression
    : boolean_term (OR boolean_expression)?
    ;

boolean_term
    : boolean_factor (AND boolean_term)?
    ;

boolean_factor
    : relational_expression
    | NOT boolean_factor
    ;

relational_expression
    : additive_expression (op=(EQ | NEQ | LT | LTE | GT | GTE) relational_expression)?
    ;

additive_expression
    : multiplicative_expression (op=(PLUS | MINUS) additive_expression)?
    ;

multiplicative_expression
    : primary_expression (op=(MULT | DIV) multiplicative_expression)?
    ;

primary_expression
    : value
    | array
    | object
    | LPAREN expression RPAREN
    | LPAREN tuple RPAREN
    | variable_reference
    | function_call
    | primary_expression index_operator
    | primary_expression attribute_operator
    | primary_expression DOT function_call
    ;

typed_assignment : typed_variable ASSIGN expression ;

assignment : ID (COMMA ID)* ASSIGN (expression | tuple) |
    LPAREN ID (COMMA ID)* RPAREN ASSIGN (expression | tuple) ;

property_assignment : ID (DOT ID)+ ASSIGN (expression | tuple) ;

indexed_assignment : ID index_operator ASSIGN (expression | tuple) ;

function_parameter :
    ID |
    typed_variable ;

function_parameters_list : LPAREN ( function_parameter (COMMA function_parameter)* )? RPAREN ;

type_requirement : COLON ID ;

function_declaration : FUNCTION (ID COLON)? ID function_parameters_list type_requirement? code_block ;

return_statement : RETURN expression | RETURN tuple | RETURN;

break_statement : BREAK ;

code_block : BLOCK_START statement+ BLOCK_END ;

for_loop_statement : FOR LPAREN ID IN expression RPAREN code_block ;

while_loop_statement : WHILE LPAREN expression RPAREN code_block ;

if_statement : IF LPAREN expression RPAREN code_block else_statement? ;

else_statement : ELSE code_block ;

simple_statement :
    typed_assignment |
    property_assignment |
    assignment |
    indexed_assignment |
    break_statement |
    return_statement |
    expression ;

statement : if_statement | simple_statement SEMI | for_loop_statement | while_loop_statement ;
```

## Example code
### Vector.lo
```
Vector = { };

function Vector:zero(self)
{
    vec = self;
    vec.x = 0;
    vec.y = 0;
    return vec;
}

function Vector:new(self, x, y)
{
    vec = self;
    vec.x = x;
    vec.y = y;
    return vec;
}

function Vector:move(self, vec)
{
    self.x = self.x + vec.x;
    self.y = self.y + vec.y;
}

function Vector:print(self)
{
    print(self.x);
    print(self.y);
}

function move(position, vec)
{
    position.x = position.x + vec.x;
    position.y = position.y + vec.y;
    return position;
}

return Vector;
```
### test.lo
```
import Vector as vec;

function sum(array: Array): Number
{
    result = 0;
    for(e in array)
    {
        result = result + e;
    }
    return result;
}

test_vec: vec = vec.zero();

print("Printing test vec");
test_vec.print();

print(sum([1,2,3]));

callback: Callback = sum;

result = callback([1,2,4]);

print(result);

player = {
    name: "Player1",
    position: vec.new(10, 13)
};

player.hp = 0.78;

function player:is_alive(self)
{
    return self.hp > 0;
}

while(player.is_alive())
{
    print("Player is alive");
    loss = 0.3;
    player.hp = player.hp - loss;
    print(player.hp);
}

print("Player died");

print_player_data = True;

if(print_player_data)
{
    print("Stats:");
    print(player.name);
    player.position.print();
}
else
{
    print("Game over");
}
```
