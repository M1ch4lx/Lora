from Lora import Lora
from antlr4 import *
from LoraLexer import LoraLexer
from LoraParser import LoraParser
from LoraVisitorImpl import LoraVisitorImpl, StopExecution
import sys


if len(sys.argv) < 2:
    print("Provide input file path")
    sys.exit()

input_file_path = sys.argv[1]

input_stream = FileStream(input_file_path)
lexer = LoraLexer(input_stream)

token_stream = CommonTokenStream(lexer)
parser = LoraParser(token_stream)

tree = parser.program()
# print(tree.toStringTree(recog=parser))

lora = Lora()

visitor = LoraVisitorImpl(lora)

try:
    result = visitor.visit(tree)
except StopExecution as e:
    print(lora.expression_result())
except Exception as e:
    print(f'In line {visitor.current_statement_line}: {e}')
