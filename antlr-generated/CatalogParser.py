# Generated from Catalog.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("#\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2!\2\7\3")
        buf.write("\2\2\2\4\r\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2")
        buf.write("\t\7\3\2\2\2\t\n\3\2\2\2\n\13\3\2\2\2\13\f\7\2\2\3\f\3")
        buf.write("\3\2\2\2\r\16\7\4\2\2\16\17\7\3\2\2\17\20\7\n\2\2\20\21")
        buf.write("\7\13\2\2\21\22\7\5\2\2\22\23\7\3\2\2\23\24\7\20\2\2\24")
        buf.write("\25\7\13\2\2\25\26\7\6\2\2\26\27\7\3\2\2\27\30\7\t\2\2")
        buf.write("\30\31\7\13\2\2\31\32\7\7\2\2\32\33\7\3\2\2\33\34\7\20")
        buf.write("\2\2\34\35\7\13\2\2\35\36\7\b\2\2\36\37\7\3\2\2\37 \7")
        buf.write("\21\2\2 !\7\f\2\2!\5\3\2\2\2\3\t")
        return buf.getvalue()


class CatalogParser ( Parser ):

    grammarFileName = "Catalog.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "': '", "'Course'", "'Title'", "'Units'", 
                     "'Desc'", "'Prereq'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COURSELITERAL", "TITLELITERAL", 
                      "UNITSLITERAL", "DESCLITERAL", "PREREQLITERAL", "NUMBER", 
                      "WORD", "WS", "WSPLUS", "PUNC", "UNITS", "COURSENAME", 
                      "TITLEDESC", "PREREQ" ]

    RULE_catalog = 0
    RULE_course = 1

    ruleNames =  [ "catalog", "course" ]

    EOF = Token.EOF
    T__0=1
    COURSELITERAL=2
    TITLELITERAL=3
    UNITSLITERAL=4
    DESCLITERAL=5
    PREREQLITERAL=6
    NUMBER=7
    WORD=8
    WS=9
    WSPLUS=10
    PUNC=11
    UNITS=12
    COURSENAME=13
    TITLEDESC=14
    PREREQ=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CatalogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CatalogParser.EOF, 0)

        def course(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CatalogParser.CourseContext)
            else:
                return self.getTypedRuleContext(CatalogParser.CourseContext,i)


        def getRuleIndex(self):
            return CatalogParser.RULE_catalog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatalog" ):
                listener.enterCatalog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatalog" ):
                listener.exitCatalog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatalog" ):
                return visitor.visitCatalog(self)
            else:
                return visitor.visitChildren(self)




    def catalog(self):

        localctx = CatalogParser.CatalogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_catalog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.course()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CatalogParser.COURSELITERAL):
                    break

            self.state = 9
            self.match(CatalogParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CourseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COURSELITERAL(self):
            return self.getToken(CatalogParser.COURSELITERAL, 0)

        def WORD(self):
            return self.getToken(CatalogParser.WORD, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(CatalogParser.WS)
            else:
                return self.getToken(CatalogParser.WS, i)

        def TITLELITERAL(self):
            return self.getToken(CatalogParser.TITLELITERAL, 0)

        def TITLEDESC(self, i:int=None):
            if i is None:
                return self.getTokens(CatalogParser.TITLEDESC)
            else:
                return self.getToken(CatalogParser.TITLEDESC, i)

        def UNITSLITERAL(self):
            return self.getToken(CatalogParser.UNITSLITERAL, 0)

        def NUMBER(self):
            return self.getToken(CatalogParser.NUMBER, 0)

        def DESCLITERAL(self):
            return self.getToken(CatalogParser.DESCLITERAL, 0)

        def PREREQLITERAL(self):
            return self.getToken(CatalogParser.PREREQLITERAL, 0)

        def PREREQ(self):
            return self.getToken(CatalogParser.PREREQ, 0)

        def WSPLUS(self):
            return self.getToken(CatalogParser.WSPLUS, 0)

        def getRuleIndex(self):
            return CatalogParser.RULE_course

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourse" ):
                listener.enterCourse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourse" ):
                listener.exitCourse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourse" ):
                return visitor.visitCourse(self)
            else:
                return visitor.visitChildren(self)




    def course(self):

        localctx = CatalogParser.CourseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_course)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(CatalogParser.COURSELITERAL)
            self.state = 12
            self.match(CatalogParser.T__0)
            self.state = 13
            self.match(CatalogParser.WORD)
            self.state = 14
            self.match(CatalogParser.WS)
            self.state = 15
            self.match(CatalogParser.TITLELITERAL)
            self.state = 16
            self.match(CatalogParser.T__0)
            self.state = 17
            self.match(CatalogParser.TITLEDESC)
            self.state = 18
            self.match(CatalogParser.WS)
            self.state = 19
            self.match(CatalogParser.UNITSLITERAL)
            self.state = 20
            self.match(CatalogParser.T__0)
            self.state = 21
            self.match(CatalogParser.NUMBER)
            self.state = 22
            self.match(CatalogParser.WS)
            self.state = 23
            self.match(CatalogParser.DESCLITERAL)
            self.state = 24
            self.match(CatalogParser.T__0)
            self.state = 25
            self.match(CatalogParser.TITLEDESC)
            self.state = 26
            self.match(CatalogParser.WS)
            self.state = 27
            self.match(CatalogParser.PREREQLITERAL)
            self.state = 28
            self.match(CatalogParser.T__0)
            self.state = 29
            self.match(CatalogParser.PREREQ)
            self.state = 30
            self.match(CatalogParser.WSPLUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





