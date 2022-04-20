# Generated from logo3d.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
else:
    from logo3dParser import logo3dParser

# This class defines a complete generic visitor for a parse tree produced by logo3dParser.

class logo3dVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logo3dParser#root.
    def visitRoot(self, ctx:logo3dParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#func.
    def visitFunc(self, ctx:logo3dParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#lines.
    def visitLines(self, ctx:logo3dParser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#assig.
    def visitAssig(self, ctx:logo3dParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#procediment.
    def visitProcediment(self, ctx:logo3dParser.ProcedimentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#lectura.
    def visitLectura(self, ctx:logo3dParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#escriptura.
    def visitEscriptura(self, ctx:logo3dParser.EscripturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#condicional.
    def visitCondicional(self, ctx:logo3dParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#wbucle.
    def visitWbucle(self, ctx:logo3dParser.WbucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#fbucle.
    def visitFbucle(self, ctx:logo3dParser.FbucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Div.
    def visitDiv(self, ctx:logo3dParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#NonOp.
    def visitNonOp(self, ctx:logo3dParser.NonOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Res.
    def visitRes(self, ctx:logo3dParser.ResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Mul.
    def visitMul(self, ctx:logo3dParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Lt.
    def visitLt(self, ctx:logo3dParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Gte.
    def visitGte(self, ctx:logo3dParser.GteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Sum.
    def visitSum(self, ctx:logo3dParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#nEq.
    def visitNEq(self, ctx:logo3dParser.NEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Eq.
    def visitEq(self, ctx:logo3dParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Lte.
    def visitLte(self, ctx:logo3dParser.LteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Gt.
    def visitGt(self, ctx:logo3dParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Float.
    def visitFloat(self, ctx:logo3dParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Int.
    def visitInt(self, ctx:logo3dParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Word.
    def visitWord(self, ctx:logo3dParser.WordContext):
        return self.visitChildren(ctx)



del logo3dParser