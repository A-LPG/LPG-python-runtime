
    ##line 120 "dtParserTemplateF.gi

from lpg2 import ArrayList, BadParseException, RuleAction, PrsStream, ParseTable, BacktrackingParser, IToken, ErrorToken, ILexStream, NullExportedSymbolsException, UnimplementedTerminalsException,  UndefinedEofSymbolException, NotBacktrackParseTableException, BadParseSymFileException, IPrsStream, Monitor, DiagnoseParser, IAst, IAstVisitor, IAbstractArrayList, NotDeterministicParseTableException,DeterministicParser, NullTerminalSymbolsException 
from LPGParserprs import  LPGParserprs 
from LPGParsersym import  LPGParsersym 

    ##line 8 "LPGParser.g


 
    ##line 128 "dtParserTemplateF.gi

class LPGParser(RuleAction):

    def ruleAction(self, ruleNumber) :
        act = self.__rule_action[ruleNumber]
        if act:
            act() 
    
    prsTable = LPGParserprs()

    def getParseTable(sel):
        return LPGParser.prsTable 

    def getParser(self):
        return self.dtParser 

    def setResult(self, object1 ):
        self.dtParser.setSym1(object1) 

    def getRhsSym(self, i):
        return self.dtParser.getSym(i) 

    def getRhsTokenIndex(self, i)  :  
        return self.dtParser.getToken(i) 

    def getRhsIToken(self, i) :
        return self.prsStream.getIToken(self.getRhsTokenIndex(i)) 
    
    def getRhsFirstTokenIndex(self, i) :
        return self.dtParser.getFirstToken(i) 

    def getRhsFirstIToken(self, i)  : 
        return self.prsStream.getIToken(self.getRhsFirstTokenIndex(i)) 

    def getRhsLastTokenIndex(self, i) :
        return self.dtParser.getLastToken(i) 

    def getRhsLastIToken(self, i) :
        return self.prsStream.getIToken(self.getRhsLastTokenIndex(i)) 

    def getLeftSpan(self) :
        return self.dtParser.getFirstToken() 

    def getLeftIToken(self) :
        return self.prsStream.getIToken(self.getLeftSpan()) 

    def getRightSpan(self)  :
        return self.dtParser.getLastToken() 

    def getRightIToken(self) :
        return self.prsStream.getIToken(self.getRightSpan()) 

    def getRhsErrorTokenIndex(self, i)  :
    
        index = self.dtParser.getToken(i)
        err = self.prsStream.getIToken(index)
        return index  if isinstance(err,ErrorToken)  else 0
    
    def getRhsErrorIToken(self, i) :
    
        index = self.dtParser.getToken(i)
        err = self.prsStream.getIToken(index)
        return  err if  isinstance(err,ErrorToken) else  None
    

    def reset(self, lexStream ) : 
    
        self.prsStream.resetLexStream(lexStream)
        self.dtParser.reset(self.prsStream)

        try:
            self.prsStream.remapTerminalSymbols(self.orderedTerminalSymbols(), LPGParser.prsTable.getEoftSymbol())    
        except NullExportedSymbolsException as e :
            pass
        except NullTerminalSymbolsException as e :
            pass
        except UnimplementedTerminalsException as e :
            if self.unimplementedSymbolsWarning:

                unimplemented_symbols = e.getSymbols()
                print("The Lexer will not scan the following token(s):")
                for i in range(unimplemented_symbols.size()):
                    id = unimplemented_symbols.get(i)
                    print("    " + str(LPGParsersym.orderedTerminalSymbols[id]) )      

        except UndefinedEofSymbolException as e :           
            raise ( UndefinedEofSymbolException
                                ("The Lexer does not implement the Eof symbol " +
                                LPGParsersym.orderedTerminalSymbols[LPGParser.prsTable.getEoftSymbol()]))
    def __init__(self, lexStream = None):
    
        
        self.__rule_action = [None]* (147 + 2)
        self.prsStream=PrsStream()
        self.btParser=None 
        self.unimplementedSymbolsWarning  = False
        self.initRuleAction()
        try:
            self.dtParser =  DeterministicParser(None, LPGParser.prsTable,  self)
        except NotDeterministicParseTableException as e:
            raise NotDeterministicParseTableException("Regenerate LPGParserprs.py with -NOBACKTRACK option")

        except BadParseSymFileException as e:        
            raise BadParseSymFileException("Bad Parser Symbol File -- LPGParsersym.py. Regenerate LPGParserprs.py")

        if lexStream is not None:
           self.reset(lexStream)
        
    
    def numTokenKinds(self) :
        return LPGParsersym.numTokenKinds 

    def orderedTerminalSymbols(self):
        return LPGParsersym.orderedTerminalSymbols 

    def getTokenKindName(self, kind ) :
        return LPGParsersym.orderedTerminalSymbols[kind]   

    def getEOFTokenKind(self) :
        return LPGParser.prsTable.getEoftSymbol() 

    def getIPrsStream(self):
        return self.prsStream 

    def parser(self, error_repair_count = 0 , monitor = None):
    
        self.dtParser.setMonitor(monitor)

        try:
            return self.dtParser.parseEntry()
        except BadParseException as e :
            self.prsStream.reset(e.error_token) # point to error token
            diagnoseParser =  DiagnoseParser(self.prsStream, LPGParser.prsTable)
            diagnoseParser.diagnose(e.error_token)
            
        return None
    #
    # Additional entry points, if any
    #
    

    ##line 38 "LPGParser.g


 
    ##line 45 "LPGParser.g


 
    ##line 222 "LPGParser.g


    ##line 273 "dtParserTemplateF.gi

    def initRuleAction(self) : 


        #
        # Rule 1:  LPG ::= options_segment LPG_INPUT
        #
         def Act1(): 
               ##line 44 "LPGParser.g"
                self.setResult(
                    ##line 44 LPGParser.g
                    LPG(self, self.getLeftIToken(), self.getRightIToken(),
                        ##line 44 LPGParser.g
                        self.getRhsSym(1),
                        ##line 44 LPGParser.g
                        self.getRhsSym(2))
                ##line 44 LPGParser.g
                )

         self.__rule_action[1]= Act1

        #
        # Rule 2:  LPG_INPUT ::= $Empty
        #
         def Act2(): 
               ##line 49 "LPGParser.g"
                self.setResult(
                    ##line 49 LPGParser.g
                    LPG_itemList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 49 LPGParser.g
                )

         self.__rule_action[2]= Act2

        #
        # Rule 3:  LPG_INPUT ::= LPG_INPUT LPG_item
        #
         def Act3(): 
               ##line 50 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[3]= Act3

        #
        # Rule 4:  LPG_item ::= ALIAS_KEY$ alias_segment END_KEY_OPT$
        #
         def Act4(): 
               ##line 53 "LPGParser.g"
                self.setResult(
                    ##line 53 LPGParser.g
                    AliasSeg(self.getLeftIToken(), self.getRightIToken(),
                             ##line 53 LPGParser.g
                             self.getRhsSym(2))
                ##line 53 LPGParser.g
                )

         self.__rule_action[4]= Act4

        #
        # Rule 5:  LPG_item ::= AST_KEY$ ast_segment END_KEY_OPT$
        #
         def Act5(): 
               ##line 54 "LPGParser.g"
                self.setResult(
                    ##line 54 LPGParser.g
                    AstSeg(self.getLeftIToken(), self.getRightIToken(),
                           ##line 54 LPGParser.g
                           self.getRhsSym(2))
                ##line 54 LPGParser.g
                )

         self.__rule_action[5]= Act5

        #
        # Rule 6:  LPG_item ::= DEFINE_KEY$ define_segment END_KEY_OPT$
        #
         def Act6(): 
               ##line 55 "LPGParser.g"
                self.setResult(
                    ##line 55 LPGParser.g
                    DefineSeg(self.getLeftIToken(), self.getRightIToken(),
                              ##line 55 LPGParser.g
                              self.getRhsSym(2))
                ##line 55 LPGParser.g
                )

         self.__rule_action[6]= Act6

        #
        # Rule 7:  LPG_item ::= EOF_KEY$ eof_segment END_KEY_OPT$
        #
         def Act7(): 
               ##line 56 "LPGParser.g"
                self.setResult(
                    ##line 56 LPGParser.g
                    EofSeg(self.getLeftIToken(), self.getRightIToken(),
                           ##line 56 LPGParser.g
                           self.getRhsSym(2))
                ##line 56 LPGParser.g
                )

         self.__rule_action[7]= Act7

        #
        # Rule 8:  LPG_item ::= EOL_KEY$ eol_segment END_KEY_OPT$
        #
         def Act8(): 
               ##line 57 "LPGParser.g"
                self.setResult(
                    ##line 57 LPGParser.g
                    EolSeg(self.getLeftIToken(), self.getRightIToken(),
                           ##line 57 LPGParser.g
                           self.getRhsSym(2))
                ##line 57 LPGParser.g
                )

         self.__rule_action[8]= Act8

        #
        # Rule 9:  LPG_item ::= ERROR_KEY$ error_segment END_KEY_OPT$
        #
         def Act9(): 
               ##line 58 "LPGParser.g"
                self.setResult(
                    ##line 58 LPGParser.g
                    ErrorSeg(self.getLeftIToken(), self.getRightIToken(),
                             ##line 58 LPGParser.g
                             self.getRhsSym(2))
                ##line 58 LPGParser.g
                )

         self.__rule_action[9]= Act9

        #
        # Rule 10:  LPG_item ::= EXPORT_KEY$ export_segment END_KEY_OPT$
        #
         def Act10(): 
               ##line 59 "LPGParser.g"
                self.setResult(
                    ##line 59 LPGParser.g
                    ExportSeg(self.getLeftIToken(), self.getRightIToken(),
                              ##line 59 LPGParser.g
                              self.getRhsSym(2))
                ##line 59 LPGParser.g
                )

         self.__rule_action[10]= Act10

        #
        # Rule 11:  LPG_item ::= GLOBALS_KEY$ globals_segment END_KEY_OPT$
        #
         def Act11(): 
               ##line 60 "LPGParser.g"
                self.setResult(
                    ##line 60 LPGParser.g
                    GlobalsSeg(self.getLeftIToken(), self.getRightIToken(),
                               ##line 60 LPGParser.g
                               self.getRhsSym(2))
                ##line 60 LPGParser.g
                )

         self.__rule_action[11]= Act11

        #
        # Rule 12:  LPG_item ::= HEADERS_KEY$ headers_segment END_KEY_OPT$
        #
         def Act12(): 
               ##line 61 "LPGParser.g"
                self.setResult(
                    ##line 61 LPGParser.g
                    HeadersSeg(self.getLeftIToken(), self.getRightIToken(),
                               ##line 61 LPGParser.g
                               self.getRhsSym(2))
                ##line 61 LPGParser.g
                )

         self.__rule_action[12]= Act12

        #
        # Rule 13:  LPG_item ::= IDENTIFIER_KEY$ identifier_segment END_KEY_OPT$
        #
         def Act13(): 
               ##line 62 "LPGParser.g"
                self.setResult(
                    ##line 62 LPGParser.g
                    IdentifierSeg(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 62 LPGParser.g
                                  self.getRhsSym(2))
                ##line 62 LPGParser.g
                )

         self.__rule_action[13]= Act13

        #
        # Rule 14:  LPG_item ::= IMPORT_KEY$ import_segment END_KEY_OPT$
        #
         def Act14(): 
               ##line 63 "LPGParser.g"
                self.setResult(
                    ##line 63 LPGParser.g
                    ImportSeg(self.getLeftIToken(), self.getRightIToken(),
                              ##line 63 LPGParser.g
                              self.getRhsSym(2))
                ##line 63 LPGParser.g
                )

         self.__rule_action[14]= Act14

        #
        # Rule 15:  LPG_item ::= INCLUDE_KEY$ include_segment END_KEY_OPT$
        #
         def Act15(): 
               ##line 64 "LPGParser.g"
                self.setResult(
                    ##line 64 LPGParser.g
                    IncludeSeg(self.getLeftIToken(), self.getRightIToken(),
                               ##line 64 LPGParser.g
                               self.getRhsSym(2))
                ##line 64 LPGParser.g
                )

         self.__rule_action[15]= Act15

        #
        # Rule 16:  LPG_item ::= KEYWORDS_KEY$ keywords_segment END_KEY_OPT$
        #
         def Act16(): 
               ##line 65 "LPGParser.g"
                self.setResult(
                    ##line 65 LPGParser.g
                    KeywordsSeg(self.getLeftIToken(), self.getRightIToken(),
                                ##line 65 LPGParser.g
                                self.getRhsSym(2))
                ##line 65 LPGParser.g
                )

         self.__rule_action[16]= Act16

        #
        # Rule 17:  LPG_item ::= NAMES_KEY$ names_segment END_KEY_OPT$
        #
         def Act17(): 
               ##line 66 "LPGParser.g"
                self.setResult(
                    ##line 66 LPGParser.g
                    NamesSeg(self.getLeftIToken(), self.getRightIToken(),
                             ##line 66 LPGParser.g
                             self.getRhsSym(2))
                ##line 66 LPGParser.g
                )

         self.__rule_action[17]= Act17

        #
        # Rule 18:  LPG_item ::= NOTICE_KEY$ notice_segment END_KEY_OPT$
        #
         def Act18(): 
               ##line 67 "LPGParser.g"
                self.setResult(
                    ##line 67 LPGParser.g
                    NoticeSeg(self.getLeftIToken(), self.getRightIToken(),
                              ##line 67 LPGParser.g
                              self.getRhsSym(2))
                ##line 67 LPGParser.g
                )

         self.__rule_action[18]= Act18

        #
        # Rule 19:  LPG_item ::= RULES_KEY$ rules_segment END_KEY_OPT$
        #
         def Act19(): 
               ##line 68 "LPGParser.g"
                self.setResult(
                    ##line 68 LPGParser.g
                    RulesSeg(self.getLeftIToken(), self.getRightIToken(),
                             ##line 68 LPGParser.g
                             self.getRhsSym(2))
                ##line 68 LPGParser.g
                )

         self.__rule_action[19]= Act19

        #
        # Rule 20:  LPG_item ::= SOFT_KEYWORDS_KEY$ keywords_segment END_KEY_OPT$
        #
         def Act20(): 
               ##line 69 "LPGParser.g"
                self.setResult(
                    ##line 69 LPGParser.g
                    SoftKeywordsSeg(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 69 LPGParser.g
                                    self.getRhsSym(2))
                ##line 69 LPGParser.g
                )

         self.__rule_action[20]= Act20

        #
        # Rule 21:  LPG_item ::= START_KEY$ start_segment END_KEY_OPT$
        #
         def Act21(): 
               ##line 70 "LPGParser.g"
                self.setResult(
                    ##line 70 LPGParser.g
                    StartSeg(self.getLeftIToken(), self.getRightIToken(),
                             ##line 70 LPGParser.g
                             self.getRhsSym(2))
                ##line 70 LPGParser.g
                )

         self.__rule_action[21]= Act21

        #
        # Rule 22:  LPG_item ::= TERMINALS_KEY$ terminals_segment END_KEY_OPT$
        #
         def Act22(): 
               ##line 71 "LPGParser.g"
                self.setResult(
                    ##line 71 LPGParser.g
                    TerminalsSeg(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 71 LPGParser.g
                                 self.getRhsSym(2))
                ##line 71 LPGParser.g
                )

         self.__rule_action[22]= Act22

        #
        # Rule 23:  LPG_item ::= TRAILERS_KEY$ trailers_segment END_KEY_OPT$
        #
         def Act23(): 
               ##line 72 "LPGParser.g"
                self.setResult(
                    ##line 72 LPGParser.g
                    TrailersSeg(self.getLeftIToken(), self.getRightIToken(),
                                ##line 72 LPGParser.g
                                self.getRhsSym(2))
                ##line 72 LPGParser.g
                )

         self.__rule_action[23]= Act23

        #
        # Rule 24:  LPG_item ::= TYPES_KEY$ types_segment END_KEY_OPT$
        #
         def Act24(): 
               ##line 73 "LPGParser.g"
                self.setResult(
                    ##line 73 LPGParser.g
                    TypesSeg(self.getLeftIToken(), self.getRightIToken(),
                             ##line 73 LPGParser.g
                             self.getRhsSym(2))
                ##line 73 LPGParser.g
                )

         self.__rule_action[24]= Act24

        #
        # Rule 25:  LPG_item ::= RECOVER_KEY$ recover_segment END_KEY_OPT$
        #
         def Act25(): 
               ##line 74 "LPGParser.g"
                self.setResult(
                    ##line 74 LPGParser.g
                    RecoverSeg(self.getLeftIToken(), self.getRightIToken(),
                               ##line 74 LPGParser.g
                               self.getRhsSym(2))
                ##line 74 LPGParser.g
                )

         self.__rule_action[25]= Act25

        #
        # Rule 26:  LPG_item ::= DISJOINTPREDECESSORSETS_KEY$ predecessor_segment END_KEY_OPT$
        #
         def Act26(): 
               ##line 75 "LPGParser.g"
                self.setResult(
                    ##line 75 LPGParser.g
                    PredecessorSeg(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 75 LPGParser.g
                                   self.getRhsSym(2))
                ##line 75 LPGParser.g
                )

         self.__rule_action[26]= Act26

        #
        # Rule 27:  options_segment ::= $Empty
        #
         def Act27(): 
               ##line 78 "LPGParser.g"
                self.setResult(
                    ##line 78 LPGParser.g
                    option_specList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 78 LPGParser.g
                )

         self.__rule_action[27]= Act27

        #
        # Rule 28:  options_segment ::= options_segment option_spec
        #
         def Act28(): 
               ##line 78 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[28]= Act28

        #
        # Rule 29:  option_spec ::= OPTIONS_KEY$ option_list
        #
         def Act29(): 
               ##line 79 "LPGParser.g"
                self.setResult(
                    ##line 79 LPGParser.g
                    option_spec(self.getLeftIToken(), self.getRightIToken(),
                                ##line 79 LPGParser.g
                                self.getRhsSym(2))
                ##line 79 LPGParser.g
                )

         self.__rule_action[29]= Act29

        #
        # Rule 30:  option_list ::= option
        #
         def Act30(): 
               ##line 80 "LPGParser.g"
                self.setResult(
                    ##line 80 LPGParser.g
                    optionList.optionListfromElement(self.getRhsSym(1), True )
                ##line 80 LPGParser.g
                )

         self.__rule_action[30]= Act30

        #
        # Rule 31:  option_list ::= option_list ,$ option
        #
         def Act31(): 
               ##line 80 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(3))

         self.__rule_action[31]= Act31

        #
        # Rule 32:  option ::= SYMBOL option_value
        #
         def Act32(): 
               ##line 81 "LPGParser.g"
                self.setResult(
                    ##line 81 LPGParser.g
                    option(self.getLeftIToken(), self.getRightIToken(),
                           ##line 81 LPGParser.g
                           ASTNodeToken(self.getRhsIToken(1)),
                           ##line 81 LPGParser.g
                           self.getRhsSym(2))
                ##line 81 LPGParser.g
                )

         self.__rule_action[32]= Act32

        #
        # Rule 33:  option_value ::= $Empty
        #
         def Act33(): 
               ##line 82 "LPGParser.g"
                self.setResult(None)

         self.__rule_action[33]= Act33

        #
        # Rule 34:  option_value ::= =$ SYMBOL
        #
         def Act34(): 
               ##line 82 "LPGParser.g"
                self.setResult(
                    ##line 82 LPGParser.g
                    option_value0(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 82 LPGParser.g
                                  ASTNodeToken(self.getRhsIToken(2)))
                ##line 82 LPGParser.g
                )

         self.__rule_action[34]= Act34

        #
        # Rule 35:  option_value ::= =$ ($ symbol_list )$
        #
         def Act35(): 
               ##line 82 "LPGParser.g"
                self.setResult(
                    ##line 82 LPGParser.g
                    option_value1(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 82 LPGParser.g
                                  self.getRhsSym(3))
                ##line 82 LPGParser.g
                )

         self.__rule_action[35]= Act35

        #
        # Rule 36:  symbol_list ::= SYMBOL
        #
         def Act36(): 
               ##line 84 "LPGParser.g"
                self.setResult(
                    ##line 84 LPGParser.g
                    SYMBOLList.SYMBOLListfromElement(ASTNodeToken(self.getRhsIToken(1)), True )
                ##line 84 LPGParser.g
                )

         self.__rule_action[36]= Act36

        #
        # Rule 37:  symbol_list ::= symbol_list ,$ SYMBOL
        #
         def Act37(): 
               ##line 85 "LPGParser.g"
                (self.getRhsSym(1)).addElement(ASTNodeToken(self.getRhsIToken(3)))

         self.__rule_action[37]= Act37

        #
        # Rule 38:  alias_segment ::= aliasSpec
        #
         def Act38(): 
               ##line 88 "LPGParser.g"
                self.setResult(
                    ##line 88 LPGParser.g
                    aliasSpecList.aliasSpecListfromElement(self.getRhsSym(1), True )
                ##line 88 LPGParser.g
                )

         self.__rule_action[38]= Act38

        #
        # Rule 39:  alias_segment ::= alias_segment aliasSpec
        #
         def Act39(): 
               ##line 88 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[39]= Act39

        #
        # Rule 40:  aliasSpec ::= ERROR_KEY produces alias_rhs
        #
         def Act40(): 
               ##line 90 "LPGParser.g"
                self.setResult(
                    ##line 90 LPGParser.g
                    aliasSpec0(self.getLeftIToken(), self.getRightIToken(),
                               ##line 90 LPGParser.g
                               ASTNodeToken(self.getRhsIToken(1)),
                               ##line 90 LPGParser.g
                               self.getRhsSym(2),
                               ##line 90 LPGParser.g
                               self.getRhsSym(3))
                ##line 90 LPGParser.g
                )

         self.__rule_action[40]= Act40

        #
        # Rule 41:  aliasSpec ::= EOL_KEY produces alias_rhs
        #
         def Act41(): 
               ##line 91 "LPGParser.g"
                self.setResult(
                    ##line 91 LPGParser.g
                    aliasSpec1(self.getLeftIToken(), self.getRightIToken(),
                               ##line 91 LPGParser.g
                               ASTNodeToken(self.getRhsIToken(1)),
                               ##line 91 LPGParser.g
                               self.getRhsSym(2),
                               ##line 91 LPGParser.g
                               self.getRhsSym(3))
                ##line 91 LPGParser.g
                )

         self.__rule_action[41]= Act41

        #
        # Rule 42:  aliasSpec ::= EOF_KEY produces alias_rhs
        #
         def Act42(): 
               ##line 92 "LPGParser.g"
                self.setResult(
                    ##line 92 LPGParser.g
                    aliasSpec2(self.getLeftIToken(), self.getRightIToken(),
                               ##line 92 LPGParser.g
                               ASTNodeToken(self.getRhsIToken(1)),
                               ##line 92 LPGParser.g
                               self.getRhsSym(2),
                               ##line 92 LPGParser.g
                               self.getRhsSym(3))
                ##line 92 LPGParser.g
                )

         self.__rule_action[42]= Act42

        #
        # Rule 43:  aliasSpec ::= IDENTIFIER_KEY produces alias_rhs
        #
         def Act43(): 
               ##line 93 "LPGParser.g"
                self.setResult(
                    ##line 93 LPGParser.g
                    aliasSpec3(self.getLeftIToken(), self.getRightIToken(),
                               ##line 93 LPGParser.g
                               ASTNodeToken(self.getRhsIToken(1)),
                               ##line 93 LPGParser.g
                               self.getRhsSym(2),
                               ##line 93 LPGParser.g
                               self.getRhsSym(3))
                ##line 93 LPGParser.g
                )

         self.__rule_action[43]= Act43

        #
        # Rule 44:  aliasSpec ::= SYMBOL produces alias_rhs
        #
         def Act44(): 
               ##line 94 "LPGParser.g"
                self.setResult(
                    ##line 94 LPGParser.g
                    aliasSpec4(self.getLeftIToken(), self.getRightIToken(),
                               ##line 94 LPGParser.g
                               ASTNodeToken(self.getRhsIToken(1)),
                               ##line 94 LPGParser.g
                               self.getRhsSym(2),
                               ##line 94 LPGParser.g
                               self.getRhsSym(3))
                ##line 94 LPGParser.g
                )

         self.__rule_action[44]= Act44

        #
        # Rule 45:  aliasSpec ::= alias_lhs_macro_name produces alias_rhs
        #
         def Act45(): 
               ##line 95 "LPGParser.g"
                self.setResult(
                    ##line 95 LPGParser.g
                    aliasSpec5(self.getLeftIToken(), self.getRightIToken(),
                               ##line 95 LPGParser.g
                               self.getRhsSym(1),
                               ##line 95 LPGParser.g
                               self.getRhsSym(2),
                               ##line 95 LPGParser.g
                               self.getRhsSym(3))
                ##line 95 LPGParser.g
                )

         self.__rule_action[45]= Act45

        #
        # Rule 46:  alias_lhs_macro_name ::= MACRO_NAME
        #
         def Act46(): 
               ##line 97 "LPGParser.g"
                self.setResult(
                    ##line 97 LPGParser.g
                    alias_lhs_macro_name(self.getRhsIToken(1))
                ##line 97 LPGParser.g
                )

         self.__rule_action[46]= Act46

        #
        # Rule 47:  alias_rhs ::= SYMBOL
        #
         def Act47(): 
               ##line 99 "LPGParser.g"
                self.setResult(
                    ##line 99 LPGParser.g
                    alias_rhs0(self.getRhsIToken(1))
                ##line 99 LPGParser.g
                )

         self.__rule_action[47]= Act47

        #
        # Rule 48:  alias_rhs ::= MACRO_NAME
        #
         def Act48(): 
               ##line 100 "LPGParser.g"
                self.setResult(
                    ##line 100 LPGParser.g
                    alias_rhs1(self.getRhsIToken(1))
                ##line 100 LPGParser.g
                )

         self.__rule_action[48]= Act48

        #
        # Rule 49:  alias_rhs ::= ERROR_KEY
        #
         def Act49(): 
               ##line 101 "LPGParser.g"
                self.setResult(
                    ##line 101 LPGParser.g
                    alias_rhs2(self.getRhsIToken(1))
                ##line 101 LPGParser.g
                )

         self.__rule_action[49]= Act49

        #
        # Rule 50:  alias_rhs ::= EOL_KEY
        #
         def Act50(): 
               ##line 102 "LPGParser.g"
                self.setResult(
                    ##line 102 LPGParser.g
                    alias_rhs3(self.getRhsIToken(1))
                ##line 102 LPGParser.g
                )

         self.__rule_action[50]= Act50

        #
        # Rule 51:  alias_rhs ::= EOF_KEY
        #
         def Act51(): 
               ##line 103 "LPGParser.g"
                self.setResult(
                    ##line 103 LPGParser.g
                    alias_rhs4(self.getRhsIToken(1))
                ##line 103 LPGParser.g
                )

         self.__rule_action[51]= Act51

        #
        # Rule 52:  alias_rhs ::= EMPTY_KEY
        #
         def Act52(): 
               ##line 104 "LPGParser.g"
                self.setResult(
                    ##line 104 LPGParser.g
                    alias_rhs5(self.getRhsIToken(1))
                ##line 104 LPGParser.g
                )

         self.__rule_action[52]= Act52

        #
        # Rule 53:  alias_rhs ::= IDENTIFIER_KEY
        #
         def Act53(): 
               ##line 105 "LPGParser.g"
                self.setResult(
                    ##line 105 LPGParser.g
                    alias_rhs6(self.getRhsIToken(1))
                ##line 105 LPGParser.g
                )

         self.__rule_action[53]= Act53

        #
        # Rule 54:  ast_segment ::= action_segment_list
        #
        
                 
        #
        # Rule 55:  define_segment ::= defineSpec
        #
         def Act55(): 
               ##line 111 "LPGParser.g"
                self.setResult(
                    ##line 111 LPGParser.g
                    defineSpecList.defineSpecListfromElement(self.getRhsSym(1), True )
                ##line 111 LPGParser.g
                )

         self.__rule_action[55]= Act55

        #
        # Rule 56:  define_segment ::= define_segment defineSpec
        #
         def Act56(): 
               ##line 111 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[56]= Act56

        #
        # Rule 57:  defineSpec ::= macro_name_symbol macro_segment
        #
         def Act57(): 
               ##line 112 "LPGParser.g"
                self.setResult(
                    ##line 112 LPGParser.g
                    defineSpec(self.getLeftIToken(), self.getRightIToken(),
                               ##line 112 LPGParser.g
                               self.getRhsSym(1),
                               ##line 112 LPGParser.g
                               self.getRhsSym(2))
                ##line 112 LPGParser.g
                )

         self.__rule_action[57]= Act57

        #
        # Rule 58:  macro_name_symbol ::= MACRO_NAME
        #
         def Act58(): 
               ##line 115 "LPGParser.g"
                self.setResult(
                    ##line 115 LPGParser.g
                    macro_name_symbol0(self.getRhsIToken(1))
                ##line 115 LPGParser.g
                )

         self.__rule_action[58]= Act58

        #
        # Rule 59:  macro_name_symbol ::= SYMBOL
        #
         def Act59(): 
               ##line 116 "LPGParser.g"
                self.setResult(
                    ##line 116 LPGParser.g
                    macro_name_symbol1(self.getRhsIToken(1))
                ##line 116 LPGParser.g
                )

         self.__rule_action[59]= Act59

        #
        # Rule 60:  macro_segment ::= BLOCK
        #
         def Act60(): 
               ##line 117 "LPGParser.g"
                self.setResult(
                    ##line 117 LPGParser.g
                    macro_segment(self.getRhsIToken(1))
                ##line 117 LPGParser.g
                )

         self.__rule_action[60]= Act60

        #
        # Rule 61:  eol_segment ::= terminal_symbol
        #
        
                 
        #
        # Rule 62:  eof_segment ::= terminal_symbol
        #
        
                 
        #
        # Rule 63:  error_segment ::= terminal_symbol
        #
        
                 
        #
        # Rule 64:  export_segment ::= terminal_symbol
        #
         def Act64(): 
               ##line 127 "LPGParser.g"
                self.setResult(
                    ##line 127 LPGParser.g
                    terminal_symbolList.terminal_symbolListfromElement(self.getRhsSym(1), True )
                ##line 127 LPGParser.g
                )

         self.__rule_action[64]= Act64

        #
        # Rule 65:  export_segment ::= export_segment terminal_symbol
        #
         def Act65(): 
               ##line 127 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[65]= Act65

        #
        # Rule 66:  globals_segment ::= action_segment
        #
         def Act66(): 
               ##line 130 "LPGParser.g"
                self.setResult(
                    ##line 130 LPGParser.g
                    action_segmentList.action_segmentListfromElement(self.getRhsSym(1), True )
                ##line 130 LPGParser.g
                )

         self.__rule_action[66]= Act66

        #
        # Rule 67:  globals_segment ::= globals_segment action_segment
        #
         def Act67(): 
               ##line 130 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[67]= Act67

        #
        # Rule 68:  headers_segment ::= action_segment_list
        #
        
                 
        #
        # Rule 69:  identifier_segment ::= terminal_symbol
        #
        
                 
        #
        # Rule 70:  import_segment ::= SYMBOL drop_command_list
        #
         def Act70(): 
               ##line 139 "LPGParser.g"
                self.setResult(
                    ##line 139 LPGParser.g
                    import_segment(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 139 LPGParser.g
                                   ASTNodeToken(self.getRhsIToken(1)),
                                   ##line 139 LPGParser.g
                                   self.getRhsSym(2))
                ##line 139 LPGParser.g
                )

         self.__rule_action[70]= Act70

        #
        # Rule 71:  drop_command_list ::= $Empty
        #
         def Act71(): 
               ##line 141 "LPGParser.g"
                self.setResult(
                    ##line 141 LPGParser.g
                    drop_commandList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 141 LPGParser.g
                )

         self.__rule_action[71]= Act71

        #
        # Rule 72:  drop_command_list ::= drop_command_list drop_command
        #
         def Act72(): 
               ##line 141 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[72]= Act72

        #
        # Rule 73:  drop_command ::= DROPSYMBOLS_KEY drop_symbols
        #
         def Act73(): 
               ##line 143 "LPGParser.g"
                self.setResult(
                    ##line 143 LPGParser.g
                    drop_command0(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 143 LPGParser.g
                                  ASTNodeToken(self.getRhsIToken(1)),
                                  ##line 143 LPGParser.g
                                  self.getRhsSym(2))
                ##line 143 LPGParser.g
                )

         self.__rule_action[73]= Act73

        #
        # Rule 74:  drop_command ::= DROPRULES_KEY drop_rules
        #
         def Act74(): 
               ##line 144 "LPGParser.g"
                self.setResult(
                    ##line 144 LPGParser.g
                    drop_command1(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 144 LPGParser.g
                                  ASTNodeToken(self.getRhsIToken(1)),
                                  ##line 144 LPGParser.g
                                  self.getRhsSym(2))
                ##line 144 LPGParser.g
                )

         self.__rule_action[74]= Act74

        #
        # Rule 75:  drop_symbols ::= SYMBOL
        #
         def Act75(): 
               ##line 146 "LPGParser.g"
                self.setResult(
                    ##line 146 LPGParser.g
                    SYMBOLList.SYMBOLListfromElement(ASTNodeToken(self.getRhsIToken(1)), True )
                ##line 146 LPGParser.g
                )

         self.__rule_action[75]= Act75

        #
        # Rule 76:  drop_symbols ::= drop_symbols SYMBOL
        #
         def Act76(): 
               ##line 147 "LPGParser.g"
                (self.getRhsSym(1)).addElement(ASTNodeToken(self.getRhsIToken(2)))

         self.__rule_action[76]= Act76

        #
        # Rule 77:  drop_rules ::= drop_rule
        #
         def Act77(): 
               ##line 148 "LPGParser.g"
                self.setResult(
                    ##line 148 LPGParser.g
                    drop_ruleList.drop_ruleListfromElement(self.getRhsSym(1), True )
                ##line 148 LPGParser.g
                )

         self.__rule_action[77]= Act77

        #
        # Rule 78:  drop_rules ::= drop_rules drop_rule
        #
         def Act78(): 
               ##line 149 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[78]= Act78

        #
        # Rule 79:  drop_rule ::= SYMBOL optMacroName produces ruleList
        #
         def Act79(): 
               ##line 151 "LPGParser.g"
                self.setResult(
                    ##line 151 LPGParser.g
                    drop_rule(self.getLeftIToken(), self.getRightIToken(),
                              ##line 151 LPGParser.g
                              ASTNodeToken(self.getRhsIToken(1)),
                              ##line 151 LPGParser.g
                              self.getRhsSym(2),
                              ##line 151 LPGParser.g
                              self.getRhsSym(3),
                              ##line 151 LPGParser.g
                              self.getRhsSym(4))
                ##line 151 LPGParser.g
                )

         self.__rule_action[79]= Act79

        #
        # Rule 80:  optMacroName ::= $Empty
        #
         def Act80(): 
               ##line 153 "LPGParser.g"
                self.setResult(None)

         self.__rule_action[80]= Act80

        #
        # Rule 81:  optMacroName ::= MACRO_NAME
        #
         def Act81(): 
               ##line 153 "LPGParser.g"
                self.setResult(
                    ##line 153 LPGParser.g
                    optMacroName(self.getRhsIToken(1))
                ##line 153 LPGParser.g
                )

         self.__rule_action[81]= Act81

        #
        # Rule 82:  include_segment ::= SYMBOL
        #
         def Act82(): 
               ##line 156 "LPGParser.g"
                self.setResult(
                    ##line 156 LPGParser.g
                    include_segment(self.getRhsIToken(1))
                ##line 156 LPGParser.g
                )

         self.__rule_action[82]= Act82

        #
        # Rule 83:  keywords_segment ::= keywordSpec
        #
         def Act83(): 
               ##line 159 "LPGParser.g"
                self.setResult(
                    ##line 159 LPGParser.g
                    keywordSpecList.keywordSpecListfromElement(self.getRhsSym(1), True )
                ##line 159 LPGParser.g
                )

         self.__rule_action[83]= Act83

        #
        # Rule 84:  keywords_segment ::= keywords_segment keywordSpec
        #
         def Act84(): 
               ##line 159 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[84]= Act84

        #
        # Rule 85:  keywordSpec ::= terminal_symbol
        #
        
                 
        #
        # Rule 86:  keywordSpec ::= terminal_symbol produces name
        #
         def Act86(): 
               ##line 161 "LPGParser.g"
                self.setResult(
                    ##line 161 LPGParser.g
                    keywordSpec(self.getLeftIToken(), self.getRightIToken(),
                                ##line 161 LPGParser.g
                                self.getRhsSym(1),
                                ##line 161 LPGParser.g
                                self.getRhsSym(2),
                                ##line 161 LPGParser.g
                                self.getRhsSym(3))
                ##line 161 LPGParser.g
                )

         self.__rule_action[86]= Act86

        #
        # Rule 87:  names_segment ::= nameSpec
        #
         def Act87(): 
               ##line 164 "LPGParser.g"
                self.setResult(
                    ##line 164 LPGParser.g
                    nameSpecList.nameSpecListfromElement(self.getRhsSym(1), True )
                ##line 164 LPGParser.g
                )

         self.__rule_action[87]= Act87

        #
        # Rule 88:  names_segment ::= names_segment nameSpec
        #
         def Act88(): 
               ##line 164 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[88]= Act88

        #
        # Rule 89:  nameSpec ::= name produces name
        #
         def Act89(): 
               ##line 165 "LPGParser.g"
                self.setResult(
                    ##line 165 LPGParser.g
                    nameSpec(self.getLeftIToken(), self.getRightIToken(),
                             ##line 165 LPGParser.g
                             self.getRhsSym(1),
                             ##line 165 LPGParser.g
                             self.getRhsSym(2),
                             ##line 165 LPGParser.g
                             self.getRhsSym(3))
                ##line 165 LPGParser.g
                )

         self.__rule_action[89]= Act89

        #
        # Rule 90:  name ::= SYMBOL
        #
         def Act90(): 
               ##line 167 "LPGParser.g"
                self.setResult(
                    ##line 167 LPGParser.g
                    name0(self.getRhsIToken(1))
                ##line 167 LPGParser.g
                )

         self.__rule_action[90]= Act90

        #
        # Rule 91:  name ::= MACRO_NAME
        #
         def Act91(): 
               ##line 168 "LPGParser.g"
                self.setResult(
                    ##line 168 LPGParser.g
                    name1(self.getRhsIToken(1))
                ##line 168 LPGParser.g
                )

         self.__rule_action[91]= Act91

        #
        # Rule 92:  name ::= EMPTY_KEY
        #
         def Act92(): 
               ##line 169 "LPGParser.g"
                self.setResult(
                    ##line 169 LPGParser.g
                    name2(self.getRhsIToken(1))
                ##line 169 LPGParser.g
                )

         self.__rule_action[92]= Act92

        #
        # Rule 93:  name ::= ERROR_KEY
        #
         def Act93(): 
               ##line 170 "LPGParser.g"
                self.setResult(
                    ##line 170 LPGParser.g
                    name3(self.getRhsIToken(1))
                ##line 170 LPGParser.g
                )

         self.__rule_action[93]= Act93

        #
        # Rule 94:  name ::= EOL_KEY
        #
         def Act94(): 
               ##line 171 "LPGParser.g"
                self.setResult(
                    ##line 171 LPGParser.g
                    name4(self.getRhsIToken(1))
                ##line 171 LPGParser.g
                )

         self.__rule_action[94]= Act94

        #
        # Rule 95:  name ::= IDENTIFIER_KEY
        #
         def Act95(): 
               ##line 172 "LPGParser.g"
                self.setResult(
                    ##line 172 LPGParser.g
                    name5(self.getRhsIToken(1))
                ##line 172 LPGParser.g
                )

         self.__rule_action[95]= Act95

        #
        # Rule 96:  notice_segment ::= action_segment
        #
         def Act96(): 
               ##line 175 "LPGParser.g"
                self.setResult(
                    ##line 175 LPGParser.g
                    action_segmentList.action_segmentListfromElement(self.getRhsSym(1), True )
                ##line 175 LPGParser.g
                )

         self.__rule_action[96]= Act96

        #
        # Rule 97:  notice_segment ::= notice_segment action_segment
        #
         def Act97(): 
               ##line 175 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[97]= Act97

        #
        # Rule 98:  rules_segment ::= action_segment_list nonTermList
        #
         def Act98(): 
               ##line 178 "LPGParser.g"
                self.setResult(
                    ##line 178 LPGParser.g
                    rules_segment(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 178 LPGParser.g
                                  self.getRhsSym(1),
                                  ##line 178 LPGParser.g
                                  self.getRhsSym(2))
                ##line 178 LPGParser.g
                )

         self.__rule_action[98]= Act98

        #
        # Rule 99:  nonTermList ::= $Empty
        #
         def Act99(): 
               ##line 180 "LPGParser.g"
                self.setResult(
                    ##line 180 LPGParser.g
                    nonTermList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 180 LPGParser.g
                )

         self.__rule_action[99]= Act99

        #
        # Rule 100:  nonTermList ::= nonTermList nonTerm
        #
         def Act100(): 
               ##line 180 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[100]= Act100

        #
        # Rule 101:  nonTerm ::= ruleNameWithAttributes produces ruleList
        #
         def Act101(): 
               ##line 182 "LPGParser.g"
                self.setResult(
                    ##line 182 LPGParser.g
                    nonTerm(self.getLeftIToken(), self.getRightIToken(),
                            ##line 182 LPGParser.g
                            self.getRhsSym(1),
                            ##line 182 LPGParser.g
                            self.getRhsSym(2),
                            ##line 182 LPGParser.g
                            self.getRhsSym(3))
                ##line 182 LPGParser.g
                )

         self.__rule_action[101]= Act101

        #
        # Rule 102:  ruleNameWithAttributes ::= SYMBOL
        #
         def Act102(): 
               ##line 185 "LPGParser.g"
                self.setResult(
                    ##line 185 LPGParser.g
                    RuleName(self.getLeftIToken(), self.getRightIToken(),
                             ##line 185 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(1)),
                             ##line 185 LPGParser.g
                             None,
                             ##line 185 LPGParser.g
                             None)
                ##line 185 LPGParser.g
                )

         self.__rule_action[102]= Act102

        #
        # Rule 103:  ruleNameWithAttributes ::= SYMBOL MACRO_NAME$className
        #
         def Act103(): 
               ##line 186 "LPGParser.g"
                self.setResult(
                    ##line 186 LPGParser.g
                    RuleName(self.getLeftIToken(), self.getRightIToken(),
                             ##line 186 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(1)),
                             ##line 186 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(2)),
                             ##line 186 LPGParser.g
                             None)
                ##line 186 LPGParser.g
                )

         self.__rule_action[103]= Act103

        #
        # Rule 104:  ruleNameWithAttributes ::= SYMBOL MACRO_NAME$className MACRO_NAME$arrayElement
        #
         def Act104(): 
               ##line 187 "LPGParser.g"
                self.setResult(
                    ##line 187 LPGParser.g
                    RuleName(self.getLeftIToken(), self.getRightIToken(),
                             ##line 187 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(1)),
                             ##line 187 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(2)),
                             ##line 187 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(3)))
                ##line 187 LPGParser.g
                )

         self.__rule_action[104]= Act104

        #
        # Rule 105:  ruleList ::= rule
        #
         def Act105(): 
               ##line 201 "LPGParser.g"
                self.setResult(
                    ##line 201 LPGParser.g
                    ruleList.ruleListfromElement(self.getRhsSym(1), True )
                ##line 201 LPGParser.g
                )

         self.__rule_action[105]= Act105

        #
        # Rule 106:  ruleList ::= ruleList |$ rule
        #
         def Act106(): 
               ##line 201 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(3))

         self.__rule_action[106]= Act106

        #
        # Rule 107:  produces ::= ::=
        #
         def Act107(): 
               ##line 203 "LPGParser.g"
                self.setResult(
                    ##line 203 LPGParser.g
                    produces0(self.getRhsIToken(1))
                ##line 203 LPGParser.g
                )

         self.__rule_action[107]= Act107

        #
        # Rule 108:  produces ::= ::=?
        #
         def Act108(): 
               ##line 204 "LPGParser.g"
                self.setResult(
                    ##line 204 LPGParser.g
                    produces1(self.getRhsIToken(1))
                ##line 204 LPGParser.g
                )

         self.__rule_action[108]= Act108

        #
        # Rule 109:  produces ::= ->
        #
         def Act109(): 
               ##line 205 "LPGParser.g"
                self.setResult(
                    ##line 205 LPGParser.g
                    produces2(self.getRhsIToken(1))
                ##line 205 LPGParser.g
                )

         self.__rule_action[109]= Act109

        #
        # Rule 110:  produces ::= ->?
        #
         def Act110(): 
               ##line 206 "LPGParser.g"
                self.setResult(
                    ##line 206 LPGParser.g
                    produces3(self.getRhsIToken(1))
                ##line 206 LPGParser.g
                )

         self.__rule_action[110]= Act110

        #
        # Rule 111:  rule ::= symWithAttrsList opt_action_segment
        #
         def Act111(): 
               ##line 208 "LPGParser.g"
                self.setResult(
                    ##line 208 LPGParser.g
                    rule(self.getLeftIToken(), self.getRightIToken(),
                         ##line 208 LPGParser.g
                         self.getRhsSym(1),
                         ##line 208 LPGParser.g
                         self.getRhsSym(2))
                ##line 208 LPGParser.g
                )

         self.__rule_action[111]= Act111

        #
        # Rule 112:  symWithAttrsList ::= $Empty
        #
         def Act112(): 
               ##line 210 "LPGParser.g"
                self.setResult(
                    ##line 210 LPGParser.g
                    symWithAttrsList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 210 LPGParser.g
                )

         self.__rule_action[112]= Act112

        #
        # Rule 113:  symWithAttrsList ::= symWithAttrsList symWithAttrs
        #
         def Act113(): 
               ##line 210 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[113]= Act113

        #
        # Rule 114:  symWithAttrs ::= EMPTY_KEY
        #
         def Act114(): 
               ##line 212 "LPGParser.g"
                self.setResult(
                    ##line 212 LPGParser.g
                    symWithAttrs0(self.getRhsIToken(1))
                ##line 212 LPGParser.g
                )

         self.__rule_action[114]= Act114

        #
        # Rule 115:  symWithAttrs ::= SYMBOL optAttrList
        #
         def Act115(): 
               ##line 213 "LPGParser.g"
                self.setResult(
                    ##line 213 LPGParser.g
                    symWithAttrs1(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 213 LPGParser.g
                                  ASTNodeToken(self.getRhsIToken(1)),
                                  ##line 213 LPGParser.g
                                  self.getRhsSym(2))
                ##line 213 LPGParser.g
                )

         self.__rule_action[115]= Act115

        #
        # Rule 116:  optAttrList ::= $Empty
        #
         def Act116(): 
               ##line 216 "LPGParser.g"
                self.setResult(
                    ##line 216 LPGParser.g
                    symAttrs(self.getLeftIToken(), self.getRightIToken(),
                             ##line 216 LPGParser.g
                             None)
                ##line 216 LPGParser.g
                )

         self.__rule_action[116]= Act116

        #
        # Rule 117:  optAttrList ::= MACRO_NAME
        #
         def Act117(): 
               ##line 217 "LPGParser.g"
                self.setResult(
                    ##line 217 LPGParser.g
                    symAttrs(self.getLeftIToken(), self.getRightIToken(),
                             ##line 217 LPGParser.g
                             ASTNodeToken(self.getRhsIToken(1)))
                ##line 217 LPGParser.g
                )

         self.__rule_action[117]= Act117

        #
        # Rule 118:  opt_action_segment ::= $Empty
        #
         def Act118(): 
               ##line 219 "LPGParser.g"
                self.setResult(None)

         self.__rule_action[118]= Act118

        #
        # Rule 119:  opt_action_segment ::= action_segment
        #
        
                 
        #
        # Rule 120:  action_segment ::= BLOCK
        #
         def Act120(): 
               ##line 221 "LPGParser.g"
                self.setResult(
                    ##line 221 LPGParser.g
                    action_segment(self, self.getRhsIToken(1))
                ##line 221 LPGParser.g
                )

         self.__rule_action[120]= Act120

        #
        # Rule 121:  start_segment ::= start_symbol
        #
         def Act121(): 
               ##line 226 "LPGParser.g"
                self.setResult(
                    ##line 226 LPGParser.g
                    start_symbolList.start_symbolListfromElement(self.getRhsSym(1), True )
                ##line 226 LPGParser.g
                )

         self.__rule_action[121]= Act121

        #
        # Rule 122:  start_segment ::= start_segment start_symbol
        #
         def Act122(): 
               ##line 226 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[122]= Act122

        #
        # Rule 123:  start_symbol ::= SYMBOL
        #
         def Act123(): 
               ##line 227 "LPGParser.g"
                self.setResult(
                    ##line 227 LPGParser.g
                    start_symbol0(self.getRhsIToken(1))
                ##line 227 LPGParser.g
                )

         self.__rule_action[123]= Act123

        #
        # Rule 124:  start_symbol ::= MACRO_NAME
        #
         def Act124(): 
               ##line 228 "LPGParser.g"
                self.setResult(
                    ##line 228 LPGParser.g
                    start_symbol1(self.getRhsIToken(1))
                ##line 228 LPGParser.g
                )

         self.__rule_action[124]= Act124

        #
        # Rule 125:  terminals_segment ::= terminal
        #
         def Act125(): 
               ##line 231 "LPGParser.g"
                self.setResult(
                    ##line 231 LPGParser.g
                    terminalList.terminalListfromElement(self.getRhsSym(1), True )
                ##line 231 LPGParser.g
                )

         self.__rule_action[125]= Act125

        #
        # Rule 126:  terminals_segment ::= terminals_segment terminal
        #
         def Act126(): 
               ##line 231 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[126]= Act126

        #
        # Rule 127:  terminal ::= terminal_symbol optTerminalAlias
        #
         def Act127(): 
               ##line 234 "LPGParser.g"
                self.setResult(
                    ##line 234 LPGParser.g
                    terminal(self.getLeftIToken(), self.getRightIToken(),
                             ##line 234 LPGParser.g
                             self.getRhsSym(1),
                             ##line 234 LPGParser.g
                             self.getRhsSym(2))
                ##line 234 LPGParser.g
                )

         self.__rule_action[127]= Act127

        #
        # Rule 128:  optTerminalAlias ::= $Empty
        #
         def Act128(): 
               ##line 236 "LPGParser.g"
                self.setResult(None)

         self.__rule_action[128]= Act128

        #
        # Rule 129:  optTerminalAlias ::= produces name
        #
         def Act129(): 
               ##line 236 "LPGParser.g"
                self.setResult(
                    ##line 236 LPGParser.g
                    optTerminalAlias(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 236 LPGParser.g
                                     self.getRhsSym(1),
                                     ##line 236 LPGParser.g
                                     self.getRhsSym(2))
                ##line 236 LPGParser.g
                )

         self.__rule_action[129]= Act129

        #
        # Rule 130:  terminal_symbol ::= SYMBOL
        #
         def Act130(): 
               ##line 238 "LPGParser.g"
                self.setResult(
                    ##line 238 LPGParser.g
                    terminal_symbol0(self.getRhsIToken(1))
                ##line 238 LPGParser.g
                )

         self.__rule_action[130]= Act130

        #
        # Rule 131:  terminal_symbol ::= MACRO_NAME
        #
         def Act131(): 
               ##line 240 "LPGParser.g"
                self.setResult(
                    ##line 240 LPGParser.g
                    terminal_symbol1(self.getRhsIToken(1))
                ##line 240 LPGParser.g
                )

         self.__rule_action[131]= Act131

        #
        # Rule 132:  trailers_segment ::= action_segment_list
        #
        
                 
        #
        # Rule 133:  types_segment ::= type_declarations
        #
         def Act133(): 
               ##line 246 "LPGParser.g"
                self.setResult(
                    ##line 246 LPGParser.g
                    type_declarationsList.type_declarationsListfromElement(self.getRhsSym(1), True )
                ##line 246 LPGParser.g
                )

         self.__rule_action[133]= Act133

        #
        # Rule 134:  types_segment ::= types_segment type_declarations
        #
         def Act134(): 
               ##line 246 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[134]= Act134

        #
        # Rule 135:  type_declarations ::= SYMBOL produces barSymbolList opt_action_segment
        #
         def Act135(): 
               ##line 248 "LPGParser.g"
                self.setResult(
                    ##line 248 LPGParser.g
                    type_declarations(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 248 LPGParser.g
                                      ASTNodeToken(self.getRhsIToken(1)),
                                      ##line 248 LPGParser.g
                                      self.getRhsSym(2),
                                      ##line 248 LPGParser.g
                                      self.getRhsSym(3),
                                      ##line 248 LPGParser.g
                                      self.getRhsSym(4))
                ##line 248 LPGParser.g
                )

         self.__rule_action[135]= Act135

        #
        # Rule 136:  barSymbolList ::= SYMBOL
        #
         def Act136(): 
               ##line 249 "LPGParser.g"
                self.setResult(
                    ##line 249 LPGParser.g
                    SYMBOLList.SYMBOLListfromElement(ASTNodeToken(self.getRhsIToken(1)), True )
                ##line 249 LPGParser.g
                )

         self.__rule_action[136]= Act136

        #
        # Rule 137:  barSymbolList ::= barSymbolList |$ SYMBOL
        #
         def Act137(): 
               ##line 249 "LPGParser.g"
                (self.getRhsSym(1)).addElement(ASTNodeToken(self.getRhsIToken(3)))

         self.__rule_action[137]= Act137

        #
        # Rule 138:  predecessor_segment ::= $Empty
        #
         def Act138(): 
               ##line 252 "LPGParser.g"
                self.setResult(
                    ##line 252 LPGParser.g
                    symbol_pairList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 252 LPGParser.g
                )

         self.__rule_action[138]= Act138

        #
        # Rule 139:  predecessor_segment ::= predecessor_segment symbol_pair
        #
         def Act139(): 
               ##line 252 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[139]= Act139

        #
        # Rule 140:  symbol_pair ::= SYMBOL SYMBOL
        #
         def Act140(): 
               ##line 254 "LPGParser.g"
                self.setResult(
                    ##line 254 LPGParser.g
                    symbol_pair(self.getLeftIToken(), self.getRightIToken(),
                                ##line 254 LPGParser.g
                                ASTNodeToken(self.getRhsIToken(1)),
                                ##line 254 LPGParser.g
                                ASTNodeToken(self.getRhsIToken(2)))
                ##line 254 LPGParser.g
                )

         self.__rule_action[140]= Act140

        #
        # Rule 141:  recover_segment ::= $Empty
        #
         def Act141(): 
               ##line 257 "LPGParser.g"
                self.setResult(
                    ##line 257 LPGParser.g
                    SYMBOLList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 257 LPGParser.g
                )

         self.__rule_action[141]= Act141

        #
        # Rule 142:  recover_segment ::= recover_segment recover_symbol
        #
         def Act142(): 
               ##line 257 "LPGParser.g"
                self.setResult(self.getRhsSym(1))

         self.__rule_action[142]= Act142

        #
        # Rule 143:  recover_symbol ::= SYMBOL
        #
         def Act143(): 
               ##line 259 "LPGParser.g"
                self.setResult(
                    ##line 259 LPGParser.g
                    recover_symbol(self.getRhsIToken(1))
                ##line 259 LPGParser.g
                )

         self.__rule_action[143]= Act143

        #
        # Rule 144:  END_KEY_OPT ::= $Empty
        #
         def Act144(): 
               ##line 262 "LPGParser.g"
                self.setResult(None)

         self.__rule_action[144]= Act144

        #
        # Rule 145:  END_KEY_OPT ::= END_KEY
        #
         def Act145(): 
               ##line 263 "LPGParser.g"
                self.setResult(
                    ##line 263 LPGParser.g
                    END_KEY_OPT(self.getRhsIToken(1))
                ##line 263 LPGParser.g
                )

         self.__rule_action[145]= Act145

        #
        # Rule 146:  action_segment_list ::= $Empty
        #
         def Act146(): 
               ##line 265 "LPGParser.g"
                self.setResult(
                    ##line 265 LPGParser.g
                    action_segmentList(self.getLeftIToken(), self.getRightIToken(), True )
                ##line 265 LPGParser.g
                )

         self.__rule_action[146]= Act146

        #
        # Rule 147:  action_segment_list ::= action_segment_list action_segment
        #
         def Act147(): 
               ##line 266 "LPGParser.g"
                (self.getRhsSym(1)).addElement(self.getRhsSym(2))

         self.__rule_action[147]= Act147

    ##line 277 "dtParserTemplateF.gi

    

class IRootForLPGParser(object):
    
        __slots__ = ()
        def  getLeftIToken(self)  : raise TypeError('Can not instantiate abstract class  with abstract methods')
        def  getRightIToken(self)  : raise TypeError('Can not instantiate abstract class  with abstract methods')

        def  accept(self, v):pass
    

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>alias_lhs_macro_name
 *<li>macro_segment
 *<li>optMacroName
 *<li>include_segment
 *<li>RuleName
 *<li>symAttrs
 *<li>action_segment
 *<li>recover_symbol
 *<li>END_KEY_OPT
 *<li>alias_rhs0
 *<li>alias_rhs1
 *<li>alias_rhs2
 *<li>alias_rhs3
 *<li>alias_rhs4
 *<li>alias_rhs5
 *<li>alias_rhs6
 *<li>macro_name_symbol0
 *<li>macro_name_symbol1
 *<li>name0
 *<li>name1
 *<li>name2
 *<li>name3
 *<li>name4
 *<li>name5
 *<li>produces0
 *<li>produces1
 *<li>produces2
 *<li>produces3
 *<li>symWithAttrs0
 *<li>symWithAttrs1
 *<li>start_symbol0
 *<li>start_symbol1
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class IASTNodeToken(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LPG</b>
 */'''
class ILPG(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>option_specList</b>
 */'''
class Ioptions_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LPG_itemList</b>
 */'''
class ILPG_INPUT(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AliasSeg
 *<li>AstSeg
 *<li>DefineSeg
 *<li>EofSeg
 *<li>EolSeg
 *<li>ErrorSeg
 *<li>ExportSeg
 *<li>GlobalsSeg
 *<li>HeadersSeg
 *<li>IdentifierSeg
 *<li>ImportSeg
 *<li>IncludeSeg
 *<li>KeywordsSeg
 *<li>NamesSeg
 *<li>NoticeSeg
 *<li>RulesSeg
 *<li>SoftKeywordsSeg
 *<li>StartSeg
 *<li>TerminalsSeg
 *<li>TrailersSeg
 *<li>TypesSeg
 *<li>RecoverSeg
 *<li>PredecessorSeg
 *</ul>
 *</b>
 */'''
class ILPG_item(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>aliasSpecList</b>
 */'''
class Ialias_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>action_segmentList</b>
 */'''
class Iast_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>defineSpecList</b>
 */'''
class Idefine_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class Ieof_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class Ieol_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class Ierror_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>terminal_symbolList</b>
 */'''
class Iexport_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>action_segmentList</b>
 */'''
class Iglobals_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>action_segmentList</b>
 */'''
class Iheaders_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class Iidentifier_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>import_segment</b>
 */'''
class Iimport_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>keywordSpecList</b>
 */'''
class Ikeywords_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>nameSpecList</b>
 */'''
class Inames_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>action_segmentList</b>
 */'''
class Inotice_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>rules_segment</b>
 */'''
class Irules_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>start_symbolList</b>
 */'''
class Istart_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>terminalList</b>
 */'''
class Iterminals_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>action_segmentList</b>
 */'''
class Itrailers_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>type_declarationsList</b>
 */'''
class Itypes_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SYMBOLList</b>
 */'''
class Irecover_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>symbol_pairList</b>
 */'''
class Ipredecessor_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>option_spec</b>
 */'''
class Ioption_spec(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>optionList</b>
 */'''
class Ioption_list(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>option</b>
 */'''
class Ioption(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>option_value0
 *<li>option_value1
 *</ul>
 *</b>
 */'''
class Ioption_value(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SYMBOLList</b>
 */'''
class Isymbol_list(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>aliasSpec0
 *<li>aliasSpec1
 *<li>aliasSpec2
 *<li>aliasSpec3
 *<li>aliasSpec4
 *<li>aliasSpec5
 *</ul>
 *</b>
 */'''
class IaliasSpec(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>defineSpec</b>
 */'''
class IdefineSpec(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>drop_commandList</b>
 */'''
class Idrop_command_list(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>drop_command0
 *<li>drop_command1
 *</ul>
 *</b>
 */'''
class Idrop_command(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SYMBOLList</b>
 */'''
class Idrop_symbols(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>drop_ruleList</b>
 */'''
class Idrop_rules(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>drop_rule</b>
 */'''
class Idrop_rule(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ruleList</b>
 */'''
class IruleList(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>keywordSpec
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class IkeywordSpec(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>nameSpec</b>
 */'''
class InameSpec(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>nonTermList</b>
 */'''
class InonTermList(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>nonTerm</b>
 */'''
class InonTerm(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>rule</b>
 */'''
class Irule(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>symWithAttrsList</b>
 */'''
class IsymWithAttrsList(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>action_segment</b>
 */'''
class Iopt_action_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>terminal</b>
 */'''
class Iterminal(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>optTerminalAlias</b>
 */'''
class IoptTerminalAlias(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>type_declarations</b>
 */'''
class Itype_declarations(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SYMBOLList</b>
 */'''
class IbarSymbolList(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>symbol_pair</b>
 */'''
class Isymbol_pair(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>END_KEY_OPT</b>
 */'''
class IEND_KEY_OPT(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>include_segment</b>
 */'''
class Iinclude_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>produces0
 *<li>produces1
 *<li>produces2
 *<li>produces3
 *</ul>
 *</b>
 */'''
class Iproduces(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>alias_rhs0
 *<li>alias_rhs1
 *<li>alias_rhs2
 *<li>alias_rhs3
 *<li>alias_rhs4
 *<li>alias_rhs5
 *<li>alias_rhs6
 *</ul>
 *</b>
 */'''
class Ialias_rhs(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>alias_lhs_macro_name</b>
 */'''
class Ialias_lhs_macro_name(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>action_segmentList</b>
 */'''
class Iaction_segment_list(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>macro_name_symbol0
 *<li>macro_name_symbol1
 *</ul>
 *</b>
 */'''
class Imacro_name_symbol(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>macro_segment</b>
 */'''
class Imacro_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>terminal_symbol0
 *<li>terminal_symbol1
 *</ul>
 *</b>
 */'''
class Iterminal_symbol(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>action_segment</b>
 */'''
class Iaction_segment(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>optMacroName</b>
 */'''
class IoptMacroName(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>name0
 *<li>name1
 *<li>name2
 *<li>name3
 *<li>name4
 *<li>name5
 *</ul>
 *</b>
 */'''
class Iname(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>RuleName</b>
 */'''
class IruleNameWithAttributes(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>symWithAttrs0
 *<li>symWithAttrs1
 *</ul>
 *</b>
 */'''
class IsymWithAttrs(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is implemented by <b>symAttrs</b>
 */'''
class IoptAttrList(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>start_symbol0
 *<li>start_symbol1
 *</ul>
 *</b>
 */'''
class Istart_symbol(IRootForLPGParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>ASTNodeToken</b>. It is also implemented by <b>recover_symbol</b>
 */'''
class Irecover_symbol(IRootForLPGParser):
        __slots__ = ()

class ASTNode(IAst):
    
        def getNextAst(self): return None
        def  setParent(self, parent):  self.parent = parent
        def  getParent(self): return self.parent

        def getLeftIToken(self) :  return self.leftIToken
        def getRightIToken(self):  return self.rightIToken
        def getPrecedingAdjuncts(self)  : return self.leftIToken.getPrecedingAdjuncts()
        def getFollowingAdjuncts(self)  : return self.rightIToken.getFollowingAdjuncts()

        def  toString(self) :  
        
            info = self.leftIToken.getILexStream().toString(self.leftIToken.getStartOffset(), self.rightIToken.getEndOffset())
            return info if  info else  ""
        

        __slots__ = ('parent', 'leftIToken', 'rightIToken', 'nextAst')
        def __init__(self,leftIToken  , rightIToken  = None ):
        
            self.parent = None
            self.leftIToken = leftIToken
            if rightIToken: self.rightIToken = rightIToken
            else:            self.rightIToken = leftIToken
        

        def  initialize(self): pass

        '''/**
         * A list of all children of this node, excluding the null ones.
         */'''
        def  getChildren(self):
        
            _content = self.getAllChildren() 
            k = -1
            for i in range(_content.size):
            
                element = _content.get(i)
                if element:
                
                    k += 1
                    if (k != i):
                        _content.set(k, element)
                
            
            i = _content.size() - 1
            while i > k : # remove extraneous elements
                i-=1
                _content.remove(i)
            return _content
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def   getAllChildren(self): raise TypeError('Can not instantiate abstract class  with abstract methods')

        def  accept(self, v):pass
    

class AbstractASTNodeList ( ASTNode , IAbstractArrayList):
    
        def size(self): return self._content.size()
        def getList(self): return self._content
        def  getElementAt(self,i ) : return self._content.get( i if self.left_recursive else  self._content.size() - 1 - i)
        def  getArrayList(self)  :
        
            if not self.left_recursive: # reverse the list 
            
                i = 0
                n = self._content.size() - 1
                while i < n :
                
                    ith = self._content.get(i)
                    nth = self._content.get(n)
                    self._content.set(i, nth)
                    self._content.set(n, ith)
                    i+=1
                    n-=1
                
                self.left_recursive = True
            
            return self._content
        
        '''/**
         * @deprecated replaced by {@link #addElement()}
         *
         */'''
        def  add(self, element )  :
        
            self.addElement(element)
            return True
        

        def  addElement(self,element) : 
        
            self._content.add(element)
            if self.left_recursive:
                 self.rightIToken = element.getRightIToken()
            else :
                 self.leftIToken = element.getLeftIToken()
        

        __slots__ = ('left_recursive', '_content')
        def __init__(self,leftToken , rightToken  , left_recursive ):        
              super(AbstractASTNodeList, self).__init__(leftToken, rightToken)
              self.left_recursive = left_recursive
              self._content = ArrayList()
        

        '''/**
         * Make a copy of the list and return it. Note that we obtain the local list by
         * invoking getArrayList so as to make sure that the list we return is in proper order.
         */'''
        def  getAllChildren(self):
        
            return self.getArrayList().clone()
        

    

class ASTNodeToken ( ASTNode, IASTNodeToken):
    
        __slots__ = ()
        def __init__(self,token) : super(ASTNodeToken,self).__init__(token)
        def  getIToken(self): return self.leftIToken
        def  toString(self):  return self.leftIToken.toString()

        '''/**
         * A token class has no children. So, we return the empty list.
         */'''
        def  getAllChildren(self)  :  return ArrayList()


        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitASTNodeToken(self)
            v.endVisitASTNodeToken(self)
        
    

'''/**
 *<b>
#*<li>Rule 1:  LPG ::= options_segment LPG_INPUT
 *</b>
 */'''
class LPG ( ASTNode ,ILPG):
    
        def getEnvironment(self): return self.environment


        def  getoptions_segment(self)  :  return self._options_segment
        def  setoptions_segment(self,  _options_segment) :   self._options_segment = _options_segment
        def  getLPG_INPUT(self)  :  return self._LPG_INPUT
        def  setLPG_INPUT(self,  _LPG_INPUT) :   self._LPG_INPUT = _LPG_INPUT

        __slots__ = ('environment', '_options_segment', '_LPG_INPUT')

        def __init__(self, environment ,leftIToken, rightIToken,
                             _options_segment,
                             _LPG_INPUT):
        
            super(LPG, self).__init__(leftIToken, rightIToken)

            self.environment = environment
            self._options_segment = _options_segment
            _options_segment.setParent(self)
            self._LPG_INPUT = _LPG_INPUT
            _LPG_INPUT.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._options_segment:  _content.add(self._options_segment)
            if self._LPG_INPUT:  _content.add(self._LPG_INPUT)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitLPG(self)
            if checkChildren:
            
                self._options_segment.accept(v)
                self._LPG_INPUT.accept(v)
            
            v.endVisitLPG(self)
        
    

'''/**
 *<b>
#*<li>Rule 2:  LPG_INPUT ::= $Empty
#*<li>Rule 3:  LPG_INPUT ::= LPG_INPUT LPG_item
 *</b>
 */'''
class LPG_itemList ( AbstractASTNodeList, ILPG_INPUT):
    
        def  getLPG_itemAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(LPG_itemList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def LPG_itemListfromElement(element,left_recursive)  :
        
            obj = LPG_itemList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _LPG_item): 
        
            super(LPG_itemList, self).addElement( _LPG_item)
            _LPG_item.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getLPG_itemAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 4:  LPG_item ::= ALIAS_KEY$ alias_segment END_KEY_OPT$
 *</b>
 */'''
class AliasSeg ( ASTNode ,ILPG_item):
    

        def  getalias_segment(self)  :  return self._alias_segment
        def  setalias_segment(self,  _alias_segment) :   self._alias_segment = _alias_segment

        __slots__ = '_alias_segment'

        def __init__(self, leftIToken, rightIToken,
                             _alias_segment):
        
            super(AliasSeg, self).__init__(leftIToken, rightIToken)

            self._alias_segment = _alias_segment
            _alias_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._alias_segment:  _content.add(self._alias_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitAliasSeg(self)
            if checkChildren:
                self._alias_segment.accept(v)
            v.endVisitAliasSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 5:  LPG_item ::= AST_KEY$ ast_segment END_KEY_OPT$
 *</b>
 */'''
class AstSeg ( ASTNode ,ILPG_item):
    

        def  getast_segment(self)  :  return self._ast_segment
        def  setast_segment(self,  _ast_segment) :   self._ast_segment = _ast_segment

        __slots__ = '_ast_segment'

        def __init__(self, leftIToken, rightIToken,
                             _ast_segment):
        
            super(AstSeg, self).__init__(leftIToken, rightIToken)

            self._ast_segment = _ast_segment
            _ast_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ast_segment:  _content.add(self._ast_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitAstSeg(self)
            if checkChildren:
                self._ast_segment.accept(v)
            v.endVisitAstSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 6:  LPG_item ::= DEFINE_KEY$ define_segment END_KEY_OPT$
 *</b>
 */'''
class DefineSeg ( ASTNode ,ILPG_item):
    

        def  getdefine_segment(self)  :  return self._define_segment
        def  setdefine_segment(self,  _define_segment) :   self._define_segment = _define_segment

        __slots__ = '_define_segment'

        def __init__(self, leftIToken, rightIToken,
                             _define_segment):
        
            super(DefineSeg, self).__init__(leftIToken, rightIToken)

            self._define_segment = _define_segment
            _define_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._define_segment:  _content.add(self._define_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitDefineSeg(self)
            if checkChildren:
                self._define_segment.accept(v)
            v.endVisitDefineSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 7:  LPG_item ::= EOF_KEY$ eof_segment END_KEY_OPT$
 *</b>
 */'''
class EofSeg ( ASTNode ,ILPG_item):
    

        def  geteof_segment(self)  :  return self._eof_segment
        def  seteof_segment(self,  _eof_segment) :   self._eof_segment = _eof_segment

        __slots__ = '_eof_segment'

        def __init__(self, leftIToken, rightIToken,
                             _eof_segment):
        
            super(EofSeg, self).__init__(leftIToken, rightIToken)

            self._eof_segment = _eof_segment
            _eof_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._eof_segment:  _content.add(self._eof_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitEofSeg(self)
            if checkChildren:
                self._eof_segment.accept(v)
            v.endVisitEofSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 8:  LPG_item ::= EOL_KEY$ eol_segment END_KEY_OPT$
 *</b>
 */'''
class EolSeg ( ASTNode ,ILPG_item):
    

        def  geteol_segment(self)  :  return self._eol_segment
        def  seteol_segment(self,  _eol_segment) :   self._eol_segment = _eol_segment

        __slots__ = '_eol_segment'

        def __init__(self, leftIToken, rightIToken,
                             _eol_segment):
        
            super(EolSeg, self).__init__(leftIToken, rightIToken)

            self._eol_segment = _eol_segment
            _eol_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._eol_segment:  _content.add(self._eol_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitEolSeg(self)
            if checkChildren:
                self._eol_segment.accept(v)
            v.endVisitEolSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 9:  LPG_item ::= ERROR_KEY$ error_segment END_KEY_OPT$
 *</b>
 */'''
class ErrorSeg ( ASTNode ,ILPG_item):
    

        def  geterror_segment(self)  :  return self._error_segment
        def  seterror_segment(self,  _error_segment) :   self._error_segment = _error_segment

        __slots__ = '_error_segment'

        def __init__(self, leftIToken, rightIToken,
                             _error_segment):
        
            super(ErrorSeg, self).__init__(leftIToken, rightIToken)

            self._error_segment = _error_segment
            _error_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._error_segment:  _content.add(self._error_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitErrorSeg(self)
            if checkChildren:
                self._error_segment.accept(v)
            v.endVisitErrorSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 10:  LPG_item ::= EXPORT_KEY$ export_segment END_KEY_OPT$
 *</b>
 */'''
class ExportSeg ( ASTNode ,ILPG_item):
    

        def  getexport_segment(self)  :  return self._export_segment
        def  setexport_segment(self,  _export_segment) :   self._export_segment = _export_segment

        __slots__ = '_export_segment'

        def __init__(self, leftIToken, rightIToken,
                             _export_segment):
        
            super(ExportSeg, self).__init__(leftIToken, rightIToken)

            self._export_segment = _export_segment
            _export_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._export_segment:  _content.add(self._export_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitExportSeg(self)
            if checkChildren:
                self._export_segment.accept(v)
            v.endVisitExportSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 11:  LPG_item ::= GLOBALS_KEY$ globals_segment END_KEY_OPT$
 *</b>
 */'''
class GlobalsSeg ( ASTNode ,ILPG_item):
    

        def  getglobals_segment(self)  :  return self._globals_segment
        def  setglobals_segment(self,  _globals_segment) :   self._globals_segment = _globals_segment

        __slots__ = '_globals_segment'

        def __init__(self, leftIToken, rightIToken,
                             _globals_segment):
        
            super(GlobalsSeg, self).__init__(leftIToken, rightIToken)

            self._globals_segment = _globals_segment
            _globals_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._globals_segment:  _content.add(self._globals_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitGlobalsSeg(self)
            if checkChildren:
                self._globals_segment.accept(v)
            v.endVisitGlobalsSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 12:  LPG_item ::= HEADERS_KEY$ headers_segment END_KEY_OPT$
 *</b>
 */'''
class HeadersSeg ( ASTNode ,ILPG_item):
    

        def  getheaders_segment(self)  :  return self._headers_segment
        def  setheaders_segment(self,  _headers_segment) :   self._headers_segment = _headers_segment

        __slots__ = '_headers_segment'

        def __init__(self, leftIToken, rightIToken,
                             _headers_segment):
        
            super(HeadersSeg, self).__init__(leftIToken, rightIToken)

            self._headers_segment = _headers_segment
            _headers_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._headers_segment:  _content.add(self._headers_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitHeadersSeg(self)
            if checkChildren:
                self._headers_segment.accept(v)
            v.endVisitHeadersSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 13:  LPG_item ::= IDENTIFIER_KEY$ identifier_segment END_KEY_OPT$
 *</b>
 */'''
class IdentifierSeg ( ASTNode ,ILPG_item):
    

        def  getidentifier_segment(self)  :  return self._identifier_segment
        def  setidentifier_segment(self,  _identifier_segment) :   self._identifier_segment = _identifier_segment

        __slots__ = '_identifier_segment'

        def __init__(self, leftIToken, rightIToken,
                             _identifier_segment):
        
            super(IdentifierSeg, self).__init__(leftIToken, rightIToken)

            self._identifier_segment = _identifier_segment
            _identifier_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._identifier_segment:  _content.add(self._identifier_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitIdentifierSeg(self)
            if checkChildren:
                self._identifier_segment.accept(v)
            v.endVisitIdentifierSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 14:  LPG_item ::= IMPORT_KEY$ import_segment END_KEY_OPT$
 *</b>
 */'''
class ImportSeg ( ASTNode ,ILPG_item):
    

        def  getimport_segment(self)  :  return self._import_segment
        def  setimport_segment(self,  _import_segment) :   self._import_segment = _import_segment

        __slots__ = '_import_segment'

        def __init__(self, leftIToken, rightIToken,
                             _import_segment):
        
            super(ImportSeg, self).__init__(leftIToken, rightIToken)

            self._import_segment = _import_segment
            _import_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._import_segment:  _content.add(self._import_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitImportSeg(self)
            if checkChildren:
                self._import_segment.accept(v)
            v.endVisitImportSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 15:  LPG_item ::= INCLUDE_KEY$ include_segment END_KEY_OPT$
 *</b>
 */'''
class IncludeSeg ( ASTNode ,ILPG_item):
    

        def  getinclude_segment(self)  :  return self._include_segment
        def  setinclude_segment(self,  _include_segment) :   self._include_segment = _include_segment

        __slots__ = '_include_segment'

        def __init__(self, leftIToken, rightIToken,
                             _include_segment):
        
            super(IncludeSeg, self).__init__(leftIToken, rightIToken)

            self._include_segment = _include_segment
            _include_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._include_segment:  _content.add(self._include_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitIncludeSeg(self)
            if checkChildren:
                self._include_segment.accept(v)
            v.endVisitIncludeSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 16:  LPG_item ::= KEYWORDS_KEY$ keywords_segment END_KEY_OPT$
 *</b>
 */'''
class KeywordsSeg ( ASTNode ,ILPG_item):
    

        def  getkeywords_segment(self)  :  return self._keywords_segment
        def  setkeywords_segment(self,  _keywords_segment) :   self._keywords_segment = _keywords_segment

        __slots__ = '_keywords_segment'

        def __init__(self, leftIToken, rightIToken,
                             _keywords_segment):
        
            super(KeywordsSeg, self).__init__(leftIToken, rightIToken)

            self._keywords_segment = _keywords_segment
            _keywords_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._keywords_segment:  _content.add(self._keywords_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitKeywordsSeg(self)
            if checkChildren:
                self._keywords_segment.accept(v)
            v.endVisitKeywordsSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 17:  LPG_item ::= NAMES_KEY$ names_segment END_KEY_OPT$
 *</b>
 */'''
class NamesSeg ( ASTNode ,ILPG_item):
    

        def  getnames_segment(self)  :  return self._names_segment
        def  setnames_segment(self,  _names_segment) :   self._names_segment = _names_segment

        __slots__ = '_names_segment'

        def __init__(self, leftIToken, rightIToken,
                             _names_segment):
        
            super(NamesSeg, self).__init__(leftIToken, rightIToken)

            self._names_segment = _names_segment
            _names_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._names_segment:  _content.add(self._names_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitNamesSeg(self)
            if checkChildren:
                self._names_segment.accept(v)
            v.endVisitNamesSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 18:  LPG_item ::= NOTICE_KEY$ notice_segment END_KEY_OPT$
 *</b>
 */'''
class NoticeSeg ( ASTNode ,ILPG_item):
    

        def  getnotice_segment(self)  :  return self._notice_segment
        def  setnotice_segment(self,  _notice_segment) :   self._notice_segment = _notice_segment

        __slots__ = '_notice_segment'

        def __init__(self, leftIToken, rightIToken,
                             _notice_segment):
        
            super(NoticeSeg, self).__init__(leftIToken, rightIToken)

            self._notice_segment = _notice_segment
            _notice_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._notice_segment:  _content.add(self._notice_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitNoticeSeg(self)
            if checkChildren:
                self._notice_segment.accept(v)
            v.endVisitNoticeSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 19:  LPG_item ::= RULES_KEY$ rules_segment END_KEY_OPT$
 *</b>
 */'''
class RulesSeg ( ASTNode ,ILPG_item):
    

        def  getrules_segment(self)  :  return self._rules_segment
        def  setrules_segment(self,  _rules_segment) :   self._rules_segment = _rules_segment

        __slots__ = '_rules_segment'

        def __init__(self, leftIToken, rightIToken,
                             _rules_segment):
        
            super(RulesSeg, self).__init__(leftIToken, rightIToken)

            self._rules_segment = _rules_segment
            _rules_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._rules_segment:  _content.add(self._rules_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitRulesSeg(self)
            if checkChildren:
                self._rules_segment.accept(v)
            v.endVisitRulesSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 20:  LPG_item ::= SOFT_KEYWORDS_KEY$ keywords_segment END_KEY_OPT$
 *</b>
 */'''
class SoftKeywordsSeg ( ASTNode ,ILPG_item):
    

        def  getkeywords_segment(self)  :  return self._keywords_segment
        def  setkeywords_segment(self,  _keywords_segment) :   self._keywords_segment = _keywords_segment

        __slots__ = '_keywords_segment'

        def __init__(self, leftIToken, rightIToken,
                             _keywords_segment):
        
            super(SoftKeywordsSeg, self).__init__(leftIToken, rightIToken)

            self._keywords_segment = _keywords_segment
            _keywords_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._keywords_segment:  _content.add(self._keywords_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitSoftKeywordsSeg(self)
            if checkChildren:
                self._keywords_segment.accept(v)
            v.endVisitSoftKeywordsSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 21:  LPG_item ::= START_KEY$ start_segment END_KEY_OPT$
 *</b>
 */'''
class StartSeg ( ASTNode ,ILPG_item):
    

        def  getstart_segment(self)  :  return self._start_segment
        def  setstart_segment(self,  _start_segment) :   self._start_segment = _start_segment

        __slots__ = '_start_segment'

        def __init__(self, leftIToken, rightIToken,
                             _start_segment):
        
            super(StartSeg, self).__init__(leftIToken, rightIToken)

            self._start_segment = _start_segment
            _start_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._start_segment:  _content.add(self._start_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitStartSeg(self)
            if checkChildren:
                self._start_segment.accept(v)
            v.endVisitStartSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 22:  LPG_item ::= TERMINALS_KEY$ terminals_segment END_KEY_OPT$
 *</b>
 */'''
class TerminalsSeg ( ASTNode ,ILPG_item):
    

        def  getterminals_segment(self)  :  return self._terminals_segment
        def  setterminals_segment(self,  _terminals_segment) :   self._terminals_segment = _terminals_segment

        __slots__ = '_terminals_segment'

        def __init__(self, leftIToken, rightIToken,
                             _terminals_segment):
        
            super(TerminalsSeg, self).__init__(leftIToken, rightIToken)

            self._terminals_segment = _terminals_segment
            _terminals_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._terminals_segment:  _content.add(self._terminals_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitTerminalsSeg(self)
            if checkChildren:
                self._terminals_segment.accept(v)
            v.endVisitTerminalsSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 23:  LPG_item ::= TRAILERS_KEY$ trailers_segment END_KEY_OPT$
 *</b>
 */'''
class TrailersSeg ( ASTNode ,ILPG_item):
    

        def  gettrailers_segment(self)  :  return self._trailers_segment
        def  settrailers_segment(self,  _trailers_segment) :   self._trailers_segment = _trailers_segment

        __slots__ = '_trailers_segment'

        def __init__(self, leftIToken, rightIToken,
                             _trailers_segment):
        
            super(TrailersSeg, self).__init__(leftIToken, rightIToken)

            self._trailers_segment = _trailers_segment
            _trailers_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._trailers_segment:  _content.add(self._trailers_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitTrailersSeg(self)
            if checkChildren:
                self._trailers_segment.accept(v)
            v.endVisitTrailersSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 24:  LPG_item ::= TYPES_KEY$ types_segment END_KEY_OPT$
 *</b>
 */'''
class TypesSeg ( ASTNode ,ILPG_item):
    

        def  gettypes_segment(self)  :  return self._types_segment
        def  settypes_segment(self,  _types_segment) :   self._types_segment = _types_segment

        __slots__ = '_types_segment'

        def __init__(self, leftIToken, rightIToken,
                             _types_segment):
        
            super(TypesSeg, self).__init__(leftIToken, rightIToken)

            self._types_segment = _types_segment
            _types_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._types_segment:  _content.add(self._types_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitTypesSeg(self)
            if checkChildren:
                self._types_segment.accept(v)
            v.endVisitTypesSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 25:  LPG_item ::= RECOVER_KEY$ recover_segment END_KEY_OPT$
 *</b>
 */'''
class RecoverSeg ( ASTNode ,ILPG_item):
    

        def  getrecover_segment(self)  :  return self._recover_segment
        def  setrecover_segment(self,  _recover_segment) :   self._recover_segment = _recover_segment

        __slots__ = '_recover_segment'

        def __init__(self, leftIToken, rightIToken,
                             _recover_segment):
        
            super(RecoverSeg, self).__init__(leftIToken, rightIToken)

            self._recover_segment = _recover_segment
            _recover_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._recover_segment:  _content.add(self._recover_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitRecoverSeg(self)
            if checkChildren:
                self._recover_segment.accept(v)
            v.endVisitRecoverSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 26:  LPG_item ::= DISJOINTPREDECESSORSETS_KEY$ predecessor_segment END_KEY_OPT$
 *</b>
 */'''
class PredecessorSeg ( ASTNode ,ILPG_item):
    

        def  getpredecessor_segment(self)  :  return self._predecessor_segment
        def  setpredecessor_segment(self,  _predecessor_segment) :   self._predecessor_segment = _predecessor_segment

        __slots__ = '_predecessor_segment'

        def __init__(self, leftIToken, rightIToken,
                             _predecessor_segment):
        
            super(PredecessorSeg, self).__init__(leftIToken, rightIToken)

            self._predecessor_segment = _predecessor_segment
            _predecessor_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._predecessor_segment:  _content.add(self._predecessor_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitPredecessorSeg(self)
            if checkChildren:
                self._predecessor_segment.accept(v)
            v.endVisitPredecessorSeg(self)
        
    

'''/**
 *<b>
#*<li>Rule 27:  options_segment ::= $Empty
#*<li>Rule 28:  options_segment ::= options_segment option_spec
 *</b>
 */'''
class option_specList ( AbstractASTNodeList, Ioptions_segment):
    
        def  getoption_specAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(option_specList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def option_specListfromElement(element,left_recursive)  :
        
            obj = option_specList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _option_spec): 
        
            super(option_specList, self).addElement( _option_spec)
            _option_spec.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getoption_specAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 29:  option_spec ::= OPTIONS_KEY$ option_list
 *</b>
 */'''
class option_spec ( ASTNode ,Ioption_spec):
    

        def  getoption_list(self)  :  return self._option_list
        def  setoption_list(self,  _option_list) :   self._option_list = _option_list

        __slots__ = '_option_list'

        def __init__(self, leftIToken, rightIToken,
                             _option_list):
        
            super(option_spec, self).__init__(leftIToken, rightIToken)

            self._option_list = _option_list
            _option_list.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._option_list:  _content.add(self._option_list)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitoption_spec(self)
            if checkChildren:
                self._option_list.accept(v)
            v.endVisitoption_spec(self)
        
    

'''/**
 *<b>
#*<li>Rule 30:  option_list ::= option
#*<li>Rule 31:  option_list ::= option_list ,$ option
 *</b>
 */'''
class optionList ( AbstractASTNodeList, Ioption_list):
    
        def  getoptionAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(optionList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def optionListfromElement(element,left_recursive)  :
        
            obj = optionList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _option): 
        
            super(optionList, self).addElement( _option)
            _option.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getoptionAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 32:  option ::= SYMBOL option_value
 *</b>
 */'''
class option ( ASTNode ,Ioption):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        '''/**
         * The value returned by <b>getoption_value</b> may be <b>null</b>
         */'''
        def  getoption_value(self)  :  return self._option_value
        def  setoption_value(self,  _option_value) :   self._option_value = _option_value

        __slots__ = ('_SYMBOL', '_option_value')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _option_value):
        
            super(option, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._option_value = _option_value
            if _option_value: _option_value.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._option_value:  _content.add(self._option_value)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitoption(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                if self._option_value: self._option_value.accept(v)
            
            v.endVisitoption(self)
        
    

'''/**
 *<b>
#*<li>Rule 36:  symbol_list ::= SYMBOL
#*<li>Rule 37:  symbol_list ::= symbol_list ,$ SYMBOL
#*<li>Rule 75:  drop_symbols ::= SYMBOL
#*<li>Rule 76:  drop_symbols ::= drop_symbols SYMBOL
#*<li>Rule 136:  barSymbolList ::= SYMBOL
#*<li>Rule 137:  barSymbolList ::= barSymbolList |$ SYMBOL
#*<li>Rule 141:  recover_segment ::= $Empty
#*<li>Rule 142:  recover_segment ::= recover_segment recover_symbol
 *</b>
 */'''
class SYMBOLList ( AbstractASTNodeList, Isymbol_list, Idrop_symbols, IbarSymbolList, Irecover_segment):
    
        def  getSYMBOLAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(SYMBOLList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def SYMBOLListfromElement(element,left_recursive)  :
        
            obj = SYMBOLList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _SYMBOL): 
        
            super(SYMBOLList, self).addElement( _SYMBOL)
            _SYMBOL.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getSYMBOLAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 38:  alias_segment ::= aliasSpec
#*<li>Rule 39:  alias_segment ::= alias_segment aliasSpec
 *</b>
 */'''
class aliasSpecList ( AbstractASTNodeList, Ialias_segment):
    
        def  getaliasSpecAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(aliasSpecList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def aliasSpecListfromElement(element,left_recursive)  :
        
            obj = aliasSpecList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _aliasSpec): 
        
            super(aliasSpecList, self).addElement( _aliasSpec)
            _aliasSpec.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getaliasSpecAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 46:  alias_lhs_macro_name ::= MACRO_NAME
 *</b>
 */'''
class alias_lhs_macro_name ( ASTNodeToken ,Ialias_lhs_macro_name):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_lhs_macro_name, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_lhs_macro_name(self)
            v.endVisitalias_lhs_macro_name(self)
        
    

'''/**
 *<b>
#*<li>Rule 55:  define_segment ::= defineSpec
#*<li>Rule 56:  define_segment ::= define_segment defineSpec
 *</b>
 */'''
class defineSpecList ( AbstractASTNodeList, Idefine_segment):
    
        def  getdefineSpecAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(defineSpecList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def defineSpecListfromElement(element,left_recursive)  :
        
            obj = defineSpecList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _defineSpec): 
        
            super(defineSpecList, self).addElement( _defineSpec)
            _defineSpec.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getdefineSpecAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 57:  defineSpec ::= macro_name_symbol macro_segment
 *</b>
 */'''
class defineSpec ( ASTNode ,IdefineSpec):
    

        def  getmacro_name_symbol(self)  :  return self._macro_name_symbol
        def  setmacro_name_symbol(self,  _macro_name_symbol) :   self._macro_name_symbol = _macro_name_symbol
        def  getmacro_segment(self)  :  return self._macro_segment
        def  setmacro_segment(self,  _macro_segment) :   self._macro_segment = _macro_segment

        __slots__ = ('_macro_name_symbol', '_macro_segment')

        def __init__(self, leftIToken, rightIToken,
                             _macro_name_symbol,
                             _macro_segment):
        
            super(defineSpec, self).__init__(leftIToken, rightIToken)

            self._macro_name_symbol = _macro_name_symbol
            _macro_name_symbol.setParent(self)
            self._macro_segment = _macro_segment
            _macro_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._macro_name_symbol:  _content.add(self._macro_name_symbol)
            if self._macro_segment:  _content.add(self._macro_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitdefineSpec(self)
            if checkChildren:
            
                self._macro_name_symbol.accept(v)
                self._macro_segment.accept(v)
            
            v.endVisitdefineSpec(self)
        
    

'''/**
 *<b>
#*<li>Rule 60:  macro_segment ::= BLOCK
 *</b>
 */'''
class macro_segment ( ASTNodeToken ,Imacro_segment):
    
        def  getBLOCK(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(macro_segment, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitmacro_segment(self)
            v.endVisitmacro_segment(self)
        
    

'''/**
 *<b>
#*<li>Rule 64:  export_segment ::= terminal_symbol
#*<li>Rule 65:  export_segment ::= export_segment terminal_symbol
 *</b>
 */'''
class terminal_symbolList ( AbstractASTNodeList, Iexport_segment):
    
        def  getterminal_symbolAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(terminal_symbolList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def terminal_symbolListfromElement(element,left_recursive)  :
        
            obj = terminal_symbolList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _terminal_symbol): 
        
            super(terminal_symbolList, self).addElement( _terminal_symbol)
            _terminal_symbol.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getterminal_symbolAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 66:  globals_segment ::= action_segment
#*<li>Rule 67:  globals_segment ::= globals_segment action_segment
#*<li>Rule 96:  notice_segment ::= action_segment
#*<li>Rule 97:  notice_segment ::= notice_segment action_segment
#*<li>Rule 146:  action_segment_list ::= $Empty
#*<li>Rule 147:  action_segment_list ::= action_segment_list action_segment
 *</b>
 */'''
class action_segmentList ( AbstractASTNodeList, Iglobals_segment, Inotice_segment, Iaction_segment_list):
    
        def  getaction_segmentAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(action_segmentList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def action_segmentListfromElement(element,left_recursive)  :
        
            obj = action_segmentList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _action_segment): 
        
            super(action_segmentList, self).addElement( _action_segment)
            _action_segment.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getaction_segmentAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 70:  import_segment ::= SYMBOL drop_command_list
 *</b>
 */'''
class import_segment ( ASTNode ,Iimport_segment):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        def  getdrop_command_list(self)  :  return self._drop_command_list
        def  setdrop_command_list(self,  _drop_command_list) :   self._drop_command_list = _drop_command_list

        __slots__ = ('_SYMBOL', '_drop_command_list')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _drop_command_list):
        
            super(import_segment, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._drop_command_list = _drop_command_list
            _drop_command_list.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._drop_command_list:  _content.add(self._drop_command_list)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitimport_segment(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                self._drop_command_list.accept(v)
            
            v.endVisitimport_segment(self)
        
    

'''/**
 *<b>
#*<li>Rule 71:  drop_command_list ::= $Empty
#*<li>Rule 72:  drop_command_list ::= drop_command_list drop_command
 *</b>
 */'''
class drop_commandList ( AbstractASTNodeList, Idrop_command_list):
    
        def  getdrop_commandAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(drop_commandList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def drop_commandListfromElement(element,left_recursive)  :
        
            obj = drop_commandList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _drop_command): 
        
            super(drop_commandList, self).addElement( _drop_command)
            _drop_command.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getdrop_commandAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 77:  drop_rules ::= drop_rule
#*<li>Rule 78:  drop_rules ::= drop_rules drop_rule
 *</b>
 */'''
class drop_ruleList ( AbstractASTNodeList, Idrop_rules):
    
        def  getdrop_ruleAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(drop_ruleList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def drop_ruleListfromElement(element,left_recursive)  :
        
            obj = drop_ruleList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _drop_rule): 
        
            super(drop_ruleList, self).addElement( _drop_rule)
            _drop_rule.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getdrop_ruleAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 79:  drop_rule ::= SYMBOL optMacroName produces ruleList
 *</b>
 */'''
class drop_rule ( ASTNode ,Idrop_rule):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        '''/**
         * The value returned by <b>getoptMacroName</b> may be <b>null</b>
         */'''
        def  getoptMacroName(self)  :  return self._optMacroName
        def  setoptMacroName(self,  _optMacroName) :   self._optMacroName = _optMacroName
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getruleList(self)  :  return self._ruleList
        def  setruleList(self,  _ruleList) :   self._ruleList = _ruleList

        __slots__ = ('_SYMBOL', '_optMacroName', '_produces', '_ruleList')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _optMacroName,
                             _produces,
                             _ruleList):
        
            super(drop_rule, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._optMacroName = _optMacroName
            if _optMacroName: _optMacroName.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._ruleList = _ruleList
            _ruleList.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._optMacroName:  _content.add(self._optMacroName)
            if self._produces:  _content.add(self._produces)
            if self._ruleList:  _content.add(self._ruleList)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitdrop_rule(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                if self._optMacroName: self._optMacroName.accept(v)
                self._produces.accept(v)
                self._ruleList.accept(v)
            
            v.endVisitdrop_rule(self)
        
    

'''/**
 *<em>
#*<li>Rule 80:  optMacroName ::= $Empty
 *</em>
 *<p>
 *<b>
#*<li>Rule 81:  optMacroName ::= MACRO_NAME
 *</b>
 */'''
class optMacroName ( ASTNodeToken ,IoptMacroName):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(optMacroName, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitoptMacroName(self)
            v.endVisitoptMacroName(self)
        
    

'''/**
 *<b>
#*<li>Rule 82:  include_segment ::= SYMBOL
 *</b>
 */'''
class include_segment ( ASTNodeToken ,Iinclude_segment):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(include_segment, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitinclude_segment(self)
            v.endVisitinclude_segment(self)
        
    

'''/**
 *<b>
#*<li>Rule 83:  keywords_segment ::= keywordSpec
#*<li>Rule 84:  keywords_segment ::= keywords_segment keywordSpec
 *</b>
 */'''
class keywordSpecList ( AbstractASTNodeList, Ikeywords_segment):
    
        def  getkeywordSpecAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(keywordSpecList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def keywordSpecListfromElement(element,left_recursive)  :
        
            obj = keywordSpecList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _keywordSpec): 
        
            super(keywordSpecList, self).addElement( _keywordSpec)
            _keywordSpec.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getkeywordSpecAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<em>
#*<li>Rule 85:  keywordSpec ::= terminal_symbol
 *</em>
 *<p>
 *<b>
#*<li>Rule 86:  keywordSpec ::= terminal_symbol produces name
 *</b>
 */'''
class keywordSpec ( ASTNode ,IkeywordSpec):
    

        def  getterminal_symbol(self)  :  return self._terminal_symbol
        def  setterminal_symbol(self,  _terminal_symbol) :   self._terminal_symbol = _terminal_symbol
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getname(self)  :  return self._name
        def  setname(self,  _name) :   self._name = _name

        __slots__ = ('_terminal_symbol', '_produces', '_name')

        def __init__(self, leftIToken, rightIToken,
                             _terminal_symbol,
                             _produces,
                             _name):
        
            super(keywordSpec, self).__init__(leftIToken, rightIToken)

            self._terminal_symbol = _terminal_symbol
            _terminal_symbol.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._name = _name
            _name.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._terminal_symbol:  _content.add(self._terminal_symbol)
            if self._produces:  _content.add(self._produces)
            if self._name:  _content.add(self._name)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitkeywordSpec(self)
            if checkChildren:
            
                self._terminal_symbol.accept(v)
                self._produces.accept(v)
                self._name.accept(v)
            
            v.endVisitkeywordSpec(self)
        
    

'''/**
 *<b>
#*<li>Rule 87:  names_segment ::= nameSpec
#*<li>Rule 88:  names_segment ::= names_segment nameSpec
 *</b>
 */'''
class nameSpecList ( AbstractASTNodeList, Inames_segment):
    
        def  getnameSpecAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(nameSpecList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def nameSpecListfromElement(element,left_recursive)  :
        
            obj = nameSpecList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _nameSpec): 
        
            super(nameSpecList, self).addElement( _nameSpec)
            _nameSpec.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getnameSpecAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 89:  nameSpec ::= name produces name
 *</b>
 */'''
class nameSpec ( ASTNode ,InameSpec):
    

        def  getname(self)  :  return self._name
        def  setname(self,  _name) :   self._name = _name
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getname3(self)  :  return self._name3
        def  setname3(self,  _name3) :   self._name3 = _name3

        __slots__ = ('_name', '_produces', '_name3')

        def __init__(self, leftIToken, rightIToken,
                             _name,
                             _produces,
                             _name3):
        
            super(nameSpec, self).__init__(leftIToken, rightIToken)

            self._name = _name
            _name.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._name3 = _name3
            _name3.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._name:  _content.add(self._name)
            if self._produces:  _content.add(self._produces)
            if self._name3:  _content.add(self._name3)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitnameSpec(self)
            if checkChildren:
            
                self._name.accept(v)
                self._produces.accept(v)
                self._name3.accept(v)
            
            v.endVisitnameSpec(self)
        
    

'''/**
 *<b>
#*<li>Rule 98:  rules_segment ::= action_segment_list nonTermList
 *</b>
 */'''
class rules_segment ( ASTNode ,Irules_segment):
    

        def  getaction_segment_list(self)  :  return self._action_segment_list
        def  setaction_segment_list(self,  _action_segment_list) :   self._action_segment_list = _action_segment_list
        def  getnonTermList(self)  :  return self._nonTermList
        def  setnonTermList(self,  _nonTermList) :   self._nonTermList = _nonTermList

        __slots__ = ('_action_segment_list', '_nonTermList')

        def __init__(self, leftIToken, rightIToken,
                             _action_segment_list,
                             _nonTermList):
        
            super(rules_segment, self).__init__(leftIToken, rightIToken)

            self._action_segment_list = _action_segment_list
            _action_segment_list.setParent(self)
            self._nonTermList = _nonTermList
            _nonTermList.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._action_segment_list:  _content.add(self._action_segment_list)
            if self._nonTermList:  _content.add(self._nonTermList)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitrules_segment(self)
            if checkChildren:
            
                self._action_segment_list.accept(v)
                self._nonTermList.accept(v)
            
            v.endVisitrules_segment(self)
        
    

'''/**
 *<b>
#*<li>Rule 99:  nonTermList ::= $Empty
#*<li>Rule 100:  nonTermList ::= nonTermList nonTerm
 *</b>
 */'''
class nonTermList ( AbstractASTNodeList, InonTermList):
    
        def  getnonTermAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(nonTermList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def nonTermListfromElement(element,left_recursive)  :
        
            obj = nonTermList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _nonTerm): 
        
            super(nonTermList, self).addElement( _nonTerm)
            _nonTerm.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getnonTermAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 101:  nonTerm ::= ruleNameWithAttributes produces ruleList
 *</b>
 */'''
class nonTerm ( ASTNode ,InonTerm):
    

        def  getruleNameWithAttributes(self)  :  return self._ruleNameWithAttributes
        def  setruleNameWithAttributes(self,  _ruleNameWithAttributes) :   self._ruleNameWithAttributes = _ruleNameWithAttributes
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getruleList(self)  :  return self._ruleList
        def  setruleList(self,  _ruleList) :   self._ruleList = _ruleList

        __slots__ = ('_ruleNameWithAttributes', '_produces', '_ruleList')

        def __init__(self, leftIToken, rightIToken,
                             _ruleNameWithAttributes,
                             _produces,
                             _ruleList):
        
            super(nonTerm, self).__init__(leftIToken, rightIToken)

            self._ruleNameWithAttributes = _ruleNameWithAttributes
            _ruleNameWithAttributes.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._ruleList = _ruleList
            _ruleList.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ruleNameWithAttributes:  _content.add(self._ruleNameWithAttributes)
            if self._produces:  _content.add(self._produces)
            if self._ruleList:  _content.add(self._ruleList)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitnonTerm(self)
            if checkChildren:
            
                self._ruleNameWithAttributes.accept(v)
                self._produces.accept(v)
                self._ruleList.accept(v)
            
            v.endVisitnonTerm(self)
        
    

'''/**
 *<b>
#*<li>Rule 102:  ruleNameWithAttributes ::= SYMBOL
#*<li>Rule 103:  ruleNameWithAttributes ::= SYMBOL MACRO_NAME$className
#*<li>Rule 104:  ruleNameWithAttributes ::= SYMBOL MACRO_NAME$className MACRO_NAME$arrayElement
 *</b>
 */'''
class RuleName ( ASTNode, IruleNameWithAttributes):
    

        def  getSYMBOL(self)  : return self._SYMBOL
        '''/**
         * The value returned by <b>getclassName</b> may be <b>null</b>
         */'''
        def  getclassName(self)  : return self._className
        '''/**
         * The value returned by <b>getarrayElement</b> may be <b>null</b>
         */'''
        def  getarrayElement(self)  : return self._arrayElement

        __slots__ = ('_SYMBOL', '_className', '_arrayElement')

        def __init__(self,leftIToken  , rightIToken  ,
                            _SYMBOL,
                            _className,
                            _arrayElement):
        
            super(RuleName, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._className = _className
            if (_className): _className.setParent(self)
            self._arrayElement = _arrayElement
            if (_arrayElement): _arrayElement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._className:  _content.add(self._className)
            if self._arrayElement:  _content.add(self._arrayElement)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitRuleName(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                if self._className: self._className.accept(v)
                if self._arrayElement: self._arrayElement.accept(v)
            
            v.endVisitRuleName(self)
        
    

'''/**
 *<b>
#*<li>Rule 105:  ruleList ::= rule
#*<li>Rule 106:  ruleList ::= ruleList |$ rule
 *</b>
 */'''
class ruleList ( AbstractASTNodeList, IruleList):
    
        def  getruleAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(ruleList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def ruleListfromElement(element,left_recursive)  :
        
            obj = ruleList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _rule): 
        
            super(ruleList, self).addElement( _rule)
            _rule.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getruleAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 111:  rule ::= symWithAttrsList opt_action_segment
 *</b>
 */'''
class rule ( ASTNode ,Irule):
    

        def  getsymWithAttrsList(self)  :  return self._symWithAttrsList
        def  setsymWithAttrsList(self,  _symWithAttrsList) :   self._symWithAttrsList = _symWithAttrsList
        '''/**
         * The value returned by <b>getopt_action_segment</b> may be <b>null</b>
         */'''
        def  getopt_action_segment(self)  :  return self._opt_action_segment
        def  setopt_action_segment(self,  _opt_action_segment) :   self._opt_action_segment = _opt_action_segment

        __slots__ = ('_symWithAttrsList', '_opt_action_segment')

        def __init__(self, leftIToken, rightIToken,
                             _symWithAttrsList,
                             _opt_action_segment):
        
            super(rule, self).__init__(leftIToken, rightIToken)

            self._symWithAttrsList = _symWithAttrsList
            _symWithAttrsList.setParent(self)
            self._opt_action_segment = _opt_action_segment
            if _opt_action_segment: _opt_action_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._symWithAttrsList:  _content.add(self._symWithAttrsList)
            if self._opt_action_segment:  _content.add(self._opt_action_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitrule(self)
            if checkChildren:
            
                self._symWithAttrsList.accept(v)
                if self._opt_action_segment: self._opt_action_segment.accept(v)
            
            v.endVisitrule(self)
        
    

'''/**
 *<b>
#*<li>Rule 112:  symWithAttrsList ::= $Empty
#*<li>Rule 113:  symWithAttrsList ::= symWithAttrsList symWithAttrs
 *</b>
 */'''
class symWithAttrsList ( AbstractASTNodeList, IsymWithAttrsList):
    
        def  getsymWithAttrsAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(symWithAttrsList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def symWithAttrsListfromElement(element,left_recursive)  :
        
            obj = symWithAttrsList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _symWithAttrs): 
        
            super(symWithAttrsList, self).addElement( _symWithAttrs)
            _symWithAttrs.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getsymWithAttrsAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 116:  optAttrList ::= $Empty
#*<li>Rule 117:  optAttrList ::= MACRO_NAME
 *</b>
 */'''
class symAttrs ( ASTNode, IoptAttrList):
    

        '''/**
         * The value returned by <b>getMACRO_NAME</b> may be <b>null</b>
         */'''
        def  getMACRO_NAME(self)  : return self._MACRO_NAME

        __slots__ = '_MACRO_NAME'

        def __init__(self,leftIToken  , rightIToken  ,
                            _MACRO_NAME):
        
            super(symAttrs, self).__init__(leftIToken, rightIToken)

            self._MACRO_NAME = _MACRO_NAME
            if (_MACRO_NAME): _MACRO_NAME.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MACRO_NAME:  _content.add(self._MACRO_NAME)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitsymAttrs(self)
            if checkChildren:
                if self._MACRO_NAME: self._MACRO_NAME.accept(v)
            v.endVisitsymAttrs(self)
        
    

'''/**
 *<b>
#*<li>Rule 120:  action_segment ::= BLOCK
 *</b>
 */'''
class action_segment ( ASTNodeToken ,Iaction_segment):
    
        def getEnvironment(self): return self.environment

        def  getBLOCK(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,environment , token  ):        
            super(action_segment, self).__init__(token)
            self.environment = environment
            self.initialize()
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitaction_segment(self)
            v.endVisitaction_segment(self)
        
    

'''/**
 *<b>
#*<li>Rule 121:  start_segment ::= start_symbol
#*<li>Rule 122:  start_segment ::= start_segment start_symbol
 *</b>
 */'''
class start_symbolList ( AbstractASTNodeList, Istart_segment):
    
        def  getstart_symbolAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(start_symbolList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def start_symbolListfromElement(element,left_recursive)  :
        
            obj = start_symbolList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _start_symbol): 
        
            super(start_symbolList, self).addElement( _start_symbol)
            _start_symbol.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getstart_symbolAt(i)
                    element.accept(v)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 125:  terminals_segment ::= terminal
#*<li>Rule 126:  terminals_segment ::= terminals_segment terminal
 *</b>
 */'''
class terminalList ( AbstractASTNodeList, Iterminals_segment):
    
        def  getterminalAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(terminalList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def terminalListfromElement(element,left_recursive)  :
        
            obj = terminalList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _terminal): 
        
            super(terminalList, self).addElement( _terminal)
            _terminal.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getterminalAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 127:  terminal ::= terminal_symbol optTerminalAlias
 *</b>
 */'''
class terminal ( ASTNode ,Iterminal):
    

        def  getterminal_symbol(self)  :  return self._terminal_symbol
        def  setterminal_symbol(self,  _terminal_symbol) :   self._terminal_symbol = _terminal_symbol
        '''/**
         * The value returned by <b>getoptTerminalAlias</b> may be <b>null</b>
         */'''
        def  getoptTerminalAlias(self)  :  return self._optTerminalAlias
        def  setoptTerminalAlias(self,  _optTerminalAlias) :   self._optTerminalAlias = _optTerminalAlias

        __slots__ = ('_terminal_symbol', '_optTerminalAlias')

        def __init__(self, leftIToken, rightIToken,
                             _terminal_symbol,
                             _optTerminalAlias):
        
            super(terminal, self).__init__(leftIToken, rightIToken)

            self._terminal_symbol = _terminal_symbol
            _terminal_symbol.setParent(self)
            self._optTerminalAlias = _optTerminalAlias
            if _optTerminalAlias: _optTerminalAlias.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._terminal_symbol:  _content.add(self._terminal_symbol)
            if self._optTerminalAlias:  _content.add(self._optTerminalAlias)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitterminal(self)
            if checkChildren:
            
                self._terminal_symbol.accept(v)
                if self._optTerminalAlias: self._optTerminalAlias.accept(v)
            
            v.endVisitterminal(self)
        
    

'''/**
 *<em>
#*<li>Rule 128:  optTerminalAlias ::= $Empty
 *</em>
 *<p>
 *<b>
#*<li>Rule 129:  optTerminalAlias ::= produces name
 *</b>
 */'''
class optTerminalAlias ( ASTNode ,IoptTerminalAlias):
    

        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getname(self)  :  return self._name
        def  setname(self,  _name) :   self._name = _name

        __slots__ = ('_produces', '_name')

        def __init__(self, leftIToken, rightIToken,
                             _produces,
                             _name):
        
            super(optTerminalAlias, self).__init__(leftIToken, rightIToken)

            self._produces = _produces
            _produces.setParent(self)
            self._name = _name
            _name.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._produces:  _content.add(self._produces)
            if self._name:  _content.add(self._name)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitoptTerminalAlias(self)
            if checkChildren:
            
                self._produces.accept(v)
                self._name.accept(v)
            
            v.endVisitoptTerminalAlias(self)
        
    

'''/**
 *<b>
#*<li>Rule 133:  types_segment ::= type_declarations
#*<li>Rule 134:  types_segment ::= types_segment type_declarations
 *</b>
 */'''
class type_declarationsList ( AbstractASTNodeList, Itypes_segment):
    
        def  gettype_declarationsAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(type_declarationsList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def type_declarationsListfromElement(element,left_recursive)  :
        
            obj = type_declarationsList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _type_declarations): 
        
            super(type_declarationsList, self).addElement( _type_declarations)
            _type_declarations.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.gettype_declarationsAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 135:  type_declarations ::= SYMBOL produces barSymbolList opt_action_segment
 *</b>
 */'''
class type_declarations ( ASTNode ,Itype_declarations):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getbarSymbolList(self)  :  return self._barSymbolList
        def  setbarSymbolList(self,  _barSymbolList) :   self._barSymbolList = _barSymbolList
        '''/**
         * The value returned by <b>getopt_action_segment</b> may be <b>null</b>
         */'''
        def  getopt_action_segment(self)  :  return self._opt_action_segment
        def  setopt_action_segment(self,  _opt_action_segment) :   self._opt_action_segment = _opt_action_segment

        __slots__ = ('_SYMBOL', '_produces', '_barSymbolList', '_opt_action_segment')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _produces,
                             _barSymbolList,
                             _opt_action_segment):
        
            super(type_declarations, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._barSymbolList = _barSymbolList
            _barSymbolList.setParent(self)
            self._opt_action_segment = _opt_action_segment
            if _opt_action_segment: _opt_action_segment.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._produces:  _content.add(self._produces)
            if self._barSymbolList:  _content.add(self._barSymbolList)
            if self._opt_action_segment:  _content.add(self._opt_action_segment)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visittype_declarations(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                self._produces.accept(v)
                self._barSymbolList.accept(v)
                if self._opt_action_segment: self._opt_action_segment.accept(v)
            
            v.endVisittype_declarations(self)
        
    

'''/**
 *<b>
#*<li>Rule 138:  predecessor_segment ::= $Empty
#*<li>Rule 139:  predecessor_segment ::= predecessor_segment symbol_pair
 *</b>
 */'''
class symbol_pairList ( AbstractASTNodeList, Ipredecessor_segment):
    
        def  getsymbol_pairAt(self, i): return  self.getElementAt(i)

        __slots__ = ()
        def __init__(self,leftToken, rightToken, left_recursive):
        
            super(symbol_pairList, self).__init__(leftToken, rightToken, left_recursive)
        

        @staticmethod
        def symbol_pairListfromElement(element,left_recursive)  :
        
            obj = symbol_pairList(element.getLeftIToken(),element.getRightIToken(), left_recursive)
            obj._content.add(element)
            element.setParent(obj)
            return obj
        

        def  addElement(self,  _symbol_pair): 
        
            super(symbol_pairList, self).addElement( _symbol_pair)
            _symbol_pair.setParent(self)
        


        def  accept(self, v) : 
        
            if (not v.preVisit(self)): return
            self.enter( v)
            v.postVisit(self)
        
        def enter(self, v) : 
        
            checkChildren = v.visit(self)
            if checkChildren:
            
                for i in range(self.size()):
                
                    element = self.getsymbol_pairAt(i)
                    if not v.preVisit(element): continue
                    element.enter(v)
                    v.postVisit(element)
                
            
            v.endVisit(self)
        
    

'''/**
 *<b>
#*<li>Rule 140:  symbol_pair ::= SYMBOL SYMBOL
 *</b>
 */'''
class symbol_pair ( ASTNode ,Isymbol_pair):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        def  getSYMBOL2(self)  :  return self._SYMBOL2
        def  setSYMBOL2(self,  _SYMBOL2) :   self._SYMBOL2 = _SYMBOL2

        __slots__ = ('_SYMBOL', '_SYMBOL2')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _SYMBOL2):
        
            super(symbol_pair, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._SYMBOL2 = _SYMBOL2
            _SYMBOL2.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._SYMBOL2:  _content.add(self._SYMBOL2)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitsymbol_pair(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                self._SYMBOL2.accept(v)
            
            v.endVisitsymbol_pair(self)
        
    

'''/**
 *<b>
#*<li>Rule 143:  recover_symbol ::= SYMBOL
 *</b>
 */'''
class recover_symbol ( ASTNodeToken ,Irecover_symbol):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(recover_symbol, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitrecover_symbol(self)
            v.endVisitrecover_symbol(self)
        
    

'''/**
 *<em>
#*<li>Rule 144:  END_KEY_OPT ::= $Empty
 *</em>
 *<p>
 *<b>
#*<li>Rule 145:  END_KEY_OPT ::= END_KEY
 *</b>
 */'''
class END_KEY_OPT ( ASTNodeToken ,IEND_KEY_OPT):
    
        def  getEND_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(END_KEY_OPT, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitEND_KEY_OPT(self)
            v.endVisitEND_KEY_OPT(self)
        
    

'''/**
 *<b>
#*<li>Rule 34:  option_value ::= =$ SYMBOL
 *</b>
 */'''
class option_value0 ( ASTNode ,Ioption_value):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL

        __slots__ = '_SYMBOL'

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL):
        
            super(option_value0, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitoption_value0(self)
            if checkChildren:
                self._SYMBOL.accept(v)
            v.endVisitoption_value0(self)
        
    

'''/**
 *<b>
#*<li>Rule 35:  option_value ::= =$ ($ symbol_list )$
 *</b>
 */'''
class option_value1 ( ASTNode ,Ioption_value):
    

        def  getsymbol_list(self)  :  return self._symbol_list
        def  setsymbol_list(self,  _symbol_list) :   self._symbol_list = _symbol_list

        __slots__ = '_symbol_list'

        def __init__(self, leftIToken, rightIToken,
                             _symbol_list):
        
            super(option_value1, self).__init__(leftIToken, rightIToken)

            self._symbol_list = _symbol_list
            _symbol_list.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._symbol_list:  _content.add(self._symbol_list)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitoption_value1(self)
            if checkChildren:
                self._symbol_list.accept(v)
            v.endVisitoption_value1(self)
        
    

'''/**
 *<b>
#*<li>Rule 40:  aliasSpec ::= ERROR_KEY produces alias_rhs
 *</b>
 */'''
class aliasSpec0 ( ASTNode ,IaliasSpec):
    

        def  getERROR_KEY(self)  :  return self._ERROR_KEY
        def  setERROR_KEY(self,  _ERROR_KEY) :   self._ERROR_KEY = _ERROR_KEY
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getalias_rhs(self)  :  return self._alias_rhs
        def  setalias_rhs(self,  _alias_rhs) :   self._alias_rhs = _alias_rhs

        __slots__ = ('_ERROR_KEY', '_produces', '_alias_rhs')

        def __init__(self, leftIToken, rightIToken,
                             _ERROR_KEY,
                             _produces,
                             _alias_rhs):
        
            super(aliasSpec0, self).__init__(leftIToken, rightIToken)

            self._ERROR_KEY = _ERROR_KEY
            _ERROR_KEY.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._alias_rhs = _alias_rhs
            _alias_rhs.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ERROR_KEY:  _content.add(self._ERROR_KEY)
            if self._produces:  _content.add(self._produces)
            if self._alias_rhs:  _content.add(self._alias_rhs)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitaliasSpec0(self)
            if checkChildren:
            
                self._ERROR_KEY.accept(v)
                self._produces.accept(v)
                self._alias_rhs.accept(v)
            
            v.endVisitaliasSpec0(self)
        
    

'''/**
 *<b>
#*<li>Rule 41:  aliasSpec ::= EOL_KEY produces alias_rhs
 *</b>
 */'''
class aliasSpec1 ( ASTNode ,IaliasSpec):
    

        def  getEOL_KEY(self)  :  return self._EOL_KEY
        def  setEOL_KEY(self,  _EOL_KEY) :   self._EOL_KEY = _EOL_KEY
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getalias_rhs(self)  :  return self._alias_rhs
        def  setalias_rhs(self,  _alias_rhs) :   self._alias_rhs = _alias_rhs

        __slots__ = ('_EOL_KEY', '_produces', '_alias_rhs')

        def __init__(self, leftIToken, rightIToken,
                             _EOL_KEY,
                             _produces,
                             _alias_rhs):
        
            super(aliasSpec1, self).__init__(leftIToken, rightIToken)

            self._EOL_KEY = _EOL_KEY
            _EOL_KEY.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._alias_rhs = _alias_rhs
            _alias_rhs.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._EOL_KEY:  _content.add(self._EOL_KEY)
            if self._produces:  _content.add(self._produces)
            if self._alias_rhs:  _content.add(self._alias_rhs)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitaliasSpec1(self)
            if checkChildren:
            
                self._EOL_KEY.accept(v)
                self._produces.accept(v)
                self._alias_rhs.accept(v)
            
            v.endVisitaliasSpec1(self)
        
    

'''/**
 *<b>
#*<li>Rule 42:  aliasSpec ::= EOF_KEY produces alias_rhs
 *</b>
 */'''
class aliasSpec2 ( ASTNode ,IaliasSpec):
    

        def  getEOF_KEY(self)  :  return self._EOF_KEY
        def  setEOF_KEY(self,  _EOF_KEY) :   self._EOF_KEY = _EOF_KEY
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getalias_rhs(self)  :  return self._alias_rhs
        def  setalias_rhs(self,  _alias_rhs) :   self._alias_rhs = _alias_rhs

        __slots__ = ('_EOF_KEY', '_produces', '_alias_rhs')

        def __init__(self, leftIToken, rightIToken,
                             _EOF_KEY,
                             _produces,
                             _alias_rhs):
        
            super(aliasSpec2, self).__init__(leftIToken, rightIToken)

            self._EOF_KEY = _EOF_KEY
            _EOF_KEY.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._alias_rhs = _alias_rhs
            _alias_rhs.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._EOF_KEY:  _content.add(self._EOF_KEY)
            if self._produces:  _content.add(self._produces)
            if self._alias_rhs:  _content.add(self._alias_rhs)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitaliasSpec2(self)
            if checkChildren:
            
                self._EOF_KEY.accept(v)
                self._produces.accept(v)
                self._alias_rhs.accept(v)
            
            v.endVisitaliasSpec2(self)
        
    

'''/**
 *<b>
#*<li>Rule 43:  aliasSpec ::= IDENTIFIER_KEY produces alias_rhs
 *</b>
 */'''
class aliasSpec3 ( ASTNode ,IaliasSpec):
    

        def  getIDENTIFIER_KEY(self)  :  return self._IDENTIFIER_KEY
        def  setIDENTIFIER_KEY(self,  _IDENTIFIER_KEY) :   self._IDENTIFIER_KEY = _IDENTIFIER_KEY
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getalias_rhs(self)  :  return self._alias_rhs
        def  setalias_rhs(self,  _alias_rhs) :   self._alias_rhs = _alias_rhs

        __slots__ = ('_IDENTIFIER_KEY', '_produces', '_alias_rhs')

        def __init__(self, leftIToken, rightIToken,
                             _IDENTIFIER_KEY,
                             _produces,
                             _alias_rhs):
        
            super(aliasSpec3, self).__init__(leftIToken, rightIToken)

            self._IDENTIFIER_KEY = _IDENTIFIER_KEY
            _IDENTIFIER_KEY.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._alias_rhs = _alias_rhs
            _alias_rhs.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._IDENTIFIER_KEY:  _content.add(self._IDENTIFIER_KEY)
            if self._produces:  _content.add(self._produces)
            if self._alias_rhs:  _content.add(self._alias_rhs)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitaliasSpec3(self)
            if checkChildren:
            
                self._IDENTIFIER_KEY.accept(v)
                self._produces.accept(v)
                self._alias_rhs.accept(v)
            
            v.endVisitaliasSpec3(self)
        
    

'''/**
 *<b>
#*<li>Rule 44:  aliasSpec ::= SYMBOL produces alias_rhs
 *</b>
 */'''
class aliasSpec4 ( ASTNode ,IaliasSpec):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getalias_rhs(self)  :  return self._alias_rhs
        def  setalias_rhs(self,  _alias_rhs) :   self._alias_rhs = _alias_rhs

        __slots__ = ('_SYMBOL', '_produces', '_alias_rhs')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _produces,
                             _alias_rhs):
        
            super(aliasSpec4, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._alias_rhs = _alias_rhs
            _alias_rhs.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._produces:  _content.add(self._produces)
            if self._alias_rhs:  _content.add(self._alias_rhs)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitaliasSpec4(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                self._produces.accept(v)
                self._alias_rhs.accept(v)
            
            v.endVisitaliasSpec4(self)
        
    

'''/**
 *<b>
#*<li>Rule 45:  aliasSpec ::= alias_lhs_macro_name produces alias_rhs
 *</b>
 */'''
class aliasSpec5 ( ASTNode ,IaliasSpec):
    

        def  getalias_lhs_macro_name(self)  :  return self._alias_lhs_macro_name
        def  setalias_lhs_macro_name(self,  _alias_lhs_macro_name) :   self._alias_lhs_macro_name = _alias_lhs_macro_name
        def  getproduces(self)  :  return self._produces
        def  setproduces(self,  _produces) :   self._produces = _produces
        def  getalias_rhs(self)  :  return self._alias_rhs
        def  setalias_rhs(self,  _alias_rhs) :   self._alias_rhs = _alias_rhs

        __slots__ = ('_alias_lhs_macro_name', '_produces', '_alias_rhs')

        def __init__(self, leftIToken, rightIToken,
                             _alias_lhs_macro_name,
                             _produces,
                             _alias_rhs):
        
            super(aliasSpec5, self).__init__(leftIToken, rightIToken)

            self._alias_lhs_macro_name = _alias_lhs_macro_name
            _alias_lhs_macro_name.setParent(self)
            self._produces = _produces
            _produces.setParent(self)
            self._alias_rhs = _alias_rhs
            _alias_rhs.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._alias_lhs_macro_name:  _content.add(self._alias_lhs_macro_name)
            if self._produces:  _content.add(self._produces)
            if self._alias_rhs:  _content.add(self._alias_rhs)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitaliasSpec5(self)
            if checkChildren:
            
                self._alias_lhs_macro_name.accept(v)
                self._produces.accept(v)
                self._alias_rhs.accept(v)
            
            v.endVisitaliasSpec5(self)
        
    

'''/**
 *<b>
#*<li>Rule 47:  alias_rhs ::= SYMBOL
 *</b>
 */'''
class alias_rhs0 ( ASTNodeToken ,Ialias_rhs):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs0(self)
            v.endVisitalias_rhs0(self)
        
    

'''/**
 *<b>
#*<li>Rule 48:  alias_rhs ::= MACRO_NAME
 *</b>
 */'''
class alias_rhs1 ( ASTNodeToken ,Ialias_rhs):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs1, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs1(self)
            v.endVisitalias_rhs1(self)
        
    

'''/**
 *<b>
#*<li>Rule 49:  alias_rhs ::= ERROR_KEY
 *</b>
 */'''
class alias_rhs2 ( ASTNodeToken ,Ialias_rhs):
    
        def  getERROR_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs2, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs2(self)
            v.endVisitalias_rhs2(self)
        
    

'''/**
 *<b>
#*<li>Rule 50:  alias_rhs ::= EOL_KEY
 *</b>
 */'''
class alias_rhs3 ( ASTNodeToken ,Ialias_rhs):
    
        def  getEOL_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs3, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs3(self)
            v.endVisitalias_rhs3(self)
        
    

'''/**
 *<b>
#*<li>Rule 51:  alias_rhs ::= EOF_KEY
 *</b>
 */'''
class alias_rhs4 ( ASTNodeToken ,Ialias_rhs):
    
        def  getEOF_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs4, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs4(self)
            v.endVisitalias_rhs4(self)
        
    

'''/**
 *<b>
#*<li>Rule 52:  alias_rhs ::= EMPTY_KEY
 *</b>
 */'''
class alias_rhs5 ( ASTNodeToken ,Ialias_rhs):
    
        def  getEMPTY_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs5, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs5(self)
            v.endVisitalias_rhs5(self)
        
    

'''/**
 *<b>
#*<li>Rule 53:  alias_rhs ::= IDENTIFIER_KEY
 *</b>
 */'''
class alias_rhs6 ( ASTNodeToken ,Ialias_rhs):
    
        def  getIDENTIFIER_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(alias_rhs6, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitalias_rhs6(self)
            v.endVisitalias_rhs6(self)
        
    

'''/**
 *<b>
#*<li>Rule 58:  macro_name_symbol ::= MACRO_NAME
 *</b>
 */'''
class macro_name_symbol0 ( ASTNodeToken ,Imacro_name_symbol):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(macro_name_symbol0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitmacro_name_symbol0(self)
            v.endVisitmacro_name_symbol0(self)
        
    

'''/**
 *<b>
#*<li>Rule 59:  macro_name_symbol ::= SYMBOL
 *</b>
 */'''
class macro_name_symbol1 ( ASTNodeToken ,Imacro_name_symbol):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(macro_name_symbol1, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitmacro_name_symbol1(self)
            v.endVisitmacro_name_symbol1(self)
        
    

'''/**
 *<b>
#*<li>Rule 73:  drop_command ::= DROPSYMBOLS_KEY drop_symbols
 *</b>
 */'''
class drop_command0 ( ASTNode ,Idrop_command):
    

        def  getDROPSYMBOLS_KEY(self)  :  return self._DROPSYMBOLS_KEY
        def  setDROPSYMBOLS_KEY(self,  _DROPSYMBOLS_KEY) :   self._DROPSYMBOLS_KEY = _DROPSYMBOLS_KEY
        def  getdrop_symbols(self)  :  return self._drop_symbols
        def  setdrop_symbols(self,  _drop_symbols) :   self._drop_symbols = _drop_symbols

        __slots__ = ('_DROPSYMBOLS_KEY', '_drop_symbols')

        def __init__(self, leftIToken, rightIToken,
                             _DROPSYMBOLS_KEY,
                             _drop_symbols):
        
            super(drop_command0, self).__init__(leftIToken, rightIToken)

            self._DROPSYMBOLS_KEY = _DROPSYMBOLS_KEY
            _DROPSYMBOLS_KEY.setParent(self)
            self._drop_symbols = _drop_symbols
            _drop_symbols.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._DROPSYMBOLS_KEY:  _content.add(self._DROPSYMBOLS_KEY)
            if self._drop_symbols:  _content.add(self._drop_symbols)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitdrop_command0(self)
            if checkChildren:
            
                self._DROPSYMBOLS_KEY.accept(v)
                self._drop_symbols.accept(v)
            
            v.endVisitdrop_command0(self)
        
    

'''/**
 *<b>
#*<li>Rule 74:  drop_command ::= DROPRULES_KEY drop_rules
 *</b>
 */'''
class drop_command1 ( ASTNode ,Idrop_command):
    

        def  getDROPRULES_KEY(self)  :  return self._DROPRULES_KEY
        def  setDROPRULES_KEY(self,  _DROPRULES_KEY) :   self._DROPRULES_KEY = _DROPRULES_KEY
        def  getdrop_rules(self)  :  return self._drop_rules
        def  setdrop_rules(self,  _drop_rules) :   self._drop_rules = _drop_rules

        __slots__ = ('_DROPRULES_KEY', '_drop_rules')

        def __init__(self, leftIToken, rightIToken,
                             _DROPRULES_KEY,
                             _drop_rules):
        
            super(drop_command1, self).__init__(leftIToken, rightIToken)

            self._DROPRULES_KEY = _DROPRULES_KEY
            _DROPRULES_KEY.setParent(self)
            self._drop_rules = _drop_rules
            _drop_rules.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._DROPRULES_KEY:  _content.add(self._DROPRULES_KEY)
            if self._drop_rules:  _content.add(self._drop_rules)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitdrop_command1(self)
            if checkChildren:
            
                self._DROPRULES_KEY.accept(v)
                self._drop_rules.accept(v)
            
            v.endVisitdrop_command1(self)
        
    

'''/**
 *<b>
#*<li>Rule 90:  name ::= SYMBOL
 *</b>
 */'''
class name0 ( ASTNodeToken ,Iname):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(name0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitname0(self)
            v.endVisitname0(self)
        
    

'''/**
 *<b>
#*<li>Rule 91:  name ::= MACRO_NAME
 *</b>
 */'''
class name1 ( ASTNodeToken ,Iname):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(name1, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitname1(self)
            v.endVisitname1(self)
        
    

'''/**
 *<b>
#*<li>Rule 92:  name ::= EMPTY_KEY
 *</b>
 */'''
class name2 ( ASTNodeToken ,Iname):
    
        def  getEMPTY_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(name2, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitname2(self)
            v.endVisitname2(self)
        
    

'''/**
 *<b>
#*<li>Rule 93:  name ::= ERROR_KEY
 *</b>
 */'''
class name3 ( ASTNodeToken ,Iname):
    
        def  getERROR_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(name3, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitname3(self)
            v.endVisitname3(self)
        
    

'''/**
 *<b>
#*<li>Rule 94:  name ::= EOL_KEY
 *</b>
 */'''
class name4 ( ASTNodeToken ,Iname):
    
        def  getEOL_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(name4, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitname4(self)
            v.endVisitname4(self)
        
    

'''/**
 *<b>
#*<li>Rule 95:  name ::= IDENTIFIER_KEY
 *</b>
 */'''
class name5 ( ASTNodeToken ,Iname):
    
        def  getIDENTIFIER_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(name5, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitname5(self)
            v.endVisitname5(self)
        
    

'''/**
 *<b>
#*<li>Rule 107:  produces ::= ::=
 *</b>
 */'''
class produces0 ( ASTNodeToken ,Iproduces):
    
        def  getEQUIVALENCE(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(produces0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitproduces0(self)
            v.endVisitproduces0(self)
        
    

'''/**
 *<b>
#*<li>Rule 108:  produces ::= ::=?
 *</b>
 */'''
class produces1 ( ASTNodeToken ,Iproduces):
    
        def  getPRIORITY_EQUIVALENCE(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(produces1, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitproduces1(self)
            v.endVisitproduces1(self)
        
    

'''/**
 *<b>
#*<li>Rule 109:  produces ::= ->
 *</b>
 */'''
class produces2 ( ASTNodeToken ,Iproduces):
    
        def  getARROW(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(produces2, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitproduces2(self)
            v.endVisitproduces2(self)
        
    

'''/**
 *<b>
#*<li>Rule 110:  produces ::= ->?
 *</b>
 */'''
class produces3 ( ASTNodeToken ,Iproduces):
    
        def  getPRIORITY_ARROW(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(produces3, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitproduces3(self)
            v.endVisitproduces3(self)
        
    

'''/**
 *<b>
#*<li>Rule 114:  symWithAttrs ::= EMPTY_KEY
 *</b>
 */'''
class symWithAttrs0 ( ASTNodeToken ,IsymWithAttrs):
    
        def  getEMPTY_KEY(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(symWithAttrs0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitsymWithAttrs0(self)
            v.endVisitsymWithAttrs0(self)
        
    

'''/**
 *<b>
#*<li>Rule 115:  symWithAttrs ::= SYMBOL optAttrList
 *</b>
 */'''
class symWithAttrs1 ( ASTNode ,IsymWithAttrs):
    

        def  getSYMBOL(self)  :  return self._SYMBOL
        def  setSYMBOL(self,  _SYMBOL) :   self._SYMBOL = _SYMBOL
        '''/**
         * The value returned by <b>getoptAttrList</b> may be <b>null</b>
         */'''
        def  getoptAttrList(self)  :  return self._optAttrList
        def  setoptAttrList(self,  _optAttrList) :   self._optAttrList = _optAttrList

        __slots__ = ('_SYMBOL', '_optAttrList')

        def __init__(self, leftIToken, rightIToken,
                             _SYMBOL,
                             _optAttrList):
        
            super(symWithAttrs1, self).__init__(leftIToken, rightIToken)

            self._SYMBOL = _SYMBOL
            _SYMBOL.setParent(self)
            self._optAttrList = _optAttrList
            if _optAttrList: _optAttrList.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SYMBOL:  _content.add(self._SYMBOL)
            if self._optAttrList:  _content.add(self._optAttrList)
            return _content
        

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            checkChildren = v.visitsymWithAttrs1(self)
            if checkChildren:
            
                self._SYMBOL.accept(v)
                if self._optAttrList: self._optAttrList.accept(v)
            
            v.endVisitsymWithAttrs1(self)
        
    

'''/**
 *<b>
#*<li>Rule 123:  start_symbol ::= SYMBOL
 *</b>
 */'''
class start_symbol0 ( ASTNodeToken ,Istart_symbol):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(start_symbol0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitstart_symbol0(self)
            v.endVisitstart_symbol0(self)
        
    

'''/**
 *<b>
#*<li>Rule 124:  start_symbol ::= MACRO_NAME
 *</b>
 */'''
class start_symbol1 ( ASTNodeToken ,Istart_symbol):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(start_symbol1, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitstart_symbol1(self)
            v.endVisitstart_symbol1(self)
        
    

'''/**
 *<b>
#*<li>Rule 130:  terminal_symbol ::= SYMBOL
 *</b>
 */'''
class terminal_symbol0 ( ASTNodeToken ,Iterminal_symbol):
    
        def  getSYMBOL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(terminal_symbol0, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitterminal_symbol0(self)
            v.endVisitterminal_symbol0(self)
        
    

'''/**
 *<b>
#*<li>Rule 131:  terminal_symbol ::= MACRO_NAME
 *</b>
 */'''
class terminal_symbol1 ( ASTNodeToken ,Iterminal_symbol):
    
        def  getMACRO_NAME(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(terminal_symbol1, self).__init__(token)
            self.initialize()

        def  accept(self, v ): 
        
            if not v.preVisit(self): return
            self.enter( v)
            v.postVisit(self)
        

        def  enter(self, v): 
        
            v.visitterminal_symbol1(self)
            v.endVisitterminal_symbol1(self)
        
    

class Visitor (IAstVisitor):
    
        __slots__ = ()
        def visit(self, n): pass
        def endVisit(self, n) : pass

        def visitASTNodeToken(self, n):pass
        def endVisitASTNodeToken(self, n): pass

        def visitLPG(self, n):pass
        def endVisitLPG(self, n): pass

        def visitLPG_itemList(self, n):pass
        def endVisitLPG_itemList(self, n): pass

        def visitAliasSeg(self, n):pass
        def endVisitAliasSeg(self, n): pass

        def visitAstSeg(self, n):pass
        def endVisitAstSeg(self, n): pass

        def visitDefineSeg(self, n):pass
        def endVisitDefineSeg(self, n): pass

        def visitEofSeg(self, n):pass
        def endVisitEofSeg(self, n): pass

        def visitEolSeg(self, n):pass
        def endVisitEolSeg(self, n): pass

        def visitErrorSeg(self, n):pass
        def endVisitErrorSeg(self, n): pass

        def visitExportSeg(self, n):pass
        def endVisitExportSeg(self, n): pass

        def visitGlobalsSeg(self, n):pass
        def endVisitGlobalsSeg(self, n): pass

        def visitHeadersSeg(self, n):pass
        def endVisitHeadersSeg(self, n): pass

        def visitIdentifierSeg(self, n):pass
        def endVisitIdentifierSeg(self, n): pass

        def visitImportSeg(self, n):pass
        def endVisitImportSeg(self, n): pass

        def visitIncludeSeg(self, n):pass
        def endVisitIncludeSeg(self, n): pass

        def visitKeywordsSeg(self, n):pass
        def endVisitKeywordsSeg(self, n): pass

        def visitNamesSeg(self, n):pass
        def endVisitNamesSeg(self, n): pass

        def visitNoticeSeg(self, n):pass
        def endVisitNoticeSeg(self, n): pass

        def visitRulesSeg(self, n):pass
        def endVisitRulesSeg(self, n): pass

        def visitSoftKeywordsSeg(self, n):pass
        def endVisitSoftKeywordsSeg(self, n): pass

        def visitStartSeg(self, n):pass
        def endVisitStartSeg(self, n): pass

        def visitTerminalsSeg(self, n):pass
        def endVisitTerminalsSeg(self, n): pass

        def visitTrailersSeg(self, n):pass
        def endVisitTrailersSeg(self, n): pass

        def visitTypesSeg(self, n):pass
        def endVisitTypesSeg(self, n): pass

        def visitRecoverSeg(self, n):pass
        def endVisitRecoverSeg(self, n): pass

        def visitPredecessorSeg(self, n):pass
        def endVisitPredecessorSeg(self, n): pass

        def visitoption_specList(self, n):pass
        def endVisitoption_specList(self, n): pass

        def visitoption_spec(self, n):pass
        def endVisitoption_spec(self, n): pass

        def visitoptionList(self, n):pass
        def endVisitoptionList(self, n): pass

        def visitoption(self, n):pass
        def endVisitoption(self, n): pass

        def visitSYMBOLList(self, n):pass
        def endVisitSYMBOLList(self, n): pass

        def visitaliasSpecList(self, n):pass
        def endVisitaliasSpecList(self, n): pass

        def visitalias_lhs_macro_name(self, n):pass
        def endVisitalias_lhs_macro_name(self, n): pass

        def visitdefineSpecList(self, n):pass
        def endVisitdefineSpecList(self, n): pass

        def visitdefineSpec(self, n):pass
        def endVisitdefineSpec(self, n): pass

        def visitmacro_segment(self, n):pass
        def endVisitmacro_segment(self, n): pass

        def visitterminal_symbolList(self, n):pass
        def endVisitterminal_symbolList(self, n): pass

        def visitaction_segmentList(self, n):pass
        def endVisitaction_segmentList(self, n): pass

        def visitimport_segment(self, n):pass
        def endVisitimport_segment(self, n): pass

        def visitdrop_commandList(self, n):pass
        def endVisitdrop_commandList(self, n): pass

        def visitdrop_ruleList(self, n):pass
        def endVisitdrop_ruleList(self, n): pass

        def visitdrop_rule(self, n):pass
        def endVisitdrop_rule(self, n): pass

        def visitoptMacroName(self, n):pass
        def endVisitoptMacroName(self, n): pass

        def visitinclude_segment(self, n):pass
        def endVisitinclude_segment(self, n): pass

        def visitkeywordSpecList(self, n):pass
        def endVisitkeywordSpecList(self, n): pass

        def visitkeywordSpec(self, n):pass
        def endVisitkeywordSpec(self, n): pass

        def visitnameSpecList(self, n):pass
        def endVisitnameSpecList(self, n): pass

        def visitnameSpec(self, n):pass
        def endVisitnameSpec(self, n): pass

        def visitrules_segment(self, n):pass
        def endVisitrules_segment(self, n): pass

        def visitnonTermList(self, n):pass
        def endVisitnonTermList(self, n): pass

        def visitnonTerm(self, n):pass
        def endVisitnonTerm(self, n): pass

        def visitRuleName(self, n):pass
        def endVisitRuleName(self, n): pass

        def visitruleList(self, n):pass
        def endVisitruleList(self, n): pass

        def visitrule(self, n):pass
        def endVisitrule(self, n): pass

        def visitsymWithAttrsList(self, n):pass
        def endVisitsymWithAttrsList(self, n): pass

        def visitsymAttrs(self, n):pass
        def endVisitsymAttrs(self, n): pass

        def visitaction_segment(self, n):pass
        def endVisitaction_segment(self, n): pass

        def visitstart_symbolList(self, n):pass
        def endVisitstart_symbolList(self, n): pass

        def visitterminalList(self, n):pass
        def endVisitterminalList(self, n): pass

        def visitterminal(self, n):pass
        def endVisitterminal(self, n): pass

        def visitoptTerminalAlias(self, n):pass
        def endVisitoptTerminalAlias(self, n): pass

        def visittype_declarationsList(self, n):pass
        def endVisittype_declarationsList(self, n): pass

        def visittype_declarations(self, n):pass
        def endVisittype_declarations(self, n): pass

        def visitsymbol_pairList(self, n):pass
        def endVisitsymbol_pairList(self, n): pass

        def visitsymbol_pair(self, n):pass
        def endVisitsymbol_pair(self, n): pass

        def visitrecover_symbol(self, n):pass
        def endVisitrecover_symbol(self, n): pass

        def visitEND_KEY_OPT(self, n):pass
        def endVisitEND_KEY_OPT(self, n): pass

        def visitoption_value0(self, n):pass
        def endVisitoption_value0(self, n): pass

        def visitoption_value1(self, n):pass
        def endVisitoption_value1(self, n): pass

        def visitaliasSpec0(self, n):pass
        def endVisitaliasSpec0(self, n): pass

        def visitaliasSpec1(self, n):pass
        def endVisitaliasSpec1(self, n): pass

        def visitaliasSpec2(self, n):pass
        def endVisitaliasSpec2(self, n): pass

        def visitaliasSpec3(self, n):pass
        def endVisitaliasSpec3(self, n): pass

        def visitaliasSpec4(self, n):pass
        def endVisitaliasSpec4(self, n): pass

        def visitaliasSpec5(self, n):pass
        def endVisitaliasSpec5(self, n): pass

        def visitalias_rhs0(self, n):pass
        def endVisitalias_rhs0(self, n): pass

        def visitalias_rhs1(self, n):pass
        def endVisitalias_rhs1(self, n): pass

        def visitalias_rhs2(self, n):pass
        def endVisitalias_rhs2(self, n): pass

        def visitalias_rhs3(self, n):pass
        def endVisitalias_rhs3(self, n): pass

        def visitalias_rhs4(self, n):pass
        def endVisitalias_rhs4(self, n): pass

        def visitalias_rhs5(self, n):pass
        def endVisitalias_rhs5(self, n): pass

        def visitalias_rhs6(self, n):pass
        def endVisitalias_rhs6(self, n): pass

        def visitmacro_name_symbol0(self, n):pass
        def endVisitmacro_name_symbol0(self, n): pass

        def visitmacro_name_symbol1(self, n):pass
        def endVisitmacro_name_symbol1(self, n): pass

        def visitdrop_command0(self, n):pass
        def endVisitdrop_command0(self, n): pass

        def visitdrop_command1(self, n):pass
        def endVisitdrop_command1(self, n): pass

        def visitname0(self, n):pass
        def endVisitname0(self, n): pass

        def visitname1(self, n):pass
        def endVisitname1(self, n): pass

        def visitname2(self, n):pass
        def endVisitname2(self, n): pass

        def visitname3(self, n):pass
        def endVisitname3(self, n): pass

        def visitname4(self, n):pass
        def endVisitname4(self, n): pass

        def visitname5(self, n):pass
        def endVisitname5(self, n): pass

        def visitproduces0(self, n):pass
        def endVisitproduces0(self, n): pass

        def visitproduces1(self, n):pass
        def endVisitproduces1(self, n): pass

        def visitproduces2(self, n):pass
        def endVisitproduces2(self, n): pass

        def visitproduces3(self, n):pass
        def endVisitproduces3(self, n): pass

        def visitsymWithAttrs0(self, n):pass
        def endVisitsymWithAttrs0(self, n): pass

        def visitsymWithAttrs1(self, n):pass
        def endVisitsymWithAttrs1(self, n): pass

        def visitstart_symbol0(self, n):pass
        def endVisitstart_symbol0(self, n): pass

        def visitstart_symbol1(self, n):pass
        def endVisitstart_symbol1(self, n): pass

        def visitterminal_symbol0(self, n):pass
        def endVisitterminal_symbol0(self, n): pass

        def visitterminal_symbol1(self, n):pass
        def endVisitterminal_symbol1(self, n): pass

    

class AbstractVisitor(Visitor):
        __slots__ = ()
    
        def  unimplementedVisitor(self,s ): raise TypeError('Can not instantiate abstract class  with abstract methods')

        def  preVisit(self, element ): return True

        def  postVisit(self,element ): pass

        def visitASTNodeToken(self, n):
            self.unimplementedVisitor("visit(ASTNodeToken)")
            return True
        def endVisitASTNodeToken(self, n): self.unimplementedVisitor("endVisit(ASTNodeToken)")

        def visitLPG(self, n):
            self.unimplementedVisitor("visit(LPG)")
            return True
        def endVisitLPG(self, n): self.unimplementedVisitor("endVisit(LPG)")

        def visitLPG_itemList(self, n):
            self.unimplementedVisitor("visit(LPG_itemList)")
            return True
        def endVisitLPG_itemList(self, n): self.unimplementedVisitor("endVisit(LPG_itemList)")

        def visitAliasSeg(self, n):
            self.unimplementedVisitor("visit(AliasSeg)")
            return True
        def endVisitAliasSeg(self, n): self.unimplementedVisitor("endVisit(AliasSeg)")

        def visitAstSeg(self, n):
            self.unimplementedVisitor("visit(AstSeg)")
            return True
        def endVisitAstSeg(self, n): self.unimplementedVisitor("endVisit(AstSeg)")

        def visitDefineSeg(self, n):
            self.unimplementedVisitor("visit(DefineSeg)")
            return True
        def endVisitDefineSeg(self, n): self.unimplementedVisitor("endVisit(DefineSeg)")

        def visitEofSeg(self, n):
            self.unimplementedVisitor("visit(EofSeg)")
            return True
        def endVisitEofSeg(self, n): self.unimplementedVisitor("endVisit(EofSeg)")

        def visitEolSeg(self, n):
            self.unimplementedVisitor("visit(EolSeg)")
            return True
        def endVisitEolSeg(self, n): self.unimplementedVisitor("endVisit(EolSeg)")

        def visitErrorSeg(self, n):
            self.unimplementedVisitor("visit(ErrorSeg)")
            return True
        def endVisitErrorSeg(self, n): self.unimplementedVisitor("endVisit(ErrorSeg)")

        def visitExportSeg(self, n):
            self.unimplementedVisitor("visit(ExportSeg)")
            return True
        def endVisitExportSeg(self, n): self.unimplementedVisitor("endVisit(ExportSeg)")

        def visitGlobalsSeg(self, n):
            self.unimplementedVisitor("visit(GlobalsSeg)")
            return True
        def endVisitGlobalsSeg(self, n): self.unimplementedVisitor("endVisit(GlobalsSeg)")

        def visitHeadersSeg(self, n):
            self.unimplementedVisitor("visit(HeadersSeg)")
            return True
        def endVisitHeadersSeg(self, n): self.unimplementedVisitor("endVisit(HeadersSeg)")

        def visitIdentifierSeg(self, n):
            self.unimplementedVisitor("visit(IdentifierSeg)")
            return True
        def endVisitIdentifierSeg(self, n): self.unimplementedVisitor("endVisit(IdentifierSeg)")

        def visitImportSeg(self, n):
            self.unimplementedVisitor("visit(ImportSeg)")
            return True
        def endVisitImportSeg(self, n): self.unimplementedVisitor("endVisit(ImportSeg)")

        def visitIncludeSeg(self, n):
            self.unimplementedVisitor("visit(IncludeSeg)")
            return True
        def endVisitIncludeSeg(self, n): self.unimplementedVisitor("endVisit(IncludeSeg)")

        def visitKeywordsSeg(self, n):
            self.unimplementedVisitor("visit(KeywordsSeg)")
            return True
        def endVisitKeywordsSeg(self, n): self.unimplementedVisitor("endVisit(KeywordsSeg)")

        def visitNamesSeg(self, n):
            self.unimplementedVisitor("visit(NamesSeg)")
            return True
        def endVisitNamesSeg(self, n): self.unimplementedVisitor("endVisit(NamesSeg)")

        def visitNoticeSeg(self, n):
            self.unimplementedVisitor("visit(NoticeSeg)")
            return True
        def endVisitNoticeSeg(self, n): self.unimplementedVisitor("endVisit(NoticeSeg)")

        def visitRulesSeg(self, n):
            self.unimplementedVisitor("visit(RulesSeg)")
            return True
        def endVisitRulesSeg(self, n): self.unimplementedVisitor("endVisit(RulesSeg)")

        def visitSoftKeywordsSeg(self, n):
            self.unimplementedVisitor("visit(SoftKeywordsSeg)")
            return True
        def endVisitSoftKeywordsSeg(self, n): self.unimplementedVisitor("endVisit(SoftKeywordsSeg)")

        def visitStartSeg(self, n):
            self.unimplementedVisitor("visit(StartSeg)")
            return True
        def endVisitStartSeg(self, n): self.unimplementedVisitor("endVisit(StartSeg)")

        def visitTerminalsSeg(self, n):
            self.unimplementedVisitor("visit(TerminalsSeg)")
            return True
        def endVisitTerminalsSeg(self, n): self.unimplementedVisitor("endVisit(TerminalsSeg)")

        def visitTrailersSeg(self, n):
            self.unimplementedVisitor("visit(TrailersSeg)")
            return True
        def endVisitTrailersSeg(self, n): self.unimplementedVisitor("endVisit(TrailersSeg)")

        def visitTypesSeg(self, n):
            self.unimplementedVisitor("visit(TypesSeg)")
            return True
        def endVisitTypesSeg(self, n): self.unimplementedVisitor("endVisit(TypesSeg)")

        def visitRecoverSeg(self, n):
            self.unimplementedVisitor("visit(RecoverSeg)")
            return True
        def endVisitRecoverSeg(self, n): self.unimplementedVisitor("endVisit(RecoverSeg)")

        def visitPredecessorSeg(self, n):
            self.unimplementedVisitor("visit(PredecessorSeg)")
            return True
        def endVisitPredecessorSeg(self, n): self.unimplementedVisitor("endVisit(PredecessorSeg)")

        def visitoption_specList(self, n):
            self.unimplementedVisitor("visit(option_specList)")
            return True
        def endVisitoption_specList(self, n): self.unimplementedVisitor("endVisit(option_specList)")

        def visitoption_spec(self, n):
            self.unimplementedVisitor("visit(option_spec)")
            return True
        def endVisitoption_spec(self, n): self.unimplementedVisitor("endVisit(option_spec)")

        def visitoptionList(self, n):
            self.unimplementedVisitor("visit(optionList)")
            return True
        def endVisitoptionList(self, n): self.unimplementedVisitor("endVisit(optionList)")

        def visitoption(self, n):
            self.unimplementedVisitor("visit(option)")
            return True
        def endVisitoption(self, n): self.unimplementedVisitor("endVisit(option)")

        def visitSYMBOLList(self, n):
            self.unimplementedVisitor("visit(SYMBOLList)")
            return True
        def endVisitSYMBOLList(self, n): self.unimplementedVisitor("endVisit(SYMBOLList)")

        def visitaliasSpecList(self, n):
            self.unimplementedVisitor("visit(aliasSpecList)")
            return True
        def endVisitaliasSpecList(self, n): self.unimplementedVisitor("endVisit(aliasSpecList)")

        def visitalias_lhs_macro_name(self, n):
            self.unimplementedVisitor("visit(alias_lhs_macro_name)")
            return True
        def endVisitalias_lhs_macro_name(self, n): self.unimplementedVisitor("endVisit(alias_lhs_macro_name)")

        def visitdefineSpecList(self, n):
            self.unimplementedVisitor("visit(defineSpecList)")
            return True
        def endVisitdefineSpecList(self, n): self.unimplementedVisitor("endVisit(defineSpecList)")

        def visitdefineSpec(self, n):
            self.unimplementedVisitor("visit(defineSpec)")
            return True
        def endVisitdefineSpec(self, n): self.unimplementedVisitor("endVisit(defineSpec)")

        def visitmacro_segment(self, n):
            self.unimplementedVisitor("visit(macro_segment)")
            return True
        def endVisitmacro_segment(self, n): self.unimplementedVisitor("endVisit(macro_segment)")

        def visitterminal_symbolList(self, n):
            self.unimplementedVisitor("visit(terminal_symbolList)")
            return True
        def endVisitterminal_symbolList(self, n): self.unimplementedVisitor("endVisit(terminal_symbolList)")

        def visitaction_segmentList(self, n):
            self.unimplementedVisitor("visit(action_segmentList)")
            return True
        def endVisitaction_segmentList(self, n): self.unimplementedVisitor("endVisit(action_segmentList)")

        def visitimport_segment(self, n):
            self.unimplementedVisitor("visit(import_segment)")
            return True
        def endVisitimport_segment(self, n): self.unimplementedVisitor("endVisit(import_segment)")

        def visitdrop_commandList(self, n):
            self.unimplementedVisitor("visit(drop_commandList)")
            return True
        def endVisitdrop_commandList(self, n): self.unimplementedVisitor("endVisit(drop_commandList)")

        def visitdrop_ruleList(self, n):
            self.unimplementedVisitor("visit(drop_ruleList)")
            return True
        def endVisitdrop_ruleList(self, n): self.unimplementedVisitor("endVisit(drop_ruleList)")

        def visitdrop_rule(self, n):
            self.unimplementedVisitor("visit(drop_rule)")
            return True
        def endVisitdrop_rule(self, n): self.unimplementedVisitor("endVisit(drop_rule)")

        def visitoptMacroName(self, n):
            self.unimplementedVisitor("visit(optMacroName)")
            return True
        def endVisitoptMacroName(self, n): self.unimplementedVisitor("endVisit(optMacroName)")

        def visitinclude_segment(self, n):
            self.unimplementedVisitor("visit(include_segment)")
            return True
        def endVisitinclude_segment(self, n): self.unimplementedVisitor("endVisit(include_segment)")

        def visitkeywordSpecList(self, n):
            self.unimplementedVisitor("visit(keywordSpecList)")
            return True
        def endVisitkeywordSpecList(self, n): self.unimplementedVisitor("endVisit(keywordSpecList)")

        def visitkeywordSpec(self, n):
            self.unimplementedVisitor("visit(keywordSpec)")
            return True
        def endVisitkeywordSpec(self, n): self.unimplementedVisitor("endVisit(keywordSpec)")

        def visitnameSpecList(self, n):
            self.unimplementedVisitor("visit(nameSpecList)")
            return True
        def endVisitnameSpecList(self, n): self.unimplementedVisitor("endVisit(nameSpecList)")

        def visitnameSpec(self, n):
            self.unimplementedVisitor("visit(nameSpec)")
            return True
        def endVisitnameSpec(self, n): self.unimplementedVisitor("endVisit(nameSpec)")

        def visitrules_segment(self, n):
            self.unimplementedVisitor("visit(rules_segment)")
            return True
        def endVisitrules_segment(self, n): self.unimplementedVisitor("endVisit(rules_segment)")

        def visitnonTermList(self, n):
            self.unimplementedVisitor("visit(nonTermList)")
            return True
        def endVisitnonTermList(self, n): self.unimplementedVisitor("endVisit(nonTermList)")

        def visitnonTerm(self, n):
            self.unimplementedVisitor("visit(nonTerm)")
            return True
        def endVisitnonTerm(self, n): self.unimplementedVisitor("endVisit(nonTerm)")

        def visitRuleName(self, n):
            self.unimplementedVisitor("visit(RuleName)")
            return True
        def endVisitRuleName(self, n): self.unimplementedVisitor("endVisit(RuleName)")

        def visitruleList(self, n):
            self.unimplementedVisitor("visit(ruleList)")
            return True
        def endVisitruleList(self, n): self.unimplementedVisitor("endVisit(ruleList)")

        def visitrule(self, n):
            self.unimplementedVisitor("visit(rule)")
            return True
        def endVisitrule(self, n): self.unimplementedVisitor("endVisit(rule)")

        def visitsymWithAttrsList(self, n):
            self.unimplementedVisitor("visit(symWithAttrsList)")
            return True
        def endVisitsymWithAttrsList(self, n): self.unimplementedVisitor("endVisit(symWithAttrsList)")

        def visitsymAttrs(self, n):
            self.unimplementedVisitor("visit(symAttrs)")
            return True
        def endVisitsymAttrs(self, n): self.unimplementedVisitor("endVisit(symAttrs)")

        def visitaction_segment(self, n):
            self.unimplementedVisitor("visit(action_segment)")
            return True
        def endVisitaction_segment(self, n): self.unimplementedVisitor("endVisit(action_segment)")

        def visitstart_symbolList(self, n):
            self.unimplementedVisitor("visit(start_symbolList)")
            return True
        def endVisitstart_symbolList(self, n): self.unimplementedVisitor("endVisit(start_symbolList)")

        def visitterminalList(self, n):
            self.unimplementedVisitor("visit(terminalList)")
            return True
        def endVisitterminalList(self, n): self.unimplementedVisitor("endVisit(terminalList)")

        def visitterminal(self, n):
            self.unimplementedVisitor("visit(terminal)")
            return True
        def endVisitterminal(self, n): self.unimplementedVisitor("endVisit(terminal)")

        def visitoptTerminalAlias(self, n):
            self.unimplementedVisitor("visit(optTerminalAlias)")
            return True
        def endVisitoptTerminalAlias(self, n): self.unimplementedVisitor("endVisit(optTerminalAlias)")

        def visittype_declarationsList(self, n):
            self.unimplementedVisitor("visit(type_declarationsList)")
            return True
        def endVisittype_declarationsList(self, n): self.unimplementedVisitor("endVisit(type_declarationsList)")

        def visittype_declarations(self, n):
            self.unimplementedVisitor("visit(type_declarations)")
            return True
        def endVisittype_declarations(self, n): self.unimplementedVisitor("endVisit(type_declarations)")

        def visitsymbol_pairList(self, n):
            self.unimplementedVisitor("visit(symbol_pairList)")
            return True
        def endVisitsymbol_pairList(self, n): self.unimplementedVisitor("endVisit(symbol_pairList)")

        def visitsymbol_pair(self, n):
            self.unimplementedVisitor("visit(symbol_pair)")
            return True
        def endVisitsymbol_pair(self, n): self.unimplementedVisitor("endVisit(symbol_pair)")

        def visitrecover_symbol(self, n):
            self.unimplementedVisitor("visit(recover_symbol)")
            return True
        def endVisitrecover_symbol(self, n): self.unimplementedVisitor("endVisit(recover_symbol)")

        def visitEND_KEY_OPT(self, n):
            self.unimplementedVisitor("visit(END_KEY_OPT)")
            return True
        def endVisitEND_KEY_OPT(self, n): self.unimplementedVisitor("endVisit(END_KEY_OPT)")

        def visitoption_value0(self, n):
            self.unimplementedVisitor("visit(option_value0)")
            return True
        def endVisitoption_value0(self, n): self.unimplementedVisitor("endVisit(option_value0)")

        def visitoption_value1(self, n):
            self.unimplementedVisitor("visit(option_value1)")
            return True
        def endVisitoption_value1(self, n): self.unimplementedVisitor("endVisit(option_value1)")

        def visitaliasSpec0(self, n):
            self.unimplementedVisitor("visit(aliasSpec0)")
            return True
        def endVisitaliasSpec0(self, n): self.unimplementedVisitor("endVisit(aliasSpec0)")

        def visitaliasSpec1(self, n):
            self.unimplementedVisitor("visit(aliasSpec1)")
            return True
        def endVisitaliasSpec1(self, n): self.unimplementedVisitor("endVisit(aliasSpec1)")

        def visitaliasSpec2(self, n):
            self.unimplementedVisitor("visit(aliasSpec2)")
            return True
        def endVisitaliasSpec2(self, n): self.unimplementedVisitor("endVisit(aliasSpec2)")

        def visitaliasSpec3(self, n):
            self.unimplementedVisitor("visit(aliasSpec3)")
            return True
        def endVisitaliasSpec3(self, n): self.unimplementedVisitor("endVisit(aliasSpec3)")

        def visitaliasSpec4(self, n):
            self.unimplementedVisitor("visit(aliasSpec4)")
            return True
        def endVisitaliasSpec4(self, n): self.unimplementedVisitor("endVisit(aliasSpec4)")

        def visitaliasSpec5(self, n):
            self.unimplementedVisitor("visit(aliasSpec5)")
            return True
        def endVisitaliasSpec5(self, n): self.unimplementedVisitor("endVisit(aliasSpec5)")

        def visitalias_rhs0(self, n):
            self.unimplementedVisitor("visit(alias_rhs0)")
            return True
        def endVisitalias_rhs0(self, n): self.unimplementedVisitor("endVisit(alias_rhs0)")

        def visitalias_rhs1(self, n):
            self.unimplementedVisitor("visit(alias_rhs1)")
            return True
        def endVisitalias_rhs1(self, n): self.unimplementedVisitor("endVisit(alias_rhs1)")

        def visitalias_rhs2(self, n):
            self.unimplementedVisitor("visit(alias_rhs2)")
            return True
        def endVisitalias_rhs2(self, n): self.unimplementedVisitor("endVisit(alias_rhs2)")

        def visitalias_rhs3(self, n):
            self.unimplementedVisitor("visit(alias_rhs3)")
            return True
        def endVisitalias_rhs3(self, n): self.unimplementedVisitor("endVisit(alias_rhs3)")

        def visitalias_rhs4(self, n):
            self.unimplementedVisitor("visit(alias_rhs4)")
            return True
        def endVisitalias_rhs4(self, n): self.unimplementedVisitor("endVisit(alias_rhs4)")

        def visitalias_rhs5(self, n):
            self.unimplementedVisitor("visit(alias_rhs5)")
            return True
        def endVisitalias_rhs5(self, n): self.unimplementedVisitor("endVisit(alias_rhs5)")

        def visitalias_rhs6(self, n):
            self.unimplementedVisitor("visit(alias_rhs6)")
            return True
        def endVisitalias_rhs6(self, n): self.unimplementedVisitor("endVisit(alias_rhs6)")

        def visitmacro_name_symbol0(self, n):
            self.unimplementedVisitor("visit(macro_name_symbol0)")
            return True
        def endVisitmacro_name_symbol0(self, n): self.unimplementedVisitor("endVisit(macro_name_symbol0)")

        def visitmacro_name_symbol1(self, n):
            self.unimplementedVisitor("visit(macro_name_symbol1)")
            return True
        def endVisitmacro_name_symbol1(self, n): self.unimplementedVisitor("endVisit(macro_name_symbol1)")

        def visitdrop_command0(self, n):
            self.unimplementedVisitor("visit(drop_command0)")
            return True
        def endVisitdrop_command0(self, n): self.unimplementedVisitor("endVisit(drop_command0)")

        def visitdrop_command1(self, n):
            self.unimplementedVisitor("visit(drop_command1)")
            return True
        def endVisitdrop_command1(self, n): self.unimplementedVisitor("endVisit(drop_command1)")

        def visitname0(self, n):
            self.unimplementedVisitor("visit(name0)")
            return True
        def endVisitname0(self, n): self.unimplementedVisitor("endVisit(name0)")

        def visitname1(self, n):
            self.unimplementedVisitor("visit(name1)")
            return True
        def endVisitname1(self, n): self.unimplementedVisitor("endVisit(name1)")

        def visitname2(self, n):
            self.unimplementedVisitor("visit(name2)")
            return True
        def endVisitname2(self, n): self.unimplementedVisitor("endVisit(name2)")

        def visitname3(self, n):
            self.unimplementedVisitor("visit(name3)")
            return True
        def endVisitname3(self, n): self.unimplementedVisitor("endVisit(name3)")

        def visitname4(self, n):
            self.unimplementedVisitor("visit(name4)")
            return True
        def endVisitname4(self, n): self.unimplementedVisitor("endVisit(name4)")

        def visitname5(self, n):
            self.unimplementedVisitor("visit(name5)")
            return True
        def endVisitname5(self, n): self.unimplementedVisitor("endVisit(name5)")

        def visitproduces0(self, n):
            self.unimplementedVisitor("visit(produces0)")
            return True
        def endVisitproduces0(self, n): self.unimplementedVisitor("endVisit(produces0)")

        def visitproduces1(self, n):
            self.unimplementedVisitor("visit(produces1)")
            return True
        def endVisitproduces1(self, n): self.unimplementedVisitor("endVisit(produces1)")

        def visitproduces2(self, n):
            self.unimplementedVisitor("visit(produces2)")
            return True
        def endVisitproduces2(self, n): self.unimplementedVisitor("endVisit(produces2)")

        def visitproduces3(self, n):
            self.unimplementedVisitor("visit(produces3)")
            return True
        def endVisitproduces3(self, n): self.unimplementedVisitor("endVisit(produces3)")

        def visitsymWithAttrs0(self, n):
            self.unimplementedVisitor("visit(symWithAttrs0)")
            return True
        def endVisitsymWithAttrs0(self, n): self.unimplementedVisitor("endVisit(symWithAttrs0)")

        def visitsymWithAttrs1(self, n):
            self.unimplementedVisitor("visit(symWithAttrs1)")
            return True
        def endVisitsymWithAttrs1(self, n): self.unimplementedVisitor("endVisit(symWithAttrs1)")

        def visitstart_symbol0(self, n):
            self.unimplementedVisitor("visit(start_symbol0)")
            return True
        def endVisitstart_symbol0(self, n): self.unimplementedVisitor("endVisit(start_symbol0)")

        def visitstart_symbol1(self, n):
            self.unimplementedVisitor("visit(start_symbol1)")
            return True
        def endVisitstart_symbol1(self, n): self.unimplementedVisitor("endVisit(start_symbol1)")

        def visitterminal_symbol0(self, n):
            self.unimplementedVisitor("visit(terminal_symbol0)")
            return True
        def endVisitterminal_symbol0(self, n): self.unimplementedVisitor("endVisit(terminal_symbol0)")

        def visitterminal_symbol1(self, n):
            self.unimplementedVisitor("visit(terminal_symbol1)")
            return True
        def endVisitterminal_symbol1(self, n): self.unimplementedVisitor("endVisit(terminal_symbol1)")


        def visit(self, n):
        
            if isinstance(n, ASTNodeToken): return self.visitASTNodeToken( n)
            elif isinstance(n, LPG): return self.visitLPG( n)
            elif isinstance(n, LPG_itemList): return self.visitLPG_itemList( n)
            elif isinstance(n, AliasSeg): return self.visitAliasSeg( n)
            elif isinstance(n, AstSeg): return self.visitAstSeg( n)
            elif isinstance(n, DefineSeg): return self.visitDefineSeg( n)
            elif isinstance(n, EofSeg): return self.visitEofSeg( n)
            elif isinstance(n, EolSeg): return self.visitEolSeg( n)
            elif isinstance(n, ErrorSeg): return self.visitErrorSeg( n)
            elif isinstance(n, ExportSeg): return self.visitExportSeg( n)
            elif isinstance(n, GlobalsSeg): return self.visitGlobalsSeg( n)
            elif isinstance(n, HeadersSeg): return self.visitHeadersSeg( n)
            elif isinstance(n, IdentifierSeg): return self.visitIdentifierSeg( n)
            elif isinstance(n, ImportSeg): return self.visitImportSeg( n)
            elif isinstance(n, IncludeSeg): return self.visitIncludeSeg( n)
            elif isinstance(n, KeywordsSeg): return self.visitKeywordsSeg( n)
            elif isinstance(n, NamesSeg): return self.visitNamesSeg( n)
            elif isinstance(n, NoticeSeg): return self.visitNoticeSeg( n)
            elif isinstance(n, RulesSeg): return self.visitRulesSeg( n)
            elif isinstance(n, SoftKeywordsSeg): return self.visitSoftKeywordsSeg( n)
            elif isinstance(n, StartSeg): return self.visitStartSeg( n)
            elif isinstance(n, TerminalsSeg): return self.visitTerminalsSeg( n)
            elif isinstance(n, TrailersSeg): return self.visitTrailersSeg( n)
            elif isinstance(n, TypesSeg): return self.visitTypesSeg( n)
            elif isinstance(n, RecoverSeg): return self.visitRecoverSeg( n)
            elif isinstance(n, PredecessorSeg): return self.visitPredecessorSeg( n)
            elif isinstance(n, option_specList): return self.visitoption_specList( n)
            elif isinstance(n, option_spec): return self.visitoption_spec( n)
            elif isinstance(n, optionList): return self.visitoptionList( n)
            elif isinstance(n, option): return self.visitoption( n)
            elif isinstance(n, SYMBOLList): return self.visitSYMBOLList( n)
            elif isinstance(n, aliasSpecList): return self.visitaliasSpecList( n)
            elif isinstance(n, alias_lhs_macro_name): return self.visitalias_lhs_macro_name( n)
            elif isinstance(n, defineSpecList): return self.visitdefineSpecList( n)
            elif isinstance(n, defineSpec): return self.visitdefineSpec( n)
            elif isinstance(n, macro_segment): return self.visitmacro_segment( n)
            elif isinstance(n, terminal_symbolList): return self.visitterminal_symbolList( n)
            elif isinstance(n, action_segmentList): return self.visitaction_segmentList( n)
            elif isinstance(n, import_segment): return self.visitimport_segment( n)
            elif isinstance(n, drop_commandList): return self.visitdrop_commandList( n)
            elif isinstance(n, drop_ruleList): return self.visitdrop_ruleList( n)
            elif isinstance(n, drop_rule): return self.visitdrop_rule( n)
            elif isinstance(n, optMacroName): return self.visitoptMacroName( n)
            elif isinstance(n, include_segment): return self.visitinclude_segment( n)
            elif isinstance(n, keywordSpecList): return self.visitkeywordSpecList( n)
            elif isinstance(n, keywordSpec): return self.visitkeywordSpec( n)
            elif isinstance(n, nameSpecList): return self.visitnameSpecList( n)
            elif isinstance(n, nameSpec): return self.visitnameSpec( n)
            elif isinstance(n, rules_segment): return self.visitrules_segment( n)
            elif isinstance(n, nonTermList): return self.visitnonTermList( n)
            elif isinstance(n, nonTerm): return self.visitnonTerm( n)
            elif isinstance(n, RuleName): return self.visitRuleName( n)
            elif isinstance(n, ruleList): return self.visitruleList( n)
            elif isinstance(n, rule): return self.visitrule( n)
            elif isinstance(n, symWithAttrsList): return self.visitsymWithAttrsList( n)
            elif isinstance(n, symAttrs): return self.visitsymAttrs( n)
            elif isinstance(n, action_segment): return self.visitaction_segment( n)
            elif isinstance(n, start_symbolList): return self.visitstart_symbolList( n)
            elif isinstance(n, terminalList): return self.visitterminalList( n)
            elif isinstance(n, terminal): return self.visitterminal( n)
            elif isinstance(n, optTerminalAlias): return self.visitoptTerminalAlias( n)
            elif isinstance(n, type_declarationsList): return self.visittype_declarationsList( n)
            elif isinstance(n, type_declarations): return self.visittype_declarations( n)
            elif isinstance(n, symbol_pairList): return self.visitsymbol_pairList( n)
            elif isinstance(n, symbol_pair): return self.visitsymbol_pair( n)
            elif isinstance(n, recover_symbol): return self.visitrecover_symbol( n)
            elif isinstance(n, END_KEY_OPT): return self.visitEND_KEY_OPT( n)
            elif isinstance(n, option_value0): return self.visitoption_value0( n)
            elif isinstance(n, option_value1): return self.visitoption_value1( n)
            elif isinstance(n, aliasSpec0): return self.visitaliasSpec0( n)
            elif isinstance(n, aliasSpec1): return self.visitaliasSpec1( n)
            elif isinstance(n, aliasSpec2): return self.visitaliasSpec2( n)
            elif isinstance(n, aliasSpec3): return self.visitaliasSpec3( n)
            elif isinstance(n, aliasSpec4): return self.visitaliasSpec4( n)
            elif isinstance(n, aliasSpec5): return self.visitaliasSpec5( n)
            elif isinstance(n, alias_rhs0): return self.visitalias_rhs0( n)
            elif isinstance(n, alias_rhs1): return self.visitalias_rhs1( n)
            elif isinstance(n, alias_rhs2): return self.visitalias_rhs2( n)
            elif isinstance(n, alias_rhs3): return self.visitalias_rhs3( n)
            elif isinstance(n, alias_rhs4): return self.visitalias_rhs4( n)
            elif isinstance(n, alias_rhs5): return self.visitalias_rhs5( n)
            elif isinstance(n, alias_rhs6): return self.visitalias_rhs6( n)
            elif isinstance(n, macro_name_symbol0): return self.visitmacro_name_symbol0( n)
            elif isinstance(n, macro_name_symbol1): return self.visitmacro_name_symbol1( n)
            elif isinstance(n, drop_command0): return self.visitdrop_command0( n)
            elif isinstance(n, drop_command1): return self.visitdrop_command1( n)
            elif isinstance(n, name0): return self.visitname0( n)
            elif isinstance(n, name1): return self.visitname1( n)
            elif isinstance(n, name2): return self.visitname2( n)
            elif isinstance(n, name3): return self.visitname3( n)
            elif isinstance(n, name4): return self.visitname4( n)
            elif isinstance(n, name5): return self.visitname5( n)
            elif isinstance(n, produces0): return self.visitproduces0( n)
            elif isinstance(n, produces1): return self.visitproduces1( n)
            elif isinstance(n, produces2): return self.visitproduces2( n)
            elif isinstance(n, produces3): return self.visitproduces3( n)
            elif isinstance(n, symWithAttrs0): return self.visitsymWithAttrs0( n)
            elif isinstance(n, symWithAttrs1): return self.visitsymWithAttrs1( n)
            elif isinstance(n, start_symbol0): return self.visitstart_symbol0( n)
            elif isinstance(n, start_symbol1): return self.visitstart_symbol1( n)
            elif isinstance(n, terminal_symbol0): return self.visitterminal_symbol0( n)
            elif isinstance(n, terminal_symbol1): return self.visitterminal_symbol1( n)
            raise ValueError("visit(" + n.toString() + ")")
        
        def endVisit(self, n) : 
        
            if (isinstance(n, ASTNodeToken)): self.endVisitASTNodeToken( n)
            elif (isinstance(n, LPG)): self.endVisitLPG( n)
            elif (isinstance(n, LPG_itemList)): self.endVisitLPG_itemList( n)
            elif (isinstance(n, AliasSeg)): self.endVisitAliasSeg( n)
            elif (isinstance(n, AstSeg)): self.endVisitAstSeg( n)
            elif (isinstance(n, DefineSeg)): self.endVisitDefineSeg( n)
            elif (isinstance(n, EofSeg)): self.endVisitEofSeg( n)
            elif (isinstance(n, EolSeg)): self.endVisitEolSeg( n)
            elif (isinstance(n, ErrorSeg)): self.endVisitErrorSeg( n)
            elif (isinstance(n, ExportSeg)): self.endVisitExportSeg( n)
            elif (isinstance(n, GlobalsSeg)): self.endVisitGlobalsSeg( n)
            elif (isinstance(n, HeadersSeg)): self.endVisitHeadersSeg( n)
            elif (isinstance(n, IdentifierSeg)): self.endVisitIdentifierSeg( n)
            elif (isinstance(n, ImportSeg)): self.endVisitImportSeg( n)
            elif (isinstance(n, IncludeSeg)): self.endVisitIncludeSeg( n)
            elif (isinstance(n, KeywordsSeg)): self.endVisitKeywordsSeg( n)
            elif (isinstance(n, NamesSeg)): self.endVisitNamesSeg( n)
            elif (isinstance(n, NoticeSeg)): self.endVisitNoticeSeg( n)
            elif (isinstance(n, RulesSeg)): self.endVisitRulesSeg( n)
            elif (isinstance(n, SoftKeywordsSeg)): self.endVisitSoftKeywordsSeg( n)
            elif (isinstance(n, StartSeg)): self.endVisitStartSeg( n)
            elif (isinstance(n, TerminalsSeg)): self.endVisitTerminalsSeg( n)
            elif (isinstance(n, TrailersSeg)): self.endVisitTrailersSeg( n)
            elif (isinstance(n, TypesSeg)): self.endVisitTypesSeg( n)
            elif (isinstance(n, RecoverSeg)): self.endVisitRecoverSeg( n)
            elif (isinstance(n, PredecessorSeg)): self.endVisitPredecessorSeg( n)
            elif (isinstance(n, option_specList)): self.endVisitoption_specList( n)
            elif (isinstance(n, option_spec)): self.endVisitoption_spec( n)
            elif (isinstance(n, optionList)): self.endVisitoptionList( n)
            elif (isinstance(n, option)): self.endVisitoption( n)
            elif (isinstance(n, SYMBOLList)): self.endVisitSYMBOLList( n)
            elif (isinstance(n, aliasSpecList)): self.endVisitaliasSpecList( n)
            elif (isinstance(n, alias_lhs_macro_name)): self.endVisitalias_lhs_macro_name( n)
            elif (isinstance(n, defineSpecList)): self.endVisitdefineSpecList( n)
            elif (isinstance(n, defineSpec)): self.endVisitdefineSpec( n)
            elif (isinstance(n, macro_segment)): self.endVisitmacro_segment( n)
            elif (isinstance(n, terminal_symbolList)): self.endVisitterminal_symbolList( n)
            elif (isinstance(n, action_segmentList)): self.endVisitaction_segmentList( n)
            elif (isinstance(n, import_segment)): self.endVisitimport_segment( n)
            elif (isinstance(n, drop_commandList)): self.endVisitdrop_commandList( n)
            elif (isinstance(n, drop_ruleList)): self.endVisitdrop_ruleList( n)
            elif (isinstance(n, drop_rule)): self.endVisitdrop_rule( n)
            elif (isinstance(n, optMacroName)): self.endVisitoptMacroName( n)
            elif (isinstance(n, include_segment)): self.endVisitinclude_segment( n)
            elif (isinstance(n, keywordSpecList)): self.endVisitkeywordSpecList( n)
            elif (isinstance(n, keywordSpec)): self.endVisitkeywordSpec( n)
            elif (isinstance(n, nameSpecList)): self.endVisitnameSpecList( n)
            elif (isinstance(n, nameSpec)): self.endVisitnameSpec( n)
            elif (isinstance(n, rules_segment)): self.endVisitrules_segment( n)
            elif (isinstance(n, nonTermList)): self.endVisitnonTermList( n)
            elif (isinstance(n, nonTerm)): self.endVisitnonTerm( n)
            elif (isinstance(n, RuleName)): self.endVisitRuleName( n)
            elif (isinstance(n, ruleList)): self.endVisitruleList( n)
            elif (isinstance(n, rule)): self.endVisitrule( n)
            elif (isinstance(n, symWithAttrsList)): self.endVisitsymWithAttrsList( n)
            elif (isinstance(n, symAttrs)): self.endVisitsymAttrs( n)
            elif (isinstance(n, action_segment)): self.endVisitaction_segment( n)
            elif (isinstance(n, start_symbolList)): self.endVisitstart_symbolList( n)
            elif (isinstance(n, terminalList)): self.endVisitterminalList( n)
            elif (isinstance(n, terminal)): self.endVisitterminal( n)
            elif (isinstance(n, optTerminalAlias)): self.endVisitoptTerminalAlias( n)
            elif (isinstance(n, type_declarationsList)): self.endVisittype_declarationsList( n)
            elif (isinstance(n, type_declarations)): self.endVisittype_declarations( n)
            elif (isinstance(n, symbol_pairList)): self.endVisitsymbol_pairList( n)
            elif (isinstance(n, symbol_pair)): self.endVisitsymbol_pair( n)
            elif (isinstance(n, recover_symbol)): self.endVisitrecover_symbol( n)
            elif (isinstance(n, END_KEY_OPT)): self.endVisitEND_KEY_OPT( n)
            elif (isinstance(n, option_value0)): self.endVisitoption_value0( n)
            elif (isinstance(n, option_value1)): self.endVisitoption_value1( n)
            elif (isinstance(n, aliasSpec0)): self.endVisitaliasSpec0( n)
            elif (isinstance(n, aliasSpec1)): self.endVisitaliasSpec1( n)
            elif (isinstance(n, aliasSpec2)): self.endVisitaliasSpec2( n)
            elif (isinstance(n, aliasSpec3)): self.endVisitaliasSpec3( n)
            elif (isinstance(n, aliasSpec4)): self.endVisitaliasSpec4( n)
            elif (isinstance(n, aliasSpec5)): self.endVisitaliasSpec5( n)
            elif (isinstance(n, alias_rhs0)): self.endVisitalias_rhs0( n)
            elif (isinstance(n, alias_rhs1)): self.endVisitalias_rhs1( n)
            elif (isinstance(n, alias_rhs2)): self.endVisitalias_rhs2( n)
            elif (isinstance(n, alias_rhs3)): self.endVisitalias_rhs3( n)
            elif (isinstance(n, alias_rhs4)): self.endVisitalias_rhs4( n)
            elif (isinstance(n, alias_rhs5)): self.endVisitalias_rhs5( n)
            elif (isinstance(n, alias_rhs6)): self.endVisitalias_rhs6( n)
            elif (isinstance(n, macro_name_symbol0)): self.endVisitmacro_name_symbol0( n)
            elif (isinstance(n, macro_name_symbol1)): self.endVisitmacro_name_symbol1( n)
            elif (isinstance(n, drop_command0)): self.endVisitdrop_command0( n)
            elif (isinstance(n, drop_command1)): self.endVisitdrop_command1( n)
            elif (isinstance(n, name0)): self.endVisitname0( n)
            elif (isinstance(n, name1)): self.endVisitname1( n)
            elif (isinstance(n, name2)): self.endVisitname2( n)
            elif (isinstance(n, name3)): self.endVisitname3( n)
            elif (isinstance(n, name4)): self.endVisitname4( n)
            elif (isinstance(n, name5)): self.endVisitname5( n)
            elif (isinstance(n, produces0)): self.endVisitproduces0( n)
            elif (isinstance(n, produces1)): self.endVisitproduces1( n)
            elif (isinstance(n, produces2)): self.endVisitproduces2( n)
            elif (isinstance(n, produces3)): self.endVisitproduces3( n)
            elif (isinstance(n, symWithAttrs0)): self.endVisitsymWithAttrs0( n)
            elif (isinstance(n, symWithAttrs1)): self.endVisitsymWithAttrs1( n)
            elif (isinstance(n, start_symbol0)): self.endVisitstart_symbol0( n)
            elif (isinstance(n, start_symbol1)): self.endVisitstart_symbol1( n)
            elif (isinstance(n, terminal_symbol0)): self.endVisitterminal_symbol0( n)
            elif (isinstance(n, terminal_symbol1)): self.endVisitterminal_symbol1( n)
            raise ValueError("visit(" + n.toString() + ")")
        
    

