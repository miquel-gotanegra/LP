if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

#amb els fills: ctx.getChildren() (és un generador)
#l = list(ctx.getChildren()) o
#op1, op, op2 = list(ctx.getChildren())
#
#n.getText(): text del node CARACTER CONCRET DE AQUESTA REGLA
#ExprParser.symbolicNames[n.getSymbol().type]: token del node en format text NOM DE LA REGLA
#ExprParser.MES: índex intern del token MES per al parser. Es sol utilitzar junt amb n.getSymbol().type
#
#podem intercanviar informació amb un visitor mitjançant el constructor __init__ i fent que el mètode de la regla arrel torni quelcom
#quan un node pertany a la part lèxica conté l'atribut getSymbol i quan pertany a la part sintàctica l'atribut getRuleIndex.


class TreeVisitor(ExprVisitor): #subclasse de ExprVisitor
    
    #constructor
    def __init__(self):
        self.nivell = 0


    def visitExpr(self, ctx): #ctx es el contexte (la part dreta son els fills del contexte)
        l = list(ctx.getChildren())
        if len(l) == 1:
            print("  " * self.nivell +
                  ExprParser.symbolicNames[l[0].getSymbol().type] +
                  '(' +l[0].getText() + ')')
        else:  # len(l) == 3
            print('  ' *  self.nivell + 'MES(+)')
            self.nivell += 1
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1 