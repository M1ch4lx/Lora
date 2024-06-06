from Lora import Lora
from antlr4 import *
from LoraLexer import LoraLexer
from LoraParser import LoraParser
from LoraVisitorImpl import LoraVisitorImpl, StopExecution
import sys
from enum import Enum
from StandardLibrary import StandardLibrary


class LoraCommand(Enum):
    INVALID = 0
    EXIT = 1
    LOAD = 2


lora = Lora()
lora.import_library(StandardLibrary())
visitor = LoraVisitorImpl(lora)


def load_file(input_file_path):
    input_stream = FileStream(input_file_path)
    lexer = LoraLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    parser = LoraParser(token_stream)

    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    try:
        result = visitor.visit(tree)
    except StopExecution as e:
        print(lora.expression_result())
    except Exception as e:
        print(f'In line {visitor.current_statement_line}: {e}')


def process_input(command):
    if len(command) == 1:
        if command[0] == 'exit':
            return LoraCommand.EXIT, None
    if len(command) == 2:
        if command[0] == 'load':
            file_path = command[1]
            if not file_path.endswith('.lora'):
                file_path += '.lora'
            return LoraCommand.LOAD, file_path
    return LoraCommand.INVALID, None


def lora_interactive_terminal():
    while True:
        input_string = input('>>>')

        if input_string.startswith('!'):
            command, arg = process_input(input_string[1:].split())
            if command == LoraCommand.INVALID:
                print('Invalid command')
            if command == LoraCommand.EXIT:
                break
            if command == LoraCommand.LOAD:
                load_file(arg)
            continue

        if not input_string.endswith(';'):
            input_string += ';'

        input_stream = InputStream(input_string)
        lexer = LoraLexer(input_stream)

        token_stream = CommonTokenStream(lexer)
        parser = LoraParser(token_stream)

        try:
            ctx = parser.program()
            if ctx.getChildCount() > 1:
                raise Exception('Expected only one simple statement')
            statements = ctx.statement()
            if len(statements) == 0:
                raise Exception('Expected simple statement')
            simple_statement = ctx.statement()[0].simple_statement()
            if not simple_statement:
                raise Exception('Expected simple statement')

            tree = simple_statement

            result = visitor.visit(tree)
            if not lora.is_expression_stack_empty():
                print(lora.expression_result())
        except StopExecution as e:
            print(lora.expression_result())
        except Exception as e:
            print(e)


if len(sys.argv) < 2:
    lora_interactive_terminal()
    sys.exit()

input_file_path = sys.argv[1]

if not input_file_path.endswith('.lora'):
    input_file_path += '.lora'

load_file(input_file_path)
