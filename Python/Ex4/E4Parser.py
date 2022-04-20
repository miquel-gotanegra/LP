# Generated from E4.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\2\3\2\3\3\3\3\5\3\27\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\5\5 \n\5\3\5\3\5\3\5\7\5%\n\5\f\5")
        buf.write("\16\5(\13\5\3\6\3\6\3\6\3\6\2\3\b\7\2\4\6\b\n\2\2\2+\2")
        buf.write("\17\3\2\2\2\4\26\3\2\2\2\6\30\3\2\2\2\b\37\3\2\2\2\n)")
        buf.write("\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3")
        buf.write("\2\2\2\17\20\3\2\2\2\20\22\3\2\2\2\21\17\3\2\2\2\22\23")
        buf.write("\7\2\2\3\23\3\3\2\2\2\24\27\5\n\6\2\25\27\5\6\4\2\26\24")
        buf.write("\3\2\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31\7\5\2\2\31\32")
        buf.write("\7\3\2\2\32\33\5\b\5\2\33\7\3\2\2\2\34\35\b\5\1\2\35 ")
        buf.write("\7\6\2\2\36 \7\5\2\2\37\34\3\2\2\2\37\36\3\2\2\2 &\3\2")
        buf.write("\2\2!\"\f\5\2\2\"#\7\7\2\2#%\5\b\5\6$!\3\2\2\2%(\3\2\2")
        buf.write("\2&$\3\2\2\2&\'\3\2\2\2\'\t\3\2\2\2(&\3\2\2\2)*\7\4\2")
        buf.write("\2*+\7\5\2\2+\13\3\2\2\2\6\17\26\37&")
        return buf.getvalue()


class E4Parser ( Parser ):

    grammarFileName = "E4.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' := '", "'write'", "<INVALID>", "<INVALID>", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "EQ", "WRITE", "WORD", "NUM", "MES", 
                      "WS" ]

    RULE_root = 0
    RULE_func = 1
    RULE_assig = 2
    RULE_expr = 3
    RULE_write = 4

    ruleNames =  [ "root", "func", "assig", "expr", "write" ]

    EOF = Token.EOF
    EQ=1
    WRITE=2
    WORD=3
    NUM=4
    MES=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(E4Parser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(E4Parser.FuncContext)
            else:
                return self.getTypedRuleContext(E4Parser.FuncContext,i)


        def getRuleIndex(self):
            return E4Parser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = E4Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==E4Parser.WRITE or _la==E4Parser.WORD:
                self.state = 10
                self.func()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(E4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write(self):
            return self.getTypedRuleContext(E4Parser.WriteContext,0)


        def assig(self):
            return self.getTypedRuleContext(E4Parser.AssigContext,0)


        def getRuleIndex(self):
            return E4Parser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = E4Parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [E4Parser.WRITE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.write()
                pass
            elif token in [E4Parser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.assig()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(E4Parser.WORD, 0)

        def EQ(self):
            return self.getToken(E4Parser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(E4Parser.ExprContext,0)


        def getRuleIndex(self):
            return E4Parser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = E4Parser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(E4Parser.WORD)
            self.state = 23
            self.match(E4Parser.EQ)
            self.state = 24
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(E4Parser.NUM, 0)

        def WORD(self):
            return self.getToken(E4Parser.WORD, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(E4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(E4Parser.ExprContext,i)


        def MES(self):
            return self.getToken(E4Parser.MES, 0)

        def getRuleIndex(self):
            return E4Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = E4Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [E4Parser.NUM]:
                self.state = 27
                self.match(E4Parser.NUM)
                pass
            elif token in [E4Parser.WORD]:
                self.state = 28
                self.match(E4Parser.WORD)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = E4Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 31
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 32
                    self.match(E4Parser.MES)
                    self.state = 33
                    self.expr(4) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(E4Parser.WRITE, 0)

        def WORD(self):
            return self.getToken(E4Parser.WORD, 0)

        def getRuleIndex(self):
            return E4Parser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = E4Parser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(E4Parser.WRITE)
            self.state = 40
            self.match(E4Parser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




