# Generated from G01.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\31\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\3\2\2\4")
        buf.write("\2\4\2\2\2\32\2\b\3\2\2\2\4\26\3\2\2\2\6\t\5\4\3\2\7\t")
        buf.write("\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13\7\3")
        buf.write("\2\2\13\f\7\7\2\2\f\27\7\7\2\2\r\16\7\4\2\2\16\17\7\7")
        buf.write("\2\2\17\27\7\7\2\2\20\21\7\5\2\2\21\22\7\7\2\2\22\27\7")
        buf.write("\7\2\2\23\24\7\6\2\2\24\25\7\7\2\2\25\27\7\7\2\2\26\n")
        buf.write("\3\2\2\2\26\r\3\2\2\2\26\20\3\2\2\2\26\23\3\2\2\2\27\5")
        buf.write("\3\2\2\2\4\b\26")
        return buf.getvalue()


class G01Parser ( Parser ):

    grammarFileName = "G01.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'G28'", "'F'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(G01Parser.ExprContext,0)


        def getRuleIndex(self):
            return G01Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = G01Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [G01Parser.T__0, G01Parser.T__1, G01Parser.T__2, G01Parser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [G01Parser.EOF]:
                self.enterOuterAlt(localctx, 2)

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


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G01Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnotherDrawExprUsingG28Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.a_cord = None # Token
            self.b_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnotherDrawExprUsingG28" ):
                listener.enterAnotherDrawExprUsingG28(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnotherDrawExprUsingG28" ):
                listener.exitAnotherDrawExprUsingG28(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnotherDrawExprUsingG28" ):
                return visitor.visitAnotherDrawExprUsingG28(self)
            else:
                return visitor.visitChildren(self)


    class PrintForAllGrammarCodesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintForAllGrammarCodes" ):
                listener.enterPrintForAllGrammarCodes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintForAllGrammarCodes" ):
                listener.exitPrintForAllGrammarCodes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintForAllGrammarCodes" ):
                return visitor.visitPrintForAllGrammarCodes(self)
            else:
                return visitor.visitChildren(self)


    class OneDrawExprUsingG01Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneDrawExprUsingG01" ):
                listener.enterOneDrawExprUsingG01(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneDrawExprUsingG01" ):
                listener.exitOneDrawExprUsingG01(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneDrawExprUsingG01" ):
                return visitor.visitOneDrawExprUsingG01(self)
            else:
                return visitor.visitChildren(self)


    class LastDrawExprUsingFContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G01Parser.ExprContext
            super().__init__(parser)
            self.c_cord = None # Token
            self.d_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(G01Parser.NUMBER)
            else:
                return self.getToken(G01Parser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastDrawExprUsingF" ):
                listener.enterLastDrawExprUsingF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastDrawExprUsingF" ):
                listener.exitLastDrawExprUsingF(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLastDrawExprUsingF" ):
                return visitor.visitLastDrawExprUsingF(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = G01Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [G01Parser.T__0]:
                localctx = G01Parser.OneDrawExprUsingG01Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(G01Parser.T__0)
                self.state = 9
                localctx.x_cord = self.match(G01Parser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__1]:
                localctx = G01Parser.AnotherDrawExprUsingG28Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(G01Parser.T__1)
                self.state = 12
                localctx.a_cord = self.match(G01Parser.NUMBER)
                self.state = 13
                localctx.b_cord = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__2]:
                localctx = G01Parser.LastDrawExprUsingFContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(G01Parser.T__2)
                self.state = 15
                localctx.c_cord = self.match(G01Parser.NUMBER)
                self.state = 16
                localctx.d_cord = self.match(G01Parser.NUMBER)
                pass
            elif token in [G01Parser.T__3]:
                localctx = G01Parser.PrintForAllGrammarCodesContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.match(G01Parser.T__3)
                self.state = 18
                localctx.x_cord = self.match(G01Parser.NUMBER)
                self.state = 19
                localctx.y_cord = self.match(G01Parser.NUMBER)
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





