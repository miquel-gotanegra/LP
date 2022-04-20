# Generated from E4.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("-\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\6\4\34")
        buf.write("\n\4\r\4\16\4\35\3\5\6\5!\n\5\r\5\16\5\"\3\6\3\6\3\7\6")
        buf.write("\7(\n\7\r\7\16\7)\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\3\2\5\5\2C\\c|\u0082\u0101\3\2\62;\4\2\f\f\"\"\2/\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\24\3\2\2\2\7\33\3\2")
        buf.write("\2\2\t \3\2\2\2\13$\3\2\2\2\r\'\3\2\2\2\17\20\7\"\2\2")
        buf.write("\20\21\7<\2\2\21\22\7?\2\2\22\23\7\"\2\2\23\4\3\2\2\2")
        buf.write("\24\25\7y\2\2\25\26\7t\2\2\26\27\7k\2\2\27\30\7v\2\2\30")
        buf.write("\31\7g\2\2\31\6\3\2\2\2\32\34\t\2\2\2\33\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\b\3\2\2\2\37")
        buf.write("!\t\3\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2")
        buf.write("#\n\3\2\2\2$%\7-\2\2%\f\3\2\2\2&(\t\4\2\2\'&\3\2\2\2(")
        buf.write(")\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\b\7\2\2,\16")
        buf.write("\3\2\2\2\6\2\35\")\3\b\2\2")
        return buf.getvalue()


class E4Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    WRITE = 2
    WORD = 3
    NUM = 4
    MES = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' := '", "'write'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "WRITE", "WORD", "NUM", "MES", "WS" ]

    ruleNames = [ "EQ", "WRITE", "WORD", "NUM", "MES", "WS" ]

    grammarFileName = "E4.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


