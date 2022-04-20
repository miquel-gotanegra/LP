# Generated from E4.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .E4Parser import E4Parser
else:
    from E4Parser import E4Parser

# This class defines a complete generic visitor for a parse tree produced by E4Parser.

class E4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by E4Parser#root.
    def visitRoot(self, ctx:E4Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by E4Parser#func.
    def visitFunc(self, ctx:E4Parser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by E4Parser#assig.
    def visitAssig(self, ctx:E4Parser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by E4Parser#expr.
    def visitExpr(self, ctx:E4Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by E4Parser#write.
    def visitWrite(self, ctx:E4Parser.WriteContext):
        return self.visitChildren(ctx)



del E4Parser