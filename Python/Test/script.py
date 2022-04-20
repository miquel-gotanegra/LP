from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor


input_stream = InputStream(input('? ')) #una sola linia
#input_stream = StdinStream() #tota la entrada
#input_stream = FileStream(sys.argv[1]) #nom archiu com a paràmetre
#input_stream = FileStream(sys.argv[1], encoding='utf-8') #si el archiu te accents
#cal afegir a la gramatica WORD : [a-zA-Z\u0080-\u00FF]+ ;


lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()
#print(tree.toStringTree(recog=parser))

visitor = EvalVisitor()
visitor.visit(tree)

#La recursivitat va d'esquerra a dreta
#la multiplicacio te prioritat sobre la suma
# expr : expr '*' expr
#    | expr '+' expr
#    | INT
# ;

#si volem que la associativitat sigui de dreta a esquerra
#expr : <assoc=right> expr '^' expr
#    | INT
#    ;
