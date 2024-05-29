# Generated from Lora.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,288,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,4,0,65,8,0,11,0,
        12,0,66,1,1,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,1,5,1,5,5,5,86,8,5,10,5,12,5,89,9,5,1,6,1,6,1,6,3,6,94,8,6,
        1,6,1,6,1,7,1,7,1,7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,1,7,1,7,1,
        8,1,8,1,8,1,8,5,8,113,8,8,10,8,12,8,116,9,8,3,8,118,8,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,130,8,10,10,10,12,10,133,
        9,10,3,10,135,8,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,156,8,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        5,12,171,8,12,10,12,12,12,174,9,12,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,5,14,183,8,14,10,14,12,14,186,9,14,1,14,1,14,1,14,3,14,191,
        8,14,1,14,1,14,1,14,1,14,5,14,197,8,14,10,14,12,14,200,9,14,1,14,
        1,14,1,14,1,14,3,14,206,8,14,3,14,208,8,14,1,15,1,15,3,15,212,8,
        15,1,16,1,16,1,16,1,16,5,16,218,8,16,10,16,12,16,221,9,16,3,16,223,
        8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,3,18,
        236,8,18,1,19,1,19,1,20,1,20,4,20,242,8,20,11,20,12,20,243,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,268,8,23,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,3,25,278,8,25,1,26,1,26,1,26,1,26,
        1,26,1,26,3,26,286,8,26,1,26,0,1,24,27,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,4,1,0,12,16,
        1,0,25,26,1,0,23,24,1,0,27,35,300,0,59,1,0,0,0,2,68,1,0,0,0,4,74,
        1,0,0,0,6,78,1,0,0,0,8,80,1,0,0,0,10,82,1,0,0,0,12,90,1,0,0,0,14,
        97,1,0,0,0,16,108,1,0,0,0,18,121,1,0,0,0,20,125,1,0,0,0,22,138,1,
        0,0,0,24,155,1,0,0,0,26,175,1,0,0,0,28,207,1,0,0,0,30,211,1,0,0,
        0,32,213,1,0,0,0,34,226,1,0,0,0,36,235,1,0,0,0,38,237,1,0,0,0,40,
        239,1,0,0,0,42,247,1,0,0,0,44,255,1,0,0,0,46,261,1,0,0,0,48,269,
        1,0,0,0,50,277,1,0,0,0,52,285,1,0,0,0,54,55,3,2,1,0,55,56,5,38,0,
        0,56,58,1,0,0,0,57,54,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,
        1,0,0,0,60,64,1,0,0,0,61,59,1,0,0,0,62,65,3,52,26,0,63,65,3,34,17,
        0,64,62,1,0,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,
        1,0,0,0,67,1,1,0,0,0,68,69,5,9,0,0,69,72,5,11,0,0,70,71,5,10,0,0,
        71,73,5,11,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,3,1,0,0,0,74,75,5,
        11,0,0,75,76,5,39,0,0,76,77,5,11,0,0,77,5,1,0,0,0,78,79,7,0,0,0,
        79,7,1,0,0,0,80,81,5,11,0,0,81,9,1,0,0,0,82,87,3,24,12,0,83,84,5,
        37,0,0,84,86,3,24,12,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,
        87,88,1,0,0,0,88,11,1,0,0,0,89,87,1,0,0,0,90,91,5,11,0,0,91,93,5,
        19,0,0,92,94,3,10,5,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,
        95,96,5,20,0,0,96,13,1,0,0,0,97,98,5,21,0,0,98,103,3,24,12,0,99,
        100,5,37,0,0,100,102,3,24,12,0,101,99,1,0,0,0,102,105,1,0,0,0,103,
        101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,
        107,5,22,0,0,107,15,1,0,0,0,108,117,5,21,0,0,109,114,3,24,12,0,110,
        111,5,37,0,0,111,113,3,24,12,0,112,110,1,0,0,0,113,116,1,0,0,0,114,
        112,1,0,0,0,114,115,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,117,
        109,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,5,22,0,0,120,
        17,1,0,0,0,121,122,5,11,0,0,122,123,5,39,0,0,123,124,3,24,12,0,124,
        19,1,0,0,0,125,134,5,17,0,0,126,131,3,18,9,0,127,128,5,37,0,0,128,
        130,3,18,9,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,
        132,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,134,126,1,0,0,0,134,
        135,1,0,0,0,135,136,1,0,0,0,136,137,5,18,0,0,137,21,1,0,0,0,138,
        139,5,40,0,0,139,140,5,11,0,0,140,23,1,0,0,0,141,142,6,12,-1,0,142,
        156,3,6,3,0,143,156,3,16,8,0,144,156,3,20,10,0,145,146,5,19,0,0,
        146,147,3,24,12,0,147,148,5,20,0,0,148,156,1,0,0,0,149,150,5,19,
        0,0,150,151,3,10,5,0,151,152,5,20,0,0,152,156,1,0,0,0,153,156,3,
        8,4,0,154,156,3,12,6,0,155,141,1,0,0,0,155,143,1,0,0,0,155,144,1,
        0,0,0,155,145,1,0,0,0,155,149,1,0,0,0,155,153,1,0,0,0,155,154,1,
        0,0,0,156,172,1,0,0,0,157,158,10,3,0,0,158,159,7,1,0,0,159,171,3,
        24,12,4,160,161,10,2,0,0,161,162,7,2,0,0,162,171,3,24,12,3,163,164,
        10,1,0,0,164,165,7,3,0,0,165,171,3,24,12,2,166,167,10,5,0,0,167,
        171,3,14,7,0,168,169,10,4,0,0,169,171,3,22,11,0,170,157,1,0,0,0,
        170,160,1,0,0,0,170,163,1,0,0,0,170,166,1,0,0,0,170,168,1,0,0,0,
        171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,25,1,0,0,0,174,
        172,1,0,0,0,175,176,3,4,2,0,176,177,5,36,0,0,177,178,3,24,12,0,178,
        27,1,0,0,0,179,184,5,11,0,0,180,181,5,37,0,0,181,183,5,11,0,0,182,
        180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,
        187,1,0,0,0,186,184,1,0,0,0,187,190,5,36,0,0,188,191,3,24,12,0,189,
        191,3,10,5,0,190,188,1,0,0,0,190,189,1,0,0,0,191,208,1,0,0,0,192,
        193,5,19,0,0,193,198,5,11,0,0,194,195,5,37,0,0,195,197,5,11,0,0,
        196,194,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,
        199,201,1,0,0,0,200,198,1,0,0,0,201,202,5,20,0,0,202,205,5,36,0,
        0,203,206,3,24,12,0,204,206,3,10,5,0,205,203,1,0,0,0,205,204,1,0,
        0,0,206,208,1,0,0,0,207,179,1,0,0,0,207,192,1,0,0,0,208,29,1,0,0,
        0,209,212,5,11,0,0,210,212,3,4,2,0,211,209,1,0,0,0,211,210,1,0,0,
        0,212,31,1,0,0,0,213,222,5,19,0,0,214,219,3,30,15,0,215,216,5,37,
        0,0,216,218,3,30,15,0,217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,
        0,0,0,219,220,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,222,214,1,
        0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,225,5,20,0,0,225,33,1,
        0,0,0,226,227,5,6,0,0,227,228,5,11,0,0,228,229,3,32,16,0,229,230,
        3,40,20,0,230,35,1,0,0,0,231,232,5,7,0,0,232,236,3,24,12,0,233,234,
        5,7,0,0,234,236,3,10,5,0,235,231,1,0,0,0,235,233,1,0,0,0,236,37,
        1,0,0,0,237,238,5,5,0,0,238,39,1,0,0,0,239,241,5,17,0,0,240,242,
        3,52,26,0,241,240,1,0,0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,
        1,0,0,0,244,245,1,0,0,0,245,246,5,18,0,0,246,41,1,0,0,0,247,248,
        5,2,0,0,248,249,5,19,0,0,249,250,5,11,0,0,250,251,5,4,0,0,251,252,
        3,24,12,0,252,253,5,20,0,0,253,254,3,40,20,0,254,43,1,0,0,0,255,
        256,5,3,0,0,256,257,5,19,0,0,257,258,3,24,12,0,258,259,5,20,0,0,
        259,260,3,40,20,0,260,45,1,0,0,0,261,262,5,1,0,0,262,263,5,19,0,
        0,263,264,3,24,12,0,264,265,5,20,0,0,265,267,3,40,20,0,266,268,3,
        48,24,0,267,266,1,0,0,0,267,268,1,0,0,0,268,47,1,0,0,0,269,270,5,
        8,0,0,270,271,3,40,20,0,271,49,1,0,0,0,272,278,3,26,13,0,273,278,
        3,28,14,0,274,278,3,38,19,0,275,278,3,36,18,0,276,278,3,24,12,0,
        277,272,1,0,0,0,277,273,1,0,0,0,277,274,1,0,0,0,277,275,1,0,0,0,
        277,276,1,0,0,0,278,51,1,0,0,0,279,286,3,46,23,0,280,281,3,50,25,
        0,281,282,5,38,0,0,282,286,1,0,0,0,283,286,3,42,21,0,284,286,3,44,
        22,0,285,279,1,0,0,0,285,280,1,0,0,0,285,283,1,0,0,0,285,284,1,0,
        0,0,286,53,1,0,0,0,27,59,64,66,72,87,93,103,114,117,131,134,155,
        170,172,184,190,198,205,207,211,219,222,235,243,267,277,285
    ]

