from antlr4 import *
import sys
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser
from visitor import visitor

if len(sys.argv) < 2:
    raise Exception(
        "Usage: phyton3 logo3d.py input_file.l3d [func, param1,...]")
input_stream = FileStream(sys.argv[1])


lexer = logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = logo3dParser(token_stream)
tree = parser.root()
# print(tree.toStringTree(recog=parser))

if(len(sys.argv) > 2):
    func = sys.argv[2]
    param = sys.argv[3:]
else:
    func = 'main'
    param = []


visitor = visitor(func, param)
visitor.visit(tree)
