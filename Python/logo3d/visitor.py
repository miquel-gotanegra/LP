from collections import namedtuple
from turtle3d import Turtle3D
if __name__ is not None and "." in __name__:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor

Func = namedtuple('Func', 'param ctx')


class visitor (logo3dVisitor):  # subclasse de logo3dVisitor
    # constructor
    mem = []  # faig servir una llista com una pila per mantenir el contexte al entrar/sortir de les funcions
    # per accedir al cim de la pila fem mem[-1], ja que en python els vectors fan wrap i aixo ens dona l'ultim element

    funcions = {}

    turtlefunctions = {'forward', 'backward', 'right',
                       'left', 'up', 'down', 'hide', 'show', 'home', 'color'}

    funini = ''
    paramini = []
    turt = None

    def __init__(self, func, param):
        visitor.mem.append({})

        visitor.funini = func
        visitor.paramini = param
        # print(param)

        # afegim les funcions del turtle a la llista de funcions
        visitor.funcions['forward'] = Func(['units'], 0)
        visitor.funcions['backward'] = Func(['units'], 0)
        visitor.funcions['right'] = Func(['a'], 0)
        visitor.funcions['left'] = Func(['a'], 0)
        visitor.funcions['up'] = Func(['b'], 0)
        visitor.funcions['down'] = Func(['b'], 0)
        visitor.funcions['hide'] = Func([], 0)
        visitor.funcions['show'] = Func([], 0)
        visitor.funcions['home'] = Func([], 0)
        visitor.funcions['color'] = Func(['r', 'g', 'b'], 0)

    def visitRoot(self, ctx: logo3dParser.RootContext):
        # parse del codi
        self.visitChildren(ctx)

        # print(visitor.funcions)

        # triar la funcio per la que comencem i posar el seu contexte
        name = visitor.funini
        values = []

        if name not in visitor.funcions:
            raise Exception("Cria a procediment no definit! --> "+name+"()")

        keys = visitor.funcions[name].param

        for k in visitor.paramini:
            if k.isnumeric():
                values.append(float(k))
            else:
                values.append(k)

        if len(keys) != len(values):
            raise Exception(
                'El nombre de parametres no concorda amb la definicio del procediment--> ' + name+'('+str(keys)+')')

        a = dict(zip(keys, values))

        if name in visitor.turtlefunctions:
            self.turtleProc(name, values)

        else:
            visitor.mem.append(a)

            self.visitChildren(visitor.funcions[name].ctx)
            visitor.mem.pop()
            # print(visitor.mem[-1])

    # %%%%%%%%%%%%%%%%  ASSIG   %%%%%%%%%%%%%%%%
    def visitAssig(self, ctx: logo3dParser.AssigContext):
        l = list(ctx.getChildren())
        var = l[0].getText()
        val = self.visit(l[2])
        visitor.mem[-1][var] = val

    # %%%%%%%%%%%%%%%%  EXPRESION   %%%%%%%%%%%%%%%%
    def visitMul(self, ctx: logo3dParser.MulContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) * self.visit(l[2])

    def visitDiv(self, ctx: logo3dParser.DivContext):
        l = list(ctx.getChildren())
        if (self.visit(l[2]) == 0):
            raise Exception("No es pot dividir entre 0!")
        return self.visit(l[0]) / self.visit(l[2])

    def visitSum(self, ctx: logo3dParser.SumContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) + self.visit(l[2])

    def visitRes(self, ctx: logo3dParser.SumContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])

    def visitEq(self, ctx: logo3dParser.EqContext):
        l = list(ctx.getChildren())
        if self.visit(l[0]) == self.visit(l[2]):
            return 1
        else:
            return 0

    def visitNEq(self, ctx: logo3dParser.NEqContext):
        l = list(ctx.getChildren())
        if self.visit(l[0]) != self.visit(l[2]):
            return 1
        else:
            return 0

    def visitLt(self, ctx: logo3dParser.LtContext):
        l = list(ctx.getChildren())
        if self.visit(l[0]) < self.visit(l[2]):
            return 1
        else:
            return 0

    def visitGt(self, ctx: logo3dParser.LtContext):
        l = list(ctx.getChildren())
        if self.visit(l[0]) > self.visit(l[2]):
            return 1
        else:
            return 0

    def visitLte(self, ctx: logo3dParser.LtContext):
        l = list(ctx.getChildren())
        if self.visit(l[0]) <= self.visit(l[2]):
            return 1
        else:
            return 0

    def visitGte(self, ctx: logo3dParser.LtContext):
        l = list(ctx.getChildren())
        if self.visit(l[0]) >= self.visit(l[2]):
            return 1
        else:
            return 0

    # %%%%%%%%%%%%%%%%    VAR       %%%%%%%%%%%%%%%%

    def visitInt(self, ctx: logo3dParser.IntContext):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    # Visit a parse tree produced by logo3dParser#Float.
    def visitFloat(self, ctx: logo3dParser.FloatContext):
        l = list(ctx.getChildren())
        return float(l[0].getText())

    # Visit a parse tree produced by logo3dParser#Word.
    def visitWord(self, ctx: logo3dParser.WordContext):
        l = list(ctx.getChildren())
        x = l[0].getText()
        if x in visitor.mem[-1]:
            return visitor.mem[-1][x]
        else:
            visitor.mem[-1][x] = 0
            return visitor.mem[-1][x]

    # %%%%%%%%%%%%%%%%  LECTURA/ECRITURA   %%%%%%%%%%%%%%%%

    def visitLectura(self, ctx: logo3dParser.LecturaContext):
        l = list(ctx.getChildren())
        x = l[1].getText()
        print('insert ' + x + ': ', end='')  # opcional
        visitor.mem[-1][x] = float(input())

    def visitEscriptura(self, ctx: logo3dParser.EscripturaContext):
        l = list(ctx.getChildren())
        x = self.visit(l[1])
        print(x)

    # %%%%%%%%%%%%%%%%    COND/WHILE/FOR    %%%%%%%%%%%%%%%%

    def visitCondicional(self, ctx: logo3dParser.CondicionalContext):
        l = list(ctx.getChildren())
        if not(-0.000001 < self.visit(l[1]) < 0.000001):
            i = 3
            while l[i].getText() != 'ELSE' and l[i].getText() != 'END':
                self.visit(l[i])
                i += 1

        else:
            els = False
            aux = -1
            for i in range(3, len(l)):
                if l[i].getText() == 'ELSE':
                    els = True
                    aux = i

            if els:
                i = aux + 1
                while l[i].getText() != 'END':
                    self.visit(l[i])
                    i += 1

    def visitWbucle(self, ctx: logo3dParser.WbucleContext):
        l = list(ctx.getChildren())
        while not(-0.000001 < self.visit(l[1]) < 0.000001):
            for i in range(3, len(l)-1):
                self.visit(l[i])

    def visitFbucle(self, ctx: logo3dParser.FbucleContext):
        l = list(ctx.getChildren())
        i = l[1].getText()
        ini = int(self.visit(l[3]))
        final = int(self.visit(l[5]))

        visitor.mem[-1][i] = ini

        while (visitor.mem[-1][i] <= final):
            for k in range(7, len(l)-1):
                self.visit(l[k])
            ini += 1
            visitor.mem[-1][i] = ini

    # %%%%%%%%%%%%%%%%    PROCEDIMENT    %%%%%%%%%%%%%%%%

    def visitProcediment(self, ctx: logo3dParser.ProcedimentContext):
        l = list(ctx.getChildren())
        name = l[0].getText()

        if name not in visitor.funcions:
            raise Exception("Cria a procediment no definit! --> "+name+"()")

        values = []
        i = 2
        while l[i].getText() != ')':
            if l[i].getText() != ',':
                values.append(self.visit(l[i]))
            i += 1

        keys = visitor.funcions[name].param

        if len(keys) != len(values):
            raise Exception(
                'El nombre de parametres no concorda amb la definicio del procediment--> ' + name+'('+str(keys)+')')

        a = dict(zip(keys, values))

        if name in visitor.turtlefunctions:
            self.turtleProc(name, values)

        else:
            visitor.mem.append(a)

            self.visitChildren(visitor.funcions[name].ctx)
            visitor.mem.pop()
            # print(visitor.mem[-1])

    def turtleProc(self, name, values):
        if visitor.turt is None:
            visitor.turt = Turtle3D()

        if name == 'forward':
            visitor.turt.forward(values[0])
        elif name == 'backward':
            visitor.turt.backward(values[0])
        elif name == 'right':
            visitor.turt.right(values[0])
        elif name == 'left':
            visitor.turt.left(values[0])
        elif name == 'up':
            visitor.turt.up(values[0])
        elif name == 'down':
            visitor.turt.down(values[0])
        elif name == 'hide':
            visitor.turt.hide()
        elif name == 'show':
            visitor.turt.show()
        elif name == 'home':
            visitor.turt.home()
        elif name == 'color':
            visitor.turt.color(values[0], values[1], values[2])

    # %%%%%%%%%%%%%%%%       FUNCIO       %%%%%%%%%%%%%%%%

    def visitFunc(self, ctx: logo3dParser.FuncContext):
        l = list(ctx.getChildren())
        nom = l[1].getText()
        if nom in visitor.funcions:
            raise Exception("Redefinicio del procediment--> " + nom + "()")
        param = []
        i = 3
        while l[i].getText() != ')':
            if l[i].getText() != ',':
                if(l[i].getText() in param):
                    raise Exception(
                        "Nom de parametres repetits a la definicio de--> "+nom+"()")
                param.append(l[i].getText())
            i += 1

        visitor.funcions[nom] = Func(param, ctx)
