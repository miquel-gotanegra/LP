if __name__ is not None and "." in __name__:
    from .E4Parser import E4Parser
    from .E4Visitor import E4Visitor
else:
    from E4Parser import E4Parser
    from E4Visitor import E4Visitor


class CVisitor(E4Visitor): #subclasse de E4Visitor
    #constructor
    mem = {}
    
    def visitRoot(self, ctx:E4Parser.RootContext):
        self.visitChildren(ctx)

    def visitAssig(self, ctx:E4Parser.AssigContext):
        l = list(ctx.getChildren())
        var = l[0].getText()
        val = self.visit(l[2])
        CVisitor.mem[var]=val


    # Visit a parse tree produced by E4Parser#expr.
    def visitExpr(self, ctx:E4Parser.ExprContext):
        
        l = list(ctx.getChildren())
        if len(l) == 1:
            x = l[0].getText()
            if x.isnumeric() :
                return int(x)
            else :
                return CVisitor.mem.get(x,0)
        else:  # len(l) == 3
            return self.visit(l[0]) + self.visit(l[2])


    # Visit a parse tree produced by E4Parser#write.
    def visitWrite(self, ctx:E4Parser.WriteContext):
        l = list(ctx.getChildren())
        print('Valor de '+l[1].getText()+" es "+ str(CVisitor.mem[l[1].getText()]))

        