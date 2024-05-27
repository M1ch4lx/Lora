from antlr4 import *
from LoraLexer import LoraLexer
from LoraParser import LoraParser
from LoraVisitorImpl import LoraVisitorImpl
import sys
from Lora import *

if len(sys.argv) < 2:
    print("Provide input file path")
    sys.exit()

input_file_path = sys.argv[1]

input_stream = FileStream(input_file_path)
lexer = LoraLexer(input_stream)

#token_stream = CommonTokenStream(lexer)
#token_stream.fill()
#for token in token_stream.tokens:
#    print(token)

token_stream = CommonTokenStream(lexer)
parser = LoraParser(token_stream)

tree = parser.program()
print(tree.toStringTree(recog=parser))

#listener = LoraListenerImpl()
#walker = ParseTreeWalker()
#walker.walk(listener, tree)

lora = Lora()

visitor = LoraVisitorImpl(lora)
result = visitor.visit(tree)
#for res in result:
#    print(res)