class LoraParser ( Parser ):

    grammarFileName = "Lora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'for'", "'while'", "'in'", "'break'", 
                     "'function'", "'return'", "'else'", "'import'", "'as'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'None'", "'{'", "'}'", "'('", "')'", 
                     "'['", "']'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'and'", "'or'", "'not'", 
                     "'='", "','", "';'", "':'", "'.'", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "IF", "FOR", "WHILE", "IN", "BREAK", 
                      "FUNCTION", "RETURN", "ELSE", "IMPORT", "AS", "ID", 
                      "INTEGER_VALUE", "FLOAT_VALUE", "STRING_VALUE", "BOOL_VALUE", 
                      "NONE", "BLOCK_START", "BLOCK_END", "LPAREN", "RPAREN", 
                      "LSQUARE", "RSQUARE", "PLUS", "MINUS", "MULT", "DIV", 
                      "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "AND", "OR", 
                      "NOT", "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", 
                      "INTEND", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_import_statement = 1
    RULE_typed_variable = 2
    RULE_value = 3
    RULE_variable_reference = 4
    RULE_tuple = 5
    RULE_function_call = 6
    RULE_index_operator = 7
    RULE_array = 8
    RULE_object_field = 9
    RULE_object = 10
    RULE_attribute_operator = 11
    RULE_expression = 12
    RULE_typed_assignment = 13
    RULE_assignment = 14
    RULE_function_parameter = 15
    RULE_function_parameters_list = 16
    RULE_function_declaration = 17
    RULE_return_statement = 18
    RULE_break_statement = 19
    RULE_code_block = 20
    RULE_for_loop_statement = 21
    RULE_while_loop_statement = 22
    RULE_if_statement = 23
    RULE_else_statement = 24
    RULE_simple_statement = 25
    RULE_statement = 26

    ruleNames =  [ "program", "import_statement", "typed_variable", "value", 
                   "variable_reference", "tuple", "function_call", "index_operator", 
                   "array", "object_field", "object", "attribute_operator", 
                   "expression", "typed_assignment", "assignment", "function_parameter", 
                   "function_parameters_list", "function_declaration", "return_statement", 
                   "break_statement", "code_block", "for_loop_statement", 
                   "while_loop_statement", "if_statement", "else_statement", 
                   "simple_statement", "statement" ]

    EOF = Token.EOF
    IF=1
    FOR=2
    WHILE=3
    IN=4
    BREAK=5
    FUNCTION=6
    RETURN=7
    ELSE=8
    IMPORT=9
    AS=10
    ID=11
    INTEGER_VALUE=12
    FLOAT_VALUE=13
    STRING_VALUE=14
    BOOL_VALUE=15
    NONE=16
    BLOCK_START=17
    BLOCK_END=18
    LPAREN=19
    RPAREN=20
    LSQUARE=21
    RSQUARE=22
    PLUS=23
    MINUS=24
    MULT=25
    DIV=26
    EQ=27
    NEQ=28
    LT=29
    LTE=30
    GT=31
    GTE=32
    AND=33
    OR=34
    NOT=35
    ASSIGN=36
    COMMA=37
    SEMI=38
    COLON=39
    DOT=40
    INTEND=41
    WS=42
    COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.Import_statementContext)
            else:
                return self.getTypedRuleContext(LoraParser.Import_statementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.SEMI)
            else:
                return self.getToken(LoraParser.SEMI, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.StatementContext)
            else:
                return self.getTypedRuleContext(LoraParser.StatementContext,i)


        def function_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.Function_declarationContext)
            else:
                return self.getTypedRuleContext(LoraParser.Function_declarationContext,i)


        def getRuleIndex(self):
            return LoraParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LoraParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 54
                self.import_statement()
                self.state = 55
                self.match(LoraParser.SEMI)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 5, 7, 11, 12, 13, 14, 15, 16, 17, 19, 21]:
                    self.state = 62
                    self.statement()
                    pass
                elif token in [6]:
                    self.state = 63
                    self.function_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2881774) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(LoraParser.IMPORT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.ID)
            else:
                return self.getToken(LoraParser.ID, i)

        def AS(self):
            return self.getToken(LoraParser.AS, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_statement" ):
                listener.enterImport_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_statement" ):
                listener.exitImport_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_statement" ):
                return visitor.visitImport_statement(self)
            else:
                return visitor.visitChildren(self)




    def import_statement(self):

        localctx = LoraParser.Import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_import_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LoraParser.IMPORT)
            self.state = 69
            self.match(LoraParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 70
                self.match(LoraParser.AS)
                self.state = 71
                self.match(LoraParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typed_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.ID)
            else:
                return self.getToken(LoraParser.ID, i)

        def COLON(self):
            return self.getToken(LoraParser.COLON, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_typed_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyped_variable" ):
                listener.enterTyped_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyped_variable" ):
                listener.exitTyped_variable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyped_variable" ):
                return visitor.visitTyped_variable(self)
            else:
                return visitor.visitChildren(self)




    def typed_variable(self):

        localctx = LoraParser.Typed_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typed_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(LoraParser.ID)
            self.state = 75
            self.match(LoraParser.COLON)
            self.state = 76
            self.match(LoraParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_VALUE(self):
            return self.getToken(LoraParser.INTEGER_VALUE, 0)

        def FLOAT_VALUE(self):
            return self.getToken(LoraParser.FLOAT_VALUE, 0)

        def STRING_VALUE(self):
            return self.getToken(LoraParser.STRING_VALUE, 0)

        def BOOL_VALUE(self):
            return self.getToken(LoraParser.BOOL_VALUE, 0)

        def NONE(self):
            return self.getToken(LoraParser.NONE, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = LoraParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_variable_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_reference" ):
                listener.enterVariable_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_reference" ):
                listener.exitVariable_reference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_reference" ):
                return visitor.visitVariable_reference(self)
            else:
                return visitor.visitChildren(self)




    def variable_reference(self):

        localctx = LoraParser.Variable_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LoraParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoraParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.COMMA)
            else:
                return self.getToken(LoraParser.COMMA, i)

        def getRuleIndex(self):
            return LoraParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = LoraParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.expression(0)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 83
                self.match(LoraParser.COMMA)
                self.state = 84
                self.expression(0)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def tuple_(self):
            return self.getTypedRuleContext(LoraParser.TupleContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = LoraParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(LoraParser.ID)
            self.state = 91
            self.match(LoraParser.LPAREN)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2881536) != 0):
                self.state = 92
                self.tuple_()


            self.state = 95
            self.match(LoraParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(LoraParser.LSQUARE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoraParser.ExpressionContext,i)


        def RSQUARE(self):
            return self.getToken(LoraParser.RSQUARE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.COMMA)
            else:
                return self.getToken(LoraParser.COMMA, i)

        def getRuleIndex(self):
            return LoraParser.RULE_index_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_operator" ):
                listener.enterIndex_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_operator" ):
                listener.exitIndex_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = LoraParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_index_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(LoraParser.LSQUARE)
            self.state = 98
            self.expression(0)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 99
                self.match(LoraParser.COMMA)
                self.state = 100
                self.expression(0)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(LoraParser.RSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(LoraParser.LSQUARE, 0)

        def RSQUARE(self):
            return self.getToken(LoraParser.RSQUARE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoraParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.COMMA)
            else:
                return self.getToken(LoraParser.COMMA, i)

        def getRuleIndex(self):
            return LoraParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = LoraParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(LoraParser.LSQUARE)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2881536) != 0):
                self.state = 109
                self.expression(0)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 110
                    self.match(LoraParser.COMMA)
                    self.state = 111
                    self.expression(0)
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 119
            self.match(LoraParser.RSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def COLON(self):
            return self.getToken(LoraParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_object_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_field" ):
                listener.enterObject_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_field" ):
                listener.exitObject_field(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_field" ):
                return visitor.visitObject_field(self)
            else:
                return visitor.visitChildren(self)




    def object_field(self):

        localctx = LoraParser.Object_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_object_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(LoraParser.ID)
            self.state = 122
            self.match(LoraParser.COLON)
            self.state = 123
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_START(self):
            return self.getToken(LoraParser.BLOCK_START, 0)

        def BLOCK_END(self):
            return self.getToken(LoraParser.BLOCK_END, 0)

        def object_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.Object_fieldContext)
            else:
                return self.getTypedRuleContext(LoraParser.Object_fieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.COMMA)
            else:
                return self.getToken(LoraParser.COMMA, i)

        def getRuleIndex(self):
            return LoraParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = LoraParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(LoraParser.BLOCK_START)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 126
                self.object_field()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 127
                    self.match(LoraParser.COMMA)
                    self.state = 128
                    self.object_field()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 136
            self.match(LoraParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(LoraParser.DOT, 0)

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_attribute_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_operator" ):
                listener.enterAttribute_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_operator" ):
                listener.exitAttribute_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_operator" ):
                return visitor.visitAttribute_operator(self)
            else:
                return visitor.visitChildren(self)




    def attribute_operator(self):

        localctx = LoraParser.Attribute_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attribute_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(LoraParser.DOT)
            self.state = 139
            self.match(LoraParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def value(self):
            return self.getTypedRuleContext(LoraParser.ValueContext,0)


        def array(self):
            return self.getTypedRuleContext(LoraParser.ArrayContext,0)


        def object_(self):
            return self.getTypedRuleContext(LoraParser.ObjectContext,0)


        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoraParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def tuple_(self):
            return self.getTypedRuleContext(LoraParser.TupleContext,0)


        def variable_reference(self):
            return self.getTypedRuleContext(LoraParser.Variable_referenceContext,0)


        def function_call(self):
            return self.getTypedRuleContext(LoraParser.Function_callContext,0)


        def MULT(self):
            return self.getToken(LoraParser.MULT, 0)

        def DIV(self):
            return self.getToken(LoraParser.DIV, 0)

        def PLUS(self):
            return self.getToken(LoraParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LoraParser.MINUS, 0)

        def EQ(self):
            return self.getToken(LoraParser.EQ, 0)

        def NEQ(self):
            return self.getToken(LoraParser.NEQ, 0)

        def LT(self):
            return self.getToken(LoraParser.LT, 0)

        def LTE(self):
            return self.getToken(LoraParser.LTE, 0)

        def GT(self):
            return self.getToken(LoraParser.GT, 0)

        def GTE(self):
            return self.getToken(LoraParser.GTE, 0)

        def AND(self):
            return self.getToken(LoraParser.AND, 0)

        def OR(self):
            return self.getToken(LoraParser.OR, 0)

        def NOT(self):
            return self.getToken(LoraParser.NOT, 0)

        def index_operator(self):
            return self.getTypedRuleContext(LoraParser.Index_operatorContext,0)


        def attribute_operator(self):
            return self.getTypedRuleContext(LoraParser.Attribute_operatorContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LoraParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 142
                self.value()
                pass

            elif la_ == 2:
                self.state = 143
                self.array()
                pass

            elif la_ == 3:
                self.state = 144
                self.object_()
                pass

            elif la_ == 4:
                self.state = 145
                self.match(LoraParser.LPAREN)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(LoraParser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 149
                self.match(LoraParser.LPAREN)
                self.state = 150
                self.tuple_()
                self.state = 151
                self.match(LoraParser.RPAREN)
                pass

            elif la_ == 6:
                self.state = 153
                self.variable_reference()
                pass

            elif la_ == 7:
                self.state = 154
                self.function_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 170
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = LoraParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 158
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 159
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = LoraParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 161
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 162
                        self.expression(3)
                        pass

                    elif la_ == 3:
                        localctx = LoraParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 164
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68585259008) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 165
                        self.expression(2)
                        pass

                    elif la_ == 4:
                        localctx = LoraParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 167
                        self.index_operator()
                        pass

                    elif la_ == 5:
                        localctx = LoraParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 169
                        self.attribute_operator()
                        pass

             
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Typed_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typed_variable(self):
            return self.getTypedRuleContext(LoraParser.Typed_variableContext,0)


        def ASSIGN(self):
            return self.getToken(LoraParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_typed_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyped_assignment" ):
                listener.enterTyped_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyped_assignment" ):
                listener.exitTyped_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyped_assignment" ):
                return visitor.visitTyped_assignment(self)
            else:
                return visitor.visitChildren(self)




    def typed_assignment(self):

        localctx = LoraParser.Typed_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typed_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.typed_variable()
            self.state = 176
            self.match(LoraParser.ASSIGN)
            self.state = 177
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.ID)
            else:
                return self.getToken(LoraParser.ID, i)

        def ASSIGN(self):
            return self.getToken(LoraParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(LoraParser.TupleContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.COMMA)
            else:
                return self.getToken(LoraParser.COMMA, i)

        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LoraParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(LoraParser.ID)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 180
                    self.match(LoraParser.COMMA)
                    self.state = 181
                    self.match(LoraParser.ID)
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 187
                self.match(LoraParser.ASSIGN)
                self.state = 190
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 188
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 189
                    self.tuple_()
                    pass


                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(LoraParser.LPAREN)
                self.state = 193
                self.match(LoraParser.ID)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 194
                    self.match(LoraParser.COMMA)
                    self.state = 195
                    self.match(LoraParser.ID)
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 201
                self.match(LoraParser.RPAREN)
                self.state = 202
                self.match(LoraParser.ASSIGN)
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 204
                    self.tuple_()
                    pass


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


    class Function_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def typed_variable(self):
            return self.getTypedRuleContext(LoraParser.Typed_variableContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_function_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_parameter" ):
                listener.enterFunction_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_parameter" ):
                listener.exitFunction_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_parameter" ):
                return visitor.visitFunction_parameter(self)
            else:
                return visitor.visitChildren(self)




    def function_parameter(self):

        localctx = LoraParser.Function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_parameter)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(LoraParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.typed_variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_parameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def function_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.Function_parameterContext)
            else:
                return self.getTypedRuleContext(LoraParser.Function_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LoraParser.COMMA)
            else:
                return self.getToken(LoraParser.COMMA, i)

        def getRuleIndex(self):
            return LoraParser.RULE_function_parameters_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_parameters_list" ):
                listener.enterFunction_parameters_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_parameters_list" ):
                listener.exitFunction_parameters_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_parameters_list" ):
                return visitor.visitFunction_parameters_list(self)
            else:
                return visitor.visitChildren(self)




    def function_parameters_list(self):

        localctx = LoraParser.Function_parameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_parameters_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(LoraParser.LPAREN)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 214
                self.function_parameter()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 215
                    self.match(LoraParser.COMMA)
                    self.state = 216
                    self.function_parameter()
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 224
            self.match(LoraParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LoraParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def function_parameters_list(self):
            return self.getTypedRuleContext(LoraParser.Function_parameters_listContext,0)


        def code_block(self):
            return self.getTypedRuleContext(LoraParser.Code_blockContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = LoraParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(LoraParser.FUNCTION)
            self.state = 227
            self.match(LoraParser.ID)
            self.state = 228
            self.function_parameters_list()
            self.state = 229
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LoraParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(LoraParser.TupleContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = LoraParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_statement)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(LoraParser.RETURN)
                self.state = 232
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(LoraParser.RETURN)
                self.state = 234
                self.tuple_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(LoraParser.BREAK, 0)

        def getRuleIndex(self):
            return LoraParser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = LoraParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(LoraParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_START(self):
            return self.getToken(LoraParser.BLOCK_START, 0)

        def BLOCK_END(self):
            return self.getToken(LoraParser.BLOCK_END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoraParser.StatementContext)
            else:
                return self.getTypedRuleContext(LoraParser.StatementContext,i)


        def getRuleIndex(self):
            return LoraParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = LoraParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(LoraParser.BLOCK_START)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240
                self.statement()
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2881710) != 0)):
                    break

            self.state = 245
            self.match(LoraParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LoraParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def ID(self):
            return self.getToken(LoraParser.ID, 0)

        def IN(self):
            return self.getToken(LoraParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(LoraParser.Code_blockContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_for_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop_statement" ):
                listener.enterFor_loop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop_statement" ):
                listener.exitFor_loop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_statement" ):
                return visitor.visitFor_loop_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_statement(self):

        localctx = LoraParser.For_loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_loop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(LoraParser.FOR)
            self.state = 248
            self.match(LoraParser.LPAREN)
            self.state = 249
            self.match(LoraParser.ID)
            self.state = 250
            self.match(LoraParser.IN)
            self.state = 251
            self.expression(0)
            self.state = 252
            self.match(LoraParser.RPAREN)
            self.state = 253
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LoraParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(LoraParser.Code_blockContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_while_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop_statement" ):
                listener.enterWhile_loop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop_statement" ):
                listener.exitWhile_loop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop_statement" ):
                return visitor.visitWhile_loop_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_loop_statement(self):

        localctx = LoraParser.While_loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_while_loop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(LoraParser.WHILE)
            self.state = 256
            self.match(LoraParser.LPAREN)
            self.state = 257
            self.expression(0)
            self.state = 258
            self.match(LoraParser.RPAREN)
            self.state = 259
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LoraParser.IF, 0)

        def LPAREN(self):
            return self.getToken(LoraParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LoraParser.RPAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(LoraParser.Code_blockContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(LoraParser.Else_statementContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = LoraParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(LoraParser.IF)
            self.state = 262
            self.match(LoraParser.LPAREN)
            self.state = 263
            self.expression(0)
            self.state = 264
            self.match(LoraParser.RPAREN)
            self.state = 265
            self.code_block()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 266
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LoraParser.ELSE, 0)

        def code_block(self):
            return self.getTypedRuleContext(LoraParser.Code_blockContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = LoraParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(LoraParser.ELSE)
            self.state = 270
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typed_assignment(self):
            return self.getTypedRuleContext(LoraParser.Typed_assignmentContext,0)


        def assignment(self):
            return self.getTypedRuleContext(LoraParser.AssignmentContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(LoraParser.Break_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(LoraParser.Return_statementContext,0)


        def expression(self):
            return self.getTypedRuleContext(LoraParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_simple_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_statement" ):
                listener.enterSimple_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_statement" ):
                listener.exitSimple_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_statement" ):
                return visitor.visitSimple_statement(self)
            else:
                return visitor.visitChildren(self)




    def simple_statement(self):

        localctx = LoraParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_simple_statement)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.typed_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 275
                self.return_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 276
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(LoraParser.If_statementContext,0)


        def simple_statement(self):
            return self.getTypedRuleContext(LoraParser.Simple_statementContext,0)


        def SEMI(self):
            return self.getToken(LoraParser.SEMI, 0)

        def for_loop_statement(self):
            return self.getTypedRuleContext(LoraParser.For_loop_statementContext,0)


        def while_loop_statement(self):
            return self.getTypedRuleContext(LoraParser.While_loop_statementContext,0)


        def getRuleIndex(self):
            return LoraParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LoraParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.if_statement()
                pass
            elif token in [5, 7, 11, 12, 13, 14, 15, 16, 17, 19, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.simple_statement()
                self.state = 281
                self.match(LoraParser.SEMI)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.for_loop_statement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.while_loop_statement()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




