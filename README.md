# Interpreter Lora

## Opis projektu
- Jest to interpreter języka Lora przeznaczonego do wizualizacji matematycznych
- Interpreter implementowany jest w języku Python
- Parsery generowane są przy pomocy Antlr 4
- Lora docelowa ma być używana przez matematyków oraz inżynierów danych, z założenia ma to być język prosty i łatwy do nauczenia

## Założenia języka
- W Lora każde przypisanie jest kopią
- Lora umożliwia dynamiczne tworzenie obiektów
- W Lora nie ma referencji
- Możliwe jest dodawanie metod do obiektów
- Lore można łatwo rozwijać poprzez pisanie nowych funkcji w Pythonie
- Lora ma zaimplementowany konwerter między typami Pythonowymi a tymi z Lora
- Typy danych: Number, Tuple, Array, Callback, String, Boolean, Object

## Środowisko interaktywne
Lora umożliwia uruchomienie środowiska interaktywnego, komendy w środowisku:
- !exit - wyjście ze środowiska
- !load <nazwa_pliku> - wykonanie pliku

## Struktura interpretera - najważniejsze komponent
- Lora - główna klasa przechowująca stan programu, zajmuje się ewaluacją wyrażeń, zarządzaniem zmiennymi oraz zbiorem funkcji
- Context - zawiera zmienne i inne parametry dotyczące aktualnego zasięgu
- LoraVisitorImpl - implementacja visitora - aktualnie duża część logiki wykonywania kodu znajduje się też w visitorze

## Eksportowanie funkcji języka Python do Lora
Lora umożliwia bardzo łatwe dodawanie funkcji z języka Python do środowiska - wszystko odbywa się poprzez dodawanie dekoratorów
``` python3
@export('range')
def lora_range(start: int, stop: int):
    return list(range(start, stop))


@export('Array')
class ArrayPrototype:
    @export
    def size(array: list):
        return len(array)
```

## Marshalling typów
Jak widać w przykładzie powyżej operujemy jedynie typami z języka Python, jest to możliwe dzięki komponentowi który kownertuje obiekty z jednego języka na drugi.

## Opis języka

### Zmienne
Tworzenie zmiennych wygląda tak jak w Python, możemy tworzyć w podobny sposób krotki, tablice i dynamiczne obiekty.
Ważne jest aby pamiętać że w Lora nie ma referencji i wszystko jest kopią.

### Prototypowanie
Lora umożliwia specyficzny sposób pisania pseudo klas, inspirowany językiem Lua, poniżej przykładowa implementacja wektora.
Należy jednak pamiętać że nie jest to klasa, Vector jest zwyczajnym obiektem z którym możemy potem zrobić co chcemy, należy to potraktować bardziej jako wzorzec projektowy.
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

function Vector:add(self, vec)
{
    self.x = self.x + vec.x;
    self.y = self.y + vec.y;
}

function Vector:print(self)
{
    print(self.x);
    print(self.y);
}

return Vector;
```

Aby lepiej zrozumieć jak programować w Lora proszę o przejście do sekcji z przykładami.

## Aktualne możeliwości i plany na przyszłość
Na ten moment możliwości jeśli chodzi o wizualizacje są dość okrojone - można robić proste animacje wektorowe oraz rysować proste wkresy.
Mimo to jednak język jest już na tyle rozwinięty że dodawanie nowych funkcjonalności jest bardzo ułatwione, w przyszłości warto by rozszerzyć funkcje wizualizacji oraz dodać więcej ogólnych funkcji.

## Uruchamianie

### Wymagania
- zainstalowane narzędzie antlr

### Generowanie parsera
```antlr4 Lora.g4 -Dlanguage=Python3 -visitor```

### Uruchamianie
Wykonanie pliku:
```python -m LoraRun <nazwa_pliku>```
Środowisko interaktywne:
```python -m LoraRun```

## Tokeny
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

## Gramatyka
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

## Przykładowy kod
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

function linspace(begin, end, count)
{
    length = end - begin;
    step = length / (count + 1);
    array = [];
    current = begin + step;
    for(i in range(0, count))
    {
        array = array + [current];
        current = current + step;
    }
    return array;
}

function calculate_values(args, func)
{
    values = args;
    for(pair in enumerate(args))
    {
        i, arg = pair;
        values[i] = func(arg);
    }
    return values;
}

function identity(x)
{
    return x;
}

function linear(x)
{
    return 2*x + 5;
}

function quadratic(x)
{
    return 2*x*x + 5;
}

x = linspace(0, 100, 100);

#y = calculate_values(x, identity);
#y = calculate_values(x, linear);
y = calculate_values(x, quadratic);

plot(x, y);

function bubbleSort(array: Array) {
    n = array.size();
    for (i in range(0, n-1)) {
        for (j in range(0, n-(i+1))) {
            if (array[j] > array[j+1]) {
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    return array;
}

array = bubbleSort([1, 3, 2, 1, 2, 7, 5, 9, 10, 2]);
print(array);
# bubbleSort(123);

function fibonacci_recursive(n: Number) : Number {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
    }
}

result_recursive = [];
for (i in range(0, 10)) {
    result_recursive = result_recursive + [fibonacci_recursive(i)];
}

print(result_recursive);

v = vec.new(0,0);
v.print();
```
