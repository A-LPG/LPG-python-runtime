#
# This is the grammar specification from the Final Draft of the generic spec.
#
########################################
# Copyright (c) 2007 IBM Corporation.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http:#www.eclipse.org/legal/epl-v10.html
#
#Contributors:
#    Philippe Charles (pcharles@us.ibm.com) - initial API and implementation

########################################


    ##line 123 "btParserTemplateF.gi

from lpg2 import ArrayList, BadParseException, RuleAction, PrsStream, ParseTable, BacktrackingParser, IToken, ErrorToken, ILexStream, NullExportedSymbolsException, UnimplementedTerminalsException,  UndefinedEofSymbolException, NotBacktrackParseTableException, BadParseSymFileException, IPrsStream, Monitor, DiagnoseParser, IAst, IAstVisitor, IAbstractArrayList, NotDeterministicParseTableException,DeterministicParser, NullTerminalSymbolsException 
from JavaParserprs import  JavaParserprs 
from JavaParsersym import  JavaParsersym 

    ##line 18 "GJavaParser.g



    ##line 131 "btParserTemplateF.gi

class JavaParser (RuleAction):

    def ruleAction(self, ruleNumber) :
        act = self.__rule_action[ruleNumber]
        if act:
            act() 

    prsTable  =  JavaParserprs()

    def getParseTable(self) : 
        return JavaParser.prsTable 

    def getParser(self):
        return self.btParser 

    def setResult(self, object1) : 
        self.btParser.setSym1(object1) 

    def getRhsSym(self, i):
        return self.btParser.getSym(i) 

    def getRhsTokenIndex(self, i) : 
        return self.btParser.getToken(i) 

    def getRhsIToken(self, i) : 
        return self.prsStream.getIToken(self.getRhsTokenIndex(i)) 
    
    def getRhsFirstTokenIndex(self, i):
        return self.btParser.getFirstToken(i) 

    def getRhsFirstIToken(self, i) : 
        return self.prsStream.getIToken(self.getRhsFirstTokenIndex(i)) 

    def getRhsLastTokenIndex(self, i) :
        return self.btParser.getLastToken(i) 

    def getRhsLastIToken(self, i): 
        return self.prsStream.getIToken(self.getRhsLastTokenIndex(i)) 

    def getLeftSpan(self)  : 
        return self.btParser.getFirstToken() 

    def getLeftIToken(self) : 
        return self.prsStream.getIToken(self.getLeftSpan()) 

    def getRightSpan(self)  : 
        return self.btParser.getLastToken() 

    def getRightIToken(self) : 
        return self.prsStream.getIToken(self.getRightSpan()) 

    def getRhsErrorTokenIndex(self, i):
    
        index = self.btParser.getToken(i)
        err = self.prsStream.getIToken(index)
        return ( index  if isinstance(err,ErrorToken)  else 0)
    
    def getRhsErrorIToken(self, i):
    
        index = self.btParser.getToken(i)
        err = self.prsStream.getIToken(index)
        return  err if  isinstance(err,ErrorToken) else  None
    
    def reset(self,lexStream ): 
    
        self.prsStream.resetLexStream(lexStream)
        self.btParser.reset(self.prsStream)

        try: 
            self.prsStream.remapTerminalSymbols(self.orderedTerminalSymbols(), JavaParser.prsTable.getEoftSymbol())
        except NullExportedSymbolsException as e :
            pass
        
        except UnimplementedTerminalsException as e:
            if (self.unimplementedSymbolsWarning): 
                unimplemented_symbols = e.getSymbols()
                print("The Lexer will not scan the following token(s):")
                for i in range(unimplemented_symbols.size()):
                    id = unimplemented_symbols.get(i)
                    print("    " + str(JavaParsersym.orderedTerminalSymbols[id]))               
                
                print("")
            
        
        except UndefinedEofSymbolException as e:
            raise  ( UndefinedEofSymbolException
                ("The Lexer does not implement the Eof symbol " +
                JavaParsersym.orderedTerminalSymbols[JavaParser.prsTable.getEoftSymbol()]))
            

        
    
    
    def __init__(self,lexStream=None):
    
        self.__rule_action = [None]* (539 + 2)
        self.prsStream   =  PrsStream()
        self.btParser  = None 
        self.unimplementedSymbolsWarning  = False
        self.initRuleAction()

        try:
            self.btParser =  BacktrackingParser(None, JavaParser.prsTable,  self) 
        except  NotBacktrackParseTableException as e:
            raise NotBacktrackParseTableException("Regenerate JavaParserprs.py with -BACKTRACK option")
        except BadParseSymFileException as e:
            raise BadParseSymFileException("Bad Parser Symbol File -- JavaParsersym.py")
            
        if lexStream is not None:
           self.reset(lexStream)
        
    def numTokenKinds(self)  : 
        return JavaParsersym.numTokenKinds 

    def orderedTerminalSymbols(self):
        return JavaParsersym.orderedTerminalSymbols 

    def getTokenKindName(self, kind )  :
        return JavaParsersym.orderedTerminalSymbols[kind] 

    def getEOFTokenKind(self) :
        return JavaParser.prsTable.getEoftSymbol() 

    def getIPrsStream(self):
        return self.prsStream 

    def parser(self, error_repair_count=0 ,  monitor=None) :  
    
        self.btParser.setMonitor(monitor)
        
        try:
            return  self.btParser.fuzzyParse(error_repair_count)
        except BadParseException as e :
                 
            self.prsStream.reset(e.error_token) # point to error token

            diagnoseParser =  DiagnoseParser(self.prsStream, JavaParser.prsTable)
            diagnoseParser.diagnose(e.error_token)
            

        return None
    
    #
    # Additional entry points, if any
    #
    
   
    def parseClassBodyDeclarationsopt(self, monitor = None, error_repair_count = 0) :

        self.btParser.setMonitor(monitor)
        try:
            return  self.btParser.fuzzyParseEntry(JavaParsersym.TK_ClassBodyDeclarationsoptMarker, error_repair_count)
        except BadParseException as e:
            self.prsStream.reset(e.error_token) # point to error token
            diagnoseParser =  DiagnoseParser(self.prsStream, JavaParser.prsTable)
            diagnoseParser.diagnoseEntry(JavaParsersym.TK_ClassBodyDeclarationsoptMarker, e.error_token)
            
        return None
    

   
    def parseLPGUserAction(self, monitor = None, error_repair_count = 0) :

        self.btParser.setMonitor(monitor)
        try:
            return  self.btParser.fuzzyParseEntry(JavaParsersym.TK_LPGUserActionMarker, error_repair_count)
        except BadParseException as e:
            self.prsStream.reset(e.error_token) # point to error token
            diagnoseParser =  DiagnoseParser(self.prsStream, JavaParser.prsTable)
            diagnoseParser.diagnoseEntry(JavaParsersym.TK_LPGUserActionMarker, e.error_token)
            
        return None
    


    ##line 186 "GJavaParser.g


    
    ##line 283 "btParserTemplateF.gi

    def initRuleAction(self) : 


        #
        # Rule 3:  identifier ::= IDENTIFIER
        #
         def Act3(): 
               ##line 185 "GJavaParser.g"
                self.setResult(
                    ##line 185 GJavaParser.g
                    identifier(self, self.getRhsIToken(1))
                ##line 185 GJavaParser.g
                )

         self.__rule_action[3]= Act3

        #
        # Rule 4:  LPGUserAction ::= BlockStatementsopt
        #
        
                 
        #
        # Rule 5:  LPGUserAction ::= $BeginAction BlockStatementsopt $EndAction
        #
         def Act5(): 
               ##line 191 "GJavaParser.g"
                self.setResult(
                    ##line 191 GJavaParser.g
                    LPGUserAction0(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 191 GJavaParser.g
                                   AstToken(self.getRhsIToken(1)),
                                   ##line 191 GJavaParser.g
                                   self.getRhsSym(2),
                                   ##line 191 GJavaParser.g
                                   AstToken(self.getRhsIToken(3)))
                ##line 191 GJavaParser.g
                )

         self.__rule_action[5]= Act5

        #
        # Rule 6:  LPGUserAction ::= $BeginJava BlockStatementsopt $EndJava
        #
         def Act6(): 
               ##line 192 "GJavaParser.g"
                self.setResult(
                    ##line 192 GJavaParser.g
                    LPGUserAction1(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 192 GJavaParser.g
                                   AstToken(self.getRhsIToken(1)),
                                   ##line 192 GJavaParser.g
                                   self.getRhsSym(2),
                                   ##line 192 GJavaParser.g
                                   AstToken(self.getRhsIToken(3)))
                ##line 192 GJavaParser.g
                )

         self.__rule_action[6]= Act6

        #
        # Rule 7:  LPGUserAction ::= $NoAction
        #
         def Act7(): 
               ##line 193 "GJavaParser.g"
                self.setResult(
                    ##line 193 GJavaParser.g
                    LPGUserAction2(self.getRhsIToken(1))
                ##line 193 GJavaParser.g
                )

         self.__rule_action[7]= Act7

        #
        # Rule 8:  LPGUserAction ::= $NullAction
        #
         def Act8(): 
               ##line 194 "GJavaParser.g"
                self.setResult(
                    ##line 194 GJavaParser.g
                    LPGUserAction3(self.getRhsIToken(1))
                ##line 194 GJavaParser.g
                )

         self.__rule_action[8]= Act8

        #
        # Rule 9:  LPGUserAction ::= $BadAction
        #
         def Act9(): 
               ##line 195 "GJavaParser.g"
                self.setResult(
                    ##line 195 GJavaParser.g
                    LPGUserAction4(self.getRhsIToken(1))
                ##line 195 GJavaParser.g
                )

         self.__rule_action[9]= Act9

        #
        # Rule 10:  Type ::= PrimitiveType
        #
        
                 
        #
        # Rule 11:  Type ::= ReferenceType
        #
        
                 
        #
        # Rule 12:  PrimitiveType ::= NumericType
        #
        
                 
        #
        # Rule 13:  PrimitiveType ::= boolean
        #
         def Act13(): 
               ##line 204 "GJavaParser.g"
                self.setResult(
                    ##line 204 GJavaParser.g
                    PrimitiveType(self.getRhsIToken(1))
                ##line 204 GJavaParser.g
                )

         self.__rule_action[13]= Act13

        #
        # Rule 14:  NumericType ::= IntegralType
        #
        
                 
        #
        # Rule 15:  NumericType ::= FloatingPointType
        #
        
                 
        #
        # Rule 16:  IntegralType ::= byte
        #
         def Act16(): 
               ##line 209 "GJavaParser.g"
                self.setResult(
                    ##line 209 GJavaParser.g
                    IntegralType0(self.getRhsIToken(1))
                ##line 209 GJavaParser.g
                )

         self.__rule_action[16]= Act16

        #
        # Rule 17:  IntegralType ::= short
        #
         def Act17(): 
               ##line 210 "GJavaParser.g"
                self.setResult(
                    ##line 210 GJavaParser.g
                    IntegralType1(self.getRhsIToken(1))
                ##line 210 GJavaParser.g
                )

         self.__rule_action[17]= Act17

        #
        # Rule 18:  IntegralType ::= int
        #
         def Act18(): 
               ##line 211 "GJavaParser.g"
                self.setResult(
                    ##line 211 GJavaParser.g
                    IntegralType2(self.getRhsIToken(1))
                ##line 211 GJavaParser.g
                )

         self.__rule_action[18]= Act18

        #
        # Rule 19:  IntegralType ::= long
        #
         def Act19(): 
               ##line 212 "GJavaParser.g"
                self.setResult(
                    ##line 212 GJavaParser.g
                    IntegralType3(self.getRhsIToken(1))
                ##line 212 GJavaParser.g
                )

         self.__rule_action[19]= Act19

        #
        # Rule 20:  IntegralType ::= char
        #
         def Act20(): 
               ##line 213 "GJavaParser.g"
                self.setResult(
                    ##line 213 GJavaParser.g
                    IntegralType4(self.getRhsIToken(1))
                ##line 213 GJavaParser.g
                )

         self.__rule_action[20]= Act20

        #
        # Rule 21:  FloatingPointType ::= float
        #
         def Act21(): 
               ##line 215 "GJavaParser.g"
                self.setResult(
                    ##line 215 GJavaParser.g
                    FloatingPointType0(self.getRhsIToken(1))
                ##line 215 GJavaParser.g
                )

         self.__rule_action[21]= Act21

        #
        # Rule 22:  FloatingPointType ::= double
        #
         def Act22(): 
               ##line 216 "GJavaParser.g"
                self.setResult(
                    ##line 216 GJavaParser.g
                    FloatingPointType1(self.getRhsIToken(1))
                ##line 216 GJavaParser.g
                )

         self.__rule_action[22]= Act22

        #
        # Rule 23:  ReferenceType ::= ClassOrInterfaceType
        #
        
                 
        #
        # Rule 24:  ReferenceType ::= TypeVariable
        #
        
                 
        #
        # Rule 25:  ReferenceType ::= ArrayType
        #
        
                 
        #
        # Rule 26:  ClassOrInterfaceType ::= ClassType
        #
        
                 
        #
        # Rule 27:  ClassType ::= TypeName TypeArgumentsopt
        #
         def Act27(): 
               ##line 228 "GJavaParser.g"
                self.setResult(
                    ##line 228 GJavaParser.g
                    ClassType(self.getLeftIToken(), self.getRightIToken(),
                              ##line 228 GJavaParser.g
                              self.getRhsSym(1),
                              ##line 228 GJavaParser.g
                              self.getRhsSym(2))
                ##line 228 GJavaParser.g
                )

         self.__rule_action[27]= Act27

        #
        # Rule 28:  InterfaceType ::= TypeName TypeArgumentsopt
        #
         def Act28(): 
               ##line 230 "GJavaParser.g"
                self.setResult(
                    ##line 230 GJavaParser.g
                    InterfaceType(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 230 GJavaParser.g
                                  self.getRhsSym(1),
                                  ##line 230 GJavaParser.g
                                  self.getRhsSym(2))
                ##line 230 GJavaParser.g
                )

         self.__rule_action[28]= Act28

        #
        # Rule 29:  TypeName ::= identifier
        #
        
                 
        #
        # Rule 30:  TypeName ::= TypeName . identifier
        #
         def Act30(): 
               ##line 233 "GJavaParser.g"
                self.setResult(
                    ##line 233 GJavaParser.g
                    TypeName(self.getLeftIToken(), self.getRightIToken(),
                             ##line 233 GJavaParser.g
                             self.getRhsSym(1),
                             ##line 233 GJavaParser.g
                             AstToken(self.getRhsIToken(2)),
                             ##line 233 GJavaParser.g
                             self.getRhsSym(3))
                ##line 233 GJavaParser.g
                )

         self.__rule_action[30]= Act30

        #
        # Rule 31:  ClassName ::= TypeName
        #
        
                 
        #
        # Rule 32:  TypeVariable ::= identifier
        #
        
                 
        #
        # Rule 33:  ArrayType ::= Type [ ]
        #
         def Act33(): 
               ##line 239 "GJavaParser.g"
                self.setResult(
                    ##line 239 GJavaParser.g
                    ArrayType(self.getLeftIToken(), self.getRightIToken(),
                              ##line 239 GJavaParser.g
                              self.getRhsSym(1),
                              ##line 239 GJavaParser.g
                              AstToken(self.getRhsIToken(2)),
                              ##line 239 GJavaParser.g
                              AstToken(self.getRhsIToken(3)))
                ##line 239 GJavaParser.g
                )

         self.__rule_action[33]= Act33

        #
        # Rule 34:  TypeParameter ::= TypeVariable TypeBoundopt
        #
         def Act34(): 
               ##line 241 "GJavaParser.g"
                self.setResult(
                    ##line 241 GJavaParser.g
                    TypeParameter(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 241 GJavaParser.g
                                  self.getRhsSym(1),
                                  ##line 241 GJavaParser.g
                                  self.getRhsSym(2))
                ##line 241 GJavaParser.g
                )

         self.__rule_action[34]= Act34

        #
        # Rule 35:  TypeBound ::= extends ClassOrInterfaceType AdditionalBoundListopt
        #
         def Act35(): 
               ##line 243 "GJavaParser.g"
                self.setResult(
                    ##line 243 GJavaParser.g
                    TypeBound(self.getLeftIToken(), self.getRightIToken(),
                              ##line 243 GJavaParser.g
                              AstToken(self.getRhsIToken(1)),
                              ##line 243 GJavaParser.g
                              self.getRhsSym(2),
                              ##line 243 GJavaParser.g
                              self.getRhsSym(3))
                ##line 243 GJavaParser.g
                )

         self.__rule_action[35]= Act35

        #
        # Rule 36:  AdditionalBoundList ::= AdditionalBound
        #
        
                 
        #
        # Rule 37:  AdditionalBoundList ::= AdditionalBoundList AdditionalBound
        #
         def Act37(): 
               ##line 246 "GJavaParser.g"
                self.setResult(
                    ##line 246 GJavaParser.g
                    AdditionalBoundList(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 246 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 246 GJavaParser.g
                                        self.getRhsSym(2))
                ##line 246 GJavaParser.g
                )

         self.__rule_action[37]= Act37

        #
        # Rule 38:  AdditionalBound ::= & InterfaceType
        #
         def Act38(): 
               ##line 248 "GJavaParser.g"
                self.setResult(
                    ##line 248 GJavaParser.g
                    AdditionalBound(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 248 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 248 GJavaParser.g
                                    self.getRhsSym(2))
                ##line 248 GJavaParser.g
                )

         self.__rule_action[38]= Act38

        #
        # Rule 39:  TypeArguments ::= < ActualTypeArgumentList >
        #
         def Act39(): 
               ##line 250 "GJavaParser.g"
                self.setResult(
                    ##line 250 GJavaParser.g
                    TypeArguments(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 250 GJavaParser.g
                                  AstToken(self.getRhsIToken(1)),
                                  ##line 250 GJavaParser.g
                                  self.getRhsSym(2),
                                  ##line 250 GJavaParser.g
                                  AstToken(self.getRhsIToken(3)))
                ##line 250 GJavaParser.g
                )

         self.__rule_action[39]= Act39

        #
        # Rule 40:  ActualTypeArgumentList ::= ActualTypeArgument
        #
        
                 
        #
        # Rule 41:  ActualTypeArgumentList ::= ActualTypeArgumentList , ActualTypeArgument
        #
         def Act41(): 
               ##line 253 "GJavaParser.g"
                self.setResult(
                    ##line 253 GJavaParser.g
                    ActualTypeArgumentList(self.getLeftIToken(), self.getRightIToken(),
                                           ##line 253 GJavaParser.g
                                           self.getRhsSym(1),
                                           ##line 253 GJavaParser.g
                                           AstToken(self.getRhsIToken(2)),
                                           ##line 253 GJavaParser.g
                                           self.getRhsSym(3))
                ##line 253 GJavaParser.g
                )

         self.__rule_action[41]= Act41

        #
        # Rule 42:  ActualTypeArgument ::= ReferenceType
        #
        
                 
        #
        # Rule 43:  ActualTypeArgument ::= Wildcard
        #
        
                 
        #
        # Rule 44:  Wildcard ::= ? WildcardBoundsOpt
        #
         def Act44(): 
               ##line 258 "GJavaParser.g"
                self.setResult(
                    ##line 258 GJavaParser.g
                    Wildcard(self.getLeftIToken(), self.getRightIToken(),
                             ##line 258 GJavaParser.g
                             AstToken(self.getRhsIToken(1)),
                             ##line 258 GJavaParser.g
                             self.getRhsSym(2))
                ##line 258 GJavaParser.g
                )

         self.__rule_action[44]= Act44

        #
        # Rule 45:  WildcardBounds ::= extends ReferenceType
        #
         def Act45(): 
               ##line 260 "GJavaParser.g"
                self.setResult(
                    ##line 260 GJavaParser.g
                    WildcardBounds0(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 260 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 260 GJavaParser.g
                                    self.getRhsSym(2))
                ##line 260 GJavaParser.g
                )

         self.__rule_action[45]= Act45

        #
        # Rule 46:  WildcardBounds ::= super ReferenceType
        #
         def Act46(): 
               ##line 261 "GJavaParser.g"
                self.setResult(
                    ##line 261 GJavaParser.g
                    WildcardBounds1(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 261 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 261 GJavaParser.g
                                    self.getRhsSym(2))
                ##line 261 GJavaParser.g
                )

         self.__rule_action[46]= Act46

        #
        # Rule 47:  PackageName ::= identifier
        #
        
                 
        #
        # Rule 48:  PackageName ::= PackageName . identifier
        #
         def Act48(): 
               ##line 268 "GJavaParser.g"
                self.setResult(
                    ##line 268 GJavaParser.g
                    PackageName(self.getLeftIToken(), self.getRightIToken(),
                                ##line 268 GJavaParser.g
                                self.getRhsSym(1),
                                ##line 268 GJavaParser.g
                                AstToken(self.getRhsIToken(2)),
                                ##line 268 GJavaParser.g
                                self.getRhsSym(3))
                ##line 268 GJavaParser.g
                )

         self.__rule_action[48]= Act48

        #
        # Rule 49:  ExpressionName ::= identifier
        #
        
                 
        #
        # Rule 50:  ExpressionName ::= AmbiguousName . identifier
        #
         def Act50(): 
               ##line 277 "GJavaParser.g"
                self.setResult(
                    ##line 277 GJavaParser.g
                    ExpressionName(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 277 GJavaParser.g
                                   self.getRhsSym(1),
                                   ##line 277 GJavaParser.g
                                   AstToken(self.getRhsIToken(2)),
                                   ##line 277 GJavaParser.g
                                   self.getRhsSym(3))
                ##line 277 GJavaParser.g
                )

         self.__rule_action[50]= Act50

        #
        # Rule 51:  MethodName ::= identifier
        #
        
                 
        #
        # Rule 52:  MethodName ::= AmbiguousName . identifier
        #
         def Act52(): 
               ##line 280 "GJavaParser.g"
                self.setResult(
                    ##line 280 GJavaParser.g
                    MethodName(self.getLeftIToken(), self.getRightIToken(),
                               ##line 280 GJavaParser.g
                               self.getRhsSym(1),
                               ##line 280 GJavaParser.g
                               AstToken(self.getRhsIToken(2)),
                               ##line 280 GJavaParser.g
                               self.getRhsSym(3))
                ##line 280 GJavaParser.g
                )

         self.__rule_action[52]= Act52

        #
        # Rule 53:  PackageOrTypeName ::= identifier
        #
        
                 
        #
        # Rule 54:  PackageOrTypeName ::= PackageOrTypeName . identifier
        #
         def Act54(): 
               ##line 283 "GJavaParser.g"
                self.setResult(
                    ##line 283 GJavaParser.g
                    PackageOrTypeName(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 283 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 283 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 283 GJavaParser.g
                                      self.getRhsSym(3))
                ##line 283 GJavaParser.g
                )

         self.__rule_action[54]= Act54

        #
        # Rule 55:  AmbiguousName ::= identifier
        #
        
                 
        #
        # Rule 56:  AmbiguousName ::= AmbiguousName . identifier
        #
         def Act56(): 
               ##line 286 "GJavaParser.g"
                self.setResult(
                    ##line 286 GJavaParser.g
                    AmbiguousName(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 286 GJavaParser.g
                                  self.getRhsSym(1),
                                  ##line 286 GJavaParser.g
                                  AstToken(self.getRhsIToken(2)),
                                  ##line 286 GJavaParser.g
                                  self.getRhsSym(3))
                ##line 286 GJavaParser.g
                )

         self.__rule_action[56]= Act56

        #
        # Rule 57:  CompilationUnit ::= PackageDeclarationopt ImportDeclarationsopt TypeDeclarationsopt
        #
         def Act57(): 
               ##line 290 "GJavaParser.g"
                self.setResult(
                    ##line 290 GJavaParser.g
                    CompilationUnit(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 290 GJavaParser.g
                                    self.getRhsSym(1),
                                    ##line 290 GJavaParser.g
                                    self.getRhsSym(2),
                                    ##line 290 GJavaParser.g
                                    self.getRhsSym(3))
                ##line 290 GJavaParser.g
                )

         self.__rule_action[57]= Act57

        #
        # Rule 58:  ImportDeclarations ::= ImportDeclaration
        #
        
                 
        #
        # Rule 59:  ImportDeclarations ::= ImportDeclarations ImportDeclaration
        #
         def Act59(): 
               ##line 293 "GJavaParser.g"
                self.setResult(
                    ##line 293 GJavaParser.g
                    ImportDeclarations(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 293 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 293 GJavaParser.g
                                       self.getRhsSym(2))
                ##line 293 GJavaParser.g
                )

         self.__rule_action[59]= Act59

        #
        # Rule 60:  TypeDeclarations ::= TypeDeclaration
        #
        
                 
        #
        # Rule 61:  TypeDeclarations ::= TypeDeclarations TypeDeclaration
        #
         def Act61(): 
               ##line 296 "GJavaParser.g"
                self.setResult(
                    ##line 296 GJavaParser.g
                    TypeDeclarations(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 296 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 296 GJavaParser.g
                                     self.getRhsSym(2))
                ##line 296 GJavaParser.g
                )

         self.__rule_action[61]= Act61

        #
        # Rule 62:  PackageDeclaration ::= Annotationsopt package PackageName ;
        #
         def Act62(): 
               ##line 298 "GJavaParser.g"
                self.setResult(
                    ##line 298 GJavaParser.g
                    PackageDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 298 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 298 GJavaParser.g
                                       AstToken(self.getRhsIToken(2)),
                                       ##line 298 GJavaParser.g
                                       self.getRhsSym(3),
                                       ##line 298 GJavaParser.g
                                       AstToken(self.getRhsIToken(4)))
                ##line 298 GJavaParser.g
                )

         self.__rule_action[62]= Act62

        #
        # Rule 63:  ImportDeclaration ::= SingleTypeImportDeclaration
        #
        
                 
        #
        # Rule 64:  ImportDeclaration ::= TypeImportOnDemandDeclaration
        #
        
                 
        #
        # Rule 65:  ImportDeclaration ::= SingleStaticImportDeclaration
        #
        
                 
        #
        # Rule 66:  ImportDeclaration ::= StaticImportOnDemandDeclaration
        #
        
                 
        #
        # Rule 67:  SingleTypeImportDeclaration ::= import TypeName ;
        #
         def Act67(): 
               ##line 305 "GJavaParser.g"
                self.setResult(
                    ##line 305 GJavaParser.g
                    SingleTypeImportDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                                ##line 305 GJavaParser.g
                                                AstToken(self.getRhsIToken(1)),
                                                ##line 305 GJavaParser.g
                                                self.getRhsSym(2),
                                                ##line 305 GJavaParser.g
                                                AstToken(self.getRhsIToken(3)))
                ##line 305 GJavaParser.g
                )

         self.__rule_action[67]= Act67

        #
        # Rule 68:  TypeImportOnDemandDeclaration ::= import PackageOrTypeName . * ;
        #
         def Act68(): 
               ##line 307 "GJavaParser.g"
                self.setResult(
                    ##line 307 GJavaParser.g
                    TypeImportOnDemandDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                                  ##line 307 GJavaParser.g
                                                  AstToken(self.getRhsIToken(1)),
                                                  ##line 307 GJavaParser.g
                                                  self.getRhsSym(2),
                                                  ##line 307 GJavaParser.g
                                                  AstToken(self.getRhsIToken(3)),
                                                  ##line 307 GJavaParser.g
                                                  AstToken(self.getRhsIToken(4)),
                                                  ##line 307 GJavaParser.g
                                                  AstToken(self.getRhsIToken(5)))
                ##line 307 GJavaParser.g
                )

         self.__rule_action[68]= Act68

        #
        # Rule 69:  SingleStaticImportDeclaration ::= import static TypeName . identifier ;
        #
         def Act69(): 
               ##line 309 "GJavaParser.g"
                self.setResult(
                    ##line 309 GJavaParser.g
                    SingleStaticImportDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                                  ##line 309 GJavaParser.g
                                                  AstToken(self.getRhsIToken(1)),
                                                  ##line 309 GJavaParser.g
                                                  AstToken(self.getRhsIToken(2)),
                                                  ##line 309 GJavaParser.g
                                                  self.getRhsSym(3),
                                                  ##line 309 GJavaParser.g
                                                  AstToken(self.getRhsIToken(4)),
                                                  ##line 309 GJavaParser.g
                                                  self.getRhsSym(5),
                                                  ##line 309 GJavaParser.g
                                                  AstToken(self.getRhsIToken(6)))
                ##line 309 GJavaParser.g
                )

         self.__rule_action[69]= Act69

        #
        # Rule 70:  StaticImportOnDemandDeclaration ::= import static TypeName . * ;
        #
         def Act70(): 
               ##line 311 "GJavaParser.g"
                self.setResult(
                    ##line 311 GJavaParser.g
                    StaticImportOnDemandDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                                    ##line 311 GJavaParser.g
                                                    AstToken(self.getRhsIToken(1)),
                                                    ##line 311 GJavaParser.g
                                                    AstToken(self.getRhsIToken(2)),
                                                    ##line 311 GJavaParser.g
                                                    self.getRhsSym(3),
                                                    ##line 311 GJavaParser.g
                                                    AstToken(self.getRhsIToken(4)),
                                                    ##line 311 GJavaParser.g
                                                    AstToken(self.getRhsIToken(5)),
                                                    ##line 311 GJavaParser.g
                                                    AstToken(self.getRhsIToken(6)))
                ##line 311 GJavaParser.g
                )

         self.__rule_action[70]= Act70

        #
        # Rule 71:  TypeDeclaration ::= ClassDeclaration
        #
        
                 
        #
        # Rule 72:  TypeDeclaration ::= InterfaceDeclaration
        #
        
                 
        #
        # Rule 73:  TypeDeclaration ::= ;
        #
         def Act73(): 
               ##line 315 "GJavaParser.g"
                self.setResult(
                    ##line 315 GJavaParser.g
                    TypeDeclaration(self.getRhsIToken(1))
                ##line 315 GJavaParser.g
                )

         self.__rule_action[73]= Act73

        #
        # Rule 74:  ClassDeclaration ::= NormalClassDeclaration
        #
        
                 
        #
        # Rule 75:  ClassDeclaration ::= EnumDeclaration
        #
        
                 
        #
        # Rule 76:  NormalClassDeclaration ::= ClassModifiersopt class identifier TypeParametersopt Superopt Interfacesopt ClassBody
        #
         def Act76(): 
               ##line 322 "GJavaParser.g"
                self.setResult(
                    ##line 322 GJavaParser.g
                    NormalClassDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                           ##line 322 GJavaParser.g
                                           self.getRhsSym(1),
                                           ##line 322 GJavaParser.g
                                           AstToken(self.getRhsIToken(2)),
                                           ##line 322 GJavaParser.g
                                           self.getRhsSym(3),
                                           ##line 322 GJavaParser.g
                                           self.getRhsSym(4),
                                           ##line 322 GJavaParser.g
                                           self.getRhsSym(5),
                                           ##line 322 GJavaParser.g
                                           self.getRhsSym(6),
                                           ##line 322 GJavaParser.g
                                           self.getRhsSym(7))
                ##line 322 GJavaParser.g
                )

         self.__rule_action[76]= Act76

        #
        # Rule 77:  ClassModifiers ::= ClassModifier
        #
        
                 
        #
        # Rule 78:  ClassModifiers ::= ClassModifiers ClassModifier
        #
         def Act78(): 
               ##line 325 "GJavaParser.g"
                self.setResult(
                    ##line 325 GJavaParser.g
                    ClassModifiers(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 325 GJavaParser.g
                                   self.getRhsSym(1),
                                   ##line 325 GJavaParser.g
                                   self.getRhsSym(2))
                ##line 325 GJavaParser.g
                )

         self.__rule_action[78]= Act78

        #
        # Rule 79:  ClassModifier ::= Annotation
        #
        
                 
        #
        # Rule 80:  ClassModifier ::= public
        #
         def Act80(): 
               ##line 328 "GJavaParser.g"
                self.setResult(
                    ##line 328 GJavaParser.g
                    ClassModifier0(self.getRhsIToken(1))
                ##line 328 GJavaParser.g
                )

         self.__rule_action[80]= Act80

        #
        # Rule 81:  ClassModifier ::= protected
        #
         def Act81(): 
               ##line 329 "GJavaParser.g"
                self.setResult(
                    ##line 329 GJavaParser.g
                    ClassModifier1(self.getRhsIToken(1))
                ##line 329 GJavaParser.g
                )

         self.__rule_action[81]= Act81

        #
        # Rule 82:  ClassModifier ::= private
        #
         def Act82(): 
               ##line 330 "GJavaParser.g"
                self.setResult(
                    ##line 330 GJavaParser.g
                    ClassModifier2(self.getRhsIToken(1))
                ##line 330 GJavaParser.g
                )

         self.__rule_action[82]= Act82

        #
        # Rule 83:  ClassModifier ::= abstract
        #
         def Act83(): 
               ##line 331 "GJavaParser.g"
                self.setResult(
                    ##line 331 GJavaParser.g
                    ClassModifier3(self.getRhsIToken(1))
                ##line 331 GJavaParser.g
                )

         self.__rule_action[83]= Act83

        #
        # Rule 84:  ClassModifier ::= static
        #
         def Act84(): 
               ##line 332 "GJavaParser.g"
                self.setResult(
                    ##line 332 GJavaParser.g
                    ClassModifier4(self.getRhsIToken(1))
                ##line 332 GJavaParser.g
                )

         self.__rule_action[84]= Act84

        #
        # Rule 85:  ClassModifier ::= final
        #
         def Act85(): 
               ##line 333 "GJavaParser.g"
                self.setResult(
                    ##line 333 GJavaParser.g
                    ClassModifier5(self.getRhsIToken(1))
                ##line 333 GJavaParser.g
                )

         self.__rule_action[85]= Act85

        #
        # Rule 86:  ClassModifier ::= strictfp
        #
         def Act86(): 
               ##line 334 "GJavaParser.g"
                self.setResult(
                    ##line 334 GJavaParser.g
                    ClassModifier6(self.getRhsIToken(1))
                ##line 334 GJavaParser.g
                )

         self.__rule_action[86]= Act86

        #
        # Rule 87:  TypeParameters ::= < TypeParameterList >
        #
         def Act87(): 
               ##line 336 "GJavaParser.g"
                self.setResult(
                    ##line 336 GJavaParser.g
                    TypeParameters(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 336 GJavaParser.g
                                   AstToken(self.getRhsIToken(1)),
                                   ##line 336 GJavaParser.g
                                   self.getRhsSym(2),
                                   ##line 336 GJavaParser.g
                                   AstToken(self.getRhsIToken(3)))
                ##line 336 GJavaParser.g
                )

         self.__rule_action[87]= Act87

        #
        # Rule 88:  TypeParameterList ::= TypeParameter
        #
        
                 
        #
        # Rule 89:  TypeParameterList ::= TypeParameterList , TypeParameter
        #
         def Act89(): 
               ##line 339 "GJavaParser.g"
                self.setResult(
                    ##line 339 GJavaParser.g
                    TypeParameterList(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 339 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 339 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 339 GJavaParser.g
                                      self.getRhsSym(3))
                ##line 339 GJavaParser.g
                )

         self.__rule_action[89]= Act89

        #
        # Rule 90:  Super ::= extends ClassType
        #
         def Act90(): 
               ##line 341 "GJavaParser.g"
                self.setResult(
                    ##line 341 GJavaParser.g
                    Super(self.getLeftIToken(), self.getRightIToken(),
                          ##line 341 GJavaParser.g
                          AstToken(self.getRhsIToken(1)),
                          ##line 341 GJavaParser.g
                          self.getRhsSym(2))
                ##line 341 GJavaParser.g
                )

         self.__rule_action[90]= Act90

        #
        # Rule 91:  Interfaces ::= implements InterfaceTypeList
        #
         def Act91(): 
               ##line 348 "GJavaParser.g"
                self.setResult(
                    ##line 348 GJavaParser.g
                    Interfaces(self.getLeftIToken(), self.getRightIToken(),
                               ##line 348 GJavaParser.g
                               AstToken(self.getRhsIToken(1)),
                               ##line 348 GJavaParser.g
                               self.getRhsSym(2))
                ##line 348 GJavaParser.g
                )

         self.__rule_action[91]= Act91

        #
        # Rule 92:  InterfaceTypeList ::= InterfaceType
        #
        
                 
        #
        # Rule 93:  InterfaceTypeList ::= InterfaceTypeList , InterfaceType
        #
         def Act93(): 
               ##line 351 "GJavaParser.g"
                self.setResult(
                    ##line 351 GJavaParser.g
                    InterfaceTypeList(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 351 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 351 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 351 GJavaParser.g
                                      self.getRhsSym(3))
                ##line 351 GJavaParser.g
                )

         self.__rule_action[93]= Act93

        #
        # Rule 94:  ClassBody ::= { ClassBodyDeclarationsopt }
        #
         def Act94(): 
               ##line 358 "GJavaParser.g"
                self.setResult(
                    ##line 358 GJavaParser.g
                    ClassBody(self.getLeftIToken(), self.getRightIToken(),
                              ##line 358 GJavaParser.g
                              AstToken(self.getRhsIToken(1)),
                              ##line 358 GJavaParser.g
                              self.getRhsSym(2),
                              ##line 358 GJavaParser.g
                              AstToken(self.getRhsIToken(3)))
                ##line 358 GJavaParser.g
                )

         self.__rule_action[94]= Act94

        #
        # Rule 95:  ClassBodyDeclarations ::= ClassBodyDeclaration
        #
        
                 
        #
        # Rule 96:  ClassBodyDeclarations ::= ClassBodyDeclarations ClassBodyDeclaration
        #
         def Act96(): 
               ##line 361 "GJavaParser.g"
                self.setResult(
                    ##line 361 GJavaParser.g
                    ClassBodyDeclarations(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 361 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 361 GJavaParser.g
                                          self.getRhsSym(2))
                ##line 361 GJavaParser.g
                )

         self.__rule_action[96]= Act96

        #
        # Rule 97:  ClassBodyDeclaration ::= ClassMemberDeclaration
        #
        
                 
        #
        # Rule 98:  ClassBodyDeclaration ::= InstanceInitializer
        #
        
                 
        #
        # Rule 99:  ClassBodyDeclaration ::= StaticInitializer
        #
        
                 
        #
        # Rule 100:  ClassBodyDeclaration ::= ConstructorDeclaration
        #
        
                 
        #
        # Rule 101:  ClassMemberDeclaration ::= FieldDeclaration
        #
        
                 
        #
        # Rule 102:  ClassMemberDeclaration ::= MethodDeclaration
        #
        
                 
        #
        # Rule 103:  ClassMemberDeclaration ::= ClassDeclaration
        #
        
                 
        #
        # Rule 104:  ClassMemberDeclaration ::= InterfaceDeclaration
        #
        
                 
        #
        # Rule 105:  ClassMemberDeclaration ::= ;
        #
         def Act105(): 
               ##line 372 "GJavaParser.g"
                self.setResult(
                    ##line 372 GJavaParser.g
                    ClassMemberDeclaration(self.getRhsIToken(1))
                ##line 372 GJavaParser.g
                )

         self.__rule_action[105]= Act105

        #
        # Rule 106:  FieldDeclaration ::= FieldModifiersopt Type VariableDeclarators ;
        #
         def Act106(): 
               ##line 374 "GJavaParser.g"
                self.setResult(
                    ##line 374 GJavaParser.g
                    FieldDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 374 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 374 GJavaParser.g
                                     self.getRhsSym(2),
                                     ##line 374 GJavaParser.g
                                     self.getRhsSym(3),
                                     ##line 374 GJavaParser.g
                                     AstToken(self.getRhsIToken(4)))
                ##line 374 GJavaParser.g
                )

         self.__rule_action[106]= Act106

        #
        # Rule 107:  VariableDeclarators ::= VariableDeclarator
        #
        
                 
        #
        # Rule 108:  VariableDeclarators ::= VariableDeclarators , VariableDeclarator
        #
         def Act108(): 
               ##line 377 "GJavaParser.g"
                self.setResult(
                    ##line 377 GJavaParser.g
                    VariableDeclarators(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 377 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 377 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 377 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 377 GJavaParser.g
                )

         self.__rule_action[108]= Act108

        #
        # Rule 109:  VariableDeclarator ::= VariableDeclaratorId
        #
        
                 
        #
        # Rule 110:  VariableDeclarator ::= VariableDeclaratorId = VariableInitializer
        #
         def Act110(): 
               ##line 380 "GJavaParser.g"
                self.setResult(
                    ##line 380 GJavaParser.g
                    VariableDeclarator(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 380 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 380 GJavaParser.g
                                       AstToken(self.getRhsIToken(2)),
                                       ##line 380 GJavaParser.g
                                       self.getRhsSym(3))
                ##line 380 GJavaParser.g
                )

         self.__rule_action[110]= Act110

        #
        # Rule 111:  VariableDeclaratorId ::= identifier
        #
        
                 
        #
        # Rule 112:  VariableDeclaratorId ::= VariableDeclaratorId [ ]
        #
         def Act112(): 
               ##line 383 "GJavaParser.g"
                self.setResult(
                    ##line 383 GJavaParser.g
                    VariableDeclaratorId(self.getLeftIToken(), self.getRightIToken(),
                                         ##line 383 GJavaParser.g
                                         self.getRhsSym(1),
                                         ##line 383 GJavaParser.g
                                         AstToken(self.getRhsIToken(2)),
                                         ##line 383 GJavaParser.g
                                         AstToken(self.getRhsIToken(3)))
                ##line 383 GJavaParser.g
                )

         self.__rule_action[112]= Act112

        #
        # Rule 113:  VariableInitializer ::= Expression
        #
        
                 
        #
        # Rule 114:  VariableInitializer ::= ArrayInitializer
        #
        
                 
        #
        # Rule 115:  FieldModifiers ::= FieldModifier
        #
        
                 
        #
        # Rule 116:  FieldModifiers ::= FieldModifiers FieldModifier
        #
         def Act116(): 
               ##line 389 "GJavaParser.g"
                self.setResult(
                    ##line 389 GJavaParser.g
                    FieldModifiers(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 389 GJavaParser.g
                                   self.getRhsSym(1),
                                   ##line 389 GJavaParser.g
                                   self.getRhsSym(2))
                ##line 389 GJavaParser.g
                )

         self.__rule_action[116]= Act116

        #
        # Rule 117:  FieldModifier ::= Annotation
        #
        
                 
        #
        # Rule 118:  FieldModifier ::= public
        #
         def Act118(): 
               ##line 392 "GJavaParser.g"
                self.setResult(
                    ##line 392 GJavaParser.g
                    FieldModifier0(self.getRhsIToken(1))
                ##line 392 GJavaParser.g
                )

         self.__rule_action[118]= Act118

        #
        # Rule 119:  FieldModifier ::= protected
        #
         def Act119(): 
               ##line 393 "GJavaParser.g"
                self.setResult(
                    ##line 393 GJavaParser.g
                    FieldModifier1(self.getRhsIToken(1))
                ##line 393 GJavaParser.g
                )

         self.__rule_action[119]= Act119

        #
        # Rule 120:  FieldModifier ::= private
        #
         def Act120(): 
               ##line 394 "GJavaParser.g"
                self.setResult(
                    ##line 394 GJavaParser.g
                    FieldModifier2(self.getRhsIToken(1))
                ##line 394 GJavaParser.g
                )

         self.__rule_action[120]= Act120

        #
        # Rule 121:  FieldModifier ::= static
        #
         def Act121(): 
               ##line 395 "GJavaParser.g"
                self.setResult(
                    ##line 395 GJavaParser.g
                    FieldModifier3(self.getRhsIToken(1))
                ##line 395 GJavaParser.g
                )

         self.__rule_action[121]= Act121

        #
        # Rule 122:  FieldModifier ::= final
        #
         def Act122(): 
               ##line 396 "GJavaParser.g"
                self.setResult(
                    ##line 396 GJavaParser.g
                    FieldModifier4(self.getRhsIToken(1))
                ##line 396 GJavaParser.g
                )

         self.__rule_action[122]= Act122

        #
        # Rule 123:  FieldModifier ::= transient
        #
         def Act123(): 
               ##line 397 "GJavaParser.g"
                self.setResult(
                    ##line 397 GJavaParser.g
                    FieldModifier5(self.getRhsIToken(1))
                ##line 397 GJavaParser.g
                )

         self.__rule_action[123]= Act123

        #
        # Rule 124:  FieldModifier ::= volatile
        #
         def Act124(): 
               ##line 398 "GJavaParser.g"
                self.setResult(
                    ##line 398 GJavaParser.g
                    FieldModifier6(self.getRhsIToken(1))
                ##line 398 GJavaParser.g
                )

         self.__rule_action[124]= Act124

        #
        # Rule 125:  MethodDeclaration ::= MethodHeader MethodBody
        #
         def Act125(): 
               ##line 400 "GJavaParser.g"
                self.setResult(
                    ##line 400 GJavaParser.g
                    MethodDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 400 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 400 GJavaParser.g
                                      self.getRhsSym(2))
                ##line 400 GJavaParser.g
                )

         self.__rule_action[125]= Act125

        #
        # Rule 126:  MethodHeader ::= MethodModifiersopt TypeParametersopt ResultType MethodDeclarator Throwsopt
        #
         def Act126(): 
               ##line 402 "GJavaParser.g"
                self.setResult(
                    ##line 402 GJavaParser.g
                    MethodHeader(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 402 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 402 GJavaParser.g
                                 self.getRhsSym(2),
                                 ##line 402 GJavaParser.g
                                 self.getRhsSym(3),
                                 ##line 402 GJavaParser.g
                                 self.getRhsSym(4),
                                 ##line 402 GJavaParser.g
                                 self.getRhsSym(5))
                ##line 402 GJavaParser.g
                )

         self.__rule_action[126]= Act126

        #
        # Rule 127:  ResultType ::= Type
        #
        
                 
        #
        # Rule 128:  ResultType ::= void
        #
         def Act128(): 
               ##line 405 "GJavaParser.g"
                self.setResult(
                    ##line 405 GJavaParser.g
                    ResultType(self.getRhsIToken(1))
                ##line 405 GJavaParser.g
                )

         self.__rule_action[128]= Act128

        #
        # Rule 129:  MethodDeclarator ::= identifier ( FormalParameterListopt )
        #
         def Act129(): 
               ##line 407 "GJavaParser.g"
                self.setResult(
                    ##line 407 GJavaParser.g
                    MethodDeclarator0(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 407 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 407 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 407 GJavaParser.g
                                      self.getRhsSym(3),
                                      ##line 407 GJavaParser.g
                                      AstToken(self.getRhsIToken(4)))
                ##line 407 GJavaParser.g
                )

         self.__rule_action[129]= Act129

        #
        # Rule 130:  MethodDeclarator ::= MethodDeclarator [ ]
        #
         def Act130(): 
               ##line 409 "GJavaParser.g"
                self.setResult(
                    ##line 409 GJavaParser.g
                    MethodDeclarator1(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 409 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 409 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 409 GJavaParser.g
                                      AstToken(self.getRhsIToken(3)))
                ##line 409 GJavaParser.g
                )

         self.__rule_action[130]= Act130

        #
        # Rule 131:  FormalParameterList ::= LastFormalParameter
        #
        
                 
        #
        # Rule 132:  FormalParameterList ::= FormalParameters , LastFormalParameter
        #
         def Act132(): 
               ##line 412 "GJavaParser.g"
                self.setResult(
                    ##line 412 GJavaParser.g
                    FormalParameterList(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 412 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 412 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 412 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 412 GJavaParser.g
                )

         self.__rule_action[132]= Act132

        #
        # Rule 133:  FormalParameters ::= FormalParameter
        #
        
                 
        #
        # Rule 134:  FormalParameters ::= FormalParameters , FormalParameter
        #
         def Act134(): 
               ##line 415 "GJavaParser.g"
                self.setResult(
                    ##line 415 GJavaParser.g
                    FormalParameters(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 415 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 415 GJavaParser.g
                                     AstToken(self.getRhsIToken(2)),
                                     ##line 415 GJavaParser.g
                                     self.getRhsSym(3))
                ##line 415 GJavaParser.g
                )

         self.__rule_action[134]= Act134

        #
        # Rule 135:  FormalParameter ::= VariableModifiersopt Type VariableDeclaratorId
        #
         def Act135(): 
               ##line 417 "GJavaParser.g"
                self.setResult(
                    ##line 417 GJavaParser.g
                    FormalParameter(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 417 GJavaParser.g
                                    self.getRhsSym(1),
                                    ##line 417 GJavaParser.g
                                    self.getRhsSym(2),
                                    ##line 417 GJavaParser.g
                                    self.getRhsSym(3))
                ##line 417 GJavaParser.g
                )

         self.__rule_action[135]= Act135

        #
        # Rule 136:  VariableModifiers ::= VariableModifier
        #
        
                 
        #
        # Rule 137:  VariableModifiers ::= VariableModifiers VariableModifier
        #
         def Act137(): 
               ##line 420 "GJavaParser.g"
                self.setResult(
                    ##line 420 GJavaParser.g
                    VariableModifiers(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 420 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 420 GJavaParser.g
                                      self.getRhsSym(2))
                ##line 420 GJavaParser.g
                )

         self.__rule_action[137]= Act137

        #
        # Rule 138:  VariableModifier ::= final
        #
         def Act138(): 
               ##line 422 "GJavaParser.g"
                self.setResult(
                    ##line 422 GJavaParser.g
                    VariableModifier(self.getRhsIToken(1))
                ##line 422 GJavaParser.g
                )

         self.__rule_action[138]= Act138

        #
        # Rule 139:  VariableModifier ::= Annotations
        #
        
                 
        #
        # Rule 140:  LastFormalParameter ::= VariableModifiersopt Type ...opt VariableDeclaratorId
        #
         def Act140(): 
               ##line 425 "GJavaParser.g"
                self.setResult(
                    ##line 425 GJavaParser.g
                    LastFormalParameter(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 425 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 425 GJavaParser.g
                                        self.getRhsSym(2),
                                        ##line 425 GJavaParser.g
                                        self.getRhsSym(3),
                                        ##line 425 GJavaParser.g
                                        self.getRhsSym(4))
                ##line 425 GJavaParser.g
                )

         self.__rule_action[140]= Act140

        #
        # Rule 141:  MethodModifiers ::= MethodModifier
        #
        
                 
        #
        # Rule 142:  MethodModifiers ::= MethodModifiers MethodModifier
        #
         def Act142(): 
               ##line 434 "GJavaParser.g"
                self.setResult(
                    ##line 434 GJavaParser.g
                    MethodModifiers(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 434 GJavaParser.g
                                    self.getRhsSym(1),
                                    ##line 434 GJavaParser.g
                                    self.getRhsSym(2))
                ##line 434 GJavaParser.g
                )

         self.__rule_action[142]= Act142

        #
        # Rule 143:  MethodModifier ::= Annotations
        #
        
                 
        #
        # Rule 144:  MethodModifier ::= public
        #
         def Act144(): 
               ##line 437 "GJavaParser.g"
                self.setResult(
                    ##line 437 GJavaParser.g
                    MethodModifier0(self.getRhsIToken(1))
                ##line 437 GJavaParser.g
                )

         self.__rule_action[144]= Act144

        #
        # Rule 145:  MethodModifier ::= protected
        #
         def Act145(): 
               ##line 438 "GJavaParser.g"
                self.setResult(
                    ##line 438 GJavaParser.g
                    MethodModifier1(self.getRhsIToken(1))
                ##line 438 GJavaParser.g
                )

         self.__rule_action[145]= Act145

        #
        # Rule 146:  MethodModifier ::= private
        #
         def Act146(): 
               ##line 439 "GJavaParser.g"
                self.setResult(
                    ##line 439 GJavaParser.g
                    MethodModifier2(self.getRhsIToken(1))
                ##line 439 GJavaParser.g
                )

         self.__rule_action[146]= Act146

        #
        # Rule 147:  MethodModifier ::= abstract
        #
         def Act147(): 
               ##line 440 "GJavaParser.g"
                self.setResult(
                    ##line 440 GJavaParser.g
                    MethodModifier3(self.getRhsIToken(1))
                ##line 440 GJavaParser.g
                )

         self.__rule_action[147]= Act147

        #
        # Rule 148:  MethodModifier ::= static
        #
         def Act148(): 
               ##line 441 "GJavaParser.g"
                self.setResult(
                    ##line 441 GJavaParser.g
                    MethodModifier4(self.getRhsIToken(1))
                ##line 441 GJavaParser.g
                )

         self.__rule_action[148]= Act148

        #
        # Rule 149:  MethodModifier ::= final
        #
         def Act149(): 
               ##line 442 "GJavaParser.g"
                self.setResult(
                    ##line 442 GJavaParser.g
                    MethodModifier5(self.getRhsIToken(1))
                ##line 442 GJavaParser.g
                )

         self.__rule_action[149]= Act149

        #
        # Rule 150:  MethodModifier ::= synchronized
        #
         def Act150(): 
               ##line 443 "GJavaParser.g"
                self.setResult(
                    ##line 443 GJavaParser.g
                    MethodModifier6(self.getRhsIToken(1))
                ##line 443 GJavaParser.g
                )

         self.__rule_action[150]= Act150

        #
        # Rule 151:  MethodModifier ::= native
        #
         def Act151(): 
               ##line 444 "GJavaParser.g"
                self.setResult(
                    ##line 444 GJavaParser.g
                    MethodModifier7(self.getRhsIToken(1))
                ##line 444 GJavaParser.g
                )

         self.__rule_action[151]= Act151

        #
        # Rule 152:  MethodModifier ::= strictfp
        #
         def Act152(): 
               ##line 445 "GJavaParser.g"
                self.setResult(
                    ##line 445 GJavaParser.g
                    MethodModifier8(self.getRhsIToken(1))
                ##line 445 GJavaParser.g
                )

         self.__rule_action[152]= Act152

        #
        # Rule 153:  Throws ::= throws ExceptionTypeList
        #
         def Act153(): 
               ##line 447 "GJavaParser.g"
                self.setResult(
                    ##line 447 GJavaParser.g
                    Throws(self.getLeftIToken(), self.getRightIToken(),
                           ##line 447 GJavaParser.g
                           AstToken(self.getRhsIToken(1)),
                           ##line 447 GJavaParser.g
                           self.getRhsSym(2))
                ##line 447 GJavaParser.g
                )

         self.__rule_action[153]= Act153

        #
        # Rule 154:  ExceptionTypeList ::= ExceptionType
        #
        
                 
        #
        # Rule 155:  ExceptionTypeList ::= ExceptionTypeList , ExceptionType
        #
         def Act155(): 
               ##line 450 "GJavaParser.g"
                self.setResult(
                    ##line 450 GJavaParser.g
                    ExceptionTypeList(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 450 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 450 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 450 GJavaParser.g
                                      self.getRhsSym(3))
                ##line 450 GJavaParser.g
                )

         self.__rule_action[155]= Act155

        #
        # Rule 156:  ExceptionType ::= ClassType
        #
        
                 
        #
        # Rule 157:  ExceptionType ::= TypeVariable
        #
        
                 
        #
        # Rule 158:  MethodBody ::= Block
        #
        
                 
        #
        # Rule 159:  MethodBody ::= ;
        #
         def Act159(): 
               ##line 456 "GJavaParser.g"
                self.setResult(
                    ##line 456 GJavaParser.g
                    MethodBody(self.getRhsIToken(1))
                ##line 456 GJavaParser.g
                )

         self.__rule_action[159]= Act159

        #
        # Rule 160:  InstanceInitializer ::= Block
        #
        
                 
        #
        # Rule 161:  StaticInitializer ::= static Block
        #
         def Act161(): 
               ##line 460 "GJavaParser.g"
                self.setResult(
                    ##line 460 GJavaParser.g
                    StaticInitializer(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 460 GJavaParser.g
                                      AstToken(self.getRhsIToken(1)),
                                      ##line 460 GJavaParser.g
                                      self.getRhsSym(2))
                ##line 460 GJavaParser.g
                )

         self.__rule_action[161]= Act161

        #
        # Rule 162:  ConstructorDeclaration ::= ConstructorModifiersopt ConstructorDeclarator Throwsopt ConstructorBody
        #
         def Act162(): 
               ##line 462 "GJavaParser.g"
                self.setResult(
                    ##line 462 GJavaParser.g
                    ConstructorDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                           ##line 462 GJavaParser.g
                                           self.getRhsSym(1),
                                           ##line 462 GJavaParser.g
                                           self.getRhsSym(2),
                                           ##line 462 GJavaParser.g
                                           self.getRhsSym(3),
                                           ##line 462 GJavaParser.g
                                           self.getRhsSym(4))
                ##line 462 GJavaParser.g
                )

         self.__rule_action[162]= Act162

        #
        # Rule 163:  ConstructorDeclarator ::= TypeParametersopt SimpleTypeName ( FormalParameterListopt )
        #
         def Act163(): 
               ##line 464 "GJavaParser.g"
                self.setResult(
                    ##line 464 GJavaParser.g
                    ConstructorDeclarator(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 464 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 464 GJavaParser.g
                                          self.getRhsSym(2),
                                          ##line 464 GJavaParser.g
                                          AstToken(self.getRhsIToken(3)),
                                          ##line 464 GJavaParser.g
                                          self.getRhsSym(4),
                                          ##line 464 GJavaParser.g
                                          AstToken(self.getRhsIToken(5)))
                ##line 464 GJavaParser.g
                )

         self.__rule_action[163]= Act163

        #
        # Rule 164:  SimpleTypeName ::= identifier
        #
        
                 
        #
        # Rule 165:  ConstructorModifiers ::= ConstructorModifier
        #
        
                 
        #
        # Rule 166:  ConstructorModifiers ::= ConstructorModifiers ConstructorModifier
        #
         def Act166(): 
               ##line 469 "GJavaParser.g"
                self.setResult(
                    ##line 469 GJavaParser.g
                    ConstructorModifiers(self.getLeftIToken(), self.getRightIToken(),
                                         ##line 469 GJavaParser.g
                                         self.getRhsSym(1),
                                         ##line 469 GJavaParser.g
                                         self.getRhsSym(2))
                ##line 469 GJavaParser.g
                )

         self.__rule_action[166]= Act166

        #
        # Rule 167:  ConstructorModifier ::= Annotations
        #
        
                 
        #
        # Rule 168:  ConstructorModifier ::= public
        #
         def Act168(): 
               ##line 472 "GJavaParser.g"
                self.setResult(
                    ##line 472 GJavaParser.g
                    ConstructorModifier0(self.getRhsIToken(1))
                ##line 472 GJavaParser.g
                )

         self.__rule_action[168]= Act168

        #
        # Rule 169:  ConstructorModifier ::= protected
        #
         def Act169(): 
               ##line 473 "GJavaParser.g"
                self.setResult(
                    ##line 473 GJavaParser.g
                    ConstructorModifier1(self.getRhsIToken(1))
                ##line 473 GJavaParser.g
                )

         self.__rule_action[169]= Act169

        #
        # Rule 170:  ConstructorModifier ::= private
        #
         def Act170(): 
               ##line 474 "GJavaParser.g"
                self.setResult(
                    ##line 474 GJavaParser.g
                    ConstructorModifier2(self.getRhsIToken(1))
                ##line 474 GJavaParser.g
                )

         self.__rule_action[170]= Act170

        #
        # Rule 171:  ConstructorBody ::= { ExplicitConstructorInvocationopt BlockStatementsopt }
        #
         def Act171(): 
               ##line 476 "GJavaParser.g"
                self.setResult(
                    ##line 476 GJavaParser.g
                    ConstructorBody(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 476 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 476 GJavaParser.g
                                    self.getRhsSym(2),
                                    ##line 476 GJavaParser.g
                                    self.getRhsSym(3),
                                    ##line 476 GJavaParser.g
                                    AstToken(self.getRhsIToken(4)))
                ##line 476 GJavaParser.g
                )

         self.__rule_action[171]= Act171

        #
        # Rule 172:  ExplicitConstructorInvocation ::= TypeArgumentsopt this ( ArgumentListopt ) ;
        #
         def Act172(): 
               ##line 478 "GJavaParser.g"
                self.setResult(
                    ##line 478 GJavaParser.g
                    ExplicitConstructorInvocation0(self.getLeftIToken(), self.getRightIToken(),
                                                   ##line 478 GJavaParser.g
                                                   self.getRhsSym(1),
                                                   ##line 478 GJavaParser.g
                                                   AstToken(self.getRhsIToken(2)),
                                                   ##line 478 GJavaParser.g
                                                   AstToken(self.getRhsIToken(3)),
                                                   ##line 478 GJavaParser.g
                                                   self.getRhsSym(4),
                                                   ##line 478 GJavaParser.g
                                                   AstToken(self.getRhsIToken(5)),
                                                   ##line 478 GJavaParser.g
                                                   AstToken(self.getRhsIToken(6)))
                ##line 478 GJavaParser.g
                )

         self.__rule_action[172]= Act172

        #
        # Rule 173:  ExplicitConstructorInvocation ::= TypeArgumentsopt super ( ArgumentListopt ) ;
        #
         def Act173(): 
               ##line 479 "GJavaParser.g"
                self.setResult(
                    ##line 479 GJavaParser.g
                    ExplicitConstructorInvocation1(self.getLeftIToken(), self.getRightIToken(),
                                                   ##line 479 GJavaParser.g
                                                   self.getRhsSym(1),
                                                   ##line 479 GJavaParser.g
                                                   AstToken(self.getRhsIToken(2)),
                                                   ##line 479 GJavaParser.g
                                                   AstToken(self.getRhsIToken(3)),
                                                   ##line 479 GJavaParser.g
                                                   self.getRhsSym(4),
                                                   ##line 479 GJavaParser.g
                                                   AstToken(self.getRhsIToken(5)),
                                                   ##line 479 GJavaParser.g
                                                   AstToken(self.getRhsIToken(6)))
                ##line 479 GJavaParser.g
                )

         self.__rule_action[173]= Act173

        #
        # Rule 174:  ExplicitConstructorInvocation ::= Primary . TypeArgumentsopt super ( ArgumentListopt ) ;
        #
         def Act174(): 
               ##line 480 "GJavaParser.g"
                self.setResult(
                    ##line 480 GJavaParser.g
                    ExplicitConstructorInvocation2(self.getLeftIToken(), self.getRightIToken(),
                                                   ##line 480 GJavaParser.g
                                                   self.getRhsSym(1),
                                                   ##line 480 GJavaParser.g
                                                   AstToken(self.getRhsIToken(2)),
                                                   ##line 480 GJavaParser.g
                                                   self.getRhsSym(3),
                                                   ##line 480 GJavaParser.g
                                                   AstToken(self.getRhsIToken(4)),
                                                   ##line 480 GJavaParser.g
                                                   AstToken(self.getRhsIToken(5)),
                                                   ##line 480 GJavaParser.g
                                                   self.getRhsSym(6),
                                                   ##line 480 GJavaParser.g
                                                   AstToken(self.getRhsIToken(7)),
                                                   ##line 480 GJavaParser.g
                                                   AstToken(self.getRhsIToken(8)))
                ##line 480 GJavaParser.g
                )

         self.__rule_action[174]= Act174

        #
        # Rule 175:  EnumDeclaration ::= ClassModifiersopt enum identifier Interfacesopt EnumBody
        #
         def Act175(): 
               ##line 482 "GJavaParser.g"
                self.setResult(
                    ##line 482 GJavaParser.g
                    EnumDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 482 GJavaParser.g
                                    self.getRhsSym(1),
                                    ##line 482 GJavaParser.g
                                    AstToken(self.getRhsIToken(2)),
                                    ##line 482 GJavaParser.g
                                    self.getRhsSym(3),
                                    ##line 482 GJavaParser.g
                                    self.getRhsSym(4),
                                    ##line 482 GJavaParser.g
                                    self.getRhsSym(5))
                ##line 482 GJavaParser.g
                )

         self.__rule_action[175]= Act175

        #
        # Rule 176:  EnumBody ::= { EnumConstantsopt ,opt EnumBodyDeclarationsopt }
        #
         def Act176(): 
               ##line 484 "GJavaParser.g"
                self.setResult(
                    ##line 484 GJavaParser.g
                    EnumBody(self.getLeftIToken(), self.getRightIToken(),
                             ##line 484 GJavaParser.g
                             AstToken(self.getRhsIToken(1)),
                             ##line 484 GJavaParser.g
                             self.getRhsSym(2),
                             ##line 484 GJavaParser.g
                             self.getRhsSym(3),
                             ##line 484 GJavaParser.g
                             self.getRhsSym(4),
                             ##line 484 GJavaParser.g
                             AstToken(self.getRhsIToken(5)))
                ##line 484 GJavaParser.g
                )

         self.__rule_action[176]= Act176

        #
        # Rule 177:  EnumConstants ::= EnumConstant
        #
        
                 
        #
        # Rule 178:  EnumConstants ::= EnumConstants , EnumConstant
        #
         def Act178(): 
               ##line 487 "GJavaParser.g"
                self.setResult(
                    ##line 487 GJavaParser.g
                    EnumConstants(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 487 GJavaParser.g
                                  self.getRhsSym(1),
                                  ##line 487 GJavaParser.g
                                  AstToken(self.getRhsIToken(2)),
                                  ##line 487 GJavaParser.g
                                  self.getRhsSym(3))
                ##line 487 GJavaParser.g
                )

         self.__rule_action[178]= Act178

        #
        # Rule 179:  EnumConstant ::= Annotationsopt identifier Argumentsopt ClassBodyopt
        #
         def Act179(): 
               ##line 489 "GJavaParser.g"
                self.setResult(
                    ##line 489 GJavaParser.g
                    EnumConstant(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 489 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 489 GJavaParser.g
                                 self.getRhsSym(2),
                                 ##line 489 GJavaParser.g
                                 self.getRhsSym(3),
                                 ##line 489 GJavaParser.g
                                 self.getRhsSym(4))
                ##line 489 GJavaParser.g
                )

         self.__rule_action[179]= Act179

        #
        # Rule 180:  Arguments ::= ( ArgumentListopt )
        #
         def Act180(): 
               ##line 491 "GJavaParser.g"
                self.setResult(
                    ##line 491 GJavaParser.g
                    Arguments(self.getLeftIToken(), self.getRightIToken(),
                              ##line 491 GJavaParser.g
                              AstToken(self.getRhsIToken(1)),
                              ##line 491 GJavaParser.g
                              self.getRhsSym(2),
                              ##line 491 GJavaParser.g
                              AstToken(self.getRhsIToken(3)))
                ##line 491 GJavaParser.g
                )

         self.__rule_action[180]= Act180

        #
        # Rule 181:  EnumBodyDeclarations ::= ; ClassBodyDeclarationsopt
        #
         def Act181(): 
               ##line 493 "GJavaParser.g"
                self.setResult(
                    ##line 493 GJavaParser.g
                    EnumBodyDeclarations(self.getLeftIToken(), self.getRightIToken(),
                                         ##line 493 GJavaParser.g
                                         AstToken(self.getRhsIToken(1)),
                                         ##line 493 GJavaParser.g
                                         self.getRhsSym(2))
                ##line 493 GJavaParser.g
                )

         self.__rule_action[181]= Act181

        #
        # Rule 182:  InterfaceDeclaration ::= NormalInterfaceDeclaration
        #
        
                 
        #
        # Rule 183:  InterfaceDeclaration ::= AnnotationTypeDeclaration
        #
        
                 
        #
        # Rule 184:  NormalInterfaceDeclaration ::= InterfaceModifiersopt interface identifier TypeParametersopt ExtendsInterfacesopt InterfaceBody
        #
         def Act184(): 
               ##line 500 "GJavaParser.g"
                self.setResult(
                    ##line 500 GJavaParser.g
                    NormalInterfaceDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                               ##line 500 GJavaParser.g
                                               self.getRhsSym(1),
                                               ##line 500 GJavaParser.g
                                               AstToken(self.getRhsIToken(2)),
                                               ##line 500 GJavaParser.g
                                               self.getRhsSym(3),
                                               ##line 500 GJavaParser.g
                                               self.getRhsSym(4),
                                               ##line 500 GJavaParser.g
                                               self.getRhsSym(5),
                                               ##line 500 GJavaParser.g
                                               self.getRhsSym(6))
                ##line 500 GJavaParser.g
                )

         self.__rule_action[184]= Act184

        #
        # Rule 185:  InterfaceModifiers ::= InterfaceModifier
        #
        
                 
        #
        # Rule 186:  InterfaceModifiers ::= InterfaceModifiers InterfaceModifier
        #
         def Act186(): 
               ##line 503 "GJavaParser.g"
                self.setResult(
                    ##line 503 GJavaParser.g
                    InterfaceModifiers(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 503 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 503 GJavaParser.g
                                       self.getRhsSym(2))
                ##line 503 GJavaParser.g
                )

         self.__rule_action[186]= Act186

        #
        # Rule 187:  InterfaceModifier ::= Annotation
        #
        
                 
        #
        # Rule 188:  InterfaceModifier ::= public
        #
         def Act188(): 
               ##line 506 "GJavaParser.g"
                self.setResult(
                    ##line 506 GJavaParser.g
                    InterfaceModifier0(self.getRhsIToken(1))
                ##line 506 GJavaParser.g
                )

         self.__rule_action[188]= Act188

        #
        # Rule 189:  InterfaceModifier ::= protected
        #
         def Act189(): 
               ##line 507 "GJavaParser.g"
                self.setResult(
                    ##line 507 GJavaParser.g
                    InterfaceModifier1(self.getRhsIToken(1))
                ##line 507 GJavaParser.g
                )

         self.__rule_action[189]= Act189

        #
        # Rule 190:  InterfaceModifier ::= private
        #
         def Act190(): 
               ##line 508 "GJavaParser.g"
                self.setResult(
                    ##line 508 GJavaParser.g
                    InterfaceModifier2(self.getRhsIToken(1))
                ##line 508 GJavaParser.g
                )

         self.__rule_action[190]= Act190

        #
        # Rule 191:  InterfaceModifier ::= abstract
        #
         def Act191(): 
               ##line 509 "GJavaParser.g"
                self.setResult(
                    ##line 509 GJavaParser.g
                    InterfaceModifier3(self.getRhsIToken(1))
                ##line 509 GJavaParser.g
                )

         self.__rule_action[191]= Act191

        #
        # Rule 192:  InterfaceModifier ::= static
        #
         def Act192(): 
               ##line 510 "GJavaParser.g"
                self.setResult(
                    ##line 510 GJavaParser.g
                    InterfaceModifier4(self.getRhsIToken(1))
                ##line 510 GJavaParser.g
                )

         self.__rule_action[192]= Act192

        #
        # Rule 193:  InterfaceModifier ::= strictfp
        #
         def Act193(): 
               ##line 511 "GJavaParser.g"
                self.setResult(
                    ##line 511 GJavaParser.g
                    InterfaceModifier5(self.getRhsIToken(1))
                ##line 511 GJavaParser.g
                )

         self.__rule_action[193]= Act193

        #
        # Rule 194:  ExtendsInterfaces ::= extends InterfaceType
        #
         def Act194(): 
               ##line 513 "GJavaParser.g"
                self.setResult(
                    ##line 513 GJavaParser.g
                    ExtendsInterfaces0(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 513 GJavaParser.g
                                       AstToken(self.getRhsIToken(1)),
                                       ##line 513 GJavaParser.g
                                       self.getRhsSym(2))
                ##line 513 GJavaParser.g
                )

         self.__rule_action[194]= Act194

        #
        # Rule 195:  ExtendsInterfaces ::= ExtendsInterfaces , InterfaceType
        #
         def Act195(): 
               ##line 514 "GJavaParser.g"
                self.setResult(
                    ##line 514 GJavaParser.g
                    ExtendsInterfaces1(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 514 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 514 GJavaParser.g
                                       AstToken(self.getRhsIToken(2)),
                                       ##line 514 GJavaParser.g
                                       self.getRhsSym(3))
                ##line 514 GJavaParser.g
                )

         self.__rule_action[195]= Act195

        #
        # Rule 196:  InterfaceBody ::= { InterfaceMemberDeclarationsopt }
        #
         def Act196(): 
               ##line 521 "GJavaParser.g"
                self.setResult(
                    ##line 521 GJavaParser.g
                    InterfaceBody(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 521 GJavaParser.g
                                  AstToken(self.getRhsIToken(1)),
                                  ##line 521 GJavaParser.g
                                  self.getRhsSym(2),
                                  ##line 521 GJavaParser.g
                                  AstToken(self.getRhsIToken(3)))
                ##line 521 GJavaParser.g
                )

         self.__rule_action[196]= Act196

        #
        # Rule 197:  InterfaceMemberDeclarations ::= InterfaceMemberDeclaration
        #
        
                 
        #
        # Rule 198:  InterfaceMemberDeclarations ::= InterfaceMemberDeclarations InterfaceMemberDeclaration
        #
         def Act198(): 
               ##line 524 "GJavaParser.g"
                self.setResult(
                    ##line 524 GJavaParser.g
                    InterfaceMemberDeclarations(self.getLeftIToken(), self.getRightIToken(),
                                                ##line 524 GJavaParser.g
                                                self.getRhsSym(1),
                                                ##line 524 GJavaParser.g
                                                self.getRhsSym(2))
                ##line 524 GJavaParser.g
                )

         self.__rule_action[198]= Act198

        #
        # Rule 199:  InterfaceMemberDeclaration ::= ConstantDeclaration
        #
        
                 
        #
        # Rule 200:  InterfaceMemberDeclaration ::= AbstractMethodDeclaration
        #
        
                 
        #
        # Rule 201:  InterfaceMemberDeclaration ::= ClassDeclaration
        #
        
                 
        #
        # Rule 202:  InterfaceMemberDeclaration ::= InterfaceDeclaration
        #
        
                 
        #
        # Rule 203:  InterfaceMemberDeclaration ::= ;
        #
         def Act203(): 
               ##line 530 "GJavaParser.g"
                self.setResult(
                    ##line 530 GJavaParser.g
                    InterfaceMemberDeclaration(self.getRhsIToken(1))
                ##line 530 GJavaParser.g
                )

         self.__rule_action[203]= Act203

        #
        # Rule 204:  ConstantDeclaration ::= ConstantModifiersopt Type VariableDeclarators
        #
         def Act204(): 
               ##line 532 "GJavaParser.g"
                self.setResult(
                    ##line 532 GJavaParser.g
                    ConstantDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 532 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 532 GJavaParser.g
                                        self.getRhsSym(2),
                                        ##line 532 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 532 GJavaParser.g
                )

         self.__rule_action[204]= Act204

        #
        # Rule 205:  ConstantModifiers ::= ConstantModifier
        #
        
                 
        #
        # Rule 206:  ConstantModifiers ::= ConstantModifiers ConstantModifier
        #
         def Act206(): 
               ##line 535 "GJavaParser.g"
                self.setResult(
                    ##line 535 GJavaParser.g
                    ConstantModifiers(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 535 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 535 GJavaParser.g
                                      self.getRhsSym(2))
                ##line 535 GJavaParser.g
                )

         self.__rule_action[206]= Act206

        #
        # Rule 207:  ConstantModifier ::= Annotation
        #
        
                 
        #
        # Rule 208:  ConstantModifier ::= public
        #
         def Act208(): 
               ##line 538 "GJavaParser.g"
                self.setResult(
                    ##line 538 GJavaParser.g
                    ConstantModifier0(self.getRhsIToken(1))
                ##line 538 GJavaParser.g
                )

         self.__rule_action[208]= Act208

        #
        # Rule 209:  ConstantModifier ::= static
        #
         def Act209(): 
               ##line 539 "GJavaParser.g"
                self.setResult(
                    ##line 539 GJavaParser.g
                    ConstantModifier1(self.getRhsIToken(1))
                ##line 539 GJavaParser.g
                )

         self.__rule_action[209]= Act209

        #
        # Rule 210:  ConstantModifier ::= final
        #
         def Act210(): 
               ##line 540 "GJavaParser.g"
                self.setResult(
                    ##line 540 GJavaParser.g
                    ConstantModifier2(self.getRhsIToken(1))
                ##line 540 GJavaParser.g
                )

         self.__rule_action[210]= Act210

        #
        # Rule 211:  AbstractMethodDeclaration ::= AbstractMethodModifiersopt TypeParametersopt ResultType MethodDeclarator Throwsopt ;
        #
         def Act211(): 
               ##line 542 "GJavaParser.g"
                self.setResult(
                    ##line 542 GJavaParser.g
                    AbstractMethodDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 542 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 542 GJavaParser.g
                                              self.getRhsSym(2),
                                              ##line 542 GJavaParser.g
                                              self.getRhsSym(3),
                                              ##line 542 GJavaParser.g
                                              self.getRhsSym(4),
                                              ##line 542 GJavaParser.g
                                              self.getRhsSym(5),
                                              ##line 542 GJavaParser.g
                                              AstToken(self.getRhsIToken(6)))
                ##line 542 GJavaParser.g
                )

         self.__rule_action[211]= Act211

        #
        # Rule 212:  AbstractMethodModifiers ::= AbstractMethodModifier
        #
        
                 
        #
        # Rule 213:  AbstractMethodModifiers ::= AbstractMethodModifiers AbstractMethodModifier
        #
         def Act213(): 
               ##line 545 "GJavaParser.g"
                self.setResult(
                    ##line 545 GJavaParser.g
                    AbstractMethodModifiers(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 545 GJavaParser.g
                                            self.getRhsSym(1),
                                            ##line 545 GJavaParser.g
                                            self.getRhsSym(2))
                ##line 545 GJavaParser.g
                )

         self.__rule_action[213]= Act213

        #
        # Rule 214:  AbstractMethodModifier ::= Annotations
        #
        
                 
        #
        # Rule 215:  AbstractMethodModifier ::= public
        #
         def Act215(): 
               ##line 548 "GJavaParser.g"
                self.setResult(
                    ##line 548 GJavaParser.g
                    AbstractMethodModifier0(self.getRhsIToken(1))
                ##line 548 GJavaParser.g
                )

         self.__rule_action[215]= Act215

        #
        # Rule 216:  AbstractMethodModifier ::= abstract
        #
         def Act216(): 
               ##line 549 "GJavaParser.g"
                self.setResult(
                    ##line 549 GJavaParser.g
                    AbstractMethodModifier1(self.getRhsIToken(1))
                ##line 549 GJavaParser.g
                )

         self.__rule_action[216]= Act216

        #
        # Rule 217:  AnnotationTypeDeclaration ::= InterfaceModifiersopt @ interface identifier AnnotationTypeBody
        #
         def Act217(): 
               ##line 551 "GJavaParser.g"
                self.setResult(
                    ##line 551 GJavaParser.g
                    AnnotationTypeDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 551 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 551 GJavaParser.g
                                              AstToken(self.getRhsIToken(2)),
                                              ##line 551 GJavaParser.g
                                              AstToken(self.getRhsIToken(3)),
                                              ##line 551 GJavaParser.g
                                              self.getRhsSym(4),
                                              ##line 551 GJavaParser.g
                                              self.getRhsSym(5))
                ##line 551 GJavaParser.g
                )

         self.__rule_action[217]= Act217

        #
        # Rule 218:  AnnotationTypeBody ::= { AnnotationTypeElementDeclarationsopt }
        #
         def Act218(): 
               ##line 553 "GJavaParser.g"
                self.setResult(
                    ##line 553 GJavaParser.g
                    AnnotationTypeBody(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 553 GJavaParser.g
                                       AstToken(self.getRhsIToken(1)),
                                       ##line 553 GJavaParser.g
                                       self.getRhsSym(2),
                                       ##line 553 GJavaParser.g
                                       AstToken(self.getRhsIToken(3)))
                ##line 553 GJavaParser.g
                )

         self.__rule_action[218]= Act218

        #
        # Rule 219:  AnnotationTypeElementDeclarations ::= AnnotationTypeElementDeclaration
        #
        
                 
        #
        # Rule 220:  AnnotationTypeElementDeclarations ::= AnnotationTypeElementDeclarations AnnotationTypeElementDeclaration
        #
         def Act220(): 
               ##line 556 "GJavaParser.g"
                self.setResult(
                    ##line 556 GJavaParser.g
                    AnnotationTypeElementDeclarations(self.getLeftIToken(), self.getRightIToken(),
                                                      ##line 556 GJavaParser.g
                                                      self.getRhsSym(1),
                                                      ##line 556 GJavaParser.g
                                                      self.getRhsSym(2))
                ##line 556 GJavaParser.g
                )

         self.__rule_action[220]= Act220

        #
        # Rule 221:  AnnotationTypeElementDeclaration ::= AbstractMethodModifiersopt Type identifier ( ) DefaultValueopt ;
        #
         def Act221(): 
               ##line 558 "GJavaParser.g"
                self.setResult(
                    ##line 558 GJavaParser.g
                    AnnotationTypeElementDeclaration0(self.getLeftIToken(), self.getRightIToken(),
                                                      ##line 558 GJavaParser.g
                                                      self.getRhsSym(1),
                                                      ##line 558 GJavaParser.g
                                                      self.getRhsSym(2),
                                                      ##line 558 GJavaParser.g
                                                      self.getRhsSym(3),
                                                      ##line 558 GJavaParser.g
                                                      AstToken(self.getRhsIToken(4)),
                                                      ##line 558 GJavaParser.g
                                                      AstToken(self.getRhsIToken(5)),
                                                      ##line 558 GJavaParser.g
                                                      self.getRhsSym(6),
                                                      ##line 558 GJavaParser.g
                                                      AstToken(self.getRhsIToken(7)))
                ##line 558 GJavaParser.g
                )

         self.__rule_action[221]= Act221

        #
        # Rule 222:  AnnotationTypeElementDeclaration ::= ConstantDeclaration
        #
        
                 
        #
        # Rule 223:  AnnotationTypeElementDeclaration ::= ClassDeclaration
        #
        
                 
        #
        # Rule 224:  AnnotationTypeElementDeclaration ::= InterfaceDeclaration
        #
        
                 
        #
        # Rule 225:  AnnotationTypeElementDeclaration ::= EnumDeclaration
        #
        
                 
        #
        # Rule 226:  AnnotationTypeElementDeclaration ::= AnnotationTypeDeclaration
        #
        
                 
        #
        # Rule 227:  AnnotationTypeElementDeclaration ::= ;
        #
         def Act227(): 
               ##line 564 "GJavaParser.g"
                self.setResult(
                    ##line 564 GJavaParser.g
                    AnnotationTypeElementDeclaration1(self.getRhsIToken(1))
                ##line 564 GJavaParser.g
                )

         self.__rule_action[227]= Act227

        #
        # Rule 228:  DefaultValue ::= default ElementValue
        #
         def Act228(): 
               ##line 566 "GJavaParser.g"
                self.setResult(
                    ##line 566 GJavaParser.g
                    DefaultValue(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 566 GJavaParser.g
                                 AstToken(self.getRhsIToken(1)),
                                 ##line 566 GJavaParser.g
                                 self.getRhsSym(2))
                ##line 566 GJavaParser.g
                )

         self.__rule_action[228]= Act228

        #
        # Rule 229:  Annotations ::= Annotation
        #
        
                 
        #
        # Rule 230:  Annotations ::= Annotations Annotation
        #
         def Act230(): 
               ##line 569 "GJavaParser.g"
                self.setResult(
                    ##line 569 GJavaParser.g
                    Annotations(self.getLeftIToken(), self.getRightIToken(),
                                ##line 569 GJavaParser.g
                                self.getRhsSym(1),
                                ##line 569 GJavaParser.g
                                self.getRhsSym(2))
                ##line 569 GJavaParser.g
                )

         self.__rule_action[230]= Act230

        #
        # Rule 231:  Annotation ::= NormalAnnotation
        #
        
                 
        #
        # Rule 232:  Annotation ::= MarkerAnnotation
        #
        
                 
        #
        # Rule 233:  Annotation ::= SingleElementAnnotation
        #
        
                 
        #
        # Rule 234:  NormalAnnotation ::= @ TypeName ( ElementValuePairsopt )
        #
         def Act234(): 
               ##line 575 "GJavaParser.g"
                self.setResult(
                    ##line 575 GJavaParser.g
                    NormalAnnotation(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 575 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 575 GJavaParser.g
                                     self.getRhsSym(2),
                                     ##line 575 GJavaParser.g
                                     AstToken(self.getRhsIToken(3)),
                                     ##line 575 GJavaParser.g
                                     self.getRhsSym(4),
                                     ##line 575 GJavaParser.g
                                     AstToken(self.getRhsIToken(5)))
                ##line 575 GJavaParser.g
                )

         self.__rule_action[234]= Act234

        #
        # Rule 235:  ElementValuePairs ::= ElementValuePair
        #
        
                 
        #
        # Rule 236:  ElementValuePairs ::= ElementValuePairs , ElementValuePair
        #
         def Act236(): 
               ##line 578 "GJavaParser.g"
                self.setResult(
                    ##line 578 GJavaParser.g
                    ElementValuePairs(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 578 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 578 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 578 GJavaParser.g
                                      self.getRhsSym(3))
                ##line 578 GJavaParser.g
                )

         self.__rule_action[236]= Act236

        #
        # Rule 237:  ElementValuePair ::= SimpleName = ElementValue
        #
         def Act237(): 
               ##line 580 "GJavaParser.g"
                self.setResult(
                    ##line 580 GJavaParser.g
                    ElementValuePair(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 580 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 580 GJavaParser.g
                                     AstToken(self.getRhsIToken(2)),
                                     ##line 580 GJavaParser.g
                                     self.getRhsSym(3))
                ##line 580 GJavaParser.g
                )

         self.__rule_action[237]= Act237

        #
        # Rule 238:  SimpleName ::= identifier
        #
        
                 
        #
        # Rule 239:  ElementValue ::= ConditionalExpression
        #
        
                 
        #
        # Rule 240:  ElementValue ::= Annotation
        #
        
                 
        #
        # Rule 241:  ElementValue ::= ElementValueArrayInitializer
        #
        
                 
        #
        # Rule 242:  ElementValueArrayInitializer ::= { ElementValuesopt ,opt }
        #
         def Act242(): 
               ##line 588 "GJavaParser.g"
                self.setResult(
                    ##line 588 GJavaParser.g
                    ElementValueArrayInitializer(self.getLeftIToken(), self.getRightIToken(),
                                                 ##line 588 GJavaParser.g
                                                 AstToken(self.getRhsIToken(1)),
                                                 ##line 588 GJavaParser.g
                                                 self.getRhsSym(2),
                                                 ##line 588 GJavaParser.g
                                                 self.getRhsSym(3),
                                                 ##line 588 GJavaParser.g
                                                 AstToken(self.getRhsIToken(4)))
                ##line 588 GJavaParser.g
                )

         self.__rule_action[242]= Act242

        #
        # Rule 243:  ElementValues ::= ElementValue
        #
        
                 
        #
        # Rule 244:  ElementValues ::= ElementValues , ElementValue
        #
         def Act244(): 
               ##line 591 "GJavaParser.g"
                self.setResult(
                    ##line 591 GJavaParser.g
                    ElementValues(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 591 GJavaParser.g
                                  self.getRhsSym(1),
                                  ##line 591 GJavaParser.g
                                  AstToken(self.getRhsIToken(2)),
                                  ##line 591 GJavaParser.g
                                  self.getRhsSym(3))
                ##line 591 GJavaParser.g
                )

         self.__rule_action[244]= Act244

        #
        # Rule 245:  MarkerAnnotation ::= @ TypeName
        #
         def Act245(): 
               ##line 593 "GJavaParser.g"
                self.setResult(
                    ##line 593 GJavaParser.g
                    MarkerAnnotation(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 593 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 593 GJavaParser.g
                                     self.getRhsSym(2))
                ##line 593 GJavaParser.g
                )

         self.__rule_action[245]= Act245

        #
        # Rule 246:  SingleElementAnnotation ::= @ TypeName ( ElementValue )
        #
         def Act246(): 
               ##line 595 "GJavaParser.g"
                self.setResult(
                    ##line 595 GJavaParser.g
                    SingleElementAnnotation(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 595 GJavaParser.g
                                            AstToken(self.getRhsIToken(1)),
                                            ##line 595 GJavaParser.g
                                            self.getRhsSym(2),
                                            ##line 595 GJavaParser.g
                                            AstToken(self.getRhsIToken(3)),
                                            ##line 595 GJavaParser.g
                                            self.getRhsSym(4),
                                            ##line 595 GJavaParser.g
                                            AstToken(self.getRhsIToken(5)))
                ##line 595 GJavaParser.g
                )

         self.__rule_action[246]= Act246

        #
        # Rule 247:  ArrayInitializer ::= { VariableInitializersopt ,opt }
        #
         def Act247(): 
               ##line 599 "GJavaParser.g"
                self.setResult(
                    ##line 599 GJavaParser.g
                    ArrayInitializer(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 599 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 599 GJavaParser.g
                                     self.getRhsSym(2),
                                     ##line 599 GJavaParser.g
                                     self.getRhsSym(3),
                                     ##line 599 GJavaParser.g
                                     AstToken(self.getRhsIToken(4)))
                ##line 599 GJavaParser.g
                )

         self.__rule_action[247]= Act247

        #
        # Rule 248:  VariableInitializers ::= VariableInitializer
        #
        
                 
        #
        # Rule 249:  VariableInitializers ::= VariableInitializers , VariableInitializer
        #
         def Act249(): 
               ##line 602 "GJavaParser.g"
                self.setResult(
                    ##line 602 GJavaParser.g
                    VariableInitializers(self.getLeftIToken(), self.getRightIToken(),
                                         ##line 602 GJavaParser.g
                                         self.getRhsSym(1),
                                         ##line 602 GJavaParser.g
                                         AstToken(self.getRhsIToken(2)),
                                         ##line 602 GJavaParser.g
                                         self.getRhsSym(3))
                ##line 602 GJavaParser.g
                )

         self.__rule_action[249]= Act249

        #
        # Rule 250:  Block ::= { BlockStatementsopt }
        #
         def Act250(): 
               ##line 618 "GJavaParser.g"
                self.setResult(
                    ##line 618 GJavaParser.g
                    Block(self.getLeftIToken(), self.getRightIToken(),
                          ##line 618 GJavaParser.g
                          AstToken(self.getRhsIToken(1)),
                          ##line 618 GJavaParser.g
                          self.getRhsSym(2),
                          ##line 618 GJavaParser.g
                          AstToken(self.getRhsIToken(3)))
                ##line 618 GJavaParser.g
                )

         self.__rule_action[250]= Act250

        #
        # Rule 251:  BlockStatements ::= BlockStatement
        #
        
                 
        #
        # Rule 252:  BlockStatements ::= BlockStatements BlockStatement
        #
         def Act252(): 
               ##line 621 "GJavaParser.g"
                self.setResult(
                    ##line 621 GJavaParser.g
                    BlockStatements(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 621 GJavaParser.g
                                    self.getRhsSym(1),
                                    ##line 621 GJavaParser.g
                                    self.getRhsSym(2))
                ##line 621 GJavaParser.g
                )

         self.__rule_action[252]= Act252

        #
        # Rule 253:  BlockStatement ::= LocalVariableDeclarationStatement
        #
        
                 
        #
        # Rule 254:  BlockStatement ::= ClassDeclaration
        #
        
                 
        #
        # Rule 255:  BlockStatement ::= Statement
        #
        
                 
        #
        # Rule 256:  LocalVariableDeclarationStatement ::= LocalVariableDeclaration ;
        #
         def Act256(): 
               ##line 627 "GJavaParser.g"
                self.setResult(
                    ##line 627 GJavaParser.g
                    LocalVariableDeclarationStatement(self.getLeftIToken(), self.getRightIToken(),
                                                      ##line 627 GJavaParser.g
                                                      self.getRhsSym(1),
                                                      ##line 627 GJavaParser.g
                                                      AstToken(self.getRhsIToken(2)))
                ##line 627 GJavaParser.g
                )

         self.__rule_action[256]= Act256

        #
        # Rule 257:  LocalVariableDeclaration ::= VariableModifiersopt Type VariableDeclarators
        #
         def Act257(): 
               ##line 629 "GJavaParser.g"
                self.setResult(
                    ##line 629 GJavaParser.g
                    LocalVariableDeclaration(self.getLeftIToken(), self.getRightIToken(),
                                             ##line 629 GJavaParser.g
                                             self.getRhsSym(1),
                                             ##line 629 GJavaParser.g
                                             self.getRhsSym(2),
                                             ##line 629 GJavaParser.g
                                             self.getRhsSym(3))
                ##line 629 GJavaParser.g
                )

         self.__rule_action[257]= Act257

        #
        # Rule 258:  Statement ::= StatementWithoutTrailingSubstatement
        #
        
                 
        #
        # Rule 259:  Statement ::= LabeledStatement
        #
        
                 
        #
        # Rule 260:  Statement ::= IfThenStatement
        #
        
                 
        #
        # Rule 261:  Statement ::= IfThenElseStatement
        #
        
                 
        #
        # Rule 262:  Statement ::= WhileStatement
        #
        
                 
        #
        # Rule 263:  Statement ::= ForStatement
        #
        
                 
        #
        # Rule 264:  StatementWithoutTrailingSubstatement ::= Block
        #
        
                 
        #
        # Rule 265:  StatementWithoutTrailingSubstatement ::= EmptyStatement
        #
        
                 
        #
        # Rule 266:  StatementWithoutTrailingSubstatement ::= ExpressionStatement
        #
        
                 
        #
        # Rule 267:  StatementWithoutTrailingSubstatement ::= AssertStatement
        #
        
                 
        #
        # Rule 268:  StatementWithoutTrailingSubstatement ::= SwitchStatement
        #
        
                 
        #
        # Rule 269:  StatementWithoutTrailingSubstatement ::= DoStatement
        #
        
                 
        #
        # Rule 270:  StatementWithoutTrailingSubstatement ::= BreakStatement
        #
        
                 
        #
        # Rule 271:  StatementWithoutTrailingSubstatement ::= ContinueStatement
        #
        
                 
        #
        # Rule 272:  StatementWithoutTrailingSubstatement ::= ReturnStatement
        #
        
                 
        #
        # Rule 273:  StatementWithoutTrailingSubstatement ::= SynchronizedStatement
        #
        
                 
        #
        # Rule 274:  StatementWithoutTrailingSubstatement ::= ThrowStatement
        #
        
                 
        #
        # Rule 275:  StatementWithoutTrailingSubstatement ::= TryStatement
        #
        
                 
        #
        # Rule 276:  StatementNoShortIf ::= StatementWithoutTrailingSubstatement
        #
        
                 
        #
        # Rule 277:  StatementNoShortIf ::= LabeledStatementNoShortIf
        #
        
                 
        #
        # Rule 278:  StatementNoShortIf ::= IfThenElseStatementNoShortIf
        #
        
                 
        #
        # Rule 279:  StatementNoShortIf ::= WhileStatementNoShortIf
        #
        
                 
        #
        # Rule 280:  StatementNoShortIf ::= ForStatementNoShortIf
        #
        
                 
        #
        # Rule 281:  IfThenStatement ::= if ( Expression ) Statement
        #
         def Act281(): 
               ##line 672 "GJavaParser.g"
                self.setResult(
                    ##line 672 GJavaParser.g
                    IfThenStatement(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 672 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 672 GJavaParser.g
                                    AstToken(self.getRhsIToken(2)),
                                    ##line 672 GJavaParser.g
                                    self.getRhsSym(3),
                                    ##line 672 GJavaParser.g
                                    AstToken(self.getRhsIToken(4)),
                                    ##line 672 GJavaParser.g
                                    self.getRhsSym(5))
                ##line 672 GJavaParser.g
                )

         self.__rule_action[281]= Act281

        #
        # Rule 282:  IfThenElseStatement ::= if ( Expression ) StatementNoShortIf else Statement
        #
         def Act282(): 
               ##line 674 "GJavaParser.g"
                self.setResult(
                    ##line 674 GJavaParser.g
                    IfThenElseStatement(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 674 GJavaParser.g
                                        AstToken(self.getRhsIToken(1)),
                                        ##line 674 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 674 GJavaParser.g
                                        self.getRhsSym(3),
                                        ##line 674 GJavaParser.g
                                        AstToken(self.getRhsIToken(4)),
                                        ##line 674 GJavaParser.g
                                        self.getRhsSym(5),
                                        ##line 674 GJavaParser.g
                                        AstToken(self.getRhsIToken(6)),
                                        ##line 674 GJavaParser.g
                                        self.getRhsSym(7))
                ##line 674 GJavaParser.g
                )

         self.__rule_action[282]= Act282

        #
        # Rule 283:  IfThenElseStatementNoShortIf ::= if ( Expression ) StatementNoShortIf else StatementNoShortIf
        #
         def Act283(): 
               ##line 676 "GJavaParser.g"
                self.setResult(
                    ##line 676 GJavaParser.g
                    IfThenElseStatementNoShortIf(self.getLeftIToken(), self.getRightIToken(),
                                                 ##line 676 GJavaParser.g
                                                 AstToken(self.getRhsIToken(1)),
                                                 ##line 676 GJavaParser.g
                                                 AstToken(self.getRhsIToken(2)),
                                                 ##line 676 GJavaParser.g
                                                 self.getRhsSym(3),
                                                 ##line 676 GJavaParser.g
                                                 AstToken(self.getRhsIToken(4)),
                                                 ##line 676 GJavaParser.g
                                                 self.getRhsSym(5),
                                                 ##line 676 GJavaParser.g
                                                 AstToken(self.getRhsIToken(6)),
                                                 ##line 676 GJavaParser.g
                                                 self.getRhsSym(7))
                ##line 676 GJavaParser.g
                )

         self.__rule_action[283]= Act283

        #
        # Rule 284:  EmptyStatement ::= ;
        #
         def Act284(): 
               ##line 678 "GJavaParser.g"
                self.setResult(
                    ##line 678 GJavaParser.g
                    EmptyStatement(self.getRhsIToken(1))
                ##line 678 GJavaParser.g
                )

         self.__rule_action[284]= Act284

        #
        # Rule 285:  LabeledStatement ::= identifier : Statement
        #
         def Act285(): 
               ##line 680 "GJavaParser.g"
                self.setResult(
                    ##line 680 GJavaParser.g
                    LabeledStatement(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 680 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 680 GJavaParser.g
                                     AstToken(self.getRhsIToken(2)),
                                     ##line 680 GJavaParser.g
                                     self.getRhsSym(3))
                ##line 680 GJavaParser.g
                )

         self.__rule_action[285]= Act285

        #
        # Rule 286:  LabeledStatementNoShortIf ::= identifier : StatementNoShortIf
        #
         def Act286(): 
               ##line 682 "GJavaParser.g"
                self.setResult(
                    ##line 682 GJavaParser.g
                    LabeledStatementNoShortIf(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 682 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 682 GJavaParser.g
                                              AstToken(self.getRhsIToken(2)),
                                              ##line 682 GJavaParser.g
                                              self.getRhsSym(3))
                ##line 682 GJavaParser.g
                )

         self.__rule_action[286]= Act286

        #
        # Rule 287:  ExpressionStatement ::= StatementExpression ;
        #
         def Act287(): 
               ##line 684 "GJavaParser.g"
                self.setResult(
                    ##line 684 GJavaParser.g
                    ExpressionStatement(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 684 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 684 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)))
                ##line 684 GJavaParser.g
                )

         self.__rule_action[287]= Act287

        #
        # Rule 288:  StatementExpression ::= Assignment
        #
        
                 
        #
        # Rule 289:  StatementExpression ::= PreIncrementExpression
        #
        
                 
        #
        # Rule 290:  StatementExpression ::= PreDecrementExpression
        #
        
                 
        #
        # Rule 291:  StatementExpression ::= PostIncrementExpression
        #
        
                 
        #
        # Rule 292:  StatementExpression ::= PostDecrementExpression
        #
        
                 
        #
        # Rule 293:  StatementExpression ::= MethodInvocation
        #
        
                 
        #
        # Rule 294:  StatementExpression ::= ClassInstanceCreationExpression
        #
        
                 
        #
        # Rule 295:  AssertStatement ::= assert Expression ;
        #
         def Act295(): 
               ##line 703 "GJavaParser.g"
                self.setResult(
                    ##line 703 GJavaParser.g
                    AssertStatement0(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 703 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 703 GJavaParser.g
                                     self.getRhsSym(2),
                                     ##line 703 GJavaParser.g
                                     AstToken(self.getRhsIToken(3)))
                ##line 703 GJavaParser.g
                )

         self.__rule_action[295]= Act295

        #
        # Rule 296:  AssertStatement ::= assert Expression : Expression ;
        #
         def Act296(): 
               ##line 704 "GJavaParser.g"
                self.setResult(
                    ##line 704 GJavaParser.g
                    AssertStatement1(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 704 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 704 GJavaParser.g
                                     self.getRhsSym(2),
                                     ##line 704 GJavaParser.g
                                     AstToken(self.getRhsIToken(3)),
                                     ##line 704 GJavaParser.g
                                     self.getRhsSym(4),
                                     ##line 704 GJavaParser.g
                                     AstToken(self.getRhsIToken(5)))
                ##line 704 GJavaParser.g
                )

         self.__rule_action[296]= Act296

        #
        # Rule 297:  SwitchStatement ::= switch ( Expression ) SwitchBlock
        #
         def Act297(): 
               ##line 706 "GJavaParser.g"
                self.setResult(
                    ##line 706 GJavaParser.g
                    SwitchStatement(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 706 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 706 GJavaParser.g
                                    AstToken(self.getRhsIToken(2)),
                                    ##line 706 GJavaParser.g
                                    self.getRhsSym(3),
                                    ##line 706 GJavaParser.g
                                    AstToken(self.getRhsIToken(4)),
                                    ##line 706 GJavaParser.g
                                    self.getRhsSym(5))
                ##line 706 GJavaParser.g
                )

         self.__rule_action[297]= Act297

        #
        # Rule 298:  SwitchBlock ::= { SwitchBlockStatementGroupsopt SwitchLabelsopt }
        #
         def Act298(): 
               ##line 708 "GJavaParser.g"
                self.setResult(
                    ##line 708 GJavaParser.g
                    SwitchBlock(self.getLeftIToken(), self.getRightIToken(),
                                ##line 708 GJavaParser.g
                                AstToken(self.getRhsIToken(1)),
                                ##line 708 GJavaParser.g
                                self.getRhsSym(2),
                                ##line 708 GJavaParser.g
                                self.getRhsSym(3),
                                ##line 708 GJavaParser.g
                                AstToken(self.getRhsIToken(4)))
                ##line 708 GJavaParser.g
                )

         self.__rule_action[298]= Act298

        #
        # Rule 299:  SwitchBlockStatementGroups ::= SwitchBlockStatementGroup
        #
        
                 
        #
        # Rule 300:  SwitchBlockStatementGroups ::= SwitchBlockStatementGroups SwitchBlockStatementGroup
        #
         def Act300(): 
               ##line 711 "GJavaParser.g"
                self.setResult(
                    ##line 711 GJavaParser.g
                    SwitchBlockStatementGroups(self.getLeftIToken(), self.getRightIToken(),
                                               ##line 711 GJavaParser.g
                                               self.getRhsSym(1),
                                               ##line 711 GJavaParser.g
                                               self.getRhsSym(2))
                ##line 711 GJavaParser.g
                )

         self.__rule_action[300]= Act300

        #
        # Rule 301:  SwitchBlockStatementGroup ::= SwitchLabels BlockStatements
        #
         def Act301(): 
               ##line 713 "GJavaParser.g"
                self.setResult(
                    ##line 713 GJavaParser.g
                    SwitchBlockStatementGroup(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 713 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 713 GJavaParser.g
                                              self.getRhsSym(2))
                ##line 713 GJavaParser.g
                )

         self.__rule_action[301]= Act301

        #
        # Rule 302:  SwitchLabels ::= SwitchLabel
        #
        
                 
        #
        # Rule 303:  SwitchLabels ::= SwitchLabels SwitchLabel
        #
         def Act303(): 
               ##line 716 "GJavaParser.g"
                self.setResult(
                    ##line 716 GJavaParser.g
                    SwitchLabels(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 716 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 716 GJavaParser.g
                                 self.getRhsSym(2))
                ##line 716 GJavaParser.g
                )

         self.__rule_action[303]= Act303

        #
        # Rule 304:  SwitchLabel ::= case ConstantExpression :
        #
         def Act304(): 
               ##line 718 "GJavaParser.g"
                self.setResult(
                    ##line 718 GJavaParser.g
                    SwitchLabel0(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 718 GJavaParser.g
                                 AstToken(self.getRhsIToken(1)),
                                 ##line 718 GJavaParser.g
                                 self.getRhsSym(2),
                                 ##line 718 GJavaParser.g
                                 AstToken(self.getRhsIToken(3)))
                ##line 718 GJavaParser.g
                )

         self.__rule_action[304]= Act304

        #
        # Rule 305:  SwitchLabel ::= case EnumConstant :
        #
         def Act305(): 
               ##line 719 "GJavaParser.g"
                self.setResult(
                    ##line 719 GJavaParser.g
                    SwitchLabel1(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 719 GJavaParser.g
                                 AstToken(self.getRhsIToken(1)),
                                 ##line 719 GJavaParser.g
                                 self.getRhsSym(2),
                                 ##line 719 GJavaParser.g
                                 AstToken(self.getRhsIToken(3)))
                ##line 719 GJavaParser.g
                )

         self.__rule_action[305]= Act305

        #
        # Rule 306:  SwitchLabel ::= default :
        #
         def Act306(): 
               ##line 720 "GJavaParser.g"
                self.setResult(
                    ##line 720 GJavaParser.g
                    SwitchLabel2(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 720 GJavaParser.g
                                 AstToken(self.getRhsIToken(1)),
                                 ##line 720 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)))
                ##line 720 GJavaParser.g
                )

         self.__rule_action[306]= Act306

        #
        # Rule 307:  EnumConstant ::= identifier
        #
        
                 
        #
        # Rule 308:  WhileStatement ::= while ( Expression ) Statement
        #
         def Act308(): 
               ##line 724 "GJavaParser.g"
                self.setResult(
                    ##line 724 GJavaParser.g
                    WhileStatement(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 724 GJavaParser.g
                                   AstToken(self.getRhsIToken(1)),
                                   ##line 724 GJavaParser.g
                                   AstToken(self.getRhsIToken(2)),
                                   ##line 724 GJavaParser.g
                                   self.getRhsSym(3),
                                   ##line 724 GJavaParser.g
                                   AstToken(self.getRhsIToken(4)),
                                   ##line 724 GJavaParser.g
                                   self.getRhsSym(5))
                ##line 724 GJavaParser.g
                )

         self.__rule_action[308]= Act308

        #
        # Rule 309:  WhileStatementNoShortIf ::= while ( Expression ) StatementNoShortIf
        #
         def Act309(): 
               ##line 726 "GJavaParser.g"
                self.setResult(
                    ##line 726 GJavaParser.g
                    WhileStatementNoShortIf(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 726 GJavaParser.g
                                            AstToken(self.getRhsIToken(1)),
                                            ##line 726 GJavaParser.g
                                            AstToken(self.getRhsIToken(2)),
                                            ##line 726 GJavaParser.g
                                            self.getRhsSym(3),
                                            ##line 726 GJavaParser.g
                                            AstToken(self.getRhsIToken(4)),
                                            ##line 726 GJavaParser.g
                                            self.getRhsSym(5))
                ##line 726 GJavaParser.g
                )

         self.__rule_action[309]= Act309

        #
        # Rule 310:  DoStatement ::= do Statement while ( Expression ) ;
        #
         def Act310(): 
               ##line 728 "GJavaParser.g"
                self.setResult(
                    ##line 728 GJavaParser.g
                    DoStatement(self.getLeftIToken(), self.getRightIToken(),
                                ##line 728 GJavaParser.g
                                AstToken(self.getRhsIToken(1)),
                                ##line 728 GJavaParser.g
                                self.getRhsSym(2),
                                ##line 728 GJavaParser.g
                                AstToken(self.getRhsIToken(3)),
                                ##line 728 GJavaParser.g
                                AstToken(self.getRhsIToken(4)),
                                ##line 728 GJavaParser.g
                                self.getRhsSym(5),
                                ##line 728 GJavaParser.g
                                AstToken(self.getRhsIToken(6)),
                                ##line 728 GJavaParser.g
                                AstToken(self.getRhsIToken(7)))
                ##line 728 GJavaParser.g
                )

         self.__rule_action[310]= Act310

        #
        # Rule 311:  ForStatement ::= BasicForStatement
        #
        
                 
        #
        # Rule 312:  ForStatement ::= EnhancedForStatement
        #
        
                 
        #
        # Rule 313:  BasicForStatement ::= for ( ForInitopt ; Expressionopt ; ForUpdateopt ) Statement
        #
         def Act313(): 
               ##line 733 "GJavaParser.g"
                self.setResult(
                    ##line 733 GJavaParser.g
                    BasicForStatement(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 733 GJavaParser.g
                                      AstToken(self.getRhsIToken(1)),
                                      ##line 733 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 733 GJavaParser.g
                                      self.getRhsSym(3),
                                      ##line 733 GJavaParser.g
                                      AstToken(self.getRhsIToken(4)),
                                      ##line 733 GJavaParser.g
                                      self.getRhsSym(5),
                                      ##line 733 GJavaParser.g
                                      AstToken(self.getRhsIToken(6)),
                                      ##line 733 GJavaParser.g
                                      self.getRhsSym(7),
                                      ##line 733 GJavaParser.g
                                      AstToken(self.getRhsIToken(8)),
                                      ##line 733 GJavaParser.g
                                      self.getRhsSym(9))
                ##line 733 GJavaParser.g
                )

         self.__rule_action[313]= Act313

        #
        # Rule 314:  ForStatementNoShortIf ::= for ( ForInitopt ; Expressionopt ; ForUpdateopt ) StatementNoShortIf
        #
         def Act314(): 
               ##line 735 "GJavaParser.g"
                self.setResult(
                    ##line 735 GJavaParser.g
                    ForStatementNoShortIf(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 735 GJavaParser.g
                                          AstToken(self.getRhsIToken(1)),
                                          ##line 735 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 735 GJavaParser.g
                                          self.getRhsSym(3),
                                          ##line 735 GJavaParser.g
                                          AstToken(self.getRhsIToken(4)),
                                          ##line 735 GJavaParser.g
                                          self.getRhsSym(5),
                                          ##line 735 GJavaParser.g
                                          AstToken(self.getRhsIToken(6)),
                                          ##line 735 GJavaParser.g
                                          self.getRhsSym(7),
                                          ##line 735 GJavaParser.g
                                          AstToken(self.getRhsIToken(8)),
                                          ##line 735 GJavaParser.g
                                          self.getRhsSym(9))
                ##line 735 GJavaParser.g
                )

         self.__rule_action[314]= Act314

        #
        # Rule 315:  ForInit ::= StatementExpressionList
        #
        
                 
        #
        # Rule 316:  ForInit ::= LocalVariableDeclaration
        #
        
                 
        #
        # Rule 317:  ForUpdate ::= StatementExpressionList
        #
        
                 
        #
        # Rule 318:  StatementExpressionList ::= StatementExpression
        #
        
                 
        #
        # Rule 319:  StatementExpressionList ::= StatementExpressionList , StatementExpression
        #
         def Act319(): 
               ##line 743 "GJavaParser.g"
                self.setResult(
                    ##line 743 GJavaParser.g
                    StatementExpressionList(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 743 GJavaParser.g
                                            self.getRhsSym(1),
                                            ##line 743 GJavaParser.g
                                            AstToken(self.getRhsIToken(2)),
                                            ##line 743 GJavaParser.g
                                            self.getRhsSym(3))
                ##line 743 GJavaParser.g
                )

         self.__rule_action[319]= Act319

        #
        # Rule 320:  EnhancedForStatement ::= for ( FormalParameter : Expression ) Statement
        #
         def Act320(): 
               ##line 745 "GJavaParser.g"
                self.setResult(
                    ##line 745 GJavaParser.g
                    EnhancedForStatement(self.getLeftIToken(), self.getRightIToken(),
                                         ##line 745 GJavaParser.g
                                         AstToken(self.getRhsIToken(1)),
                                         ##line 745 GJavaParser.g
                                         AstToken(self.getRhsIToken(2)),
                                         ##line 745 GJavaParser.g
                                         self.getRhsSym(3),
                                         ##line 745 GJavaParser.g
                                         AstToken(self.getRhsIToken(4)),
                                         ##line 745 GJavaParser.g
                                         self.getRhsSym(5),
                                         ##line 745 GJavaParser.g
                                         AstToken(self.getRhsIToken(6)),
                                         ##line 745 GJavaParser.g
                                         self.getRhsSym(7))
                ##line 745 GJavaParser.g
                )

         self.__rule_action[320]= Act320

        #
        # Rule 321:  BreakStatement ::= break identifieropt ;
        #
         def Act321(): 
               ##line 747 "GJavaParser.g"
                self.setResult(
                    ##line 747 GJavaParser.g
                    BreakStatement(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 747 GJavaParser.g
                                   AstToken(self.getRhsIToken(1)),
                                   ##line 747 GJavaParser.g
                                   self.getRhsSym(2),
                                   ##line 747 GJavaParser.g
                                   AstToken(self.getRhsIToken(3)))
                ##line 747 GJavaParser.g
                )

         self.__rule_action[321]= Act321

        #
        # Rule 322:  ContinueStatement ::= continue identifieropt ;
        #
         def Act322(): 
               ##line 749 "GJavaParser.g"
                self.setResult(
                    ##line 749 GJavaParser.g
                    ContinueStatement(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 749 GJavaParser.g
                                      AstToken(self.getRhsIToken(1)),
                                      ##line 749 GJavaParser.g
                                      self.getRhsSym(2),
                                      ##line 749 GJavaParser.g
                                      AstToken(self.getRhsIToken(3)))
                ##line 749 GJavaParser.g
                )

         self.__rule_action[322]= Act322

        #
        # Rule 323:  ReturnStatement ::= return Expressionopt ;
        #
         def Act323(): 
               ##line 751 "GJavaParser.g"
                self.setResult(
                    ##line 751 GJavaParser.g
                    ReturnStatement(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 751 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 751 GJavaParser.g
                                    self.getRhsSym(2),
                                    ##line 751 GJavaParser.g
                                    AstToken(self.getRhsIToken(3)))
                ##line 751 GJavaParser.g
                )

         self.__rule_action[323]= Act323

        #
        # Rule 324:  ThrowStatement ::= throw Expression ;
        #
         def Act324(): 
               ##line 753 "GJavaParser.g"
                self.setResult(
                    ##line 753 GJavaParser.g
                    ThrowStatement(self.getLeftIToken(), self.getRightIToken(),
                                   ##line 753 GJavaParser.g
                                   AstToken(self.getRhsIToken(1)),
                                   ##line 753 GJavaParser.g
                                   self.getRhsSym(2),
                                   ##line 753 GJavaParser.g
                                   AstToken(self.getRhsIToken(3)))
                ##line 753 GJavaParser.g
                )

         self.__rule_action[324]= Act324

        #
        # Rule 325:  SynchronizedStatement ::= synchronized ( Expression ) Block
        #
         def Act325(): 
               ##line 755 "GJavaParser.g"
                self.setResult(
                    ##line 755 GJavaParser.g
                    SynchronizedStatement(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 755 GJavaParser.g
                                          AstToken(self.getRhsIToken(1)),
                                          ##line 755 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 755 GJavaParser.g
                                          self.getRhsSym(3),
                                          ##line 755 GJavaParser.g
                                          AstToken(self.getRhsIToken(4)),
                                          ##line 755 GJavaParser.g
                                          self.getRhsSym(5))
                ##line 755 GJavaParser.g
                )

         self.__rule_action[325]= Act325

        #
        # Rule 326:  TryStatement ::= try Block Catches
        #
         def Act326(): 
               ##line 757 "GJavaParser.g"
                self.setResult(
                    ##line 757 GJavaParser.g
                    TryStatement0(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 757 GJavaParser.g
                                  AstToken(self.getRhsIToken(1)),
                                  ##line 757 GJavaParser.g
                                  self.getRhsSym(2),
                                  ##line 757 GJavaParser.g
                                  self.getRhsSym(3))
                ##line 757 GJavaParser.g
                )

         self.__rule_action[326]= Act326

        #
        # Rule 327:  TryStatement ::= try Block Catchesopt Finally
        #
         def Act327(): 
               ##line 758 "GJavaParser.g"
                self.setResult(
                    ##line 758 GJavaParser.g
                    TryStatement1(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 758 GJavaParser.g
                                  AstToken(self.getRhsIToken(1)),
                                  ##line 758 GJavaParser.g
                                  self.getRhsSym(2),
                                  ##line 758 GJavaParser.g
                                  self.getRhsSym(3),
                                  ##line 758 GJavaParser.g
                                  self.getRhsSym(4))
                ##line 758 GJavaParser.g
                )

         self.__rule_action[327]= Act327

        #
        # Rule 328:  Catches ::= CatchClause
        #
        
                 
        #
        # Rule 329:  Catches ::= Catches CatchClause
        #
         def Act329(): 
               ##line 761 "GJavaParser.g"
                self.setResult(
                    ##line 761 GJavaParser.g
                    Catches(self.getLeftIToken(), self.getRightIToken(),
                            ##line 761 GJavaParser.g
                            self.getRhsSym(1),
                            ##line 761 GJavaParser.g
                            self.getRhsSym(2))
                ##line 761 GJavaParser.g
                )

         self.__rule_action[329]= Act329

        #
        # Rule 330:  CatchClause ::= catch ( FormalParameter ) Block
        #
         def Act330(): 
               ##line 763 "GJavaParser.g"
                self.setResult(
                    ##line 763 GJavaParser.g
                    CatchClause(self.getLeftIToken(), self.getRightIToken(),
                                ##line 763 GJavaParser.g
                                AstToken(self.getRhsIToken(1)),
                                ##line 763 GJavaParser.g
                                AstToken(self.getRhsIToken(2)),
                                ##line 763 GJavaParser.g
                                self.getRhsSym(3),
                                ##line 763 GJavaParser.g
                                AstToken(self.getRhsIToken(4)),
                                ##line 763 GJavaParser.g
                                self.getRhsSym(5))
                ##line 763 GJavaParser.g
                )

         self.__rule_action[330]= Act330

        #
        # Rule 331:  Finally ::= finally Block
        #
         def Act331(): 
               ##line 765 "GJavaParser.g"
                self.setResult(
                    ##line 765 GJavaParser.g
                    Finally(self.getLeftIToken(), self.getRightIToken(),
                            ##line 765 GJavaParser.g
                            AstToken(self.getRhsIToken(1)),
                            ##line 765 GJavaParser.g
                            self.getRhsSym(2))
                ##line 765 GJavaParser.g
                )

         self.__rule_action[331]= Act331

        #
        # Rule 332:  Primary ::= PrimaryNoNewArray
        #
        
                 
        #
        # Rule 333:  Primary ::= ArrayCreationExpression
        #
        
                 
        #
        # Rule 334:  PrimaryNoNewArray ::= Literal
        #
        
                 
        #
        # Rule 335:  PrimaryNoNewArray ::= Type . class
        #
         def Act335(): 
               ##line 781 "GJavaParser.g"
                self.setResult(
                    ##line 781 GJavaParser.g
                    PrimaryNoNewArray0(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 781 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 781 GJavaParser.g
                                       AstToken(self.getRhsIToken(2)),
                                       ##line 781 GJavaParser.g
                                       AstToken(self.getRhsIToken(3)))
                ##line 781 GJavaParser.g
                )

         self.__rule_action[335]= Act335

        #
        # Rule 336:  PrimaryNoNewArray ::= void . class
        #
         def Act336(): 
               ##line 782 "GJavaParser.g"
                self.setResult(
                    ##line 782 GJavaParser.g
                    PrimaryNoNewArray1(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 782 GJavaParser.g
                                       AstToken(self.getRhsIToken(1)),
                                       ##line 782 GJavaParser.g
                                       AstToken(self.getRhsIToken(2)),
                                       ##line 782 GJavaParser.g
                                       AstToken(self.getRhsIToken(3)))
                ##line 782 GJavaParser.g
                )

         self.__rule_action[336]= Act336

        #
        # Rule 337:  PrimaryNoNewArray ::= this
        #
         def Act337(): 
               ##line 783 "GJavaParser.g"
                self.setResult(
                    ##line 783 GJavaParser.g
                    PrimaryNoNewArray2(self.getRhsIToken(1))
                ##line 783 GJavaParser.g
                )

         self.__rule_action[337]= Act337

        #
        # Rule 338:  PrimaryNoNewArray ::= ClassName . this
        #
         def Act338(): 
               ##line 784 "GJavaParser.g"
                self.setResult(
                    ##line 784 GJavaParser.g
                    PrimaryNoNewArray3(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 784 GJavaParser.g
                                       self.getRhsSym(1),
                                       ##line 784 GJavaParser.g
                                       AstToken(self.getRhsIToken(2)),
                                       ##line 784 GJavaParser.g
                                       AstToken(self.getRhsIToken(3)))
                ##line 784 GJavaParser.g
                )

         self.__rule_action[338]= Act338

        #
        # Rule 339:  PrimaryNoNewArray ::= ( Expression )
        #
         def Act339(): 
               ##line 785 "GJavaParser.g"
                self.setResult(
                    ##line 785 GJavaParser.g
                    PrimaryNoNewArray4(self.getLeftIToken(), self.getRightIToken(),
                                       ##line 785 GJavaParser.g
                                       AstToken(self.getRhsIToken(1)),
                                       ##line 785 GJavaParser.g
                                       self.getRhsSym(2),
                                       ##line 785 GJavaParser.g
                                       AstToken(self.getRhsIToken(3)))
                ##line 785 GJavaParser.g
                )

         self.__rule_action[339]= Act339

        #
        # Rule 340:  PrimaryNoNewArray ::= ClassInstanceCreationExpression
        #
        
                 
        #
        # Rule 341:  PrimaryNoNewArray ::= FieldAccess
        #
        
                 
        #
        # Rule 342:  PrimaryNoNewArray ::= MethodInvocation
        #
        
                 
        #
        # Rule 343:  PrimaryNoNewArray ::= ArrayAccess
        #
        
                 
        #
        # Rule 344:  Literal ::= IntegerLiteral
        #
         def Act344(): 
               ##line 791 "GJavaParser.g"
                self.setResult(
                    ##line 791 GJavaParser.g
                    Literal0(self.getRhsIToken(1))
                ##line 791 GJavaParser.g
                )

         self.__rule_action[344]= Act344

        #
        # Rule 345:  Literal ::= LongLiteral
        #
         def Act345(): 
               ##line 792 "GJavaParser.g"
                self.setResult(
                    ##line 792 GJavaParser.g
                    Literal1(self.getRhsIToken(1))
                ##line 792 GJavaParser.g
                )

         self.__rule_action[345]= Act345

        #
        # Rule 346:  Literal ::= FloatingPointLiteral
        #
         def Act346(): 
               ##line 793 "GJavaParser.g"
                self.setResult(
                    ##line 793 GJavaParser.g
                    Literal2(self.getRhsIToken(1))
                ##line 793 GJavaParser.g
                )

         self.__rule_action[346]= Act346

        #
        # Rule 347:  Literal ::= DoubleLiteral
        #
         def Act347(): 
               ##line 794 "GJavaParser.g"
                self.setResult(
                    ##line 794 GJavaParser.g
                    Literal3(self.getRhsIToken(1))
                ##line 794 GJavaParser.g
                )

         self.__rule_action[347]= Act347

        #
        # Rule 348:  Literal ::= BooleanLiteral
        #
        
                 
        #
        # Rule 349:  Literal ::= CharacterLiteral
        #
         def Act349(): 
               ##line 796 "GJavaParser.g"
                self.setResult(
                    ##line 796 GJavaParser.g
                    Literal4(self.getRhsIToken(1))
                ##line 796 GJavaParser.g
                )

         self.__rule_action[349]= Act349

        #
        # Rule 350:  Literal ::= StringLiteral
        #
         def Act350(): 
               ##line 797 "GJavaParser.g"
                self.setResult(
                    ##line 797 GJavaParser.g
                    Literal5(self.getRhsIToken(1))
                ##line 797 GJavaParser.g
                )

         self.__rule_action[350]= Act350

        #
        # Rule 351:  Literal ::= null
        #
         def Act351(): 
               ##line 798 "GJavaParser.g"
                self.setResult(
                    ##line 798 GJavaParser.g
                    Literal6(self.getRhsIToken(1))
                ##line 798 GJavaParser.g
                )

         self.__rule_action[351]= Act351

        #
        # Rule 352:  BooleanLiteral ::= true
        #
         def Act352(): 
               ##line 800 "GJavaParser.g"
                self.setResult(
                    ##line 800 GJavaParser.g
                    BooleanLiteral0(self.getRhsIToken(1))
                ##line 800 GJavaParser.g
                )

         self.__rule_action[352]= Act352

        #
        # Rule 353:  BooleanLiteral ::= false
        #
         def Act353(): 
               ##line 801 "GJavaParser.g"
                self.setResult(
                    ##line 801 GJavaParser.g
                    BooleanLiteral1(self.getRhsIToken(1))
                ##line 801 GJavaParser.g
                )

         self.__rule_action[353]= Act353

        #
        # Rule 354:  ClassInstanceCreationExpression ::= new TypeArgumentsopt ClassOrInterfaceType TypeArgumentsopt ( ArgumentListopt ) ClassBodyopt
        #
         def Act354(): 
               ##line 808 "GJavaParser.g"
                self.setResult(
                    ##line 808 GJavaParser.g
                    ClassInstanceCreationExpression0(self.getLeftIToken(), self.getRightIToken(),
                                                     ##line 808 GJavaParser.g
                                                     AstToken(self.getRhsIToken(1)),
                                                     ##line 808 GJavaParser.g
                                                     self.getRhsSym(2),
                                                     ##line 808 GJavaParser.g
                                                     self.getRhsSym(3),
                                                     ##line 808 GJavaParser.g
                                                     self.getRhsSym(4),
                                                     ##line 808 GJavaParser.g
                                                     AstToken(self.getRhsIToken(5)),
                                                     ##line 808 GJavaParser.g
                                                     self.getRhsSym(6),
                                                     ##line 808 GJavaParser.g
                                                     AstToken(self.getRhsIToken(7)),
                                                     ##line 808 GJavaParser.g
                                                     self.getRhsSym(8))
                ##line 808 GJavaParser.g
                )

         self.__rule_action[354]= Act354

        #
        # Rule 355:  ClassInstanceCreationExpression ::= Primary . new TypeArgumentsopt identifier TypeArgumentsopt ( ArgumentListopt ) ClassBodyopt
        #
         def Act355(): 
               ##line 809 "GJavaParser.g"
                self.setResult(
                    ##line 809 GJavaParser.g
                    ClassInstanceCreationExpression1(self.getLeftIToken(), self.getRightIToken(),
                                                     ##line 809 GJavaParser.g
                                                     self.getRhsSym(1),
                                                     ##line 809 GJavaParser.g
                                                     AstToken(self.getRhsIToken(2)),
                                                     ##line 809 GJavaParser.g
                                                     AstToken(self.getRhsIToken(3)),
                                                     ##line 809 GJavaParser.g
                                                     self.getRhsSym(4),
                                                     ##line 809 GJavaParser.g
                                                     self.getRhsSym(5),
                                                     ##line 809 GJavaParser.g
                                                     self.getRhsSym(6),
                                                     ##line 809 GJavaParser.g
                                                     AstToken(self.getRhsIToken(7)),
                                                     ##line 809 GJavaParser.g
                                                     self.getRhsSym(8),
                                                     ##line 809 GJavaParser.g
                                                     AstToken(self.getRhsIToken(9)),
                                                     ##line 809 GJavaParser.g
                                                     self.getRhsSym(10))
                ##line 809 GJavaParser.g
                )

         self.__rule_action[355]= Act355

        #
        # Rule 356:  ArgumentList ::= Expression
        #
        
                 
        #
        # Rule 357:  ArgumentList ::= ArgumentList , Expression
        #
         def Act357(): 
               ##line 813 "GJavaParser.g"
                self.setResult(
                    ##line 813 GJavaParser.g
                    ArgumentList(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 813 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 813 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)),
                                 ##line 813 GJavaParser.g
                                 self.getRhsSym(3))
                ##line 813 GJavaParser.g
                )

         self.__rule_action[357]= Act357

        #
        # Rule 358:  ArrayCreationExpression ::= new PrimitiveType DimExprs Dimsopt
        #
         def Act358(): 
               ##line 823 "GJavaParser.g"
                self.setResult(
                    ##line 823 GJavaParser.g
                    ArrayCreationExpression0(self.getLeftIToken(), self.getRightIToken(),
                                             ##line 823 GJavaParser.g
                                             AstToken(self.getRhsIToken(1)),
                                             ##line 823 GJavaParser.g
                                             self.getRhsSym(2),
                                             ##line 823 GJavaParser.g
                                             self.getRhsSym(3),
                                             ##line 823 GJavaParser.g
                                             self.getRhsSym(4))
                ##line 823 GJavaParser.g
                )

         self.__rule_action[358]= Act358

        #
        # Rule 359:  ArrayCreationExpression ::= new ClassOrInterfaceType DimExprs Dimsopt
        #
         def Act359(): 
               ##line 824 "GJavaParser.g"
                self.setResult(
                    ##line 824 GJavaParser.g
                    ArrayCreationExpression1(self.getLeftIToken(), self.getRightIToken(),
                                             ##line 824 GJavaParser.g
                                             AstToken(self.getRhsIToken(1)),
                                             ##line 824 GJavaParser.g
                                             self.getRhsSym(2),
                                             ##line 824 GJavaParser.g
                                             self.getRhsSym(3),
                                             ##line 824 GJavaParser.g
                                             self.getRhsSym(4))
                ##line 824 GJavaParser.g
                )

         self.__rule_action[359]= Act359

        #
        # Rule 360:  ArrayCreationExpression ::= new PrimitiveType Dims ArrayInitializer
        #
         def Act360(): 
               ##line 825 "GJavaParser.g"
                self.setResult(
                    ##line 825 GJavaParser.g
                    ArrayCreationExpression2(self.getLeftIToken(), self.getRightIToken(),
                                             ##line 825 GJavaParser.g
                                             AstToken(self.getRhsIToken(1)),
                                             ##line 825 GJavaParser.g
                                             self.getRhsSym(2),
                                             ##line 825 GJavaParser.g
                                             self.getRhsSym(3),
                                             ##line 825 GJavaParser.g
                                             self.getRhsSym(4))
                ##line 825 GJavaParser.g
                )

         self.__rule_action[360]= Act360

        #
        # Rule 361:  ArrayCreationExpression ::= new ClassOrInterfaceType Dims ArrayInitializer
        #
         def Act361(): 
               ##line 826 "GJavaParser.g"
                self.setResult(
                    ##line 826 GJavaParser.g
                    ArrayCreationExpression3(self.getLeftIToken(), self.getRightIToken(),
                                             ##line 826 GJavaParser.g
                                             AstToken(self.getRhsIToken(1)),
                                             ##line 826 GJavaParser.g
                                             self.getRhsSym(2),
                                             ##line 826 GJavaParser.g
                                             self.getRhsSym(3),
                                             ##line 826 GJavaParser.g
                                             self.getRhsSym(4))
                ##line 826 GJavaParser.g
                )

         self.__rule_action[361]= Act361

        #
        # Rule 362:  DimExprs ::= DimExpr
        #
        
                 
        #
        # Rule 363:  DimExprs ::= DimExprs DimExpr
        #
         def Act363(): 
               ##line 829 "GJavaParser.g"
                self.setResult(
                    ##line 829 GJavaParser.g
                    DimExprs(self.getLeftIToken(), self.getRightIToken(),
                             ##line 829 GJavaParser.g
                             self.getRhsSym(1),
                             ##line 829 GJavaParser.g
                             self.getRhsSym(2))
                ##line 829 GJavaParser.g
                )

         self.__rule_action[363]= Act363

        #
        # Rule 364:  DimExpr ::= [ Expression ]
        #
         def Act364(): 
               ##line 831 "GJavaParser.g"
                self.setResult(
                    ##line 831 GJavaParser.g
                    DimExpr(self.getLeftIToken(), self.getRightIToken(),
                            ##line 831 GJavaParser.g
                            AstToken(self.getRhsIToken(1)),
                            ##line 831 GJavaParser.g
                            self.getRhsSym(2),
                            ##line 831 GJavaParser.g
                            AstToken(self.getRhsIToken(3)))
                ##line 831 GJavaParser.g
                )

         self.__rule_action[364]= Act364

        #
        # Rule 365:  Dims ::= [ ]
        #
         def Act365(): 
               ##line 833 "GJavaParser.g"
                self.setResult(
                    ##line 833 GJavaParser.g
                    Dims0(self.getLeftIToken(), self.getRightIToken(),
                          ##line 833 GJavaParser.g
                          AstToken(self.getRhsIToken(1)),
                          ##line 833 GJavaParser.g
                          AstToken(self.getRhsIToken(2)))
                ##line 833 GJavaParser.g
                )

         self.__rule_action[365]= Act365

        #
        # Rule 366:  Dims ::= Dims [ ]
        #
         def Act366(): 
               ##line 834 "GJavaParser.g"
                self.setResult(
                    ##line 834 GJavaParser.g
                    Dims1(self.getLeftIToken(), self.getRightIToken(),
                          ##line 834 GJavaParser.g
                          self.getRhsSym(1),
                          ##line 834 GJavaParser.g
                          AstToken(self.getRhsIToken(2)),
                          ##line 834 GJavaParser.g
                          AstToken(self.getRhsIToken(3)))
                ##line 834 GJavaParser.g
                )

         self.__rule_action[366]= Act366

        #
        # Rule 367:  FieldAccess ::= Primary . identifier
        #
         def Act367(): 
               ##line 836 "GJavaParser.g"
                self.setResult(
                    ##line 836 GJavaParser.g
                    FieldAccess0(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 836 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 836 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)),
                                 ##line 836 GJavaParser.g
                                 self.getRhsSym(3))
                ##line 836 GJavaParser.g
                )

         self.__rule_action[367]= Act367

        #
        # Rule 368:  FieldAccess ::= super . identifier
        #
         def Act368(): 
               ##line 837 "GJavaParser.g"
                self.setResult(
                    ##line 837 GJavaParser.g
                    FieldAccess1(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 837 GJavaParser.g
                                 AstToken(self.getRhsIToken(1)),
                                 ##line 837 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)),
                                 ##line 837 GJavaParser.g
                                 self.getRhsSym(3))
                ##line 837 GJavaParser.g
                )

         self.__rule_action[368]= Act368

        #
        # Rule 369:  FieldAccess ::= ClassName . super . identifier
        #
         def Act369(): 
               ##line 838 "GJavaParser.g"
                self.setResult(
                    ##line 838 GJavaParser.g
                    FieldAccess2(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 838 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 838 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)),
                                 ##line 838 GJavaParser.g
                                 AstToken(self.getRhsIToken(3)),
                                 ##line 838 GJavaParser.g
                                 AstToken(self.getRhsIToken(4)),
                                 ##line 838 GJavaParser.g
                                 self.getRhsSym(5))
                ##line 838 GJavaParser.g
                )

         self.__rule_action[369]= Act369

        #
        # Rule 370:  MethodInvocation ::= MethodName ( ArgumentListopt )
        #
         def Act370(): 
               ##line 840 "GJavaParser.g"
                self.setResult(
                    ##line 840 GJavaParser.g
                    MethodInvocation0(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 840 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 840 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 840 GJavaParser.g
                                      self.getRhsSym(3),
                                      ##line 840 GJavaParser.g
                                      AstToken(self.getRhsIToken(4)))
                ##line 840 GJavaParser.g
                )

         self.__rule_action[370]= Act370

        #
        # Rule 371:  MethodInvocation ::= Primary . TypeArgumentsopt identifier ( ArgumentListopt )
        #
         def Act371(): 
               ##line 841 "GJavaParser.g"
                self.setResult(
                    ##line 841 GJavaParser.g
                    MethodInvocation1(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 841 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 841 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 841 GJavaParser.g
                                      self.getRhsSym(3),
                                      ##line 841 GJavaParser.g
                                      self.getRhsSym(4),
                                      ##line 841 GJavaParser.g
                                      AstToken(self.getRhsIToken(5)),
                                      ##line 841 GJavaParser.g
                                      self.getRhsSym(6),
                                      ##line 841 GJavaParser.g
                                      AstToken(self.getRhsIToken(7)))
                ##line 841 GJavaParser.g
                )

         self.__rule_action[371]= Act371

        #
        # Rule 372:  MethodInvocation ::= super . TypeArgumentsopt identifier ( ArgumentListopt )
        #
         def Act372(): 
               ##line 842 "GJavaParser.g"
                self.setResult(
                    ##line 842 GJavaParser.g
                    MethodInvocation2(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 842 GJavaParser.g
                                      AstToken(self.getRhsIToken(1)),
                                      ##line 842 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 842 GJavaParser.g
                                      self.getRhsSym(3),
                                      ##line 842 GJavaParser.g
                                      self.getRhsSym(4),
                                      ##line 842 GJavaParser.g
                                      AstToken(self.getRhsIToken(5)),
                                      ##line 842 GJavaParser.g
                                      self.getRhsSym(6),
                                      ##line 842 GJavaParser.g
                                      AstToken(self.getRhsIToken(7)))
                ##line 842 GJavaParser.g
                )

         self.__rule_action[372]= Act372

        #
        # Rule 373:  MethodInvocation ::= ClassName . super . TypeArgumentsopt identifier ( ArgumentListopt )
        #
         def Act373(): 
               ##line 843 "GJavaParser.g"
                self.setResult(
                    ##line 843 GJavaParser.g
                    MethodInvocation3(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 843 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 843 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 843 GJavaParser.g
                                      AstToken(self.getRhsIToken(3)),
                                      ##line 843 GJavaParser.g
                                      AstToken(self.getRhsIToken(4)),
                                      ##line 843 GJavaParser.g
                                      self.getRhsSym(5),
                                      ##line 843 GJavaParser.g
                                      self.getRhsSym(6),
                                      ##line 843 GJavaParser.g
                                      AstToken(self.getRhsIToken(7)),
                                      ##line 843 GJavaParser.g
                                      self.getRhsSym(8),
                                      ##line 843 GJavaParser.g
                                      AstToken(self.getRhsIToken(9)))
                ##line 843 GJavaParser.g
                )

         self.__rule_action[373]= Act373

        #
        # Rule 374:  MethodInvocation ::= TypeName . TypeArguments identifier ( ArgumentListopt )
        #
         def Act374(): 
               ##line 844 "GJavaParser.g"
                self.setResult(
                    ##line 844 GJavaParser.g
                    MethodInvocation4(self.getLeftIToken(), self.getRightIToken(),
                                      ##line 844 GJavaParser.g
                                      self.getRhsSym(1),
                                      ##line 844 GJavaParser.g
                                      AstToken(self.getRhsIToken(2)),
                                      ##line 844 GJavaParser.g
                                      self.getRhsSym(3),
                                      ##line 844 GJavaParser.g
                                      self.getRhsSym(4),
                                      ##line 844 GJavaParser.g
                                      AstToken(self.getRhsIToken(5)),
                                      ##line 844 GJavaParser.g
                                      self.getRhsSym(6),
                                      ##line 844 GJavaParser.g
                                      AstToken(self.getRhsIToken(7)))
                ##line 844 GJavaParser.g
                )

         self.__rule_action[374]= Act374

        #
        # Rule 375:  ArrayAccess ::= ExpressionName [ Expression ]
        #
         def Act375(): 
               ##line 852 "GJavaParser.g"
                self.setResult(
                    ##line 852 GJavaParser.g
                    ArrayAccess0(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 852 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 852 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)),
                                 ##line 852 GJavaParser.g
                                 self.getRhsSym(3),
                                 ##line 852 GJavaParser.g
                                 AstToken(self.getRhsIToken(4)))
                ##line 852 GJavaParser.g
                )

         self.__rule_action[375]= Act375

        #
        # Rule 376:  ArrayAccess ::= PrimaryNoNewArray [ Expression ]
        #
         def Act376(): 
               ##line 853 "GJavaParser.g"
                self.setResult(
                    ##line 853 GJavaParser.g
                    ArrayAccess1(self.getLeftIToken(), self.getRightIToken(),
                                 ##line 853 GJavaParser.g
                                 self.getRhsSym(1),
                                 ##line 853 GJavaParser.g
                                 AstToken(self.getRhsIToken(2)),
                                 ##line 853 GJavaParser.g
                                 self.getRhsSym(3),
                                 ##line 853 GJavaParser.g
                                 AstToken(self.getRhsIToken(4)))
                ##line 853 GJavaParser.g
                )

         self.__rule_action[376]= Act376

        #
        # Rule 377:  PostfixExpression ::= Primary
        #
        
                 
        #
        # Rule 378:  PostfixExpression ::= ExpressionName
        #
        
                 
        #
        # Rule 379:  PostfixExpression ::= PostIncrementExpression
        #
        
                 
        #
        # Rule 380:  PostfixExpression ::= PostDecrementExpression
        #
        
                 
        #
        # Rule 381:  PostIncrementExpression ::= PostfixExpression ++
        #
         def Act381(): 
               ##line 860 "GJavaParser.g"
                self.setResult(
                    ##line 860 GJavaParser.g
                    PostIncrementExpression(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 860 GJavaParser.g
                                            self.getRhsSym(1),
                                            ##line 860 GJavaParser.g
                                            AstToken(self.getRhsIToken(2)))
                ##line 860 GJavaParser.g
                )

         self.__rule_action[381]= Act381

        #
        # Rule 382:  PostDecrementExpression ::= PostfixExpression --
        #
         def Act382(): 
               ##line 862 "GJavaParser.g"
                self.setResult(
                    ##line 862 GJavaParser.g
                    PostDecrementExpression(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 862 GJavaParser.g
                                            self.getRhsSym(1),
                                            ##line 862 GJavaParser.g
                                            AstToken(self.getRhsIToken(2)))
                ##line 862 GJavaParser.g
                )

         self.__rule_action[382]= Act382

        #
        # Rule 383:  UnaryExpression ::= PreIncrementExpression
        #
        
                 
        #
        # Rule 384:  UnaryExpression ::= PreDecrementExpression
        #
        
                 
        #
        # Rule 385:  UnaryExpression ::= + UnaryExpression
        #
         def Act385(): 
               ##line 866 "GJavaParser.g"
                self.setResult(
                    ##line 866 GJavaParser.g
                    UnaryExpression0(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 866 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 866 GJavaParser.g
                                     self.getRhsSym(2))
                ##line 866 GJavaParser.g
                )

         self.__rule_action[385]= Act385

        #
        # Rule 386:  UnaryExpression ::= - UnaryExpression
        #
         def Act386(): 
               ##line 867 "GJavaParser.g"
                self.setResult(
                    ##line 867 GJavaParser.g
                    UnaryExpression1(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 867 GJavaParser.g
                                     AstToken(self.getRhsIToken(1)),
                                     ##line 867 GJavaParser.g
                                     self.getRhsSym(2))
                ##line 867 GJavaParser.g
                )

         self.__rule_action[386]= Act386

        #
        # Rule 387:  UnaryExpression ::= UnaryExpressionNotPlusMinus
        #
        
                 
        #
        # Rule 388:  PreIncrementExpression ::= ++ UnaryExpression
        #
         def Act388(): 
               ##line 870 "GJavaParser.g"
                self.setResult(
                    ##line 870 GJavaParser.g
                    PreIncrementExpression(self.getLeftIToken(), self.getRightIToken(),
                                           ##line 870 GJavaParser.g
                                           AstToken(self.getRhsIToken(1)),
                                           ##line 870 GJavaParser.g
                                           self.getRhsSym(2))
                ##line 870 GJavaParser.g
                )

         self.__rule_action[388]= Act388

        #
        # Rule 389:  PreDecrementExpression ::= -- UnaryExpression
        #
         def Act389(): 
               ##line 872 "GJavaParser.g"
                self.setResult(
                    ##line 872 GJavaParser.g
                    PreDecrementExpression(self.getLeftIToken(), self.getRightIToken(),
                                           ##line 872 GJavaParser.g
                                           AstToken(self.getRhsIToken(1)),
                                           ##line 872 GJavaParser.g
                                           self.getRhsSym(2))
                ##line 872 GJavaParser.g
                )

         self.__rule_action[389]= Act389

        #
        # Rule 390:  UnaryExpressionNotPlusMinus ::= PostfixExpression
        #
        
                 
        #
        # Rule 391:  UnaryExpressionNotPlusMinus ::= ~ UnaryExpression
        #
         def Act391(): 
               ##line 875 "GJavaParser.g"
                self.setResult(
                    ##line 875 GJavaParser.g
                    UnaryExpressionNotPlusMinus0(self.getLeftIToken(), self.getRightIToken(),
                                                 ##line 875 GJavaParser.g
                                                 AstToken(self.getRhsIToken(1)),
                                                 ##line 875 GJavaParser.g
                                                 self.getRhsSym(2))
                ##line 875 GJavaParser.g
                )

         self.__rule_action[391]= Act391

        #
        # Rule 392:  UnaryExpressionNotPlusMinus ::= ! UnaryExpression
        #
         def Act392(): 
               ##line 876 "GJavaParser.g"
                self.setResult(
                    ##line 876 GJavaParser.g
                    UnaryExpressionNotPlusMinus1(self.getLeftIToken(), self.getRightIToken(),
                                                 ##line 876 GJavaParser.g
                                                 AstToken(self.getRhsIToken(1)),
                                                 ##line 876 GJavaParser.g
                                                 self.getRhsSym(2))
                ##line 876 GJavaParser.g
                )

         self.__rule_action[392]= Act392

        #
        # Rule 393:  UnaryExpressionNotPlusMinus ::= CastExpression
        #
        
                 
        #
        # Rule 394:  CastExpression ::= ( PrimitiveType Dimsopt ) UnaryExpression
        #
         def Act394(): 
               ##line 879 "GJavaParser.g"
                self.setResult(
                    ##line 879 GJavaParser.g
                    CastExpression0(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 879 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 879 GJavaParser.g
                                    self.getRhsSym(2),
                                    ##line 879 GJavaParser.g
                                    self.getRhsSym(3),
                                    ##line 879 GJavaParser.g
                                    AstToken(self.getRhsIToken(4)),
                                    ##line 879 GJavaParser.g
                                    self.getRhsSym(5))
                ##line 879 GJavaParser.g
                )

         self.__rule_action[394]= Act394

        #
        # Rule 395:  CastExpression ::= ( ReferenceType ) UnaryExpressionNotPlusMinus
        #
         def Act395(): 
               ##line 880 "GJavaParser.g"
                self.setResult(
                    ##line 880 GJavaParser.g
                    CastExpression1(self.getLeftIToken(), self.getRightIToken(),
                                    ##line 880 GJavaParser.g
                                    AstToken(self.getRhsIToken(1)),
                                    ##line 880 GJavaParser.g
                                    self.getRhsSym(2),
                                    ##line 880 GJavaParser.g
                                    AstToken(self.getRhsIToken(3)),
                                    ##line 880 GJavaParser.g
                                    self.getRhsSym(4))
                ##line 880 GJavaParser.g
                )

         self.__rule_action[395]= Act395

        #
        # Rule 396:  MultiplicativeExpression ::= UnaryExpression
        #
        
                 
        #
        # Rule 397:  MultiplicativeExpression ::= MultiplicativeExpression * UnaryExpression
        #
         def Act397(): 
               ##line 883 "GJavaParser.g"
                self.setResult(
                    ##line 883 GJavaParser.g
                    MultiplicativeExpression0(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 883 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 883 GJavaParser.g
                                              AstToken(self.getRhsIToken(2)),
                                              ##line 883 GJavaParser.g
                                              self.getRhsSym(3))
                ##line 883 GJavaParser.g
                )

         self.__rule_action[397]= Act397

        #
        # Rule 398:  MultiplicativeExpression ::= MultiplicativeExpression / UnaryExpression
        #
         def Act398(): 
               ##line 884 "GJavaParser.g"
                self.setResult(
                    ##line 884 GJavaParser.g
                    MultiplicativeExpression1(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 884 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 884 GJavaParser.g
                                              AstToken(self.getRhsIToken(2)),
                                              ##line 884 GJavaParser.g
                                              self.getRhsSym(3))
                ##line 884 GJavaParser.g
                )

         self.__rule_action[398]= Act398

        #
        # Rule 399:  MultiplicativeExpression ::= MultiplicativeExpression % UnaryExpression
        #
         def Act399(): 
               ##line 885 "GJavaParser.g"
                self.setResult(
                    ##line 885 GJavaParser.g
                    MultiplicativeExpression2(self.getLeftIToken(), self.getRightIToken(),
                                              ##line 885 GJavaParser.g
                                              self.getRhsSym(1),
                                              ##line 885 GJavaParser.g
                                              AstToken(self.getRhsIToken(2)),
                                              ##line 885 GJavaParser.g
                                              self.getRhsSym(3))
                ##line 885 GJavaParser.g
                )

         self.__rule_action[399]= Act399

        #
        # Rule 400:  AdditiveExpression ::= MultiplicativeExpression
        #
        
                 
        #
        # Rule 401:  AdditiveExpression ::= AdditiveExpression + MultiplicativeExpression
        #
         def Act401(): 
               ##line 888 "GJavaParser.g"
                self.setResult(
                    ##line 888 GJavaParser.g
                    AdditiveExpression0(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 888 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 888 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 888 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 888 GJavaParser.g
                )

         self.__rule_action[401]= Act401

        #
        # Rule 402:  AdditiveExpression ::= AdditiveExpression - MultiplicativeExpression
        #
         def Act402(): 
               ##line 889 "GJavaParser.g"
                self.setResult(
                    ##line 889 GJavaParser.g
                    AdditiveExpression1(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 889 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 889 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 889 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 889 GJavaParser.g
                )

         self.__rule_action[402]= Act402

        #
        # Rule 403:  ShiftExpression ::= AdditiveExpression
        #
        
                 
        #
        # Rule 404:  ShiftExpression ::= ShiftExpression << AdditiveExpression
        #
         def Act404(): 
               ##line 892 "GJavaParser.g"
                self.setResult(
                    ##line 892 GJavaParser.g
                    ShiftExpression0(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 892 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 892 GJavaParser.g
                                     AstToken(self.getRhsIToken(2)),
                                     ##line 892 GJavaParser.g
                                     self.getRhsSym(3))
                ##line 892 GJavaParser.g
                )

         self.__rule_action[404]= Act404

        #
        # Rule 405:  ShiftExpression ::= ShiftExpression > > AdditiveExpression
        #
         def Act405(): 
               ##line 893 "GJavaParser.g"
                self.setResult(
                    ##line 893 GJavaParser.g
                    ShiftExpression1(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 893 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 893 GJavaParser.g
                                     AstToken(self.getRhsIToken(2)),
                                     ##line 893 GJavaParser.g
                                     AstToken(self.getRhsIToken(3)),
                                     ##line 893 GJavaParser.g
                                     self.getRhsSym(4))
                ##line 893 GJavaParser.g
                )

         self.__rule_action[405]= Act405

        #
        # Rule 406:  ShiftExpression ::= ShiftExpression > > > AdditiveExpression
        #
         def Act406(): 
               ##line 894 "GJavaParser.g"
                self.setResult(
                    ##line 894 GJavaParser.g
                    ShiftExpression2(self.getLeftIToken(), self.getRightIToken(),
                                     ##line 894 GJavaParser.g
                                     self.getRhsSym(1),
                                     ##line 894 GJavaParser.g
                                     AstToken(self.getRhsIToken(2)),
                                     ##line 894 GJavaParser.g
                                     AstToken(self.getRhsIToken(3)),
                                     ##line 894 GJavaParser.g
                                     AstToken(self.getRhsIToken(4)),
                                     ##line 894 GJavaParser.g
                                     self.getRhsSym(5))
                ##line 894 GJavaParser.g
                )

         self.__rule_action[406]= Act406

        #
        # Rule 407:  RelationalExpression ::= ShiftExpression
        #
        
                 
        #
        # Rule 408:  RelationalExpression ::= RelationalExpression < ShiftExpression
        #
         def Act408(): 
               ##line 897 "GJavaParser.g"
                self.setResult(
                    ##line 897 GJavaParser.g
                    RelationalExpression0(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 897 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 897 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 897 GJavaParser.g
                                          self.getRhsSym(3))
                ##line 897 GJavaParser.g
                )

         self.__rule_action[408]= Act408

        #
        # Rule 409:  RelationalExpression ::= RelationalExpression > ShiftExpression
        #
         def Act409(): 
               ##line 898 "GJavaParser.g"
                self.setResult(
                    ##line 898 GJavaParser.g
                    RelationalExpression1(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 898 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 898 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 898 GJavaParser.g
                                          self.getRhsSym(3))
                ##line 898 GJavaParser.g
                )

         self.__rule_action[409]= Act409

        #
        # Rule 410:  RelationalExpression ::= RelationalExpression <= ShiftExpression
        #
         def Act410(): 
               ##line 899 "GJavaParser.g"
                self.setResult(
                    ##line 899 GJavaParser.g
                    RelationalExpression2(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 899 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 899 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 899 GJavaParser.g
                                          self.getRhsSym(3))
                ##line 899 GJavaParser.g
                )

         self.__rule_action[410]= Act410

        #
        # Rule 411:  RelationalExpression ::= RelationalExpression > = ShiftExpression
        #
         def Act411(): 
               ##line 900 "GJavaParser.g"
                self.setResult(
                    ##line 900 GJavaParser.g
                    RelationalExpression3(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 900 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 900 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 900 GJavaParser.g
                                          AstToken(self.getRhsIToken(3)),
                                          ##line 900 GJavaParser.g
                                          self.getRhsSym(4))
                ##line 900 GJavaParser.g
                )

         self.__rule_action[411]= Act411

        #
        # Rule 412:  RelationalExpression ::= RelationalExpression instanceof ReferenceType
        #
         def Act412(): 
               ##line 901 "GJavaParser.g"
                self.setResult(
                    ##line 901 GJavaParser.g
                    RelationalExpression4(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 901 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 901 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 901 GJavaParser.g
                                          self.getRhsSym(3))
                ##line 901 GJavaParser.g
                )

         self.__rule_action[412]= Act412

        #
        # Rule 413:  EqualityExpression ::= RelationalExpression
        #
        
                 
        #
        # Rule 414:  EqualityExpression ::= EqualityExpression == RelationalExpression
        #
         def Act414(): 
               ##line 904 "GJavaParser.g"
                self.setResult(
                    ##line 904 GJavaParser.g
                    EqualityExpression0(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 904 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 904 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 904 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 904 GJavaParser.g
                )

         self.__rule_action[414]= Act414

        #
        # Rule 415:  EqualityExpression ::= EqualityExpression != RelationalExpression
        #
         def Act415(): 
               ##line 905 "GJavaParser.g"
                self.setResult(
                    ##line 905 GJavaParser.g
                    EqualityExpression1(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 905 GJavaParser.g
                                        self.getRhsSym(1),
                                        ##line 905 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 905 GJavaParser.g
                                        self.getRhsSym(3))
                ##line 905 GJavaParser.g
                )

         self.__rule_action[415]= Act415

        #
        # Rule 416:  AndExpression ::= EqualityExpression
        #
        
                 
        #
        # Rule 417:  AndExpression ::= AndExpression & EqualityExpression
        #
         def Act417(): 
               ##line 908 "GJavaParser.g"
                self.setResult(
                    ##line 908 GJavaParser.g
                    AndExpression(self.getLeftIToken(), self.getRightIToken(),
                                  ##line 908 GJavaParser.g
                                  self.getRhsSym(1),
                                  ##line 908 GJavaParser.g
                                  AstToken(self.getRhsIToken(2)),
                                  ##line 908 GJavaParser.g
                                  self.getRhsSym(3))
                ##line 908 GJavaParser.g
                )

         self.__rule_action[417]= Act417

        #
        # Rule 418:  ExclusiveOrExpression ::= AndExpression
        #
        
                 
        #
        # Rule 419:  ExclusiveOrExpression ::= ExclusiveOrExpression ^ AndExpression
        #
         def Act419(): 
               ##line 911 "GJavaParser.g"
                self.setResult(
                    ##line 911 GJavaParser.g
                    ExclusiveOrExpression(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 911 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 911 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 911 GJavaParser.g
                                          self.getRhsSym(3))
                ##line 911 GJavaParser.g
                )

         self.__rule_action[419]= Act419

        #
        # Rule 420:  InclusiveOrExpression ::= ExclusiveOrExpression
        #
        
                 
        #
        # Rule 421:  InclusiveOrExpression ::= InclusiveOrExpression | ExclusiveOrExpression
        #
         def Act421(): 
               ##line 914 "GJavaParser.g"
                self.setResult(
                    ##line 914 GJavaParser.g
                    InclusiveOrExpression(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 914 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 914 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 914 GJavaParser.g
                                          self.getRhsSym(3))
                ##line 914 GJavaParser.g
                )

         self.__rule_action[421]= Act421

        #
        # Rule 422:  ConditionalAndExpression ::= InclusiveOrExpression
        #
        
                 
        #
        # Rule 423:  ConditionalAndExpression ::= ConditionalAndExpression && InclusiveOrExpression
        #
         def Act423(): 
               ##line 917 "GJavaParser.g"
                self.setResult(
                    ##line 917 GJavaParser.g
                    ConditionalAndExpression(self.getLeftIToken(), self.getRightIToken(),
                                             ##line 917 GJavaParser.g
                                             self.getRhsSym(1),
                                             ##line 917 GJavaParser.g
                                             AstToken(self.getRhsIToken(2)),
                                             ##line 917 GJavaParser.g
                                             self.getRhsSym(3))
                ##line 917 GJavaParser.g
                )

         self.__rule_action[423]= Act423

        #
        # Rule 424:  ConditionalOrExpression ::= ConditionalAndExpression
        #
        
                 
        #
        # Rule 425:  ConditionalOrExpression ::= ConditionalOrExpression || ConditionalAndExpression
        #
         def Act425(): 
               ##line 920 "GJavaParser.g"
                self.setResult(
                    ##line 920 GJavaParser.g
                    ConditionalOrExpression(self.getLeftIToken(), self.getRightIToken(),
                                            ##line 920 GJavaParser.g
                                            self.getRhsSym(1),
                                            ##line 920 GJavaParser.g
                                            AstToken(self.getRhsIToken(2)),
                                            ##line 920 GJavaParser.g
                                            self.getRhsSym(3))
                ##line 920 GJavaParser.g
                )

         self.__rule_action[425]= Act425

        #
        # Rule 426:  ConditionalExpression ::= ConditionalOrExpression
        #
        
                 
        #
        # Rule 427:  ConditionalExpression ::= ConditionalOrExpression ? Expression : ConditionalExpression
        #
         def Act427(): 
               ##line 923 "GJavaParser.g"
                self.setResult(
                    ##line 923 GJavaParser.g
                    ConditionalExpression(self.getLeftIToken(), self.getRightIToken(),
                                          ##line 923 GJavaParser.g
                                          self.getRhsSym(1),
                                          ##line 923 GJavaParser.g
                                          AstToken(self.getRhsIToken(2)),
                                          ##line 923 GJavaParser.g
                                          self.getRhsSym(3),
                                          ##line 923 GJavaParser.g
                                          AstToken(self.getRhsIToken(4)),
                                          ##line 923 GJavaParser.g
                                          self.getRhsSym(5))
                ##line 923 GJavaParser.g
                )

         self.__rule_action[427]= Act427

        #
        # Rule 428:  AssignmentExpression ::= ConditionalExpression
        #
        
                 
        #
        # Rule 429:  AssignmentExpression ::= Assignment
        #
        
                 
        #
        # Rule 430:  Assignment ::= LeftHandSide AssignmentOperator AssignmentExpression
        #
         def Act430(): 
               ##line 928 "GJavaParser.g"
                self.setResult(
                    ##line 928 GJavaParser.g
                    Assignment(self.getLeftIToken(), self.getRightIToken(),
                               ##line 928 GJavaParser.g
                               self.getRhsSym(1),
                               ##line 928 GJavaParser.g
                               self.getRhsSym(2),
                               ##line 928 GJavaParser.g
                               self.getRhsSym(3))
                ##line 928 GJavaParser.g
                )

         self.__rule_action[430]= Act430

        #
        # Rule 431:  LeftHandSide ::= ExpressionName
        #
        
                 
        #
        # Rule 432:  LeftHandSide ::= FieldAccess
        #
        
                 
        #
        # Rule 433:  LeftHandSide ::= ArrayAccess
        #
        
                 
        #
        # Rule 434:  AssignmentOperator ::= =
        #
         def Act434(): 
               ##line 934 "GJavaParser.g"
                self.setResult(
                    ##line 934 GJavaParser.g
                    AssignmentOperator0(self.getRhsIToken(1))
                ##line 934 GJavaParser.g
                )

         self.__rule_action[434]= Act434

        #
        # Rule 435:  AssignmentOperator ::= *=
        #
         def Act435(): 
               ##line 935 "GJavaParser.g"
                self.setResult(
                    ##line 935 GJavaParser.g
                    AssignmentOperator1(self.getRhsIToken(1))
                ##line 935 GJavaParser.g
                )

         self.__rule_action[435]= Act435

        #
        # Rule 436:  AssignmentOperator ::= /=
        #
         def Act436(): 
               ##line 936 "GJavaParser.g"
                self.setResult(
                    ##line 936 GJavaParser.g
                    AssignmentOperator2(self.getRhsIToken(1))
                ##line 936 GJavaParser.g
                )

         self.__rule_action[436]= Act436

        #
        # Rule 437:  AssignmentOperator ::= %=
        #
         def Act437(): 
               ##line 937 "GJavaParser.g"
                self.setResult(
                    ##line 937 GJavaParser.g
                    AssignmentOperator3(self.getRhsIToken(1))
                ##line 937 GJavaParser.g
                )

         self.__rule_action[437]= Act437

        #
        # Rule 438:  AssignmentOperator ::= +=
        #
         def Act438(): 
               ##line 938 "GJavaParser.g"
                self.setResult(
                    ##line 938 GJavaParser.g
                    AssignmentOperator4(self.getRhsIToken(1))
                ##line 938 GJavaParser.g
                )

         self.__rule_action[438]= Act438

        #
        # Rule 439:  AssignmentOperator ::= -=
        #
         def Act439(): 
               ##line 939 "GJavaParser.g"
                self.setResult(
                    ##line 939 GJavaParser.g
                    AssignmentOperator5(self.getRhsIToken(1))
                ##line 939 GJavaParser.g
                )

         self.__rule_action[439]= Act439

        #
        # Rule 440:  AssignmentOperator ::= <<=
        #
         def Act440(): 
               ##line 940 "GJavaParser.g"
                self.setResult(
                    ##line 940 GJavaParser.g
                    AssignmentOperator6(self.getRhsIToken(1))
                ##line 940 GJavaParser.g
                )

         self.__rule_action[440]= Act440

        #
        # Rule 441:  AssignmentOperator ::= > > =
        #
         def Act441(): 
               ##line 941 "GJavaParser.g"
                self.setResult(
                    ##line 941 GJavaParser.g
                    AssignmentOperator7(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 941 GJavaParser.g
                                        AstToken(self.getRhsIToken(1)),
                                        ##line 941 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 941 GJavaParser.g
                                        AstToken(self.getRhsIToken(3)))
                ##line 941 GJavaParser.g
                )

         self.__rule_action[441]= Act441

        #
        # Rule 442:  AssignmentOperator ::= > > > =
        #
         def Act442(): 
               ##line 942 "GJavaParser.g"
                self.setResult(
                    ##line 942 GJavaParser.g
                    AssignmentOperator8(self.getLeftIToken(), self.getRightIToken(),
                                        ##line 942 GJavaParser.g
                                        AstToken(self.getRhsIToken(1)),
                                        ##line 942 GJavaParser.g
                                        AstToken(self.getRhsIToken(2)),
                                        ##line 942 GJavaParser.g
                                        AstToken(self.getRhsIToken(3)),
                                        ##line 942 GJavaParser.g
                                        AstToken(self.getRhsIToken(4)))
                ##line 942 GJavaParser.g
                )

         self.__rule_action[442]= Act442

        #
        # Rule 443:  AssignmentOperator ::= &=
        #
         def Act443(): 
               ##line 943 "GJavaParser.g"
                self.setResult(
                    ##line 943 GJavaParser.g
                    AssignmentOperator9(self.getRhsIToken(1))
                ##line 943 GJavaParser.g
                )

         self.__rule_action[443]= Act443

        #
        # Rule 444:  AssignmentOperator ::= ^=
        #
         def Act444(): 
               ##line 944 "GJavaParser.g"
                self.setResult(
                    ##line 944 GJavaParser.g
                    AssignmentOperator10(self.getRhsIToken(1))
                ##line 944 GJavaParser.g
                )

         self.__rule_action[444]= Act444

        #
        # Rule 445:  AssignmentOperator ::= |=
        #
         def Act445(): 
               ##line 945 "GJavaParser.g"
                self.setResult(
                    ##line 945 GJavaParser.g
                    AssignmentOperator11(self.getRhsIToken(1))
                ##line 945 GJavaParser.g
                )

         self.__rule_action[445]= Act445

        #
        # Rule 446:  Expression ::= AssignmentExpression
        #
        
                 
        #
        # Rule 447:  ConstantExpression ::= Expression
        #
        
                 
        #
        # Rule 448:  Dimsopt ::= $Empty
        #
         def Act448(): 
               ##line 954 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[448]= Act448

        #
        # Rule 449:  Dimsopt ::= Dims
        #
        
                 
        #
        # Rule 450:  Catchesopt ::= $Empty
        #
         def Act450(): 
               ##line 957 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[450]= Act450

        #
        # Rule 451:  Catchesopt ::= Catches
        #
        
                 
        #
        # Rule 452:  identifieropt ::= $Empty
        #
         def Act452(): 
               ##line 960 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[452]= Act452

        #
        # Rule 453:  identifieropt ::= identifier
        #
        
                 
        #
        # Rule 454:  ForUpdateopt ::= $Empty
        #
         def Act454(): 
               ##line 963 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[454]= Act454

        #
        # Rule 455:  ForUpdateopt ::= ForUpdate
        #
        
                 
        #
        # Rule 456:  Expressionopt ::= $Empty
        #
         def Act456(): 
               ##line 966 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[456]= Act456

        #
        # Rule 457:  Expressionopt ::= Expression
        #
        
                 
        #
        # Rule 458:  ForInitopt ::= $Empty
        #
         def Act458(): 
               ##line 969 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[458]= Act458

        #
        # Rule 459:  ForInitopt ::= ForInit
        #
        
                 
        #
        # Rule 460:  SwitchLabelsopt ::= $Empty
        #
         def Act460(): 
               ##line 972 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[460]= Act460

        #
        # Rule 461:  SwitchLabelsopt ::= SwitchLabels
        #
        
                 
        #
        # Rule 462:  SwitchBlockStatementGroupsopt ::= $Empty
        #
         def Act462(): 
               ##line 975 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[462]= Act462

        #
        # Rule 463:  SwitchBlockStatementGroupsopt ::= SwitchBlockStatementGroups
        #
        
                 
        #
        # Rule 464:  VariableModifiersopt ::= $Empty
        #
         def Act464(): 
               ##line 978 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[464]= Act464

        #
        # Rule 465:  VariableModifiersopt ::= VariableModifiers
        #
        
                 
        #
        # Rule 466:  VariableInitializersopt ::= $Empty
        #
         def Act466(): 
               ##line 981 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[466]= Act466

        #
        # Rule 467:  VariableInitializersopt ::= VariableInitializers
        #
        
                 
        #
        # Rule 468:  ElementValuesopt ::= $Empty
        #
         def Act468(): 
               ##line 984 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[468]= Act468

        #
        # Rule 469:  ElementValuesopt ::= ElementValues
        #
        
                 
        #
        # Rule 470:  ElementValuePairsopt ::= $Empty
        #
         def Act470(): 
               ##line 987 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[470]= Act470

        #
        # Rule 471:  ElementValuePairsopt ::= ElementValuePairs
        #
        
                 
        #
        # Rule 472:  DefaultValueopt ::= $Empty
        #
         def Act472(): 
               ##line 990 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[472]= Act472

        #
        # Rule 473:  DefaultValueopt ::= DefaultValue
        #
        
                 
        #
        # Rule 474:  AnnotationTypeElementDeclarationsopt ::= $Empty
        #
         def Act474(): 
               ##line 993 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[474]= Act474

        #
        # Rule 475:  AnnotationTypeElementDeclarationsopt ::= AnnotationTypeElementDeclarations
        #
        
                 
        #
        # Rule 476:  AbstractMethodModifiersopt ::= $Empty
        #
         def Act476(): 
               ##line 996 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[476]= Act476

        #
        # Rule 477:  AbstractMethodModifiersopt ::= AbstractMethodModifiers
        #
        
                 
        #
        # Rule 478:  ConstantModifiersopt ::= $Empty
        #
         def Act478(): 
               ##line 999 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[478]= Act478

        #
        # Rule 479:  ConstantModifiersopt ::= ConstantModifiers
        #
        
                 
        #
        # Rule 480:  InterfaceMemberDeclarationsopt ::= $Empty
        #
         def Act480(): 
               ##line 1002 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[480]= Act480

        #
        # Rule 481:  InterfaceMemberDeclarationsopt ::= InterfaceMemberDeclarations
        #
        
                 
        #
        # Rule 482:  ExtendsInterfacesopt ::= $Empty
        #
         def Act482(): 
               ##line 1005 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[482]= Act482

        #
        # Rule 483:  ExtendsInterfacesopt ::= ExtendsInterfaces
        #
        
                 
        #
        # Rule 484:  InterfaceModifiersopt ::= $Empty
        #
         def Act484(): 
               ##line 1008 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[484]= Act484

        #
        # Rule 485:  InterfaceModifiersopt ::= InterfaceModifiers
        #
        
                 
        #
        # Rule 486:  ClassBodyopt ::= $Empty
        #
         def Act486(): 
               ##line 1011 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[486]= Act486

        #
        # Rule 487:  ClassBodyopt ::= ClassBody
        #
        
                 
        #
        # Rule 488:  Argumentsopt ::= $Empty
        #
         def Act488(): 
               ##line 1014 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[488]= Act488

        #
        # Rule 489:  Argumentsopt ::= Arguments
        #
        
                 
        #
        # Rule 490:  EnumBodyDeclarationsopt ::= $Empty
        #
         def Act490(): 
               ##line 1017 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[490]= Act490

        #
        # Rule 491:  EnumBodyDeclarationsopt ::= EnumBodyDeclarations
        #
        
                 
        #
        # Rule 492:  ,opt ::= $Empty
        #
         def Act492(): 
               ##line 1020 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[492]= Act492

        #
        # Rule 493:  ,opt ::= ,
        #
         def Act493(): 
               ##line 1021 "GJavaParser.g"
                self.setResult(
                    ##line 1021 GJavaParser.g
                    Commaopt(self.getRhsIToken(1))
                ##line 1021 GJavaParser.g
                )

         self.__rule_action[493]= Act493

        #
        # Rule 494:  EnumConstantsopt ::= $Empty
        #
         def Act494(): 
               ##line 1023 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[494]= Act494

        #
        # Rule 495:  EnumConstantsopt ::= EnumConstants
        #
        
                 
        #
        # Rule 496:  ArgumentListopt ::= $Empty
        #
         def Act496(): 
               ##line 1026 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[496]= Act496

        #
        # Rule 497:  ArgumentListopt ::= ArgumentList
        #
        
                 
        #
        # Rule 498:  BlockStatementsopt ::= $Empty
        #
         def Act498(): 
               ##line 1029 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[498]= Act498

        #
        # Rule 499:  BlockStatementsopt ::= BlockStatements
        #
        
                 
        #
        # Rule 500:  ExplicitConstructorInvocationopt ::= $Empty
        #
         def Act500(): 
               ##line 1032 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[500]= Act500

        #
        # Rule 501:  ExplicitConstructorInvocationopt ::= ExplicitConstructorInvocation
        #
        
                 
        #
        # Rule 502:  ConstructorModifiersopt ::= $Empty
        #
         def Act502(): 
               ##line 1035 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[502]= Act502

        #
        # Rule 503:  ConstructorModifiersopt ::= ConstructorModifiers
        #
        
                 
        #
        # Rule 504:  ...opt ::= $Empty
        #
         def Act504(): 
               ##line 1038 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[504]= Act504

        #
        # Rule 505:  ...opt ::= ...
        #
         def Act505(): 
               ##line 1039 "GJavaParser.g"
                self.setResult(
                    ##line 1039 GJavaParser.g
                    Ellipsisopt(self.getRhsIToken(1))
                ##line 1039 GJavaParser.g
                )

         self.__rule_action[505]= Act505

        #
        # Rule 506:  FormalParameterListopt ::= $Empty
        #
         def Act506(): 
               ##line 1041 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[506]= Act506

        #
        # Rule 507:  FormalParameterListopt ::= FormalParameterList
        #
        
                 
        #
        # Rule 508:  Throwsopt ::= $Empty
        #
         def Act508(): 
               ##line 1044 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[508]= Act508

        #
        # Rule 509:  Throwsopt ::= Throws
        #
        
                 
        #
        # Rule 510:  MethodModifiersopt ::= $Empty
        #
         def Act510(): 
               ##line 1047 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[510]= Act510

        #
        # Rule 511:  MethodModifiersopt ::= MethodModifiers
        #
        
                 
        #
        # Rule 512:  FieldModifiersopt ::= $Empty
        #
         def Act512(): 
               ##line 1050 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[512]= Act512

        #
        # Rule 513:  FieldModifiersopt ::= FieldModifiers
        #
        
                 
        #
        # Rule 514:  ClassBodyDeclarationsopt ::= $Empty
        #
         def Act514(): 
               ##line 1053 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[514]= Act514

        #
        # Rule 515:  ClassBodyDeclarationsopt ::= ClassBodyDeclarations
        #
        
                 
        #
        # Rule 516:  Interfacesopt ::= $Empty
        #
         def Act516(): 
               ##line 1056 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[516]= Act516

        #
        # Rule 517:  Interfacesopt ::= Interfaces
        #
        
                 
        #
        # Rule 518:  Superopt ::= $Empty
        #
         def Act518(): 
               ##line 1059 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[518]= Act518

        #
        # Rule 519:  Superopt ::= Super
        #
        
                 
        #
        # Rule 520:  TypeParametersopt ::= $Empty
        #
         def Act520(): 
               ##line 1062 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[520]= Act520

        #
        # Rule 521:  TypeParametersopt ::= TypeParameters
        #
        
                 
        #
        # Rule 522:  ClassModifiersopt ::= $Empty
        #
         def Act522(): 
               ##line 1065 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[522]= Act522

        #
        # Rule 523:  ClassModifiersopt ::= ClassModifiers
        #
        
                 
        #
        # Rule 524:  Annotationsopt ::= $Empty
        #
         def Act524(): 
               ##line 1068 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[524]= Act524

        #
        # Rule 525:  Annotationsopt ::= Annotations
        #
        
                 
        #
        # Rule 526:  TypeDeclarationsopt ::= $Empty
        #
         def Act526(): 
               ##line 1071 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[526]= Act526

        #
        # Rule 527:  TypeDeclarationsopt ::= TypeDeclarations
        #
        
                 
        #
        # Rule 528:  ImportDeclarationsopt ::= $Empty
        #
         def Act528(): 
               ##line 1074 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[528]= Act528

        #
        # Rule 529:  ImportDeclarationsopt ::= ImportDeclarations
        #
        
                 
        #
        # Rule 530:  PackageDeclarationopt ::= $Empty
        #
         def Act530(): 
               ##line 1077 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[530]= Act530

        #
        # Rule 531:  PackageDeclarationopt ::= PackageDeclaration
        #
        
                 
        #
        # Rule 532:  WildcardBoundsOpt ::= $Empty
        #
         def Act532(): 
               ##line 1080 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[532]= Act532

        #
        # Rule 533:  WildcardBoundsOpt ::= WildcardBounds
        #
        
                 
        #
        # Rule 534:  AdditionalBoundListopt ::= $Empty
        #
         def Act534(): 
               ##line 1083 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[534]= Act534

        #
        # Rule 535:  AdditionalBoundListopt ::= AdditionalBoundList
        #
        
                 
        #
        # Rule 536:  TypeBoundopt ::= $Empty
        #
         def Act536(): 
               ##line 1086 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[536]= Act536

        #
        # Rule 537:  TypeBoundopt ::= TypeBound
        #
        
                 
        #
        # Rule 538:  TypeArgumentsopt ::= $Empty
        #
         def Act538(): 
               ##line 1089 "GJavaParser.g"
                self.setResult(None)

         self.__rule_action[538]= Act538

        #
        # Rule 539:  TypeArgumentsopt ::= TypeArguments
        #
        
                 
    ##line 287 "btParserTemplateF.gi

    

class IRootForJavaParser(object):
    
        __slots__ = ()
        def  getLeftIToken(self)  : raise TypeError('Can not instantiate abstract class  with abstract methods')
        def  getRightIToken(self)  : raise TypeError('Can not instantiate abstract class  with abstract methods')

        def  acceptWithVisitor(self, v) : pass
        def  acceptWithArg(self, v, o) : pass
        def  acceptWithResult(self, v):pass 
        def  acceptWithResultArgument(self, v, o) : pass
    

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>PrimitiveType
 *<li>ClassType
 *<li>ArrayType
 *<li>TypeDeclaration
 *<li>NormalClassDeclaration
 *<li>ClassMemberDeclaration
 *<li>FieldDeclaration
 *<li>MethodDeclaration
 *<li>ResultType
 *<li>VariableModifier
 *<li>MethodBody
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>InterfaceMemberDeclaration
 *<li>ConstantDeclaration
 *<li>AbstractMethodDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>Block
 *<li>BlockStatements
 *<li>LocalVariableDeclarationStatement
 *<li>IfThenStatement
 *<li>IfThenElseStatement
 *<li>EmptyStatement
 *<li>LabeledStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatement
 *<li>DoStatement
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>Commaopt
 *<li>Ellipsisopt
 *<li>LPGUserAction0
 *<li>LPGUserAction1
 *<li>LPGUserAction2
 *<li>LPGUserAction3
 *<li>LPGUserAction4
 *<li>IntegralType0
 *<li>IntegralType1
 *<li>IntegralType2
 *<li>IntegralType3
 *<li>IntegralType4
 *<li>FloatingPointType0
 *<li>FloatingPointType1
 *<li>ClassModifier0
 *<li>ClassModifier1
 *<li>ClassModifier2
 *<li>ClassModifier3
 *<li>ClassModifier4
 *<li>ClassModifier5
 *<li>ClassModifier6
 *<li>FieldModifier0
 *<li>FieldModifier1
 *<li>FieldModifier2
 *<li>FieldModifier3
 *<li>FieldModifier4
 *<li>FieldModifier5
 *<li>FieldModifier6
 *<li>MethodModifier0
 *<li>MethodModifier1
 *<li>MethodModifier2
 *<li>MethodModifier3
 *<li>MethodModifier4
 *<li>MethodModifier5
 *<li>MethodModifier6
 *<li>MethodModifier7
 *<li>MethodModifier8
 *<li>ConstructorModifier0
 *<li>ConstructorModifier1
 *<li>ConstructorModifier2
 *<li>InterfaceModifier0
 *<li>InterfaceModifier1
 *<li>InterfaceModifier2
 *<li>InterfaceModifier3
 *<li>InterfaceModifier4
 *<li>InterfaceModifier5
 *<li>ConstantModifier0
 *<li>ConstantModifier1
 *<li>ConstantModifier2
 *<li>AbstractMethodModifier0
 *<li>AbstractMethodModifier1
 *<li>AnnotationTypeElementDeclaration0
 *<li>AnnotationTypeElementDeclaration1
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>AssignmentOperator0
 *<li>AssignmentOperator1
 *<li>AssignmentOperator2
 *<li>AssignmentOperator3
 *<li>AssignmentOperator4
 *<li>AssignmentOperator5
 *<li>AssignmentOperator6
 *<li>AssignmentOperator7
 *<li>AssignmentOperator8
 *<li>AssignmentOperator9
 *<li>AssignmentOperator10
 *<li>AssignmentOperator11
 *</ul>
 *</b>
 */'''
class IAstToken(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>CompilationUnit</b>
 */'''
class ICompilationUnit(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>ClassBodyDeclarations
 *<li>ClassMemberDeclaration
 *<li>FieldDeclaration
 *<li>MethodDeclaration
 *<li>StaticInitializer
 *<li>ConstructorDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>Block
 *</ul>
 *</b>
 */'''
class IClassBodyDeclarationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeArguments</b>
 */'''
class ITypeArgumentsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>TypeName
 *</ul>
 *</b>
 */'''
class IClassName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeBound</b>
 */'''
class ITypeBoundopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AdditionalBoundList
 *<li>AdditionalBound
 *</ul>
 *</b>
 */'''
class IAdditionalBoundListopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ClassType
 *<li>ArrayType
 *<li>ActualTypeArgumentList
 *<li>Wildcard
 *</ul>
 *</b>
 */'''
class IActualTypeArgumentList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>WildcardBounds0
 *<li>WildcardBounds1
 *</ul>
 *</b>
 */'''
class IWildcardBoundsOpt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>PackageName
 *</ul>
 *</b>
 */'''
class IPackageName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>AmbiguousName
 *</ul>
 *</b>
 */'''
class IAmbiguousName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>MethodName
 *</ul>
 *</b>
 */'''
class IMethodName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>PackageOrTypeName
 *</ul>
 *</b>
 */'''
class IPackageOrTypeName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>PackageDeclaration</b>
 */'''
class IPackageDeclarationopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ImportDeclarations
 *<li>SingleTypeImportDeclaration
 *<li>TypeImportOnDemandDeclaration
 *<li>SingleStaticImportDeclaration
 *<li>StaticImportOnDemandDeclaration
 *</ul>
 *</b>
 */'''
class IImportDeclarationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>TypeDeclarations
 *<li>TypeDeclaration
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class ITypeDeclarationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *</ul>
 *</b>
 */'''
class IAnnotationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ClassModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ClassModifier0
 *<li>ClassModifier1
 *<li>ClassModifier2
 *<li>ClassModifier3
 *<li>ClassModifier4
 *<li>ClassModifier5
 *<li>ClassModifier6
 *</ul>
 *</b>
 */'''
class IClassModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeParameters</b>
 */'''
class ITypeParametersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Super</b>
 */'''
class ISuperopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Interfaces</b>
 */'''
class IInterfacesopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>TypeParameter
 *<li>TypeParameterList
 *</ul>
 *</b>
 */'''
class ITypeParameterList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>InterfaceType
 *<li>InterfaceTypeList
 *</ul>
 *</b>
 */'''
class IInterfaceTypeList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>FieldModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>FieldModifier0
 *<li>FieldModifier1
 *<li>FieldModifier2
 *<li>FieldModifier3
 *<li>FieldModifier4
 *<li>FieldModifier5
 *<li>FieldModifier6
 *</ul>
 *</b>
 */'''
class IFieldModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>VariableDeclarators
 *<li>VariableDeclarator
 *<li>VariableDeclaratorId
 *</ul>
 *</b>
 */'''
class IVariableDeclarators(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>MethodHeader</b>
 */'''
class IMethodHeader(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>MethodModifiers
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>MethodModifier0
 *<li>MethodModifier1
 *<li>MethodModifier2
 *<li>MethodModifier3
 *<li>MethodModifier4
 *<li>MethodModifier5
 *<li>MethodModifier6
 *<li>MethodModifier7
 *<li>MethodModifier8
 *</ul>
 *</b>
 */'''
class IMethodModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>MethodDeclarator0
 *<li>MethodDeclarator1
 *</ul>
 *</b>
 */'''
class IMethodDeclarator(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Throws</b>
 */'''
class IThrowsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>FormalParameterList
 *<li>LastFormalParameter
 *</ul>
 *</b>
 */'''
class IFormalParameterListopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>FormalParameters
 *<li>FormalParameter
 *</ul>
 *</b>
 */'''
class IFormalParameters(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>VariableModifiers
 *<li>VariableModifier
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *</ul>
 *</b>
 */'''
class IVariableModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ClassType
 *<li>ExceptionTypeList
 *</ul>
 *</b>
 */'''
class IExceptionTypeList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ConstructorModifiers
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ConstructorModifier0
 *<li>ConstructorModifier1
 *<li>ConstructorModifier2
 *</ul>
 *</b>
 */'''
class IConstructorModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ConstructorDeclarator</b>
 */'''
class IConstructorDeclarator(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ConstructorBody</b>
 */'''
class IConstructorBody(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>identifier</b>
 */'''
class ISimpleTypeName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ExplicitConstructorInvocation0
 *<li>ExplicitConstructorInvocation1
 *<li>ExplicitConstructorInvocation2
 *</ul>
 *</b>
 */'''
class IExplicitConstructorInvocationopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>ArgumentList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IArgumentListopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>EnumBody</b>
 */'''
class IEnumBody(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>EnumConstants
 *<li>EnumConstant
 *</ul>
 *</b>
 */'''
class IEnumConstantsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>EnumBodyDeclarations</b>
 */'''
class IEnumBodyDeclarationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Arguments</b>
 */'''
class IArgumentsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ClassBody</b>
 */'''
class IClassBodyopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>InterfaceModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>InterfaceModifier0
 *<li>InterfaceModifier1
 *<li>InterfaceModifier2
 *<li>InterfaceModifier3
 *<li>InterfaceModifier4
 *<li>InterfaceModifier5
 *</ul>
 *</b>
 */'''
class IInterfaceModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ExtendsInterfaces0
 *<li>ExtendsInterfaces1
 *</ul>
 *</b>
 */'''
class IExtendsInterfacesopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>InterfaceBody</b>
 */'''
class IInterfaceBody(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>InterfaceMemberDeclarations
 *<li>InterfaceMemberDeclaration
 *<li>ConstantDeclaration
 *<li>AbstractMethodDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class IInterfaceMemberDeclarationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ConstantModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ConstantModifier0
 *<li>ConstantModifier1
 *<li>ConstantModifier2
 *</ul>
 *</b>
 */'''
class IConstantModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AbstractMethodModifiers
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>AbstractMethodModifier0
 *<li>AbstractMethodModifier1
 *</ul>
 *</b>
 */'''
class IAbstractMethodModifiersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>AnnotationTypeBody</b>
 */'''
class IAnnotationTypeBody(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>ConstantDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>AnnotationTypeElementDeclarations
 *<li>AnnotationTypeElementDeclaration0
 *<li>AnnotationTypeElementDeclaration1
 *</ul>
 *</b>
 */'''
class IAnnotationTypeElementDeclarationsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>DefaultValue</b>
 */'''
class IDefaultValueopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ElementValuePairs
 *<li>ElementValuePair
 *</ul>
 *</b>
 */'''
class IElementValuePairsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>identifier</b>
 */'''
class ISimpleName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>NormalAnnotation
 *<li>ElementValueArrayInitializer
 *<li>ElementValues
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IElementValuesopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>ArrayInitializer
 *<li>VariableInitializers
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IVariableInitializersopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Block
 *<li>IfThenElseStatementNoShortIf
 *<li>EmptyStatement
 *<li>LabeledStatementNoShortIf
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatementNoShortIf
 *<li>DoStatement
 *<li>ForStatementNoShortIf
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class IStatementNoShortIf(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SwitchBlock</b>
 */'''
class ISwitchBlock(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>SwitchBlockStatementGroups
 *<li>SwitchBlockStatementGroup
 *</ul>
 *</b>
 */'''
class ISwitchBlockStatementGroupsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>SwitchLabels
 *<li>SwitchLabel0
 *<li>SwitchLabel1
 *<li>SwitchLabel2
 *</ul>
 *</b>
 */'''
class ISwitchLabelsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IConstantExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>LocalVariableDeclaration
 *<li>StatementExpressionList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>Assignment
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IForInitopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IExpressionopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>StatementExpressionList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>Assignment
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IForUpdateopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>identifier</b>
 */'''
class Iidentifieropt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Catches
 *<li>CatchClause
 *</ul>
 *</b>
 */'''
class ICatchesopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Finally</b>
 */'''
class IFinally(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>DimExprs
 *<li>DimExpr
 *</ul>
 *</b>
 */'''
class IDimExprs(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Dims0
 *<li>Dims1
 *</ul>
 *</b>
 */'''
class IDimsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *</ul>
 *</b>
 */'''
class ILeftHandSide(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>Commaopt</b>
 */'''
class ICommaopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>Ellipsisopt</b>
 */'''
class IEllipsisopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>Block
 *<li>BlockStatements
 *<li>LocalVariableDeclarationStatement
 *<li>IfThenStatement
 *<li>IfThenElseStatement
 *<li>EmptyStatement
 *<li>LabeledStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatement
 *<li>DoStatement
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>LPGUserAction0
 *<li>LPGUserAction1
 *<li>LPGUserAction2
 *<li>LPGUserAction3
 *<li>LPGUserAction4
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class ILPGUserAction(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>identifier</b>
 */'''
class Iidentifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>Block
 *<li>BlockStatements
 *<li>LocalVariableDeclarationStatement
 *<li>IfThenStatement
 *<li>IfThenElseStatement
 *<li>EmptyStatement
 *<li>LabeledStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatement
 *<li>DoStatement
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class IBlockStatementsopt(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>PrimitiveType
 *<li>ClassType
 *<li>ArrayType
 *<li>IntegralType0
 *<li>IntegralType1
 *<li>IntegralType2
 *<li>IntegralType3
 *<li>IntegralType4
 *<li>FloatingPointType0
 *<li>FloatingPointType1
 *</ul>
 *</b>
 */'''
class IType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>PrimitiveType
 *<li>IntegralType0
 *<li>IntegralType1
 *<li>IntegralType2
 *<li>IntegralType3
 *<li>IntegralType4
 *<li>FloatingPointType0
 *<li>FloatingPointType1
 *</ul>
 *</b>
 */'''
class IPrimitiveType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ClassType
 *<li>ArrayType
 *</ul>
 *</b>
 */'''
class IReferenceType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>IntegralType0
 *<li>IntegralType1
 *<li>IntegralType2
 *<li>IntegralType3
 *<li>IntegralType4
 *<li>FloatingPointType0
 *<li>FloatingPointType1
 *</ul>
 *</b>
 */'''
class INumericType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>IntegralType0
 *<li>IntegralType1
 *<li>IntegralType2
 *<li>IntegralType3
 *<li>IntegralType4
 *</ul>
 *</b>
 */'''
class IIntegralType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>FloatingPointType0
 *<li>FloatingPointType1
 *</ul>
 *</b>
 */'''
class IFloatingPointType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ClassType</b>
 */'''
class IClassOrInterfaceType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>identifier</b>
 */'''
class ITypeVariable(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ArrayType</b>
 */'''
class IArrayType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ClassType</b>
 */'''
class IClassType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>TypeName
 *</ul>
 *</b>
 */'''
class ITypeName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>InterfaceType</b>
 */'''
class IInterfaceType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeParameter</b>
 */'''
class ITypeParameter(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeBound</b>
 */'''
class ITypeBound(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AdditionalBoundList
 *<li>AdditionalBound
 *</ul>
 *</b>
 */'''
class IAdditionalBoundList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>AdditionalBound</b>
 */'''
class IAdditionalBound(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeArguments</b>
 */'''
class ITypeArguments(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ClassType
 *<li>ArrayType
 *<li>Wildcard
 *</ul>
 *</b>
 */'''
class IActualTypeArgument(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Wildcard</b>
 */'''
class IWildcard(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>WildcardBounds0
 *<li>WildcardBounds1
 *</ul>
 *</b>
 */'''
class IWildcardBounds(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *</ul>
 *</b>
 */'''
class IExpressionName(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ImportDeclarations
 *<li>SingleTypeImportDeclaration
 *<li>TypeImportOnDemandDeclaration
 *<li>SingleStaticImportDeclaration
 *<li>StaticImportOnDemandDeclaration
 *</ul>
 *</b>
 */'''
class IImportDeclarations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>SingleTypeImportDeclaration
 *<li>TypeImportOnDemandDeclaration
 *<li>SingleStaticImportDeclaration
 *<li>StaticImportOnDemandDeclaration
 *</ul>
 *</b>
 */'''
class IImportDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>TypeDeclarations
 *<li>TypeDeclaration
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class ITypeDeclarations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>TypeDeclaration
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class ITypeDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>PackageDeclaration</b>
 */'''
class IPackageDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SingleTypeImportDeclaration</b>
 */'''
class ISingleTypeImportDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeImportOnDemandDeclaration</b>
 */'''
class ITypeImportOnDemandDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SingleStaticImportDeclaration</b>
 */'''
class ISingleStaticImportDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>StaticImportOnDemandDeclaration</b>
 */'''
class IStaticImportOnDemandDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *</ul>
 *</b>
 */'''
class IClassDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class IInterfaceDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>NormalClassDeclaration</b>
 */'''
class INormalClassDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>EnumDeclaration</b>
 */'''
class IEnumDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ClassBody</b>
 */'''
class IClassBody(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ClassModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ClassModifier0
 *<li>ClassModifier1
 *<li>ClassModifier2
 *<li>ClassModifier3
 *<li>ClassModifier4
 *<li>ClassModifier5
 *<li>ClassModifier6
 *</ul>
 *</b>
 */'''
class IClassModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ClassModifier0
 *<li>ClassModifier1
 *<li>ClassModifier2
 *<li>ClassModifier3
 *<li>ClassModifier4
 *<li>ClassModifier5
 *<li>ClassModifier6
 *</ul>
 *</b>
 */'''
class IClassModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *</ul>
 *</b>
 */'''
class IAnnotation(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>TypeParameters</b>
 */'''
class ITypeParameters(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Super</b>
 */'''
class ISuper(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Interfaces</b>
 */'''
class IInterfaces(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>ClassBodyDeclarations
 *<li>ClassMemberDeclaration
 *<li>FieldDeclaration
 *<li>MethodDeclaration
 *<li>StaticInitializer
 *<li>ConstructorDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>Block
 *</ul>
 *</b>
 */'''
class IClassBodyDeclarations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>ClassMemberDeclaration
 *<li>FieldDeclaration
 *<li>MethodDeclaration
 *<li>StaticInitializer
 *<li>ConstructorDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>Block
 *</ul>
 *</b>
 */'''
class IClassBodyDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>ClassMemberDeclaration
 *<li>FieldDeclaration
 *<li>MethodDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class IClassMemberDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Block</b>
 */'''
class IInstanceInitializer(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>StaticInitializer</b>
 */'''
class IStaticInitializer(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ConstructorDeclaration</b>
 */'''
class IConstructorDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>FieldDeclaration</b>
 */'''
class IFieldDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>MethodDeclaration</b>
 */'''
class IMethodDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>VariableDeclarator
 *<li>VariableDeclaratorId
 *</ul>
 *</b>
 */'''
class IVariableDeclarator(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>VariableDeclaratorId
 *</ul>
 *</b>
 */'''
class IVariableDeclaratorId(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>ArrayInitializer
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IVariableInitializer(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ArrayInitializer</b>
 */'''
class IArrayInitializer(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>FieldModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>FieldModifier0
 *<li>FieldModifier1
 *<li>FieldModifier2
 *<li>FieldModifier3
 *<li>FieldModifier4
 *<li>FieldModifier5
 *<li>FieldModifier6
 *</ul>
 *</b>
 */'''
class IFieldModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>FieldModifier0
 *<li>FieldModifier1
 *<li>FieldModifier2
 *<li>FieldModifier3
 *<li>FieldModifier4
 *<li>FieldModifier5
 *<li>FieldModifier6
 *</ul>
 *</b>
 */'''
class IFieldModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>MethodBody
 *<li>Block
 *</ul>
 *</b>
 */'''
class IMethodBody(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>PrimitiveType
 *<li>ClassType
 *<li>ArrayType
 *<li>ResultType
 *<li>IntegralType0
 *<li>IntegralType1
 *<li>IntegralType2
 *<li>IntegralType3
 *<li>IntegralType4
 *<li>FloatingPointType0
 *<li>FloatingPointType1
 *</ul>
 *</b>
 */'''
class IResultType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>FormalParameterList
 *<li>LastFormalParameter
 *</ul>
 *</b>
 */'''
class IFormalParameterList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LastFormalParameter</b>
 */'''
class ILastFormalParameter(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>FormalParameter</b>
 */'''
class IFormalParameter(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>VariableModifiers
 *<li>VariableModifier
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *</ul>
 *</b>
 */'''
class IVariableModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>VariableModifier
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *</ul>
 *</b>
 */'''
class IVariableModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *</ul>
 *</b>
 */'''
class IAnnotations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>MethodModifiers
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>MethodModifier0
 *<li>MethodModifier1
 *<li>MethodModifier2
 *<li>MethodModifier3
 *<li>MethodModifier4
 *<li>MethodModifier5
 *<li>MethodModifier6
 *<li>MethodModifier7
 *<li>MethodModifier8
 *</ul>
 *</b>
 */'''
class IMethodModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>MethodModifier0
 *<li>MethodModifier1
 *<li>MethodModifier2
 *<li>MethodModifier3
 *<li>MethodModifier4
 *<li>MethodModifier5
 *<li>MethodModifier6
 *<li>MethodModifier7
 *<li>MethodModifier8
 *</ul>
 *</b>
 */'''
class IMethodModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Throws</b>
 */'''
class IThrows(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ClassType
 *</ul>
 *</b>
 */'''
class IExceptionType(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Block</b>
 */'''
class IBlock(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ConstructorModifiers
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ConstructorModifier0
 *<li>ConstructorModifier1
 *<li>ConstructorModifier2
 *</ul>
 *</b>
 */'''
class IConstructorModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ConstructorModifier0
 *<li>ConstructorModifier1
 *<li>ConstructorModifier2
 *</ul>
 *</b>
 */'''
class IConstructorModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ExplicitConstructorInvocation0
 *<li>ExplicitConstructorInvocation1
 *<li>ExplicitConstructorInvocation2
 *</ul>
 *</b>
 */'''
class IExplicitConstructorInvocation(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *</ul>
 *</b>
 */'''
class IPrimary(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>EnumConstants
 *<li>EnumConstant
 *</ul>
 *</b>
 */'''
class IEnumConstants(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>EnumConstant
 *</ul>
 *</b>
 */'''
class IEnumConstant(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Arguments</b>
 */'''
class IArguments(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>EnumBodyDeclarations</b>
 */'''
class IEnumBodyDeclarations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>NormalInterfaceDeclaration</b>
 */'''
class INormalInterfaceDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>AnnotationTypeDeclaration</b>
 */'''
class IAnnotationTypeDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>InterfaceModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>InterfaceModifier0
 *<li>InterfaceModifier1
 *<li>InterfaceModifier2
 *<li>InterfaceModifier3
 *<li>InterfaceModifier4
 *<li>InterfaceModifier5
 *</ul>
 *</b>
 */'''
class IInterfaceModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>InterfaceModifier0
 *<li>InterfaceModifier1
 *<li>InterfaceModifier2
 *<li>InterfaceModifier3
 *<li>InterfaceModifier4
 *<li>InterfaceModifier5
 *</ul>
 *</b>
 */'''
class IInterfaceModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ExtendsInterfaces0
 *<li>ExtendsInterfaces1
 *</ul>
 *</b>
 */'''
class IExtendsInterfaces(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>InterfaceMemberDeclarations
 *<li>InterfaceMemberDeclaration
 *<li>ConstantDeclaration
 *<li>AbstractMethodDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class IInterfaceMemberDeclarations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>InterfaceMemberDeclaration
 *<li>ConstantDeclaration
 *<li>AbstractMethodDeclaration
 *<li>AnnotationTypeDeclaration
 *</ul>
 *</b>
 */'''
class IInterfaceMemberDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ConstantDeclaration</b>
 */'''
class IConstantDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>AbstractMethodDeclaration</b>
 */'''
class IAbstractMethodDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ConstantModifiers
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ConstantModifier0
 *<li>ConstantModifier1
 *<li>ConstantModifier2
 *</ul>
 *</b>
 */'''
class IConstantModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>ConstantModifier0
 *<li>ConstantModifier1
 *<li>ConstantModifier2
 *</ul>
 *</b>
 */'''
class IConstantModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AbstractMethodModifiers
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>AbstractMethodModifier0
 *<li>AbstractMethodModifier1
 *</ul>
 *</b>
 */'''
class IAbstractMethodModifiers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Annotations
 *<li>NormalAnnotation
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>AbstractMethodModifier0
 *<li>AbstractMethodModifier1
 *</ul>
 *</b>
 */'''
class IAbstractMethodModifier(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>ConstantDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>AnnotationTypeElementDeclarations
 *<li>AnnotationTypeElementDeclaration0
 *<li>AnnotationTypeElementDeclaration1
 *</ul>
 *</b>
 */'''
class IAnnotationTypeElementDeclarations(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>NormalInterfaceDeclaration
 *<li>ConstantDeclaration
 *<li>AnnotationTypeDeclaration
 *<li>AnnotationTypeElementDeclaration0
 *<li>AnnotationTypeElementDeclaration1
 *</ul>
 *</b>
 */'''
class IAnnotationTypeElementDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>DefaultValue</b>
 */'''
class IDefaultValue(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>NormalAnnotation
 *<li>ElementValueArrayInitializer
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IElementValue(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>NormalAnnotation</b>
 */'''
class INormalAnnotation(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>MarkerAnnotation</b>
 */'''
class IMarkerAnnotation(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SingleElementAnnotation</b>
 */'''
class ISingleElementAnnotation(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ElementValuePairs
 *<li>ElementValuePair
 *</ul>
 *</b>
 */'''
class IElementValuePairs(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ElementValuePair</b>
 */'''
class IElementValuePair(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IConditionalExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ElementValueArrayInitializer</b>
 */'''
class IElementValueArrayInitializer(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>NormalAnnotation
 *<li>ElementValueArrayInitializer
 *<li>ElementValues
 *<li>MarkerAnnotation
 *<li>SingleElementAnnotation
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IElementValues(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>ArrayInitializer
 *<li>VariableInitializers
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IVariableInitializers(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>Block
 *<li>BlockStatements
 *<li>LocalVariableDeclarationStatement
 *<li>IfThenStatement
 *<li>IfThenElseStatement
 *<li>EmptyStatement
 *<li>LabeledStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatement
 *<li>DoStatement
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class IBlockStatements(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>NormalClassDeclaration
 *<li>EnumDeclaration
 *<li>Block
 *<li>LocalVariableDeclarationStatement
 *<li>IfThenStatement
 *<li>IfThenElseStatement
 *<li>EmptyStatement
 *<li>LabeledStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatement
 *<li>DoStatement
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class IBlockStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LocalVariableDeclarationStatement</b>
 */'''
class ILocalVariableDeclarationStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Block
 *<li>IfThenStatement
 *<li>IfThenElseStatement
 *<li>EmptyStatement
 *<li>LabeledStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>WhileStatement
 *<li>DoStatement
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class IStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LocalVariableDeclaration</b>
 */'''
class ILocalVariableDeclaration(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Block
 *<li>EmptyStatement
 *<li>ExpressionStatement
 *<li>SwitchStatement
 *<li>DoStatement
 *<li>BreakStatement
 *<li>ContinueStatement
 *<li>ReturnStatement
 *<li>ThrowStatement
 *<li>SynchronizedStatement
 *<li>AssertStatement0
 *<li>AssertStatement1
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class IStatementWithoutTrailingSubstatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LabeledStatement</b>
 */'''
class ILabeledStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>IfThenStatement</b>
 */'''
class IIfThenStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>IfThenElseStatement</b>
 */'''
class IIfThenElseStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>WhileStatement</b>
 */'''
class IWhileStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>BasicForStatement
 *<li>EnhancedForStatement
 *</ul>
 *</b>
 */'''
class IForStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by <b>EmptyStatement</b>
 */'''
class IEmptyStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ExpressionStatement</b>
 */'''
class IExpressionStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AssertStatement0
 *<li>AssertStatement1
 *</ul>
 *</b>
 */'''
class IAssertStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SwitchStatement</b>
 */'''
class ISwitchStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>DoStatement</b>
 */'''
class IDoStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>BreakStatement</b>
 */'''
class IBreakStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ContinueStatement</b>
 */'''
class IContinueStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ReturnStatement</b>
 */'''
class IReturnStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SynchronizedStatement</b>
 */'''
class ISynchronizedStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ThrowStatement</b>
 */'''
class IThrowStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>TryStatement0
 *<li>TryStatement1
 *</ul>
 *</b>
 */'''
class ITryStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>LabeledStatementNoShortIf</b>
 */'''
class ILabeledStatementNoShortIf(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>IfThenElseStatementNoShortIf</b>
 */'''
class IIfThenElseStatementNoShortIf(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>WhileStatementNoShortIf</b>
 */'''
class IWhileStatementNoShortIf(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>ForStatementNoShortIf</b>
 */'''
class IForStatementNoShortIf(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>Assignment
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IStatementExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>Assignment</b>
 */'''
class IAssignment(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>PreIncrementExpression</b>
 */'''
class IPreIncrementExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>PreDecrementExpression</b>
 */'''
class IPreDecrementExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>PostIncrementExpression</b>
 */'''
class IPostIncrementExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>PostDecrementExpression</b>
 */'''
class IPostDecrementExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IMethodInvocation(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *</ul>
 *</b>
 */'''
class IClassInstanceCreationExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>SwitchBlockStatementGroups
 *<li>SwitchBlockStatementGroup
 *</ul>
 *</b>
 */'''
class ISwitchBlockStatementGroups(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>SwitchBlockStatementGroup</b>
 */'''
class ISwitchBlockStatementGroup(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>SwitchLabels
 *<li>SwitchLabel0
 *<li>SwitchLabel1
 *<li>SwitchLabel2
 *</ul>
 *</b>
 */'''
class ISwitchLabels(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>SwitchLabel0
 *<li>SwitchLabel1
 *<li>SwitchLabel2
 *</ul>
 *</b>
 */'''
class ISwitchLabel(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>BasicForStatement</b>
 */'''
class IBasicForStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>EnhancedForStatement</b>
 */'''
class IEnhancedForStatement(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>LocalVariableDeclaration
 *<li>StatementExpressionList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>Assignment
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IForInit(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>StatementExpressionList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>Assignment
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IStatementExpressionList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>StatementExpressionList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>Assignment
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *</ul>
 *</b>
 */'''
class IForUpdate(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Catches
 *<li>CatchClause
 *</ul>
 *</b>
 */'''
class ICatches(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>CatchClause</b>
 */'''
class ICatchClause(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *</ul>
 *</b>
 */'''
class IPrimaryNoNewArray(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *</ul>
 *</b>
 */'''
class IArrayCreationExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *</ul>
 *</b>
 */'''
class ILiteral(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *</ul>
 *</b>
 */'''
class IFieldAccess(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *</ul>
 *</b>
 */'''
class IArrayAccess(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is always implemented by <b>AstToken</b>. It is also implemented by:
 *<b>
 *<ul>
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *</ul>
 *</b>
 */'''
class IBooleanLiteral(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>ArgumentList
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IArgumentList(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>Dims0
 *<li>Dims1
 *</ul>
 *</b>
 */'''
class IDims(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by <b>DimExpr</b>
 */'''
class IDimExpr(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *</ul>
 *</b>
 */'''
class IPostfixExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *</ul>
 *</b>
 */'''
class IUnaryExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *</ul>
 *</b>
 */'''
class IUnaryExpressionNotPlusMinus(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>CastExpression0
 *<li>CastExpression1
 *</ul>
 *</b>
 */'''
class ICastExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *</ul>
 *</b>
 */'''
class IMultiplicativeExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *</ul>
 *</b>
 */'''
class IAdditiveExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *</ul>
 *</b>
 */'''
class IShiftExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *</ul>
 *</b>
 */'''
class IRelationalExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IEqualityExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IAndExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IExclusiveOrExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IInclusiveOrExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IConditionalAndExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IConditionalOrExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>identifier
 *<li>ExpressionName
 *<li>PostIncrementExpression
 *<li>PostDecrementExpression
 *<li>PreIncrementExpression
 *<li>PreDecrementExpression
 *<li>AndExpression
 *<li>ExclusiveOrExpression
 *<li>InclusiveOrExpression
 *<li>ConditionalAndExpression
 *<li>ConditionalOrExpression
 *<li>ConditionalExpression
 *<li>Assignment
 *<li>PrimaryNoNewArray0
 *<li>PrimaryNoNewArray1
 *<li>PrimaryNoNewArray2
 *<li>PrimaryNoNewArray3
 *<li>PrimaryNoNewArray4
 *<li>Literal0
 *<li>Literal1
 *<li>Literal2
 *<li>Literal3
 *<li>Literal4
 *<li>Literal5
 *<li>Literal6
 *<li>BooleanLiteral0
 *<li>BooleanLiteral1
 *<li>ClassInstanceCreationExpression0
 *<li>ClassInstanceCreationExpression1
 *<li>ArrayCreationExpression0
 *<li>ArrayCreationExpression1
 *<li>ArrayCreationExpression2
 *<li>ArrayCreationExpression3
 *<li>FieldAccess0
 *<li>FieldAccess1
 *<li>FieldAccess2
 *<li>MethodInvocation0
 *<li>MethodInvocation1
 *<li>MethodInvocation2
 *<li>MethodInvocation3
 *<li>MethodInvocation4
 *<li>ArrayAccess0
 *<li>ArrayAccess1
 *<li>UnaryExpression0
 *<li>UnaryExpression1
 *<li>UnaryExpressionNotPlusMinus0
 *<li>UnaryExpressionNotPlusMinus1
 *<li>CastExpression0
 *<li>CastExpression1
 *<li>MultiplicativeExpression0
 *<li>MultiplicativeExpression1
 *<li>MultiplicativeExpression2
 *<li>AdditiveExpression0
 *<li>AdditiveExpression1
 *<li>ShiftExpression0
 *<li>ShiftExpression1
 *<li>ShiftExpression2
 *<li>RelationalExpression0
 *<li>RelationalExpression1
 *<li>RelationalExpression2
 *<li>RelationalExpression3
 *<li>RelationalExpression4
 *<li>EqualityExpression0
 *<li>EqualityExpression1
 *</ul>
 *</b>
 */'''
class IAssignmentExpression(IRootForJavaParser):
        __slots__ = ()

'''/**
 * is implemented by:
 *<b>
 *<ul>
 *<li>AssignmentOperator0
 *<li>AssignmentOperator1
 *<li>AssignmentOperator2
 *<li>AssignmentOperator3
 *<li>AssignmentOperator4
 *<li>AssignmentOperator5
 *<li>AssignmentOperator6
 *<li>AssignmentOperator7
 *<li>AssignmentOperator8
 *<li>AssignmentOperator9
 *<li>AssignmentOperator10
 *<li>AssignmentOperator11
 *</ul>
 *</b>
 */'''
class IAssignmentOperator(IRootForJavaParser):
        __slots__ = ()

class Ast(IAst):
    
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

        def  acceptWithVisitor(self, v) : pass
        def  acceptWithArg(self, v, o) : pass
        def  acceptWithResult(self, v):pass 
        def  acceptWithResultArgument(self, v, o) : pass
        def  accept(self, v):  pass
    

class AbstractAstList ( Ast , IAbstractArrayList):
    
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
              super(AbstractAstList, self).__init__(leftToken, rightToken)
              self.left_recursive = left_recursive
              self._content = ArrayList()
        

        '''/**
         * Make a copy of the list and return it. Note that we obtain the local list by
         * invoking getArrayList so as to make sure that the list we return is in proper order.
         */'''
        def  getAllChildren(self):
        
            return self.getArrayList().clone()
        

    

class AstToken ( Ast, IAstToken):
    
        __slots__ = ()
        def __init__(self,token) : super(AstToken,self).__init__(token)
        def  getIToken(self): return self.leftIToken
        def  toString(self):  return self.leftIToken.toString()

        '''/**
         * A token class has no children. So, we return the empty list.
         */'''
        def  getAllChildren(self)  :  return ArrayList()


        def  acceptWithVisitor(self, v):  v.visitAstToken(self)
        def  acceptWithArg(self, v, o):  v.visitAstToken(self, o)
        def  acceptWithResult(self, v):  return v.visitAstToken(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAstToken(self, o)
    

'''/**
 *<b>
*<li>Rule 3:  identifier ::= IDENTIFIER
 *</b>
 */'''
class identifier ( AstToken ,Iidentifier):
    
        def getEnvironment(self): return self.environment

        def  getIDENTIFIER(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,environment , token  ):        
            super(identifier, self).__init__(token)
            self.environment = environment
            self.initialize()
        

        def  acceptWithVisitor(self, v):  v.visitidentifier(self)
        def  acceptWithArg(self, v, o):  v.visitidentifier(self, o)
        def  acceptWithResult(self, v):  return v.visitidentifier(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitidentifier(self, o)
    

'''/**
 *<em>
*<li>Rule 12:  PrimitiveType ::= NumericType
 *</em>
 *<p>
 *<b>
*<li>Rule 13:  PrimitiveType ::= boolean
 *</b>
 */'''
class PrimitiveType ( AstToken ,IPrimitiveType):
    
        def  getboolean(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(PrimitiveType, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitPrimitiveType(self)
        def  acceptWithArg(self, v, o):  v.visitPrimitiveType(self, o)
        def  acceptWithResult(self, v):  return v.visitPrimitiveType(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPrimitiveType(self, o)
    

'''/**
 *<b>
*<li>Rule 27:  ClassType ::= TypeName TypeArgumentsopt
 *</b>
 */'''
class ClassType ( Ast ,IClassType):
    

        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt

        __slots__ = ('_TypeName', '_TypeArgumentsopt')

        def __init__(self, leftIToken, rightIToken,
                             _TypeName,
                             _TypeArgumentsopt):
        
            super(ClassType, self).__init__(leftIToken, rightIToken)

            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeName:  _content.add(self._TypeName)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitClassType(self)
        def  acceptWithArg(self, v, o):  v.visitClassType(self, o)
        def  acceptWithResult(self, v):  return v.visitClassType(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassType(self, o)
    

'''/**
 *<b>
*<li>Rule 28:  InterfaceType ::= TypeName TypeArgumentsopt
 *</b>
 */'''
class InterfaceType ( Ast ,IInterfaceType):
    

        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt

        __slots__ = ('_TypeName', '_TypeArgumentsopt')

        def __init__(self, leftIToken, rightIToken,
                             _TypeName,
                             _TypeArgumentsopt):
        
            super(InterfaceType, self).__init__(leftIToken, rightIToken)

            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeName:  _content.add(self._TypeName)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInterfaceType(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceType(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceType(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceType(self, o)
    

'''/**
 *<em>
*<li>Rule 29:  TypeName ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 30:  TypeName ::= TypeName . identifier
 *</b>
 */'''
class TypeName ( Ast ,ITypeName):
    

        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_TypeName', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _TypeName,
                             _DOT,
                             _identifier):
        
            super(TypeName, self).__init__(leftIToken, rightIToken)

            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeName:  _content.add(self._TypeName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeName(self)
        def  acceptWithArg(self, v, o):  v.visitTypeName(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeName(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeName(self, o)
    

'''/**
 *<b>
*<li>Rule 33:  ArrayType ::= Type [ ]
 *</b>
 */'''
class ArrayType ( Ast ,IArrayType):
    

        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_Type', '_LBRACKET', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _Type,
                             _LBRACKET,
                             _RBRACKET):
        
            super(ArrayType, self).__init__(leftIToken, rightIToken)

            self._Type = _Type
            _Type.setParent(self)
            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Type:  _content.add(self._Type)
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayType(self)
        def  acceptWithArg(self, v, o):  v.visitArrayType(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayType(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayType(self, o)
    

'''/**
 *<b>
*<li>Rule 34:  TypeParameter ::= TypeVariable TypeBoundopt
 *</b>
 */'''
class TypeParameter ( Ast ,ITypeParameter):
    

        def  getTypeVariable(self)  :  return self._TypeVariable
        def  setTypeVariable(self,  _TypeVariable) :   self._TypeVariable = _TypeVariable
        '''/**
         * The value returned by <b>getTypeBoundopt</b> may be <b>null</b>
         */'''
        def  getTypeBoundopt(self)  :  return self._TypeBoundopt
        def  setTypeBoundopt(self,  _TypeBoundopt) :   self._TypeBoundopt = _TypeBoundopt

        __slots__ = ('_TypeVariable', '_TypeBoundopt')

        def __init__(self, leftIToken, rightIToken,
                             _TypeVariable,
                             _TypeBoundopt):
        
            super(TypeParameter, self).__init__(leftIToken, rightIToken)

            self._TypeVariable = _TypeVariable
            _TypeVariable.setParent(self)
            self._TypeBoundopt = _TypeBoundopt
            if _TypeBoundopt: _TypeBoundopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeVariable:  _content.add(self._TypeVariable)
            if self._TypeBoundopt:  _content.add(self._TypeBoundopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeParameter(self)
        def  acceptWithArg(self, v, o):  v.visitTypeParameter(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeParameter(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeParameter(self, o)
    

'''/**
 *<b>
*<li>Rule 35:  TypeBound ::= extends ClassOrInterfaceType AdditionalBoundListopt
 *</b>
 */'''
class TypeBound ( Ast ,ITypeBound):
    

        def  getextends(self)  :  return self._extends
        def  setextends(self,  _extends) :   self._extends = _extends
        def  getClassOrInterfaceType(self)  :  return self._ClassOrInterfaceType
        def  setClassOrInterfaceType(self,  _ClassOrInterfaceType) :   self._ClassOrInterfaceType = _ClassOrInterfaceType
        '''/**
         * The value returned by <b>getAdditionalBoundListopt</b> may be <b>null</b>
         */'''
        def  getAdditionalBoundListopt(self)  :  return self._AdditionalBoundListopt
        def  setAdditionalBoundListopt(self,  _AdditionalBoundListopt) :   self._AdditionalBoundListopt = _AdditionalBoundListopt

        __slots__ = ('_extends', '_ClassOrInterfaceType', '_AdditionalBoundListopt')

        def __init__(self, leftIToken, rightIToken,
                             _extends,
                             _ClassOrInterfaceType,
                             _AdditionalBoundListopt):
        
            super(TypeBound, self).__init__(leftIToken, rightIToken)

            self._extends = _extends
            _extends.setParent(self)
            self._ClassOrInterfaceType = _ClassOrInterfaceType
            _ClassOrInterfaceType.setParent(self)
            self._AdditionalBoundListopt = _AdditionalBoundListopt
            if _AdditionalBoundListopt: _AdditionalBoundListopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._extends:  _content.add(self._extends)
            if self._ClassOrInterfaceType:  _content.add(self._ClassOrInterfaceType)
            if self._AdditionalBoundListopt:  _content.add(self._AdditionalBoundListopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeBound(self)
        def  acceptWithArg(self, v, o):  v.visitTypeBound(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeBound(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeBound(self, o)
    

'''/**
 *<em>
*<li>Rule 36:  AdditionalBoundList ::= AdditionalBound
 *</em>
 *<p>
 *<b>
*<li>Rule 37:  AdditionalBoundList ::= AdditionalBoundList AdditionalBound
 *</b>
 */'''
class AdditionalBoundList ( Ast ,IAdditionalBoundList):
    

        def  getAdditionalBoundList(self)  :  return self._AdditionalBoundList
        def  setAdditionalBoundList(self,  _AdditionalBoundList) :   self._AdditionalBoundList = _AdditionalBoundList
        def  getAdditionalBound(self)  :  return self._AdditionalBound
        def  setAdditionalBound(self,  _AdditionalBound) :   self._AdditionalBound = _AdditionalBound

        __slots__ = ('_AdditionalBoundList', '_AdditionalBound')

        def __init__(self, leftIToken, rightIToken,
                             _AdditionalBoundList,
                             _AdditionalBound):
        
            super(AdditionalBoundList, self).__init__(leftIToken, rightIToken)

            self._AdditionalBoundList = _AdditionalBoundList
            _AdditionalBoundList.setParent(self)
            self._AdditionalBound = _AdditionalBound
            _AdditionalBound.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AdditionalBoundList:  _content.add(self._AdditionalBoundList)
            if self._AdditionalBound:  _content.add(self._AdditionalBound)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAdditionalBoundList(self)
        def  acceptWithArg(self, v, o):  v.visitAdditionalBoundList(self, o)
        def  acceptWithResult(self, v):  return v.visitAdditionalBoundList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAdditionalBoundList(self, o)
    

'''/**
 *<b>
*<li>Rule 38:  AdditionalBound ::= & InterfaceType
 *</b>
 */'''
class AdditionalBound ( Ast ,IAdditionalBound):
    

        def  getAND(self)  :  return self._AND
        def  setAND(self,  _AND) :   self._AND = _AND
        def  getInterfaceType(self)  :  return self._InterfaceType
        def  setInterfaceType(self,  _InterfaceType) :   self._InterfaceType = _InterfaceType

        __slots__ = ('_AND', '_InterfaceType')

        def __init__(self, leftIToken, rightIToken,
                             _AND,
                             _InterfaceType):
        
            super(AdditionalBound, self).__init__(leftIToken, rightIToken)

            self._AND = _AND
            _AND.setParent(self)
            self._InterfaceType = _InterfaceType
            _InterfaceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AND:  _content.add(self._AND)
            if self._InterfaceType:  _content.add(self._InterfaceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAdditionalBound(self)
        def  acceptWithArg(self, v, o):  v.visitAdditionalBound(self, o)
        def  acceptWithResult(self, v):  return v.visitAdditionalBound(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAdditionalBound(self, o)
    

'''/**
 *<b>
*<li>Rule 39:  TypeArguments ::= < ActualTypeArgumentList >
 *</b>
 */'''
class TypeArguments ( Ast ,ITypeArguments):
    

        def  getLESS(self)  :  return self._LESS
        def  setLESS(self,  _LESS) :   self._LESS = _LESS
        def  getActualTypeArgumentList(self)  :  return self._ActualTypeArgumentList
        def  setActualTypeArgumentList(self,  _ActualTypeArgumentList) :   self._ActualTypeArgumentList = _ActualTypeArgumentList
        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER

        __slots__ = ('_LESS', '_ActualTypeArgumentList', '_GREATER')

        def __init__(self, leftIToken, rightIToken,
                             _LESS,
                             _ActualTypeArgumentList,
                             _GREATER):
        
            super(TypeArguments, self).__init__(leftIToken, rightIToken)

            self._LESS = _LESS
            _LESS.setParent(self)
            self._ActualTypeArgumentList = _ActualTypeArgumentList
            _ActualTypeArgumentList.setParent(self)
            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LESS:  _content.add(self._LESS)
            if self._ActualTypeArgumentList:  _content.add(self._ActualTypeArgumentList)
            if self._GREATER:  _content.add(self._GREATER)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeArguments(self)
        def  acceptWithArg(self, v, o):  v.visitTypeArguments(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeArguments(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeArguments(self, o)
    

'''/**
 *<em>
*<li>Rule 40:  ActualTypeArgumentList ::= ActualTypeArgument
 *</em>
 *<p>
 *<b>
*<li>Rule 41:  ActualTypeArgumentList ::= ActualTypeArgumentList , ActualTypeArgument
 *</b>
 */'''
class ActualTypeArgumentList ( Ast ,IActualTypeArgumentList):
    

        def  getActualTypeArgumentList(self)  :  return self._ActualTypeArgumentList
        def  setActualTypeArgumentList(self,  _ActualTypeArgumentList) :   self._ActualTypeArgumentList = _ActualTypeArgumentList
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getActualTypeArgument(self)  :  return self._ActualTypeArgument
        def  setActualTypeArgument(self,  _ActualTypeArgument) :   self._ActualTypeArgument = _ActualTypeArgument

        __slots__ = ('_ActualTypeArgumentList', '_COMMA', '_ActualTypeArgument')

        def __init__(self, leftIToken, rightIToken,
                             _ActualTypeArgumentList,
                             _COMMA,
                             _ActualTypeArgument):
        
            super(ActualTypeArgumentList, self).__init__(leftIToken, rightIToken)

            self._ActualTypeArgumentList = _ActualTypeArgumentList
            _ActualTypeArgumentList.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._ActualTypeArgument = _ActualTypeArgument
            _ActualTypeArgument.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ActualTypeArgumentList:  _content.add(self._ActualTypeArgumentList)
            if self._COMMA:  _content.add(self._COMMA)
            if self._ActualTypeArgument:  _content.add(self._ActualTypeArgument)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitActualTypeArgumentList(self)
        def  acceptWithArg(self, v, o):  v.visitActualTypeArgumentList(self, o)
        def  acceptWithResult(self, v):  return v.visitActualTypeArgumentList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitActualTypeArgumentList(self, o)
    

'''/**
 *<b>
*<li>Rule 44:  Wildcard ::= ? WildcardBoundsOpt
 *</b>
 */'''
class Wildcard ( Ast ,IWildcard):
    

        def  getQUESTION(self)  :  return self._QUESTION
        def  setQUESTION(self,  _QUESTION) :   self._QUESTION = _QUESTION
        '''/**
         * The value returned by <b>getWildcardBoundsOpt</b> may be <b>null</b>
         */'''
        def  getWildcardBoundsOpt(self)  :  return self._WildcardBoundsOpt
        def  setWildcardBoundsOpt(self,  _WildcardBoundsOpt) :   self._WildcardBoundsOpt = _WildcardBoundsOpt

        __slots__ = ('_QUESTION', '_WildcardBoundsOpt')

        def __init__(self, leftIToken, rightIToken,
                             _QUESTION,
                             _WildcardBoundsOpt):
        
            super(Wildcard, self).__init__(leftIToken, rightIToken)

            self._QUESTION = _QUESTION
            _QUESTION.setParent(self)
            self._WildcardBoundsOpt = _WildcardBoundsOpt
            if _WildcardBoundsOpt: _WildcardBoundsOpt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._QUESTION:  _content.add(self._QUESTION)
            if self._WildcardBoundsOpt:  _content.add(self._WildcardBoundsOpt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitWildcard(self)
        def  acceptWithArg(self, v, o):  v.visitWildcard(self, o)
        def  acceptWithResult(self, v):  return v.visitWildcard(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitWildcard(self, o)
    

'''/**
 *<em>
*<li>Rule 47:  PackageName ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 48:  PackageName ::= PackageName . identifier
 *</b>
 */'''
class PackageName ( Ast ,IPackageName):
    

        def  getPackageName(self)  :  return self._PackageName
        def  setPackageName(self,  _PackageName) :   self._PackageName = _PackageName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_PackageName', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _PackageName,
                             _DOT,
                             _identifier):
        
            super(PackageName, self).__init__(leftIToken, rightIToken)

            self._PackageName = _PackageName
            _PackageName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PackageName:  _content.add(self._PackageName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPackageName(self)
        def  acceptWithArg(self, v, o):  v.visitPackageName(self, o)
        def  acceptWithResult(self, v):  return v.visitPackageName(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPackageName(self, o)
    

'''/**
 *<em>
*<li>Rule 49:  ExpressionName ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 50:  ExpressionName ::= AmbiguousName . identifier
 *</b>
 */'''
class ExpressionName ( Ast ,IExpressionName):
    

        def  getAmbiguousName(self)  :  return self._AmbiguousName
        def  setAmbiguousName(self,  _AmbiguousName) :   self._AmbiguousName = _AmbiguousName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_AmbiguousName', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _AmbiguousName,
                             _DOT,
                             _identifier):
        
            super(ExpressionName, self).__init__(leftIToken, rightIToken)

            self._AmbiguousName = _AmbiguousName
            _AmbiguousName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AmbiguousName:  _content.add(self._AmbiguousName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExpressionName(self)
        def  acceptWithArg(self, v, o):  v.visitExpressionName(self, o)
        def  acceptWithResult(self, v):  return v.visitExpressionName(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExpressionName(self, o)
    

'''/**
 *<em>
*<li>Rule 51:  MethodName ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 52:  MethodName ::= AmbiguousName . identifier
 *</b>
 */'''
class MethodName ( Ast ,IMethodName):
    

        def  getAmbiguousName(self)  :  return self._AmbiguousName
        def  setAmbiguousName(self,  _AmbiguousName) :   self._AmbiguousName = _AmbiguousName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_AmbiguousName', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _AmbiguousName,
                             _DOT,
                             _identifier):
        
            super(MethodName, self).__init__(leftIToken, rightIToken)

            self._AmbiguousName = _AmbiguousName
            _AmbiguousName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AmbiguousName:  _content.add(self._AmbiguousName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodName(self)
        def  acceptWithArg(self, v, o):  v.visitMethodName(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodName(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodName(self, o)
    

'''/**
 *<em>
*<li>Rule 53:  PackageOrTypeName ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 54:  PackageOrTypeName ::= PackageOrTypeName . identifier
 *</b>
 */'''
class PackageOrTypeName ( Ast ,IPackageOrTypeName):
    

        def  getPackageOrTypeName(self)  :  return self._PackageOrTypeName
        def  setPackageOrTypeName(self,  _PackageOrTypeName) :   self._PackageOrTypeName = _PackageOrTypeName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_PackageOrTypeName', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _PackageOrTypeName,
                             _DOT,
                             _identifier):
        
            super(PackageOrTypeName, self).__init__(leftIToken, rightIToken)

            self._PackageOrTypeName = _PackageOrTypeName
            _PackageOrTypeName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PackageOrTypeName:  _content.add(self._PackageOrTypeName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPackageOrTypeName(self)
        def  acceptWithArg(self, v, o):  v.visitPackageOrTypeName(self, o)
        def  acceptWithResult(self, v):  return v.visitPackageOrTypeName(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPackageOrTypeName(self, o)
    

'''/**
 *<em>
*<li>Rule 55:  AmbiguousName ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 56:  AmbiguousName ::= AmbiguousName . identifier
 *</b>
 */'''
class AmbiguousName ( Ast ,IAmbiguousName):
    

        def  getAmbiguousName(self)  :  return self._AmbiguousName
        def  setAmbiguousName(self,  _AmbiguousName) :   self._AmbiguousName = _AmbiguousName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_AmbiguousName', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _AmbiguousName,
                             _DOT,
                             _identifier):
        
            super(AmbiguousName, self).__init__(leftIToken, rightIToken)

            self._AmbiguousName = _AmbiguousName
            _AmbiguousName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AmbiguousName:  _content.add(self._AmbiguousName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAmbiguousName(self)
        def  acceptWithArg(self, v, o):  v.visitAmbiguousName(self, o)
        def  acceptWithResult(self, v):  return v.visitAmbiguousName(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAmbiguousName(self, o)
    

'''/**
 *<b>
*<li>Rule 57:  CompilationUnit ::= PackageDeclarationopt ImportDeclarationsopt TypeDeclarationsopt
 *</b>
 */'''
class CompilationUnit ( Ast ,ICompilationUnit):
    

        '''/**
         * The value returned by <b>getPackageDeclarationopt</b> may be <b>null</b>
         */'''
        def  getPackageDeclarationopt(self)  :  return self._PackageDeclarationopt
        def  setPackageDeclarationopt(self,  _PackageDeclarationopt) :   self._PackageDeclarationopt = _PackageDeclarationopt
        '''/**
         * The value returned by <b>getImportDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getImportDeclarationsopt(self)  :  return self._ImportDeclarationsopt
        def  setImportDeclarationsopt(self,  _ImportDeclarationsopt) :   self._ImportDeclarationsopt = _ImportDeclarationsopt
        '''/**
         * The value returned by <b>getTypeDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getTypeDeclarationsopt(self)  :  return self._TypeDeclarationsopt
        def  setTypeDeclarationsopt(self,  _TypeDeclarationsopt) :   self._TypeDeclarationsopt = _TypeDeclarationsopt

        __slots__ = ('_PackageDeclarationopt', '_ImportDeclarationsopt', '_TypeDeclarationsopt')

        def __init__(self, leftIToken, rightIToken,
                             _PackageDeclarationopt,
                             _ImportDeclarationsopt,
                             _TypeDeclarationsopt):
        
            super(CompilationUnit, self).__init__(leftIToken, rightIToken)

            self._PackageDeclarationopt = _PackageDeclarationopt
            if _PackageDeclarationopt: _PackageDeclarationopt.setParent(self)
            self._ImportDeclarationsopt = _ImportDeclarationsopt
            if _ImportDeclarationsopt: _ImportDeclarationsopt.setParent(self)
            self._TypeDeclarationsopt = _TypeDeclarationsopt
            if _TypeDeclarationsopt: _TypeDeclarationsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PackageDeclarationopt:  _content.add(self._PackageDeclarationopt)
            if self._ImportDeclarationsopt:  _content.add(self._ImportDeclarationsopt)
            if self._TypeDeclarationsopt:  _content.add(self._TypeDeclarationsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitCompilationUnit(self)
        def  acceptWithArg(self, v, o):  v.visitCompilationUnit(self, o)
        def  acceptWithResult(self, v):  return v.visitCompilationUnit(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitCompilationUnit(self, o)
    

'''/**
 *<em>
*<li>Rule 58:  ImportDeclarations ::= ImportDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 59:  ImportDeclarations ::= ImportDeclarations ImportDeclaration
 *</b>
 */'''
class ImportDeclarations ( Ast ,IImportDeclarations):
    

        def  getImportDeclarations(self)  :  return self._ImportDeclarations
        def  setImportDeclarations(self,  _ImportDeclarations) :   self._ImportDeclarations = _ImportDeclarations
        def  getImportDeclaration(self)  :  return self._ImportDeclaration
        def  setImportDeclaration(self,  _ImportDeclaration) :   self._ImportDeclaration = _ImportDeclaration

        __slots__ = ('_ImportDeclarations', '_ImportDeclaration')

        def __init__(self, leftIToken, rightIToken,
                             _ImportDeclarations,
                             _ImportDeclaration):
        
            super(ImportDeclarations, self).__init__(leftIToken, rightIToken)

            self._ImportDeclarations = _ImportDeclarations
            _ImportDeclarations.setParent(self)
            self._ImportDeclaration = _ImportDeclaration
            _ImportDeclaration.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ImportDeclarations:  _content.add(self._ImportDeclarations)
            if self._ImportDeclaration:  _content.add(self._ImportDeclaration)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitImportDeclarations(self)
        def  acceptWithArg(self, v, o):  v.visitImportDeclarations(self, o)
        def  acceptWithResult(self, v):  return v.visitImportDeclarations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitImportDeclarations(self, o)
    

'''/**
 *<em>
*<li>Rule 60:  TypeDeclarations ::= TypeDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 61:  TypeDeclarations ::= TypeDeclarations TypeDeclaration
 *</b>
 */'''
class TypeDeclarations ( Ast ,ITypeDeclarations):
    

        def  getTypeDeclarations(self)  :  return self._TypeDeclarations
        def  setTypeDeclarations(self,  _TypeDeclarations) :   self._TypeDeclarations = _TypeDeclarations
        def  getTypeDeclaration(self)  :  return self._TypeDeclaration
        def  setTypeDeclaration(self,  _TypeDeclaration) :   self._TypeDeclaration = _TypeDeclaration

        __slots__ = ('_TypeDeclarations', '_TypeDeclaration')

        def __init__(self, leftIToken, rightIToken,
                             _TypeDeclarations,
                             _TypeDeclaration):
        
            super(TypeDeclarations, self).__init__(leftIToken, rightIToken)

            self._TypeDeclarations = _TypeDeclarations
            _TypeDeclarations.setParent(self)
            self._TypeDeclaration = _TypeDeclaration
            _TypeDeclaration.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeDeclarations:  _content.add(self._TypeDeclarations)
            if self._TypeDeclaration:  _content.add(self._TypeDeclaration)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeDeclarations(self)
        def  acceptWithArg(self, v, o):  v.visitTypeDeclarations(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeDeclarations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeDeclarations(self, o)
    

'''/**
 *<b>
*<li>Rule 62:  PackageDeclaration ::= Annotationsopt package PackageName ;
 *</b>
 */'''
class PackageDeclaration ( Ast ,IPackageDeclaration):
    

        '''/**
         * The value returned by <b>getAnnotationsopt</b> may be <b>null</b>
         */'''
        def  getAnnotationsopt(self)  :  return self._Annotationsopt
        def  setAnnotationsopt(self,  _Annotationsopt) :   self._Annotationsopt = _Annotationsopt
        def  getpackage(self)  :  return self._package
        def  setpackage(self,  _package) :   self._package = _package
        def  getPackageName(self)  :  return self._PackageName
        def  setPackageName(self,  _PackageName) :   self._PackageName = _PackageName
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_Annotationsopt', '_package', '_PackageName', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _Annotationsopt,
                             _package,
                             _PackageName,
                             _SEMICOLON):
        
            super(PackageDeclaration, self).__init__(leftIToken, rightIToken)

            self._Annotationsopt = _Annotationsopt
            if _Annotationsopt: _Annotationsopt.setParent(self)
            self._package = _package
            _package.setParent(self)
            self._PackageName = _PackageName
            _PackageName.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Annotationsopt:  _content.add(self._Annotationsopt)
            if self._package:  _content.add(self._package)
            if self._PackageName:  _content.add(self._PackageName)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPackageDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitPackageDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitPackageDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPackageDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 67:  SingleTypeImportDeclaration ::= import TypeName ;
 *</b>
 */'''
class SingleTypeImportDeclaration ( Ast ,ISingleTypeImportDeclaration):
    

        def  getimport(self)  :  return self._import
        def  setimport(self,  _import) :   self._import = _import
        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_import', '_TypeName', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _import,
                             _TypeName,
                             _SEMICOLON):
        
            super(SingleTypeImportDeclaration, self).__init__(leftIToken, rightIToken)

            self._import = _import
            _import.setParent(self)
            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._import:  _content.add(self._import)
            if self._TypeName:  _content.add(self._TypeName)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSingleTypeImportDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitSingleTypeImportDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitSingleTypeImportDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSingleTypeImportDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 68:  TypeImportOnDemandDeclaration ::= import PackageOrTypeName . * ;
 *</b>
 */'''
class TypeImportOnDemandDeclaration ( Ast ,ITypeImportOnDemandDeclaration):
    

        def  getimport(self)  :  return self._import
        def  setimport(self,  _import) :   self._import = _import
        def  getPackageOrTypeName(self)  :  return self._PackageOrTypeName
        def  setPackageOrTypeName(self,  _PackageOrTypeName) :   self._PackageOrTypeName = _PackageOrTypeName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getMULTIPLY(self)  :  return self._MULTIPLY
        def  setMULTIPLY(self,  _MULTIPLY) :   self._MULTIPLY = _MULTIPLY
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_import', '_PackageOrTypeName', '_DOT', '_MULTIPLY', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _import,
                             _PackageOrTypeName,
                             _DOT,
                             _MULTIPLY,
                             _SEMICOLON):
        
            super(TypeImportOnDemandDeclaration, self).__init__(leftIToken, rightIToken)

            self._import = _import
            _import.setParent(self)
            self._PackageOrTypeName = _PackageOrTypeName
            _PackageOrTypeName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._MULTIPLY = _MULTIPLY
            _MULTIPLY.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._import:  _content.add(self._import)
            if self._PackageOrTypeName:  _content.add(self._PackageOrTypeName)
            if self._DOT:  _content.add(self._DOT)
            if self._MULTIPLY:  _content.add(self._MULTIPLY)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeImportOnDemandDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitTypeImportOnDemandDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeImportOnDemandDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeImportOnDemandDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 69:  SingleStaticImportDeclaration ::= import static TypeName . identifier ;
 *</b>
 */'''
class SingleStaticImportDeclaration ( Ast ,ISingleStaticImportDeclaration):
    

        def  getimport(self)  :  return self._import
        def  setimport(self,  _import) :   self._import = _import
        def  getstatic(self)  :  return self._static
        def  setstatic(self,  _static) :   self._static = _static
        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_import', '_static', '_TypeName', '_DOT', '_identifier', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _import,
                             _static,
                             _TypeName,
                             _DOT,
                             _identifier,
                             _SEMICOLON):
        
            super(SingleStaticImportDeclaration, self).__init__(leftIToken, rightIToken)

            self._import = _import
            _import.setParent(self)
            self._static = _static
            _static.setParent(self)
            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._import:  _content.add(self._import)
            if self._static:  _content.add(self._static)
            if self._TypeName:  _content.add(self._TypeName)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSingleStaticImportDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitSingleStaticImportDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitSingleStaticImportDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSingleStaticImportDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 70:  StaticImportOnDemandDeclaration ::= import static TypeName . * ;
 *</b>
 */'''
class StaticImportOnDemandDeclaration ( Ast ,IStaticImportOnDemandDeclaration):
    

        def  getimport(self)  :  return self._import
        def  setimport(self,  _import) :   self._import = _import
        def  getstatic(self)  :  return self._static
        def  setstatic(self,  _static) :   self._static = _static
        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getMULTIPLY(self)  :  return self._MULTIPLY
        def  setMULTIPLY(self,  _MULTIPLY) :   self._MULTIPLY = _MULTIPLY
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_import', '_static', '_TypeName', '_DOT', '_MULTIPLY', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _import,
                             _static,
                             _TypeName,
                             _DOT,
                             _MULTIPLY,
                             _SEMICOLON):
        
            super(StaticImportOnDemandDeclaration, self).__init__(leftIToken, rightIToken)

            self._import = _import
            _import.setParent(self)
            self._static = _static
            _static.setParent(self)
            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._MULTIPLY = _MULTIPLY
            _MULTIPLY.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._import:  _content.add(self._import)
            if self._static:  _content.add(self._static)
            if self._TypeName:  _content.add(self._TypeName)
            if self._DOT:  _content.add(self._DOT)
            if self._MULTIPLY:  _content.add(self._MULTIPLY)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitStaticImportOnDemandDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitStaticImportOnDemandDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitStaticImportOnDemandDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitStaticImportOnDemandDeclaration(self, o)
    

'''/**
 *<em>
*<li>Rule 71:  TypeDeclaration ::= ClassDeclaration
*<li>Rule 72:  TypeDeclaration ::= InterfaceDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 73:  TypeDeclaration ::= ;
 *</b>
 */'''
class TypeDeclaration ( AstToken ,ITypeDeclaration):
    
        def  getSEMICOLON(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(TypeDeclaration, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitTypeDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitTypeDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 76:  NormalClassDeclaration ::= ClassModifiersopt class identifier TypeParametersopt Superopt Interfacesopt ClassBody
 *</b>
 */'''
class NormalClassDeclaration ( Ast ,INormalClassDeclaration):
    

        '''/**
         * The value returned by <b>getClassModifiersopt</b> may be <b>null</b>
         */'''
        def  getClassModifiersopt(self)  :  return self._ClassModifiersopt
        def  setClassModifiersopt(self,  _ClassModifiersopt) :   self._ClassModifiersopt = _ClassModifiersopt
        def  getclass(self)  :  return self._class
        def  setclass(self,  _class) :   self._class = _class
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        '''/**
         * The value returned by <b>getTypeParametersopt</b> may be <b>null</b>
         */'''
        def  getTypeParametersopt(self)  :  return self._TypeParametersopt
        def  setTypeParametersopt(self,  _TypeParametersopt) :   self._TypeParametersopt = _TypeParametersopt
        '''/**
         * The value returned by <b>getSuperopt</b> may be <b>null</b>
         */'''
        def  getSuperopt(self)  :  return self._Superopt
        def  setSuperopt(self,  _Superopt) :   self._Superopt = _Superopt
        '''/**
         * The value returned by <b>getInterfacesopt</b> may be <b>null</b>
         */'''
        def  getInterfacesopt(self)  :  return self._Interfacesopt
        def  setInterfacesopt(self,  _Interfacesopt) :   self._Interfacesopt = _Interfacesopt
        def  getClassBody(self)  :  return self._ClassBody
        def  setClassBody(self,  _ClassBody) :   self._ClassBody = _ClassBody

        __slots__ = ('_ClassModifiersopt', '_class', '_identifier', '_TypeParametersopt', '_Superopt', '_Interfacesopt', '_ClassBody')

        def __init__(self, leftIToken, rightIToken,
                             _ClassModifiersopt,
                             _class,
                             _identifier,
                             _TypeParametersopt,
                             _Superopt,
                             _Interfacesopt,
                             _ClassBody):
        
            super(NormalClassDeclaration, self).__init__(leftIToken, rightIToken)

            self._ClassModifiersopt = _ClassModifiersopt
            if _ClassModifiersopt: _ClassModifiersopt.setParent(self)
            self._class = _class
            _class.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._TypeParametersopt = _TypeParametersopt
            if _TypeParametersopt: _TypeParametersopt.setParent(self)
            self._Superopt = _Superopt
            if _Superopt: _Superopt.setParent(self)
            self._Interfacesopt = _Interfacesopt
            if _Interfacesopt: _Interfacesopt.setParent(self)
            self._ClassBody = _ClassBody
            _ClassBody.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassModifiersopt:  _content.add(self._ClassModifiersopt)
            if self._class:  _content.add(self._class)
            if self._identifier:  _content.add(self._identifier)
            if self._TypeParametersopt:  _content.add(self._TypeParametersopt)
            if self._Superopt:  _content.add(self._Superopt)
            if self._Interfacesopt:  _content.add(self._Interfacesopt)
            if self._ClassBody:  _content.add(self._ClassBody)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitNormalClassDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitNormalClassDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitNormalClassDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitNormalClassDeclaration(self, o)
    

'''/**
 *<em>
*<li>Rule 77:  ClassModifiers ::= ClassModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 78:  ClassModifiers ::= ClassModifiers ClassModifier
 *</b>
 */'''
class ClassModifiers ( Ast ,IClassModifiers):
    

        def  getClassModifiers(self)  :  return self._ClassModifiers
        def  setClassModifiers(self,  _ClassModifiers) :   self._ClassModifiers = _ClassModifiers
        def  getClassModifier(self)  :  return self._ClassModifier
        def  setClassModifier(self,  _ClassModifier) :   self._ClassModifier = _ClassModifier

        __slots__ = ('_ClassModifiers', '_ClassModifier')

        def __init__(self, leftIToken, rightIToken,
                             _ClassModifiers,
                             _ClassModifier):
        
            super(ClassModifiers, self).__init__(leftIToken, rightIToken)

            self._ClassModifiers = _ClassModifiers
            _ClassModifiers.setParent(self)
            self._ClassModifier = _ClassModifier
            _ClassModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassModifiers:  _content.add(self._ClassModifiers)
            if self._ClassModifier:  _content.add(self._ClassModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitClassModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 87:  TypeParameters ::= < TypeParameterList >
 *</b>
 */'''
class TypeParameters ( Ast ,ITypeParameters):
    

        def  getLESS(self)  :  return self._LESS
        def  setLESS(self,  _LESS) :   self._LESS = _LESS
        def  getTypeParameterList(self)  :  return self._TypeParameterList
        def  setTypeParameterList(self,  _TypeParameterList) :   self._TypeParameterList = _TypeParameterList
        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER

        __slots__ = ('_LESS', '_TypeParameterList', '_GREATER')

        def __init__(self, leftIToken, rightIToken,
                             _LESS,
                             _TypeParameterList,
                             _GREATER):
        
            super(TypeParameters, self).__init__(leftIToken, rightIToken)

            self._LESS = _LESS
            _LESS.setParent(self)
            self._TypeParameterList = _TypeParameterList
            _TypeParameterList.setParent(self)
            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LESS:  _content.add(self._LESS)
            if self._TypeParameterList:  _content.add(self._TypeParameterList)
            if self._GREATER:  _content.add(self._GREATER)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeParameters(self)
        def  acceptWithArg(self, v, o):  v.visitTypeParameters(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeParameters(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeParameters(self, o)
    

'''/**
 *<em>
*<li>Rule 88:  TypeParameterList ::= TypeParameter
 *</em>
 *<p>
 *<b>
*<li>Rule 89:  TypeParameterList ::= TypeParameterList , TypeParameter
 *</b>
 */'''
class TypeParameterList ( Ast ,ITypeParameterList):
    

        def  getTypeParameterList(self)  :  return self._TypeParameterList
        def  setTypeParameterList(self,  _TypeParameterList) :   self._TypeParameterList = _TypeParameterList
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getTypeParameter(self)  :  return self._TypeParameter
        def  setTypeParameter(self,  _TypeParameter) :   self._TypeParameter = _TypeParameter

        __slots__ = ('_TypeParameterList', '_COMMA', '_TypeParameter')

        def __init__(self, leftIToken, rightIToken,
                             _TypeParameterList,
                             _COMMA,
                             _TypeParameter):
        
            super(TypeParameterList, self).__init__(leftIToken, rightIToken)

            self._TypeParameterList = _TypeParameterList
            _TypeParameterList.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._TypeParameter = _TypeParameter
            _TypeParameter.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeParameterList:  _content.add(self._TypeParameterList)
            if self._COMMA:  _content.add(self._COMMA)
            if self._TypeParameter:  _content.add(self._TypeParameter)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTypeParameterList(self)
        def  acceptWithArg(self, v, o):  v.visitTypeParameterList(self, o)
        def  acceptWithResult(self, v):  return v.visitTypeParameterList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTypeParameterList(self, o)
    

'''/**
 *<b>
*<li>Rule 90:  Super ::= extends ClassType
 *</b>
 */'''
class Super ( Ast ,ISuper):
    

        def  getextends(self)  :  return self._extends
        def  setextends(self,  _extends) :   self._extends = _extends
        def  getClassType(self)  :  return self._ClassType
        def  setClassType(self,  _ClassType) :   self._ClassType = _ClassType

        __slots__ = ('_extends', '_ClassType')

        def __init__(self, leftIToken, rightIToken,
                             _extends,
                             _ClassType):
        
            super(Super, self).__init__(leftIToken, rightIToken)

            self._extends = _extends
            _extends.setParent(self)
            self._ClassType = _ClassType
            _ClassType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._extends:  _content.add(self._extends)
            if self._ClassType:  _content.add(self._ClassType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSuper(self)
        def  acceptWithArg(self, v, o):  v.visitSuper(self, o)
        def  acceptWithResult(self, v):  return v.visitSuper(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSuper(self, o)
    

'''/**
 *<b>
*<li>Rule 91:  Interfaces ::= implements InterfaceTypeList
 *</b>
 */'''
class Interfaces ( Ast ,IInterfaces):
    

        def  getimplements(self)  :  return self._implements
        def  setimplements(self,  _implements) :   self._implements = _implements
        def  getInterfaceTypeList(self)  :  return self._InterfaceTypeList
        def  setInterfaceTypeList(self,  _InterfaceTypeList) :   self._InterfaceTypeList = _InterfaceTypeList

        __slots__ = ('_implements', '_InterfaceTypeList')

        def __init__(self, leftIToken, rightIToken,
                             _implements,
                             _InterfaceTypeList):
        
            super(Interfaces, self).__init__(leftIToken, rightIToken)

            self._implements = _implements
            _implements.setParent(self)
            self._InterfaceTypeList = _InterfaceTypeList
            _InterfaceTypeList.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._implements:  _content.add(self._implements)
            if self._InterfaceTypeList:  _content.add(self._InterfaceTypeList)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInterfaces(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaces(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaces(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaces(self, o)
    

'''/**
 *<em>
*<li>Rule 92:  InterfaceTypeList ::= InterfaceType
 *</em>
 *<p>
 *<b>
*<li>Rule 93:  InterfaceTypeList ::= InterfaceTypeList , InterfaceType
 *</b>
 */'''
class InterfaceTypeList ( Ast ,IInterfaceTypeList):
    

        def  getInterfaceTypeList(self)  :  return self._InterfaceTypeList
        def  setInterfaceTypeList(self,  _InterfaceTypeList) :   self._InterfaceTypeList = _InterfaceTypeList
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getInterfaceType(self)  :  return self._InterfaceType
        def  setInterfaceType(self,  _InterfaceType) :   self._InterfaceType = _InterfaceType

        __slots__ = ('_InterfaceTypeList', '_COMMA', '_InterfaceType')

        def __init__(self, leftIToken, rightIToken,
                             _InterfaceTypeList,
                             _COMMA,
                             _InterfaceType):
        
            super(InterfaceTypeList, self).__init__(leftIToken, rightIToken)

            self._InterfaceTypeList = _InterfaceTypeList
            _InterfaceTypeList.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._InterfaceType = _InterfaceType
            _InterfaceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._InterfaceTypeList:  _content.add(self._InterfaceTypeList)
            if self._COMMA:  _content.add(self._COMMA)
            if self._InterfaceType:  _content.add(self._InterfaceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInterfaceTypeList(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceTypeList(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceTypeList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceTypeList(self, o)
    

'''/**
 *<b>
*<li>Rule 94:  ClassBody ::= { ClassBodyDeclarationsopt }
 *</b>
 */'''
class ClassBody ( Ast ,IClassBody):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getClassBodyDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getClassBodyDeclarationsopt(self)  :  return self._ClassBodyDeclarationsopt
        def  setClassBodyDeclarationsopt(self,  _ClassBodyDeclarationsopt) :   self._ClassBodyDeclarationsopt = _ClassBodyDeclarationsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_ClassBodyDeclarationsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _ClassBodyDeclarationsopt,
                             _RBRACE):
        
            super(ClassBody, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._ClassBodyDeclarationsopt = _ClassBodyDeclarationsopt
            if _ClassBodyDeclarationsopt: _ClassBodyDeclarationsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._ClassBodyDeclarationsopt:  _content.add(self._ClassBodyDeclarationsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitClassBody(self)
        def  acceptWithArg(self, v, o):  v.visitClassBody(self, o)
        def  acceptWithResult(self, v):  return v.visitClassBody(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassBody(self, o)
    

'''/**
 *<em>
*<li>Rule 95:  ClassBodyDeclarations ::= ClassBodyDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 96:  ClassBodyDeclarations ::= ClassBodyDeclarations ClassBodyDeclaration
 *</b>
 */'''
class ClassBodyDeclarations ( Ast ,IClassBodyDeclarations):
    

        def  getClassBodyDeclarations(self)  :  return self._ClassBodyDeclarations
        def  setClassBodyDeclarations(self,  _ClassBodyDeclarations) :   self._ClassBodyDeclarations = _ClassBodyDeclarations
        def  getClassBodyDeclaration(self)  :  return self._ClassBodyDeclaration
        def  setClassBodyDeclaration(self,  _ClassBodyDeclaration) :   self._ClassBodyDeclaration = _ClassBodyDeclaration

        __slots__ = ('_ClassBodyDeclarations', '_ClassBodyDeclaration')

        def __init__(self, leftIToken, rightIToken,
                             _ClassBodyDeclarations,
                             _ClassBodyDeclaration):
        
            super(ClassBodyDeclarations, self).__init__(leftIToken, rightIToken)

            self._ClassBodyDeclarations = _ClassBodyDeclarations
            _ClassBodyDeclarations.setParent(self)
            self._ClassBodyDeclaration = _ClassBodyDeclaration
            _ClassBodyDeclaration.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassBodyDeclarations:  _content.add(self._ClassBodyDeclarations)
            if self._ClassBodyDeclaration:  _content.add(self._ClassBodyDeclaration)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitClassBodyDeclarations(self)
        def  acceptWithArg(self, v, o):  v.visitClassBodyDeclarations(self, o)
        def  acceptWithResult(self, v):  return v.visitClassBodyDeclarations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassBodyDeclarations(self, o)
    

'''/**
 *<em>
*<li>Rule 101:  ClassMemberDeclaration ::= FieldDeclaration
*<li>Rule 102:  ClassMemberDeclaration ::= MethodDeclaration
*<li>Rule 103:  ClassMemberDeclaration ::= ClassDeclaration
*<li>Rule 104:  ClassMemberDeclaration ::= InterfaceDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 105:  ClassMemberDeclaration ::= ;
 *</b>
 */'''
class ClassMemberDeclaration ( AstToken ,IClassMemberDeclaration):
    
        def  getSEMICOLON(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassMemberDeclaration, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassMemberDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitClassMemberDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitClassMemberDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassMemberDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 106:  FieldDeclaration ::= FieldModifiersopt Type VariableDeclarators ;
 *</b>
 */'''
class FieldDeclaration ( Ast ,IFieldDeclaration):
    

        '''/**
         * The value returned by <b>getFieldModifiersopt</b> may be <b>null</b>
         */'''
        def  getFieldModifiersopt(self)  :  return self._FieldModifiersopt
        def  setFieldModifiersopt(self,  _FieldModifiersopt) :   self._FieldModifiersopt = _FieldModifiersopt
        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getVariableDeclarators(self)  :  return self._VariableDeclarators
        def  setVariableDeclarators(self,  _VariableDeclarators) :   self._VariableDeclarators = _VariableDeclarators
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_FieldModifiersopt', '_Type', '_VariableDeclarators', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _FieldModifiersopt,
                             _Type,
                             _VariableDeclarators,
                             _SEMICOLON):
        
            super(FieldDeclaration, self).__init__(leftIToken, rightIToken)

            self._FieldModifiersopt = _FieldModifiersopt
            if _FieldModifiersopt: _FieldModifiersopt.setParent(self)
            self._Type = _Type
            _Type.setParent(self)
            self._VariableDeclarators = _VariableDeclarators
            _VariableDeclarators.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._FieldModifiersopt:  _content.add(self._FieldModifiersopt)
            if self._Type:  _content.add(self._Type)
            if self._VariableDeclarators:  _content.add(self._VariableDeclarators)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFieldDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitFieldDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldDeclaration(self, o)
    

'''/**
 *<em>
*<li>Rule 107:  VariableDeclarators ::= VariableDeclarator
 *</em>
 *<p>
 *<b>
*<li>Rule 108:  VariableDeclarators ::= VariableDeclarators , VariableDeclarator
 *</b>
 */'''
class VariableDeclarators ( Ast ,IVariableDeclarators):
    

        def  getVariableDeclarators(self)  :  return self._VariableDeclarators
        def  setVariableDeclarators(self,  _VariableDeclarators) :   self._VariableDeclarators = _VariableDeclarators
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getVariableDeclarator(self)  :  return self._VariableDeclarator
        def  setVariableDeclarator(self,  _VariableDeclarator) :   self._VariableDeclarator = _VariableDeclarator

        __slots__ = ('_VariableDeclarators', '_COMMA', '_VariableDeclarator')

        def __init__(self, leftIToken, rightIToken,
                             _VariableDeclarators,
                             _COMMA,
                             _VariableDeclarator):
        
            super(VariableDeclarators, self).__init__(leftIToken, rightIToken)

            self._VariableDeclarators = _VariableDeclarators
            _VariableDeclarators.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._VariableDeclarator = _VariableDeclarator
            _VariableDeclarator.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableDeclarators:  _content.add(self._VariableDeclarators)
            if self._COMMA:  _content.add(self._COMMA)
            if self._VariableDeclarator:  _content.add(self._VariableDeclarator)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitVariableDeclarators(self)
        def  acceptWithArg(self, v, o):  v.visitVariableDeclarators(self, o)
        def  acceptWithResult(self, v):  return v.visitVariableDeclarators(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitVariableDeclarators(self, o)
    

'''/**
 *<em>
*<li>Rule 109:  VariableDeclarator ::= VariableDeclaratorId
 *</em>
 *<p>
 *<b>
*<li>Rule 110:  VariableDeclarator ::= VariableDeclaratorId = VariableInitializer
 *</b>
 */'''
class VariableDeclarator ( Ast ,IVariableDeclarator):
    

        def  getVariableDeclaratorId(self)  :  return self._VariableDeclaratorId
        def  setVariableDeclaratorId(self,  _VariableDeclaratorId) :   self._VariableDeclaratorId = _VariableDeclaratorId
        def  getEQUAL(self)  :  return self._EQUAL
        def  setEQUAL(self,  _EQUAL) :   self._EQUAL = _EQUAL
        def  getVariableInitializer(self)  :  return self._VariableInitializer
        def  setVariableInitializer(self,  _VariableInitializer) :   self._VariableInitializer = _VariableInitializer

        __slots__ = ('_VariableDeclaratorId', '_EQUAL', '_VariableInitializer')

        def __init__(self, leftIToken, rightIToken,
                             _VariableDeclaratorId,
                             _EQUAL,
                             _VariableInitializer):
        
            super(VariableDeclarator, self).__init__(leftIToken, rightIToken)

            self._VariableDeclaratorId = _VariableDeclaratorId
            _VariableDeclaratorId.setParent(self)
            self._EQUAL = _EQUAL
            _EQUAL.setParent(self)
            self._VariableInitializer = _VariableInitializer
            _VariableInitializer.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableDeclaratorId:  _content.add(self._VariableDeclaratorId)
            if self._EQUAL:  _content.add(self._EQUAL)
            if self._VariableInitializer:  _content.add(self._VariableInitializer)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitVariableDeclarator(self)
        def  acceptWithArg(self, v, o):  v.visitVariableDeclarator(self, o)
        def  acceptWithResult(self, v):  return v.visitVariableDeclarator(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitVariableDeclarator(self, o)
    

'''/**
 *<em>
*<li>Rule 111:  VariableDeclaratorId ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 112:  VariableDeclaratorId ::= VariableDeclaratorId [ ]
 *</b>
 */'''
class VariableDeclaratorId ( Ast ,IVariableDeclaratorId):
    

        def  getVariableDeclaratorId(self)  :  return self._VariableDeclaratorId
        def  setVariableDeclaratorId(self,  _VariableDeclaratorId) :   self._VariableDeclaratorId = _VariableDeclaratorId
        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_VariableDeclaratorId', '_LBRACKET', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _VariableDeclaratorId,
                             _LBRACKET,
                             _RBRACKET):
        
            super(VariableDeclaratorId, self).__init__(leftIToken, rightIToken)

            self._VariableDeclaratorId = _VariableDeclaratorId
            _VariableDeclaratorId.setParent(self)
            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableDeclaratorId:  _content.add(self._VariableDeclaratorId)
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitVariableDeclaratorId(self)
        def  acceptWithArg(self, v, o):  v.visitVariableDeclaratorId(self, o)
        def  acceptWithResult(self, v):  return v.visitVariableDeclaratorId(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitVariableDeclaratorId(self, o)
    

'''/**
 *<em>
*<li>Rule 115:  FieldModifiers ::= FieldModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 116:  FieldModifiers ::= FieldModifiers FieldModifier
 *</b>
 */'''
class FieldModifiers ( Ast ,IFieldModifiers):
    

        def  getFieldModifiers(self)  :  return self._FieldModifiers
        def  setFieldModifiers(self,  _FieldModifiers) :   self._FieldModifiers = _FieldModifiers
        def  getFieldModifier(self)  :  return self._FieldModifier
        def  setFieldModifier(self,  _FieldModifier) :   self._FieldModifier = _FieldModifier

        __slots__ = ('_FieldModifiers', '_FieldModifier')

        def __init__(self, leftIToken, rightIToken,
                             _FieldModifiers,
                             _FieldModifier):
        
            super(FieldModifiers, self).__init__(leftIToken, rightIToken)

            self._FieldModifiers = _FieldModifiers
            _FieldModifiers.setParent(self)
            self._FieldModifier = _FieldModifier
            _FieldModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._FieldModifiers:  _content.add(self._FieldModifiers)
            if self._FieldModifier:  _content.add(self._FieldModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFieldModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 125:  MethodDeclaration ::= MethodHeader MethodBody
 *</b>
 */'''
class MethodDeclaration ( Ast ,IMethodDeclaration):
    

        def  getMethodHeader(self)  :  return self._MethodHeader
        def  setMethodHeader(self,  _MethodHeader) :   self._MethodHeader = _MethodHeader
        def  getMethodBody(self)  :  return self._MethodBody
        def  setMethodBody(self,  _MethodBody) :   self._MethodBody = _MethodBody

        __slots__ = ('_MethodHeader', '_MethodBody')

        def __init__(self, leftIToken, rightIToken,
                             _MethodHeader,
                             _MethodBody):
        
            super(MethodDeclaration, self).__init__(leftIToken, rightIToken)

            self._MethodHeader = _MethodHeader
            _MethodHeader.setParent(self)
            self._MethodBody = _MethodBody
            _MethodBody.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MethodHeader:  _content.add(self._MethodHeader)
            if self._MethodBody:  _content.add(self._MethodBody)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitMethodDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 126:  MethodHeader ::= MethodModifiersopt TypeParametersopt ResultType MethodDeclarator Throwsopt
 *</b>
 */'''
class MethodHeader ( Ast ,IMethodHeader):
    

        '''/**
         * The value returned by <b>getMethodModifiersopt</b> may be <b>null</b>
         */'''
        def  getMethodModifiersopt(self)  :  return self._MethodModifiersopt
        def  setMethodModifiersopt(self,  _MethodModifiersopt) :   self._MethodModifiersopt = _MethodModifiersopt
        '''/**
         * The value returned by <b>getTypeParametersopt</b> may be <b>null</b>
         */'''
        def  getTypeParametersopt(self)  :  return self._TypeParametersopt
        def  setTypeParametersopt(self,  _TypeParametersopt) :   self._TypeParametersopt = _TypeParametersopt
        def  getResultType(self)  :  return self._ResultType
        def  setResultType(self,  _ResultType) :   self._ResultType = _ResultType
        def  getMethodDeclarator(self)  :  return self._MethodDeclarator
        def  setMethodDeclarator(self,  _MethodDeclarator) :   self._MethodDeclarator = _MethodDeclarator
        '''/**
         * The value returned by <b>getThrowsopt</b> may be <b>null</b>
         */'''
        def  getThrowsopt(self)  :  return self._Throwsopt
        def  setThrowsopt(self,  _Throwsopt) :   self._Throwsopt = _Throwsopt

        __slots__ = ('_MethodModifiersopt', '_TypeParametersopt', '_ResultType', '_MethodDeclarator', '_Throwsopt')

        def __init__(self, leftIToken, rightIToken,
                             _MethodModifiersopt,
                             _TypeParametersopt,
                             _ResultType,
                             _MethodDeclarator,
                             _Throwsopt):
        
            super(MethodHeader, self).__init__(leftIToken, rightIToken)

            self._MethodModifiersopt = _MethodModifiersopt
            if _MethodModifiersopt: _MethodModifiersopt.setParent(self)
            self._TypeParametersopt = _TypeParametersopt
            if _TypeParametersopt: _TypeParametersopt.setParent(self)
            self._ResultType = _ResultType
            _ResultType.setParent(self)
            self._MethodDeclarator = _MethodDeclarator
            _MethodDeclarator.setParent(self)
            self._Throwsopt = _Throwsopt
            if _Throwsopt: _Throwsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MethodModifiersopt:  _content.add(self._MethodModifiersopt)
            if self._TypeParametersopt:  _content.add(self._TypeParametersopt)
            if self._ResultType:  _content.add(self._ResultType)
            if self._MethodDeclarator:  _content.add(self._MethodDeclarator)
            if self._Throwsopt:  _content.add(self._Throwsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodHeader(self)
        def  acceptWithArg(self, v, o):  v.visitMethodHeader(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodHeader(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodHeader(self, o)
    

'''/**
 *<em>
*<li>Rule 127:  ResultType ::= Type
 *</em>
 *<p>
 *<b>
*<li>Rule 128:  ResultType ::= void
 *</b>
 */'''
class ResultType ( AstToken ,IResultType):
    
        def  getvoid(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ResultType, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitResultType(self)
        def  acceptWithArg(self, v, o):  v.visitResultType(self, o)
        def  acceptWithResult(self, v):  return v.visitResultType(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitResultType(self, o)
    

'''/**
 *<em>
*<li>Rule 131:  FormalParameterList ::= LastFormalParameter
 *</em>
 *<p>
 *<b>
*<li>Rule 132:  FormalParameterList ::= FormalParameters , LastFormalParameter
 *</b>
 */'''
class FormalParameterList ( Ast ,IFormalParameterList):
    

        def  getFormalParameters(self)  :  return self._FormalParameters
        def  setFormalParameters(self,  _FormalParameters) :   self._FormalParameters = _FormalParameters
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getLastFormalParameter(self)  :  return self._LastFormalParameter
        def  setLastFormalParameter(self,  _LastFormalParameter) :   self._LastFormalParameter = _LastFormalParameter

        __slots__ = ('_FormalParameters', '_COMMA', '_LastFormalParameter')

        def __init__(self, leftIToken, rightIToken,
                             _FormalParameters,
                             _COMMA,
                             _LastFormalParameter):
        
            super(FormalParameterList, self).__init__(leftIToken, rightIToken)

            self._FormalParameters = _FormalParameters
            _FormalParameters.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._LastFormalParameter = _LastFormalParameter
            _LastFormalParameter.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._FormalParameters:  _content.add(self._FormalParameters)
            if self._COMMA:  _content.add(self._COMMA)
            if self._LastFormalParameter:  _content.add(self._LastFormalParameter)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFormalParameterList(self)
        def  acceptWithArg(self, v, o):  v.visitFormalParameterList(self, o)
        def  acceptWithResult(self, v):  return v.visitFormalParameterList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFormalParameterList(self, o)
    

'''/**
 *<em>
*<li>Rule 133:  FormalParameters ::= FormalParameter
 *</em>
 *<p>
 *<b>
*<li>Rule 134:  FormalParameters ::= FormalParameters , FormalParameter
 *</b>
 */'''
class FormalParameters ( Ast ,IFormalParameters):
    

        def  getFormalParameters(self)  :  return self._FormalParameters
        def  setFormalParameters(self,  _FormalParameters) :   self._FormalParameters = _FormalParameters
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getFormalParameter(self)  :  return self._FormalParameter
        def  setFormalParameter(self,  _FormalParameter) :   self._FormalParameter = _FormalParameter

        __slots__ = ('_FormalParameters', '_COMMA', '_FormalParameter')

        def __init__(self, leftIToken, rightIToken,
                             _FormalParameters,
                             _COMMA,
                             _FormalParameter):
        
            super(FormalParameters, self).__init__(leftIToken, rightIToken)

            self._FormalParameters = _FormalParameters
            _FormalParameters.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._FormalParameter = _FormalParameter
            _FormalParameter.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._FormalParameters:  _content.add(self._FormalParameters)
            if self._COMMA:  _content.add(self._COMMA)
            if self._FormalParameter:  _content.add(self._FormalParameter)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFormalParameters(self)
        def  acceptWithArg(self, v, o):  v.visitFormalParameters(self, o)
        def  acceptWithResult(self, v):  return v.visitFormalParameters(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFormalParameters(self, o)
    

'''/**
 *<b>
*<li>Rule 135:  FormalParameter ::= VariableModifiersopt Type VariableDeclaratorId
 *</b>
 */'''
class FormalParameter ( Ast ,IFormalParameter):
    

        '''/**
         * The value returned by <b>getVariableModifiersopt</b> may be <b>null</b>
         */'''
        def  getVariableModifiersopt(self)  :  return self._VariableModifiersopt
        def  setVariableModifiersopt(self,  _VariableModifiersopt) :   self._VariableModifiersopt = _VariableModifiersopt
        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getVariableDeclaratorId(self)  :  return self._VariableDeclaratorId
        def  setVariableDeclaratorId(self,  _VariableDeclaratorId) :   self._VariableDeclaratorId = _VariableDeclaratorId

        __slots__ = ('_VariableModifiersopt', '_Type', '_VariableDeclaratorId')

        def __init__(self, leftIToken, rightIToken,
                             _VariableModifiersopt,
                             _Type,
                             _VariableDeclaratorId):
        
            super(FormalParameter, self).__init__(leftIToken, rightIToken)

            self._VariableModifiersopt = _VariableModifiersopt
            if _VariableModifiersopt: _VariableModifiersopt.setParent(self)
            self._Type = _Type
            _Type.setParent(self)
            self._VariableDeclaratorId = _VariableDeclaratorId
            _VariableDeclaratorId.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableModifiersopt:  _content.add(self._VariableModifiersopt)
            if self._Type:  _content.add(self._Type)
            if self._VariableDeclaratorId:  _content.add(self._VariableDeclaratorId)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFormalParameter(self)
        def  acceptWithArg(self, v, o):  v.visitFormalParameter(self, o)
        def  acceptWithResult(self, v):  return v.visitFormalParameter(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFormalParameter(self, o)
    

'''/**
 *<em>
*<li>Rule 136:  VariableModifiers ::= VariableModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 137:  VariableModifiers ::= VariableModifiers VariableModifier
 *</b>
 */'''
class VariableModifiers ( Ast ,IVariableModifiers):
    

        def  getVariableModifiers(self)  :  return self._VariableModifiers
        def  setVariableModifiers(self,  _VariableModifiers) :   self._VariableModifiers = _VariableModifiers
        def  getVariableModifier(self)  :  return self._VariableModifier
        def  setVariableModifier(self,  _VariableModifier) :   self._VariableModifier = _VariableModifier

        __slots__ = ('_VariableModifiers', '_VariableModifier')

        def __init__(self, leftIToken, rightIToken,
                             _VariableModifiers,
                             _VariableModifier):
        
            super(VariableModifiers, self).__init__(leftIToken, rightIToken)

            self._VariableModifiers = _VariableModifiers
            _VariableModifiers.setParent(self)
            self._VariableModifier = _VariableModifier
            _VariableModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableModifiers:  _content.add(self._VariableModifiers)
            if self._VariableModifier:  _content.add(self._VariableModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitVariableModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitVariableModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitVariableModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitVariableModifiers(self, o)
    

'''/**
 *<em>
*<li>Rule 139:  VariableModifier ::= Annotations
 *</em>
 *<p>
 *<b>
*<li>Rule 138:  VariableModifier ::= final
 *</b>
 */'''
class VariableModifier ( AstToken ,IVariableModifier):
    
        def  getfinal(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(VariableModifier, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitVariableModifier(self)
        def  acceptWithArg(self, v, o):  v.visitVariableModifier(self, o)
        def  acceptWithResult(self, v):  return v.visitVariableModifier(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitVariableModifier(self, o)
    

'''/**
 *<b>
*<li>Rule 140:  LastFormalParameter ::= VariableModifiersopt Type ...opt VariableDeclaratorId
 *</b>
 */'''
class LastFormalParameter ( Ast ,ILastFormalParameter):
    

        '''/**
         * The value returned by <b>getVariableModifiersopt</b> may be <b>null</b>
         */'''
        def  getVariableModifiersopt(self)  :  return self._VariableModifiersopt
        def  setVariableModifiersopt(self,  _VariableModifiersopt) :   self._VariableModifiersopt = _VariableModifiersopt
        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        '''/**
         * The value returned by <b>getEllipsisopt</b> may be <b>null</b>
         */'''
        def  getEllipsisopt(self)  :  return self._Ellipsisopt
        def  setEllipsisopt(self,  _Ellipsisopt) :   self._Ellipsisopt = _Ellipsisopt
        def  getVariableDeclaratorId(self)  :  return self._VariableDeclaratorId
        def  setVariableDeclaratorId(self,  _VariableDeclaratorId) :   self._VariableDeclaratorId = _VariableDeclaratorId

        __slots__ = ('_VariableModifiersopt', '_Type', '_Ellipsisopt', '_VariableDeclaratorId')

        def __init__(self, leftIToken, rightIToken,
                             _VariableModifiersopt,
                             _Type,
                             _Ellipsisopt,
                             _VariableDeclaratorId):
        
            super(LastFormalParameter, self).__init__(leftIToken, rightIToken)

            self._VariableModifiersopt = _VariableModifiersopt
            if _VariableModifiersopt: _VariableModifiersopt.setParent(self)
            self._Type = _Type
            _Type.setParent(self)
            self._Ellipsisopt = _Ellipsisopt
            if _Ellipsisopt: _Ellipsisopt.setParent(self)
            self._VariableDeclaratorId = _VariableDeclaratorId
            _VariableDeclaratorId.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableModifiersopt:  _content.add(self._VariableModifiersopt)
            if self._Type:  _content.add(self._Type)
            if self._Ellipsisopt:  _content.add(self._Ellipsisopt)
            if self._VariableDeclaratorId:  _content.add(self._VariableDeclaratorId)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLastFormalParameter(self)
        def  acceptWithArg(self, v, o):  v.visitLastFormalParameter(self, o)
        def  acceptWithResult(self, v):  return v.visitLastFormalParameter(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLastFormalParameter(self, o)
    

'''/**
 *<em>
*<li>Rule 141:  MethodModifiers ::= MethodModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 142:  MethodModifiers ::= MethodModifiers MethodModifier
 *</b>
 */'''
class MethodModifiers ( Ast ,IMethodModifiers):
    

        def  getMethodModifiers(self)  :  return self._MethodModifiers
        def  setMethodModifiers(self,  _MethodModifiers) :   self._MethodModifiers = _MethodModifiers
        def  getMethodModifier(self)  :  return self._MethodModifier
        def  setMethodModifier(self,  _MethodModifier) :   self._MethodModifier = _MethodModifier

        __slots__ = ('_MethodModifiers', '_MethodModifier')

        def __init__(self, leftIToken, rightIToken,
                             _MethodModifiers,
                             _MethodModifier):
        
            super(MethodModifiers, self).__init__(leftIToken, rightIToken)

            self._MethodModifiers = _MethodModifiers
            _MethodModifiers.setParent(self)
            self._MethodModifier = _MethodModifier
            _MethodModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MethodModifiers:  _content.add(self._MethodModifiers)
            if self._MethodModifier:  _content.add(self._MethodModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 153:  Throws ::= throws ExceptionTypeList
 *</b>
 */'''
class Throws ( Ast ,IThrows):
    

        def  getthrows(self)  :  return self._throws
        def  setthrows(self,  _throws) :   self._throws = _throws
        def  getExceptionTypeList(self)  :  return self._ExceptionTypeList
        def  setExceptionTypeList(self,  _ExceptionTypeList) :   self._ExceptionTypeList = _ExceptionTypeList

        __slots__ = ('_throws', '_ExceptionTypeList')

        def __init__(self, leftIToken, rightIToken,
                             _throws,
                             _ExceptionTypeList):
        
            super(Throws, self).__init__(leftIToken, rightIToken)

            self._throws = _throws
            _throws.setParent(self)
            self._ExceptionTypeList = _ExceptionTypeList
            _ExceptionTypeList.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._throws:  _content.add(self._throws)
            if self._ExceptionTypeList:  _content.add(self._ExceptionTypeList)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitThrows(self)
        def  acceptWithArg(self, v, o):  v.visitThrows(self, o)
        def  acceptWithResult(self, v):  return v.visitThrows(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitThrows(self, o)
    

'''/**
 *<em>
*<li>Rule 154:  ExceptionTypeList ::= ExceptionType
 *</em>
 *<p>
 *<b>
*<li>Rule 155:  ExceptionTypeList ::= ExceptionTypeList , ExceptionType
 *</b>
 */'''
class ExceptionTypeList ( Ast ,IExceptionTypeList):
    

        def  getExceptionTypeList(self)  :  return self._ExceptionTypeList
        def  setExceptionTypeList(self,  _ExceptionTypeList) :   self._ExceptionTypeList = _ExceptionTypeList
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getExceptionType(self)  :  return self._ExceptionType
        def  setExceptionType(self,  _ExceptionType) :   self._ExceptionType = _ExceptionType

        __slots__ = ('_ExceptionTypeList', '_COMMA', '_ExceptionType')

        def __init__(self, leftIToken, rightIToken,
                             _ExceptionTypeList,
                             _COMMA,
                             _ExceptionType):
        
            super(ExceptionTypeList, self).__init__(leftIToken, rightIToken)

            self._ExceptionTypeList = _ExceptionTypeList
            _ExceptionTypeList.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._ExceptionType = _ExceptionType
            _ExceptionType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ExceptionTypeList:  _content.add(self._ExceptionTypeList)
            if self._COMMA:  _content.add(self._COMMA)
            if self._ExceptionType:  _content.add(self._ExceptionType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExceptionTypeList(self)
        def  acceptWithArg(self, v, o):  v.visitExceptionTypeList(self, o)
        def  acceptWithResult(self, v):  return v.visitExceptionTypeList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExceptionTypeList(self, o)
    

'''/**
 *<em>
*<li>Rule 158:  MethodBody ::= Block
 *</em>
 *<p>
 *<b>
*<li>Rule 159:  MethodBody ::= ;
 *</b>
 */'''
class MethodBody ( AstToken ,IMethodBody):
    
        def  getSEMICOLON(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodBody, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodBody(self)
        def  acceptWithArg(self, v, o):  v.visitMethodBody(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodBody(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodBody(self, o)
    

'''/**
 *<b>
*<li>Rule 161:  StaticInitializer ::= static Block
 *</b>
 */'''
class StaticInitializer ( Ast ,IStaticInitializer):
    

        def  getstatic(self)  :  return self._static
        def  setstatic(self,  _static) :   self._static = _static
        def  getBlock(self)  :  return self._Block
        def  setBlock(self,  _Block) :   self._Block = _Block

        __slots__ = ('_static', '_Block')

        def __init__(self, leftIToken, rightIToken,
                             _static,
                             _Block):
        
            super(StaticInitializer, self).__init__(leftIToken, rightIToken)

            self._static = _static
            _static.setParent(self)
            self._Block = _Block
            _Block.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._static:  _content.add(self._static)
            if self._Block:  _content.add(self._Block)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitStaticInitializer(self)
        def  acceptWithArg(self, v, o):  v.visitStaticInitializer(self, o)
        def  acceptWithResult(self, v):  return v.visitStaticInitializer(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitStaticInitializer(self, o)
    

'''/**
 *<b>
*<li>Rule 162:  ConstructorDeclaration ::= ConstructorModifiersopt ConstructorDeclarator Throwsopt ConstructorBody
 *</b>
 */'''
class ConstructorDeclaration ( Ast ,IConstructorDeclaration):
    

        '''/**
         * The value returned by <b>getConstructorModifiersopt</b> may be <b>null</b>
         */'''
        def  getConstructorModifiersopt(self)  :  return self._ConstructorModifiersopt
        def  setConstructorModifiersopt(self,  _ConstructorModifiersopt) :   self._ConstructorModifiersopt = _ConstructorModifiersopt
        def  getConstructorDeclarator(self)  :  return self._ConstructorDeclarator
        def  setConstructorDeclarator(self,  _ConstructorDeclarator) :   self._ConstructorDeclarator = _ConstructorDeclarator
        '''/**
         * The value returned by <b>getThrowsopt</b> may be <b>null</b>
         */'''
        def  getThrowsopt(self)  :  return self._Throwsopt
        def  setThrowsopt(self,  _Throwsopt) :   self._Throwsopt = _Throwsopt
        def  getConstructorBody(self)  :  return self._ConstructorBody
        def  setConstructorBody(self,  _ConstructorBody) :   self._ConstructorBody = _ConstructorBody

        __slots__ = ('_ConstructorModifiersopt', '_ConstructorDeclarator', '_Throwsopt', '_ConstructorBody')

        def __init__(self, leftIToken, rightIToken,
                             _ConstructorModifiersopt,
                             _ConstructorDeclarator,
                             _Throwsopt,
                             _ConstructorBody):
        
            super(ConstructorDeclaration, self).__init__(leftIToken, rightIToken)

            self._ConstructorModifiersopt = _ConstructorModifiersopt
            if _ConstructorModifiersopt: _ConstructorModifiersopt.setParent(self)
            self._ConstructorDeclarator = _ConstructorDeclarator
            _ConstructorDeclarator.setParent(self)
            self._Throwsopt = _Throwsopt
            if _Throwsopt: _Throwsopt.setParent(self)
            self._ConstructorBody = _ConstructorBody
            _ConstructorBody.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConstructorModifiersopt:  _content.add(self._ConstructorModifiersopt)
            if self._ConstructorDeclarator:  _content.add(self._ConstructorDeclarator)
            if self._Throwsopt:  _content.add(self._Throwsopt)
            if self._ConstructorBody:  _content.add(self._ConstructorBody)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConstructorDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 163:  ConstructorDeclarator ::= TypeParametersopt SimpleTypeName ( FormalParameterListopt )
 *</b>
 */'''
class ConstructorDeclarator ( Ast ,IConstructorDeclarator):
    

        '''/**
         * The value returned by <b>getTypeParametersopt</b> may be <b>null</b>
         */'''
        def  getTypeParametersopt(self)  :  return self._TypeParametersopt
        def  setTypeParametersopt(self,  _TypeParametersopt) :   self._TypeParametersopt = _TypeParametersopt
        def  getSimpleTypeName(self)  :  return self._SimpleTypeName
        def  setSimpleTypeName(self,  _SimpleTypeName) :   self._SimpleTypeName = _SimpleTypeName
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getFormalParameterListopt</b> may be <b>null</b>
         */'''
        def  getFormalParameterListopt(self)  :  return self._FormalParameterListopt
        def  setFormalParameterListopt(self,  _FormalParameterListopt) :   self._FormalParameterListopt = _FormalParameterListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_TypeParametersopt', '_SimpleTypeName', '_LPAREN', '_FormalParameterListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _TypeParametersopt,
                             _SimpleTypeName,
                             _LPAREN,
                             _FormalParameterListopt,
                             _RPAREN):
        
            super(ConstructorDeclarator, self).__init__(leftIToken, rightIToken)

            self._TypeParametersopt = _TypeParametersopt
            if _TypeParametersopt: _TypeParametersopt.setParent(self)
            self._SimpleTypeName = _SimpleTypeName
            _SimpleTypeName.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._FormalParameterListopt = _FormalParameterListopt
            if _FormalParameterListopt: _FormalParameterListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeParametersopt:  _content.add(self._TypeParametersopt)
            if self._SimpleTypeName:  _content.add(self._SimpleTypeName)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._FormalParameterListopt:  _content.add(self._FormalParameterListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConstructorDeclarator(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorDeclarator(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorDeclarator(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorDeclarator(self, o)
    

'''/**
 *<em>
*<li>Rule 165:  ConstructorModifiers ::= ConstructorModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 166:  ConstructorModifiers ::= ConstructorModifiers ConstructorModifier
 *</b>
 */'''
class ConstructorModifiers ( Ast ,IConstructorModifiers):
    

        def  getConstructorModifiers(self)  :  return self._ConstructorModifiers
        def  setConstructorModifiers(self,  _ConstructorModifiers) :   self._ConstructorModifiers = _ConstructorModifiers
        def  getConstructorModifier(self)  :  return self._ConstructorModifier
        def  setConstructorModifier(self,  _ConstructorModifier) :   self._ConstructorModifier = _ConstructorModifier

        __slots__ = ('_ConstructorModifiers', '_ConstructorModifier')

        def __init__(self, leftIToken, rightIToken,
                             _ConstructorModifiers,
                             _ConstructorModifier):
        
            super(ConstructorModifiers, self).__init__(leftIToken, rightIToken)

            self._ConstructorModifiers = _ConstructorModifiers
            _ConstructorModifiers.setParent(self)
            self._ConstructorModifier = _ConstructorModifier
            _ConstructorModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConstructorModifiers:  _content.add(self._ConstructorModifiers)
            if self._ConstructorModifier:  _content.add(self._ConstructorModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConstructorModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 171:  ConstructorBody ::= { ExplicitConstructorInvocationopt BlockStatementsopt }
 *</b>
 */'''
class ConstructorBody ( Ast ,IConstructorBody):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getExplicitConstructorInvocationopt</b> may be <b>null</b>
         */'''
        def  getExplicitConstructorInvocationopt(self)  :  return self._ExplicitConstructorInvocationopt
        def  setExplicitConstructorInvocationopt(self,  _ExplicitConstructorInvocationopt) :   self._ExplicitConstructorInvocationopt = _ExplicitConstructorInvocationopt
        '''/**
         * The value returned by <b>getBlockStatementsopt</b> may be <b>null</b>
         */'''
        def  getBlockStatementsopt(self)  :  return self._BlockStatementsopt
        def  setBlockStatementsopt(self,  _BlockStatementsopt) :   self._BlockStatementsopt = _BlockStatementsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_ExplicitConstructorInvocationopt', '_BlockStatementsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _ExplicitConstructorInvocationopt,
                             _BlockStatementsopt,
                             _RBRACE):
        
            super(ConstructorBody, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._ExplicitConstructorInvocationopt = _ExplicitConstructorInvocationopt
            if _ExplicitConstructorInvocationopt: _ExplicitConstructorInvocationopt.setParent(self)
            self._BlockStatementsopt = _BlockStatementsopt
            if _BlockStatementsopt: _BlockStatementsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._ExplicitConstructorInvocationopt:  _content.add(self._ExplicitConstructorInvocationopt)
            if self._BlockStatementsopt:  _content.add(self._BlockStatementsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConstructorBody(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorBody(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorBody(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorBody(self, o)
    

'''/**
 *<b>
*<li>Rule 175:  EnumDeclaration ::= ClassModifiersopt enum identifier Interfacesopt EnumBody
 *</b>
 */'''
class EnumDeclaration ( Ast ,IEnumDeclaration):
    

        '''/**
         * The value returned by <b>getClassModifiersopt</b> may be <b>null</b>
         */'''
        def  getClassModifiersopt(self)  :  return self._ClassModifiersopt
        def  setClassModifiersopt(self,  _ClassModifiersopt) :   self._ClassModifiersopt = _ClassModifiersopt
        def  getenum(self)  :  return self._enum
        def  setenum(self,  _enum) :   self._enum = _enum
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        '''/**
         * The value returned by <b>getInterfacesopt</b> may be <b>null</b>
         */'''
        def  getInterfacesopt(self)  :  return self._Interfacesopt
        def  setInterfacesopt(self,  _Interfacesopt) :   self._Interfacesopt = _Interfacesopt
        def  getEnumBody(self)  :  return self._EnumBody
        def  setEnumBody(self,  _EnumBody) :   self._EnumBody = _EnumBody

        __slots__ = ('_ClassModifiersopt', '_enum', '_identifier', '_Interfacesopt', '_EnumBody')

        def __init__(self, leftIToken, rightIToken,
                             _ClassModifiersopt,
                             _enum,
                             _identifier,
                             _Interfacesopt,
                             _EnumBody):
        
            super(EnumDeclaration, self).__init__(leftIToken, rightIToken)

            self._ClassModifiersopt = _ClassModifiersopt
            if _ClassModifiersopt: _ClassModifiersopt.setParent(self)
            self._enum = _enum
            _enum.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._Interfacesopt = _Interfacesopt
            if _Interfacesopt: _Interfacesopt.setParent(self)
            self._EnumBody = _EnumBody
            _EnumBody.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassModifiersopt:  _content.add(self._ClassModifiersopt)
            if self._enum:  _content.add(self._enum)
            if self._identifier:  _content.add(self._identifier)
            if self._Interfacesopt:  _content.add(self._Interfacesopt)
            if self._EnumBody:  _content.add(self._EnumBody)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEnumDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitEnumDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitEnumDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEnumDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 176:  EnumBody ::= { EnumConstantsopt ,opt EnumBodyDeclarationsopt }
 *</b>
 */'''
class EnumBody ( Ast ,IEnumBody):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getEnumConstantsopt</b> may be <b>null</b>
         */'''
        def  getEnumConstantsopt(self)  :  return self._EnumConstantsopt
        def  setEnumConstantsopt(self,  _EnumConstantsopt) :   self._EnumConstantsopt = _EnumConstantsopt
        '''/**
         * The value returned by <b>getCommaopt</b> may be <b>null</b>
         */'''
        def  getCommaopt(self)  :  return self._Commaopt
        def  setCommaopt(self,  _Commaopt) :   self._Commaopt = _Commaopt
        '''/**
         * The value returned by <b>getEnumBodyDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getEnumBodyDeclarationsopt(self)  :  return self._EnumBodyDeclarationsopt
        def  setEnumBodyDeclarationsopt(self,  _EnumBodyDeclarationsopt) :   self._EnumBodyDeclarationsopt = _EnumBodyDeclarationsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_EnumConstantsopt', '_Commaopt', '_EnumBodyDeclarationsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _EnumConstantsopt,
                             _Commaopt,
                             _EnumBodyDeclarationsopt,
                             _RBRACE):
        
            super(EnumBody, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._EnumConstantsopt = _EnumConstantsopt
            if _EnumConstantsopt: _EnumConstantsopt.setParent(self)
            self._Commaopt = _Commaopt
            if _Commaopt: _Commaopt.setParent(self)
            self._EnumBodyDeclarationsopt = _EnumBodyDeclarationsopt
            if _EnumBodyDeclarationsopt: _EnumBodyDeclarationsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._EnumConstantsopt:  _content.add(self._EnumConstantsopt)
            if self._Commaopt:  _content.add(self._Commaopt)
            if self._EnumBodyDeclarationsopt:  _content.add(self._EnumBodyDeclarationsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEnumBody(self)
        def  acceptWithArg(self, v, o):  v.visitEnumBody(self, o)
        def  acceptWithResult(self, v):  return v.visitEnumBody(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEnumBody(self, o)
    

'''/**
 *<em>
*<li>Rule 177:  EnumConstants ::= EnumConstant
 *</em>
 *<p>
 *<b>
*<li>Rule 178:  EnumConstants ::= EnumConstants , EnumConstant
 *</b>
 */'''
class EnumConstants ( Ast ,IEnumConstants):
    

        def  getEnumConstants(self)  :  return self._EnumConstants
        def  setEnumConstants(self,  _EnumConstants) :   self._EnumConstants = _EnumConstants
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getEnumConstant(self)  :  return self._EnumConstant
        def  setEnumConstant(self,  _EnumConstant) :   self._EnumConstant = _EnumConstant

        __slots__ = ('_EnumConstants', '_COMMA', '_EnumConstant')

        def __init__(self, leftIToken, rightIToken,
                             _EnumConstants,
                             _COMMA,
                             _EnumConstant):
        
            super(EnumConstants, self).__init__(leftIToken, rightIToken)

            self._EnumConstants = _EnumConstants
            _EnumConstants.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._EnumConstant = _EnumConstant
            _EnumConstant.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._EnumConstants:  _content.add(self._EnumConstants)
            if self._COMMA:  _content.add(self._COMMA)
            if self._EnumConstant:  _content.add(self._EnumConstant)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEnumConstants(self)
        def  acceptWithArg(self, v, o):  v.visitEnumConstants(self, o)
        def  acceptWithResult(self, v):  return v.visitEnumConstants(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEnumConstants(self, o)
    

'''/**
 *<em>
*<li>Rule 307:  EnumConstant ::= identifier
 *</em>
 *<p>
 *<b>
*<li>Rule 179:  EnumConstant ::= Annotationsopt identifier Argumentsopt ClassBodyopt
 *</b>
 */'''
class EnumConstant ( Ast ,IEnumConstant):
    

        '''/**
         * The value returned by <b>getAnnotationsopt</b> may be <b>null</b>
         */'''
        def  getAnnotationsopt(self)  :  return self._Annotationsopt
        def  setAnnotationsopt(self,  _Annotationsopt) :   self._Annotationsopt = _Annotationsopt
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        '''/**
         * The value returned by <b>getArgumentsopt</b> may be <b>null</b>
         */'''
        def  getArgumentsopt(self)  :  return self._Argumentsopt
        def  setArgumentsopt(self,  _Argumentsopt) :   self._Argumentsopt = _Argumentsopt
        '''/**
         * The value returned by <b>getClassBodyopt</b> may be <b>null</b>
         */'''
        def  getClassBodyopt(self)  :  return self._ClassBodyopt
        def  setClassBodyopt(self,  _ClassBodyopt) :   self._ClassBodyopt = _ClassBodyopt

        __slots__ = ('_Annotationsopt', '_identifier', '_Argumentsopt', '_ClassBodyopt')

        def __init__(self, leftIToken, rightIToken,
                             _Annotationsopt,
                             _identifier,
                             _Argumentsopt,
                             _ClassBodyopt):
        
            super(EnumConstant, self).__init__(leftIToken, rightIToken)

            self._Annotationsopt = _Annotationsopt
            if _Annotationsopt: _Annotationsopt.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._Argumentsopt = _Argumentsopt
            if _Argumentsopt: _Argumentsopt.setParent(self)
            self._ClassBodyopt = _ClassBodyopt
            if _ClassBodyopt: _ClassBodyopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Annotationsopt:  _content.add(self._Annotationsopt)
            if self._identifier:  _content.add(self._identifier)
            if self._Argumentsopt:  _content.add(self._Argumentsopt)
            if self._ClassBodyopt:  _content.add(self._ClassBodyopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEnumConstant(self)
        def  acceptWithArg(self, v, o):  v.visitEnumConstant(self, o)
        def  acceptWithResult(self, v):  return v.visitEnumConstant(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEnumConstant(self, o)
    

'''/**
 *<b>
*<li>Rule 180:  Arguments ::= ( ArgumentListopt )
 *</b>
 */'''
class Arguments ( Ast ,IArguments):
    

        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_LPAREN', '_ArgumentListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN):
        
            super(Arguments, self).__init__(leftIToken, rightIToken)

            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArguments(self)
        def  acceptWithArg(self, v, o):  v.visitArguments(self, o)
        def  acceptWithResult(self, v):  return v.visitArguments(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArguments(self, o)
    

'''/**
 *<b>
*<li>Rule 181:  EnumBodyDeclarations ::= ; ClassBodyDeclarationsopt
 *</b>
 */'''
class EnumBodyDeclarations ( Ast ,IEnumBodyDeclarations):
    

        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON
        '''/**
         * The value returned by <b>getClassBodyDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getClassBodyDeclarationsopt(self)  :  return self._ClassBodyDeclarationsopt
        def  setClassBodyDeclarationsopt(self,  _ClassBodyDeclarationsopt) :   self._ClassBodyDeclarationsopt = _ClassBodyDeclarationsopt

        __slots__ = ('_SEMICOLON', '_ClassBodyDeclarationsopt')

        def __init__(self, leftIToken, rightIToken,
                             _SEMICOLON,
                             _ClassBodyDeclarationsopt):
        
            super(EnumBodyDeclarations, self).__init__(leftIToken, rightIToken)

            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self._ClassBodyDeclarationsopt = _ClassBodyDeclarationsopt
            if _ClassBodyDeclarationsopt: _ClassBodyDeclarationsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            if self._ClassBodyDeclarationsopt:  _content.add(self._ClassBodyDeclarationsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEnumBodyDeclarations(self)
        def  acceptWithArg(self, v, o):  v.visitEnumBodyDeclarations(self, o)
        def  acceptWithResult(self, v):  return v.visitEnumBodyDeclarations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEnumBodyDeclarations(self, o)
    

'''/**
 *<b>
*<li>Rule 184:  NormalInterfaceDeclaration ::= InterfaceModifiersopt interface identifier TypeParametersopt ExtendsInterfacesopt InterfaceBody
 *</b>
 */'''
class NormalInterfaceDeclaration ( Ast ,INormalInterfaceDeclaration):
    

        '''/**
         * The value returned by <b>getInterfaceModifiersopt</b> may be <b>null</b>
         */'''
        def  getInterfaceModifiersopt(self)  :  return self._InterfaceModifiersopt
        def  setInterfaceModifiersopt(self,  _InterfaceModifiersopt) :   self._InterfaceModifiersopt = _InterfaceModifiersopt
        def  getinterface(self)  :  return self._interface
        def  setinterface(self,  _interface) :   self._interface = _interface
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        '''/**
         * The value returned by <b>getTypeParametersopt</b> may be <b>null</b>
         */'''
        def  getTypeParametersopt(self)  :  return self._TypeParametersopt
        def  setTypeParametersopt(self,  _TypeParametersopt) :   self._TypeParametersopt = _TypeParametersopt
        '''/**
         * The value returned by <b>getExtendsInterfacesopt</b> may be <b>null</b>
         */'''
        def  getExtendsInterfacesopt(self)  :  return self._ExtendsInterfacesopt
        def  setExtendsInterfacesopt(self,  _ExtendsInterfacesopt) :   self._ExtendsInterfacesopt = _ExtendsInterfacesopt
        def  getInterfaceBody(self)  :  return self._InterfaceBody
        def  setInterfaceBody(self,  _InterfaceBody) :   self._InterfaceBody = _InterfaceBody

        __slots__ = ('_InterfaceModifiersopt', '_interface', '_identifier', '_TypeParametersopt', '_ExtendsInterfacesopt', '_InterfaceBody')

        def __init__(self, leftIToken, rightIToken,
                             _InterfaceModifiersopt,
                             _interface,
                             _identifier,
                             _TypeParametersopt,
                             _ExtendsInterfacesopt,
                             _InterfaceBody):
        
            super(NormalInterfaceDeclaration, self).__init__(leftIToken, rightIToken)

            self._InterfaceModifiersopt = _InterfaceModifiersopt
            if _InterfaceModifiersopt: _InterfaceModifiersopt.setParent(self)
            self._interface = _interface
            _interface.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._TypeParametersopt = _TypeParametersopt
            if _TypeParametersopt: _TypeParametersopt.setParent(self)
            self._ExtendsInterfacesopt = _ExtendsInterfacesopt
            if _ExtendsInterfacesopt: _ExtendsInterfacesopt.setParent(self)
            self._InterfaceBody = _InterfaceBody
            _InterfaceBody.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._InterfaceModifiersopt:  _content.add(self._InterfaceModifiersopt)
            if self._interface:  _content.add(self._interface)
            if self._identifier:  _content.add(self._identifier)
            if self._TypeParametersopt:  _content.add(self._TypeParametersopt)
            if self._ExtendsInterfacesopt:  _content.add(self._ExtendsInterfacesopt)
            if self._InterfaceBody:  _content.add(self._InterfaceBody)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitNormalInterfaceDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitNormalInterfaceDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitNormalInterfaceDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitNormalInterfaceDeclaration(self, o)
    

'''/**
 *<em>
*<li>Rule 185:  InterfaceModifiers ::= InterfaceModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 186:  InterfaceModifiers ::= InterfaceModifiers InterfaceModifier
 *</b>
 */'''
class InterfaceModifiers ( Ast ,IInterfaceModifiers):
    

        def  getInterfaceModifiers(self)  :  return self._InterfaceModifiers
        def  setInterfaceModifiers(self,  _InterfaceModifiers) :   self._InterfaceModifiers = _InterfaceModifiers
        def  getInterfaceModifier(self)  :  return self._InterfaceModifier
        def  setInterfaceModifier(self,  _InterfaceModifier) :   self._InterfaceModifier = _InterfaceModifier

        __slots__ = ('_InterfaceModifiers', '_InterfaceModifier')

        def __init__(self, leftIToken, rightIToken,
                             _InterfaceModifiers,
                             _InterfaceModifier):
        
            super(InterfaceModifiers, self).__init__(leftIToken, rightIToken)

            self._InterfaceModifiers = _InterfaceModifiers
            _InterfaceModifiers.setParent(self)
            self._InterfaceModifier = _InterfaceModifier
            _InterfaceModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._InterfaceModifiers:  _content.add(self._InterfaceModifiers)
            if self._InterfaceModifier:  _content.add(self._InterfaceModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 196:  InterfaceBody ::= { InterfaceMemberDeclarationsopt }
 *</b>
 */'''
class InterfaceBody ( Ast ,IInterfaceBody):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getInterfaceMemberDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getInterfaceMemberDeclarationsopt(self)  :  return self._InterfaceMemberDeclarationsopt
        def  setInterfaceMemberDeclarationsopt(self,  _InterfaceMemberDeclarationsopt) :   self._InterfaceMemberDeclarationsopt = _InterfaceMemberDeclarationsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_InterfaceMemberDeclarationsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _InterfaceMemberDeclarationsopt,
                             _RBRACE):
        
            super(InterfaceBody, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._InterfaceMemberDeclarationsopt = _InterfaceMemberDeclarationsopt
            if _InterfaceMemberDeclarationsopt: _InterfaceMemberDeclarationsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._InterfaceMemberDeclarationsopt:  _content.add(self._InterfaceMemberDeclarationsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInterfaceBody(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceBody(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceBody(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceBody(self, o)
    

'''/**
 *<em>
*<li>Rule 197:  InterfaceMemberDeclarations ::= InterfaceMemberDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 198:  InterfaceMemberDeclarations ::= InterfaceMemberDeclarations InterfaceMemberDeclaration
 *</b>
 */'''
class InterfaceMemberDeclarations ( Ast ,IInterfaceMemberDeclarations):
    

        def  getInterfaceMemberDeclarations(self)  :  return self._InterfaceMemberDeclarations
        def  setInterfaceMemberDeclarations(self,  _InterfaceMemberDeclarations) :   self._InterfaceMemberDeclarations = _InterfaceMemberDeclarations
        def  getInterfaceMemberDeclaration(self)  :  return self._InterfaceMemberDeclaration
        def  setInterfaceMemberDeclaration(self,  _InterfaceMemberDeclaration) :   self._InterfaceMemberDeclaration = _InterfaceMemberDeclaration

        __slots__ = ('_InterfaceMemberDeclarations', '_InterfaceMemberDeclaration')

        def __init__(self, leftIToken, rightIToken,
                             _InterfaceMemberDeclarations,
                             _InterfaceMemberDeclaration):
        
            super(InterfaceMemberDeclarations, self).__init__(leftIToken, rightIToken)

            self._InterfaceMemberDeclarations = _InterfaceMemberDeclarations
            _InterfaceMemberDeclarations.setParent(self)
            self._InterfaceMemberDeclaration = _InterfaceMemberDeclaration
            _InterfaceMemberDeclaration.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._InterfaceMemberDeclarations:  _content.add(self._InterfaceMemberDeclarations)
            if self._InterfaceMemberDeclaration:  _content.add(self._InterfaceMemberDeclaration)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInterfaceMemberDeclarations(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceMemberDeclarations(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceMemberDeclarations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceMemberDeclarations(self, o)
    

'''/**
 *<em>
*<li>Rule 199:  InterfaceMemberDeclaration ::= ConstantDeclaration
*<li>Rule 200:  InterfaceMemberDeclaration ::= AbstractMethodDeclaration
*<li>Rule 201:  InterfaceMemberDeclaration ::= ClassDeclaration
*<li>Rule 202:  InterfaceMemberDeclaration ::= InterfaceDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 203:  InterfaceMemberDeclaration ::= ;
 *</b>
 */'''
class InterfaceMemberDeclaration ( AstToken ,IInterfaceMemberDeclaration):
    
        def  getSEMICOLON(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceMemberDeclaration, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceMemberDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceMemberDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceMemberDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceMemberDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 204:  ConstantDeclaration ::= ConstantModifiersopt Type VariableDeclarators
 *</b>
 */'''
class ConstantDeclaration ( Ast ,IConstantDeclaration):
    

        '''/**
         * The value returned by <b>getConstantModifiersopt</b> may be <b>null</b>
         */'''
        def  getConstantModifiersopt(self)  :  return self._ConstantModifiersopt
        def  setConstantModifiersopt(self,  _ConstantModifiersopt) :   self._ConstantModifiersopt = _ConstantModifiersopt
        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getVariableDeclarators(self)  :  return self._VariableDeclarators
        def  setVariableDeclarators(self,  _VariableDeclarators) :   self._VariableDeclarators = _VariableDeclarators

        __slots__ = ('_ConstantModifiersopt', '_Type', '_VariableDeclarators')

        def __init__(self, leftIToken, rightIToken,
                             _ConstantModifiersopt,
                             _Type,
                             _VariableDeclarators):
        
            super(ConstantDeclaration, self).__init__(leftIToken, rightIToken)

            self._ConstantModifiersopt = _ConstantModifiersopt
            if _ConstantModifiersopt: _ConstantModifiersopt.setParent(self)
            self._Type = _Type
            _Type.setParent(self)
            self._VariableDeclarators = _VariableDeclarators
            _VariableDeclarators.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConstantModifiersopt:  _content.add(self._ConstantModifiersopt)
            if self._Type:  _content.add(self._Type)
            if self._VariableDeclarators:  _content.add(self._VariableDeclarators)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConstantDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitConstantDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitConstantDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstantDeclaration(self, o)
    

'''/**
 *<em>
*<li>Rule 205:  ConstantModifiers ::= ConstantModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 206:  ConstantModifiers ::= ConstantModifiers ConstantModifier
 *</b>
 */'''
class ConstantModifiers ( Ast ,IConstantModifiers):
    

        def  getConstantModifiers(self)  :  return self._ConstantModifiers
        def  setConstantModifiers(self,  _ConstantModifiers) :   self._ConstantModifiers = _ConstantModifiers
        def  getConstantModifier(self)  :  return self._ConstantModifier
        def  setConstantModifier(self,  _ConstantModifier) :   self._ConstantModifier = _ConstantModifier

        __slots__ = ('_ConstantModifiers', '_ConstantModifier')

        def __init__(self, leftIToken, rightIToken,
                             _ConstantModifiers,
                             _ConstantModifier):
        
            super(ConstantModifiers, self).__init__(leftIToken, rightIToken)

            self._ConstantModifiers = _ConstantModifiers
            _ConstantModifiers.setParent(self)
            self._ConstantModifier = _ConstantModifier
            _ConstantModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConstantModifiers:  _content.add(self._ConstantModifiers)
            if self._ConstantModifier:  _content.add(self._ConstantModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConstantModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitConstantModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitConstantModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstantModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 211:  AbstractMethodDeclaration ::= AbstractMethodModifiersopt TypeParametersopt ResultType MethodDeclarator Throwsopt ;
 *</b>
 */'''
class AbstractMethodDeclaration ( Ast ,IAbstractMethodDeclaration):
    

        '''/**
         * The value returned by <b>getAbstractMethodModifiersopt</b> may be <b>null</b>
         */'''
        def  getAbstractMethodModifiersopt(self)  :  return self._AbstractMethodModifiersopt
        def  setAbstractMethodModifiersopt(self,  _AbstractMethodModifiersopt) :   self._AbstractMethodModifiersopt = _AbstractMethodModifiersopt
        '''/**
         * The value returned by <b>getTypeParametersopt</b> may be <b>null</b>
         */'''
        def  getTypeParametersopt(self)  :  return self._TypeParametersopt
        def  setTypeParametersopt(self,  _TypeParametersopt) :   self._TypeParametersopt = _TypeParametersopt
        def  getResultType(self)  :  return self._ResultType
        def  setResultType(self,  _ResultType) :   self._ResultType = _ResultType
        def  getMethodDeclarator(self)  :  return self._MethodDeclarator
        def  setMethodDeclarator(self,  _MethodDeclarator) :   self._MethodDeclarator = _MethodDeclarator
        '''/**
         * The value returned by <b>getThrowsopt</b> may be <b>null</b>
         */'''
        def  getThrowsopt(self)  :  return self._Throwsopt
        def  setThrowsopt(self,  _Throwsopt) :   self._Throwsopt = _Throwsopt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_AbstractMethodModifiersopt', '_TypeParametersopt', '_ResultType', '_MethodDeclarator', '_Throwsopt', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _AbstractMethodModifiersopt,
                             _TypeParametersopt,
                             _ResultType,
                             _MethodDeclarator,
                             _Throwsopt,
                             _SEMICOLON):
        
            super(AbstractMethodDeclaration, self).__init__(leftIToken, rightIToken)

            self._AbstractMethodModifiersopt = _AbstractMethodModifiersopt
            if _AbstractMethodModifiersopt: _AbstractMethodModifiersopt.setParent(self)
            self._TypeParametersopt = _TypeParametersopt
            if _TypeParametersopt: _TypeParametersopt.setParent(self)
            self._ResultType = _ResultType
            _ResultType.setParent(self)
            self._MethodDeclarator = _MethodDeclarator
            _MethodDeclarator.setParent(self)
            self._Throwsopt = _Throwsopt
            if _Throwsopt: _Throwsopt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AbstractMethodModifiersopt:  _content.add(self._AbstractMethodModifiersopt)
            if self._TypeParametersopt:  _content.add(self._TypeParametersopt)
            if self._ResultType:  _content.add(self._ResultType)
            if self._MethodDeclarator:  _content.add(self._MethodDeclarator)
            if self._Throwsopt:  _content.add(self._Throwsopt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAbstractMethodDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitAbstractMethodDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitAbstractMethodDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAbstractMethodDeclaration(self, o)
    

'''/**
 *<em>
*<li>Rule 212:  AbstractMethodModifiers ::= AbstractMethodModifier
 *</em>
 *<p>
 *<b>
*<li>Rule 213:  AbstractMethodModifiers ::= AbstractMethodModifiers AbstractMethodModifier
 *</b>
 */'''
class AbstractMethodModifiers ( Ast ,IAbstractMethodModifiers):
    

        def  getAbstractMethodModifiers(self)  :  return self._AbstractMethodModifiers
        def  setAbstractMethodModifiers(self,  _AbstractMethodModifiers) :   self._AbstractMethodModifiers = _AbstractMethodModifiers
        def  getAbstractMethodModifier(self)  :  return self._AbstractMethodModifier
        def  setAbstractMethodModifier(self,  _AbstractMethodModifier) :   self._AbstractMethodModifier = _AbstractMethodModifier

        __slots__ = ('_AbstractMethodModifiers', '_AbstractMethodModifier')

        def __init__(self, leftIToken, rightIToken,
                             _AbstractMethodModifiers,
                             _AbstractMethodModifier):
        
            super(AbstractMethodModifiers, self).__init__(leftIToken, rightIToken)

            self._AbstractMethodModifiers = _AbstractMethodModifiers
            _AbstractMethodModifiers.setParent(self)
            self._AbstractMethodModifier = _AbstractMethodModifier
            _AbstractMethodModifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AbstractMethodModifiers:  _content.add(self._AbstractMethodModifiers)
            if self._AbstractMethodModifier:  _content.add(self._AbstractMethodModifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAbstractMethodModifiers(self)
        def  acceptWithArg(self, v, o):  v.visitAbstractMethodModifiers(self, o)
        def  acceptWithResult(self, v):  return v.visitAbstractMethodModifiers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAbstractMethodModifiers(self, o)
    

'''/**
 *<b>
*<li>Rule 217:  AnnotationTypeDeclaration ::= InterfaceModifiersopt @ interface identifier AnnotationTypeBody
 *</b>
 */'''
class AnnotationTypeDeclaration ( Ast ,IAnnotationTypeDeclaration):
    

        '''/**
         * The value returned by <b>getInterfaceModifiersopt</b> may be <b>null</b>
         */'''
        def  getInterfaceModifiersopt(self)  :  return self._InterfaceModifiersopt
        def  setInterfaceModifiersopt(self,  _InterfaceModifiersopt) :   self._InterfaceModifiersopt = _InterfaceModifiersopt
        def  getAT(self)  :  return self._AT
        def  setAT(self,  _AT) :   self._AT = _AT
        def  getinterface(self)  :  return self._interface
        def  setinterface(self,  _interface) :   self._interface = _interface
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getAnnotationTypeBody(self)  :  return self._AnnotationTypeBody
        def  setAnnotationTypeBody(self,  _AnnotationTypeBody) :   self._AnnotationTypeBody = _AnnotationTypeBody

        __slots__ = ('_InterfaceModifiersopt', '_AT', '_interface', '_identifier', '_AnnotationTypeBody')

        def __init__(self, leftIToken, rightIToken,
                             _InterfaceModifiersopt,
                             _AT,
                             _interface,
                             _identifier,
                             _AnnotationTypeBody):
        
            super(AnnotationTypeDeclaration, self).__init__(leftIToken, rightIToken)

            self._InterfaceModifiersopt = _InterfaceModifiersopt
            if _InterfaceModifiersopt: _InterfaceModifiersopt.setParent(self)
            self._AT = _AT
            _AT.setParent(self)
            self._interface = _interface
            _interface.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._AnnotationTypeBody = _AnnotationTypeBody
            _AnnotationTypeBody.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._InterfaceModifiersopt:  _content.add(self._InterfaceModifiersopt)
            if self._AT:  _content.add(self._AT)
            if self._interface:  _content.add(self._interface)
            if self._identifier:  _content.add(self._identifier)
            if self._AnnotationTypeBody:  _content.add(self._AnnotationTypeBody)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAnnotationTypeDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitAnnotationTypeDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitAnnotationTypeDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAnnotationTypeDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 218:  AnnotationTypeBody ::= { AnnotationTypeElementDeclarationsopt }
 *</b>
 */'''
class AnnotationTypeBody ( Ast ,IAnnotationTypeBody):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getAnnotationTypeElementDeclarationsopt</b> may be <b>null</b>
         */'''
        def  getAnnotationTypeElementDeclarationsopt(self)  :  return self._AnnotationTypeElementDeclarationsopt
        def  setAnnotationTypeElementDeclarationsopt(self,  _AnnotationTypeElementDeclarationsopt) :   self._AnnotationTypeElementDeclarationsopt = _AnnotationTypeElementDeclarationsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_AnnotationTypeElementDeclarationsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _AnnotationTypeElementDeclarationsopt,
                             _RBRACE):
        
            super(AnnotationTypeBody, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._AnnotationTypeElementDeclarationsopt = _AnnotationTypeElementDeclarationsopt
            if _AnnotationTypeElementDeclarationsopt: _AnnotationTypeElementDeclarationsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._AnnotationTypeElementDeclarationsopt:  _content.add(self._AnnotationTypeElementDeclarationsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAnnotationTypeBody(self)
        def  acceptWithArg(self, v, o):  v.visitAnnotationTypeBody(self, o)
        def  acceptWithResult(self, v):  return v.visitAnnotationTypeBody(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAnnotationTypeBody(self, o)
    

'''/**
 *<em>
*<li>Rule 219:  AnnotationTypeElementDeclarations ::= AnnotationTypeElementDeclaration
 *</em>
 *<p>
 *<b>
*<li>Rule 220:  AnnotationTypeElementDeclarations ::= AnnotationTypeElementDeclarations AnnotationTypeElementDeclaration
 *</b>
 */'''
class AnnotationTypeElementDeclarations ( Ast ,IAnnotationTypeElementDeclarations):
    

        def  getAnnotationTypeElementDeclarations(self)  :  return self._AnnotationTypeElementDeclarations
        def  setAnnotationTypeElementDeclarations(self,  _AnnotationTypeElementDeclarations) :   self._AnnotationTypeElementDeclarations = _AnnotationTypeElementDeclarations
        def  getAnnotationTypeElementDeclaration(self)  :  return self._AnnotationTypeElementDeclaration
        def  setAnnotationTypeElementDeclaration(self,  _AnnotationTypeElementDeclaration) :   self._AnnotationTypeElementDeclaration = _AnnotationTypeElementDeclaration

        __slots__ = ('_AnnotationTypeElementDeclarations', '_AnnotationTypeElementDeclaration')

        def __init__(self, leftIToken, rightIToken,
                             _AnnotationTypeElementDeclarations,
                             _AnnotationTypeElementDeclaration):
        
            super(AnnotationTypeElementDeclarations, self).__init__(leftIToken, rightIToken)

            self._AnnotationTypeElementDeclarations = _AnnotationTypeElementDeclarations
            _AnnotationTypeElementDeclarations.setParent(self)
            self._AnnotationTypeElementDeclaration = _AnnotationTypeElementDeclaration
            _AnnotationTypeElementDeclaration.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AnnotationTypeElementDeclarations:  _content.add(self._AnnotationTypeElementDeclarations)
            if self._AnnotationTypeElementDeclaration:  _content.add(self._AnnotationTypeElementDeclaration)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAnnotationTypeElementDeclarations(self)
        def  acceptWithArg(self, v, o):  v.visitAnnotationTypeElementDeclarations(self, o)
        def  acceptWithResult(self, v):  return v.visitAnnotationTypeElementDeclarations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAnnotationTypeElementDeclarations(self, o)
    

'''/**
 *<b>
*<li>Rule 228:  DefaultValue ::= default ElementValue
 *</b>
 */'''
class DefaultValue ( Ast ,IDefaultValue):
    

        def  getdefault(self)  :  return self._default
        def  setdefault(self,  _default) :   self._default = _default
        def  getElementValue(self)  :  return self._ElementValue
        def  setElementValue(self,  _ElementValue) :   self._ElementValue = _ElementValue

        __slots__ = ('_default', '_ElementValue')

        def __init__(self, leftIToken, rightIToken,
                             _default,
                             _ElementValue):
        
            super(DefaultValue, self).__init__(leftIToken, rightIToken)

            self._default = _default
            _default.setParent(self)
            self._ElementValue = _ElementValue
            _ElementValue.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._default:  _content.add(self._default)
            if self._ElementValue:  _content.add(self._ElementValue)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitDefaultValue(self)
        def  acceptWithArg(self, v, o):  v.visitDefaultValue(self, o)
        def  acceptWithResult(self, v):  return v.visitDefaultValue(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitDefaultValue(self, o)
    

'''/**
 *<em>
*<li>Rule 229:  Annotations ::= Annotation
 *</em>
 *<p>
 *<b>
*<li>Rule 230:  Annotations ::= Annotations Annotation
 *</b>
 */'''
class Annotations ( Ast ,IAnnotations):
    

        def  getAnnotations(self)  :  return self._Annotations
        def  setAnnotations(self,  _Annotations) :   self._Annotations = _Annotations
        def  getAnnotation(self)  :  return self._Annotation
        def  setAnnotation(self,  _Annotation) :   self._Annotation = _Annotation

        __slots__ = ('_Annotations', '_Annotation')

        def __init__(self, leftIToken, rightIToken,
                             _Annotations,
                             _Annotation):
        
            super(Annotations, self).__init__(leftIToken, rightIToken)

            self._Annotations = _Annotations
            _Annotations.setParent(self)
            self._Annotation = _Annotation
            _Annotation.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Annotations:  _content.add(self._Annotations)
            if self._Annotation:  _content.add(self._Annotation)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAnnotations(self)
        def  acceptWithArg(self, v, o):  v.visitAnnotations(self, o)
        def  acceptWithResult(self, v):  return v.visitAnnotations(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAnnotations(self, o)
    

'''/**
 *<b>
*<li>Rule 234:  NormalAnnotation ::= @ TypeName ( ElementValuePairsopt )
 *</b>
 */'''
class NormalAnnotation ( Ast ,INormalAnnotation):
    

        def  getAT(self)  :  return self._AT
        def  setAT(self,  _AT) :   self._AT = _AT
        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getElementValuePairsopt</b> may be <b>null</b>
         */'''
        def  getElementValuePairsopt(self)  :  return self._ElementValuePairsopt
        def  setElementValuePairsopt(self,  _ElementValuePairsopt) :   self._ElementValuePairsopt = _ElementValuePairsopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_AT', '_TypeName', '_LPAREN', '_ElementValuePairsopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _AT,
                             _TypeName,
                             _LPAREN,
                             _ElementValuePairsopt,
                             _RPAREN):
        
            super(NormalAnnotation, self).__init__(leftIToken, rightIToken)

            self._AT = _AT
            _AT.setParent(self)
            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ElementValuePairsopt = _ElementValuePairsopt
            if _ElementValuePairsopt: _ElementValuePairsopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AT:  _content.add(self._AT)
            if self._TypeName:  _content.add(self._TypeName)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ElementValuePairsopt:  _content.add(self._ElementValuePairsopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitNormalAnnotation(self)
        def  acceptWithArg(self, v, o):  v.visitNormalAnnotation(self, o)
        def  acceptWithResult(self, v):  return v.visitNormalAnnotation(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitNormalAnnotation(self, o)
    

'''/**
 *<em>
*<li>Rule 235:  ElementValuePairs ::= ElementValuePair
 *</em>
 *<p>
 *<b>
*<li>Rule 236:  ElementValuePairs ::= ElementValuePairs , ElementValuePair
 *</b>
 */'''
class ElementValuePairs ( Ast ,IElementValuePairs):
    

        def  getElementValuePairs(self)  :  return self._ElementValuePairs
        def  setElementValuePairs(self,  _ElementValuePairs) :   self._ElementValuePairs = _ElementValuePairs
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getElementValuePair(self)  :  return self._ElementValuePair
        def  setElementValuePair(self,  _ElementValuePair) :   self._ElementValuePair = _ElementValuePair

        __slots__ = ('_ElementValuePairs', '_COMMA', '_ElementValuePair')

        def __init__(self, leftIToken, rightIToken,
                             _ElementValuePairs,
                             _COMMA,
                             _ElementValuePair):
        
            super(ElementValuePairs, self).__init__(leftIToken, rightIToken)

            self._ElementValuePairs = _ElementValuePairs
            _ElementValuePairs.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._ElementValuePair = _ElementValuePair
            _ElementValuePair.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ElementValuePairs:  _content.add(self._ElementValuePairs)
            if self._COMMA:  _content.add(self._COMMA)
            if self._ElementValuePair:  _content.add(self._ElementValuePair)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitElementValuePairs(self)
        def  acceptWithArg(self, v, o):  v.visitElementValuePairs(self, o)
        def  acceptWithResult(self, v):  return v.visitElementValuePairs(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitElementValuePairs(self, o)
    

'''/**
 *<b>
*<li>Rule 237:  ElementValuePair ::= SimpleName = ElementValue
 *</b>
 */'''
class ElementValuePair ( Ast ,IElementValuePair):
    

        def  getSimpleName(self)  :  return self._SimpleName
        def  setSimpleName(self,  _SimpleName) :   self._SimpleName = _SimpleName
        def  getEQUAL(self)  :  return self._EQUAL
        def  setEQUAL(self,  _EQUAL) :   self._EQUAL = _EQUAL
        def  getElementValue(self)  :  return self._ElementValue
        def  setElementValue(self,  _ElementValue) :   self._ElementValue = _ElementValue

        __slots__ = ('_SimpleName', '_EQUAL', '_ElementValue')

        def __init__(self, leftIToken, rightIToken,
                             _SimpleName,
                             _EQUAL,
                             _ElementValue):
        
            super(ElementValuePair, self).__init__(leftIToken, rightIToken)

            self._SimpleName = _SimpleName
            _SimpleName.setParent(self)
            self._EQUAL = _EQUAL
            _EQUAL.setParent(self)
            self._ElementValue = _ElementValue
            _ElementValue.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SimpleName:  _content.add(self._SimpleName)
            if self._EQUAL:  _content.add(self._EQUAL)
            if self._ElementValue:  _content.add(self._ElementValue)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitElementValuePair(self)
        def  acceptWithArg(self, v, o):  v.visitElementValuePair(self, o)
        def  acceptWithResult(self, v):  return v.visitElementValuePair(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitElementValuePair(self, o)
    

'''/**
 *<b>
*<li>Rule 242:  ElementValueArrayInitializer ::= { ElementValuesopt ,opt }
 *</b>
 */'''
class ElementValueArrayInitializer ( Ast ,IElementValueArrayInitializer):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getElementValuesopt</b> may be <b>null</b>
         */'''
        def  getElementValuesopt(self)  :  return self._ElementValuesopt
        def  setElementValuesopt(self,  _ElementValuesopt) :   self._ElementValuesopt = _ElementValuesopt
        '''/**
         * The value returned by <b>getCommaopt</b> may be <b>null</b>
         */'''
        def  getCommaopt(self)  :  return self._Commaopt
        def  setCommaopt(self,  _Commaopt) :   self._Commaopt = _Commaopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_ElementValuesopt', '_Commaopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _ElementValuesopt,
                             _Commaopt,
                             _RBRACE):
        
            super(ElementValueArrayInitializer, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._ElementValuesopt = _ElementValuesopt
            if _ElementValuesopt: _ElementValuesopt.setParent(self)
            self._Commaopt = _Commaopt
            if _Commaopt: _Commaopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._ElementValuesopt:  _content.add(self._ElementValuesopt)
            if self._Commaopt:  _content.add(self._Commaopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitElementValueArrayInitializer(self)
        def  acceptWithArg(self, v, o):  v.visitElementValueArrayInitializer(self, o)
        def  acceptWithResult(self, v):  return v.visitElementValueArrayInitializer(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitElementValueArrayInitializer(self, o)
    

'''/**
 *<em>
*<li>Rule 243:  ElementValues ::= ElementValue
 *</em>
 *<p>
 *<b>
*<li>Rule 244:  ElementValues ::= ElementValues , ElementValue
 *</b>
 */'''
class ElementValues ( Ast ,IElementValues):
    

        def  getElementValues(self)  :  return self._ElementValues
        def  setElementValues(self,  _ElementValues) :   self._ElementValues = _ElementValues
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getElementValue(self)  :  return self._ElementValue
        def  setElementValue(self,  _ElementValue) :   self._ElementValue = _ElementValue

        __slots__ = ('_ElementValues', '_COMMA', '_ElementValue')

        def __init__(self, leftIToken, rightIToken,
                             _ElementValues,
                             _COMMA,
                             _ElementValue):
        
            super(ElementValues, self).__init__(leftIToken, rightIToken)

            self._ElementValues = _ElementValues
            _ElementValues.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._ElementValue = _ElementValue
            _ElementValue.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ElementValues:  _content.add(self._ElementValues)
            if self._COMMA:  _content.add(self._COMMA)
            if self._ElementValue:  _content.add(self._ElementValue)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitElementValues(self)
        def  acceptWithArg(self, v, o):  v.visitElementValues(self, o)
        def  acceptWithResult(self, v):  return v.visitElementValues(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitElementValues(self, o)
    

'''/**
 *<b>
*<li>Rule 245:  MarkerAnnotation ::= @ TypeName
 *</b>
 */'''
class MarkerAnnotation ( Ast ,IMarkerAnnotation):
    

        def  getAT(self)  :  return self._AT
        def  setAT(self,  _AT) :   self._AT = _AT
        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName

        __slots__ = ('_AT', '_TypeName')

        def __init__(self, leftIToken, rightIToken,
                             _AT,
                             _TypeName):
        
            super(MarkerAnnotation, self).__init__(leftIToken, rightIToken)

            self._AT = _AT
            _AT.setParent(self)
            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AT:  _content.add(self._AT)
            if self._TypeName:  _content.add(self._TypeName)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMarkerAnnotation(self)
        def  acceptWithArg(self, v, o):  v.visitMarkerAnnotation(self, o)
        def  acceptWithResult(self, v):  return v.visitMarkerAnnotation(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMarkerAnnotation(self, o)
    

'''/**
 *<b>
*<li>Rule 246:  SingleElementAnnotation ::= @ TypeName ( ElementValue )
 *</b>
 */'''
class SingleElementAnnotation ( Ast ,ISingleElementAnnotation):
    

        def  getAT(self)  :  return self._AT
        def  setAT(self,  _AT) :   self._AT = _AT
        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getElementValue(self)  :  return self._ElementValue
        def  setElementValue(self,  _ElementValue) :   self._ElementValue = _ElementValue
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_AT', '_TypeName', '_LPAREN', '_ElementValue', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _AT,
                             _TypeName,
                             _LPAREN,
                             _ElementValue,
                             _RPAREN):
        
            super(SingleElementAnnotation, self).__init__(leftIToken, rightIToken)

            self._AT = _AT
            _AT.setParent(self)
            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ElementValue = _ElementValue
            _ElementValue.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AT:  _content.add(self._AT)
            if self._TypeName:  _content.add(self._TypeName)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ElementValue:  _content.add(self._ElementValue)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSingleElementAnnotation(self)
        def  acceptWithArg(self, v, o):  v.visitSingleElementAnnotation(self, o)
        def  acceptWithResult(self, v):  return v.visitSingleElementAnnotation(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSingleElementAnnotation(self, o)
    

'''/**
 *<b>
*<li>Rule 247:  ArrayInitializer ::= { VariableInitializersopt ,opt }
 *</b>
 */'''
class ArrayInitializer ( Ast ,IArrayInitializer):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getVariableInitializersopt</b> may be <b>null</b>
         */'''
        def  getVariableInitializersopt(self)  :  return self._VariableInitializersopt
        def  setVariableInitializersopt(self,  _VariableInitializersopt) :   self._VariableInitializersopt = _VariableInitializersopt
        '''/**
         * The value returned by <b>getCommaopt</b> may be <b>null</b>
         */'''
        def  getCommaopt(self)  :  return self._Commaopt
        def  setCommaopt(self,  _Commaopt) :   self._Commaopt = _Commaopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_VariableInitializersopt', '_Commaopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _VariableInitializersopt,
                             _Commaopt,
                             _RBRACE):
        
            super(ArrayInitializer, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._VariableInitializersopt = _VariableInitializersopt
            if _VariableInitializersopt: _VariableInitializersopt.setParent(self)
            self._Commaopt = _Commaopt
            if _Commaopt: _Commaopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._VariableInitializersopt:  _content.add(self._VariableInitializersopt)
            if self._Commaopt:  _content.add(self._Commaopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayInitializer(self)
        def  acceptWithArg(self, v, o):  v.visitArrayInitializer(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayInitializer(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayInitializer(self, o)
    

'''/**
 *<em>
*<li>Rule 248:  VariableInitializers ::= VariableInitializer
 *</em>
 *<p>
 *<b>
*<li>Rule 249:  VariableInitializers ::= VariableInitializers , VariableInitializer
 *</b>
 */'''
class VariableInitializers ( Ast ,IVariableInitializers):
    

        def  getVariableInitializers(self)  :  return self._VariableInitializers
        def  setVariableInitializers(self,  _VariableInitializers) :   self._VariableInitializers = _VariableInitializers
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getVariableInitializer(self)  :  return self._VariableInitializer
        def  setVariableInitializer(self,  _VariableInitializer) :   self._VariableInitializer = _VariableInitializer

        __slots__ = ('_VariableInitializers', '_COMMA', '_VariableInitializer')

        def __init__(self, leftIToken, rightIToken,
                             _VariableInitializers,
                             _COMMA,
                             _VariableInitializer):
        
            super(VariableInitializers, self).__init__(leftIToken, rightIToken)

            self._VariableInitializers = _VariableInitializers
            _VariableInitializers.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._VariableInitializer = _VariableInitializer
            _VariableInitializer.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableInitializers:  _content.add(self._VariableInitializers)
            if self._COMMA:  _content.add(self._COMMA)
            if self._VariableInitializer:  _content.add(self._VariableInitializer)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitVariableInitializers(self)
        def  acceptWithArg(self, v, o):  v.visitVariableInitializers(self, o)
        def  acceptWithResult(self, v):  return v.visitVariableInitializers(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitVariableInitializers(self, o)
    

'''/**
 *<b>
*<li>Rule 250:  Block ::= { BlockStatementsopt }
 *</b>
 */'''
class Block ( Ast ,IBlock):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getBlockStatementsopt</b> may be <b>null</b>
         */'''
        def  getBlockStatementsopt(self)  :  return self._BlockStatementsopt
        def  setBlockStatementsopt(self,  _BlockStatementsopt) :   self._BlockStatementsopt = _BlockStatementsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_BlockStatementsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _BlockStatementsopt,
                             _RBRACE):
        
            super(Block, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._BlockStatementsopt = _BlockStatementsopt
            if _BlockStatementsopt: _BlockStatementsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._BlockStatementsopt:  _content.add(self._BlockStatementsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitBlock(self)
        def  acceptWithArg(self, v, o):  v.visitBlock(self, o)
        def  acceptWithResult(self, v):  return v.visitBlock(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitBlock(self, o)
    

'''/**
 *<em>
*<li>Rule 251:  BlockStatements ::= BlockStatement
 *</em>
 *<p>
 *<b>
*<li>Rule 252:  BlockStatements ::= BlockStatements BlockStatement
 *</b>
 */'''
class BlockStatements ( Ast ,IBlockStatements):
    

        def  getBlockStatements(self)  :  return self._BlockStatements
        def  setBlockStatements(self,  _BlockStatements) :   self._BlockStatements = _BlockStatements
        def  getBlockStatement(self)  :  return self._BlockStatement
        def  setBlockStatement(self,  _BlockStatement) :   self._BlockStatement = _BlockStatement

        __slots__ = ('_BlockStatements', '_BlockStatement')

        def __init__(self, leftIToken, rightIToken,
                             _BlockStatements,
                             _BlockStatement):
        
            super(BlockStatements, self).__init__(leftIToken, rightIToken)

            self._BlockStatements = _BlockStatements
            _BlockStatements.setParent(self)
            self._BlockStatement = _BlockStatement
            _BlockStatement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._BlockStatements:  _content.add(self._BlockStatements)
            if self._BlockStatement:  _content.add(self._BlockStatement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitBlockStatements(self)
        def  acceptWithArg(self, v, o):  v.visitBlockStatements(self, o)
        def  acceptWithResult(self, v):  return v.visitBlockStatements(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitBlockStatements(self, o)
    

'''/**
 *<b>
*<li>Rule 256:  LocalVariableDeclarationStatement ::= LocalVariableDeclaration ;
 *</b>
 */'''
class LocalVariableDeclarationStatement ( Ast ,ILocalVariableDeclarationStatement):
    

        def  getLocalVariableDeclaration(self)  :  return self._LocalVariableDeclaration
        def  setLocalVariableDeclaration(self,  _LocalVariableDeclaration) :   self._LocalVariableDeclaration = _LocalVariableDeclaration
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_LocalVariableDeclaration', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _LocalVariableDeclaration,
                             _SEMICOLON):
        
            super(LocalVariableDeclarationStatement, self).__init__(leftIToken, rightIToken)

            self._LocalVariableDeclaration = _LocalVariableDeclaration
            _LocalVariableDeclaration.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LocalVariableDeclaration:  _content.add(self._LocalVariableDeclaration)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLocalVariableDeclarationStatement(self)
        def  acceptWithArg(self, v, o):  v.visitLocalVariableDeclarationStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitLocalVariableDeclarationStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLocalVariableDeclarationStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 257:  LocalVariableDeclaration ::= VariableModifiersopt Type VariableDeclarators
 *</b>
 */'''
class LocalVariableDeclaration ( Ast ,ILocalVariableDeclaration):
    

        '''/**
         * The value returned by <b>getVariableModifiersopt</b> may be <b>null</b>
         */'''
        def  getVariableModifiersopt(self)  :  return self._VariableModifiersopt
        def  setVariableModifiersopt(self,  _VariableModifiersopt) :   self._VariableModifiersopt = _VariableModifiersopt
        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getVariableDeclarators(self)  :  return self._VariableDeclarators
        def  setVariableDeclarators(self,  _VariableDeclarators) :   self._VariableDeclarators = _VariableDeclarators

        __slots__ = ('_VariableModifiersopt', '_Type', '_VariableDeclarators')

        def __init__(self, leftIToken, rightIToken,
                             _VariableModifiersopt,
                             _Type,
                             _VariableDeclarators):
        
            super(LocalVariableDeclaration, self).__init__(leftIToken, rightIToken)

            self._VariableModifiersopt = _VariableModifiersopt
            if _VariableModifiersopt: _VariableModifiersopt.setParent(self)
            self._Type = _Type
            _Type.setParent(self)
            self._VariableDeclarators = _VariableDeclarators
            _VariableDeclarators.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._VariableModifiersopt:  _content.add(self._VariableModifiersopt)
            if self._Type:  _content.add(self._Type)
            if self._VariableDeclarators:  _content.add(self._VariableDeclarators)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLocalVariableDeclaration(self)
        def  acceptWithArg(self, v, o):  v.visitLocalVariableDeclaration(self, o)
        def  acceptWithResult(self, v):  return v.visitLocalVariableDeclaration(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLocalVariableDeclaration(self, o)
    

'''/**
 *<b>
*<li>Rule 281:  IfThenStatement ::= if ( Expression ) Statement
 *</b>
 */'''
class IfThenStatement ( Ast ,IIfThenStatement):
    

        def  getif(self)  :  return self._if
        def  setif(self,  _if) :   self._if = _if
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement

        __slots__ = ('_if', '_LPAREN', '_Expression', '_RPAREN', '_Statement')

        def __init__(self, leftIToken, rightIToken,
                             _if,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _Statement):
        
            super(IfThenStatement, self).__init__(leftIToken, rightIToken)

            self._if = _if
            _if.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._if:  _content.add(self._if)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._Statement:  _content.add(self._Statement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitIfThenStatement(self)
        def  acceptWithArg(self, v, o):  v.visitIfThenStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitIfThenStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIfThenStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 282:  IfThenElseStatement ::= if ( Expression ) StatementNoShortIf else Statement
 *</b>
 */'''
class IfThenElseStatement ( Ast ,IIfThenElseStatement):
    

        def  getif(self)  :  return self._if
        def  setif(self,  _if) :   self._if = _if
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatementNoShortIf(self)  :  return self._StatementNoShortIf
        def  setStatementNoShortIf(self,  _StatementNoShortIf) :   self._StatementNoShortIf = _StatementNoShortIf
        def  getelse(self)  :  return self._else
        def  setelse(self,  _else) :   self._else = _else
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement

        __slots__ = ('_if', '_LPAREN', '_Expression', '_RPAREN', '_StatementNoShortIf', '_else', '_Statement')

        def __init__(self, leftIToken, rightIToken,
                             _if,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _StatementNoShortIf,
                             _else,
                             _Statement):
        
            super(IfThenElseStatement, self).__init__(leftIToken, rightIToken)

            self._if = _if
            _if.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._StatementNoShortIf = _StatementNoShortIf
            _StatementNoShortIf.setParent(self)
            self._else = _else
            _else.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._if:  _content.add(self._if)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._StatementNoShortIf:  _content.add(self._StatementNoShortIf)
            if self._else:  _content.add(self._else)
            if self._Statement:  _content.add(self._Statement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitIfThenElseStatement(self)
        def  acceptWithArg(self, v, o):  v.visitIfThenElseStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitIfThenElseStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIfThenElseStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 283:  IfThenElseStatementNoShortIf ::= if ( Expression ) StatementNoShortIf else StatementNoShortIf
 *</b>
 */'''
class IfThenElseStatementNoShortIf ( Ast ,IIfThenElseStatementNoShortIf):
    

        def  getif(self)  :  return self._if
        def  setif(self,  _if) :   self._if = _if
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatementNoShortIf(self)  :  return self._StatementNoShortIf
        def  setStatementNoShortIf(self,  _StatementNoShortIf) :   self._StatementNoShortIf = _StatementNoShortIf
        def  getelse(self)  :  return self._else
        def  setelse(self,  _else) :   self._else = _else
        def  getStatementNoShortIf7(self)  :  return self._StatementNoShortIf7
        def  setStatementNoShortIf7(self,  _StatementNoShortIf7) :   self._StatementNoShortIf7 = _StatementNoShortIf7

        __slots__ = ('_if', '_LPAREN', '_Expression', '_RPAREN', '_StatementNoShortIf', '_else', '_StatementNoShortIf7')

        def __init__(self, leftIToken, rightIToken,
                             _if,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _StatementNoShortIf,
                             _else,
                             _StatementNoShortIf7):
        
            super(IfThenElseStatementNoShortIf, self).__init__(leftIToken, rightIToken)

            self._if = _if
            _if.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._StatementNoShortIf = _StatementNoShortIf
            _StatementNoShortIf.setParent(self)
            self._else = _else
            _else.setParent(self)
            self._StatementNoShortIf7 = _StatementNoShortIf7
            _StatementNoShortIf7.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._if:  _content.add(self._if)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._StatementNoShortIf:  _content.add(self._StatementNoShortIf)
            if self._else:  _content.add(self._else)
            if self._StatementNoShortIf7:  _content.add(self._StatementNoShortIf7)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitIfThenElseStatementNoShortIf(self)
        def  acceptWithArg(self, v, o):  v.visitIfThenElseStatementNoShortIf(self, o)
        def  acceptWithResult(self, v):  return v.visitIfThenElseStatementNoShortIf(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIfThenElseStatementNoShortIf(self, o)
    

'''/**
 *<b>
*<li>Rule 284:  EmptyStatement ::= ;
 *</b>
 */'''
class EmptyStatement ( AstToken ,IEmptyStatement):
    
        def  getSEMICOLON(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(EmptyStatement, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitEmptyStatement(self)
        def  acceptWithArg(self, v, o):  v.visitEmptyStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitEmptyStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEmptyStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 285:  LabeledStatement ::= identifier : Statement
 *</b>
 */'''
class LabeledStatement ( Ast ,ILabeledStatement):
    

        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement

        __slots__ = ('_identifier', '_COLON', '_Statement')

        def __init__(self, leftIToken, rightIToken,
                             _identifier,
                             _COLON,
                             _Statement):
        
            super(LabeledStatement, self).__init__(leftIToken, rightIToken)

            self._identifier = _identifier
            _identifier.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._identifier:  _content.add(self._identifier)
            if self._COLON:  _content.add(self._COLON)
            if self._Statement:  _content.add(self._Statement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLabeledStatement(self)
        def  acceptWithArg(self, v, o):  v.visitLabeledStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitLabeledStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLabeledStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 286:  LabeledStatementNoShortIf ::= identifier : StatementNoShortIf
 *</b>
 */'''
class LabeledStatementNoShortIf ( Ast ,ILabeledStatementNoShortIf):
    

        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON
        def  getStatementNoShortIf(self)  :  return self._StatementNoShortIf
        def  setStatementNoShortIf(self,  _StatementNoShortIf) :   self._StatementNoShortIf = _StatementNoShortIf

        __slots__ = ('_identifier', '_COLON', '_StatementNoShortIf')

        def __init__(self, leftIToken, rightIToken,
                             _identifier,
                             _COLON,
                             _StatementNoShortIf):
        
            super(LabeledStatementNoShortIf, self).__init__(leftIToken, rightIToken)

            self._identifier = _identifier
            _identifier.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self._StatementNoShortIf = _StatementNoShortIf
            _StatementNoShortIf.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._identifier:  _content.add(self._identifier)
            if self._COLON:  _content.add(self._COLON)
            if self._StatementNoShortIf:  _content.add(self._StatementNoShortIf)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLabeledStatementNoShortIf(self)
        def  acceptWithArg(self, v, o):  v.visitLabeledStatementNoShortIf(self, o)
        def  acceptWithResult(self, v):  return v.visitLabeledStatementNoShortIf(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLabeledStatementNoShortIf(self, o)
    

'''/**
 *<b>
*<li>Rule 287:  ExpressionStatement ::= StatementExpression ;
 *</b>
 */'''
class ExpressionStatement ( Ast ,IExpressionStatement):
    

        def  getStatementExpression(self)  :  return self._StatementExpression
        def  setStatementExpression(self,  _StatementExpression) :   self._StatementExpression = _StatementExpression
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_StatementExpression', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _StatementExpression,
                             _SEMICOLON):
        
            super(ExpressionStatement, self).__init__(leftIToken, rightIToken)

            self._StatementExpression = _StatementExpression
            _StatementExpression.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._StatementExpression:  _content.add(self._StatementExpression)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExpressionStatement(self)
        def  acceptWithArg(self, v, o):  v.visitExpressionStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitExpressionStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExpressionStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 297:  SwitchStatement ::= switch ( Expression ) SwitchBlock
 *</b>
 */'''
class SwitchStatement ( Ast ,ISwitchStatement):
    

        def  getswitch(self)  :  return self._switch
        def  setswitch(self,  _switch) :   self._switch = _switch
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getSwitchBlock(self)  :  return self._SwitchBlock
        def  setSwitchBlock(self,  _SwitchBlock) :   self._SwitchBlock = _SwitchBlock

        __slots__ = ('_switch', '_LPAREN', '_Expression', '_RPAREN', '_SwitchBlock')

        def __init__(self, leftIToken, rightIToken,
                             _switch,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _SwitchBlock):
        
            super(SwitchStatement, self).__init__(leftIToken, rightIToken)

            self._switch = _switch
            _switch.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._SwitchBlock = _SwitchBlock
            _SwitchBlock.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._switch:  _content.add(self._switch)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._SwitchBlock:  _content.add(self._SwitchBlock)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchStatement(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 298:  SwitchBlock ::= { SwitchBlockStatementGroupsopt SwitchLabelsopt }
 *</b>
 */'''
class SwitchBlock ( Ast ,ISwitchBlock):
    

        def  getLBRACE(self)  :  return self._LBRACE
        def  setLBRACE(self,  _LBRACE) :   self._LBRACE = _LBRACE
        '''/**
         * The value returned by <b>getSwitchBlockStatementGroupsopt</b> may be <b>null</b>
         */'''
        def  getSwitchBlockStatementGroupsopt(self)  :  return self._SwitchBlockStatementGroupsopt
        def  setSwitchBlockStatementGroupsopt(self,  _SwitchBlockStatementGroupsopt) :   self._SwitchBlockStatementGroupsopt = _SwitchBlockStatementGroupsopt
        '''/**
         * The value returned by <b>getSwitchLabelsopt</b> may be <b>null</b>
         */'''
        def  getSwitchLabelsopt(self)  :  return self._SwitchLabelsopt
        def  setSwitchLabelsopt(self,  _SwitchLabelsopt) :   self._SwitchLabelsopt = _SwitchLabelsopt
        def  getRBRACE(self)  :  return self._RBRACE
        def  setRBRACE(self,  _RBRACE) :   self._RBRACE = _RBRACE

        __slots__ = ('_LBRACE', '_SwitchBlockStatementGroupsopt', '_SwitchLabelsopt', '_RBRACE')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACE,
                             _SwitchBlockStatementGroupsopt,
                             _SwitchLabelsopt,
                             _RBRACE):
        
            super(SwitchBlock, self).__init__(leftIToken, rightIToken)

            self._LBRACE = _LBRACE
            _LBRACE.setParent(self)
            self._SwitchBlockStatementGroupsopt = _SwitchBlockStatementGroupsopt
            if _SwitchBlockStatementGroupsopt: _SwitchBlockStatementGroupsopt.setParent(self)
            self._SwitchLabelsopt = _SwitchLabelsopt
            if _SwitchLabelsopt: _SwitchLabelsopt.setParent(self)
            self._RBRACE = _RBRACE
            _RBRACE.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACE:  _content.add(self._LBRACE)
            if self._SwitchBlockStatementGroupsopt:  _content.add(self._SwitchBlockStatementGroupsopt)
            if self._SwitchLabelsopt:  _content.add(self._SwitchLabelsopt)
            if self._RBRACE:  _content.add(self._RBRACE)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchBlock(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchBlock(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchBlock(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchBlock(self, o)
    

'''/**
 *<em>
*<li>Rule 299:  SwitchBlockStatementGroups ::= SwitchBlockStatementGroup
 *</em>
 *<p>
 *<b>
*<li>Rule 300:  SwitchBlockStatementGroups ::= SwitchBlockStatementGroups SwitchBlockStatementGroup
 *</b>
 */'''
class SwitchBlockStatementGroups ( Ast ,ISwitchBlockStatementGroups):
    

        def  getSwitchBlockStatementGroups(self)  :  return self._SwitchBlockStatementGroups
        def  setSwitchBlockStatementGroups(self,  _SwitchBlockStatementGroups) :   self._SwitchBlockStatementGroups = _SwitchBlockStatementGroups
        def  getSwitchBlockStatementGroup(self)  :  return self._SwitchBlockStatementGroup
        def  setSwitchBlockStatementGroup(self,  _SwitchBlockStatementGroup) :   self._SwitchBlockStatementGroup = _SwitchBlockStatementGroup

        __slots__ = ('_SwitchBlockStatementGroups', '_SwitchBlockStatementGroup')

        def __init__(self, leftIToken, rightIToken,
                             _SwitchBlockStatementGroups,
                             _SwitchBlockStatementGroup):
        
            super(SwitchBlockStatementGroups, self).__init__(leftIToken, rightIToken)

            self._SwitchBlockStatementGroups = _SwitchBlockStatementGroups
            _SwitchBlockStatementGroups.setParent(self)
            self._SwitchBlockStatementGroup = _SwitchBlockStatementGroup
            _SwitchBlockStatementGroup.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SwitchBlockStatementGroups:  _content.add(self._SwitchBlockStatementGroups)
            if self._SwitchBlockStatementGroup:  _content.add(self._SwitchBlockStatementGroup)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchBlockStatementGroups(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchBlockStatementGroups(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchBlockStatementGroups(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchBlockStatementGroups(self, o)
    

'''/**
 *<b>
*<li>Rule 301:  SwitchBlockStatementGroup ::= SwitchLabels BlockStatements
 *</b>
 */'''
class SwitchBlockStatementGroup ( Ast ,ISwitchBlockStatementGroup):
    

        def  getSwitchLabels(self)  :  return self._SwitchLabels
        def  setSwitchLabels(self,  _SwitchLabels) :   self._SwitchLabels = _SwitchLabels
        def  getBlockStatements(self)  :  return self._BlockStatements
        def  setBlockStatements(self,  _BlockStatements) :   self._BlockStatements = _BlockStatements

        __slots__ = ('_SwitchLabels', '_BlockStatements')

        def __init__(self, leftIToken, rightIToken,
                             _SwitchLabels,
                             _BlockStatements):
        
            super(SwitchBlockStatementGroup, self).__init__(leftIToken, rightIToken)

            self._SwitchLabels = _SwitchLabels
            _SwitchLabels.setParent(self)
            self._BlockStatements = _BlockStatements
            _BlockStatements.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SwitchLabels:  _content.add(self._SwitchLabels)
            if self._BlockStatements:  _content.add(self._BlockStatements)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchBlockStatementGroup(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchBlockStatementGroup(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchBlockStatementGroup(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchBlockStatementGroup(self, o)
    

'''/**
 *<em>
*<li>Rule 302:  SwitchLabels ::= SwitchLabel
 *</em>
 *<p>
 *<b>
*<li>Rule 303:  SwitchLabels ::= SwitchLabels SwitchLabel
 *</b>
 */'''
class SwitchLabels ( Ast ,ISwitchLabels):
    

        def  getSwitchLabels(self)  :  return self._SwitchLabels
        def  setSwitchLabels(self,  _SwitchLabels) :   self._SwitchLabels = _SwitchLabels
        def  getSwitchLabel(self)  :  return self._SwitchLabel
        def  setSwitchLabel(self,  _SwitchLabel) :   self._SwitchLabel = _SwitchLabel

        __slots__ = ('_SwitchLabels', '_SwitchLabel')

        def __init__(self, leftIToken, rightIToken,
                             _SwitchLabels,
                             _SwitchLabel):
        
            super(SwitchLabels, self).__init__(leftIToken, rightIToken)

            self._SwitchLabels = _SwitchLabels
            _SwitchLabels.setParent(self)
            self._SwitchLabel = _SwitchLabel
            _SwitchLabel.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._SwitchLabels:  _content.add(self._SwitchLabels)
            if self._SwitchLabel:  _content.add(self._SwitchLabel)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchLabels(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchLabels(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchLabels(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchLabels(self, o)
    

'''/**
 *<b>
*<li>Rule 308:  WhileStatement ::= while ( Expression ) Statement
 *</b>
 */'''
class WhileStatement ( Ast ,IWhileStatement):
    

        def  getwhile(self)  :  return self._while
        def  setwhile(self,  _while) :   self._while = _while
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement

        __slots__ = ('_while', '_LPAREN', '_Expression', '_RPAREN', '_Statement')

        def __init__(self, leftIToken, rightIToken,
                             _while,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _Statement):
        
            super(WhileStatement, self).__init__(leftIToken, rightIToken)

            self._while = _while
            _while.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._while:  _content.add(self._while)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._Statement:  _content.add(self._Statement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitWhileStatement(self)
        def  acceptWithArg(self, v, o):  v.visitWhileStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitWhileStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitWhileStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 309:  WhileStatementNoShortIf ::= while ( Expression ) StatementNoShortIf
 *</b>
 */'''
class WhileStatementNoShortIf ( Ast ,IWhileStatementNoShortIf):
    

        def  getwhile(self)  :  return self._while
        def  setwhile(self,  _while) :   self._while = _while
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatementNoShortIf(self)  :  return self._StatementNoShortIf
        def  setStatementNoShortIf(self,  _StatementNoShortIf) :   self._StatementNoShortIf = _StatementNoShortIf

        __slots__ = ('_while', '_LPAREN', '_Expression', '_RPAREN', '_StatementNoShortIf')

        def __init__(self, leftIToken, rightIToken,
                             _while,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _StatementNoShortIf):
        
            super(WhileStatementNoShortIf, self).__init__(leftIToken, rightIToken)

            self._while = _while
            _while.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._StatementNoShortIf = _StatementNoShortIf
            _StatementNoShortIf.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._while:  _content.add(self._while)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._StatementNoShortIf:  _content.add(self._StatementNoShortIf)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitWhileStatementNoShortIf(self)
        def  acceptWithArg(self, v, o):  v.visitWhileStatementNoShortIf(self, o)
        def  acceptWithResult(self, v):  return v.visitWhileStatementNoShortIf(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitWhileStatementNoShortIf(self, o)
    

'''/**
 *<b>
*<li>Rule 310:  DoStatement ::= do Statement while ( Expression ) ;
 *</b>
 */'''
class DoStatement ( Ast ,IDoStatement):
    

        def  getdo(self)  :  return self._do
        def  setdo(self,  _do) :   self._do = _do
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement
        def  getwhile(self)  :  return self._while
        def  setwhile(self,  _while) :   self._while = _while
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_do', '_Statement', '_while', '_LPAREN', '_Expression', '_RPAREN', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _do,
                             _Statement,
                             _while,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _SEMICOLON):
        
            super(DoStatement, self).__init__(leftIToken, rightIToken)

            self._do = _do
            _do.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self._while = _while
            _while.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._do:  _content.add(self._do)
            if self._Statement:  _content.add(self._Statement)
            if self._while:  _content.add(self._while)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitDoStatement(self)
        def  acceptWithArg(self, v, o):  v.visitDoStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitDoStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitDoStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 313:  BasicForStatement ::= for ( ForInitopt ; Expressionopt ; ForUpdateopt ) Statement
 *</b>
 */'''
class BasicForStatement ( Ast ,IBasicForStatement):
    

        def  getfor(self)  :  return self._for
        def  setfor(self,  _for) :   self._for = _for
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getForInitopt</b> may be <b>null</b>
         */'''
        def  getForInitopt(self)  :  return self._ForInitopt
        def  setForInitopt(self,  _ForInitopt) :   self._ForInitopt = _ForInitopt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON
        '''/**
         * The value returned by <b>getExpressionopt</b> may be <b>null</b>
         */'''
        def  getExpressionopt(self)  :  return self._Expressionopt
        def  setExpressionopt(self,  _Expressionopt) :   self._Expressionopt = _Expressionopt
        def  getSEMICOLON6(self)  :  return self._SEMICOLON6
        def  setSEMICOLON6(self,  _SEMICOLON6) :   self._SEMICOLON6 = _SEMICOLON6
        '''/**
         * The value returned by <b>getForUpdateopt</b> may be <b>null</b>
         */'''
        def  getForUpdateopt(self)  :  return self._ForUpdateopt
        def  setForUpdateopt(self,  _ForUpdateopt) :   self._ForUpdateopt = _ForUpdateopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement

        __slots__ = ('_for', '_LPAREN', '_ForInitopt', '_SEMICOLON', '_Expressionopt', '_SEMICOLON6', '_ForUpdateopt', '_RPAREN', '_Statement')

        def __init__(self, leftIToken, rightIToken,
                             _for,
                             _LPAREN,
                             _ForInitopt,
                             _SEMICOLON,
                             _Expressionopt,
                             _SEMICOLON6,
                             _ForUpdateopt,
                             _RPAREN,
                             _Statement):
        
            super(BasicForStatement, self).__init__(leftIToken, rightIToken)

            self._for = _for
            _for.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ForInitopt = _ForInitopt
            if _ForInitopt: _ForInitopt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self._Expressionopt = _Expressionopt
            if _Expressionopt: _Expressionopt.setParent(self)
            self._SEMICOLON6 = _SEMICOLON6
            _SEMICOLON6.setParent(self)
            self._ForUpdateopt = _ForUpdateopt
            if _ForUpdateopt: _ForUpdateopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._for:  _content.add(self._for)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ForInitopt:  _content.add(self._ForInitopt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            if self._Expressionopt:  _content.add(self._Expressionopt)
            if self._SEMICOLON6:  _content.add(self._SEMICOLON6)
            if self._ForUpdateopt:  _content.add(self._ForUpdateopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._Statement:  _content.add(self._Statement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitBasicForStatement(self)
        def  acceptWithArg(self, v, o):  v.visitBasicForStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitBasicForStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitBasicForStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 314:  ForStatementNoShortIf ::= for ( ForInitopt ; Expressionopt ; ForUpdateopt ) StatementNoShortIf
 *</b>
 */'''
class ForStatementNoShortIf ( Ast ,IForStatementNoShortIf):
    

        def  getfor(self)  :  return self._for
        def  setfor(self,  _for) :   self._for = _for
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getForInitopt</b> may be <b>null</b>
         */'''
        def  getForInitopt(self)  :  return self._ForInitopt
        def  setForInitopt(self,  _ForInitopt) :   self._ForInitopt = _ForInitopt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON
        '''/**
         * The value returned by <b>getExpressionopt</b> may be <b>null</b>
         */'''
        def  getExpressionopt(self)  :  return self._Expressionopt
        def  setExpressionopt(self,  _Expressionopt) :   self._Expressionopt = _Expressionopt
        def  getSEMICOLON6(self)  :  return self._SEMICOLON6
        def  setSEMICOLON6(self,  _SEMICOLON6) :   self._SEMICOLON6 = _SEMICOLON6
        '''/**
         * The value returned by <b>getForUpdateopt</b> may be <b>null</b>
         */'''
        def  getForUpdateopt(self)  :  return self._ForUpdateopt
        def  setForUpdateopt(self,  _ForUpdateopt) :   self._ForUpdateopt = _ForUpdateopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatementNoShortIf(self)  :  return self._StatementNoShortIf
        def  setStatementNoShortIf(self,  _StatementNoShortIf) :   self._StatementNoShortIf = _StatementNoShortIf

        __slots__ = ('_for', '_LPAREN', '_ForInitopt', '_SEMICOLON', '_Expressionopt', '_SEMICOLON6', '_ForUpdateopt', '_RPAREN', '_StatementNoShortIf')

        def __init__(self, leftIToken, rightIToken,
                             _for,
                             _LPAREN,
                             _ForInitopt,
                             _SEMICOLON,
                             _Expressionopt,
                             _SEMICOLON6,
                             _ForUpdateopt,
                             _RPAREN,
                             _StatementNoShortIf):
        
            super(ForStatementNoShortIf, self).__init__(leftIToken, rightIToken)

            self._for = _for
            _for.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ForInitopt = _ForInitopt
            if _ForInitopt: _ForInitopt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self._Expressionopt = _Expressionopt
            if _Expressionopt: _Expressionopt.setParent(self)
            self._SEMICOLON6 = _SEMICOLON6
            _SEMICOLON6.setParent(self)
            self._ForUpdateopt = _ForUpdateopt
            if _ForUpdateopt: _ForUpdateopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._StatementNoShortIf = _StatementNoShortIf
            _StatementNoShortIf.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._for:  _content.add(self._for)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ForInitopt:  _content.add(self._ForInitopt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            if self._Expressionopt:  _content.add(self._Expressionopt)
            if self._SEMICOLON6:  _content.add(self._SEMICOLON6)
            if self._ForUpdateopt:  _content.add(self._ForUpdateopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._StatementNoShortIf:  _content.add(self._StatementNoShortIf)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitForStatementNoShortIf(self)
        def  acceptWithArg(self, v, o):  v.visitForStatementNoShortIf(self, o)
        def  acceptWithResult(self, v):  return v.visitForStatementNoShortIf(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitForStatementNoShortIf(self, o)
    

'''/**
 *<em>
*<li>Rule 318:  StatementExpressionList ::= StatementExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 319:  StatementExpressionList ::= StatementExpressionList , StatementExpression
 *</b>
 */'''
class StatementExpressionList ( Ast ,IStatementExpressionList):
    

        def  getStatementExpressionList(self)  :  return self._StatementExpressionList
        def  setStatementExpressionList(self,  _StatementExpressionList) :   self._StatementExpressionList = _StatementExpressionList
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getStatementExpression(self)  :  return self._StatementExpression
        def  setStatementExpression(self,  _StatementExpression) :   self._StatementExpression = _StatementExpression

        __slots__ = ('_StatementExpressionList', '_COMMA', '_StatementExpression')

        def __init__(self, leftIToken, rightIToken,
                             _StatementExpressionList,
                             _COMMA,
                             _StatementExpression):
        
            super(StatementExpressionList, self).__init__(leftIToken, rightIToken)

            self._StatementExpressionList = _StatementExpressionList
            _StatementExpressionList.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._StatementExpression = _StatementExpression
            _StatementExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._StatementExpressionList:  _content.add(self._StatementExpressionList)
            if self._COMMA:  _content.add(self._COMMA)
            if self._StatementExpression:  _content.add(self._StatementExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitStatementExpressionList(self)
        def  acceptWithArg(self, v, o):  v.visitStatementExpressionList(self, o)
        def  acceptWithResult(self, v):  return v.visitStatementExpressionList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitStatementExpressionList(self, o)
    

'''/**
 *<b>
*<li>Rule 320:  EnhancedForStatement ::= for ( FormalParameter : Expression ) Statement
 *</b>
 */'''
class EnhancedForStatement ( Ast ,IEnhancedForStatement):
    

        def  getfor(self)  :  return self._for
        def  setfor(self,  _for) :   self._for = _for
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getFormalParameter(self)  :  return self._FormalParameter
        def  setFormalParameter(self,  _FormalParameter) :   self._FormalParameter = _FormalParameter
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getStatement(self)  :  return self._Statement
        def  setStatement(self,  _Statement) :   self._Statement = _Statement

        __slots__ = ('_for', '_LPAREN', '_FormalParameter', '_COLON', '_Expression', '_RPAREN', '_Statement')

        def __init__(self, leftIToken, rightIToken,
                             _for,
                             _LPAREN,
                             _FormalParameter,
                             _COLON,
                             _Expression,
                             _RPAREN,
                             _Statement):
        
            super(EnhancedForStatement, self).__init__(leftIToken, rightIToken)

            self._for = _for
            _for.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._FormalParameter = _FormalParameter
            _FormalParameter.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._Statement = _Statement
            _Statement.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._for:  _content.add(self._for)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._FormalParameter:  _content.add(self._FormalParameter)
            if self._COLON:  _content.add(self._COLON)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._Statement:  _content.add(self._Statement)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEnhancedForStatement(self)
        def  acceptWithArg(self, v, o):  v.visitEnhancedForStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitEnhancedForStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEnhancedForStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 321:  BreakStatement ::= break identifieropt ;
 *</b>
 */'''
class BreakStatement ( Ast ,IBreakStatement):
    

        def  getbreak(self)  :  return self._break
        def  setbreak(self,  _break) :   self._break = _break
        '''/**
         * The value returned by <b>getidentifieropt</b> may be <b>null</b>
         */'''
        def  getidentifieropt(self)  :  return self._identifieropt
        def  setidentifieropt(self,  _identifieropt) :   self._identifieropt = _identifieropt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_break', '_identifieropt', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _break,
                             _identifieropt,
                             _SEMICOLON):
        
            super(BreakStatement, self).__init__(leftIToken, rightIToken)

            self._break = _break
            _break.setParent(self)
            self._identifieropt = _identifieropt
            if _identifieropt: _identifieropt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._break:  _content.add(self._break)
            if self._identifieropt:  _content.add(self._identifieropt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitBreakStatement(self)
        def  acceptWithArg(self, v, o):  v.visitBreakStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitBreakStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitBreakStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 322:  ContinueStatement ::= continue identifieropt ;
 *</b>
 */'''
class ContinueStatement ( Ast ,IContinueStatement):
    

        def  getcontinue(self)  :  return self._continue
        def  setcontinue(self,  _continue) :   self._continue = _continue
        '''/**
         * The value returned by <b>getidentifieropt</b> may be <b>null</b>
         */'''
        def  getidentifieropt(self)  :  return self._identifieropt
        def  setidentifieropt(self,  _identifieropt) :   self._identifieropt = _identifieropt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_continue', '_identifieropt', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _continue,
                             _identifieropt,
                             _SEMICOLON):
        
            super(ContinueStatement, self).__init__(leftIToken, rightIToken)

            self._continue = _continue
            _continue.setParent(self)
            self._identifieropt = _identifieropt
            if _identifieropt: _identifieropt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._continue:  _content.add(self._continue)
            if self._identifieropt:  _content.add(self._identifieropt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitContinueStatement(self)
        def  acceptWithArg(self, v, o):  v.visitContinueStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitContinueStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitContinueStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 323:  ReturnStatement ::= return Expressionopt ;
 *</b>
 */'''
class ReturnStatement ( Ast ,IReturnStatement):
    

        def  getreturn(self)  :  return self._return
        def  setreturn(self,  _return) :   self._return = _return
        '''/**
         * The value returned by <b>getExpressionopt</b> may be <b>null</b>
         */'''
        def  getExpressionopt(self)  :  return self._Expressionopt
        def  setExpressionopt(self,  _Expressionopt) :   self._Expressionopt = _Expressionopt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_return', '_Expressionopt', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _return,
                             _Expressionopt,
                             _SEMICOLON):
        
            super(ReturnStatement, self).__init__(leftIToken, rightIToken)

            self._return = _return
            _return.setParent(self)
            self._Expressionopt = _Expressionopt
            if _Expressionopt: _Expressionopt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._return:  _content.add(self._return)
            if self._Expressionopt:  _content.add(self._Expressionopt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitReturnStatement(self)
        def  acceptWithArg(self, v, o):  v.visitReturnStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitReturnStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitReturnStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 324:  ThrowStatement ::= throw Expression ;
 *</b>
 */'''
class ThrowStatement ( Ast ,IThrowStatement):
    

        def  getthrow(self)  :  return self._throw
        def  setthrow(self,  _throw) :   self._throw = _throw
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_throw', '_Expression', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _throw,
                             _Expression,
                             _SEMICOLON):
        
            super(ThrowStatement, self).__init__(leftIToken, rightIToken)

            self._throw = _throw
            _throw.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._throw:  _content.add(self._throw)
            if self._Expression:  _content.add(self._Expression)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitThrowStatement(self)
        def  acceptWithArg(self, v, o):  v.visitThrowStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitThrowStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitThrowStatement(self, o)
    

'''/**
 *<b>
*<li>Rule 325:  SynchronizedStatement ::= synchronized ( Expression ) Block
 *</b>
 */'''
class SynchronizedStatement ( Ast ,ISynchronizedStatement):
    

        def  getsynchronized(self)  :  return self._synchronized
        def  setsynchronized(self,  _synchronized) :   self._synchronized = _synchronized
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getBlock(self)  :  return self._Block
        def  setBlock(self,  _Block) :   self._Block = _Block

        __slots__ = ('_synchronized', '_LPAREN', '_Expression', '_RPAREN', '_Block')

        def __init__(self, leftIToken, rightIToken,
                             _synchronized,
                             _LPAREN,
                             _Expression,
                             _RPAREN,
                             _Block):
        
            super(SynchronizedStatement, self).__init__(leftIToken, rightIToken)

            self._synchronized = _synchronized
            _synchronized.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._Block = _Block
            _Block.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._synchronized:  _content.add(self._synchronized)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._Block:  _content.add(self._Block)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSynchronizedStatement(self)
        def  acceptWithArg(self, v, o):  v.visitSynchronizedStatement(self, o)
        def  acceptWithResult(self, v):  return v.visitSynchronizedStatement(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSynchronizedStatement(self, o)
    

'''/**
 *<em>
*<li>Rule 328:  Catches ::= CatchClause
 *</em>
 *<p>
 *<b>
*<li>Rule 329:  Catches ::= Catches CatchClause
 *</b>
 */'''
class Catches ( Ast ,ICatches):
    

        def  getCatches(self)  :  return self._Catches
        def  setCatches(self,  _Catches) :   self._Catches = _Catches
        def  getCatchClause(self)  :  return self._CatchClause
        def  setCatchClause(self,  _CatchClause) :   self._CatchClause = _CatchClause

        __slots__ = ('_Catches', '_CatchClause')

        def __init__(self, leftIToken, rightIToken,
                             _Catches,
                             _CatchClause):
        
            super(Catches, self).__init__(leftIToken, rightIToken)

            self._Catches = _Catches
            _Catches.setParent(self)
            self._CatchClause = _CatchClause
            _CatchClause.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Catches:  _content.add(self._Catches)
            if self._CatchClause:  _content.add(self._CatchClause)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitCatches(self)
        def  acceptWithArg(self, v, o):  v.visitCatches(self, o)
        def  acceptWithResult(self, v):  return v.visitCatches(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitCatches(self, o)
    

'''/**
 *<b>
*<li>Rule 330:  CatchClause ::= catch ( FormalParameter ) Block
 *</b>
 */'''
class CatchClause ( Ast ,ICatchClause):
    

        def  getcatch(self)  :  return self._catch
        def  setcatch(self,  _catch) :   self._catch = _catch
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getFormalParameter(self)  :  return self._FormalParameter
        def  setFormalParameter(self,  _FormalParameter) :   self._FormalParameter = _FormalParameter
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getBlock(self)  :  return self._Block
        def  setBlock(self,  _Block) :   self._Block = _Block

        __slots__ = ('_catch', '_LPAREN', '_FormalParameter', '_RPAREN', '_Block')

        def __init__(self, leftIToken, rightIToken,
                             _catch,
                             _LPAREN,
                             _FormalParameter,
                             _RPAREN,
                             _Block):
        
            super(CatchClause, self).__init__(leftIToken, rightIToken)

            self._catch = _catch
            _catch.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._FormalParameter = _FormalParameter
            _FormalParameter.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._Block = _Block
            _Block.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._catch:  _content.add(self._catch)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._FormalParameter:  _content.add(self._FormalParameter)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._Block:  _content.add(self._Block)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitCatchClause(self)
        def  acceptWithArg(self, v, o):  v.visitCatchClause(self, o)
        def  acceptWithResult(self, v):  return v.visitCatchClause(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitCatchClause(self, o)
    

'''/**
 *<b>
*<li>Rule 331:  Finally ::= finally Block
 *</b>
 */'''
class Finally ( Ast ,IFinally):
    

        def  getfinally(self)  :  return self._finally
        def  setfinally(self,  _finally) :   self._finally = _finally
        def  getBlock(self)  :  return self._Block
        def  setBlock(self,  _Block) :   self._Block = _Block

        __slots__ = ('_finally', '_Block')

        def __init__(self, leftIToken, rightIToken,
                             _finally,
                             _Block):
        
            super(Finally, self).__init__(leftIToken, rightIToken)

            self._finally = _finally
            _finally.setParent(self)
            self._Block = _Block
            _Block.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._finally:  _content.add(self._finally)
            if self._Block:  _content.add(self._Block)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFinally(self)
        def  acceptWithArg(self, v, o):  v.visitFinally(self, o)
        def  acceptWithResult(self, v):  return v.visitFinally(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFinally(self, o)
    

'''/**
 *<em>
*<li>Rule 356:  ArgumentList ::= Expression
 *</em>
 *<p>
 *<b>
*<li>Rule 357:  ArgumentList ::= ArgumentList , Expression
 *</b>
 */'''
class ArgumentList ( Ast ,IArgumentList):
    

        def  getArgumentList(self)  :  return self._ArgumentList
        def  setArgumentList(self,  _ArgumentList) :   self._ArgumentList = _ArgumentList
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression

        __slots__ = ('_ArgumentList', '_COMMA', '_Expression')

        def __init__(self, leftIToken, rightIToken,
                             _ArgumentList,
                             _COMMA,
                             _Expression):
        
            super(ArgumentList, self).__init__(leftIToken, rightIToken)

            self._ArgumentList = _ArgumentList
            _ArgumentList.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ArgumentList:  _content.add(self._ArgumentList)
            if self._COMMA:  _content.add(self._COMMA)
            if self._Expression:  _content.add(self._Expression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArgumentList(self)
        def  acceptWithArg(self, v, o):  v.visitArgumentList(self, o)
        def  acceptWithResult(self, v):  return v.visitArgumentList(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArgumentList(self, o)
    

'''/**
 *<em>
*<li>Rule 362:  DimExprs ::= DimExpr
 *</em>
 *<p>
 *<b>
*<li>Rule 363:  DimExprs ::= DimExprs DimExpr
 *</b>
 */'''
class DimExprs ( Ast ,IDimExprs):
    

        def  getDimExprs(self)  :  return self._DimExprs
        def  setDimExprs(self,  _DimExprs) :   self._DimExprs = _DimExprs
        def  getDimExpr(self)  :  return self._DimExpr
        def  setDimExpr(self,  _DimExpr) :   self._DimExpr = _DimExpr

        __slots__ = ('_DimExprs', '_DimExpr')

        def __init__(self, leftIToken, rightIToken,
                             _DimExprs,
                             _DimExpr):
        
            super(DimExprs, self).__init__(leftIToken, rightIToken)

            self._DimExprs = _DimExprs
            _DimExprs.setParent(self)
            self._DimExpr = _DimExpr
            _DimExpr.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._DimExprs:  _content.add(self._DimExprs)
            if self._DimExpr:  _content.add(self._DimExpr)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitDimExprs(self)
        def  acceptWithArg(self, v, o):  v.visitDimExprs(self, o)
        def  acceptWithResult(self, v):  return v.visitDimExprs(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitDimExprs(self, o)
    

'''/**
 *<b>
*<li>Rule 364:  DimExpr ::= [ Expression ]
 *</b>
 */'''
class DimExpr ( Ast ,IDimExpr):
    

        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_LBRACKET', '_Expression', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACKET,
                             _Expression,
                             _RBRACKET):
        
            super(DimExpr, self).__init__(leftIToken, rightIToken)

            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._Expression:  _content.add(self._Expression)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitDimExpr(self)
        def  acceptWithArg(self, v, o):  v.visitDimExpr(self, o)
        def  acceptWithResult(self, v):  return v.visitDimExpr(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitDimExpr(self, o)
    

'''/**
 *<b>
*<li>Rule 381:  PostIncrementExpression ::= PostfixExpression ++
 *</b>
 */'''
class PostIncrementExpression ( Ast ,IPostIncrementExpression):
    

        def  getPostfixExpression(self)  :  return self._PostfixExpression
        def  setPostfixExpression(self,  _PostfixExpression) :   self._PostfixExpression = _PostfixExpression
        def  getPLUS_PLUS(self)  :  return self._PLUS_PLUS
        def  setPLUS_PLUS(self,  _PLUS_PLUS) :   self._PLUS_PLUS = _PLUS_PLUS

        __slots__ = ('_PostfixExpression', '_PLUS_PLUS')

        def __init__(self, leftIToken, rightIToken,
                             _PostfixExpression,
                             _PLUS_PLUS):
        
            super(PostIncrementExpression, self).__init__(leftIToken, rightIToken)

            self._PostfixExpression = _PostfixExpression
            _PostfixExpression.setParent(self)
            self._PLUS_PLUS = _PLUS_PLUS
            _PLUS_PLUS.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PostfixExpression:  _content.add(self._PostfixExpression)
            if self._PLUS_PLUS:  _content.add(self._PLUS_PLUS)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPostIncrementExpression(self)
        def  acceptWithArg(self, v, o):  v.visitPostIncrementExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitPostIncrementExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPostIncrementExpression(self, o)
    

'''/**
 *<b>
*<li>Rule 382:  PostDecrementExpression ::= PostfixExpression --
 *</b>
 */'''
class PostDecrementExpression ( Ast ,IPostDecrementExpression):
    

        def  getPostfixExpression(self)  :  return self._PostfixExpression
        def  setPostfixExpression(self,  _PostfixExpression) :   self._PostfixExpression = _PostfixExpression
        def  getMINUS_MINUS(self)  :  return self._MINUS_MINUS
        def  setMINUS_MINUS(self,  _MINUS_MINUS) :   self._MINUS_MINUS = _MINUS_MINUS

        __slots__ = ('_PostfixExpression', '_MINUS_MINUS')

        def __init__(self, leftIToken, rightIToken,
                             _PostfixExpression,
                             _MINUS_MINUS):
        
            super(PostDecrementExpression, self).__init__(leftIToken, rightIToken)

            self._PostfixExpression = _PostfixExpression
            _PostfixExpression.setParent(self)
            self._MINUS_MINUS = _MINUS_MINUS
            _MINUS_MINUS.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PostfixExpression:  _content.add(self._PostfixExpression)
            if self._MINUS_MINUS:  _content.add(self._MINUS_MINUS)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPostDecrementExpression(self)
        def  acceptWithArg(self, v, o):  v.visitPostDecrementExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitPostDecrementExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPostDecrementExpression(self, o)
    

'''/**
 *<b>
*<li>Rule 388:  PreIncrementExpression ::= ++ UnaryExpression
 *</b>
 */'''
class PreIncrementExpression ( Ast ,IPreIncrementExpression):
    

        def  getPLUS_PLUS(self)  :  return self._PLUS_PLUS
        def  setPLUS_PLUS(self,  _PLUS_PLUS) :   self._PLUS_PLUS = _PLUS_PLUS
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_PLUS_PLUS', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _PLUS_PLUS,
                             _UnaryExpression):
        
            super(PreIncrementExpression, self).__init__(leftIToken, rightIToken)

            self._PLUS_PLUS = _PLUS_PLUS
            _PLUS_PLUS.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PLUS_PLUS:  _content.add(self._PLUS_PLUS)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPreIncrementExpression(self)
        def  acceptWithArg(self, v, o):  v.visitPreIncrementExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitPreIncrementExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPreIncrementExpression(self, o)
    

'''/**
 *<b>
*<li>Rule 389:  PreDecrementExpression ::= -- UnaryExpression
 *</b>
 */'''
class PreDecrementExpression ( Ast ,IPreDecrementExpression):
    

        def  getMINUS_MINUS(self)  :  return self._MINUS_MINUS
        def  setMINUS_MINUS(self,  _MINUS_MINUS) :   self._MINUS_MINUS = _MINUS_MINUS
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_MINUS_MINUS', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _MINUS_MINUS,
                             _UnaryExpression):
        
            super(PreDecrementExpression, self).__init__(leftIToken, rightIToken)

            self._MINUS_MINUS = _MINUS_MINUS
            _MINUS_MINUS.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MINUS_MINUS:  _content.add(self._MINUS_MINUS)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPreDecrementExpression(self)
        def  acceptWithArg(self, v, o):  v.visitPreDecrementExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitPreDecrementExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPreDecrementExpression(self, o)
    

'''/**
 *<em>
*<li>Rule 416:  AndExpression ::= EqualityExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 417:  AndExpression ::= AndExpression & EqualityExpression
 *</b>
 */'''
class AndExpression ( Ast ,IAndExpression):
    

        def  getAndExpression(self)  :  return self._AndExpression
        def  setAndExpression(self,  _AndExpression) :   self._AndExpression = _AndExpression
        def  getAND(self)  :  return self._AND
        def  setAND(self,  _AND) :   self._AND = _AND
        def  getEqualityExpression(self)  :  return self._EqualityExpression
        def  setEqualityExpression(self,  _EqualityExpression) :   self._EqualityExpression = _EqualityExpression

        __slots__ = ('_AndExpression', '_AND', '_EqualityExpression')

        def __init__(self, leftIToken, rightIToken,
                             _AndExpression,
                             _AND,
                             _EqualityExpression):
        
            super(AndExpression, self).__init__(leftIToken, rightIToken)

            self._AndExpression = _AndExpression
            _AndExpression.setParent(self)
            self._AND = _AND
            _AND.setParent(self)
            self._EqualityExpression = _EqualityExpression
            _EqualityExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AndExpression:  _content.add(self._AndExpression)
            if self._AND:  _content.add(self._AND)
            if self._EqualityExpression:  _content.add(self._EqualityExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAndExpression(self)
        def  acceptWithArg(self, v, o):  v.visitAndExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitAndExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAndExpression(self, o)
    

'''/**
 *<em>
*<li>Rule 418:  ExclusiveOrExpression ::= AndExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 419:  ExclusiveOrExpression ::= ExclusiveOrExpression ^ AndExpression
 *</b>
 */'''
class ExclusiveOrExpression ( Ast ,IExclusiveOrExpression):
    

        def  getExclusiveOrExpression(self)  :  return self._ExclusiveOrExpression
        def  setExclusiveOrExpression(self,  _ExclusiveOrExpression) :   self._ExclusiveOrExpression = _ExclusiveOrExpression
        def  getXOR(self)  :  return self._XOR
        def  setXOR(self,  _XOR) :   self._XOR = _XOR
        def  getAndExpression(self)  :  return self._AndExpression
        def  setAndExpression(self,  _AndExpression) :   self._AndExpression = _AndExpression

        __slots__ = ('_ExclusiveOrExpression', '_XOR', '_AndExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ExclusiveOrExpression,
                             _XOR,
                             _AndExpression):
        
            super(ExclusiveOrExpression, self).__init__(leftIToken, rightIToken)

            self._ExclusiveOrExpression = _ExclusiveOrExpression
            _ExclusiveOrExpression.setParent(self)
            self._XOR = _XOR
            _XOR.setParent(self)
            self._AndExpression = _AndExpression
            _AndExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ExclusiveOrExpression:  _content.add(self._ExclusiveOrExpression)
            if self._XOR:  _content.add(self._XOR)
            if self._AndExpression:  _content.add(self._AndExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExclusiveOrExpression(self)
        def  acceptWithArg(self, v, o):  v.visitExclusiveOrExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitExclusiveOrExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExclusiveOrExpression(self, o)
    

'''/**
 *<em>
*<li>Rule 420:  InclusiveOrExpression ::= ExclusiveOrExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 421:  InclusiveOrExpression ::= InclusiveOrExpression | ExclusiveOrExpression
 *</b>
 */'''
class InclusiveOrExpression ( Ast ,IInclusiveOrExpression):
    

        def  getInclusiveOrExpression(self)  :  return self._InclusiveOrExpression
        def  setInclusiveOrExpression(self,  _InclusiveOrExpression) :   self._InclusiveOrExpression = _InclusiveOrExpression
        def  getOR(self)  :  return self._OR
        def  setOR(self,  _OR) :   self._OR = _OR
        def  getExclusiveOrExpression(self)  :  return self._ExclusiveOrExpression
        def  setExclusiveOrExpression(self,  _ExclusiveOrExpression) :   self._ExclusiveOrExpression = _ExclusiveOrExpression

        __slots__ = ('_InclusiveOrExpression', '_OR', '_ExclusiveOrExpression')

        def __init__(self, leftIToken, rightIToken,
                             _InclusiveOrExpression,
                             _OR,
                             _ExclusiveOrExpression):
        
            super(InclusiveOrExpression, self).__init__(leftIToken, rightIToken)

            self._InclusiveOrExpression = _InclusiveOrExpression
            _InclusiveOrExpression.setParent(self)
            self._OR = _OR
            _OR.setParent(self)
            self._ExclusiveOrExpression = _ExclusiveOrExpression
            _ExclusiveOrExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._InclusiveOrExpression:  _content.add(self._InclusiveOrExpression)
            if self._OR:  _content.add(self._OR)
            if self._ExclusiveOrExpression:  _content.add(self._ExclusiveOrExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitInclusiveOrExpression(self)
        def  acceptWithArg(self, v, o):  v.visitInclusiveOrExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitInclusiveOrExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInclusiveOrExpression(self, o)
    

'''/**
 *<em>
*<li>Rule 422:  ConditionalAndExpression ::= InclusiveOrExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 423:  ConditionalAndExpression ::= ConditionalAndExpression && InclusiveOrExpression
 *</b>
 */'''
class ConditionalAndExpression ( Ast ,IConditionalAndExpression):
    

        def  getConditionalAndExpression(self)  :  return self._ConditionalAndExpression
        def  setConditionalAndExpression(self,  _ConditionalAndExpression) :   self._ConditionalAndExpression = _ConditionalAndExpression
        def  getAND_AND(self)  :  return self._AND_AND
        def  setAND_AND(self,  _AND_AND) :   self._AND_AND = _AND_AND
        def  getInclusiveOrExpression(self)  :  return self._InclusiveOrExpression
        def  setInclusiveOrExpression(self,  _InclusiveOrExpression) :   self._InclusiveOrExpression = _InclusiveOrExpression

        __slots__ = ('_ConditionalAndExpression', '_AND_AND', '_InclusiveOrExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ConditionalAndExpression,
                             _AND_AND,
                             _InclusiveOrExpression):
        
            super(ConditionalAndExpression, self).__init__(leftIToken, rightIToken)

            self._ConditionalAndExpression = _ConditionalAndExpression
            _ConditionalAndExpression.setParent(self)
            self._AND_AND = _AND_AND
            _AND_AND.setParent(self)
            self._InclusiveOrExpression = _InclusiveOrExpression
            _InclusiveOrExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConditionalAndExpression:  _content.add(self._ConditionalAndExpression)
            if self._AND_AND:  _content.add(self._AND_AND)
            if self._InclusiveOrExpression:  _content.add(self._InclusiveOrExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConditionalAndExpression(self)
        def  acceptWithArg(self, v, o):  v.visitConditionalAndExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitConditionalAndExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConditionalAndExpression(self, o)
    

'''/**
 *<em>
*<li>Rule 424:  ConditionalOrExpression ::= ConditionalAndExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 425:  ConditionalOrExpression ::= ConditionalOrExpression || ConditionalAndExpression
 *</b>
 */'''
class ConditionalOrExpression ( Ast ,IConditionalOrExpression):
    

        def  getConditionalOrExpression(self)  :  return self._ConditionalOrExpression
        def  setConditionalOrExpression(self,  _ConditionalOrExpression) :   self._ConditionalOrExpression = _ConditionalOrExpression
        def  getOR_OR(self)  :  return self._OR_OR
        def  setOR_OR(self,  _OR_OR) :   self._OR_OR = _OR_OR
        def  getConditionalAndExpression(self)  :  return self._ConditionalAndExpression
        def  setConditionalAndExpression(self,  _ConditionalAndExpression) :   self._ConditionalAndExpression = _ConditionalAndExpression

        __slots__ = ('_ConditionalOrExpression', '_OR_OR', '_ConditionalAndExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ConditionalOrExpression,
                             _OR_OR,
                             _ConditionalAndExpression):
        
            super(ConditionalOrExpression, self).__init__(leftIToken, rightIToken)

            self._ConditionalOrExpression = _ConditionalOrExpression
            _ConditionalOrExpression.setParent(self)
            self._OR_OR = _OR_OR
            _OR_OR.setParent(self)
            self._ConditionalAndExpression = _ConditionalAndExpression
            _ConditionalAndExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConditionalOrExpression:  _content.add(self._ConditionalOrExpression)
            if self._OR_OR:  _content.add(self._OR_OR)
            if self._ConditionalAndExpression:  _content.add(self._ConditionalAndExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConditionalOrExpression(self)
        def  acceptWithArg(self, v, o):  v.visitConditionalOrExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitConditionalOrExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConditionalOrExpression(self, o)
    

'''/**
 *<em>
*<li>Rule 426:  ConditionalExpression ::= ConditionalOrExpression
 *</em>
 *<p>
 *<b>
*<li>Rule 427:  ConditionalExpression ::= ConditionalOrExpression ? Expression : ConditionalExpression
 *</b>
 */'''
class ConditionalExpression ( Ast ,IConditionalExpression):
    

        def  getConditionalOrExpression(self)  :  return self._ConditionalOrExpression
        def  setConditionalOrExpression(self,  _ConditionalOrExpression) :   self._ConditionalOrExpression = _ConditionalOrExpression
        def  getQUESTION(self)  :  return self._QUESTION
        def  setQUESTION(self,  _QUESTION) :   self._QUESTION = _QUESTION
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON
        def  getConditionalExpression(self)  :  return self._ConditionalExpression
        def  setConditionalExpression(self,  _ConditionalExpression) :   self._ConditionalExpression = _ConditionalExpression

        __slots__ = ('_ConditionalOrExpression', '_QUESTION', '_Expression', '_COLON', '_ConditionalExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ConditionalOrExpression,
                             _QUESTION,
                             _Expression,
                             _COLON,
                             _ConditionalExpression):
        
            super(ConditionalExpression, self).__init__(leftIToken, rightIToken)

            self._ConditionalOrExpression = _ConditionalOrExpression
            _ConditionalOrExpression.setParent(self)
            self._QUESTION = _QUESTION
            _QUESTION.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self._ConditionalExpression = _ConditionalExpression
            _ConditionalExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ConditionalOrExpression:  _content.add(self._ConditionalOrExpression)
            if self._QUESTION:  _content.add(self._QUESTION)
            if self._Expression:  _content.add(self._Expression)
            if self._COLON:  _content.add(self._COLON)
            if self._ConditionalExpression:  _content.add(self._ConditionalExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitConditionalExpression(self)
        def  acceptWithArg(self, v, o):  v.visitConditionalExpression(self, o)
        def  acceptWithResult(self, v):  return v.visitConditionalExpression(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConditionalExpression(self, o)
    

'''/**
 *<b>
*<li>Rule 430:  Assignment ::= LeftHandSide AssignmentOperator AssignmentExpression
 *</b>
 */'''
class Assignment ( Ast ,IAssignment):
    

        def  getLeftHandSide(self)  :  return self._LeftHandSide
        def  setLeftHandSide(self,  _LeftHandSide) :   self._LeftHandSide = _LeftHandSide
        def  getAssignmentOperator(self)  :  return self._AssignmentOperator
        def  setAssignmentOperator(self,  _AssignmentOperator) :   self._AssignmentOperator = _AssignmentOperator
        def  getAssignmentExpression(self)  :  return self._AssignmentExpression
        def  setAssignmentExpression(self,  _AssignmentExpression) :   self._AssignmentExpression = _AssignmentExpression

        __slots__ = ('_LeftHandSide', '_AssignmentOperator', '_AssignmentExpression')

        def __init__(self, leftIToken, rightIToken,
                             _LeftHandSide,
                             _AssignmentOperator,
                             _AssignmentExpression):
        
            super(Assignment, self).__init__(leftIToken, rightIToken)

            self._LeftHandSide = _LeftHandSide
            _LeftHandSide.setParent(self)
            self._AssignmentOperator = _AssignmentOperator
            _AssignmentOperator.setParent(self)
            self._AssignmentExpression = _AssignmentExpression
            _AssignmentExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LeftHandSide:  _content.add(self._LeftHandSide)
            if self._AssignmentOperator:  _content.add(self._AssignmentOperator)
            if self._AssignmentExpression:  _content.add(self._AssignmentExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAssignment(self)
        def  acceptWithArg(self, v, o):  v.visitAssignment(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignment(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignment(self, o)
    

'''/**
 *<em>
*<li>Rule 492:  ,opt ::= $Empty
 *</em>
 *<p>
 *<b>
*<li>Rule 493:  ,opt ::= ,
 *</b>
 */'''
class Commaopt ( AstToken ,ICommaopt):
    
        def  getCOMMA(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Commaopt, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitCommaopt(self)
        def  acceptWithArg(self, v, o):  v.visitCommaopt(self, o)
        def  acceptWithResult(self, v):  return v.visitCommaopt(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitCommaopt(self, o)
    

'''/**
 *<em>
*<li>Rule 504:  ...opt ::= $Empty
 *</em>
 *<p>
 *<b>
*<li>Rule 505:  ...opt ::= ...
 *</b>
 */'''
class Ellipsisopt ( AstToken ,IEllipsisopt):
    
        def  getELLIPSIS(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Ellipsisopt, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitEllipsisopt(self)
        def  acceptWithArg(self, v, o):  v.visitEllipsisopt(self, o)
        def  acceptWithResult(self, v):  return v.visitEllipsisopt(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEllipsisopt(self, o)
    

'''/**
 *<b>
*<li>Rule 5:  LPGUserAction ::= $BeginAction BlockStatementsopt $EndAction
 *</b>
 */'''
class LPGUserAction0 ( Ast ,ILPGUserAction):
    

        def  getBeginAction(self)  :  return self._BeginAction
        def  setBeginAction(self,  _BeginAction) :   self._BeginAction = _BeginAction
        '''/**
         * The value returned by <b>getBlockStatementsopt</b> may be <b>null</b>
         */'''
        def  getBlockStatementsopt(self)  :  return self._BlockStatementsopt
        def  setBlockStatementsopt(self,  _BlockStatementsopt) :   self._BlockStatementsopt = _BlockStatementsopt
        def  getEndAction(self)  :  return self._EndAction
        def  setEndAction(self,  _EndAction) :   self._EndAction = _EndAction

        __slots__ = ('_BeginAction', '_BlockStatementsopt', '_EndAction')

        def __init__(self, leftIToken, rightIToken,
                             _BeginAction,
                             _BlockStatementsopt,
                             _EndAction):
        
            super(LPGUserAction0, self).__init__(leftIToken, rightIToken)

            self._BeginAction = _BeginAction
            _BeginAction.setParent(self)
            self._BlockStatementsopt = _BlockStatementsopt
            if _BlockStatementsopt: _BlockStatementsopt.setParent(self)
            self._EndAction = _EndAction
            _EndAction.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._BeginAction:  _content.add(self._BeginAction)
            if self._BlockStatementsopt:  _content.add(self._BlockStatementsopt)
            if self._EndAction:  _content.add(self._EndAction)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLPGUserAction0(self)
        def  acceptWithArg(self, v, o):  v.visitLPGUserAction0(self, o)
        def  acceptWithResult(self, v):  return v.visitLPGUserAction0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLPGUserAction0(self, o)
    

'''/**
 *<b>
*<li>Rule 6:  LPGUserAction ::= $BeginJava BlockStatementsopt $EndJava
 *</b>
 */'''
class LPGUserAction1 ( Ast ,ILPGUserAction):
    

        def  getBeginJava(self)  :  return self._BeginJava
        def  setBeginJava(self,  _BeginJava) :   self._BeginJava = _BeginJava
        '''/**
         * The value returned by <b>getBlockStatementsopt</b> may be <b>null</b>
         */'''
        def  getBlockStatementsopt(self)  :  return self._BlockStatementsopt
        def  setBlockStatementsopt(self,  _BlockStatementsopt) :   self._BlockStatementsopt = _BlockStatementsopt
        def  getEndJava(self)  :  return self._EndJava
        def  setEndJava(self,  _EndJava) :   self._EndJava = _EndJava

        __slots__ = ('_BeginJava', '_BlockStatementsopt', '_EndJava')

        def __init__(self, leftIToken, rightIToken,
                             _BeginJava,
                             _BlockStatementsopt,
                             _EndJava):
        
            super(LPGUserAction1, self).__init__(leftIToken, rightIToken)

            self._BeginJava = _BeginJava
            _BeginJava.setParent(self)
            self._BlockStatementsopt = _BlockStatementsopt
            if _BlockStatementsopt: _BlockStatementsopt.setParent(self)
            self._EndJava = _EndJava
            _EndJava.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._BeginJava:  _content.add(self._BeginJava)
            if self._BlockStatementsopt:  _content.add(self._BlockStatementsopt)
            if self._EndJava:  _content.add(self._EndJava)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitLPGUserAction1(self)
        def  acceptWithArg(self, v, o):  v.visitLPGUserAction1(self, o)
        def  acceptWithResult(self, v):  return v.visitLPGUserAction1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLPGUserAction1(self, o)
    

'''/**
 *<b>
*<li>Rule 7:  LPGUserAction ::= $NoAction
 *</b>
 */'''
class LPGUserAction2 ( AstToken ,ILPGUserAction):
    
        def  getNoAction(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(LPGUserAction2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLPGUserAction2(self)
        def  acceptWithArg(self, v, o):  v.visitLPGUserAction2(self, o)
        def  acceptWithResult(self, v):  return v.visitLPGUserAction2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLPGUserAction2(self, o)
    

'''/**
 *<b>
*<li>Rule 8:  LPGUserAction ::= $NullAction
 *</b>
 */'''
class LPGUserAction3 ( AstToken ,ILPGUserAction):
    
        def  getNullAction(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(LPGUserAction3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLPGUserAction3(self)
        def  acceptWithArg(self, v, o):  v.visitLPGUserAction3(self, o)
        def  acceptWithResult(self, v):  return v.visitLPGUserAction3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLPGUserAction3(self, o)
    

'''/**
 *<b>
*<li>Rule 9:  LPGUserAction ::= $BadAction
 *</b>
 */'''
class LPGUserAction4 ( AstToken ,ILPGUserAction):
    
        def  getBadAction(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(LPGUserAction4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLPGUserAction4(self)
        def  acceptWithArg(self, v, o):  v.visitLPGUserAction4(self, o)
        def  acceptWithResult(self, v):  return v.visitLPGUserAction4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLPGUserAction4(self, o)
    

'''/**
 *<b>
*<li>Rule 16:  IntegralType ::= byte
 *</b>
 */'''
class IntegralType0 ( AstToken ,IIntegralType):
    
        def  getbyte(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(IntegralType0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitIntegralType0(self)
        def  acceptWithArg(self, v, o):  v.visitIntegralType0(self, o)
        def  acceptWithResult(self, v):  return v.visitIntegralType0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIntegralType0(self, o)
    

'''/**
 *<b>
*<li>Rule 17:  IntegralType ::= short
 *</b>
 */'''
class IntegralType1 ( AstToken ,IIntegralType):
    
        def  getshort(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(IntegralType1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitIntegralType1(self)
        def  acceptWithArg(self, v, o):  v.visitIntegralType1(self, o)
        def  acceptWithResult(self, v):  return v.visitIntegralType1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIntegralType1(self, o)
    

'''/**
 *<b>
*<li>Rule 18:  IntegralType ::= int
 *</b>
 */'''
class IntegralType2 ( AstToken ,IIntegralType):
    
        def  getint(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(IntegralType2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitIntegralType2(self)
        def  acceptWithArg(self, v, o):  v.visitIntegralType2(self, o)
        def  acceptWithResult(self, v):  return v.visitIntegralType2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIntegralType2(self, o)
    

'''/**
 *<b>
*<li>Rule 19:  IntegralType ::= long
 *</b>
 */'''
class IntegralType3 ( AstToken ,IIntegralType):
    
        def  getlong(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(IntegralType3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitIntegralType3(self)
        def  acceptWithArg(self, v, o):  v.visitIntegralType3(self, o)
        def  acceptWithResult(self, v):  return v.visitIntegralType3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIntegralType3(self, o)
    

'''/**
 *<b>
*<li>Rule 20:  IntegralType ::= char
 *</b>
 */'''
class IntegralType4 ( AstToken ,IIntegralType):
    
        def  getchar(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(IntegralType4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitIntegralType4(self)
        def  acceptWithArg(self, v, o):  v.visitIntegralType4(self, o)
        def  acceptWithResult(self, v):  return v.visitIntegralType4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitIntegralType4(self, o)
    

'''/**
 *<b>
*<li>Rule 21:  FloatingPointType ::= float
 *</b>
 */'''
class FloatingPointType0 ( AstToken ,IFloatingPointType):
    
        def  getfloat(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FloatingPointType0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFloatingPointType0(self)
        def  acceptWithArg(self, v, o):  v.visitFloatingPointType0(self, o)
        def  acceptWithResult(self, v):  return v.visitFloatingPointType0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFloatingPointType0(self, o)
    

'''/**
 *<b>
*<li>Rule 22:  FloatingPointType ::= double
 *</b>
 */'''
class FloatingPointType1 ( AstToken ,IFloatingPointType):
    
        def  getdouble(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FloatingPointType1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFloatingPointType1(self)
        def  acceptWithArg(self, v, o):  v.visitFloatingPointType1(self, o)
        def  acceptWithResult(self, v):  return v.visitFloatingPointType1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFloatingPointType1(self, o)
    

'''/**
 *<b>
*<li>Rule 45:  WildcardBounds ::= extends ReferenceType
 *</b>
 */'''
class WildcardBounds0 ( Ast ,IWildcardBounds):
    

        def  getextends(self)  :  return self._extends
        def  setextends(self,  _extends) :   self._extends = _extends
        def  getReferenceType(self)  :  return self._ReferenceType
        def  setReferenceType(self,  _ReferenceType) :   self._ReferenceType = _ReferenceType

        __slots__ = ('_extends', '_ReferenceType')

        def __init__(self, leftIToken, rightIToken,
                             _extends,
                             _ReferenceType):
        
            super(WildcardBounds0, self).__init__(leftIToken, rightIToken)

            self._extends = _extends
            _extends.setParent(self)
            self._ReferenceType = _ReferenceType
            _ReferenceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._extends:  _content.add(self._extends)
            if self._ReferenceType:  _content.add(self._ReferenceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitWildcardBounds0(self)
        def  acceptWithArg(self, v, o):  v.visitWildcardBounds0(self, o)
        def  acceptWithResult(self, v):  return v.visitWildcardBounds0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitWildcardBounds0(self, o)
    

'''/**
 *<b>
*<li>Rule 46:  WildcardBounds ::= super ReferenceType
 *</b>
 */'''
class WildcardBounds1 ( Ast ,IWildcardBounds):
    

        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getReferenceType(self)  :  return self._ReferenceType
        def  setReferenceType(self,  _ReferenceType) :   self._ReferenceType = _ReferenceType

        __slots__ = ('_super', '_ReferenceType')

        def __init__(self, leftIToken, rightIToken,
                             _super,
                             _ReferenceType):
        
            super(WildcardBounds1, self).__init__(leftIToken, rightIToken)

            self._super = _super
            _super.setParent(self)
            self._ReferenceType = _ReferenceType
            _ReferenceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._super:  _content.add(self._super)
            if self._ReferenceType:  _content.add(self._ReferenceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitWildcardBounds1(self)
        def  acceptWithArg(self, v, o):  v.visitWildcardBounds1(self, o)
        def  acceptWithResult(self, v):  return v.visitWildcardBounds1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitWildcardBounds1(self, o)
    

'''/**
 *<b>
*<li>Rule 80:  ClassModifier ::= public
 *</b>
 */'''
class ClassModifier0 ( AstToken ,IClassModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 81:  ClassModifier ::= protected
 *</b>
 */'''
class ClassModifier1 ( AstToken ,IClassModifier):
    
        def  getprotected(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 82:  ClassModifier ::= private
 *</b>
 */'''
class ClassModifier2 ( AstToken ,IClassModifier):
    
        def  getprivate(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier2(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier2(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier2(self, o)
    

'''/**
 *<b>
*<li>Rule 83:  ClassModifier ::= abstract
 *</b>
 */'''
class ClassModifier3 ( AstToken ,IClassModifier):
    
        def  getabstract(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier3(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier3(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier3(self, o)
    

'''/**
 *<b>
*<li>Rule 84:  ClassModifier ::= static
 *</b>
 */'''
class ClassModifier4 ( AstToken ,IClassModifier):
    
        def  getstatic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier4(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier4(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier4(self, o)
    

'''/**
 *<b>
*<li>Rule 85:  ClassModifier ::= final
 *</b>
 */'''
class ClassModifier5 ( AstToken ,IClassModifier):
    
        def  getfinal(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier5, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier5(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier5(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier5(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier5(self, o)
    

'''/**
 *<b>
*<li>Rule 86:  ClassModifier ::= strictfp
 *</b>
 */'''
class ClassModifier6 ( AstToken ,IClassModifier):
    
        def  getstrictfp(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ClassModifier6, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitClassModifier6(self)
        def  acceptWithArg(self, v, o):  v.visitClassModifier6(self, o)
        def  acceptWithResult(self, v):  return v.visitClassModifier6(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassModifier6(self, o)
    

'''/**
 *<b>
*<li>Rule 118:  FieldModifier ::= public
 *</b>
 */'''
class FieldModifier0 ( AstToken ,IFieldModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 119:  FieldModifier ::= protected
 *</b>
 */'''
class FieldModifier1 ( AstToken ,IFieldModifier):
    
        def  getprotected(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 120:  FieldModifier ::= private
 *</b>
 */'''
class FieldModifier2 ( AstToken ,IFieldModifier):
    
        def  getprivate(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier2(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier2(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier2(self, o)
    

'''/**
 *<b>
*<li>Rule 121:  FieldModifier ::= static
 *</b>
 */'''
class FieldModifier3 ( AstToken ,IFieldModifier):
    
        def  getstatic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier3(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier3(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier3(self, o)
    

'''/**
 *<b>
*<li>Rule 122:  FieldModifier ::= final
 *</b>
 */'''
class FieldModifier4 ( AstToken ,IFieldModifier):
    
        def  getfinal(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier4(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier4(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier4(self, o)
    

'''/**
 *<b>
*<li>Rule 123:  FieldModifier ::= transient
 *</b>
 */'''
class FieldModifier5 ( AstToken ,IFieldModifier):
    
        def  gettransient(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier5, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier5(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier5(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier5(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier5(self, o)
    

'''/**
 *<b>
*<li>Rule 124:  FieldModifier ::= volatile
 *</b>
 */'''
class FieldModifier6 ( AstToken ,IFieldModifier):
    
        def  getvolatile(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(FieldModifier6, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitFieldModifier6(self)
        def  acceptWithArg(self, v, o):  v.visitFieldModifier6(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldModifier6(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldModifier6(self, o)
    

'''/**
 *<b>
*<li>Rule 129:  MethodDeclarator ::= identifier ( FormalParameterListopt )
 *</b>
 */'''
class MethodDeclarator0 ( Ast ,IMethodDeclarator):
    

        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getFormalParameterListopt</b> may be <b>null</b>
         */'''
        def  getFormalParameterListopt(self)  :  return self._FormalParameterListopt
        def  setFormalParameterListopt(self,  _FormalParameterListopt) :   self._FormalParameterListopt = _FormalParameterListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_identifier', '_LPAREN', '_FormalParameterListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _identifier,
                             _LPAREN,
                             _FormalParameterListopt,
                             _RPAREN):
        
            super(MethodDeclarator0, self).__init__(leftIToken, rightIToken)

            self._identifier = _identifier
            _identifier.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._FormalParameterListopt = _FormalParameterListopt
            if _FormalParameterListopt: _FormalParameterListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._identifier:  _content.add(self._identifier)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._FormalParameterListopt:  _content.add(self._FormalParameterListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodDeclarator0(self)
        def  acceptWithArg(self, v, o):  v.visitMethodDeclarator0(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodDeclarator0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodDeclarator0(self, o)
    

'''/**
 *<b>
*<li>Rule 130:  MethodDeclarator ::= MethodDeclarator [ ]
 *</b>
 */'''
class MethodDeclarator1 ( Ast ,IMethodDeclarator):
    

        def  getMethodDeclarator(self)  :  return self._MethodDeclarator
        def  setMethodDeclarator(self,  _MethodDeclarator) :   self._MethodDeclarator = _MethodDeclarator
        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_MethodDeclarator', '_LBRACKET', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _MethodDeclarator,
                             _LBRACKET,
                             _RBRACKET):
        
            super(MethodDeclarator1, self).__init__(leftIToken, rightIToken)

            self._MethodDeclarator = _MethodDeclarator
            _MethodDeclarator.setParent(self)
            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MethodDeclarator:  _content.add(self._MethodDeclarator)
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodDeclarator1(self)
        def  acceptWithArg(self, v, o):  v.visitMethodDeclarator1(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodDeclarator1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodDeclarator1(self, o)
    

'''/**
 *<b>
*<li>Rule 144:  MethodModifier ::= public
 *</b>
 */'''
class MethodModifier0 ( AstToken ,IMethodModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 145:  MethodModifier ::= protected
 *</b>
 */'''
class MethodModifier1 ( AstToken ,IMethodModifier):
    
        def  getprotected(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 146:  MethodModifier ::= private
 *</b>
 */'''
class MethodModifier2 ( AstToken ,IMethodModifier):
    
        def  getprivate(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier2(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier2(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier2(self, o)
    

'''/**
 *<b>
*<li>Rule 147:  MethodModifier ::= abstract
 *</b>
 */'''
class MethodModifier3 ( AstToken ,IMethodModifier):
    
        def  getabstract(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier3(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier3(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier3(self, o)
    

'''/**
 *<b>
*<li>Rule 148:  MethodModifier ::= static
 *</b>
 */'''
class MethodModifier4 ( AstToken ,IMethodModifier):
    
        def  getstatic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier4(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier4(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier4(self, o)
    

'''/**
 *<b>
*<li>Rule 149:  MethodModifier ::= final
 *</b>
 */'''
class MethodModifier5 ( AstToken ,IMethodModifier):
    
        def  getfinal(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier5, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier5(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier5(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier5(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier5(self, o)
    

'''/**
 *<b>
*<li>Rule 150:  MethodModifier ::= synchronized
 *</b>
 */'''
class MethodModifier6 ( AstToken ,IMethodModifier):
    
        def  getsynchronized(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier6, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier6(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier6(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier6(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier6(self, o)
    

'''/**
 *<b>
*<li>Rule 151:  MethodModifier ::= native
 *</b>
 */'''
class MethodModifier7 ( AstToken ,IMethodModifier):
    
        def  getnative(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier7, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier7(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier7(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier7(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier7(self, o)
    

'''/**
 *<b>
*<li>Rule 152:  MethodModifier ::= strictfp
 *</b>
 */'''
class MethodModifier8 ( AstToken ,IMethodModifier):
    
        def  getstrictfp(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(MethodModifier8, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitMethodModifier8(self)
        def  acceptWithArg(self, v, o):  v.visitMethodModifier8(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodModifier8(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodModifier8(self, o)
    

'''/**
 *<b>
*<li>Rule 168:  ConstructorModifier ::= public
 *</b>
 */'''
class ConstructorModifier0 ( AstToken ,IConstructorModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ConstructorModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitConstructorModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 169:  ConstructorModifier ::= protected
 *</b>
 */'''
class ConstructorModifier1 ( AstToken ,IConstructorModifier):
    
        def  getprotected(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ConstructorModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitConstructorModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 170:  ConstructorModifier ::= private
 *</b>
 */'''
class ConstructorModifier2 ( AstToken ,IConstructorModifier):
    
        def  getprivate(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ConstructorModifier2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitConstructorModifier2(self)
        def  acceptWithArg(self, v, o):  v.visitConstructorModifier2(self, o)
        def  acceptWithResult(self, v):  return v.visitConstructorModifier2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstructorModifier2(self, o)
    

'''/**
 *<b>
*<li>Rule 172:  ExplicitConstructorInvocation ::= TypeArgumentsopt this ( ArgumentListopt ) ;
 *</b>
 */'''
class ExplicitConstructorInvocation0 ( Ast ,IExplicitConstructorInvocation):
    

        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getthis(self)  :  return self._this
        def  setthis(self,  _this) :   self._this = _this
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_TypeArgumentsopt', '_this', '_LPAREN', '_ArgumentListopt', '_RPAREN', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _TypeArgumentsopt,
                             _this,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN,
                             _SEMICOLON):
        
            super(ExplicitConstructorInvocation0, self).__init__(leftIToken, rightIToken)

            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._this = _this
            _this.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._this:  _content.add(self._this)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExplicitConstructorInvocation0(self)
        def  acceptWithArg(self, v, o):  v.visitExplicitConstructorInvocation0(self, o)
        def  acceptWithResult(self, v):  return v.visitExplicitConstructorInvocation0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExplicitConstructorInvocation0(self, o)
    

'''/**
 *<b>
*<li>Rule 173:  ExplicitConstructorInvocation ::= TypeArgumentsopt super ( ArgumentListopt ) ;
 *</b>
 */'''
class ExplicitConstructorInvocation1 ( Ast ,IExplicitConstructorInvocation):
    

        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_TypeArgumentsopt', '_super', '_LPAREN', '_ArgumentListopt', '_RPAREN', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _TypeArgumentsopt,
                             _super,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN,
                             _SEMICOLON):
        
            super(ExplicitConstructorInvocation1, self).__init__(leftIToken, rightIToken)

            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._super = _super
            _super.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._super:  _content.add(self._super)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExplicitConstructorInvocation1(self)
        def  acceptWithArg(self, v, o):  v.visitExplicitConstructorInvocation1(self, o)
        def  acceptWithResult(self, v):  return v.visitExplicitConstructorInvocation1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExplicitConstructorInvocation1(self, o)
    

'''/**
 *<b>
*<li>Rule 174:  ExplicitConstructorInvocation ::= Primary . TypeArgumentsopt super ( ArgumentListopt ) ;
 *</b>
 */'''
class ExplicitConstructorInvocation2 ( Ast ,IExplicitConstructorInvocation):
    

        def  getPrimary(self)  :  return self._Primary
        def  setPrimary(self,  _Primary) :   self._Primary = _Primary
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_Primary', '_DOT', '_TypeArgumentsopt', '_super', '_LPAREN', '_ArgumentListopt', '_RPAREN', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _Primary,
                             _DOT,
                             _TypeArgumentsopt,
                             _super,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN,
                             _SEMICOLON):
        
            super(ExplicitConstructorInvocation2, self).__init__(leftIToken, rightIToken)

            self._Primary = _Primary
            _Primary.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._super = _super
            _super.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Primary:  _content.add(self._Primary)
            if self._DOT:  _content.add(self._DOT)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._super:  _content.add(self._super)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExplicitConstructorInvocation2(self)
        def  acceptWithArg(self, v, o):  v.visitExplicitConstructorInvocation2(self, o)
        def  acceptWithResult(self, v):  return v.visitExplicitConstructorInvocation2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExplicitConstructorInvocation2(self, o)
    

'''/**
 *<b>
*<li>Rule 188:  InterfaceModifier ::= public
 *</b>
 */'''
class InterfaceModifier0 ( AstToken ,IInterfaceModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 189:  InterfaceModifier ::= protected
 *</b>
 */'''
class InterfaceModifier1 ( AstToken ,IInterfaceModifier):
    
        def  getprotected(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 190:  InterfaceModifier ::= private
 *</b>
 */'''
class InterfaceModifier2 ( AstToken ,IInterfaceModifier):
    
        def  getprivate(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceModifier2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifier2(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifier2(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifier2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifier2(self, o)
    

'''/**
 *<b>
*<li>Rule 191:  InterfaceModifier ::= abstract
 *</b>
 */'''
class InterfaceModifier3 ( AstToken ,IInterfaceModifier):
    
        def  getabstract(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceModifier3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifier3(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifier3(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifier3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifier3(self, o)
    

'''/**
 *<b>
*<li>Rule 192:  InterfaceModifier ::= static
 *</b>
 */'''
class InterfaceModifier4 ( AstToken ,IInterfaceModifier):
    
        def  getstatic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceModifier4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifier4(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifier4(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifier4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifier4(self, o)
    

'''/**
 *<b>
*<li>Rule 193:  InterfaceModifier ::= strictfp
 *</b>
 */'''
class InterfaceModifier5 ( AstToken ,IInterfaceModifier):
    
        def  getstrictfp(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(InterfaceModifier5, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitInterfaceModifier5(self)
        def  acceptWithArg(self, v, o):  v.visitInterfaceModifier5(self, o)
        def  acceptWithResult(self, v):  return v.visitInterfaceModifier5(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitInterfaceModifier5(self, o)
    

'''/**
 *<b>
*<li>Rule 194:  ExtendsInterfaces ::= extends InterfaceType
 *</b>
 */'''
class ExtendsInterfaces0 ( Ast ,IExtendsInterfaces):
    

        def  getextends(self)  :  return self._extends
        def  setextends(self,  _extends) :   self._extends = _extends
        def  getInterfaceType(self)  :  return self._InterfaceType
        def  setInterfaceType(self,  _InterfaceType) :   self._InterfaceType = _InterfaceType

        __slots__ = ('_extends', '_InterfaceType')

        def __init__(self, leftIToken, rightIToken,
                             _extends,
                             _InterfaceType):
        
            super(ExtendsInterfaces0, self).__init__(leftIToken, rightIToken)

            self._extends = _extends
            _extends.setParent(self)
            self._InterfaceType = _InterfaceType
            _InterfaceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._extends:  _content.add(self._extends)
            if self._InterfaceType:  _content.add(self._InterfaceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExtendsInterfaces0(self)
        def  acceptWithArg(self, v, o):  v.visitExtendsInterfaces0(self, o)
        def  acceptWithResult(self, v):  return v.visitExtendsInterfaces0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExtendsInterfaces0(self, o)
    

'''/**
 *<b>
*<li>Rule 195:  ExtendsInterfaces ::= ExtendsInterfaces , InterfaceType
 *</b>
 */'''
class ExtendsInterfaces1 ( Ast ,IExtendsInterfaces):
    

        def  getExtendsInterfaces(self)  :  return self._ExtendsInterfaces
        def  setExtendsInterfaces(self,  _ExtendsInterfaces) :   self._ExtendsInterfaces = _ExtendsInterfaces
        def  getCOMMA(self)  :  return self._COMMA
        def  setCOMMA(self,  _COMMA) :   self._COMMA = _COMMA
        def  getInterfaceType(self)  :  return self._InterfaceType
        def  setInterfaceType(self,  _InterfaceType) :   self._InterfaceType = _InterfaceType

        __slots__ = ('_ExtendsInterfaces', '_COMMA', '_InterfaceType')

        def __init__(self, leftIToken, rightIToken,
                             _ExtendsInterfaces,
                             _COMMA,
                             _InterfaceType):
        
            super(ExtendsInterfaces1, self).__init__(leftIToken, rightIToken)

            self._ExtendsInterfaces = _ExtendsInterfaces
            _ExtendsInterfaces.setParent(self)
            self._COMMA = _COMMA
            _COMMA.setParent(self)
            self._InterfaceType = _InterfaceType
            _InterfaceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ExtendsInterfaces:  _content.add(self._ExtendsInterfaces)
            if self._COMMA:  _content.add(self._COMMA)
            if self._InterfaceType:  _content.add(self._InterfaceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitExtendsInterfaces1(self)
        def  acceptWithArg(self, v, o):  v.visitExtendsInterfaces1(self, o)
        def  acceptWithResult(self, v):  return v.visitExtendsInterfaces1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitExtendsInterfaces1(self, o)
    

'''/**
 *<b>
*<li>Rule 208:  ConstantModifier ::= public
 *</b>
 */'''
class ConstantModifier0 ( AstToken ,IConstantModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ConstantModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitConstantModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitConstantModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitConstantModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstantModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 209:  ConstantModifier ::= static
 *</b>
 */'''
class ConstantModifier1 ( AstToken ,IConstantModifier):
    
        def  getstatic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ConstantModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitConstantModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitConstantModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitConstantModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstantModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 210:  ConstantModifier ::= final
 *</b>
 */'''
class ConstantModifier2 ( AstToken ,IConstantModifier):
    
        def  getfinal(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(ConstantModifier2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitConstantModifier2(self)
        def  acceptWithArg(self, v, o):  v.visitConstantModifier2(self, o)
        def  acceptWithResult(self, v):  return v.visitConstantModifier2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitConstantModifier2(self, o)
    

'''/**
 *<b>
*<li>Rule 215:  AbstractMethodModifier ::= public
 *</b>
 */'''
class AbstractMethodModifier0 ( AstToken ,IAbstractMethodModifier):
    
        def  getpublic(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AbstractMethodModifier0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAbstractMethodModifier0(self)
        def  acceptWithArg(self, v, o):  v.visitAbstractMethodModifier0(self, o)
        def  acceptWithResult(self, v):  return v.visitAbstractMethodModifier0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAbstractMethodModifier0(self, o)
    

'''/**
 *<b>
*<li>Rule 216:  AbstractMethodModifier ::= abstract
 *</b>
 */'''
class AbstractMethodModifier1 ( AstToken ,IAbstractMethodModifier):
    
        def  getabstract(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AbstractMethodModifier1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAbstractMethodModifier1(self)
        def  acceptWithArg(self, v, o):  v.visitAbstractMethodModifier1(self, o)
        def  acceptWithResult(self, v):  return v.visitAbstractMethodModifier1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAbstractMethodModifier1(self, o)
    

'''/**
 *<b>
*<li>Rule 221:  AnnotationTypeElementDeclaration ::= AbstractMethodModifiersopt Type identifier ( ) DefaultValueopt ;
 *</b>
 */'''
class AnnotationTypeElementDeclaration0 ( Ast ,IAnnotationTypeElementDeclaration):
    

        '''/**
         * The value returned by <b>getAbstractMethodModifiersopt</b> may be <b>null</b>
         */'''
        def  getAbstractMethodModifiersopt(self)  :  return self._AbstractMethodModifiersopt
        def  setAbstractMethodModifiersopt(self,  _AbstractMethodModifiersopt) :   self._AbstractMethodModifiersopt = _AbstractMethodModifiersopt
        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        '''/**
         * The value returned by <b>getDefaultValueopt</b> may be <b>null</b>
         */'''
        def  getDefaultValueopt(self)  :  return self._DefaultValueopt
        def  setDefaultValueopt(self,  _DefaultValueopt) :   self._DefaultValueopt = _DefaultValueopt
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_AbstractMethodModifiersopt', '_Type', '_identifier', '_LPAREN', '_RPAREN', '_DefaultValueopt', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _AbstractMethodModifiersopt,
                             _Type,
                             _identifier,
                             _LPAREN,
                             _RPAREN,
                             _DefaultValueopt,
                             _SEMICOLON):
        
            super(AnnotationTypeElementDeclaration0, self).__init__(leftIToken, rightIToken)

            self._AbstractMethodModifiersopt = _AbstractMethodModifiersopt
            if _AbstractMethodModifiersopt: _AbstractMethodModifiersopt.setParent(self)
            self._Type = _Type
            _Type.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._DefaultValueopt = _DefaultValueopt
            if _DefaultValueopt: _DefaultValueopt.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AbstractMethodModifiersopt:  _content.add(self._AbstractMethodModifiersopt)
            if self._Type:  _content.add(self._Type)
            if self._identifier:  _content.add(self._identifier)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._DefaultValueopt:  _content.add(self._DefaultValueopt)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAnnotationTypeElementDeclaration0(self)
        def  acceptWithArg(self, v, o):  v.visitAnnotationTypeElementDeclaration0(self, o)
        def  acceptWithResult(self, v):  return v.visitAnnotationTypeElementDeclaration0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAnnotationTypeElementDeclaration0(self, o)
    

'''/**
 *<b>
*<li>Rule 227:  AnnotationTypeElementDeclaration ::= ;
 *</b>
 */'''
class AnnotationTypeElementDeclaration1 ( AstToken ,IAnnotationTypeElementDeclaration):
    
        def  getSEMICOLON(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AnnotationTypeElementDeclaration1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAnnotationTypeElementDeclaration1(self)
        def  acceptWithArg(self, v, o):  v.visitAnnotationTypeElementDeclaration1(self, o)
        def  acceptWithResult(self, v):  return v.visitAnnotationTypeElementDeclaration1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAnnotationTypeElementDeclaration1(self, o)
    

'''/**
 *<b>
*<li>Rule 295:  AssertStatement ::= assert Expression ;
 *</b>
 */'''
class AssertStatement0 ( Ast ,IAssertStatement):
    

        def  getassert(self)  :  return self._assert
        def  setassert(self,  _assert) :   self._assert = _assert
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_assert', '_Expression', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _assert,
                             _Expression,
                             _SEMICOLON):
        
            super(AssertStatement0, self).__init__(leftIToken, rightIToken)

            self._assert = _assert
            _assert.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._assert:  _content.add(self._assert)
            if self._Expression:  _content.add(self._Expression)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAssertStatement0(self)
        def  acceptWithArg(self, v, o):  v.visitAssertStatement0(self, o)
        def  acceptWithResult(self, v):  return v.visitAssertStatement0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssertStatement0(self, o)
    

'''/**
 *<b>
*<li>Rule 296:  AssertStatement ::= assert Expression : Expression ;
 *</b>
 */'''
class AssertStatement1 ( Ast ,IAssertStatement):
    

        def  getassert(self)  :  return self._assert
        def  setassert(self,  _assert) :   self._assert = _assert
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON
        def  getExpression4(self)  :  return self._Expression4
        def  setExpression4(self,  _Expression4) :   self._Expression4 = _Expression4
        def  getSEMICOLON(self)  :  return self._SEMICOLON
        def  setSEMICOLON(self,  _SEMICOLON) :   self._SEMICOLON = _SEMICOLON

        __slots__ = ('_assert', '_Expression', '_COLON', '_Expression4', '_SEMICOLON')

        def __init__(self, leftIToken, rightIToken,
                             _assert,
                             _Expression,
                             _COLON,
                             _Expression4,
                             _SEMICOLON):
        
            super(AssertStatement1, self).__init__(leftIToken, rightIToken)

            self._assert = _assert
            _assert.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self._Expression4 = _Expression4
            _Expression4.setParent(self)
            self._SEMICOLON = _SEMICOLON
            _SEMICOLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._assert:  _content.add(self._assert)
            if self._Expression:  _content.add(self._Expression)
            if self._COLON:  _content.add(self._COLON)
            if self._Expression4:  _content.add(self._Expression4)
            if self._SEMICOLON:  _content.add(self._SEMICOLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAssertStatement1(self)
        def  acceptWithArg(self, v, o):  v.visitAssertStatement1(self, o)
        def  acceptWithResult(self, v):  return v.visitAssertStatement1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssertStatement1(self, o)
    

'''/**
 *<b>
*<li>Rule 304:  SwitchLabel ::= case ConstantExpression :
 *</b>
 */'''
class SwitchLabel0 ( Ast ,ISwitchLabel):
    

        def  getcase(self)  :  return self._case
        def  setcase(self,  _case) :   self._case = _case
        def  getConstantExpression(self)  :  return self._ConstantExpression
        def  setConstantExpression(self,  _ConstantExpression) :   self._ConstantExpression = _ConstantExpression
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON

        __slots__ = ('_case', '_ConstantExpression', '_COLON')

        def __init__(self, leftIToken, rightIToken,
                             _case,
                             _ConstantExpression,
                             _COLON):
        
            super(SwitchLabel0, self).__init__(leftIToken, rightIToken)

            self._case = _case
            _case.setParent(self)
            self._ConstantExpression = _ConstantExpression
            _ConstantExpression.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._case:  _content.add(self._case)
            if self._ConstantExpression:  _content.add(self._ConstantExpression)
            if self._COLON:  _content.add(self._COLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchLabel0(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchLabel0(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchLabel0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchLabel0(self, o)
    

'''/**
 *<b>
*<li>Rule 305:  SwitchLabel ::= case EnumConstant :
 *</b>
 */'''
class SwitchLabel1 ( Ast ,ISwitchLabel):
    

        def  getcase(self)  :  return self._case
        def  setcase(self,  _case) :   self._case = _case
        def  getEnumConstant(self)  :  return self._EnumConstant
        def  setEnumConstant(self,  _EnumConstant) :   self._EnumConstant = _EnumConstant
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON

        __slots__ = ('_case', '_EnumConstant', '_COLON')

        def __init__(self, leftIToken, rightIToken,
                             _case,
                             _EnumConstant,
                             _COLON):
        
            super(SwitchLabel1, self).__init__(leftIToken, rightIToken)

            self._case = _case
            _case.setParent(self)
            self._EnumConstant = _EnumConstant
            _EnumConstant.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._case:  _content.add(self._case)
            if self._EnumConstant:  _content.add(self._EnumConstant)
            if self._COLON:  _content.add(self._COLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchLabel1(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchLabel1(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchLabel1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchLabel1(self, o)
    

'''/**
 *<b>
*<li>Rule 306:  SwitchLabel ::= default :
 *</b>
 */'''
class SwitchLabel2 ( Ast ,ISwitchLabel):
    

        def  getdefault(self)  :  return self._default
        def  setdefault(self,  _default) :   self._default = _default
        def  getCOLON(self)  :  return self._COLON
        def  setCOLON(self,  _COLON) :   self._COLON = _COLON

        __slots__ = ('_default', '_COLON')

        def __init__(self, leftIToken, rightIToken,
                             _default,
                             _COLON):
        
            super(SwitchLabel2, self).__init__(leftIToken, rightIToken)

            self._default = _default
            _default.setParent(self)
            self._COLON = _COLON
            _COLON.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._default:  _content.add(self._default)
            if self._COLON:  _content.add(self._COLON)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitSwitchLabel2(self)
        def  acceptWithArg(self, v, o):  v.visitSwitchLabel2(self, o)
        def  acceptWithResult(self, v):  return v.visitSwitchLabel2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitSwitchLabel2(self, o)
    

'''/**
 *<b>
*<li>Rule 326:  TryStatement ::= try Block Catches
 *</b>
 */'''
class TryStatement0 ( Ast ,ITryStatement):
    

        def  gettry(self)  :  return self._try
        def  settry(self,  _try) :   self._try = _try
        def  getBlock(self)  :  return self._Block
        def  setBlock(self,  _Block) :   self._Block = _Block
        def  getCatches(self)  :  return self._Catches
        def  setCatches(self,  _Catches) :   self._Catches = _Catches

        __slots__ = ('_try', '_Block', '_Catches')

        def __init__(self, leftIToken, rightIToken,
                             _try,
                             _Block,
                             _Catches):
        
            super(TryStatement0, self).__init__(leftIToken, rightIToken)

            self._try = _try
            _try.setParent(self)
            self._Block = _Block
            _Block.setParent(self)
            self._Catches = _Catches
            _Catches.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._try:  _content.add(self._try)
            if self._Block:  _content.add(self._Block)
            if self._Catches:  _content.add(self._Catches)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTryStatement0(self)
        def  acceptWithArg(self, v, o):  v.visitTryStatement0(self, o)
        def  acceptWithResult(self, v):  return v.visitTryStatement0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTryStatement0(self, o)
    

'''/**
 *<b>
*<li>Rule 327:  TryStatement ::= try Block Catchesopt Finally
 *</b>
 */'''
class TryStatement1 ( Ast ,ITryStatement):
    

        def  gettry(self)  :  return self._try
        def  settry(self,  _try) :   self._try = _try
        def  getBlock(self)  :  return self._Block
        def  setBlock(self,  _Block) :   self._Block = _Block
        '''/**
         * The value returned by <b>getCatchesopt</b> may be <b>null</b>
         */'''
        def  getCatchesopt(self)  :  return self._Catchesopt
        def  setCatchesopt(self,  _Catchesopt) :   self._Catchesopt = _Catchesopt
        def  getFinally(self)  :  return self._Finally
        def  setFinally(self,  _Finally) :   self._Finally = _Finally

        __slots__ = ('_try', '_Block', '_Catchesopt', '_Finally')

        def __init__(self, leftIToken, rightIToken,
                             _try,
                             _Block,
                             _Catchesopt,
                             _Finally):
        
            super(TryStatement1, self).__init__(leftIToken, rightIToken)

            self._try = _try
            _try.setParent(self)
            self._Block = _Block
            _Block.setParent(self)
            self._Catchesopt = _Catchesopt
            if _Catchesopt: _Catchesopt.setParent(self)
            self._Finally = _Finally
            _Finally.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._try:  _content.add(self._try)
            if self._Block:  _content.add(self._Block)
            if self._Catchesopt:  _content.add(self._Catchesopt)
            if self._Finally:  _content.add(self._Finally)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitTryStatement1(self)
        def  acceptWithArg(self, v, o):  v.visitTryStatement1(self, o)
        def  acceptWithResult(self, v):  return v.visitTryStatement1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitTryStatement1(self, o)
    

'''/**
 *<b>
*<li>Rule 335:  PrimaryNoNewArray ::= Type . class
 *</b>
 */'''
class PrimaryNoNewArray0 ( Ast ,IPrimaryNoNewArray):
    

        def  getType(self)  :  return self._Type
        def  setType(self,  _Type) :   self._Type = _Type
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getclass(self)  :  return self._class
        def  setclass(self,  _class) :   self._class = _class

        __slots__ = ('_Type', '_DOT', '_class')

        def __init__(self, leftIToken, rightIToken,
                             _Type,
                             _DOT,
                             _class):
        
            super(PrimaryNoNewArray0, self).__init__(leftIToken, rightIToken)

            self._Type = _Type
            _Type.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._class = _class
            _class.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Type:  _content.add(self._Type)
            if self._DOT:  _content.add(self._DOT)
            if self._class:  _content.add(self._class)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPrimaryNoNewArray0(self)
        def  acceptWithArg(self, v, o):  v.visitPrimaryNoNewArray0(self, o)
        def  acceptWithResult(self, v):  return v.visitPrimaryNoNewArray0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPrimaryNoNewArray0(self, o)
    

'''/**
 *<b>
*<li>Rule 336:  PrimaryNoNewArray ::= void . class
 *</b>
 */'''
class PrimaryNoNewArray1 ( Ast ,IPrimaryNoNewArray):
    

        def  getvoid(self)  :  return self._void
        def  setvoid(self,  _void) :   self._void = _void
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getclass(self)  :  return self._class
        def  setclass(self,  _class) :   self._class = _class

        __slots__ = ('_void', '_DOT', '_class')

        def __init__(self, leftIToken, rightIToken,
                             _void,
                             _DOT,
                             _class):
        
            super(PrimaryNoNewArray1, self).__init__(leftIToken, rightIToken)

            self._void = _void
            _void.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._class = _class
            _class.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._void:  _content.add(self._void)
            if self._DOT:  _content.add(self._DOT)
            if self._class:  _content.add(self._class)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPrimaryNoNewArray1(self)
        def  acceptWithArg(self, v, o):  v.visitPrimaryNoNewArray1(self, o)
        def  acceptWithResult(self, v):  return v.visitPrimaryNoNewArray1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPrimaryNoNewArray1(self, o)
    

'''/**
 *<b>
*<li>Rule 337:  PrimaryNoNewArray ::= this
 *</b>
 */'''
class PrimaryNoNewArray2 ( AstToken ,IPrimaryNoNewArray):
    
        def  getthis(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(PrimaryNoNewArray2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitPrimaryNoNewArray2(self)
        def  acceptWithArg(self, v, o):  v.visitPrimaryNoNewArray2(self, o)
        def  acceptWithResult(self, v):  return v.visitPrimaryNoNewArray2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPrimaryNoNewArray2(self, o)
    

'''/**
 *<b>
*<li>Rule 338:  PrimaryNoNewArray ::= ClassName . this
 *</b>
 */'''
class PrimaryNoNewArray3 ( Ast ,IPrimaryNoNewArray):
    

        def  getClassName(self)  :  return self._ClassName
        def  setClassName(self,  _ClassName) :   self._ClassName = _ClassName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getthis(self)  :  return self._this
        def  setthis(self,  _this) :   self._this = _this

        __slots__ = ('_ClassName', '_DOT', '_this')

        def __init__(self, leftIToken, rightIToken,
                             _ClassName,
                             _DOT,
                             _this):
        
            super(PrimaryNoNewArray3, self).__init__(leftIToken, rightIToken)

            self._ClassName = _ClassName
            _ClassName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._this = _this
            _this.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassName:  _content.add(self._ClassName)
            if self._DOT:  _content.add(self._DOT)
            if self._this:  _content.add(self._this)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPrimaryNoNewArray3(self)
        def  acceptWithArg(self, v, o):  v.visitPrimaryNoNewArray3(self, o)
        def  acceptWithResult(self, v):  return v.visitPrimaryNoNewArray3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPrimaryNoNewArray3(self, o)
    

'''/**
 *<b>
*<li>Rule 339:  PrimaryNoNewArray ::= ( Expression )
 *</b>
 */'''
class PrimaryNoNewArray4 ( Ast ,IPrimaryNoNewArray):
    

        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_LPAREN', '_Expression', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _LPAREN,
                             _Expression,
                             _RPAREN):
        
            super(PrimaryNoNewArray4, self).__init__(leftIToken, rightIToken)

            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._Expression:  _content.add(self._Expression)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitPrimaryNoNewArray4(self)
        def  acceptWithArg(self, v, o):  v.visitPrimaryNoNewArray4(self, o)
        def  acceptWithResult(self, v):  return v.visitPrimaryNoNewArray4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitPrimaryNoNewArray4(self, o)
    

'''/**
 *<b>
*<li>Rule 344:  Literal ::= IntegerLiteral
 *</b>
 */'''
class Literal0 ( AstToken ,ILiteral):
    
        def  getIntegerLiteral(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral0(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral0(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral0(self, o)
    

'''/**
 *<b>
*<li>Rule 345:  Literal ::= LongLiteral
 *</b>
 */'''
class Literal1 ( AstToken ,ILiteral):
    
        def  getLongLiteral(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral1(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral1(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral1(self, o)
    

'''/**
 *<b>
*<li>Rule 346:  Literal ::= FloatingPointLiteral
 *</b>
 */'''
class Literal2 ( AstToken ,ILiteral):
    
        def  getFloatingPointLiteral(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral2(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral2(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral2(self, o)
    

'''/**
 *<b>
*<li>Rule 347:  Literal ::= DoubleLiteral
 *</b>
 */'''
class Literal3 ( AstToken ,ILiteral):
    
        def  getDoubleLiteral(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral3(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral3(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral3(self, o)
    

'''/**
 *<b>
*<li>Rule 349:  Literal ::= CharacterLiteral
 *</b>
 */'''
class Literal4 ( AstToken ,ILiteral):
    
        def  getCharacterLiteral(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral4(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral4(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral4(self, o)
    

'''/**
 *<b>
*<li>Rule 350:  Literal ::= StringLiteral
 *</b>
 */'''
class Literal5 ( AstToken ,ILiteral):
    
        def  getStringLiteral(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal5, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral5(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral5(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral5(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral5(self, o)
    

'''/**
 *<b>
*<li>Rule 351:  Literal ::= null
 *</b>
 */'''
class Literal6 ( AstToken ,ILiteral):
    
        def  getnull(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(Literal6, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitLiteral6(self)
        def  acceptWithArg(self, v, o):  v.visitLiteral6(self, o)
        def  acceptWithResult(self, v):  return v.visitLiteral6(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitLiteral6(self, o)
    

'''/**
 *<b>
*<li>Rule 352:  BooleanLiteral ::= true
 *</b>
 */'''
class BooleanLiteral0 ( AstToken ,IBooleanLiteral):
    
        def  gettrue(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(BooleanLiteral0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitBooleanLiteral0(self)
        def  acceptWithArg(self, v, o):  v.visitBooleanLiteral0(self, o)
        def  acceptWithResult(self, v):  return v.visitBooleanLiteral0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitBooleanLiteral0(self, o)
    

'''/**
 *<b>
*<li>Rule 353:  BooleanLiteral ::= false
 *</b>
 */'''
class BooleanLiteral1 ( AstToken ,IBooleanLiteral):
    
        def  getfalse(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(BooleanLiteral1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitBooleanLiteral1(self)
        def  acceptWithArg(self, v, o):  v.visitBooleanLiteral1(self, o)
        def  acceptWithResult(self, v):  return v.visitBooleanLiteral1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitBooleanLiteral1(self, o)
    

'''/**
 *<b>
*<li>Rule 354:  ClassInstanceCreationExpression ::= new TypeArgumentsopt ClassOrInterfaceType TypeArgumentsopt ( ArgumentListopt ) ClassBodyopt
 *</b>
 */'''
class ClassInstanceCreationExpression0 ( Ast ,IClassInstanceCreationExpression):
    

        def  getnew(self)  :  return self._new
        def  setnew(self,  _new) :   self._new = _new
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getClassOrInterfaceType(self)  :  return self._ClassOrInterfaceType
        def  setClassOrInterfaceType(self,  _ClassOrInterfaceType) :   self._ClassOrInterfaceType = _ClassOrInterfaceType
        '''/**
         * The value returned by <b>getTypeArgumentsopt4</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt4(self)  :  return self._TypeArgumentsopt4
        def  setTypeArgumentsopt4(self,  _TypeArgumentsopt4) :   self._TypeArgumentsopt4 = _TypeArgumentsopt4
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        '''/**
         * The value returned by <b>getClassBodyopt</b> may be <b>null</b>
         */'''
        def  getClassBodyopt(self)  :  return self._ClassBodyopt
        def  setClassBodyopt(self,  _ClassBodyopt) :   self._ClassBodyopt = _ClassBodyopt

        __slots__ = ('_new', '_TypeArgumentsopt', '_ClassOrInterfaceType', '_TypeArgumentsopt4', '_LPAREN', '_ArgumentListopt', '_RPAREN', '_ClassBodyopt')

        def __init__(self, leftIToken, rightIToken,
                             _new,
                             _TypeArgumentsopt,
                             _ClassOrInterfaceType,
                             _TypeArgumentsopt4,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN,
                             _ClassBodyopt):
        
            super(ClassInstanceCreationExpression0, self).__init__(leftIToken, rightIToken)

            self._new = _new
            _new.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._ClassOrInterfaceType = _ClassOrInterfaceType
            _ClassOrInterfaceType.setParent(self)
            self._TypeArgumentsopt4 = _TypeArgumentsopt4
            if _TypeArgumentsopt4: _TypeArgumentsopt4.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._ClassBodyopt = _ClassBodyopt
            if _ClassBodyopt: _ClassBodyopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._new:  _content.add(self._new)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._ClassOrInterfaceType:  _content.add(self._ClassOrInterfaceType)
            if self._TypeArgumentsopt4:  _content.add(self._TypeArgumentsopt4)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._ClassBodyopt:  _content.add(self._ClassBodyopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitClassInstanceCreationExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitClassInstanceCreationExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitClassInstanceCreationExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassInstanceCreationExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 355:  ClassInstanceCreationExpression ::= Primary . new TypeArgumentsopt identifier TypeArgumentsopt ( ArgumentListopt ) ClassBodyopt
 *</b>
 */'''
class ClassInstanceCreationExpression1 ( Ast ,IClassInstanceCreationExpression):
    

        def  getPrimary(self)  :  return self._Primary
        def  setPrimary(self,  _Primary) :   self._Primary = _Primary
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getnew(self)  :  return self._new
        def  setnew(self,  _new) :   self._new = _new
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        '''/**
         * The value returned by <b>getTypeArgumentsopt6</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt6(self)  :  return self._TypeArgumentsopt6
        def  setTypeArgumentsopt6(self,  _TypeArgumentsopt6) :   self._TypeArgumentsopt6 = _TypeArgumentsopt6
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        '''/**
         * The value returned by <b>getClassBodyopt</b> may be <b>null</b>
         */'''
        def  getClassBodyopt(self)  :  return self._ClassBodyopt
        def  setClassBodyopt(self,  _ClassBodyopt) :   self._ClassBodyopt = _ClassBodyopt

        __slots__ = ('_Primary', '_DOT', '_new', '_TypeArgumentsopt', '_identifier', '_TypeArgumentsopt6', '_LPAREN', '_ArgumentListopt', '_RPAREN', '_ClassBodyopt')

        def __init__(self, leftIToken, rightIToken,
                             _Primary,
                             _DOT,
                             _new,
                             _TypeArgumentsopt,
                             _identifier,
                             _TypeArgumentsopt6,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN,
                             _ClassBodyopt):
        
            super(ClassInstanceCreationExpression1, self).__init__(leftIToken, rightIToken)

            self._Primary = _Primary
            _Primary.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._new = _new
            _new.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._TypeArgumentsopt6 = _TypeArgumentsopt6
            if _TypeArgumentsopt6: _TypeArgumentsopt6.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._ClassBodyopt = _ClassBodyopt
            if _ClassBodyopt: _ClassBodyopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Primary:  _content.add(self._Primary)
            if self._DOT:  _content.add(self._DOT)
            if self._new:  _content.add(self._new)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._identifier:  _content.add(self._identifier)
            if self._TypeArgumentsopt6:  _content.add(self._TypeArgumentsopt6)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._ClassBodyopt:  _content.add(self._ClassBodyopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitClassInstanceCreationExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitClassInstanceCreationExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitClassInstanceCreationExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitClassInstanceCreationExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 358:  ArrayCreationExpression ::= new PrimitiveType DimExprs Dimsopt
 *</b>
 */'''
class ArrayCreationExpression0 ( Ast ,IArrayCreationExpression):
    

        def  getnew(self)  :  return self._new
        def  setnew(self,  _new) :   self._new = _new
        def  getPrimitiveType(self)  :  return self._PrimitiveType
        def  setPrimitiveType(self,  _PrimitiveType) :   self._PrimitiveType = _PrimitiveType
        def  getDimExprs(self)  :  return self._DimExprs
        def  setDimExprs(self,  _DimExprs) :   self._DimExprs = _DimExprs
        '''/**
         * The value returned by <b>getDimsopt</b> may be <b>null</b>
         */'''
        def  getDimsopt(self)  :  return self._Dimsopt
        def  setDimsopt(self,  _Dimsopt) :   self._Dimsopt = _Dimsopt

        __slots__ = ('_new', '_PrimitiveType', '_DimExprs', '_Dimsopt')

        def __init__(self, leftIToken, rightIToken,
                             _new,
                             _PrimitiveType,
                             _DimExprs,
                             _Dimsopt):
        
            super(ArrayCreationExpression0, self).__init__(leftIToken, rightIToken)

            self._new = _new
            _new.setParent(self)
            self._PrimitiveType = _PrimitiveType
            _PrimitiveType.setParent(self)
            self._DimExprs = _DimExprs
            _DimExprs.setParent(self)
            self._Dimsopt = _Dimsopt
            if _Dimsopt: _Dimsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._new:  _content.add(self._new)
            if self._PrimitiveType:  _content.add(self._PrimitiveType)
            if self._DimExprs:  _content.add(self._DimExprs)
            if self._Dimsopt:  _content.add(self._Dimsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayCreationExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitArrayCreationExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayCreationExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayCreationExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 359:  ArrayCreationExpression ::= new ClassOrInterfaceType DimExprs Dimsopt
 *</b>
 */'''
class ArrayCreationExpression1 ( Ast ,IArrayCreationExpression):
    

        def  getnew(self)  :  return self._new
        def  setnew(self,  _new) :   self._new = _new
        def  getClassOrInterfaceType(self)  :  return self._ClassOrInterfaceType
        def  setClassOrInterfaceType(self,  _ClassOrInterfaceType) :   self._ClassOrInterfaceType = _ClassOrInterfaceType
        def  getDimExprs(self)  :  return self._DimExprs
        def  setDimExprs(self,  _DimExprs) :   self._DimExprs = _DimExprs
        '''/**
         * The value returned by <b>getDimsopt</b> may be <b>null</b>
         */'''
        def  getDimsopt(self)  :  return self._Dimsopt
        def  setDimsopt(self,  _Dimsopt) :   self._Dimsopt = _Dimsopt

        __slots__ = ('_new', '_ClassOrInterfaceType', '_DimExprs', '_Dimsopt')

        def __init__(self, leftIToken, rightIToken,
                             _new,
                             _ClassOrInterfaceType,
                             _DimExprs,
                             _Dimsopt):
        
            super(ArrayCreationExpression1, self).__init__(leftIToken, rightIToken)

            self._new = _new
            _new.setParent(self)
            self._ClassOrInterfaceType = _ClassOrInterfaceType
            _ClassOrInterfaceType.setParent(self)
            self._DimExprs = _DimExprs
            _DimExprs.setParent(self)
            self._Dimsopt = _Dimsopt
            if _Dimsopt: _Dimsopt.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._new:  _content.add(self._new)
            if self._ClassOrInterfaceType:  _content.add(self._ClassOrInterfaceType)
            if self._DimExprs:  _content.add(self._DimExprs)
            if self._Dimsopt:  _content.add(self._Dimsopt)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayCreationExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitArrayCreationExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayCreationExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayCreationExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 360:  ArrayCreationExpression ::= new PrimitiveType Dims ArrayInitializer
 *</b>
 */'''
class ArrayCreationExpression2 ( Ast ,IArrayCreationExpression):
    

        def  getnew(self)  :  return self._new
        def  setnew(self,  _new) :   self._new = _new
        def  getPrimitiveType(self)  :  return self._PrimitiveType
        def  setPrimitiveType(self,  _PrimitiveType) :   self._PrimitiveType = _PrimitiveType
        def  getDims(self)  :  return self._Dims
        def  setDims(self,  _Dims) :   self._Dims = _Dims
        def  getArrayInitializer(self)  :  return self._ArrayInitializer
        def  setArrayInitializer(self,  _ArrayInitializer) :   self._ArrayInitializer = _ArrayInitializer

        __slots__ = ('_new', '_PrimitiveType', '_Dims', '_ArrayInitializer')

        def __init__(self, leftIToken, rightIToken,
                             _new,
                             _PrimitiveType,
                             _Dims,
                             _ArrayInitializer):
        
            super(ArrayCreationExpression2, self).__init__(leftIToken, rightIToken)

            self._new = _new
            _new.setParent(self)
            self._PrimitiveType = _PrimitiveType
            _PrimitiveType.setParent(self)
            self._Dims = _Dims
            _Dims.setParent(self)
            self._ArrayInitializer = _ArrayInitializer
            _ArrayInitializer.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._new:  _content.add(self._new)
            if self._PrimitiveType:  _content.add(self._PrimitiveType)
            if self._Dims:  _content.add(self._Dims)
            if self._ArrayInitializer:  _content.add(self._ArrayInitializer)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayCreationExpression2(self)
        def  acceptWithArg(self, v, o):  v.visitArrayCreationExpression2(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayCreationExpression2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayCreationExpression2(self, o)
    

'''/**
 *<b>
*<li>Rule 361:  ArrayCreationExpression ::= new ClassOrInterfaceType Dims ArrayInitializer
 *</b>
 */'''
class ArrayCreationExpression3 ( Ast ,IArrayCreationExpression):
    

        def  getnew(self)  :  return self._new
        def  setnew(self,  _new) :   self._new = _new
        def  getClassOrInterfaceType(self)  :  return self._ClassOrInterfaceType
        def  setClassOrInterfaceType(self,  _ClassOrInterfaceType) :   self._ClassOrInterfaceType = _ClassOrInterfaceType
        def  getDims(self)  :  return self._Dims
        def  setDims(self,  _Dims) :   self._Dims = _Dims
        def  getArrayInitializer(self)  :  return self._ArrayInitializer
        def  setArrayInitializer(self,  _ArrayInitializer) :   self._ArrayInitializer = _ArrayInitializer

        __slots__ = ('_new', '_ClassOrInterfaceType', '_Dims', '_ArrayInitializer')

        def __init__(self, leftIToken, rightIToken,
                             _new,
                             _ClassOrInterfaceType,
                             _Dims,
                             _ArrayInitializer):
        
            super(ArrayCreationExpression3, self).__init__(leftIToken, rightIToken)

            self._new = _new
            _new.setParent(self)
            self._ClassOrInterfaceType = _ClassOrInterfaceType
            _ClassOrInterfaceType.setParent(self)
            self._Dims = _Dims
            _Dims.setParent(self)
            self._ArrayInitializer = _ArrayInitializer
            _ArrayInitializer.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._new:  _content.add(self._new)
            if self._ClassOrInterfaceType:  _content.add(self._ClassOrInterfaceType)
            if self._Dims:  _content.add(self._Dims)
            if self._ArrayInitializer:  _content.add(self._ArrayInitializer)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayCreationExpression3(self)
        def  acceptWithArg(self, v, o):  v.visitArrayCreationExpression3(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayCreationExpression3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayCreationExpression3(self, o)
    

'''/**
 *<b>
*<li>Rule 365:  Dims ::= [ ]
 *</b>
 */'''
class Dims0 ( Ast ,IDims):
    

        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_LBRACKET', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _LBRACKET,
                             _RBRACKET):
        
            super(Dims0, self).__init__(leftIToken, rightIToken)

            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitDims0(self)
        def  acceptWithArg(self, v, o):  v.visitDims0(self, o)
        def  acceptWithResult(self, v):  return v.visitDims0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitDims0(self, o)
    

'''/**
 *<b>
*<li>Rule 366:  Dims ::= Dims [ ]
 *</b>
 */'''
class Dims1 ( Ast ,IDims):
    

        def  getDims(self)  :  return self._Dims
        def  setDims(self,  _Dims) :   self._Dims = _Dims
        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_Dims', '_LBRACKET', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _Dims,
                             _LBRACKET,
                             _RBRACKET):
        
            super(Dims1, self).__init__(leftIToken, rightIToken)

            self._Dims = _Dims
            _Dims.setParent(self)
            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Dims:  _content.add(self._Dims)
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitDims1(self)
        def  acceptWithArg(self, v, o):  v.visitDims1(self, o)
        def  acceptWithResult(self, v):  return v.visitDims1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitDims1(self, o)
    

'''/**
 *<b>
*<li>Rule 367:  FieldAccess ::= Primary . identifier
 *</b>
 */'''
class FieldAccess0 ( Ast ,IFieldAccess):
    

        def  getPrimary(self)  :  return self._Primary
        def  setPrimary(self,  _Primary) :   self._Primary = _Primary
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_Primary', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _Primary,
                             _DOT,
                             _identifier):
        
            super(FieldAccess0, self).__init__(leftIToken, rightIToken)

            self._Primary = _Primary
            _Primary.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Primary:  _content.add(self._Primary)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFieldAccess0(self)
        def  acceptWithArg(self, v, o):  v.visitFieldAccess0(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldAccess0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldAccess0(self, o)
    

'''/**
 *<b>
*<li>Rule 368:  FieldAccess ::= super . identifier
 *</b>
 */'''
class FieldAccess1 ( Ast ,IFieldAccess):
    

        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_super', '_DOT', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _super,
                             _DOT,
                             _identifier):
        
            super(FieldAccess1, self).__init__(leftIToken, rightIToken)

            self._super = _super
            _super.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._super:  _content.add(self._super)
            if self._DOT:  _content.add(self._DOT)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFieldAccess1(self)
        def  acceptWithArg(self, v, o):  v.visitFieldAccess1(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldAccess1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldAccess1(self, o)
    

'''/**
 *<b>
*<li>Rule 369:  FieldAccess ::= ClassName . super . identifier
 *</b>
 */'''
class FieldAccess2 ( Ast ,IFieldAccess):
    

        def  getClassName(self)  :  return self._ClassName
        def  setClassName(self,  _ClassName) :   self._ClassName = _ClassName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getDOT4(self)  :  return self._DOT4
        def  setDOT4(self,  _DOT4) :   self._DOT4 = _DOT4
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier

        __slots__ = ('_ClassName', '_DOT', '_super', '_DOT4', '_identifier')

        def __init__(self, leftIToken, rightIToken,
                             _ClassName,
                             _DOT,
                             _super,
                             _DOT4,
                             _identifier):
        
            super(FieldAccess2, self).__init__(leftIToken, rightIToken)

            self._ClassName = _ClassName
            _ClassName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._super = _super
            _super.setParent(self)
            self._DOT4 = _DOT4
            _DOT4.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassName:  _content.add(self._ClassName)
            if self._DOT:  _content.add(self._DOT)
            if self._super:  _content.add(self._super)
            if self._DOT4:  _content.add(self._DOT4)
            if self._identifier:  _content.add(self._identifier)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitFieldAccess2(self)
        def  acceptWithArg(self, v, o):  v.visitFieldAccess2(self, o)
        def  acceptWithResult(self, v):  return v.visitFieldAccess2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitFieldAccess2(self, o)
    

'''/**
 *<b>
*<li>Rule 370:  MethodInvocation ::= MethodName ( ArgumentListopt )
 *</b>
 */'''
class MethodInvocation0 ( Ast ,IMethodInvocation):
    

        def  getMethodName(self)  :  return self._MethodName
        def  setMethodName(self,  _MethodName) :   self._MethodName = _MethodName
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_MethodName', '_LPAREN', '_ArgumentListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _MethodName,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN):
        
            super(MethodInvocation0, self).__init__(leftIToken, rightIToken)

            self._MethodName = _MethodName
            _MethodName.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MethodName:  _content.add(self._MethodName)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodInvocation0(self)
        def  acceptWithArg(self, v, o):  v.visitMethodInvocation0(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodInvocation0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodInvocation0(self, o)
    

'''/**
 *<b>
*<li>Rule 371:  MethodInvocation ::= Primary . TypeArgumentsopt identifier ( ArgumentListopt )
 *</b>
 */'''
class MethodInvocation1 ( Ast ,IMethodInvocation):
    

        def  getPrimary(self)  :  return self._Primary
        def  setPrimary(self,  _Primary) :   self._Primary = _Primary
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_Primary', '_DOT', '_TypeArgumentsopt', '_identifier', '_LPAREN', '_ArgumentListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _Primary,
                             _DOT,
                             _TypeArgumentsopt,
                             _identifier,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN):
        
            super(MethodInvocation1, self).__init__(leftIToken, rightIToken)

            self._Primary = _Primary
            _Primary.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._Primary:  _content.add(self._Primary)
            if self._DOT:  _content.add(self._DOT)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._identifier:  _content.add(self._identifier)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodInvocation1(self)
        def  acceptWithArg(self, v, o):  v.visitMethodInvocation1(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodInvocation1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodInvocation1(self, o)
    

'''/**
 *<b>
*<li>Rule 372:  MethodInvocation ::= super . TypeArgumentsopt identifier ( ArgumentListopt )
 *</b>
 */'''
class MethodInvocation2 ( Ast ,IMethodInvocation):
    

        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_super', '_DOT', '_TypeArgumentsopt', '_identifier', '_LPAREN', '_ArgumentListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _super,
                             _DOT,
                             _TypeArgumentsopt,
                             _identifier,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN):
        
            super(MethodInvocation2, self).__init__(leftIToken, rightIToken)

            self._super = _super
            _super.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._super:  _content.add(self._super)
            if self._DOT:  _content.add(self._DOT)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._identifier:  _content.add(self._identifier)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodInvocation2(self)
        def  acceptWithArg(self, v, o):  v.visitMethodInvocation2(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodInvocation2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodInvocation2(self, o)
    

'''/**
 *<b>
*<li>Rule 373:  MethodInvocation ::= ClassName . super . TypeArgumentsopt identifier ( ArgumentListopt )
 *</b>
 */'''
class MethodInvocation3 ( Ast ,IMethodInvocation):
    

        def  getClassName(self)  :  return self._ClassName
        def  setClassName(self,  _ClassName) :   self._ClassName = _ClassName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getsuper(self)  :  return self._super
        def  setsuper(self,  _super) :   self._super = _super
        def  getDOT4(self)  :  return self._DOT4
        def  setDOT4(self,  _DOT4) :   self._DOT4 = _DOT4
        '''/**
         * The value returned by <b>getTypeArgumentsopt</b> may be <b>null</b>
         */'''
        def  getTypeArgumentsopt(self)  :  return self._TypeArgumentsopt
        def  setTypeArgumentsopt(self,  _TypeArgumentsopt) :   self._TypeArgumentsopt = _TypeArgumentsopt
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_ClassName', '_DOT', '_super', '_DOT4', '_TypeArgumentsopt', '_identifier', '_LPAREN', '_ArgumentListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _ClassName,
                             _DOT,
                             _super,
                             _DOT4,
                             _TypeArgumentsopt,
                             _identifier,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN):
        
            super(MethodInvocation3, self).__init__(leftIToken, rightIToken)

            self._ClassName = _ClassName
            _ClassName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._super = _super
            _super.setParent(self)
            self._DOT4 = _DOT4
            _DOT4.setParent(self)
            self._TypeArgumentsopt = _TypeArgumentsopt
            if _TypeArgumentsopt: _TypeArgumentsopt.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ClassName:  _content.add(self._ClassName)
            if self._DOT:  _content.add(self._DOT)
            if self._super:  _content.add(self._super)
            if self._DOT4:  _content.add(self._DOT4)
            if self._TypeArgumentsopt:  _content.add(self._TypeArgumentsopt)
            if self._identifier:  _content.add(self._identifier)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodInvocation3(self)
        def  acceptWithArg(self, v, o):  v.visitMethodInvocation3(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodInvocation3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodInvocation3(self, o)
    

'''/**
 *<b>
*<li>Rule 374:  MethodInvocation ::= TypeName . TypeArguments identifier ( ArgumentListopt )
 *</b>
 */'''
class MethodInvocation4 ( Ast ,IMethodInvocation):
    

        def  getTypeName(self)  :  return self._TypeName
        def  setTypeName(self,  _TypeName) :   self._TypeName = _TypeName
        def  getDOT(self)  :  return self._DOT
        def  setDOT(self,  _DOT) :   self._DOT = _DOT
        def  getTypeArguments(self)  :  return self._TypeArguments
        def  setTypeArguments(self,  _TypeArguments) :   self._TypeArguments = _TypeArguments
        def  getidentifier(self)  :  return self._identifier
        def  setidentifier(self,  _identifier) :   self._identifier = _identifier
        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        '''/**
         * The value returned by <b>getArgumentListopt</b> may be <b>null</b>
         */'''
        def  getArgumentListopt(self)  :  return self._ArgumentListopt
        def  setArgumentListopt(self,  _ArgumentListopt) :   self._ArgumentListopt = _ArgumentListopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN

        __slots__ = ('_TypeName', '_DOT', '_TypeArguments', '_identifier', '_LPAREN', '_ArgumentListopt', '_RPAREN')

        def __init__(self, leftIToken, rightIToken,
                             _TypeName,
                             _DOT,
                             _TypeArguments,
                             _identifier,
                             _LPAREN,
                             _ArgumentListopt,
                             _RPAREN):
        
            super(MethodInvocation4, self).__init__(leftIToken, rightIToken)

            self._TypeName = _TypeName
            _TypeName.setParent(self)
            self._DOT = _DOT
            _DOT.setParent(self)
            self._TypeArguments = _TypeArguments
            _TypeArguments.setParent(self)
            self._identifier = _identifier
            _identifier.setParent(self)
            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ArgumentListopt = _ArgumentListopt
            if _ArgumentListopt: _ArgumentListopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TypeName:  _content.add(self._TypeName)
            if self._DOT:  _content.add(self._DOT)
            if self._TypeArguments:  _content.add(self._TypeArguments)
            if self._identifier:  _content.add(self._identifier)
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ArgumentListopt:  _content.add(self._ArgumentListopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMethodInvocation4(self)
        def  acceptWithArg(self, v, o):  v.visitMethodInvocation4(self, o)
        def  acceptWithResult(self, v):  return v.visitMethodInvocation4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMethodInvocation4(self, o)
    

'''/**
 *<b>
*<li>Rule 375:  ArrayAccess ::= ExpressionName [ Expression ]
 *</b>
 */'''
class ArrayAccess0 ( Ast ,IArrayAccess):
    

        def  getExpressionName(self)  :  return self._ExpressionName
        def  setExpressionName(self,  _ExpressionName) :   self._ExpressionName = _ExpressionName
        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_ExpressionName', '_LBRACKET', '_Expression', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _ExpressionName,
                             _LBRACKET,
                             _Expression,
                             _RBRACKET):
        
            super(ArrayAccess0, self).__init__(leftIToken, rightIToken)

            self._ExpressionName = _ExpressionName
            _ExpressionName.setParent(self)
            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ExpressionName:  _content.add(self._ExpressionName)
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._Expression:  _content.add(self._Expression)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayAccess0(self)
        def  acceptWithArg(self, v, o):  v.visitArrayAccess0(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayAccess0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayAccess0(self, o)
    

'''/**
 *<b>
*<li>Rule 376:  ArrayAccess ::= PrimaryNoNewArray [ Expression ]
 *</b>
 */'''
class ArrayAccess1 ( Ast ,IArrayAccess):
    

        def  getPrimaryNoNewArray(self)  :  return self._PrimaryNoNewArray
        def  setPrimaryNoNewArray(self,  _PrimaryNoNewArray) :   self._PrimaryNoNewArray = _PrimaryNoNewArray
        def  getLBRACKET(self)  :  return self._LBRACKET
        def  setLBRACKET(self,  _LBRACKET) :   self._LBRACKET = _LBRACKET
        def  getExpression(self)  :  return self._Expression
        def  setExpression(self,  _Expression) :   self._Expression = _Expression
        def  getRBRACKET(self)  :  return self._RBRACKET
        def  setRBRACKET(self,  _RBRACKET) :   self._RBRACKET = _RBRACKET

        __slots__ = ('_PrimaryNoNewArray', '_LBRACKET', '_Expression', '_RBRACKET')

        def __init__(self, leftIToken, rightIToken,
                             _PrimaryNoNewArray,
                             _LBRACKET,
                             _Expression,
                             _RBRACKET):
        
            super(ArrayAccess1, self).__init__(leftIToken, rightIToken)

            self._PrimaryNoNewArray = _PrimaryNoNewArray
            _PrimaryNoNewArray.setParent(self)
            self._LBRACKET = _LBRACKET
            _LBRACKET.setParent(self)
            self._Expression = _Expression
            _Expression.setParent(self)
            self._RBRACKET = _RBRACKET
            _RBRACKET.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PrimaryNoNewArray:  _content.add(self._PrimaryNoNewArray)
            if self._LBRACKET:  _content.add(self._LBRACKET)
            if self._Expression:  _content.add(self._Expression)
            if self._RBRACKET:  _content.add(self._RBRACKET)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitArrayAccess1(self)
        def  acceptWithArg(self, v, o):  v.visitArrayAccess1(self, o)
        def  acceptWithResult(self, v):  return v.visitArrayAccess1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitArrayAccess1(self, o)
    

'''/**
 *<b>
*<li>Rule 385:  UnaryExpression ::= + UnaryExpression
 *</b>
 */'''
class UnaryExpression0 ( Ast ,IUnaryExpression):
    

        def  getPLUS(self)  :  return self._PLUS
        def  setPLUS(self,  _PLUS) :   self._PLUS = _PLUS
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_PLUS', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _PLUS,
                             _UnaryExpression):
        
            super(UnaryExpression0, self).__init__(leftIToken, rightIToken)

            self._PLUS = _PLUS
            _PLUS.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._PLUS:  _content.add(self._PLUS)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitUnaryExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitUnaryExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitUnaryExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitUnaryExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 386:  UnaryExpression ::= - UnaryExpression
 *</b>
 */'''
class UnaryExpression1 ( Ast ,IUnaryExpression):
    

        def  getMINUS(self)  :  return self._MINUS
        def  setMINUS(self,  _MINUS) :   self._MINUS = _MINUS
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_MINUS', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _MINUS,
                             _UnaryExpression):
        
            super(UnaryExpression1, self).__init__(leftIToken, rightIToken)

            self._MINUS = _MINUS
            _MINUS.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MINUS:  _content.add(self._MINUS)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitUnaryExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitUnaryExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitUnaryExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitUnaryExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 391:  UnaryExpressionNotPlusMinus ::= ~ UnaryExpression
 *</b>
 */'''
class UnaryExpressionNotPlusMinus0 ( Ast ,IUnaryExpressionNotPlusMinus):
    

        def  getTWIDDLE(self)  :  return self._TWIDDLE
        def  setTWIDDLE(self,  _TWIDDLE) :   self._TWIDDLE = _TWIDDLE
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_TWIDDLE', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _TWIDDLE,
                             _UnaryExpression):
        
            super(UnaryExpressionNotPlusMinus0, self).__init__(leftIToken, rightIToken)

            self._TWIDDLE = _TWIDDLE
            _TWIDDLE.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._TWIDDLE:  _content.add(self._TWIDDLE)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitUnaryExpressionNotPlusMinus0(self)
        def  acceptWithArg(self, v, o):  v.visitUnaryExpressionNotPlusMinus0(self, o)
        def  acceptWithResult(self, v):  return v.visitUnaryExpressionNotPlusMinus0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitUnaryExpressionNotPlusMinus0(self, o)
    

'''/**
 *<b>
*<li>Rule 392:  UnaryExpressionNotPlusMinus ::= ! UnaryExpression
 *</b>
 */'''
class UnaryExpressionNotPlusMinus1 ( Ast ,IUnaryExpressionNotPlusMinus):
    

        def  getNOT(self)  :  return self._NOT
        def  setNOT(self,  _NOT) :   self._NOT = _NOT
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_NOT', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _NOT,
                             _UnaryExpression):
        
            super(UnaryExpressionNotPlusMinus1, self).__init__(leftIToken, rightIToken)

            self._NOT = _NOT
            _NOT.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._NOT:  _content.add(self._NOT)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitUnaryExpressionNotPlusMinus1(self)
        def  acceptWithArg(self, v, o):  v.visitUnaryExpressionNotPlusMinus1(self, o)
        def  acceptWithResult(self, v):  return v.visitUnaryExpressionNotPlusMinus1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitUnaryExpressionNotPlusMinus1(self, o)
    

'''/**
 *<b>
*<li>Rule 394:  CastExpression ::= ( PrimitiveType Dimsopt ) UnaryExpression
 *</b>
 */'''
class CastExpression0 ( Ast ,ICastExpression):
    

        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getPrimitiveType(self)  :  return self._PrimitiveType
        def  setPrimitiveType(self,  _PrimitiveType) :   self._PrimitiveType = _PrimitiveType
        '''/**
         * The value returned by <b>getDimsopt</b> may be <b>null</b>
         */'''
        def  getDimsopt(self)  :  return self._Dimsopt
        def  setDimsopt(self,  _Dimsopt) :   self._Dimsopt = _Dimsopt
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_LPAREN', '_PrimitiveType', '_Dimsopt', '_RPAREN', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _LPAREN,
                             _PrimitiveType,
                             _Dimsopt,
                             _RPAREN,
                             _UnaryExpression):
        
            super(CastExpression0, self).__init__(leftIToken, rightIToken)

            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._PrimitiveType = _PrimitiveType
            _PrimitiveType.setParent(self)
            self._Dimsopt = _Dimsopt
            if _Dimsopt: _Dimsopt.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._PrimitiveType:  _content.add(self._PrimitiveType)
            if self._Dimsopt:  _content.add(self._Dimsopt)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitCastExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitCastExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitCastExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitCastExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 395:  CastExpression ::= ( ReferenceType ) UnaryExpressionNotPlusMinus
 *</b>
 */'''
class CastExpression1 ( Ast ,ICastExpression):
    

        def  getLPAREN(self)  :  return self._LPAREN
        def  setLPAREN(self,  _LPAREN) :   self._LPAREN = _LPAREN
        def  getReferenceType(self)  :  return self._ReferenceType
        def  setReferenceType(self,  _ReferenceType) :   self._ReferenceType = _ReferenceType
        def  getRPAREN(self)  :  return self._RPAREN
        def  setRPAREN(self,  _RPAREN) :   self._RPAREN = _RPAREN
        def  getUnaryExpressionNotPlusMinus(self)  :  return self._UnaryExpressionNotPlusMinus
        def  setUnaryExpressionNotPlusMinus(self,  _UnaryExpressionNotPlusMinus) :   self._UnaryExpressionNotPlusMinus = _UnaryExpressionNotPlusMinus

        __slots__ = ('_LPAREN', '_ReferenceType', '_RPAREN', '_UnaryExpressionNotPlusMinus')

        def __init__(self, leftIToken, rightIToken,
                             _LPAREN,
                             _ReferenceType,
                             _RPAREN,
                             _UnaryExpressionNotPlusMinus):
        
            super(CastExpression1, self).__init__(leftIToken, rightIToken)

            self._LPAREN = _LPAREN
            _LPAREN.setParent(self)
            self._ReferenceType = _ReferenceType
            _ReferenceType.setParent(self)
            self._RPAREN = _RPAREN
            _RPAREN.setParent(self)
            self._UnaryExpressionNotPlusMinus = _UnaryExpressionNotPlusMinus
            _UnaryExpressionNotPlusMinus.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._LPAREN:  _content.add(self._LPAREN)
            if self._ReferenceType:  _content.add(self._ReferenceType)
            if self._RPAREN:  _content.add(self._RPAREN)
            if self._UnaryExpressionNotPlusMinus:  _content.add(self._UnaryExpressionNotPlusMinus)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitCastExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitCastExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitCastExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitCastExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 397:  MultiplicativeExpression ::= MultiplicativeExpression * UnaryExpression
 *</b>
 */'''
class MultiplicativeExpression0 ( Ast ,IMultiplicativeExpression):
    

        def  getMultiplicativeExpression(self)  :  return self._MultiplicativeExpression
        def  setMultiplicativeExpression(self,  _MultiplicativeExpression) :   self._MultiplicativeExpression = _MultiplicativeExpression
        def  getMULTIPLY(self)  :  return self._MULTIPLY
        def  setMULTIPLY(self,  _MULTIPLY) :   self._MULTIPLY = _MULTIPLY
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_MultiplicativeExpression', '_MULTIPLY', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _MultiplicativeExpression,
                             _MULTIPLY,
                             _UnaryExpression):
        
            super(MultiplicativeExpression0, self).__init__(leftIToken, rightIToken)

            self._MultiplicativeExpression = _MultiplicativeExpression
            _MultiplicativeExpression.setParent(self)
            self._MULTIPLY = _MULTIPLY
            _MULTIPLY.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MultiplicativeExpression:  _content.add(self._MultiplicativeExpression)
            if self._MULTIPLY:  _content.add(self._MULTIPLY)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMultiplicativeExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitMultiplicativeExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitMultiplicativeExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMultiplicativeExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 398:  MultiplicativeExpression ::= MultiplicativeExpression / UnaryExpression
 *</b>
 */'''
class MultiplicativeExpression1 ( Ast ,IMultiplicativeExpression):
    

        def  getMultiplicativeExpression(self)  :  return self._MultiplicativeExpression
        def  setMultiplicativeExpression(self,  _MultiplicativeExpression) :   self._MultiplicativeExpression = _MultiplicativeExpression
        def  getDIVIDE(self)  :  return self._DIVIDE
        def  setDIVIDE(self,  _DIVIDE) :   self._DIVIDE = _DIVIDE
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_MultiplicativeExpression', '_DIVIDE', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _MultiplicativeExpression,
                             _DIVIDE,
                             _UnaryExpression):
        
            super(MultiplicativeExpression1, self).__init__(leftIToken, rightIToken)

            self._MultiplicativeExpression = _MultiplicativeExpression
            _MultiplicativeExpression.setParent(self)
            self._DIVIDE = _DIVIDE
            _DIVIDE.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MultiplicativeExpression:  _content.add(self._MultiplicativeExpression)
            if self._DIVIDE:  _content.add(self._DIVIDE)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMultiplicativeExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitMultiplicativeExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitMultiplicativeExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMultiplicativeExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 399:  MultiplicativeExpression ::= MultiplicativeExpression % UnaryExpression
 *</b>
 */'''
class MultiplicativeExpression2 ( Ast ,IMultiplicativeExpression):
    

        def  getMultiplicativeExpression(self)  :  return self._MultiplicativeExpression
        def  setMultiplicativeExpression(self,  _MultiplicativeExpression) :   self._MultiplicativeExpression = _MultiplicativeExpression
        def  getREMAINDER(self)  :  return self._REMAINDER
        def  setREMAINDER(self,  _REMAINDER) :   self._REMAINDER = _REMAINDER
        def  getUnaryExpression(self)  :  return self._UnaryExpression
        def  setUnaryExpression(self,  _UnaryExpression) :   self._UnaryExpression = _UnaryExpression

        __slots__ = ('_MultiplicativeExpression', '_REMAINDER', '_UnaryExpression')

        def __init__(self, leftIToken, rightIToken,
                             _MultiplicativeExpression,
                             _REMAINDER,
                             _UnaryExpression):
        
            super(MultiplicativeExpression2, self).__init__(leftIToken, rightIToken)

            self._MultiplicativeExpression = _MultiplicativeExpression
            _MultiplicativeExpression.setParent(self)
            self._REMAINDER = _REMAINDER
            _REMAINDER.setParent(self)
            self._UnaryExpression = _UnaryExpression
            _UnaryExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._MultiplicativeExpression:  _content.add(self._MultiplicativeExpression)
            if self._REMAINDER:  _content.add(self._REMAINDER)
            if self._UnaryExpression:  _content.add(self._UnaryExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitMultiplicativeExpression2(self)
        def  acceptWithArg(self, v, o):  v.visitMultiplicativeExpression2(self, o)
        def  acceptWithResult(self, v):  return v.visitMultiplicativeExpression2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitMultiplicativeExpression2(self, o)
    

'''/**
 *<b>
*<li>Rule 401:  AdditiveExpression ::= AdditiveExpression + MultiplicativeExpression
 *</b>
 */'''
class AdditiveExpression0 ( Ast ,IAdditiveExpression):
    

        def  getAdditiveExpression(self)  :  return self._AdditiveExpression
        def  setAdditiveExpression(self,  _AdditiveExpression) :   self._AdditiveExpression = _AdditiveExpression
        def  getPLUS(self)  :  return self._PLUS
        def  setPLUS(self,  _PLUS) :   self._PLUS = _PLUS
        def  getMultiplicativeExpression(self)  :  return self._MultiplicativeExpression
        def  setMultiplicativeExpression(self,  _MultiplicativeExpression) :   self._MultiplicativeExpression = _MultiplicativeExpression

        __slots__ = ('_AdditiveExpression', '_PLUS', '_MultiplicativeExpression')

        def __init__(self, leftIToken, rightIToken,
                             _AdditiveExpression,
                             _PLUS,
                             _MultiplicativeExpression):
        
            super(AdditiveExpression0, self).__init__(leftIToken, rightIToken)

            self._AdditiveExpression = _AdditiveExpression
            _AdditiveExpression.setParent(self)
            self._PLUS = _PLUS
            _PLUS.setParent(self)
            self._MultiplicativeExpression = _MultiplicativeExpression
            _MultiplicativeExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AdditiveExpression:  _content.add(self._AdditiveExpression)
            if self._PLUS:  _content.add(self._PLUS)
            if self._MultiplicativeExpression:  _content.add(self._MultiplicativeExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAdditiveExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitAdditiveExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitAdditiveExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAdditiveExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 402:  AdditiveExpression ::= AdditiveExpression - MultiplicativeExpression
 *</b>
 */'''
class AdditiveExpression1 ( Ast ,IAdditiveExpression):
    

        def  getAdditiveExpression(self)  :  return self._AdditiveExpression
        def  setAdditiveExpression(self,  _AdditiveExpression) :   self._AdditiveExpression = _AdditiveExpression
        def  getMINUS(self)  :  return self._MINUS
        def  setMINUS(self,  _MINUS) :   self._MINUS = _MINUS
        def  getMultiplicativeExpression(self)  :  return self._MultiplicativeExpression
        def  setMultiplicativeExpression(self,  _MultiplicativeExpression) :   self._MultiplicativeExpression = _MultiplicativeExpression

        __slots__ = ('_AdditiveExpression', '_MINUS', '_MultiplicativeExpression')

        def __init__(self, leftIToken, rightIToken,
                             _AdditiveExpression,
                             _MINUS,
                             _MultiplicativeExpression):
        
            super(AdditiveExpression1, self).__init__(leftIToken, rightIToken)

            self._AdditiveExpression = _AdditiveExpression
            _AdditiveExpression.setParent(self)
            self._MINUS = _MINUS
            _MINUS.setParent(self)
            self._MultiplicativeExpression = _MultiplicativeExpression
            _MultiplicativeExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._AdditiveExpression:  _content.add(self._AdditiveExpression)
            if self._MINUS:  _content.add(self._MINUS)
            if self._MultiplicativeExpression:  _content.add(self._MultiplicativeExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAdditiveExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitAdditiveExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitAdditiveExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAdditiveExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 404:  ShiftExpression ::= ShiftExpression << AdditiveExpression
 *</b>
 */'''
class ShiftExpression0 ( Ast ,IShiftExpression):
    

        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression
        def  getLEFT_SHIFT(self)  :  return self._LEFT_SHIFT
        def  setLEFT_SHIFT(self,  _LEFT_SHIFT) :   self._LEFT_SHIFT = _LEFT_SHIFT
        def  getAdditiveExpression(self)  :  return self._AdditiveExpression
        def  setAdditiveExpression(self,  _AdditiveExpression) :   self._AdditiveExpression = _AdditiveExpression

        __slots__ = ('_ShiftExpression', '_LEFT_SHIFT', '_AdditiveExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ShiftExpression,
                             _LEFT_SHIFT,
                             _AdditiveExpression):
        
            super(ShiftExpression0, self).__init__(leftIToken, rightIToken)

            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self._LEFT_SHIFT = _LEFT_SHIFT
            _LEFT_SHIFT.setParent(self)
            self._AdditiveExpression = _AdditiveExpression
            _AdditiveExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            if self._LEFT_SHIFT:  _content.add(self._LEFT_SHIFT)
            if self._AdditiveExpression:  _content.add(self._AdditiveExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitShiftExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitShiftExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitShiftExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitShiftExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 405:  ShiftExpression ::= ShiftExpression > > AdditiveExpression
 *</b>
 */'''
class ShiftExpression1 ( Ast ,IShiftExpression):
    

        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression
        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER
        def  getGREATER3(self)  :  return self._GREATER3
        def  setGREATER3(self,  _GREATER3) :   self._GREATER3 = _GREATER3
        def  getAdditiveExpression(self)  :  return self._AdditiveExpression
        def  setAdditiveExpression(self,  _AdditiveExpression) :   self._AdditiveExpression = _AdditiveExpression

        __slots__ = ('_ShiftExpression', '_GREATER', '_GREATER3', '_AdditiveExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ShiftExpression,
                             _GREATER,
                             _GREATER3,
                             _AdditiveExpression):
        
            super(ShiftExpression1, self).__init__(leftIToken, rightIToken)

            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self._GREATER3 = _GREATER3
            _GREATER3.setParent(self)
            self._AdditiveExpression = _AdditiveExpression
            _AdditiveExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            if self._GREATER:  _content.add(self._GREATER)
            if self._GREATER3:  _content.add(self._GREATER3)
            if self._AdditiveExpression:  _content.add(self._AdditiveExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitShiftExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitShiftExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitShiftExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitShiftExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 406:  ShiftExpression ::= ShiftExpression > > > AdditiveExpression
 *</b>
 */'''
class ShiftExpression2 ( Ast ,IShiftExpression):
    

        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression
        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER
        def  getGREATER3(self)  :  return self._GREATER3
        def  setGREATER3(self,  _GREATER3) :   self._GREATER3 = _GREATER3
        def  getGREATER4(self)  :  return self._GREATER4
        def  setGREATER4(self,  _GREATER4) :   self._GREATER4 = _GREATER4
        def  getAdditiveExpression(self)  :  return self._AdditiveExpression
        def  setAdditiveExpression(self,  _AdditiveExpression) :   self._AdditiveExpression = _AdditiveExpression

        __slots__ = ('_ShiftExpression', '_GREATER', '_GREATER3', '_GREATER4', '_AdditiveExpression')

        def __init__(self, leftIToken, rightIToken,
                             _ShiftExpression,
                             _GREATER,
                             _GREATER3,
                             _GREATER4,
                             _AdditiveExpression):
        
            super(ShiftExpression2, self).__init__(leftIToken, rightIToken)

            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self._GREATER3 = _GREATER3
            _GREATER3.setParent(self)
            self._GREATER4 = _GREATER4
            _GREATER4.setParent(self)
            self._AdditiveExpression = _AdditiveExpression
            _AdditiveExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            if self._GREATER:  _content.add(self._GREATER)
            if self._GREATER3:  _content.add(self._GREATER3)
            if self._GREATER4:  _content.add(self._GREATER4)
            if self._AdditiveExpression:  _content.add(self._AdditiveExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitShiftExpression2(self)
        def  acceptWithArg(self, v, o):  v.visitShiftExpression2(self, o)
        def  acceptWithResult(self, v):  return v.visitShiftExpression2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitShiftExpression2(self, o)
    

'''/**
 *<b>
*<li>Rule 408:  RelationalExpression ::= RelationalExpression < ShiftExpression
 *</b>
 */'''
class RelationalExpression0 ( Ast ,IRelationalExpression):
    

        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression
        def  getLESS(self)  :  return self._LESS
        def  setLESS(self,  _LESS) :   self._LESS = _LESS
        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression

        __slots__ = ('_RelationalExpression', '_LESS', '_ShiftExpression')

        def __init__(self, leftIToken, rightIToken,
                             _RelationalExpression,
                             _LESS,
                             _ShiftExpression):
        
            super(RelationalExpression0, self).__init__(leftIToken, rightIToken)

            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self._LESS = _LESS
            _LESS.setParent(self)
            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            if self._LESS:  _content.add(self._LESS)
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitRelationalExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitRelationalExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitRelationalExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitRelationalExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 409:  RelationalExpression ::= RelationalExpression > ShiftExpression
 *</b>
 */'''
class RelationalExpression1 ( Ast ,IRelationalExpression):
    

        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression
        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER
        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression

        __slots__ = ('_RelationalExpression', '_GREATER', '_ShiftExpression')

        def __init__(self, leftIToken, rightIToken,
                             _RelationalExpression,
                             _GREATER,
                             _ShiftExpression):
        
            super(RelationalExpression1, self).__init__(leftIToken, rightIToken)

            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            if self._GREATER:  _content.add(self._GREATER)
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitRelationalExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitRelationalExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitRelationalExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitRelationalExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 410:  RelationalExpression ::= RelationalExpression <= ShiftExpression
 *</b>
 */'''
class RelationalExpression2 ( Ast ,IRelationalExpression):
    

        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression
        def  getLESS_EQUAL(self)  :  return self._LESS_EQUAL
        def  setLESS_EQUAL(self,  _LESS_EQUAL) :   self._LESS_EQUAL = _LESS_EQUAL
        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression

        __slots__ = ('_RelationalExpression', '_LESS_EQUAL', '_ShiftExpression')

        def __init__(self, leftIToken, rightIToken,
                             _RelationalExpression,
                             _LESS_EQUAL,
                             _ShiftExpression):
        
            super(RelationalExpression2, self).__init__(leftIToken, rightIToken)

            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self._LESS_EQUAL = _LESS_EQUAL
            _LESS_EQUAL.setParent(self)
            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            if self._LESS_EQUAL:  _content.add(self._LESS_EQUAL)
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitRelationalExpression2(self)
        def  acceptWithArg(self, v, o):  v.visitRelationalExpression2(self, o)
        def  acceptWithResult(self, v):  return v.visitRelationalExpression2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitRelationalExpression2(self, o)
    

'''/**
 *<b>
*<li>Rule 411:  RelationalExpression ::= RelationalExpression > = ShiftExpression
 *</b>
 */'''
class RelationalExpression3 ( Ast ,IRelationalExpression):
    

        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression
        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER
        def  getEQUAL(self)  :  return self._EQUAL
        def  setEQUAL(self,  _EQUAL) :   self._EQUAL = _EQUAL
        def  getShiftExpression(self)  :  return self._ShiftExpression
        def  setShiftExpression(self,  _ShiftExpression) :   self._ShiftExpression = _ShiftExpression

        __slots__ = ('_RelationalExpression', '_GREATER', '_EQUAL', '_ShiftExpression')

        def __init__(self, leftIToken, rightIToken,
                             _RelationalExpression,
                             _GREATER,
                             _EQUAL,
                             _ShiftExpression):
        
            super(RelationalExpression3, self).__init__(leftIToken, rightIToken)

            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self._EQUAL = _EQUAL
            _EQUAL.setParent(self)
            self._ShiftExpression = _ShiftExpression
            _ShiftExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            if self._GREATER:  _content.add(self._GREATER)
            if self._EQUAL:  _content.add(self._EQUAL)
            if self._ShiftExpression:  _content.add(self._ShiftExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitRelationalExpression3(self)
        def  acceptWithArg(self, v, o):  v.visitRelationalExpression3(self, o)
        def  acceptWithResult(self, v):  return v.visitRelationalExpression3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitRelationalExpression3(self, o)
    

'''/**
 *<b>
*<li>Rule 412:  RelationalExpression ::= RelationalExpression instanceof ReferenceType
 *</b>
 */'''
class RelationalExpression4 ( Ast ,IRelationalExpression):
    

        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression
        def  getinstanceof(self)  :  return self._instanceof
        def  setinstanceof(self,  _instanceof) :   self._instanceof = _instanceof
        def  getReferenceType(self)  :  return self._ReferenceType
        def  setReferenceType(self,  _ReferenceType) :   self._ReferenceType = _ReferenceType

        __slots__ = ('_RelationalExpression', '_instanceof', '_ReferenceType')

        def __init__(self, leftIToken, rightIToken,
                             _RelationalExpression,
                             _instanceof,
                             _ReferenceType):
        
            super(RelationalExpression4, self).__init__(leftIToken, rightIToken)

            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self._instanceof = _instanceof
            _instanceof.setParent(self)
            self._ReferenceType = _ReferenceType
            _ReferenceType.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            if self._instanceof:  _content.add(self._instanceof)
            if self._ReferenceType:  _content.add(self._ReferenceType)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitRelationalExpression4(self)
        def  acceptWithArg(self, v, o):  v.visitRelationalExpression4(self, o)
        def  acceptWithResult(self, v):  return v.visitRelationalExpression4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitRelationalExpression4(self, o)
    

'''/**
 *<b>
*<li>Rule 414:  EqualityExpression ::= EqualityExpression == RelationalExpression
 *</b>
 */'''
class EqualityExpression0 ( Ast ,IEqualityExpression):
    

        def  getEqualityExpression(self)  :  return self._EqualityExpression
        def  setEqualityExpression(self,  _EqualityExpression) :   self._EqualityExpression = _EqualityExpression
        def  getEQUAL_EQUAL(self)  :  return self._EQUAL_EQUAL
        def  setEQUAL_EQUAL(self,  _EQUAL_EQUAL) :   self._EQUAL_EQUAL = _EQUAL_EQUAL
        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression

        __slots__ = ('_EqualityExpression', '_EQUAL_EQUAL', '_RelationalExpression')

        def __init__(self, leftIToken, rightIToken,
                             _EqualityExpression,
                             _EQUAL_EQUAL,
                             _RelationalExpression):
        
            super(EqualityExpression0, self).__init__(leftIToken, rightIToken)

            self._EqualityExpression = _EqualityExpression
            _EqualityExpression.setParent(self)
            self._EQUAL_EQUAL = _EQUAL_EQUAL
            _EQUAL_EQUAL.setParent(self)
            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._EqualityExpression:  _content.add(self._EqualityExpression)
            if self._EQUAL_EQUAL:  _content.add(self._EQUAL_EQUAL)
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEqualityExpression0(self)
        def  acceptWithArg(self, v, o):  v.visitEqualityExpression0(self, o)
        def  acceptWithResult(self, v):  return v.visitEqualityExpression0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEqualityExpression0(self, o)
    

'''/**
 *<b>
*<li>Rule 415:  EqualityExpression ::= EqualityExpression != RelationalExpression
 *</b>
 */'''
class EqualityExpression1 ( Ast ,IEqualityExpression):
    

        def  getEqualityExpression(self)  :  return self._EqualityExpression
        def  setEqualityExpression(self,  _EqualityExpression) :   self._EqualityExpression = _EqualityExpression
        def  getNOT_EQUAL(self)  :  return self._NOT_EQUAL
        def  setNOT_EQUAL(self,  _NOT_EQUAL) :   self._NOT_EQUAL = _NOT_EQUAL
        def  getRelationalExpression(self)  :  return self._RelationalExpression
        def  setRelationalExpression(self,  _RelationalExpression) :   self._RelationalExpression = _RelationalExpression

        __slots__ = ('_EqualityExpression', '_NOT_EQUAL', '_RelationalExpression')

        def __init__(self, leftIToken, rightIToken,
                             _EqualityExpression,
                             _NOT_EQUAL,
                             _RelationalExpression):
        
            super(EqualityExpression1, self).__init__(leftIToken, rightIToken)

            self._EqualityExpression = _EqualityExpression
            _EqualityExpression.setParent(self)
            self._NOT_EQUAL = _NOT_EQUAL
            _NOT_EQUAL.setParent(self)
            self._RelationalExpression = _RelationalExpression
            _RelationalExpression.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._EqualityExpression:  _content.add(self._EqualityExpression)
            if self._NOT_EQUAL:  _content.add(self._NOT_EQUAL)
            if self._RelationalExpression:  _content.add(self._RelationalExpression)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitEqualityExpression1(self)
        def  acceptWithArg(self, v, o):  v.visitEqualityExpression1(self, o)
        def  acceptWithResult(self, v):  return v.visitEqualityExpression1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitEqualityExpression1(self, o)
    

'''/**
 *<b>
*<li>Rule 434:  AssignmentOperator ::= =
 *</b>
 */'''
class AssignmentOperator0 ( AstToken ,IAssignmentOperator):
    
        def  getEQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator0, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator0(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator0(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator0(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator0(self, o)
    

'''/**
 *<b>
*<li>Rule 435:  AssignmentOperator ::= *=
 *</b>
 */'''
class AssignmentOperator1 ( AstToken ,IAssignmentOperator):
    
        def  getMULTIPLY_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator1, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator1(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator1(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator1(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator1(self, o)
    

'''/**
 *<b>
*<li>Rule 436:  AssignmentOperator ::= /=
 *</b>
 */'''
class AssignmentOperator2 ( AstToken ,IAssignmentOperator):
    
        def  getDIVIDE_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator2, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator2(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator2(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator2(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator2(self, o)
    

'''/**
 *<b>
*<li>Rule 437:  AssignmentOperator ::= %=
 *</b>
 */'''
class AssignmentOperator3 ( AstToken ,IAssignmentOperator):
    
        def  getREMAINDER_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator3, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator3(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator3(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator3(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator3(self, o)
    

'''/**
 *<b>
*<li>Rule 438:  AssignmentOperator ::= +=
 *</b>
 */'''
class AssignmentOperator4 ( AstToken ,IAssignmentOperator):
    
        def  getPLUS_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator4, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator4(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator4(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator4(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator4(self, o)
    

'''/**
 *<b>
*<li>Rule 439:  AssignmentOperator ::= -=
 *</b>
 */'''
class AssignmentOperator5 ( AstToken ,IAssignmentOperator):
    
        def  getMINUS_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator5, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator5(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator5(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator5(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator5(self, o)
    

'''/**
 *<b>
*<li>Rule 440:  AssignmentOperator ::= <<=
 *</b>
 */'''
class AssignmentOperator6 ( AstToken ,IAssignmentOperator):
    
        def  getLEFT_SHIFT_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator6, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator6(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator6(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator6(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator6(self, o)
    

'''/**
 *<b>
*<li>Rule 441:  AssignmentOperator ::= > > =
 *</b>
 */'''
class AssignmentOperator7 ( Ast ,IAssignmentOperator):
    

        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER
        def  getGREATER2(self)  :  return self._GREATER2
        def  setGREATER2(self,  _GREATER2) :   self._GREATER2 = _GREATER2
        def  getEQUAL(self)  :  return self._EQUAL
        def  setEQUAL(self,  _EQUAL) :   self._EQUAL = _EQUAL

        __slots__ = ('_GREATER', '_GREATER2', '_EQUAL')

        def __init__(self, leftIToken, rightIToken,
                             _GREATER,
                             _GREATER2,
                             _EQUAL):
        
            super(AssignmentOperator7, self).__init__(leftIToken, rightIToken)

            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self._GREATER2 = _GREATER2
            _GREATER2.setParent(self)
            self._EQUAL = _EQUAL
            _EQUAL.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._GREATER:  _content.add(self._GREATER)
            if self._GREATER2:  _content.add(self._GREATER2)
            if self._EQUAL:  _content.add(self._EQUAL)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator7(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator7(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator7(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator7(self, o)
    

'''/**
 *<b>
*<li>Rule 442:  AssignmentOperator ::= > > > =
 *</b>
 */'''
class AssignmentOperator8 ( Ast ,IAssignmentOperator):
    

        def  getGREATER(self)  :  return self._GREATER
        def  setGREATER(self,  _GREATER) :   self._GREATER = _GREATER
        def  getGREATER2(self)  :  return self._GREATER2
        def  setGREATER2(self,  _GREATER2) :   self._GREATER2 = _GREATER2
        def  getGREATER3(self)  :  return self._GREATER3
        def  setGREATER3(self,  _GREATER3) :   self._GREATER3 = _GREATER3
        def  getEQUAL(self)  :  return self._EQUAL
        def  setEQUAL(self,  _EQUAL) :   self._EQUAL = _EQUAL

        __slots__ = ('_GREATER', '_GREATER2', '_GREATER3', '_EQUAL')

        def __init__(self, leftIToken, rightIToken,
                             _GREATER,
                             _GREATER2,
                             _GREATER3,
                             _EQUAL):
        
            super(AssignmentOperator8, self).__init__(leftIToken, rightIToken)

            self._GREATER = _GREATER
            _GREATER.setParent(self)
            self._GREATER2 = _GREATER2
            _GREATER2.setParent(self)
            self._GREATER3 = _GREATER3
            _GREATER3.setParent(self)
            self._EQUAL = _EQUAL
            _EQUAL.setParent(self)
            self.initialize()
        

        '''/**
         * A list of all children of this node, don't including the null ones.
         */'''
        def  getAllChildren(self)  :
        
            _content = ArrayList()
            if self._GREATER:  _content.add(self._GREATER)
            if self._GREATER2:  _content.add(self._GREATER2)
            if self._GREATER3:  _content.add(self._GREATER3)
            if self._EQUAL:  _content.add(self._EQUAL)
            return _content
        

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator8(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator8(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator8(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator8(self, o)
    

'''/**
 *<b>
*<li>Rule 443:  AssignmentOperator ::= &=
 *</b>
 */'''
class AssignmentOperator9 ( AstToken ,IAssignmentOperator):
    
        def  getAND_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator9, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator9(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator9(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator9(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator9(self, o)
    

'''/**
 *<b>
*<li>Rule 444:  AssignmentOperator ::= ^=
 *</b>
 */'''
class AssignmentOperator10 ( AstToken ,IAssignmentOperator):
    
        def  getXOR_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator10, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator10(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator10(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator10(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator10(self, o)
    

'''/**
 *<b>
*<li>Rule 445:  AssignmentOperator ::= |=
 *</b>
 */'''
class AssignmentOperator11 ( AstToken ,IAssignmentOperator):
    
        def  getOR_EQUAL(self) :  return self.leftIToken 

        __slots__ = 'environment'

        def __init__(self,token  ) : 
            super(AssignmentOperator11, self).__init__(token)
            self.initialize()

        def  acceptWithVisitor(self, v):  v.visitAssignmentOperator11(self)
        def  acceptWithArg(self, v, o):  v.visitAssignmentOperator11(self, o)
        def  acceptWithResult(self, v):  return v.visitAssignmentOperator11(self)
        def  acceptWithResultArgument(self, v, o):  return v.visitAssignmentOperator11(self, o)
    

class Visitor(object):
        __slots__ = ()
    
        def visitAstToken(self, n): pass
        def visitidentifier(self, n): pass
        def visitPrimitiveType(self, n): pass
        def visitClassType(self, n): pass
        def visitInterfaceType(self, n): pass
        def visitTypeName(self, n): pass
        def visitArrayType(self, n): pass
        def visitTypeParameter(self, n): pass
        def visitTypeBound(self, n): pass
        def visitAdditionalBoundList(self, n): pass
        def visitAdditionalBound(self, n): pass
        def visitTypeArguments(self, n): pass
        def visitActualTypeArgumentList(self, n): pass
        def visitWildcard(self, n): pass
        def visitPackageName(self, n): pass
        def visitExpressionName(self, n): pass
        def visitMethodName(self, n): pass
        def visitPackageOrTypeName(self, n): pass
        def visitAmbiguousName(self, n): pass
        def visitCompilationUnit(self, n): pass
        def visitImportDeclarations(self, n): pass
        def visitTypeDeclarations(self, n): pass
        def visitPackageDeclaration(self, n): pass
        def visitSingleTypeImportDeclaration(self, n): pass
        def visitTypeImportOnDemandDeclaration(self, n): pass
        def visitSingleStaticImportDeclaration(self, n): pass
        def visitStaticImportOnDemandDeclaration(self, n): pass
        def visitTypeDeclaration(self, n): pass
        def visitNormalClassDeclaration(self, n): pass
        def visitClassModifiers(self, n): pass
        def visitTypeParameters(self, n): pass
        def visitTypeParameterList(self, n): pass
        def visitSuper(self, n): pass
        def visitInterfaces(self, n): pass
        def visitInterfaceTypeList(self, n): pass
        def visitClassBody(self, n): pass
        def visitClassBodyDeclarations(self, n): pass
        def visitClassMemberDeclaration(self, n): pass
        def visitFieldDeclaration(self, n): pass
        def visitVariableDeclarators(self, n): pass
        def visitVariableDeclarator(self, n): pass
        def visitVariableDeclaratorId(self, n): pass
        def visitFieldModifiers(self, n): pass
        def visitMethodDeclaration(self, n): pass
        def visitMethodHeader(self, n): pass
        def visitResultType(self, n): pass
        def visitFormalParameterList(self, n): pass
        def visitFormalParameters(self, n): pass
        def visitFormalParameter(self, n): pass
        def visitVariableModifiers(self, n): pass
        def visitVariableModifier(self, n): pass
        def visitLastFormalParameter(self, n): pass
        def visitMethodModifiers(self, n): pass
        def visitThrows(self, n): pass
        def visitExceptionTypeList(self, n): pass
        def visitMethodBody(self, n): pass
        def visitStaticInitializer(self, n): pass
        def visitConstructorDeclaration(self, n): pass
        def visitConstructorDeclarator(self, n): pass
        def visitConstructorModifiers(self, n): pass
        def visitConstructorBody(self, n): pass
        def visitEnumDeclaration(self, n): pass
        def visitEnumBody(self, n): pass
        def visitEnumConstants(self, n): pass
        def visitEnumConstant(self, n): pass
        def visitArguments(self, n): pass
        def visitEnumBodyDeclarations(self, n): pass
        def visitNormalInterfaceDeclaration(self, n): pass
        def visitInterfaceModifiers(self, n): pass
        def visitInterfaceBody(self, n): pass
        def visitInterfaceMemberDeclarations(self, n): pass
        def visitInterfaceMemberDeclaration(self, n): pass
        def visitConstantDeclaration(self, n): pass
        def visitConstantModifiers(self, n): pass
        def visitAbstractMethodDeclaration(self, n): pass
        def visitAbstractMethodModifiers(self, n): pass
        def visitAnnotationTypeDeclaration(self, n): pass
        def visitAnnotationTypeBody(self, n): pass
        def visitAnnotationTypeElementDeclarations(self, n): pass
        def visitDefaultValue(self, n): pass
        def visitAnnotations(self, n): pass
        def visitNormalAnnotation(self, n): pass
        def visitElementValuePairs(self, n): pass
        def visitElementValuePair(self, n): pass
        def visitElementValueArrayInitializer(self, n): pass
        def visitElementValues(self, n): pass
        def visitMarkerAnnotation(self, n): pass
        def visitSingleElementAnnotation(self, n): pass
        def visitArrayInitializer(self, n): pass
        def visitVariableInitializers(self, n): pass
        def visitBlock(self, n): pass
        def visitBlockStatements(self, n): pass
        def visitLocalVariableDeclarationStatement(self, n): pass
        def visitLocalVariableDeclaration(self, n): pass
        def visitIfThenStatement(self, n): pass
        def visitIfThenElseStatement(self, n): pass
        def visitIfThenElseStatementNoShortIf(self, n): pass
        def visitEmptyStatement(self, n): pass
        def visitLabeledStatement(self, n): pass
        def visitLabeledStatementNoShortIf(self, n): pass
        def visitExpressionStatement(self, n): pass
        def visitSwitchStatement(self, n): pass
        def visitSwitchBlock(self, n): pass
        def visitSwitchBlockStatementGroups(self, n): pass
        def visitSwitchBlockStatementGroup(self, n): pass
        def visitSwitchLabels(self, n): pass
        def visitWhileStatement(self, n): pass
        def visitWhileStatementNoShortIf(self, n): pass
        def visitDoStatement(self, n): pass
        def visitBasicForStatement(self, n): pass
        def visitForStatementNoShortIf(self, n): pass
        def visitStatementExpressionList(self, n): pass
        def visitEnhancedForStatement(self, n): pass
        def visitBreakStatement(self, n): pass
        def visitContinueStatement(self, n): pass
        def visitReturnStatement(self, n): pass
        def visitThrowStatement(self, n): pass
        def visitSynchronizedStatement(self, n): pass
        def visitCatches(self, n): pass
        def visitCatchClause(self, n): pass
        def visitFinally(self, n): pass
        def visitArgumentList(self, n): pass
        def visitDimExprs(self, n): pass
        def visitDimExpr(self, n): pass
        def visitPostIncrementExpression(self, n): pass
        def visitPostDecrementExpression(self, n): pass
        def visitPreIncrementExpression(self, n): pass
        def visitPreDecrementExpression(self, n): pass
        def visitAndExpression(self, n): pass
        def visitExclusiveOrExpression(self, n): pass
        def visitInclusiveOrExpression(self, n): pass
        def visitConditionalAndExpression(self, n): pass
        def visitConditionalOrExpression(self, n): pass
        def visitConditionalExpression(self, n): pass
        def visitAssignment(self, n): pass
        def visitCommaopt(self, n): pass
        def visitEllipsisopt(self, n): pass
        def visitLPGUserAction0(self, n): pass
        def visitLPGUserAction1(self, n): pass
        def visitLPGUserAction2(self, n): pass
        def visitLPGUserAction3(self, n): pass
        def visitLPGUserAction4(self, n): pass
        def visitIntegralType0(self, n): pass
        def visitIntegralType1(self, n): pass
        def visitIntegralType2(self, n): pass
        def visitIntegralType3(self, n): pass
        def visitIntegralType4(self, n): pass
        def visitFloatingPointType0(self, n): pass
        def visitFloatingPointType1(self, n): pass
        def visitWildcardBounds0(self, n): pass
        def visitWildcardBounds1(self, n): pass
        def visitClassModifier0(self, n): pass
        def visitClassModifier1(self, n): pass
        def visitClassModifier2(self, n): pass
        def visitClassModifier3(self, n): pass
        def visitClassModifier4(self, n): pass
        def visitClassModifier5(self, n): pass
        def visitClassModifier6(self, n): pass
        def visitFieldModifier0(self, n): pass
        def visitFieldModifier1(self, n): pass
        def visitFieldModifier2(self, n): pass
        def visitFieldModifier3(self, n): pass
        def visitFieldModifier4(self, n): pass
        def visitFieldModifier5(self, n): pass
        def visitFieldModifier6(self, n): pass
        def visitMethodDeclarator0(self, n): pass
        def visitMethodDeclarator1(self, n): pass
        def visitMethodModifier0(self, n): pass
        def visitMethodModifier1(self, n): pass
        def visitMethodModifier2(self, n): pass
        def visitMethodModifier3(self, n): pass
        def visitMethodModifier4(self, n): pass
        def visitMethodModifier5(self, n): pass
        def visitMethodModifier6(self, n): pass
        def visitMethodModifier7(self, n): pass
        def visitMethodModifier8(self, n): pass
        def visitConstructorModifier0(self, n): pass
        def visitConstructorModifier1(self, n): pass
        def visitConstructorModifier2(self, n): pass
        def visitExplicitConstructorInvocation0(self, n): pass
        def visitExplicitConstructorInvocation1(self, n): pass
        def visitExplicitConstructorInvocation2(self, n): pass
        def visitInterfaceModifier0(self, n): pass
        def visitInterfaceModifier1(self, n): pass
        def visitInterfaceModifier2(self, n): pass
        def visitInterfaceModifier3(self, n): pass
        def visitInterfaceModifier4(self, n): pass
        def visitInterfaceModifier5(self, n): pass
        def visitExtendsInterfaces0(self, n): pass
        def visitExtendsInterfaces1(self, n): pass
        def visitConstantModifier0(self, n): pass
        def visitConstantModifier1(self, n): pass
        def visitConstantModifier2(self, n): pass
        def visitAbstractMethodModifier0(self, n): pass
        def visitAbstractMethodModifier1(self, n): pass
        def visitAnnotationTypeElementDeclaration0(self, n): pass
        def visitAnnotationTypeElementDeclaration1(self, n): pass
        def visitAssertStatement0(self, n): pass
        def visitAssertStatement1(self, n): pass
        def visitSwitchLabel0(self, n): pass
        def visitSwitchLabel1(self, n): pass
        def visitSwitchLabel2(self, n): pass
        def visitTryStatement0(self, n): pass
        def visitTryStatement1(self, n): pass
        def visitPrimaryNoNewArray0(self, n): pass
        def visitPrimaryNoNewArray1(self, n): pass
        def visitPrimaryNoNewArray2(self, n): pass
        def visitPrimaryNoNewArray3(self, n): pass
        def visitPrimaryNoNewArray4(self, n): pass
        def visitLiteral0(self, n): pass
        def visitLiteral1(self, n): pass
        def visitLiteral2(self, n): pass
        def visitLiteral3(self, n): pass
        def visitLiteral4(self, n): pass
        def visitLiteral5(self, n): pass
        def visitLiteral6(self, n): pass
        def visitBooleanLiteral0(self, n): pass
        def visitBooleanLiteral1(self, n): pass
        def visitClassInstanceCreationExpression0(self, n): pass
        def visitClassInstanceCreationExpression1(self, n): pass
        def visitArrayCreationExpression0(self, n): pass
        def visitArrayCreationExpression1(self, n): pass
        def visitArrayCreationExpression2(self, n): pass
        def visitArrayCreationExpression3(self, n): pass
        def visitDims0(self, n): pass
        def visitDims1(self, n): pass
        def visitFieldAccess0(self, n): pass
        def visitFieldAccess1(self, n): pass
        def visitFieldAccess2(self, n): pass
        def visitMethodInvocation0(self, n): pass
        def visitMethodInvocation1(self, n): pass
        def visitMethodInvocation2(self, n): pass
        def visitMethodInvocation3(self, n): pass
        def visitMethodInvocation4(self, n): pass
        def visitArrayAccess0(self, n): pass
        def visitArrayAccess1(self, n): pass
        def visitUnaryExpression0(self, n): pass
        def visitUnaryExpression1(self, n): pass
        def visitUnaryExpressionNotPlusMinus0(self, n): pass
        def visitUnaryExpressionNotPlusMinus1(self, n): pass
        def visitCastExpression0(self, n): pass
        def visitCastExpression1(self, n): pass
        def visitMultiplicativeExpression0(self, n): pass
        def visitMultiplicativeExpression1(self, n): pass
        def visitMultiplicativeExpression2(self, n): pass
        def visitAdditiveExpression0(self, n): pass
        def visitAdditiveExpression1(self, n): pass
        def visitShiftExpression0(self, n): pass
        def visitShiftExpression1(self, n): pass
        def visitShiftExpression2(self, n): pass
        def visitRelationalExpression0(self, n): pass
        def visitRelationalExpression1(self, n): pass
        def visitRelationalExpression2(self, n): pass
        def visitRelationalExpression3(self, n): pass
        def visitRelationalExpression4(self, n): pass
        def visitEqualityExpression0(self, n): pass
        def visitEqualityExpression1(self, n): pass
        def visitAssignmentOperator0(self, n): pass
        def visitAssignmentOperator1(self, n): pass
        def visitAssignmentOperator2(self, n): pass
        def visitAssignmentOperator3(self, n): pass
        def visitAssignmentOperator4(self, n): pass
        def visitAssignmentOperator5(self, n): pass
        def visitAssignmentOperator6(self, n): pass
        def visitAssignmentOperator7(self, n): pass
        def visitAssignmentOperator8(self, n): pass
        def visitAssignmentOperator9(self, n): pass
        def visitAssignmentOperator10(self, n): pass
        def visitAssignmentOperator11(self, n): pass

        def visit(self, n): pass
    
class ArgumentVisitor(object):
        __slots__ = ()
    
        def visitAstToken(self, n, o): pass
        def visitidentifier(self, n, o): pass
        def visitPrimitiveType(self, n, o): pass
        def visitClassType(self, n, o): pass
        def visitInterfaceType(self, n, o): pass
        def visitTypeName(self, n, o): pass
        def visitArrayType(self, n, o): pass
        def visitTypeParameter(self, n, o): pass
        def visitTypeBound(self, n, o): pass
        def visitAdditionalBoundList(self, n, o): pass
        def visitAdditionalBound(self, n, o): pass
        def visitTypeArguments(self, n, o): pass
        def visitActualTypeArgumentList(self, n, o): pass
        def visitWildcard(self, n, o): pass
        def visitPackageName(self, n, o): pass
        def visitExpressionName(self, n, o): pass
        def visitMethodName(self, n, o): pass
        def visitPackageOrTypeName(self, n, o): pass
        def visitAmbiguousName(self, n, o): pass
        def visitCompilationUnit(self, n, o): pass
        def visitImportDeclarations(self, n, o): pass
        def visitTypeDeclarations(self, n, o): pass
        def visitPackageDeclaration(self, n, o): pass
        def visitSingleTypeImportDeclaration(self, n, o): pass
        def visitTypeImportOnDemandDeclaration(self, n, o): pass
        def visitSingleStaticImportDeclaration(self, n, o): pass
        def visitStaticImportOnDemandDeclaration(self, n, o): pass
        def visitTypeDeclaration(self, n, o): pass
        def visitNormalClassDeclaration(self, n, o): pass
        def visitClassModifiers(self, n, o): pass
        def visitTypeParameters(self, n, o): pass
        def visitTypeParameterList(self, n, o): pass
        def visitSuper(self, n, o): pass
        def visitInterfaces(self, n, o): pass
        def visitInterfaceTypeList(self, n, o): pass
        def visitClassBody(self, n, o): pass
        def visitClassBodyDeclarations(self, n, o): pass
        def visitClassMemberDeclaration(self, n, o): pass
        def visitFieldDeclaration(self, n, o): pass
        def visitVariableDeclarators(self, n, o): pass
        def visitVariableDeclarator(self, n, o): pass
        def visitVariableDeclaratorId(self, n, o): pass
        def visitFieldModifiers(self, n, o): pass
        def visitMethodDeclaration(self, n, o): pass
        def visitMethodHeader(self, n, o): pass
        def visitResultType(self, n, o): pass
        def visitFormalParameterList(self, n, o): pass
        def visitFormalParameters(self, n, o): pass
        def visitFormalParameter(self, n, o): pass
        def visitVariableModifiers(self, n, o): pass
        def visitVariableModifier(self, n, o): pass
        def visitLastFormalParameter(self, n, o): pass
        def visitMethodModifiers(self, n, o): pass
        def visitThrows(self, n, o): pass
        def visitExceptionTypeList(self, n, o): pass
        def visitMethodBody(self, n, o): pass
        def visitStaticInitializer(self, n, o): pass
        def visitConstructorDeclaration(self, n, o): pass
        def visitConstructorDeclarator(self, n, o): pass
        def visitConstructorModifiers(self, n, o): pass
        def visitConstructorBody(self, n, o): pass
        def visitEnumDeclaration(self, n, o): pass
        def visitEnumBody(self, n, o): pass
        def visitEnumConstants(self, n, o): pass
        def visitEnumConstant(self, n, o): pass
        def visitArguments(self, n, o): pass
        def visitEnumBodyDeclarations(self, n, o): pass
        def visitNormalInterfaceDeclaration(self, n, o): pass
        def visitInterfaceModifiers(self, n, o): pass
        def visitInterfaceBody(self, n, o): pass
        def visitInterfaceMemberDeclarations(self, n, o): pass
        def visitInterfaceMemberDeclaration(self, n, o): pass
        def visitConstantDeclaration(self, n, o): pass
        def visitConstantModifiers(self, n, o): pass
        def visitAbstractMethodDeclaration(self, n, o): pass
        def visitAbstractMethodModifiers(self, n, o): pass
        def visitAnnotationTypeDeclaration(self, n, o): pass
        def visitAnnotationTypeBody(self, n, o): pass
        def visitAnnotationTypeElementDeclarations(self, n, o): pass
        def visitDefaultValue(self, n, o): pass
        def visitAnnotations(self, n, o): pass
        def visitNormalAnnotation(self, n, o): pass
        def visitElementValuePairs(self, n, o): pass
        def visitElementValuePair(self, n, o): pass
        def visitElementValueArrayInitializer(self, n, o): pass
        def visitElementValues(self, n, o): pass
        def visitMarkerAnnotation(self, n, o): pass
        def visitSingleElementAnnotation(self, n, o): pass
        def visitArrayInitializer(self, n, o): pass
        def visitVariableInitializers(self, n, o): pass
        def visitBlock(self, n, o): pass
        def visitBlockStatements(self, n, o): pass
        def visitLocalVariableDeclarationStatement(self, n, o): pass
        def visitLocalVariableDeclaration(self, n, o): pass
        def visitIfThenStatement(self, n, o): pass
        def visitIfThenElseStatement(self, n, o): pass
        def visitIfThenElseStatementNoShortIf(self, n, o): pass
        def visitEmptyStatement(self, n, o): pass
        def visitLabeledStatement(self, n, o): pass
        def visitLabeledStatementNoShortIf(self, n, o): pass
        def visitExpressionStatement(self, n, o): pass
        def visitSwitchStatement(self, n, o): pass
        def visitSwitchBlock(self, n, o): pass
        def visitSwitchBlockStatementGroups(self, n, o): pass
        def visitSwitchBlockStatementGroup(self, n, o): pass
        def visitSwitchLabels(self, n, o): pass
        def visitWhileStatement(self, n, o): pass
        def visitWhileStatementNoShortIf(self, n, o): pass
        def visitDoStatement(self, n, o): pass
        def visitBasicForStatement(self, n, o): pass
        def visitForStatementNoShortIf(self, n, o): pass
        def visitStatementExpressionList(self, n, o): pass
        def visitEnhancedForStatement(self, n, o): pass
        def visitBreakStatement(self, n, o): pass
        def visitContinueStatement(self, n, o): pass
        def visitReturnStatement(self, n, o): pass
        def visitThrowStatement(self, n, o): pass
        def visitSynchronizedStatement(self, n, o): pass
        def visitCatches(self, n, o): pass
        def visitCatchClause(self, n, o): pass
        def visitFinally(self, n, o): pass
        def visitArgumentList(self, n, o): pass
        def visitDimExprs(self, n, o): pass
        def visitDimExpr(self, n, o): pass
        def visitPostIncrementExpression(self, n, o): pass
        def visitPostDecrementExpression(self, n, o): pass
        def visitPreIncrementExpression(self, n, o): pass
        def visitPreDecrementExpression(self, n, o): pass
        def visitAndExpression(self, n, o): pass
        def visitExclusiveOrExpression(self, n, o): pass
        def visitInclusiveOrExpression(self, n, o): pass
        def visitConditionalAndExpression(self, n, o): pass
        def visitConditionalOrExpression(self, n, o): pass
        def visitConditionalExpression(self, n, o): pass
        def visitAssignment(self, n, o): pass
        def visitCommaopt(self, n, o): pass
        def visitEllipsisopt(self, n, o): pass
        def visitLPGUserAction0(self, n, o): pass
        def visitLPGUserAction1(self, n, o): pass
        def visitLPGUserAction2(self, n, o): pass
        def visitLPGUserAction3(self, n, o): pass
        def visitLPGUserAction4(self, n, o): pass
        def visitIntegralType0(self, n, o): pass
        def visitIntegralType1(self, n, o): pass
        def visitIntegralType2(self, n, o): pass
        def visitIntegralType3(self, n, o): pass
        def visitIntegralType4(self, n, o): pass
        def visitFloatingPointType0(self, n, o): pass
        def visitFloatingPointType1(self, n, o): pass
        def visitWildcardBounds0(self, n, o): pass
        def visitWildcardBounds1(self, n, o): pass
        def visitClassModifier0(self, n, o): pass
        def visitClassModifier1(self, n, o): pass
        def visitClassModifier2(self, n, o): pass
        def visitClassModifier3(self, n, o): pass
        def visitClassModifier4(self, n, o): pass
        def visitClassModifier5(self, n, o): pass
        def visitClassModifier6(self, n, o): pass
        def visitFieldModifier0(self, n, o): pass
        def visitFieldModifier1(self, n, o): pass
        def visitFieldModifier2(self, n, o): pass
        def visitFieldModifier3(self, n, o): pass
        def visitFieldModifier4(self, n, o): pass
        def visitFieldModifier5(self, n, o): pass
        def visitFieldModifier6(self, n, o): pass
        def visitMethodDeclarator0(self, n, o): pass
        def visitMethodDeclarator1(self, n, o): pass
        def visitMethodModifier0(self, n, o): pass
        def visitMethodModifier1(self, n, o): pass
        def visitMethodModifier2(self, n, o): pass
        def visitMethodModifier3(self, n, o): pass
        def visitMethodModifier4(self, n, o): pass
        def visitMethodModifier5(self, n, o): pass
        def visitMethodModifier6(self, n, o): pass
        def visitMethodModifier7(self, n, o): pass
        def visitMethodModifier8(self, n, o): pass
        def visitConstructorModifier0(self, n, o): pass
        def visitConstructorModifier1(self, n, o): pass
        def visitConstructorModifier2(self, n, o): pass
        def visitExplicitConstructorInvocation0(self, n, o): pass
        def visitExplicitConstructorInvocation1(self, n, o): pass
        def visitExplicitConstructorInvocation2(self, n, o): pass
        def visitInterfaceModifier0(self, n, o): pass
        def visitInterfaceModifier1(self, n, o): pass
        def visitInterfaceModifier2(self, n, o): pass
        def visitInterfaceModifier3(self, n, o): pass
        def visitInterfaceModifier4(self, n, o): pass
        def visitInterfaceModifier5(self, n, o): pass
        def visitExtendsInterfaces0(self, n, o): pass
        def visitExtendsInterfaces1(self, n, o): pass
        def visitConstantModifier0(self, n, o): pass
        def visitConstantModifier1(self, n, o): pass
        def visitConstantModifier2(self, n, o): pass
        def visitAbstractMethodModifier0(self, n, o): pass
        def visitAbstractMethodModifier1(self, n, o): pass
        def visitAnnotationTypeElementDeclaration0(self, n, o): pass
        def visitAnnotationTypeElementDeclaration1(self, n, o): pass
        def visitAssertStatement0(self, n, o): pass
        def visitAssertStatement1(self, n, o): pass
        def visitSwitchLabel0(self, n, o): pass
        def visitSwitchLabel1(self, n, o): pass
        def visitSwitchLabel2(self, n, o): pass
        def visitTryStatement0(self, n, o): pass
        def visitTryStatement1(self, n, o): pass
        def visitPrimaryNoNewArray0(self, n, o): pass
        def visitPrimaryNoNewArray1(self, n, o): pass
        def visitPrimaryNoNewArray2(self, n, o): pass
        def visitPrimaryNoNewArray3(self, n, o): pass
        def visitPrimaryNoNewArray4(self, n, o): pass
        def visitLiteral0(self, n, o): pass
        def visitLiteral1(self, n, o): pass
        def visitLiteral2(self, n, o): pass
        def visitLiteral3(self, n, o): pass
        def visitLiteral4(self, n, o): pass
        def visitLiteral5(self, n, o): pass
        def visitLiteral6(self, n, o): pass
        def visitBooleanLiteral0(self, n, o): pass
        def visitBooleanLiteral1(self, n, o): pass
        def visitClassInstanceCreationExpression0(self, n, o): pass
        def visitClassInstanceCreationExpression1(self, n, o): pass
        def visitArrayCreationExpression0(self, n, o): pass
        def visitArrayCreationExpression1(self, n, o): pass
        def visitArrayCreationExpression2(self, n, o): pass
        def visitArrayCreationExpression3(self, n, o): pass
        def visitDims0(self, n, o): pass
        def visitDims1(self, n, o): pass
        def visitFieldAccess0(self, n, o): pass
        def visitFieldAccess1(self, n, o): pass
        def visitFieldAccess2(self, n, o): pass
        def visitMethodInvocation0(self, n, o): pass
        def visitMethodInvocation1(self, n, o): pass
        def visitMethodInvocation2(self, n, o): pass
        def visitMethodInvocation3(self, n, o): pass
        def visitMethodInvocation4(self, n, o): pass
        def visitArrayAccess0(self, n, o): pass
        def visitArrayAccess1(self, n, o): pass
        def visitUnaryExpression0(self, n, o): pass
        def visitUnaryExpression1(self, n, o): pass
        def visitUnaryExpressionNotPlusMinus0(self, n, o): pass
        def visitUnaryExpressionNotPlusMinus1(self, n, o): pass
        def visitCastExpression0(self, n, o): pass
        def visitCastExpression1(self, n, o): pass
        def visitMultiplicativeExpression0(self, n, o): pass
        def visitMultiplicativeExpression1(self, n, o): pass
        def visitMultiplicativeExpression2(self, n, o): pass
        def visitAdditiveExpression0(self, n, o): pass
        def visitAdditiveExpression1(self, n, o): pass
        def visitShiftExpression0(self, n, o): pass
        def visitShiftExpression1(self, n, o): pass
        def visitShiftExpression2(self, n, o): pass
        def visitRelationalExpression0(self, n, o): pass
        def visitRelationalExpression1(self, n, o): pass
        def visitRelationalExpression2(self, n, o): pass
        def visitRelationalExpression3(self, n, o): pass
        def visitRelationalExpression4(self, n, o): pass
        def visitEqualityExpression0(self, n, o): pass
        def visitEqualityExpression1(self, n, o): pass
        def visitAssignmentOperator0(self, n, o): pass
        def visitAssignmentOperator1(self, n, o): pass
        def visitAssignmentOperator2(self, n, o): pass
        def visitAssignmentOperator3(self, n, o): pass
        def visitAssignmentOperator4(self, n, o): pass
        def visitAssignmentOperator5(self, n, o): pass
        def visitAssignmentOperator6(self, n, o): pass
        def visitAssignmentOperator7(self, n, o): pass
        def visitAssignmentOperator8(self, n, o): pass
        def visitAssignmentOperator9(self, n, o): pass
        def visitAssignmentOperator10(self, n, o): pass
        def visitAssignmentOperator11(self, n, o): pass

        def visit(self, n, o): pass
    
class ResultVisitor(object):
        __slots__ = ()
    
        def visitAstToken(self, n): pass
        def visitidentifier(self, n): pass
        def visitPrimitiveType(self, n): pass
        def visitClassType(self, n): pass
        def visitInterfaceType(self, n): pass
        def visitTypeName(self, n): pass
        def visitArrayType(self, n): pass
        def visitTypeParameter(self, n): pass
        def visitTypeBound(self, n): pass
        def visitAdditionalBoundList(self, n): pass
        def visitAdditionalBound(self, n): pass
        def visitTypeArguments(self, n): pass
        def visitActualTypeArgumentList(self, n): pass
        def visitWildcard(self, n): pass
        def visitPackageName(self, n): pass
        def visitExpressionName(self, n): pass
        def visitMethodName(self, n): pass
        def visitPackageOrTypeName(self, n): pass
        def visitAmbiguousName(self, n): pass
        def visitCompilationUnit(self, n): pass
        def visitImportDeclarations(self, n): pass
        def visitTypeDeclarations(self, n): pass
        def visitPackageDeclaration(self, n): pass
        def visitSingleTypeImportDeclaration(self, n): pass
        def visitTypeImportOnDemandDeclaration(self, n): pass
        def visitSingleStaticImportDeclaration(self, n): pass
        def visitStaticImportOnDemandDeclaration(self, n): pass
        def visitTypeDeclaration(self, n): pass
        def visitNormalClassDeclaration(self, n): pass
        def visitClassModifiers(self, n): pass
        def visitTypeParameters(self, n): pass
        def visitTypeParameterList(self, n): pass
        def visitSuper(self, n): pass
        def visitInterfaces(self, n): pass
        def visitInterfaceTypeList(self, n): pass
        def visitClassBody(self, n): pass
        def visitClassBodyDeclarations(self, n): pass
        def visitClassMemberDeclaration(self, n): pass
        def visitFieldDeclaration(self, n): pass
        def visitVariableDeclarators(self, n): pass
        def visitVariableDeclarator(self, n): pass
        def visitVariableDeclaratorId(self, n): pass
        def visitFieldModifiers(self, n): pass
        def visitMethodDeclaration(self, n): pass
        def visitMethodHeader(self, n): pass
        def visitResultType(self, n): pass
        def visitFormalParameterList(self, n): pass
        def visitFormalParameters(self, n): pass
        def visitFormalParameter(self, n): pass
        def visitVariableModifiers(self, n): pass
        def visitVariableModifier(self, n): pass
        def visitLastFormalParameter(self, n): pass
        def visitMethodModifiers(self, n): pass
        def visitThrows(self, n): pass
        def visitExceptionTypeList(self, n): pass
        def visitMethodBody(self, n): pass
        def visitStaticInitializer(self, n): pass
        def visitConstructorDeclaration(self, n): pass
        def visitConstructorDeclarator(self, n): pass
        def visitConstructorModifiers(self, n): pass
        def visitConstructorBody(self, n): pass
        def visitEnumDeclaration(self, n): pass
        def visitEnumBody(self, n): pass
        def visitEnumConstants(self, n): pass
        def visitEnumConstant(self, n): pass
        def visitArguments(self, n): pass
        def visitEnumBodyDeclarations(self, n): pass
        def visitNormalInterfaceDeclaration(self, n): pass
        def visitInterfaceModifiers(self, n): pass
        def visitInterfaceBody(self, n): pass
        def visitInterfaceMemberDeclarations(self, n): pass
        def visitInterfaceMemberDeclaration(self, n): pass
        def visitConstantDeclaration(self, n): pass
        def visitConstantModifiers(self, n): pass
        def visitAbstractMethodDeclaration(self, n): pass
        def visitAbstractMethodModifiers(self, n): pass
        def visitAnnotationTypeDeclaration(self, n): pass
        def visitAnnotationTypeBody(self, n): pass
        def visitAnnotationTypeElementDeclarations(self, n): pass
        def visitDefaultValue(self, n): pass
        def visitAnnotations(self, n): pass
        def visitNormalAnnotation(self, n): pass
        def visitElementValuePairs(self, n): pass
        def visitElementValuePair(self, n): pass
        def visitElementValueArrayInitializer(self, n): pass
        def visitElementValues(self, n): pass
        def visitMarkerAnnotation(self, n): pass
        def visitSingleElementAnnotation(self, n): pass
        def visitArrayInitializer(self, n): pass
        def visitVariableInitializers(self, n): pass
        def visitBlock(self, n): pass
        def visitBlockStatements(self, n): pass
        def visitLocalVariableDeclarationStatement(self, n): pass
        def visitLocalVariableDeclaration(self, n): pass
        def visitIfThenStatement(self, n): pass
        def visitIfThenElseStatement(self, n): pass
        def visitIfThenElseStatementNoShortIf(self, n): pass
        def visitEmptyStatement(self, n): pass
        def visitLabeledStatement(self, n): pass
        def visitLabeledStatementNoShortIf(self, n): pass
        def visitExpressionStatement(self, n): pass
        def visitSwitchStatement(self, n): pass
        def visitSwitchBlock(self, n): pass
        def visitSwitchBlockStatementGroups(self, n): pass
        def visitSwitchBlockStatementGroup(self, n): pass
        def visitSwitchLabels(self, n): pass
        def visitWhileStatement(self, n): pass
        def visitWhileStatementNoShortIf(self, n): pass
        def visitDoStatement(self, n): pass
        def visitBasicForStatement(self, n): pass
        def visitForStatementNoShortIf(self, n): pass
        def visitStatementExpressionList(self, n): pass
        def visitEnhancedForStatement(self, n): pass
        def visitBreakStatement(self, n): pass
        def visitContinueStatement(self, n): pass
        def visitReturnStatement(self, n): pass
        def visitThrowStatement(self, n): pass
        def visitSynchronizedStatement(self, n): pass
        def visitCatches(self, n): pass
        def visitCatchClause(self, n): pass
        def visitFinally(self, n): pass
        def visitArgumentList(self, n): pass
        def visitDimExprs(self, n): pass
        def visitDimExpr(self, n): pass
        def visitPostIncrementExpression(self, n): pass
        def visitPostDecrementExpression(self, n): pass
        def visitPreIncrementExpression(self, n): pass
        def visitPreDecrementExpression(self, n): pass
        def visitAndExpression(self, n): pass
        def visitExclusiveOrExpression(self, n): pass
        def visitInclusiveOrExpression(self, n): pass
        def visitConditionalAndExpression(self, n): pass
        def visitConditionalOrExpression(self, n): pass
        def visitConditionalExpression(self, n): pass
        def visitAssignment(self, n): pass
        def visitCommaopt(self, n): pass
        def visitEllipsisopt(self, n): pass
        def visitLPGUserAction0(self, n): pass
        def visitLPGUserAction1(self, n): pass
        def visitLPGUserAction2(self, n): pass
        def visitLPGUserAction3(self, n): pass
        def visitLPGUserAction4(self, n): pass
        def visitIntegralType0(self, n): pass
        def visitIntegralType1(self, n): pass
        def visitIntegralType2(self, n): pass
        def visitIntegralType3(self, n): pass
        def visitIntegralType4(self, n): pass
        def visitFloatingPointType0(self, n): pass
        def visitFloatingPointType1(self, n): pass
        def visitWildcardBounds0(self, n): pass
        def visitWildcardBounds1(self, n): pass
        def visitClassModifier0(self, n): pass
        def visitClassModifier1(self, n): pass
        def visitClassModifier2(self, n): pass
        def visitClassModifier3(self, n): pass
        def visitClassModifier4(self, n): pass
        def visitClassModifier5(self, n): pass
        def visitClassModifier6(self, n): pass
        def visitFieldModifier0(self, n): pass
        def visitFieldModifier1(self, n): pass
        def visitFieldModifier2(self, n): pass
        def visitFieldModifier3(self, n): pass
        def visitFieldModifier4(self, n): pass
        def visitFieldModifier5(self, n): pass
        def visitFieldModifier6(self, n): pass
        def visitMethodDeclarator0(self, n): pass
        def visitMethodDeclarator1(self, n): pass
        def visitMethodModifier0(self, n): pass
        def visitMethodModifier1(self, n): pass
        def visitMethodModifier2(self, n): pass
        def visitMethodModifier3(self, n): pass
        def visitMethodModifier4(self, n): pass
        def visitMethodModifier5(self, n): pass
        def visitMethodModifier6(self, n): pass
        def visitMethodModifier7(self, n): pass
        def visitMethodModifier8(self, n): pass
        def visitConstructorModifier0(self, n): pass
        def visitConstructorModifier1(self, n): pass
        def visitConstructorModifier2(self, n): pass
        def visitExplicitConstructorInvocation0(self, n): pass
        def visitExplicitConstructorInvocation1(self, n): pass
        def visitExplicitConstructorInvocation2(self, n): pass
        def visitInterfaceModifier0(self, n): pass
        def visitInterfaceModifier1(self, n): pass
        def visitInterfaceModifier2(self, n): pass
        def visitInterfaceModifier3(self, n): pass
        def visitInterfaceModifier4(self, n): pass
        def visitInterfaceModifier5(self, n): pass
        def visitExtendsInterfaces0(self, n): pass
        def visitExtendsInterfaces1(self, n): pass
        def visitConstantModifier0(self, n): pass
        def visitConstantModifier1(self, n): pass
        def visitConstantModifier2(self, n): pass
        def visitAbstractMethodModifier0(self, n): pass
        def visitAbstractMethodModifier1(self, n): pass
        def visitAnnotationTypeElementDeclaration0(self, n): pass
        def visitAnnotationTypeElementDeclaration1(self, n): pass
        def visitAssertStatement0(self, n): pass
        def visitAssertStatement1(self, n): pass
        def visitSwitchLabel0(self, n): pass
        def visitSwitchLabel1(self, n): pass
        def visitSwitchLabel2(self, n): pass
        def visitTryStatement0(self, n): pass
        def visitTryStatement1(self, n): pass
        def visitPrimaryNoNewArray0(self, n): pass
        def visitPrimaryNoNewArray1(self, n): pass
        def visitPrimaryNoNewArray2(self, n): pass
        def visitPrimaryNoNewArray3(self, n): pass
        def visitPrimaryNoNewArray4(self, n): pass
        def visitLiteral0(self, n): pass
        def visitLiteral1(self, n): pass
        def visitLiteral2(self, n): pass
        def visitLiteral3(self, n): pass
        def visitLiteral4(self, n): pass
        def visitLiteral5(self, n): pass
        def visitLiteral6(self, n): pass
        def visitBooleanLiteral0(self, n): pass
        def visitBooleanLiteral1(self, n): pass
        def visitClassInstanceCreationExpression0(self, n): pass
        def visitClassInstanceCreationExpression1(self, n): pass
        def visitArrayCreationExpression0(self, n): pass
        def visitArrayCreationExpression1(self, n): pass
        def visitArrayCreationExpression2(self, n): pass
        def visitArrayCreationExpression3(self, n): pass
        def visitDims0(self, n): pass
        def visitDims1(self, n): pass
        def visitFieldAccess0(self, n): pass
        def visitFieldAccess1(self, n): pass
        def visitFieldAccess2(self, n): pass
        def visitMethodInvocation0(self, n): pass
        def visitMethodInvocation1(self, n): pass
        def visitMethodInvocation2(self, n): pass
        def visitMethodInvocation3(self, n): pass
        def visitMethodInvocation4(self, n): pass
        def visitArrayAccess0(self, n): pass
        def visitArrayAccess1(self, n): pass
        def visitUnaryExpression0(self, n): pass
        def visitUnaryExpression1(self, n): pass
        def visitUnaryExpressionNotPlusMinus0(self, n): pass
        def visitUnaryExpressionNotPlusMinus1(self, n): pass
        def visitCastExpression0(self, n): pass
        def visitCastExpression1(self, n): pass
        def visitMultiplicativeExpression0(self, n): pass
        def visitMultiplicativeExpression1(self, n): pass
        def visitMultiplicativeExpression2(self, n): pass
        def visitAdditiveExpression0(self, n): pass
        def visitAdditiveExpression1(self, n): pass
        def visitShiftExpression0(self, n): pass
        def visitShiftExpression1(self, n): pass
        def visitShiftExpression2(self, n): pass
        def visitRelationalExpression0(self, n): pass
        def visitRelationalExpression1(self, n): pass
        def visitRelationalExpression2(self, n): pass
        def visitRelationalExpression3(self, n): pass
        def visitRelationalExpression4(self, n): pass
        def visitEqualityExpression0(self, n): pass
        def visitEqualityExpression1(self, n): pass
        def visitAssignmentOperator0(self, n): pass
        def visitAssignmentOperator1(self, n): pass
        def visitAssignmentOperator2(self, n): pass
        def visitAssignmentOperator3(self, n): pass
        def visitAssignmentOperator4(self, n): pass
        def visitAssignmentOperator5(self, n): pass
        def visitAssignmentOperator6(self, n): pass
        def visitAssignmentOperator7(self, n): pass
        def visitAssignmentOperator8(self, n): pass
        def visitAssignmentOperator9(self, n): pass
        def visitAssignmentOperator10(self, n): pass
        def visitAssignmentOperator11(self, n): pass

        def visit(self, n): pass
    
class ResultArgumentVisitor(object):
        __slots__ = ()
    
        def visitAstToken(self, n, o): pass
        def visitidentifier(self, n, o): pass
        def visitPrimitiveType(self, n, o): pass
        def visitClassType(self, n, o): pass
        def visitInterfaceType(self, n, o): pass
        def visitTypeName(self, n, o): pass
        def visitArrayType(self, n, o): pass
        def visitTypeParameter(self, n, o): pass
        def visitTypeBound(self, n, o): pass
        def visitAdditionalBoundList(self, n, o): pass
        def visitAdditionalBound(self, n, o): pass
        def visitTypeArguments(self, n, o): pass
        def visitActualTypeArgumentList(self, n, o): pass
        def visitWildcard(self, n, o): pass
        def visitPackageName(self, n, o): pass
        def visitExpressionName(self, n, o): pass
        def visitMethodName(self, n, o): pass
        def visitPackageOrTypeName(self, n, o): pass
        def visitAmbiguousName(self, n, o): pass
        def visitCompilationUnit(self, n, o): pass
        def visitImportDeclarations(self, n, o): pass
        def visitTypeDeclarations(self, n, o): pass
        def visitPackageDeclaration(self, n, o): pass
        def visitSingleTypeImportDeclaration(self, n, o): pass
        def visitTypeImportOnDemandDeclaration(self, n, o): pass
        def visitSingleStaticImportDeclaration(self, n, o): pass
        def visitStaticImportOnDemandDeclaration(self, n, o): pass
        def visitTypeDeclaration(self, n, o): pass
        def visitNormalClassDeclaration(self, n, o): pass
        def visitClassModifiers(self, n, o): pass
        def visitTypeParameters(self, n, o): pass
        def visitTypeParameterList(self, n, o): pass
        def visitSuper(self, n, o): pass
        def visitInterfaces(self, n, o): pass
        def visitInterfaceTypeList(self, n, o): pass
        def visitClassBody(self, n, o): pass
        def visitClassBodyDeclarations(self, n, o): pass
        def visitClassMemberDeclaration(self, n, o): pass
        def visitFieldDeclaration(self, n, o): pass
        def visitVariableDeclarators(self, n, o): pass
        def visitVariableDeclarator(self, n, o): pass
        def visitVariableDeclaratorId(self, n, o): pass
        def visitFieldModifiers(self, n, o): pass
        def visitMethodDeclaration(self, n, o): pass
        def visitMethodHeader(self, n, o): pass
        def visitResultType(self, n, o): pass
        def visitFormalParameterList(self, n, o): pass
        def visitFormalParameters(self, n, o): pass
        def visitFormalParameter(self, n, o): pass
        def visitVariableModifiers(self, n, o): pass
        def visitVariableModifier(self, n, o): pass
        def visitLastFormalParameter(self, n, o): pass
        def visitMethodModifiers(self, n, o): pass
        def visitThrows(self, n, o): pass
        def visitExceptionTypeList(self, n, o): pass
        def visitMethodBody(self, n, o): pass
        def visitStaticInitializer(self, n, o): pass
        def visitConstructorDeclaration(self, n, o): pass
        def visitConstructorDeclarator(self, n, o): pass
        def visitConstructorModifiers(self, n, o): pass
        def visitConstructorBody(self, n, o): pass
        def visitEnumDeclaration(self, n, o): pass
        def visitEnumBody(self, n, o): pass
        def visitEnumConstants(self, n, o): pass
        def visitEnumConstant(self, n, o): pass
        def visitArguments(self, n, o): pass
        def visitEnumBodyDeclarations(self, n, o): pass
        def visitNormalInterfaceDeclaration(self, n, o): pass
        def visitInterfaceModifiers(self, n, o): pass
        def visitInterfaceBody(self, n, o): pass
        def visitInterfaceMemberDeclarations(self, n, o): pass
        def visitInterfaceMemberDeclaration(self, n, o): pass
        def visitConstantDeclaration(self, n, o): pass
        def visitConstantModifiers(self, n, o): pass
        def visitAbstractMethodDeclaration(self, n, o): pass
        def visitAbstractMethodModifiers(self, n, o): pass
        def visitAnnotationTypeDeclaration(self, n, o): pass
        def visitAnnotationTypeBody(self, n, o): pass
        def visitAnnotationTypeElementDeclarations(self, n, o): pass
        def visitDefaultValue(self, n, o): pass
        def visitAnnotations(self, n, o): pass
        def visitNormalAnnotation(self, n, o): pass
        def visitElementValuePairs(self, n, o): pass
        def visitElementValuePair(self, n, o): pass
        def visitElementValueArrayInitializer(self, n, o): pass
        def visitElementValues(self, n, o): pass
        def visitMarkerAnnotation(self, n, o): pass
        def visitSingleElementAnnotation(self, n, o): pass
        def visitArrayInitializer(self, n, o): pass
        def visitVariableInitializers(self, n, o): pass
        def visitBlock(self, n, o): pass
        def visitBlockStatements(self, n, o): pass
        def visitLocalVariableDeclarationStatement(self, n, o): pass
        def visitLocalVariableDeclaration(self, n, o): pass
        def visitIfThenStatement(self, n, o): pass
        def visitIfThenElseStatement(self, n, o): pass
        def visitIfThenElseStatementNoShortIf(self, n, o): pass
        def visitEmptyStatement(self, n, o): pass
        def visitLabeledStatement(self, n, o): pass
        def visitLabeledStatementNoShortIf(self, n, o): pass
        def visitExpressionStatement(self, n, o): pass
        def visitSwitchStatement(self, n, o): pass
        def visitSwitchBlock(self, n, o): pass
        def visitSwitchBlockStatementGroups(self, n, o): pass
        def visitSwitchBlockStatementGroup(self, n, o): pass
        def visitSwitchLabels(self, n, o): pass
        def visitWhileStatement(self, n, o): pass
        def visitWhileStatementNoShortIf(self, n, o): pass
        def visitDoStatement(self, n, o): pass
        def visitBasicForStatement(self, n, o): pass
        def visitForStatementNoShortIf(self, n, o): pass
        def visitStatementExpressionList(self, n, o): pass
        def visitEnhancedForStatement(self, n, o): pass
        def visitBreakStatement(self, n, o): pass
        def visitContinueStatement(self, n, o): pass
        def visitReturnStatement(self, n, o): pass
        def visitThrowStatement(self, n, o): pass
        def visitSynchronizedStatement(self, n, o): pass
        def visitCatches(self, n, o): pass
        def visitCatchClause(self, n, o): pass
        def visitFinally(self, n, o): pass
        def visitArgumentList(self, n, o): pass
        def visitDimExprs(self, n, o): pass
        def visitDimExpr(self, n, o): pass
        def visitPostIncrementExpression(self, n, o): pass
        def visitPostDecrementExpression(self, n, o): pass
        def visitPreIncrementExpression(self, n, o): pass
        def visitPreDecrementExpression(self, n, o): pass
        def visitAndExpression(self, n, o): pass
        def visitExclusiveOrExpression(self, n, o): pass
        def visitInclusiveOrExpression(self, n, o): pass
        def visitConditionalAndExpression(self, n, o): pass
        def visitConditionalOrExpression(self, n, o): pass
        def visitConditionalExpression(self, n, o): pass
        def visitAssignment(self, n, o): pass
        def visitCommaopt(self, n, o): pass
        def visitEllipsisopt(self, n, o): pass
        def visitLPGUserAction0(self, n, o): pass
        def visitLPGUserAction1(self, n, o): pass
        def visitLPGUserAction2(self, n, o): pass
        def visitLPGUserAction3(self, n, o): pass
        def visitLPGUserAction4(self, n, o): pass
        def visitIntegralType0(self, n, o): pass
        def visitIntegralType1(self, n, o): pass
        def visitIntegralType2(self, n, o): pass
        def visitIntegralType3(self, n, o): pass
        def visitIntegralType4(self, n, o): pass
        def visitFloatingPointType0(self, n, o): pass
        def visitFloatingPointType1(self, n, o): pass
        def visitWildcardBounds0(self, n, o): pass
        def visitWildcardBounds1(self, n, o): pass
        def visitClassModifier0(self, n, o): pass
        def visitClassModifier1(self, n, o): pass
        def visitClassModifier2(self, n, o): pass
        def visitClassModifier3(self, n, o): pass
        def visitClassModifier4(self, n, o): pass
        def visitClassModifier5(self, n, o): pass
        def visitClassModifier6(self, n, o): pass
        def visitFieldModifier0(self, n, o): pass
        def visitFieldModifier1(self, n, o): pass
        def visitFieldModifier2(self, n, o): pass
        def visitFieldModifier3(self, n, o): pass
        def visitFieldModifier4(self, n, o): pass
        def visitFieldModifier5(self, n, o): pass
        def visitFieldModifier6(self, n, o): pass
        def visitMethodDeclarator0(self, n, o): pass
        def visitMethodDeclarator1(self, n, o): pass
        def visitMethodModifier0(self, n, o): pass
        def visitMethodModifier1(self, n, o): pass
        def visitMethodModifier2(self, n, o): pass
        def visitMethodModifier3(self, n, o): pass
        def visitMethodModifier4(self, n, o): pass
        def visitMethodModifier5(self, n, o): pass
        def visitMethodModifier6(self, n, o): pass
        def visitMethodModifier7(self, n, o): pass
        def visitMethodModifier8(self, n, o): pass
        def visitConstructorModifier0(self, n, o): pass
        def visitConstructorModifier1(self, n, o): pass
        def visitConstructorModifier2(self, n, o): pass
        def visitExplicitConstructorInvocation0(self, n, o): pass
        def visitExplicitConstructorInvocation1(self, n, o): pass
        def visitExplicitConstructorInvocation2(self, n, o): pass
        def visitInterfaceModifier0(self, n, o): pass
        def visitInterfaceModifier1(self, n, o): pass
        def visitInterfaceModifier2(self, n, o): pass
        def visitInterfaceModifier3(self, n, o): pass
        def visitInterfaceModifier4(self, n, o): pass
        def visitInterfaceModifier5(self, n, o): pass
        def visitExtendsInterfaces0(self, n, o): pass
        def visitExtendsInterfaces1(self, n, o): pass
        def visitConstantModifier0(self, n, o): pass
        def visitConstantModifier1(self, n, o): pass
        def visitConstantModifier2(self, n, o): pass
        def visitAbstractMethodModifier0(self, n, o): pass
        def visitAbstractMethodModifier1(self, n, o): pass
        def visitAnnotationTypeElementDeclaration0(self, n, o): pass
        def visitAnnotationTypeElementDeclaration1(self, n, o): pass
        def visitAssertStatement0(self, n, o): pass
        def visitAssertStatement1(self, n, o): pass
        def visitSwitchLabel0(self, n, o): pass
        def visitSwitchLabel1(self, n, o): pass
        def visitSwitchLabel2(self, n, o): pass
        def visitTryStatement0(self, n, o): pass
        def visitTryStatement1(self, n, o): pass
        def visitPrimaryNoNewArray0(self, n, o): pass
        def visitPrimaryNoNewArray1(self, n, o): pass
        def visitPrimaryNoNewArray2(self, n, o): pass
        def visitPrimaryNoNewArray3(self, n, o): pass
        def visitPrimaryNoNewArray4(self, n, o): pass
        def visitLiteral0(self, n, o): pass
        def visitLiteral1(self, n, o): pass
        def visitLiteral2(self, n, o): pass
        def visitLiteral3(self, n, o): pass
        def visitLiteral4(self, n, o): pass
        def visitLiteral5(self, n, o): pass
        def visitLiteral6(self, n, o): pass
        def visitBooleanLiteral0(self, n, o): pass
        def visitBooleanLiteral1(self, n, o): pass
        def visitClassInstanceCreationExpression0(self, n, o): pass
        def visitClassInstanceCreationExpression1(self, n, o): pass
        def visitArrayCreationExpression0(self, n, o): pass
        def visitArrayCreationExpression1(self, n, o): pass
        def visitArrayCreationExpression2(self, n, o): pass
        def visitArrayCreationExpression3(self, n, o): pass
        def visitDims0(self, n, o): pass
        def visitDims1(self, n, o): pass
        def visitFieldAccess0(self, n, o): pass
        def visitFieldAccess1(self, n, o): pass
        def visitFieldAccess2(self, n, o): pass
        def visitMethodInvocation0(self, n, o): pass
        def visitMethodInvocation1(self, n, o): pass
        def visitMethodInvocation2(self, n, o): pass
        def visitMethodInvocation3(self, n, o): pass
        def visitMethodInvocation4(self, n, o): pass
        def visitArrayAccess0(self, n, o): pass
        def visitArrayAccess1(self, n, o): pass
        def visitUnaryExpression0(self, n, o): pass
        def visitUnaryExpression1(self, n, o): pass
        def visitUnaryExpressionNotPlusMinus0(self, n, o): pass
        def visitUnaryExpressionNotPlusMinus1(self, n, o): pass
        def visitCastExpression0(self, n, o): pass
        def visitCastExpression1(self, n, o): pass
        def visitMultiplicativeExpression0(self, n, o): pass
        def visitMultiplicativeExpression1(self, n, o): pass
        def visitMultiplicativeExpression2(self, n, o): pass
        def visitAdditiveExpression0(self, n, o): pass
        def visitAdditiveExpression1(self, n, o): pass
        def visitShiftExpression0(self, n, o): pass
        def visitShiftExpression1(self, n, o): pass
        def visitShiftExpression2(self, n, o): pass
        def visitRelationalExpression0(self, n, o): pass
        def visitRelationalExpression1(self, n, o): pass
        def visitRelationalExpression2(self, n, o): pass
        def visitRelationalExpression3(self, n, o): pass
        def visitRelationalExpression4(self, n, o): pass
        def visitEqualityExpression0(self, n, o): pass
        def visitEqualityExpression1(self, n, o): pass
        def visitAssignmentOperator0(self, n, o): pass
        def visitAssignmentOperator1(self, n, o): pass
        def visitAssignmentOperator2(self, n, o): pass
        def visitAssignmentOperator3(self, n, o): pass
        def visitAssignmentOperator4(self, n, o): pass
        def visitAssignmentOperator5(self, n, o): pass
        def visitAssignmentOperator6(self, n, o): pass
        def visitAssignmentOperator7(self, n, o): pass
        def visitAssignmentOperator8(self, n, o): pass
        def visitAssignmentOperator9(self, n, o): pass
        def visitAssignmentOperator10(self, n, o): pass
        def visitAssignmentOperator11(self, n, o): pass

        def visit(self, n, o): pass
    
class AbstractVisitor ( Visitor, ArgumentVisitor):
          __slots__ = ()
    
          def unimplementedVisitor(self,s) :raise TypeError('Can not instantiate abstract class  with abstract methods') 

          def visitAstToken(self, n, o = None): self.unimplementedVisitor("visitAstToken(AstToken, any)")

          def visitidentifier(self, n, o = None): self.unimplementedVisitor("visitidentifier(identifier, any)")

          def visitPrimitiveType(self, n, o = None): self.unimplementedVisitor("visitPrimitiveType(PrimitiveType, any)")

          def visitClassType(self, n, o = None): self.unimplementedVisitor("visitClassType(ClassType, any)")

          def visitInterfaceType(self, n, o = None): self.unimplementedVisitor("visitInterfaceType(InterfaceType, any)")

          def visitTypeName(self, n, o = None): self.unimplementedVisitor("visitTypeName(TypeName, any)")

          def visitArrayType(self, n, o = None): self.unimplementedVisitor("visitArrayType(ArrayType, any)")

          def visitTypeParameter(self, n, o = None): self.unimplementedVisitor("visitTypeParameter(TypeParameter, any)")

          def visitTypeBound(self, n, o = None): self.unimplementedVisitor("visitTypeBound(TypeBound, any)")

          def visitAdditionalBoundList(self, n, o = None): self.unimplementedVisitor("visitAdditionalBoundList(AdditionalBoundList, any)")

          def visitAdditionalBound(self, n, o = None): self.unimplementedVisitor("visitAdditionalBound(AdditionalBound, any)")

          def visitTypeArguments(self, n, o = None): self.unimplementedVisitor("visitTypeArguments(TypeArguments, any)")

          def visitActualTypeArgumentList(self, n, o = None): self.unimplementedVisitor("visitActualTypeArgumentList(ActualTypeArgumentList, any)")

          def visitWildcard(self, n, o = None): self.unimplementedVisitor("visitWildcard(Wildcard, any)")

          def visitPackageName(self, n, o = None): self.unimplementedVisitor("visitPackageName(PackageName, any)")

          def visitExpressionName(self, n, o = None): self.unimplementedVisitor("visitExpressionName(ExpressionName, any)")

          def visitMethodName(self, n, o = None): self.unimplementedVisitor("visitMethodName(MethodName, any)")

          def visitPackageOrTypeName(self, n, o = None): self.unimplementedVisitor("visitPackageOrTypeName(PackageOrTypeName, any)")

          def visitAmbiguousName(self, n, o = None): self.unimplementedVisitor("visitAmbiguousName(AmbiguousName, any)")

          def visitCompilationUnit(self, n, o = None): self.unimplementedVisitor("visitCompilationUnit(CompilationUnit, any)")

          def visitImportDeclarations(self, n, o = None): self.unimplementedVisitor("visitImportDeclarations(ImportDeclarations, any)")

          def visitTypeDeclarations(self, n, o = None): self.unimplementedVisitor("visitTypeDeclarations(TypeDeclarations, any)")

          def visitPackageDeclaration(self, n, o = None): self.unimplementedVisitor("visitPackageDeclaration(PackageDeclaration, any)")

          def visitSingleTypeImportDeclaration(self, n, o = None): self.unimplementedVisitor("visitSingleTypeImportDeclaration(SingleTypeImportDeclaration, any)")

          def visitTypeImportOnDemandDeclaration(self, n, o = None): self.unimplementedVisitor("visitTypeImportOnDemandDeclaration(TypeImportOnDemandDeclaration, any)")

          def visitSingleStaticImportDeclaration(self, n, o = None): self.unimplementedVisitor("visitSingleStaticImportDeclaration(SingleStaticImportDeclaration, any)")

          def visitStaticImportOnDemandDeclaration(self, n, o = None): self.unimplementedVisitor("visitStaticImportOnDemandDeclaration(StaticImportOnDemandDeclaration, any)")

          def visitTypeDeclaration(self, n, o = None): self.unimplementedVisitor("visitTypeDeclaration(TypeDeclaration, any)")

          def visitNormalClassDeclaration(self, n, o = None): self.unimplementedVisitor("visitNormalClassDeclaration(NormalClassDeclaration, any)")

          def visitClassModifiers(self, n, o = None): self.unimplementedVisitor("visitClassModifiers(ClassModifiers, any)")

          def visitTypeParameters(self, n, o = None): self.unimplementedVisitor("visitTypeParameters(TypeParameters, any)")

          def visitTypeParameterList(self, n, o = None): self.unimplementedVisitor("visitTypeParameterList(TypeParameterList, any)")

          def visitSuper(self, n, o = None): self.unimplementedVisitor("visitSuper(Super, any)")

          def visitInterfaces(self, n, o = None): self.unimplementedVisitor("visitInterfaces(Interfaces, any)")

          def visitInterfaceTypeList(self, n, o = None): self.unimplementedVisitor("visitInterfaceTypeList(InterfaceTypeList, any)")

          def visitClassBody(self, n, o = None): self.unimplementedVisitor("visitClassBody(ClassBody, any)")

          def visitClassBodyDeclarations(self, n, o = None): self.unimplementedVisitor("visitClassBodyDeclarations(ClassBodyDeclarations, any)")

          def visitClassMemberDeclaration(self, n, o = None): self.unimplementedVisitor("visitClassMemberDeclaration(ClassMemberDeclaration, any)")

          def visitFieldDeclaration(self, n, o = None): self.unimplementedVisitor("visitFieldDeclaration(FieldDeclaration, any)")

          def visitVariableDeclarators(self, n, o = None): self.unimplementedVisitor("visitVariableDeclarators(VariableDeclarators, any)")

          def visitVariableDeclarator(self, n, o = None): self.unimplementedVisitor("visitVariableDeclarator(VariableDeclarator, any)")

          def visitVariableDeclaratorId(self, n, o = None): self.unimplementedVisitor("visitVariableDeclaratorId(VariableDeclaratorId, any)")

          def visitFieldModifiers(self, n, o = None): self.unimplementedVisitor("visitFieldModifiers(FieldModifiers, any)")

          def visitMethodDeclaration(self, n, o = None): self.unimplementedVisitor("visitMethodDeclaration(MethodDeclaration, any)")

          def visitMethodHeader(self, n, o = None): self.unimplementedVisitor("visitMethodHeader(MethodHeader, any)")

          def visitResultType(self, n, o = None): self.unimplementedVisitor("visitResultType(ResultType, any)")

          def visitFormalParameterList(self, n, o = None): self.unimplementedVisitor("visitFormalParameterList(FormalParameterList, any)")

          def visitFormalParameters(self, n, o = None): self.unimplementedVisitor("visitFormalParameters(FormalParameters, any)")

          def visitFormalParameter(self, n, o = None): self.unimplementedVisitor("visitFormalParameter(FormalParameter, any)")

          def visitVariableModifiers(self, n, o = None): self.unimplementedVisitor("visitVariableModifiers(VariableModifiers, any)")

          def visitVariableModifier(self, n, o = None): self.unimplementedVisitor("visitVariableModifier(VariableModifier, any)")

          def visitLastFormalParameter(self, n, o = None): self.unimplementedVisitor("visitLastFormalParameter(LastFormalParameter, any)")

          def visitMethodModifiers(self, n, o = None): self.unimplementedVisitor("visitMethodModifiers(MethodModifiers, any)")

          def visitThrows(self, n, o = None): self.unimplementedVisitor("visitThrows(Throws, any)")

          def visitExceptionTypeList(self, n, o = None): self.unimplementedVisitor("visitExceptionTypeList(ExceptionTypeList, any)")

          def visitMethodBody(self, n, o = None): self.unimplementedVisitor("visitMethodBody(MethodBody, any)")

          def visitStaticInitializer(self, n, o = None): self.unimplementedVisitor("visitStaticInitializer(StaticInitializer, any)")

          def visitConstructorDeclaration(self, n, o = None): self.unimplementedVisitor("visitConstructorDeclaration(ConstructorDeclaration, any)")

          def visitConstructorDeclarator(self, n, o = None): self.unimplementedVisitor("visitConstructorDeclarator(ConstructorDeclarator, any)")

          def visitConstructorModifiers(self, n, o = None): self.unimplementedVisitor("visitConstructorModifiers(ConstructorModifiers, any)")

          def visitConstructorBody(self, n, o = None): self.unimplementedVisitor("visitConstructorBody(ConstructorBody, any)")

          def visitEnumDeclaration(self, n, o = None): self.unimplementedVisitor("visitEnumDeclaration(EnumDeclaration, any)")

          def visitEnumBody(self, n, o = None): self.unimplementedVisitor("visitEnumBody(EnumBody, any)")

          def visitEnumConstants(self, n, o = None): self.unimplementedVisitor("visitEnumConstants(EnumConstants, any)")

          def visitEnumConstant(self, n, o = None): self.unimplementedVisitor("visitEnumConstant(EnumConstant, any)")

          def visitArguments(self, n, o = None): self.unimplementedVisitor("visitArguments(Arguments, any)")

          def visitEnumBodyDeclarations(self, n, o = None): self.unimplementedVisitor("visitEnumBodyDeclarations(EnumBodyDeclarations, any)")

          def visitNormalInterfaceDeclaration(self, n, o = None): self.unimplementedVisitor("visitNormalInterfaceDeclaration(NormalInterfaceDeclaration, any)")

          def visitInterfaceModifiers(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifiers(InterfaceModifiers, any)")

          def visitInterfaceBody(self, n, o = None): self.unimplementedVisitor("visitInterfaceBody(InterfaceBody, any)")

          def visitInterfaceMemberDeclarations(self, n, o = None): self.unimplementedVisitor("visitInterfaceMemberDeclarations(InterfaceMemberDeclarations, any)")

          def visitInterfaceMemberDeclaration(self, n, o = None): self.unimplementedVisitor("visitInterfaceMemberDeclaration(InterfaceMemberDeclaration, any)")

          def visitConstantDeclaration(self, n, o = None): self.unimplementedVisitor("visitConstantDeclaration(ConstantDeclaration, any)")

          def visitConstantModifiers(self, n, o = None): self.unimplementedVisitor("visitConstantModifiers(ConstantModifiers, any)")

          def visitAbstractMethodDeclaration(self, n, o = None): self.unimplementedVisitor("visitAbstractMethodDeclaration(AbstractMethodDeclaration, any)")

          def visitAbstractMethodModifiers(self, n, o = None): self.unimplementedVisitor("visitAbstractMethodModifiers(AbstractMethodModifiers, any)")

          def visitAnnotationTypeDeclaration(self, n, o = None): self.unimplementedVisitor("visitAnnotationTypeDeclaration(AnnotationTypeDeclaration, any)")

          def visitAnnotationTypeBody(self, n, o = None): self.unimplementedVisitor("visitAnnotationTypeBody(AnnotationTypeBody, any)")

          def visitAnnotationTypeElementDeclarations(self, n, o = None): self.unimplementedVisitor("visitAnnotationTypeElementDeclarations(AnnotationTypeElementDeclarations, any)")

          def visitDefaultValue(self, n, o = None): self.unimplementedVisitor("visitDefaultValue(DefaultValue, any)")

          def visitAnnotations(self, n, o = None): self.unimplementedVisitor("visitAnnotations(Annotations, any)")

          def visitNormalAnnotation(self, n, o = None): self.unimplementedVisitor("visitNormalAnnotation(NormalAnnotation, any)")

          def visitElementValuePairs(self, n, o = None): self.unimplementedVisitor("visitElementValuePairs(ElementValuePairs, any)")

          def visitElementValuePair(self, n, o = None): self.unimplementedVisitor("visitElementValuePair(ElementValuePair, any)")

          def visitElementValueArrayInitializer(self, n, o = None): self.unimplementedVisitor("visitElementValueArrayInitializer(ElementValueArrayInitializer, any)")

          def visitElementValues(self, n, o = None): self.unimplementedVisitor("visitElementValues(ElementValues, any)")

          def visitMarkerAnnotation(self, n, o = None): self.unimplementedVisitor("visitMarkerAnnotation(MarkerAnnotation, any)")

          def visitSingleElementAnnotation(self, n, o = None): self.unimplementedVisitor("visitSingleElementAnnotation(SingleElementAnnotation, any)")

          def visitArrayInitializer(self, n, o = None): self.unimplementedVisitor("visitArrayInitializer(ArrayInitializer, any)")

          def visitVariableInitializers(self, n, o = None): self.unimplementedVisitor("visitVariableInitializers(VariableInitializers, any)")

          def visitBlock(self, n, o = None): self.unimplementedVisitor("visitBlock(Block, any)")

          def visitBlockStatements(self, n, o = None): self.unimplementedVisitor("visitBlockStatements(BlockStatements, any)")

          def visitLocalVariableDeclarationStatement(self, n, o = None): self.unimplementedVisitor("visitLocalVariableDeclarationStatement(LocalVariableDeclarationStatement, any)")

          def visitLocalVariableDeclaration(self, n, o = None): self.unimplementedVisitor("visitLocalVariableDeclaration(LocalVariableDeclaration, any)")

          def visitIfThenStatement(self, n, o = None): self.unimplementedVisitor("visitIfThenStatement(IfThenStatement, any)")

          def visitIfThenElseStatement(self, n, o = None): self.unimplementedVisitor("visitIfThenElseStatement(IfThenElseStatement, any)")

          def visitIfThenElseStatementNoShortIf(self, n, o = None): self.unimplementedVisitor("visitIfThenElseStatementNoShortIf(IfThenElseStatementNoShortIf, any)")

          def visitEmptyStatement(self, n, o = None): self.unimplementedVisitor("visitEmptyStatement(EmptyStatement, any)")

          def visitLabeledStatement(self, n, o = None): self.unimplementedVisitor("visitLabeledStatement(LabeledStatement, any)")

          def visitLabeledStatementNoShortIf(self, n, o = None): self.unimplementedVisitor("visitLabeledStatementNoShortIf(LabeledStatementNoShortIf, any)")

          def visitExpressionStatement(self, n, o = None): self.unimplementedVisitor("visitExpressionStatement(ExpressionStatement, any)")

          def visitSwitchStatement(self, n, o = None): self.unimplementedVisitor("visitSwitchStatement(SwitchStatement, any)")

          def visitSwitchBlock(self, n, o = None): self.unimplementedVisitor("visitSwitchBlock(SwitchBlock, any)")

          def visitSwitchBlockStatementGroups(self, n, o = None): self.unimplementedVisitor("visitSwitchBlockStatementGroups(SwitchBlockStatementGroups, any)")

          def visitSwitchBlockStatementGroup(self, n, o = None): self.unimplementedVisitor("visitSwitchBlockStatementGroup(SwitchBlockStatementGroup, any)")

          def visitSwitchLabels(self, n, o = None): self.unimplementedVisitor("visitSwitchLabels(SwitchLabels, any)")

          def visitWhileStatement(self, n, o = None): self.unimplementedVisitor("visitWhileStatement(WhileStatement, any)")

          def visitWhileStatementNoShortIf(self, n, o = None): self.unimplementedVisitor("visitWhileStatementNoShortIf(WhileStatementNoShortIf, any)")

          def visitDoStatement(self, n, o = None): self.unimplementedVisitor("visitDoStatement(DoStatement, any)")

          def visitBasicForStatement(self, n, o = None): self.unimplementedVisitor("visitBasicForStatement(BasicForStatement, any)")

          def visitForStatementNoShortIf(self, n, o = None): self.unimplementedVisitor("visitForStatementNoShortIf(ForStatementNoShortIf, any)")

          def visitStatementExpressionList(self, n, o = None): self.unimplementedVisitor("visitStatementExpressionList(StatementExpressionList, any)")

          def visitEnhancedForStatement(self, n, o = None): self.unimplementedVisitor("visitEnhancedForStatement(EnhancedForStatement, any)")

          def visitBreakStatement(self, n, o = None): self.unimplementedVisitor("visitBreakStatement(BreakStatement, any)")

          def visitContinueStatement(self, n, o = None): self.unimplementedVisitor("visitContinueStatement(ContinueStatement, any)")

          def visitReturnStatement(self, n, o = None): self.unimplementedVisitor("visitReturnStatement(ReturnStatement, any)")

          def visitThrowStatement(self, n, o = None): self.unimplementedVisitor("visitThrowStatement(ThrowStatement, any)")

          def visitSynchronizedStatement(self, n, o = None): self.unimplementedVisitor("visitSynchronizedStatement(SynchronizedStatement, any)")

          def visitCatches(self, n, o = None): self.unimplementedVisitor("visitCatches(Catches, any)")

          def visitCatchClause(self, n, o = None): self.unimplementedVisitor("visitCatchClause(CatchClause, any)")

          def visitFinally(self, n, o = None): self.unimplementedVisitor("visitFinally(Finally, any)")

          def visitArgumentList(self, n, o = None): self.unimplementedVisitor("visitArgumentList(ArgumentList, any)")

          def visitDimExprs(self, n, o = None): self.unimplementedVisitor("visitDimExprs(DimExprs, any)")

          def visitDimExpr(self, n, o = None): self.unimplementedVisitor("visitDimExpr(DimExpr, any)")

          def visitPostIncrementExpression(self, n, o = None): self.unimplementedVisitor("visitPostIncrementExpression(PostIncrementExpression, any)")

          def visitPostDecrementExpression(self, n, o = None): self.unimplementedVisitor("visitPostDecrementExpression(PostDecrementExpression, any)")

          def visitPreIncrementExpression(self, n, o = None): self.unimplementedVisitor("visitPreIncrementExpression(PreIncrementExpression, any)")

          def visitPreDecrementExpression(self, n, o = None): self.unimplementedVisitor("visitPreDecrementExpression(PreDecrementExpression, any)")

          def visitAndExpression(self, n, o = None): self.unimplementedVisitor("visitAndExpression(AndExpression, any)")

          def visitExclusiveOrExpression(self, n, o = None): self.unimplementedVisitor("visitExclusiveOrExpression(ExclusiveOrExpression, any)")

          def visitInclusiveOrExpression(self, n, o = None): self.unimplementedVisitor("visitInclusiveOrExpression(InclusiveOrExpression, any)")

          def visitConditionalAndExpression(self, n, o = None): self.unimplementedVisitor("visitConditionalAndExpression(ConditionalAndExpression, any)")

          def visitConditionalOrExpression(self, n, o = None): self.unimplementedVisitor("visitConditionalOrExpression(ConditionalOrExpression, any)")

          def visitConditionalExpression(self, n, o = None): self.unimplementedVisitor("visitConditionalExpression(ConditionalExpression, any)")

          def visitAssignment(self, n, o = None): self.unimplementedVisitor("visitAssignment(Assignment, any)")

          def visitCommaopt(self, n, o = None): self.unimplementedVisitor("visitCommaopt(Commaopt, any)")

          def visitEllipsisopt(self, n, o = None): self.unimplementedVisitor("visitEllipsisopt(Ellipsisopt, any)")

          def visitLPGUserAction0(self, n, o = None): self.unimplementedVisitor("visitLPGUserAction0(LPGUserAction0, any)")

          def visitLPGUserAction1(self, n, o = None): self.unimplementedVisitor("visitLPGUserAction1(LPGUserAction1, any)")

          def visitLPGUserAction2(self, n, o = None): self.unimplementedVisitor("visitLPGUserAction2(LPGUserAction2, any)")

          def visitLPGUserAction3(self, n, o = None): self.unimplementedVisitor("visitLPGUserAction3(LPGUserAction3, any)")

          def visitLPGUserAction4(self, n, o = None): self.unimplementedVisitor("visitLPGUserAction4(LPGUserAction4, any)")

          def visitIntegralType0(self, n, o = None): self.unimplementedVisitor("visitIntegralType0(IntegralType0, any)")

          def visitIntegralType1(self, n, o = None): self.unimplementedVisitor("visitIntegralType1(IntegralType1, any)")

          def visitIntegralType2(self, n, o = None): self.unimplementedVisitor("visitIntegralType2(IntegralType2, any)")

          def visitIntegralType3(self, n, o = None): self.unimplementedVisitor("visitIntegralType3(IntegralType3, any)")

          def visitIntegralType4(self, n, o = None): self.unimplementedVisitor("visitIntegralType4(IntegralType4, any)")

          def visitFloatingPointType0(self, n, o = None): self.unimplementedVisitor("visitFloatingPointType0(FloatingPointType0, any)")

          def visitFloatingPointType1(self, n, o = None): self.unimplementedVisitor("visitFloatingPointType1(FloatingPointType1, any)")

          def visitWildcardBounds0(self, n, o = None): self.unimplementedVisitor("visitWildcardBounds0(WildcardBounds0, any)")

          def visitWildcardBounds1(self, n, o = None): self.unimplementedVisitor("visitWildcardBounds1(WildcardBounds1, any)")

          def visitClassModifier0(self, n, o = None): self.unimplementedVisitor("visitClassModifier0(ClassModifier0, any)")

          def visitClassModifier1(self, n, o = None): self.unimplementedVisitor("visitClassModifier1(ClassModifier1, any)")

          def visitClassModifier2(self, n, o = None): self.unimplementedVisitor("visitClassModifier2(ClassModifier2, any)")

          def visitClassModifier3(self, n, o = None): self.unimplementedVisitor("visitClassModifier3(ClassModifier3, any)")

          def visitClassModifier4(self, n, o = None): self.unimplementedVisitor("visitClassModifier4(ClassModifier4, any)")

          def visitClassModifier5(self, n, o = None): self.unimplementedVisitor("visitClassModifier5(ClassModifier5, any)")

          def visitClassModifier6(self, n, o = None): self.unimplementedVisitor("visitClassModifier6(ClassModifier6, any)")

          def visitFieldModifier0(self, n, o = None): self.unimplementedVisitor("visitFieldModifier0(FieldModifier0, any)")

          def visitFieldModifier1(self, n, o = None): self.unimplementedVisitor("visitFieldModifier1(FieldModifier1, any)")

          def visitFieldModifier2(self, n, o = None): self.unimplementedVisitor("visitFieldModifier2(FieldModifier2, any)")

          def visitFieldModifier3(self, n, o = None): self.unimplementedVisitor("visitFieldModifier3(FieldModifier3, any)")

          def visitFieldModifier4(self, n, o = None): self.unimplementedVisitor("visitFieldModifier4(FieldModifier4, any)")

          def visitFieldModifier5(self, n, o = None): self.unimplementedVisitor("visitFieldModifier5(FieldModifier5, any)")

          def visitFieldModifier6(self, n, o = None): self.unimplementedVisitor("visitFieldModifier6(FieldModifier6, any)")

          def visitMethodDeclarator0(self, n, o = None): self.unimplementedVisitor("visitMethodDeclarator0(MethodDeclarator0, any)")

          def visitMethodDeclarator1(self, n, o = None): self.unimplementedVisitor("visitMethodDeclarator1(MethodDeclarator1, any)")

          def visitMethodModifier0(self, n, o = None): self.unimplementedVisitor("visitMethodModifier0(MethodModifier0, any)")

          def visitMethodModifier1(self, n, o = None): self.unimplementedVisitor("visitMethodModifier1(MethodModifier1, any)")

          def visitMethodModifier2(self, n, o = None): self.unimplementedVisitor("visitMethodModifier2(MethodModifier2, any)")

          def visitMethodModifier3(self, n, o = None): self.unimplementedVisitor("visitMethodModifier3(MethodModifier3, any)")

          def visitMethodModifier4(self, n, o = None): self.unimplementedVisitor("visitMethodModifier4(MethodModifier4, any)")

          def visitMethodModifier5(self, n, o = None): self.unimplementedVisitor("visitMethodModifier5(MethodModifier5, any)")

          def visitMethodModifier6(self, n, o = None): self.unimplementedVisitor("visitMethodModifier6(MethodModifier6, any)")

          def visitMethodModifier7(self, n, o = None): self.unimplementedVisitor("visitMethodModifier7(MethodModifier7, any)")

          def visitMethodModifier8(self, n, o = None): self.unimplementedVisitor("visitMethodModifier8(MethodModifier8, any)")

          def visitConstructorModifier0(self, n, o = None): self.unimplementedVisitor("visitConstructorModifier0(ConstructorModifier0, any)")

          def visitConstructorModifier1(self, n, o = None): self.unimplementedVisitor("visitConstructorModifier1(ConstructorModifier1, any)")

          def visitConstructorModifier2(self, n, o = None): self.unimplementedVisitor("visitConstructorModifier2(ConstructorModifier2, any)")

          def visitExplicitConstructorInvocation0(self, n, o = None): self.unimplementedVisitor("visitExplicitConstructorInvocation0(ExplicitConstructorInvocation0, any)")

          def visitExplicitConstructorInvocation1(self, n, o = None): self.unimplementedVisitor("visitExplicitConstructorInvocation1(ExplicitConstructorInvocation1, any)")

          def visitExplicitConstructorInvocation2(self, n, o = None): self.unimplementedVisitor("visitExplicitConstructorInvocation2(ExplicitConstructorInvocation2, any)")

          def visitInterfaceModifier0(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifier0(InterfaceModifier0, any)")

          def visitInterfaceModifier1(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifier1(InterfaceModifier1, any)")

          def visitInterfaceModifier2(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifier2(InterfaceModifier2, any)")

          def visitInterfaceModifier3(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifier3(InterfaceModifier3, any)")

          def visitInterfaceModifier4(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifier4(InterfaceModifier4, any)")

          def visitInterfaceModifier5(self, n, o = None): self.unimplementedVisitor("visitInterfaceModifier5(InterfaceModifier5, any)")

          def visitExtendsInterfaces0(self, n, o = None): self.unimplementedVisitor("visitExtendsInterfaces0(ExtendsInterfaces0, any)")

          def visitExtendsInterfaces1(self, n, o = None): self.unimplementedVisitor("visitExtendsInterfaces1(ExtendsInterfaces1, any)")

          def visitConstantModifier0(self, n, o = None): self.unimplementedVisitor("visitConstantModifier0(ConstantModifier0, any)")

          def visitConstantModifier1(self, n, o = None): self.unimplementedVisitor("visitConstantModifier1(ConstantModifier1, any)")

          def visitConstantModifier2(self, n, o = None): self.unimplementedVisitor("visitConstantModifier2(ConstantModifier2, any)")

          def visitAbstractMethodModifier0(self, n, o = None): self.unimplementedVisitor("visitAbstractMethodModifier0(AbstractMethodModifier0, any)")

          def visitAbstractMethodModifier1(self, n, o = None): self.unimplementedVisitor("visitAbstractMethodModifier1(AbstractMethodModifier1, any)")

          def visitAnnotationTypeElementDeclaration0(self, n, o = None): self.unimplementedVisitor("visitAnnotationTypeElementDeclaration0(AnnotationTypeElementDeclaration0, any)")

          def visitAnnotationTypeElementDeclaration1(self, n, o = None): self.unimplementedVisitor("visitAnnotationTypeElementDeclaration1(AnnotationTypeElementDeclaration1, any)")

          def visitAssertStatement0(self, n, o = None): self.unimplementedVisitor("visitAssertStatement0(AssertStatement0, any)")

          def visitAssertStatement1(self, n, o = None): self.unimplementedVisitor("visitAssertStatement1(AssertStatement1, any)")

          def visitSwitchLabel0(self, n, o = None): self.unimplementedVisitor("visitSwitchLabel0(SwitchLabel0, any)")

          def visitSwitchLabel1(self, n, o = None): self.unimplementedVisitor("visitSwitchLabel1(SwitchLabel1, any)")

          def visitSwitchLabel2(self, n, o = None): self.unimplementedVisitor("visitSwitchLabel2(SwitchLabel2, any)")

          def visitTryStatement0(self, n, o = None): self.unimplementedVisitor("visitTryStatement0(TryStatement0, any)")

          def visitTryStatement1(self, n, o = None): self.unimplementedVisitor("visitTryStatement1(TryStatement1, any)")

          def visitPrimaryNoNewArray0(self, n, o = None): self.unimplementedVisitor("visitPrimaryNoNewArray0(PrimaryNoNewArray0, any)")

          def visitPrimaryNoNewArray1(self, n, o = None): self.unimplementedVisitor("visitPrimaryNoNewArray1(PrimaryNoNewArray1, any)")

          def visitPrimaryNoNewArray2(self, n, o = None): self.unimplementedVisitor("visitPrimaryNoNewArray2(PrimaryNoNewArray2, any)")

          def visitPrimaryNoNewArray3(self, n, o = None): self.unimplementedVisitor("visitPrimaryNoNewArray3(PrimaryNoNewArray3, any)")

          def visitPrimaryNoNewArray4(self, n, o = None): self.unimplementedVisitor("visitPrimaryNoNewArray4(PrimaryNoNewArray4, any)")

          def visitLiteral0(self, n, o = None): self.unimplementedVisitor("visitLiteral0(Literal0, any)")

          def visitLiteral1(self, n, o = None): self.unimplementedVisitor("visitLiteral1(Literal1, any)")

          def visitLiteral2(self, n, o = None): self.unimplementedVisitor("visitLiteral2(Literal2, any)")

          def visitLiteral3(self, n, o = None): self.unimplementedVisitor("visitLiteral3(Literal3, any)")

          def visitLiteral4(self, n, o = None): self.unimplementedVisitor("visitLiteral4(Literal4, any)")

          def visitLiteral5(self, n, o = None): self.unimplementedVisitor("visitLiteral5(Literal5, any)")

          def visitLiteral6(self, n, o = None): self.unimplementedVisitor("visitLiteral6(Literal6, any)")

          def visitBooleanLiteral0(self, n, o = None): self.unimplementedVisitor("visitBooleanLiteral0(BooleanLiteral0, any)")

          def visitBooleanLiteral1(self, n, o = None): self.unimplementedVisitor("visitBooleanLiteral1(BooleanLiteral1, any)")

          def visitClassInstanceCreationExpression0(self, n, o = None): self.unimplementedVisitor("visitClassInstanceCreationExpression0(ClassInstanceCreationExpression0, any)")

          def visitClassInstanceCreationExpression1(self, n, o = None): self.unimplementedVisitor("visitClassInstanceCreationExpression1(ClassInstanceCreationExpression1, any)")

          def visitArrayCreationExpression0(self, n, o = None): self.unimplementedVisitor("visitArrayCreationExpression0(ArrayCreationExpression0, any)")

          def visitArrayCreationExpression1(self, n, o = None): self.unimplementedVisitor("visitArrayCreationExpression1(ArrayCreationExpression1, any)")

          def visitArrayCreationExpression2(self, n, o = None): self.unimplementedVisitor("visitArrayCreationExpression2(ArrayCreationExpression2, any)")

          def visitArrayCreationExpression3(self, n, o = None): self.unimplementedVisitor("visitArrayCreationExpression3(ArrayCreationExpression3, any)")

          def visitDims0(self, n, o = None): self.unimplementedVisitor("visitDims0(Dims0, any)")

          def visitDims1(self, n, o = None): self.unimplementedVisitor("visitDims1(Dims1, any)")

          def visitFieldAccess0(self, n, o = None): self.unimplementedVisitor("visitFieldAccess0(FieldAccess0, any)")

          def visitFieldAccess1(self, n, o = None): self.unimplementedVisitor("visitFieldAccess1(FieldAccess1, any)")

          def visitFieldAccess2(self, n, o = None): self.unimplementedVisitor("visitFieldAccess2(FieldAccess2, any)")

          def visitMethodInvocation0(self, n, o = None): self.unimplementedVisitor("visitMethodInvocation0(MethodInvocation0, any)")

          def visitMethodInvocation1(self, n, o = None): self.unimplementedVisitor("visitMethodInvocation1(MethodInvocation1, any)")

          def visitMethodInvocation2(self, n, o = None): self.unimplementedVisitor("visitMethodInvocation2(MethodInvocation2, any)")

          def visitMethodInvocation3(self, n, o = None): self.unimplementedVisitor("visitMethodInvocation3(MethodInvocation3, any)")

          def visitMethodInvocation4(self, n, o = None): self.unimplementedVisitor("visitMethodInvocation4(MethodInvocation4, any)")

          def visitArrayAccess0(self, n, o = None): self.unimplementedVisitor("visitArrayAccess0(ArrayAccess0, any)")

          def visitArrayAccess1(self, n, o = None): self.unimplementedVisitor("visitArrayAccess1(ArrayAccess1, any)")

          def visitUnaryExpression0(self, n, o = None): self.unimplementedVisitor("visitUnaryExpression0(UnaryExpression0, any)")

          def visitUnaryExpression1(self, n, o = None): self.unimplementedVisitor("visitUnaryExpression1(UnaryExpression1, any)")

          def visitUnaryExpressionNotPlusMinus0(self, n, o = None): self.unimplementedVisitor("visitUnaryExpressionNotPlusMinus0(UnaryExpressionNotPlusMinus0, any)")

          def visitUnaryExpressionNotPlusMinus1(self, n, o = None): self.unimplementedVisitor("visitUnaryExpressionNotPlusMinus1(UnaryExpressionNotPlusMinus1, any)")

          def visitCastExpression0(self, n, o = None): self.unimplementedVisitor("visitCastExpression0(CastExpression0, any)")

          def visitCastExpression1(self, n, o = None): self.unimplementedVisitor("visitCastExpression1(CastExpression1, any)")

          def visitMultiplicativeExpression0(self, n, o = None): self.unimplementedVisitor("visitMultiplicativeExpression0(MultiplicativeExpression0, any)")

          def visitMultiplicativeExpression1(self, n, o = None): self.unimplementedVisitor("visitMultiplicativeExpression1(MultiplicativeExpression1, any)")

          def visitMultiplicativeExpression2(self, n, o = None): self.unimplementedVisitor("visitMultiplicativeExpression2(MultiplicativeExpression2, any)")

          def visitAdditiveExpression0(self, n, o = None): self.unimplementedVisitor("visitAdditiveExpression0(AdditiveExpression0, any)")

          def visitAdditiveExpression1(self, n, o = None): self.unimplementedVisitor("visitAdditiveExpression1(AdditiveExpression1, any)")

          def visitShiftExpression0(self, n, o = None): self.unimplementedVisitor("visitShiftExpression0(ShiftExpression0, any)")

          def visitShiftExpression1(self, n, o = None): self.unimplementedVisitor("visitShiftExpression1(ShiftExpression1, any)")

          def visitShiftExpression2(self, n, o = None): self.unimplementedVisitor("visitShiftExpression2(ShiftExpression2, any)")

          def visitRelationalExpression0(self, n, o = None): self.unimplementedVisitor("visitRelationalExpression0(RelationalExpression0, any)")

          def visitRelationalExpression1(self, n, o = None): self.unimplementedVisitor("visitRelationalExpression1(RelationalExpression1, any)")

          def visitRelationalExpression2(self, n, o = None): self.unimplementedVisitor("visitRelationalExpression2(RelationalExpression2, any)")

          def visitRelationalExpression3(self, n, o = None): self.unimplementedVisitor("visitRelationalExpression3(RelationalExpression3, any)")

          def visitRelationalExpression4(self, n, o = None): self.unimplementedVisitor("visitRelationalExpression4(RelationalExpression4, any)")

          def visitEqualityExpression0(self, n, o = None): self.unimplementedVisitor("visitEqualityExpression0(EqualityExpression0, any)")

          def visitEqualityExpression1(self, n, o = None): self.unimplementedVisitor("visitEqualityExpression1(EqualityExpression1, any)")

          def visitAssignmentOperator0(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator0(AssignmentOperator0, any)")

          def visitAssignmentOperator1(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator1(AssignmentOperator1, any)")

          def visitAssignmentOperator2(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator2(AssignmentOperator2, any)")

          def visitAssignmentOperator3(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator3(AssignmentOperator3, any)")

          def visitAssignmentOperator4(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator4(AssignmentOperator4, any)")

          def visitAssignmentOperator5(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator5(AssignmentOperator5, any)")

          def visitAssignmentOperator6(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator6(AssignmentOperator6, any)")

          def visitAssignmentOperator7(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator7(AssignmentOperator7, any)")

          def visitAssignmentOperator8(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator8(AssignmentOperator8, any)")

          def visitAssignmentOperator9(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator9(AssignmentOperator9, any)")

          def visitAssignmentOperator10(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator10(AssignmentOperator10, any)")

          def visitAssignmentOperator11(self, n, o = None): self.unimplementedVisitor("visitAssignmentOperator11(AssignmentOperator11, any)")


          def visit(self, n, o = None): 
        
            if isinstance(n, AstToken): self.visitAstToken( n, o)
            elif isinstance(n, identifier): self.visitidentifier( n, o)
            elif isinstance(n, PrimitiveType): self.visitPrimitiveType( n, o)
            elif isinstance(n, ClassType): self.visitClassType( n, o)
            elif isinstance(n, InterfaceType): self.visitInterfaceType( n, o)
            elif isinstance(n, TypeName): self.visitTypeName( n, o)
            elif isinstance(n, ArrayType): self.visitArrayType( n, o)
            elif isinstance(n, TypeParameter): self.visitTypeParameter( n, o)
            elif isinstance(n, TypeBound): self.visitTypeBound( n, o)
            elif isinstance(n, AdditionalBoundList): self.visitAdditionalBoundList( n, o)
            elif isinstance(n, AdditionalBound): self.visitAdditionalBound( n, o)
            elif isinstance(n, TypeArguments): self.visitTypeArguments( n, o)
            elif isinstance(n, ActualTypeArgumentList): self.visitActualTypeArgumentList( n, o)
            elif isinstance(n, Wildcard): self.visitWildcard( n, o)
            elif isinstance(n, PackageName): self.visitPackageName( n, o)
            elif isinstance(n, ExpressionName): self.visitExpressionName( n, o)
            elif isinstance(n, MethodName): self.visitMethodName( n, o)
            elif isinstance(n, PackageOrTypeName): self.visitPackageOrTypeName( n, o)
            elif isinstance(n, AmbiguousName): self.visitAmbiguousName( n, o)
            elif isinstance(n, CompilationUnit): self.visitCompilationUnit( n, o)
            elif isinstance(n, ImportDeclarations): self.visitImportDeclarations( n, o)
            elif isinstance(n, TypeDeclarations): self.visitTypeDeclarations( n, o)
            elif isinstance(n, PackageDeclaration): self.visitPackageDeclaration( n, o)
            elif isinstance(n, SingleTypeImportDeclaration): self.visitSingleTypeImportDeclaration( n, o)
            elif isinstance(n, TypeImportOnDemandDeclaration): self.visitTypeImportOnDemandDeclaration( n, o)
            elif isinstance(n, SingleStaticImportDeclaration): self.visitSingleStaticImportDeclaration( n, o)
            elif isinstance(n, StaticImportOnDemandDeclaration): self.visitStaticImportOnDemandDeclaration( n, o)
            elif isinstance(n, TypeDeclaration): self.visitTypeDeclaration( n, o)
            elif isinstance(n, NormalClassDeclaration): self.visitNormalClassDeclaration( n, o)
            elif isinstance(n, ClassModifiers): self.visitClassModifiers( n, o)
            elif isinstance(n, TypeParameters): self.visitTypeParameters( n, o)
            elif isinstance(n, TypeParameterList): self.visitTypeParameterList( n, o)
            elif isinstance(n, Super): self.visitSuper( n, o)
            elif isinstance(n, Interfaces): self.visitInterfaces( n, o)
            elif isinstance(n, InterfaceTypeList): self.visitInterfaceTypeList( n, o)
            elif isinstance(n, ClassBody): self.visitClassBody( n, o)
            elif isinstance(n, ClassBodyDeclarations): self.visitClassBodyDeclarations( n, o)
            elif isinstance(n, ClassMemberDeclaration): self.visitClassMemberDeclaration( n, o)
            elif isinstance(n, FieldDeclaration): self.visitFieldDeclaration( n, o)
            elif isinstance(n, VariableDeclarators): self.visitVariableDeclarators( n, o)
            elif isinstance(n, VariableDeclarator): self.visitVariableDeclarator( n, o)
            elif isinstance(n, VariableDeclaratorId): self.visitVariableDeclaratorId( n, o)
            elif isinstance(n, FieldModifiers): self.visitFieldModifiers( n, o)
            elif isinstance(n, MethodDeclaration): self.visitMethodDeclaration( n, o)
            elif isinstance(n, MethodHeader): self.visitMethodHeader( n, o)
            elif isinstance(n, ResultType): self.visitResultType( n, o)
            elif isinstance(n, FormalParameterList): self.visitFormalParameterList( n, o)
            elif isinstance(n, FormalParameters): self.visitFormalParameters( n, o)
            elif isinstance(n, FormalParameter): self.visitFormalParameter( n, o)
            elif isinstance(n, VariableModifiers): self.visitVariableModifiers( n, o)
            elif isinstance(n, VariableModifier): self.visitVariableModifier( n, o)
            elif isinstance(n, LastFormalParameter): self.visitLastFormalParameter( n, o)
            elif isinstance(n, MethodModifiers): self.visitMethodModifiers( n, o)
            elif isinstance(n, Throws): self.visitThrows( n, o)
            elif isinstance(n, ExceptionTypeList): self.visitExceptionTypeList( n, o)
            elif isinstance(n, MethodBody): self.visitMethodBody( n, o)
            elif isinstance(n, StaticInitializer): self.visitStaticInitializer( n, o)
            elif isinstance(n, ConstructorDeclaration): self.visitConstructorDeclaration( n, o)
            elif isinstance(n, ConstructorDeclarator): self.visitConstructorDeclarator( n, o)
            elif isinstance(n, ConstructorModifiers): self.visitConstructorModifiers( n, o)
            elif isinstance(n, ConstructorBody): self.visitConstructorBody( n, o)
            elif isinstance(n, EnumDeclaration): self.visitEnumDeclaration( n, o)
            elif isinstance(n, EnumBody): self.visitEnumBody( n, o)
            elif isinstance(n, EnumConstants): self.visitEnumConstants( n, o)
            elif isinstance(n, EnumConstant): self.visitEnumConstant( n, o)
            elif isinstance(n, Arguments): self.visitArguments( n, o)
            elif isinstance(n, EnumBodyDeclarations): self.visitEnumBodyDeclarations( n, o)
            elif isinstance(n, NormalInterfaceDeclaration): self.visitNormalInterfaceDeclaration( n, o)
            elif isinstance(n, InterfaceModifiers): self.visitInterfaceModifiers( n, o)
            elif isinstance(n, InterfaceBody): self.visitInterfaceBody( n, o)
            elif isinstance(n, InterfaceMemberDeclarations): self.visitInterfaceMemberDeclarations( n, o)
            elif isinstance(n, InterfaceMemberDeclaration): self.visitInterfaceMemberDeclaration( n, o)
            elif isinstance(n, ConstantDeclaration): self.visitConstantDeclaration( n, o)
            elif isinstance(n, ConstantModifiers): self.visitConstantModifiers( n, o)
            elif isinstance(n, AbstractMethodDeclaration): self.visitAbstractMethodDeclaration( n, o)
            elif isinstance(n, AbstractMethodModifiers): self.visitAbstractMethodModifiers( n, o)
            elif isinstance(n, AnnotationTypeDeclaration): self.visitAnnotationTypeDeclaration( n, o)
            elif isinstance(n, AnnotationTypeBody): self.visitAnnotationTypeBody( n, o)
            elif isinstance(n, AnnotationTypeElementDeclarations): self.visitAnnotationTypeElementDeclarations( n, o)
            elif isinstance(n, DefaultValue): self.visitDefaultValue( n, o)
            elif isinstance(n, Annotations): self.visitAnnotations( n, o)
            elif isinstance(n, NormalAnnotation): self.visitNormalAnnotation( n, o)
            elif isinstance(n, ElementValuePairs): self.visitElementValuePairs( n, o)
            elif isinstance(n, ElementValuePair): self.visitElementValuePair( n, o)
            elif isinstance(n, ElementValueArrayInitializer): self.visitElementValueArrayInitializer( n, o)
            elif isinstance(n, ElementValues): self.visitElementValues( n, o)
            elif isinstance(n, MarkerAnnotation): self.visitMarkerAnnotation( n, o)
            elif isinstance(n, SingleElementAnnotation): self.visitSingleElementAnnotation( n, o)
            elif isinstance(n, ArrayInitializer): self.visitArrayInitializer( n, o)
            elif isinstance(n, VariableInitializers): self.visitVariableInitializers( n, o)
            elif isinstance(n, Block): self.visitBlock( n, o)
            elif isinstance(n, BlockStatements): self.visitBlockStatements( n, o)
            elif isinstance(n, LocalVariableDeclarationStatement): self.visitLocalVariableDeclarationStatement( n, o)
            elif isinstance(n, LocalVariableDeclaration): self.visitLocalVariableDeclaration( n, o)
            elif isinstance(n, IfThenStatement): self.visitIfThenStatement( n, o)
            elif isinstance(n, IfThenElseStatement): self.visitIfThenElseStatement( n, o)
            elif isinstance(n, IfThenElseStatementNoShortIf): self.visitIfThenElseStatementNoShortIf( n, o)
            elif isinstance(n, EmptyStatement): self.visitEmptyStatement( n, o)
            elif isinstance(n, LabeledStatement): self.visitLabeledStatement( n, o)
            elif isinstance(n, LabeledStatementNoShortIf): self.visitLabeledStatementNoShortIf( n, o)
            elif isinstance(n, ExpressionStatement): self.visitExpressionStatement( n, o)
            elif isinstance(n, SwitchStatement): self.visitSwitchStatement( n, o)
            elif isinstance(n, SwitchBlock): self.visitSwitchBlock( n, o)
            elif isinstance(n, SwitchBlockStatementGroups): self.visitSwitchBlockStatementGroups( n, o)
            elif isinstance(n, SwitchBlockStatementGroup): self.visitSwitchBlockStatementGroup( n, o)
            elif isinstance(n, SwitchLabels): self.visitSwitchLabels( n, o)
            elif isinstance(n, WhileStatement): self.visitWhileStatement( n, o)
            elif isinstance(n, WhileStatementNoShortIf): self.visitWhileStatementNoShortIf( n, o)
            elif isinstance(n, DoStatement): self.visitDoStatement( n, o)
            elif isinstance(n, BasicForStatement): self.visitBasicForStatement( n, o)
            elif isinstance(n, ForStatementNoShortIf): self.visitForStatementNoShortIf( n, o)
            elif isinstance(n, StatementExpressionList): self.visitStatementExpressionList( n, o)
            elif isinstance(n, EnhancedForStatement): self.visitEnhancedForStatement( n, o)
            elif isinstance(n, BreakStatement): self.visitBreakStatement( n, o)
            elif isinstance(n, ContinueStatement): self.visitContinueStatement( n, o)
            elif isinstance(n, ReturnStatement): self.visitReturnStatement( n, o)
            elif isinstance(n, ThrowStatement): self.visitThrowStatement( n, o)
            elif isinstance(n, SynchronizedStatement): self.visitSynchronizedStatement( n, o)
            elif isinstance(n, Catches): self.visitCatches( n, o)
            elif isinstance(n, CatchClause): self.visitCatchClause( n, o)
            elif isinstance(n, Finally): self.visitFinally( n, o)
            elif isinstance(n, ArgumentList): self.visitArgumentList( n, o)
            elif isinstance(n, DimExprs): self.visitDimExprs( n, o)
            elif isinstance(n, DimExpr): self.visitDimExpr( n, o)
            elif isinstance(n, PostIncrementExpression): self.visitPostIncrementExpression( n, o)
            elif isinstance(n, PostDecrementExpression): self.visitPostDecrementExpression( n, o)
            elif isinstance(n, PreIncrementExpression): self.visitPreIncrementExpression( n, o)
            elif isinstance(n, PreDecrementExpression): self.visitPreDecrementExpression( n, o)
            elif isinstance(n, AndExpression): self.visitAndExpression( n, o)
            elif isinstance(n, ExclusiveOrExpression): self.visitExclusiveOrExpression( n, o)
            elif isinstance(n, InclusiveOrExpression): self.visitInclusiveOrExpression( n, o)
            elif isinstance(n, ConditionalAndExpression): self.visitConditionalAndExpression( n, o)
            elif isinstance(n, ConditionalOrExpression): self.visitConditionalOrExpression( n, o)
            elif isinstance(n, ConditionalExpression): self.visitConditionalExpression( n, o)
            elif isinstance(n, Assignment): self.visitAssignment( n, o)
            elif isinstance(n, Commaopt): self.visitCommaopt( n, o)
            elif isinstance(n, Ellipsisopt): self.visitEllipsisopt( n, o)
            elif isinstance(n, LPGUserAction0): self.visitLPGUserAction0( n, o)
            elif isinstance(n, LPGUserAction1): self.visitLPGUserAction1( n, o)
            elif isinstance(n, LPGUserAction2): self.visitLPGUserAction2( n, o)
            elif isinstance(n, LPGUserAction3): self.visitLPGUserAction3( n, o)
            elif isinstance(n, LPGUserAction4): self.visitLPGUserAction4( n, o)
            elif isinstance(n, IntegralType0): self.visitIntegralType0( n, o)
            elif isinstance(n, IntegralType1): self.visitIntegralType1( n, o)
            elif isinstance(n, IntegralType2): self.visitIntegralType2( n, o)
            elif isinstance(n, IntegralType3): self.visitIntegralType3( n, o)
            elif isinstance(n, IntegralType4): self.visitIntegralType4( n, o)
            elif isinstance(n, FloatingPointType0): self.visitFloatingPointType0( n, o)
            elif isinstance(n, FloatingPointType1): self.visitFloatingPointType1( n, o)
            elif isinstance(n, WildcardBounds0): self.visitWildcardBounds0( n, o)
            elif isinstance(n, WildcardBounds1): self.visitWildcardBounds1( n, o)
            elif isinstance(n, ClassModifier0): self.visitClassModifier0( n, o)
            elif isinstance(n, ClassModifier1): self.visitClassModifier1( n, o)
            elif isinstance(n, ClassModifier2): self.visitClassModifier2( n, o)
            elif isinstance(n, ClassModifier3): self.visitClassModifier3( n, o)
            elif isinstance(n, ClassModifier4): self.visitClassModifier4( n, o)
            elif isinstance(n, ClassModifier5): self.visitClassModifier5( n, o)
            elif isinstance(n, ClassModifier6): self.visitClassModifier6( n, o)
            elif isinstance(n, FieldModifier0): self.visitFieldModifier0( n, o)
            elif isinstance(n, FieldModifier1): self.visitFieldModifier1( n, o)
            elif isinstance(n, FieldModifier2): self.visitFieldModifier2( n, o)
            elif isinstance(n, FieldModifier3): self.visitFieldModifier3( n, o)
            elif isinstance(n, FieldModifier4): self.visitFieldModifier4( n, o)
            elif isinstance(n, FieldModifier5): self.visitFieldModifier5( n, o)
            elif isinstance(n, FieldModifier6): self.visitFieldModifier6( n, o)
            elif isinstance(n, MethodDeclarator0): self.visitMethodDeclarator0( n, o)
            elif isinstance(n, MethodDeclarator1): self.visitMethodDeclarator1( n, o)
            elif isinstance(n, MethodModifier0): self.visitMethodModifier0( n, o)
            elif isinstance(n, MethodModifier1): self.visitMethodModifier1( n, o)
            elif isinstance(n, MethodModifier2): self.visitMethodModifier2( n, o)
            elif isinstance(n, MethodModifier3): self.visitMethodModifier3( n, o)
            elif isinstance(n, MethodModifier4): self.visitMethodModifier4( n, o)
            elif isinstance(n, MethodModifier5): self.visitMethodModifier5( n, o)
            elif isinstance(n, MethodModifier6): self.visitMethodModifier6( n, o)
            elif isinstance(n, MethodModifier7): self.visitMethodModifier7( n, o)
            elif isinstance(n, MethodModifier8): self.visitMethodModifier8( n, o)
            elif isinstance(n, ConstructorModifier0): self.visitConstructorModifier0( n, o)
            elif isinstance(n, ConstructorModifier1): self.visitConstructorModifier1( n, o)
            elif isinstance(n, ConstructorModifier2): self.visitConstructorModifier2( n, o)
            elif isinstance(n, ExplicitConstructorInvocation0): self.visitExplicitConstructorInvocation0( n, o)
            elif isinstance(n, ExplicitConstructorInvocation1): self.visitExplicitConstructorInvocation1( n, o)
            elif isinstance(n, ExplicitConstructorInvocation2): self.visitExplicitConstructorInvocation2( n, o)
            elif isinstance(n, InterfaceModifier0): self.visitInterfaceModifier0( n, o)
            elif isinstance(n, InterfaceModifier1): self.visitInterfaceModifier1( n, o)
            elif isinstance(n, InterfaceModifier2): self.visitInterfaceModifier2( n, o)
            elif isinstance(n, InterfaceModifier3): self.visitInterfaceModifier3( n, o)
            elif isinstance(n, InterfaceModifier4): self.visitInterfaceModifier4( n, o)
            elif isinstance(n, InterfaceModifier5): self.visitInterfaceModifier5( n, o)
            elif isinstance(n, ExtendsInterfaces0): self.visitExtendsInterfaces0( n, o)
            elif isinstance(n, ExtendsInterfaces1): self.visitExtendsInterfaces1( n, o)
            elif isinstance(n, ConstantModifier0): self.visitConstantModifier0( n, o)
            elif isinstance(n, ConstantModifier1): self.visitConstantModifier1( n, o)
            elif isinstance(n, ConstantModifier2): self.visitConstantModifier2( n, o)
            elif isinstance(n, AbstractMethodModifier0): self.visitAbstractMethodModifier0( n, o)
            elif isinstance(n, AbstractMethodModifier1): self.visitAbstractMethodModifier1( n, o)
            elif isinstance(n, AnnotationTypeElementDeclaration0): self.visitAnnotationTypeElementDeclaration0( n, o)
            elif isinstance(n, AnnotationTypeElementDeclaration1): self.visitAnnotationTypeElementDeclaration1( n, o)
            elif isinstance(n, AssertStatement0): self.visitAssertStatement0( n, o)
            elif isinstance(n, AssertStatement1): self.visitAssertStatement1( n, o)
            elif isinstance(n, SwitchLabel0): self.visitSwitchLabel0( n, o)
            elif isinstance(n, SwitchLabel1): self.visitSwitchLabel1( n, o)
            elif isinstance(n, SwitchLabel2): self.visitSwitchLabel2( n, o)
            elif isinstance(n, TryStatement0): self.visitTryStatement0( n, o)
            elif isinstance(n, TryStatement1): self.visitTryStatement1( n, o)
            elif isinstance(n, PrimaryNoNewArray0): self.visitPrimaryNoNewArray0( n, o)
            elif isinstance(n, PrimaryNoNewArray1): self.visitPrimaryNoNewArray1( n, o)
            elif isinstance(n, PrimaryNoNewArray2): self.visitPrimaryNoNewArray2( n, o)
            elif isinstance(n, PrimaryNoNewArray3): self.visitPrimaryNoNewArray3( n, o)
            elif isinstance(n, PrimaryNoNewArray4): self.visitPrimaryNoNewArray4( n, o)
            elif isinstance(n, Literal0): self.visitLiteral0( n, o)
            elif isinstance(n, Literal1): self.visitLiteral1( n, o)
            elif isinstance(n, Literal2): self.visitLiteral2( n, o)
            elif isinstance(n, Literal3): self.visitLiteral3( n, o)
            elif isinstance(n, Literal4): self.visitLiteral4( n, o)
            elif isinstance(n, Literal5): self.visitLiteral5( n, o)
            elif isinstance(n, Literal6): self.visitLiteral6( n, o)
            elif isinstance(n, BooleanLiteral0): self.visitBooleanLiteral0( n, o)
            elif isinstance(n, BooleanLiteral1): self.visitBooleanLiteral1( n, o)
            elif isinstance(n, ClassInstanceCreationExpression0): self.visitClassInstanceCreationExpression0( n, o)
            elif isinstance(n, ClassInstanceCreationExpression1): self.visitClassInstanceCreationExpression1( n, o)
            elif isinstance(n, ArrayCreationExpression0): self.visitArrayCreationExpression0( n, o)
            elif isinstance(n, ArrayCreationExpression1): self.visitArrayCreationExpression1( n, o)
            elif isinstance(n, ArrayCreationExpression2): self.visitArrayCreationExpression2( n, o)
            elif isinstance(n, ArrayCreationExpression3): self.visitArrayCreationExpression3( n, o)
            elif isinstance(n, Dims0): self.visitDims0( n, o)
            elif isinstance(n, Dims1): self.visitDims1( n, o)
            elif isinstance(n, FieldAccess0): self.visitFieldAccess0( n, o)
            elif isinstance(n, FieldAccess1): self.visitFieldAccess1( n, o)
            elif isinstance(n, FieldAccess2): self.visitFieldAccess2( n, o)
            elif isinstance(n, MethodInvocation0): self.visitMethodInvocation0( n, o)
            elif isinstance(n, MethodInvocation1): self.visitMethodInvocation1( n, o)
            elif isinstance(n, MethodInvocation2): self.visitMethodInvocation2( n, o)
            elif isinstance(n, MethodInvocation3): self.visitMethodInvocation3( n, o)
            elif isinstance(n, MethodInvocation4): self.visitMethodInvocation4( n, o)
            elif isinstance(n, ArrayAccess0): self.visitArrayAccess0( n, o)
            elif isinstance(n, ArrayAccess1): self.visitArrayAccess1( n, o)
            elif isinstance(n, UnaryExpression0): self.visitUnaryExpression0( n, o)
            elif isinstance(n, UnaryExpression1): self.visitUnaryExpression1( n, o)
            elif isinstance(n, UnaryExpressionNotPlusMinus0): self.visitUnaryExpressionNotPlusMinus0( n, o)
            elif isinstance(n, UnaryExpressionNotPlusMinus1): self.visitUnaryExpressionNotPlusMinus1( n, o)
            elif isinstance(n, CastExpression0): self.visitCastExpression0( n, o)
            elif isinstance(n, CastExpression1): self.visitCastExpression1( n, o)
            elif isinstance(n, MultiplicativeExpression0): self.visitMultiplicativeExpression0( n, o)
            elif isinstance(n, MultiplicativeExpression1): self.visitMultiplicativeExpression1( n, o)
            elif isinstance(n, MultiplicativeExpression2): self.visitMultiplicativeExpression2( n, o)
            elif isinstance(n, AdditiveExpression0): self.visitAdditiveExpression0( n, o)
            elif isinstance(n, AdditiveExpression1): self.visitAdditiveExpression1( n, o)
            elif isinstance(n, ShiftExpression0): self.visitShiftExpression0( n, o)
            elif isinstance(n, ShiftExpression1): self.visitShiftExpression1( n, o)
            elif isinstance(n, ShiftExpression2): self.visitShiftExpression2( n, o)
            elif isinstance(n, RelationalExpression0): self.visitRelationalExpression0( n, o)
            elif isinstance(n, RelationalExpression1): self.visitRelationalExpression1( n, o)
            elif isinstance(n, RelationalExpression2): self.visitRelationalExpression2( n, o)
            elif isinstance(n, RelationalExpression3): self.visitRelationalExpression3( n, o)
            elif isinstance(n, RelationalExpression4): self.visitRelationalExpression4( n, o)
            elif isinstance(n, EqualityExpression0): self.visitEqualityExpression0( n, o)
            elif isinstance(n, EqualityExpression1): self.visitEqualityExpression1( n, o)
            elif isinstance(n, AssignmentOperator0): self.visitAssignmentOperator0( n, o)
            elif isinstance(n, AssignmentOperator1): self.visitAssignmentOperator1( n, o)
            elif isinstance(n, AssignmentOperator2): self.visitAssignmentOperator2( n, o)
            elif isinstance(n, AssignmentOperator3): self.visitAssignmentOperator3( n, o)
            elif isinstance(n, AssignmentOperator4): self.visitAssignmentOperator4( n, o)
            elif isinstance(n, AssignmentOperator5): self.visitAssignmentOperator5( n, o)
            elif isinstance(n, AssignmentOperator6): self.visitAssignmentOperator6( n, o)
            elif isinstance(n, AssignmentOperator7): self.visitAssignmentOperator7( n, o)
            elif isinstance(n, AssignmentOperator8): self.visitAssignmentOperator8( n, o)
            elif isinstance(n, AssignmentOperator9): self.visitAssignmentOperator9( n, o)
            elif isinstance(n, AssignmentOperator10): self.visitAssignmentOperator10( n, o)
            elif isinstance(n, AssignmentOperator11): self.visitAssignmentOperator11( n, o)
            else: raise ValueError("visit(" + n.toString() + ")")
        
    
class AbstractResultVisitor (ResultVisitor, ResultArgumentVisitor):
        __slots__ = ()
    
        def unimplementedVisitor(self,s ): raise TypeError('Can not instantiate abstract class  with abstract methods')

        def visitAstToken(self, n, o = None): return  self.unimplementedVisitor("visitAstToken(AstToken, any)")

        def visitidentifier(self, n, o = None): return  self.unimplementedVisitor("visitidentifier(identifier, any)")

        def visitPrimitiveType(self, n, o = None): return  self.unimplementedVisitor("visitPrimitiveType(PrimitiveType, any)")

        def visitClassType(self, n, o = None): return  self.unimplementedVisitor("visitClassType(ClassType, any)")

        def visitInterfaceType(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceType(InterfaceType, any)")

        def visitTypeName(self, n, o = None): return  self.unimplementedVisitor("visitTypeName(TypeName, any)")

        def visitArrayType(self, n, o = None): return  self.unimplementedVisitor("visitArrayType(ArrayType, any)")

        def visitTypeParameter(self, n, o = None): return  self.unimplementedVisitor("visitTypeParameter(TypeParameter, any)")

        def visitTypeBound(self, n, o = None): return  self.unimplementedVisitor("visitTypeBound(TypeBound, any)")

        def visitAdditionalBoundList(self, n, o = None): return  self.unimplementedVisitor("visitAdditionalBoundList(AdditionalBoundList, any)")

        def visitAdditionalBound(self, n, o = None): return  self.unimplementedVisitor("visitAdditionalBound(AdditionalBound, any)")

        def visitTypeArguments(self, n, o = None): return  self.unimplementedVisitor("visitTypeArguments(TypeArguments, any)")

        def visitActualTypeArgumentList(self, n, o = None): return  self.unimplementedVisitor("visitActualTypeArgumentList(ActualTypeArgumentList, any)")

        def visitWildcard(self, n, o = None): return  self.unimplementedVisitor("visitWildcard(Wildcard, any)")

        def visitPackageName(self, n, o = None): return  self.unimplementedVisitor("visitPackageName(PackageName, any)")

        def visitExpressionName(self, n, o = None): return  self.unimplementedVisitor("visitExpressionName(ExpressionName, any)")

        def visitMethodName(self, n, o = None): return  self.unimplementedVisitor("visitMethodName(MethodName, any)")

        def visitPackageOrTypeName(self, n, o = None): return  self.unimplementedVisitor("visitPackageOrTypeName(PackageOrTypeName, any)")

        def visitAmbiguousName(self, n, o = None): return  self.unimplementedVisitor("visitAmbiguousName(AmbiguousName, any)")

        def visitCompilationUnit(self, n, o = None): return  self.unimplementedVisitor("visitCompilationUnit(CompilationUnit, any)")

        def visitImportDeclarations(self, n, o = None): return  self.unimplementedVisitor("visitImportDeclarations(ImportDeclarations, any)")

        def visitTypeDeclarations(self, n, o = None): return  self.unimplementedVisitor("visitTypeDeclarations(TypeDeclarations, any)")

        def visitPackageDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitPackageDeclaration(PackageDeclaration, any)")

        def visitSingleTypeImportDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitSingleTypeImportDeclaration(SingleTypeImportDeclaration, any)")

        def visitTypeImportOnDemandDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitTypeImportOnDemandDeclaration(TypeImportOnDemandDeclaration, any)")

        def visitSingleStaticImportDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitSingleStaticImportDeclaration(SingleStaticImportDeclaration, any)")

        def visitStaticImportOnDemandDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitStaticImportOnDemandDeclaration(StaticImportOnDemandDeclaration, any)")

        def visitTypeDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitTypeDeclaration(TypeDeclaration, any)")

        def visitNormalClassDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitNormalClassDeclaration(NormalClassDeclaration, any)")

        def visitClassModifiers(self, n, o = None): return  self.unimplementedVisitor("visitClassModifiers(ClassModifiers, any)")

        def visitTypeParameters(self, n, o = None): return  self.unimplementedVisitor("visitTypeParameters(TypeParameters, any)")

        def visitTypeParameterList(self, n, o = None): return  self.unimplementedVisitor("visitTypeParameterList(TypeParameterList, any)")

        def visitSuper(self, n, o = None): return  self.unimplementedVisitor("visitSuper(Super, any)")

        def visitInterfaces(self, n, o = None): return  self.unimplementedVisitor("visitInterfaces(Interfaces, any)")

        def visitInterfaceTypeList(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceTypeList(InterfaceTypeList, any)")

        def visitClassBody(self, n, o = None): return  self.unimplementedVisitor("visitClassBody(ClassBody, any)")

        def visitClassBodyDeclarations(self, n, o = None): return  self.unimplementedVisitor("visitClassBodyDeclarations(ClassBodyDeclarations, any)")

        def visitClassMemberDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitClassMemberDeclaration(ClassMemberDeclaration, any)")

        def visitFieldDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitFieldDeclaration(FieldDeclaration, any)")

        def visitVariableDeclarators(self, n, o = None): return  self.unimplementedVisitor("visitVariableDeclarators(VariableDeclarators, any)")

        def visitVariableDeclarator(self, n, o = None): return  self.unimplementedVisitor("visitVariableDeclarator(VariableDeclarator, any)")

        def visitVariableDeclaratorId(self, n, o = None): return  self.unimplementedVisitor("visitVariableDeclaratorId(VariableDeclaratorId, any)")

        def visitFieldModifiers(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifiers(FieldModifiers, any)")

        def visitMethodDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitMethodDeclaration(MethodDeclaration, any)")

        def visitMethodHeader(self, n, o = None): return  self.unimplementedVisitor("visitMethodHeader(MethodHeader, any)")

        def visitResultType(self, n, o = None): return  self.unimplementedVisitor("visitResultType(ResultType, any)")

        def visitFormalParameterList(self, n, o = None): return  self.unimplementedVisitor("visitFormalParameterList(FormalParameterList, any)")

        def visitFormalParameters(self, n, o = None): return  self.unimplementedVisitor("visitFormalParameters(FormalParameters, any)")

        def visitFormalParameter(self, n, o = None): return  self.unimplementedVisitor("visitFormalParameter(FormalParameter, any)")

        def visitVariableModifiers(self, n, o = None): return  self.unimplementedVisitor("visitVariableModifiers(VariableModifiers, any)")

        def visitVariableModifier(self, n, o = None): return  self.unimplementedVisitor("visitVariableModifier(VariableModifier, any)")

        def visitLastFormalParameter(self, n, o = None): return  self.unimplementedVisitor("visitLastFormalParameter(LastFormalParameter, any)")

        def visitMethodModifiers(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifiers(MethodModifiers, any)")

        def visitThrows(self, n, o = None): return  self.unimplementedVisitor("visitThrows(Throws, any)")

        def visitExceptionTypeList(self, n, o = None): return  self.unimplementedVisitor("visitExceptionTypeList(ExceptionTypeList, any)")

        def visitMethodBody(self, n, o = None): return  self.unimplementedVisitor("visitMethodBody(MethodBody, any)")

        def visitStaticInitializer(self, n, o = None): return  self.unimplementedVisitor("visitStaticInitializer(StaticInitializer, any)")

        def visitConstructorDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitConstructorDeclaration(ConstructorDeclaration, any)")

        def visitConstructorDeclarator(self, n, o = None): return  self.unimplementedVisitor("visitConstructorDeclarator(ConstructorDeclarator, any)")

        def visitConstructorModifiers(self, n, o = None): return  self.unimplementedVisitor("visitConstructorModifiers(ConstructorModifiers, any)")

        def visitConstructorBody(self, n, o = None): return  self.unimplementedVisitor("visitConstructorBody(ConstructorBody, any)")

        def visitEnumDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitEnumDeclaration(EnumDeclaration, any)")

        def visitEnumBody(self, n, o = None): return  self.unimplementedVisitor("visitEnumBody(EnumBody, any)")

        def visitEnumConstants(self, n, o = None): return  self.unimplementedVisitor("visitEnumConstants(EnumConstants, any)")

        def visitEnumConstant(self, n, o = None): return  self.unimplementedVisitor("visitEnumConstant(EnumConstant, any)")

        def visitArguments(self, n, o = None): return  self.unimplementedVisitor("visitArguments(Arguments, any)")

        def visitEnumBodyDeclarations(self, n, o = None): return  self.unimplementedVisitor("visitEnumBodyDeclarations(EnumBodyDeclarations, any)")

        def visitNormalInterfaceDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitNormalInterfaceDeclaration(NormalInterfaceDeclaration, any)")

        def visitInterfaceModifiers(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifiers(InterfaceModifiers, any)")

        def visitInterfaceBody(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceBody(InterfaceBody, any)")

        def visitInterfaceMemberDeclarations(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceMemberDeclarations(InterfaceMemberDeclarations, any)")

        def visitInterfaceMemberDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceMemberDeclaration(InterfaceMemberDeclaration, any)")

        def visitConstantDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitConstantDeclaration(ConstantDeclaration, any)")

        def visitConstantModifiers(self, n, o = None): return  self.unimplementedVisitor("visitConstantModifiers(ConstantModifiers, any)")

        def visitAbstractMethodDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitAbstractMethodDeclaration(AbstractMethodDeclaration, any)")

        def visitAbstractMethodModifiers(self, n, o = None): return  self.unimplementedVisitor("visitAbstractMethodModifiers(AbstractMethodModifiers, any)")

        def visitAnnotationTypeDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitAnnotationTypeDeclaration(AnnotationTypeDeclaration, any)")

        def visitAnnotationTypeBody(self, n, o = None): return  self.unimplementedVisitor("visitAnnotationTypeBody(AnnotationTypeBody, any)")

        def visitAnnotationTypeElementDeclarations(self, n, o = None): return  self.unimplementedVisitor("visitAnnotationTypeElementDeclarations(AnnotationTypeElementDeclarations, any)")

        def visitDefaultValue(self, n, o = None): return  self.unimplementedVisitor("visitDefaultValue(DefaultValue, any)")

        def visitAnnotations(self, n, o = None): return  self.unimplementedVisitor("visitAnnotations(Annotations, any)")

        def visitNormalAnnotation(self, n, o = None): return  self.unimplementedVisitor("visitNormalAnnotation(NormalAnnotation, any)")

        def visitElementValuePairs(self, n, o = None): return  self.unimplementedVisitor("visitElementValuePairs(ElementValuePairs, any)")

        def visitElementValuePair(self, n, o = None): return  self.unimplementedVisitor("visitElementValuePair(ElementValuePair, any)")

        def visitElementValueArrayInitializer(self, n, o = None): return  self.unimplementedVisitor("visitElementValueArrayInitializer(ElementValueArrayInitializer, any)")

        def visitElementValues(self, n, o = None): return  self.unimplementedVisitor("visitElementValues(ElementValues, any)")

        def visitMarkerAnnotation(self, n, o = None): return  self.unimplementedVisitor("visitMarkerAnnotation(MarkerAnnotation, any)")

        def visitSingleElementAnnotation(self, n, o = None): return  self.unimplementedVisitor("visitSingleElementAnnotation(SingleElementAnnotation, any)")

        def visitArrayInitializer(self, n, o = None): return  self.unimplementedVisitor("visitArrayInitializer(ArrayInitializer, any)")

        def visitVariableInitializers(self, n, o = None): return  self.unimplementedVisitor("visitVariableInitializers(VariableInitializers, any)")

        def visitBlock(self, n, o = None): return  self.unimplementedVisitor("visitBlock(Block, any)")

        def visitBlockStatements(self, n, o = None): return  self.unimplementedVisitor("visitBlockStatements(BlockStatements, any)")

        def visitLocalVariableDeclarationStatement(self, n, o = None): return  self.unimplementedVisitor("visitLocalVariableDeclarationStatement(LocalVariableDeclarationStatement, any)")

        def visitLocalVariableDeclaration(self, n, o = None): return  self.unimplementedVisitor("visitLocalVariableDeclaration(LocalVariableDeclaration, any)")

        def visitIfThenStatement(self, n, o = None): return  self.unimplementedVisitor("visitIfThenStatement(IfThenStatement, any)")

        def visitIfThenElseStatement(self, n, o = None): return  self.unimplementedVisitor("visitIfThenElseStatement(IfThenElseStatement, any)")

        def visitIfThenElseStatementNoShortIf(self, n, o = None): return  self.unimplementedVisitor("visitIfThenElseStatementNoShortIf(IfThenElseStatementNoShortIf, any)")

        def visitEmptyStatement(self, n, o = None): return  self.unimplementedVisitor("visitEmptyStatement(EmptyStatement, any)")

        def visitLabeledStatement(self, n, o = None): return  self.unimplementedVisitor("visitLabeledStatement(LabeledStatement, any)")

        def visitLabeledStatementNoShortIf(self, n, o = None): return  self.unimplementedVisitor("visitLabeledStatementNoShortIf(LabeledStatementNoShortIf, any)")

        def visitExpressionStatement(self, n, o = None): return  self.unimplementedVisitor("visitExpressionStatement(ExpressionStatement, any)")

        def visitSwitchStatement(self, n, o = None): return  self.unimplementedVisitor("visitSwitchStatement(SwitchStatement, any)")

        def visitSwitchBlock(self, n, o = None): return  self.unimplementedVisitor("visitSwitchBlock(SwitchBlock, any)")

        def visitSwitchBlockStatementGroups(self, n, o = None): return  self.unimplementedVisitor("visitSwitchBlockStatementGroups(SwitchBlockStatementGroups, any)")

        def visitSwitchBlockStatementGroup(self, n, o = None): return  self.unimplementedVisitor("visitSwitchBlockStatementGroup(SwitchBlockStatementGroup, any)")

        def visitSwitchLabels(self, n, o = None): return  self.unimplementedVisitor("visitSwitchLabels(SwitchLabels, any)")

        def visitWhileStatement(self, n, o = None): return  self.unimplementedVisitor("visitWhileStatement(WhileStatement, any)")

        def visitWhileStatementNoShortIf(self, n, o = None): return  self.unimplementedVisitor("visitWhileStatementNoShortIf(WhileStatementNoShortIf, any)")

        def visitDoStatement(self, n, o = None): return  self.unimplementedVisitor("visitDoStatement(DoStatement, any)")

        def visitBasicForStatement(self, n, o = None): return  self.unimplementedVisitor("visitBasicForStatement(BasicForStatement, any)")

        def visitForStatementNoShortIf(self, n, o = None): return  self.unimplementedVisitor("visitForStatementNoShortIf(ForStatementNoShortIf, any)")

        def visitStatementExpressionList(self, n, o = None): return  self.unimplementedVisitor("visitStatementExpressionList(StatementExpressionList, any)")

        def visitEnhancedForStatement(self, n, o = None): return  self.unimplementedVisitor("visitEnhancedForStatement(EnhancedForStatement, any)")

        def visitBreakStatement(self, n, o = None): return  self.unimplementedVisitor("visitBreakStatement(BreakStatement, any)")

        def visitContinueStatement(self, n, o = None): return  self.unimplementedVisitor("visitContinueStatement(ContinueStatement, any)")

        def visitReturnStatement(self, n, o = None): return  self.unimplementedVisitor("visitReturnStatement(ReturnStatement, any)")

        def visitThrowStatement(self, n, o = None): return  self.unimplementedVisitor("visitThrowStatement(ThrowStatement, any)")

        def visitSynchronizedStatement(self, n, o = None): return  self.unimplementedVisitor("visitSynchronizedStatement(SynchronizedStatement, any)")

        def visitCatches(self, n, o = None): return  self.unimplementedVisitor("visitCatches(Catches, any)")

        def visitCatchClause(self, n, o = None): return  self.unimplementedVisitor("visitCatchClause(CatchClause, any)")

        def visitFinally(self, n, o = None): return  self.unimplementedVisitor("visitFinally(Finally, any)")

        def visitArgumentList(self, n, o = None): return  self.unimplementedVisitor("visitArgumentList(ArgumentList, any)")

        def visitDimExprs(self, n, o = None): return  self.unimplementedVisitor("visitDimExprs(DimExprs, any)")

        def visitDimExpr(self, n, o = None): return  self.unimplementedVisitor("visitDimExpr(DimExpr, any)")

        def visitPostIncrementExpression(self, n, o = None): return  self.unimplementedVisitor("visitPostIncrementExpression(PostIncrementExpression, any)")

        def visitPostDecrementExpression(self, n, o = None): return  self.unimplementedVisitor("visitPostDecrementExpression(PostDecrementExpression, any)")

        def visitPreIncrementExpression(self, n, o = None): return  self.unimplementedVisitor("visitPreIncrementExpression(PreIncrementExpression, any)")

        def visitPreDecrementExpression(self, n, o = None): return  self.unimplementedVisitor("visitPreDecrementExpression(PreDecrementExpression, any)")

        def visitAndExpression(self, n, o = None): return  self.unimplementedVisitor("visitAndExpression(AndExpression, any)")

        def visitExclusiveOrExpression(self, n, o = None): return  self.unimplementedVisitor("visitExclusiveOrExpression(ExclusiveOrExpression, any)")

        def visitInclusiveOrExpression(self, n, o = None): return  self.unimplementedVisitor("visitInclusiveOrExpression(InclusiveOrExpression, any)")

        def visitConditionalAndExpression(self, n, o = None): return  self.unimplementedVisitor("visitConditionalAndExpression(ConditionalAndExpression, any)")

        def visitConditionalOrExpression(self, n, o = None): return  self.unimplementedVisitor("visitConditionalOrExpression(ConditionalOrExpression, any)")

        def visitConditionalExpression(self, n, o = None): return  self.unimplementedVisitor("visitConditionalExpression(ConditionalExpression, any)")

        def visitAssignment(self, n, o = None): return  self.unimplementedVisitor("visitAssignment(Assignment, any)")

        def visitCommaopt(self, n, o = None): return  self.unimplementedVisitor("visitCommaopt(Commaopt, any)")

        def visitEllipsisopt(self, n, o = None): return  self.unimplementedVisitor("visitEllipsisopt(Ellipsisopt, any)")

        def visitLPGUserAction0(self, n, o = None): return  self.unimplementedVisitor("visitLPGUserAction0(LPGUserAction0, any)")

        def visitLPGUserAction1(self, n, o = None): return  self.unimplementedVisitor("visitLPGUserAction1(LPGUserAction1, any)")

        def visitLPGUserAction2(self, n, o = None): return  self.unimplementedVisitor("visitLPGUserAction2(LPGUserAction2, any)")

        def visitLPGUserAction3(self, n, o = None): return  self.unimplementedVisitor("visitLPGUserAction3(LPGUserAction3, any)")

        def visitLPGUserAction4(self, n, o = None): return  self.unimplementedVisitor("visitLPGUserAction4(LPGUserAction4, any)")

        def visitIntegralType0(self, n, o = None): return  self.unimplementedVisitor("visitIntegralType0(IntegralType0, any)")

        def visitIntegralType1(self, n, o = None): return  self.unimplementedVisitor("visitIntegralType1(IntegralType1, any)")

        def visitIntegralType2(self, n, o = None): return  self.unimplementedVisitor("visitIntegralType2(IntegralType2, any)")

        def visitIntegralType3(self, n, o = None): return  self.unimplementedVisitor("visitIntegralType3(IntegralType3, any)")

        def visitIntegralType4(self, n, o = None): return  self.unimplementedVisitor("visitIntegralType4(IntegralType4, any)")

        def visitFloatingPointType0(self, n, o = None): return  self.unimplementedVisitor("visitFloatingPointType0(FloatingPointType0, any)")

        def visitFloatingPointType1(self, n, o = None): return  self.unimplementedVisitor("visitFloatingPointType1(FloatingPointType1, any)")

        def visitWildcardBounds0(self, n, o = None): return  self.unimplementedVisitor("visitWildcardBounds0(WildcardBounds0, any)")

        def visitWildcardBounds1(self, n, o = None): return  self.unimplementedVisitor("visitWildcardBounds1(WildcardBounds1, any)")

        def visitClassModifier0(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier0(ClassModifier0, any)")

        def visitClassModifier1(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier1(ClassModifier1, any)")

        def visitClassModifier2(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier2(ClassModifier2, any)")

        def visitClassModifier3(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier3(ClassModifier3, any)")

        def visitClassModifier4(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier4(ClassModifier4, any)")

        def visitClassModifier5(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier5(ClassModifier5, any)")

        def visitClassModifier6(self, n, o = None): return  self.unimplementedVisitor("visitClassModifier6(ClassModifier6, any)")

        def visitFieldModifier0(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier0(FieldModifier0, any)")

        def visitFieldModifier1(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier1(FieldModifier1, any)")

        def visitFieldModifier2(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier2(FieldModifier2, any)")

        def visitFieldModifier3(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier3(FieldModifier3, any)")

        def visitFieldModifier4(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier4(FieldModifier4, any)")

        def visitFieldModifier5(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier5(FieldModifier5, any)")

        def visitFieldModifier6(self, n, o = None): return  self.unimplementedVisitor("visitFieldModifier6(FieldModifier6, any)")

        def visitMethodDeclarator0(self, n, o = None): return  self.unimplementedVisitor("visitMethodDeclarator0(MethodDeclarator0, any)")

        def visitMethodDeclarator1(self, n, o = None): return  self.unimplementedVisitor("visitMethodDeclarator1(MethodDeclarator1, any)")

        def visitMethodModifier0(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier0(MethodModifier0, any)")

        def visitMethodModifier1(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier1(MethodModifier1, any)")

        def visitMethodModifier2(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier2(MethodModifier2, any)")

        def visitMethodModifier3(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier3(MethodModifier3, any)")

        def visitMethodModifier4(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier4(MethodModifier4, any)")

        def visitMethodModifier5(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier5(MethodModifier5, any)")

        def visitMethodModifier6(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier6(MethodModifier6, any)")

        def visitMethodModifier7(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier7(MethodModifier7, any)")

        def visitMethodModifier8(self, n, o = None): return  self.unimplementedVisitor("visitMethodModifier8(MethodModifier8, any)")

        def visitConstructorModifier0(self, n, o = None): return  self.unimplementedVisitor("visitConstructorModifier0(ConstructorModifier0, any)")

        def visitConstructorModifier1(self, n, o = None): return  self.unimplementedVisitor("visitConstructorModifier1(ConstructorModifier1, any)")

        def visitConstructorModifier2(self, n, o = None): return  self.unimplementedVisitor("visitConstructorModifier2(ConstructorModifier2, any)")

        def visitExplicitConstructorInvocation0(self, n, o = None): return  self.unimplementedVisitor("visitExplicitConstructorInvocation0(ExplicitConstructorInvocation0, any)")

        def visitExplicitConstructorInvocation1(self, n, o = None): return  self.unimplementedVisitor("visitExplicitConstructorInvocation1(ExplicitConstructorInvocation1, any)")

        def visitExplicitConstructorInvocation2(self, n, o = None): return  self.unimplementedVisitor("visitExplicitConstructorInvocation2(ExplicitConstructorInvocation2, any)")

        def visitInterfaceModifier0(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifier0(InterfaceModifier0, any)")

        def visitInterfaceModifier1(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifier1(InterfaceModifier1, any)")

        def visitInterfaceModifier2(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifier2(InterfaceModifier2, any)")

        def visitInterfaceModifier3(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifier3(InterfaceModifier3, any)")

        def visitInterfaceModifier4(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifier4(InterfaceModifier4, any)")

        def visitInterfaceModifier5(self, n, o = None): return  self.unimplementedVisitor("visitInterfaceModifier5(InterfaceModifier5, any)")

        def visitExtendsInterfaces0(self, n, o = None): return  self.unimplementedVisitor("visitExtendsInterfaces0(ExtendsInterfaces0, any)")

        def visitExtendsInterfaces1(self, n, o = None): return  self.unimplementedVisitor("visitExtendsInterfaces1(ExtendsInterfaces1, any)")

        def visitConstantModifier0(self, n, o = None): return  self.unimplementedVisitor("visitConstantModifier0(ConstantModifier0, any)")

        def visitConstantModifier1(self, n, o = None): return  self.unimplementedVisitor("visitConstantModifier1(ConstantModifier1, any)")

        def visitConstantModifier2(self, n, o = None): return  self.unimplementedVisitor("visitConstantModifier2(ConstantModifier2, any)")

        def visitAbstractMethodModifier0(self, n, o = None): return  self.unimplementedVisitor("visitAbstractMethodModifier0(AbstractMethodModifier0, any)")

        def visitAbstractMethodModifier1(self, n, o = None): return  self.unimplementedVisitor("visitAbstractMethodModifier1(AbstractMethodModifier1, any)")

        def visitAnnotationTypeElementDeclaration0(self, n, o = None): return  self.unimplementedVisitor("visitAnnotationTypeElementDeclaration0(AnnotationTypeElementDeclaration0, any)")

        def visitAnnotationTypeElementDeclaration1(self, n, o = None): return  self.unimplementedVisitor("visitAnnotationTypeElementDeclaration1(AnnotationTypeElementDeclaration1, any)")

        def visitAssertStatement0(self, n, o = None): return  self.unimplementedVisitor("visitAssertStatement0(AssertStatement0, any)")

        def visitAssertStatement1(self, n, o = None): return  self.unimplementedVisitor("visitAssertStatement1(AssertStatement1, any)")

        def visitSwitchLabel0(self, n, o = None): return  self.unimplementedVisitor("visitSwitchLabel0(SwitchLabel0, any)")

        def visitSwitchLabel1(self, n, o = None): return  self.unimplementedVisitor("visitSwitchLabel1(SwitchLabel1, any)")

        def visitSwitchLabel2(self, n, o = None): return  self.unimplementedVisitor("visitSwitchLabel2(SwitchLabel2, any)")

        def visitTryStatement0(self, n, o = None): return  self.unimplementedVisitor("visitTryStatement0(TryStatement0, any)")

        def visitTryStatement1(self, n, o = None): return  self.unimplementedVisitor("visitTryStatement1(TryStatement1, any)")

        def visitPrimaryNoNewArray0(self, n, o = None): return  self.unimplementedVisitor("visitPrimaryNoNewArray0(PrimaryNoNewArray0, any)")

        def visitPrimaryNoNewArray1(self, n, o = None): return  self.unimplementedVisitor("visitPrimaryNoNewArray1(PrimaryNoNewArray1, any)")

        def visitPrimaryNoNewArray2(self, n, o = None): return  self.unimplementedVisitor("visitPrimaryNoNewArray2(PrimaryNoNewArray2, any)")

        def visitPrimaryNoNewArray3(self, n, o = None): return  self.unimplementedVisitor("visitPrimaryNoNewArray3(PrimaryNoNewArray3, any)")

        def visitPrimaryNoNewArray4(self, n, o = None): return  self.unimplementedVisitor("visitPrimaryNoNewArray4(PrimaryNoNewArray4, any)")

        def visitLiteral0(self, n, o = None): return  self.unimplementedVisitor("visitLiteral0(Literal0, any)")

        def visitLiteral1(self, n, o = None): return  self.unimplementedVisitor("visitLiteral1(Literal1, any)")

        def visitLiteral2(self, n, o = None): return  self.unimplementedVisitor("visitLiteral2(Literal2, any)")

        def visitLiteral3(self, n, o = None): return  self.unimplementedVisitor("visitLiteral3(Literal3, any)")

        def visitLiteral4(self, n, o = None): return  self.unimplementedVisitor("visitLiteral4(Literal4, any)")

        def visitLiteral5(self, n, o = None): return  self.unimplementedVisitor("visitLiteral5(Literal5, any)")

        def visitLiteral6(self, n, o = None): return  self.unimplementedVisitor("visitLiteral6(Literal6, any)")

        def visitBooleanLiteral0(self, n, o = None): return  self.unimplementedVisitor("visitBooleanLiteral0(BooleanLiteral0, any)")

        def visitBooleanLiteral1(self, n, o = None): return  self.unimplementedVisitor("visitBooleanLiteral1(BooleanLiteral1, any)")

        def visitClassInstanceCreationExpression0(self, n, o = None): return  self.unimplementedVisitor("visitClassInstanceCreationExpression0(ClassInstanceCreationExpression0, any)")

        def visitClassInstanceCreationExpression1(self, n, o = None): return  self.unimplementedVisitor("visitClassInstanceCreationExpression1(ClassInstanceCreationExpression1, any)")

        def visitArrayCreationExpression0(self, n, o = None): return  self.unimplementedVisitor("visitArrayCreationExpression0(ArrayCreationExpression0, any)")

        def visitArrayCreationExpression1(self, n, o = None): return  self.unimplementedVisitor("visitArrayCreationExpression1(ArrayCreationExpression1, any)")

        def visitArrayCreationExpression2(self, n, o = None): return  self.unimplementedVisitor("visitArrayCreationExpression2(ArrayCreationExpression2, any)")

        def visitArrayCreationExpression3(self, n, o = None): return  self.unimplementedVisitor("visitArrayCreationExpression3(ArrayCreationExpression3, any)")

        def visitDims0(self, n, o = None): return  self.unimplementedVisitor("visitDims0(Dims0, any)")

        def visitDims1(self, n, o = None): return  self.unimplementedVisitor("visitDims1(Dims1, any)")

        def visitFieldAccess0(self, n, o = None): return  self.unimplementedVisitor("visitFieldAccess0(FieldAccess0, any)")

        def visitFieldAccess1(self, n, o = None): return  self.unimplementedVisitor("visitFieldAccess1(FieldAccess1, any)")

        def visitFieldAccess2(self, n, o = None): return  self.unimplementedVisitor("visitFieldAccess2(FieldAccess2, any)")

        def visitMethodInvocation0(self, n, o = None): return  self.unimplementedVisitor("visitMethodInvocation0(MethodInvocation0, any)")

        def visitMethodInvocation1(self, n, o = None): return  self.unimplementedVisitor("visitMethodInvocation1(MethodInvocation1, any)")

        def visitMethodInvocation2(self, n, o = None): return  self.unimplementedVisitor("visitMethodInvocation2(MethodInvocation2, any)")

        def visitMethodInvocation3(self, n, o = None): return  self.unimplementedVisitor("visitMethodInvocation3(MethodInvocation3, any)")

        def visitMethodInvocation4(self, n, o = None): return  self.unimplementedVisitor("visitMethodInvocation4(MethodInvocation4, any)")

        def visitArrayAccess0(self, n, o = None): return  self.unimplementedVisitor("visitArrayAccess0(ArrayAccess0, any)")

        def visitArrayAccess1(self, n, o = None): return  self.unimplementedVisitor("visitArrayAccess1(ArrayAccess1, any)")

        def visitUnaryExpression0(self, n, o = None): return  self.unimplementedVisitor("visitUnaryExpression0(UnaryExpression0, any)")

        def visitUnaryExpression1(self, n, o = None): return  self.unimplementedVisitor("visitUnaryExpression1(UnaryExpression1, any)")

        def visitUnaryExpressionNotPlusMinus0(self, n, o = None): return  self.unimplementedVisitor("visitUnaryExpressionNotPlusMinus0(UnaryExpressionNotPlusMinus0, any)")

        def visitUnaryExpressionNotPlusMinus1(self, n, o = None): return  self.unimplementedVisitor("visitUnaryExpressionNotPlusMinus1(UnaryExpressionNotPlusMinus1, any)")

        def visitCastExpression0(self, n, o = None): return  self.unimplementedVisitor("visitCastExpression0(CastExpression0, any)")

        def visitCastExpression1(self, n, o = None): return  self.unimplementedVisitor("visitCastExpression1(CastExpression1, any)")

        def visitMultiplicativeExpression0(self, n, o = None): return  self.unimplementedVisitor("visitMultiplicativeExpression0(MultiplicativeExpression0, any)")

        def visitMultiplicativeExpression1(self, n, o = None): return  self.unimplementedVisitor("visitMultiplicativeExpression1(MultiplicativeExpression1, any)")

        def visitMultiplicativeExpression2(self, n, o = None): return  self.unimplementedVisitor("visitMultiplicativeExpression2(MultiplicativeExpression2, any)")

        def visitAdditiveExpression0(self, n, o = None): return  self.unimplementedVisitor("visitAdditiveExpression0(AdditiveExpression0, any)")

        def visitAdditiveExpression1(self, n, o = None): return  self.unimplementedVisitor("visitAdditiveExpression1(AdditiveExpression1, any)")

        def visitShiftExpression0(self, n, o = None): return  self.unimplementedVisitor("visitShiftExpression0(ShiftExpression0, any)")

        def visitShiftExpression1(self, n, o = None): return  self.unimplementedVisitor("visitShiftExpression1(ShiftExpression1, any)")

        def visitShiftExpression2(self, n, o = None): return  self.unimplementedVisitor("visitShiftExpression2(ShiftExpression2, any)")

        def visitRelationalExpression0(self, n, o = None): return  self.unimplementedVisitor("visitRelationalExpression0(RelationalExpression0, any)")

        def visitRelationalExpression1(self, n, o = None): return  self.unimplementedVisitor("visitRelationalExpression1(RelationalExpression1, any)")

        def visitRelationalExpression2(self, n, o = None): return  self.unimplementedVisitor("visitRelationalExpression2(RelationalExpression2, any)")

        def visitRelationalExpression3(self, n, o = None): return  self.unimplementedVisitor("visitRelationalExpression3(RelationalExpression3, any)")

        def visitRelationalExpression4(self, n, o = None): return  self.unimplementedVisitor("visitRelationalExpression4(RelationalExpression4, any)")

        def visitEqualityExpression0(self, n, o = None): return  self.unimplementedVisitor("visitEqualityExpression0(EqualityExpression0, any)")

        def visitEqualityExpression1(self, n, o = None): return  self.unimplementedVisitor("visitEqualityExpression1(EqualityExpression1, any)")

        def visitAssignmentOperator0(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator0(AssignmentOperator0, any)")

        def visitAssignmentOperator1(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator1(AssignmentOperator1, any)")

        def visitAssignmentOperator2(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator2(AssignmentOperator2, any)")

        def visitAssignmentOperator3(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator3(AssignmentOperator3, any)")

        def visitAssignmentOperator4(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator4(AssignmentOperator4, any)")

        def visitAssignmentOperator5(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator5(AssignmentOperator5, any)")

        def visitAssignmentOperator6(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator6(AssignmentOperator6, any)")

        def visitAssignmentOperator7(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator7(AssignmentOperator7, any)")

        def visitAssignmentOperator8(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator8(AssignmentOperator8, any)")

        def visitAssignmentOperator9(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator9(AssignmentOperator9, any)")

        def visitAssignmentOperator10(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator10(AssignmentOperator10, any)")

        def visitAssignmentOperator11(self, n, o = None): return  self.unimplementedVisitor("visitAssignmentOperator11(AssignmentOperator11, any)")


        def visit(self, n, o = None):
        
            if isinstance(n, AstToken): return self.visitAstToken(n, o)
            elif isinstance(n, identifier): return self.visitidentifier(n, o)
            elif isinstance(n, PrimitiveType): return self.visitPrimitiveType(n, o)
            elif isinstance(n, ClassType): return self.visitClassType(n, o)
            elif isinstance(n, InterfaceType): return self.visitInterfaceType(n, o)
            elif isinstance(n, TypeName): return self.visitTypeName(n, o)
            elif isinstance(n, ArrayType): return self.visitArrayType(n, o)
            elif isinstance(n, TypeParameter): return self.visitTypeParameter(n, o)
            elif isinstance(n, TypeBound): return self.visitTypeBound(n, o)
            elif isinstance(n, AdditionalBoundList): return self.visitAdditionalBoundList(n, o)
            elif isinstance(n, AdditionalBound): return self.visitAdditionalBound(n, o)
            elif isinstance(n, TypeArguments): return self.visitTypeArguments(n, o)
            elif isinstance(n, ActualTypeArgumentList): return self.visitActualTypeArgumentList(n, o)
            elif isinstance(n, Wildcard): return self.visitWildcard(n, o)
            elif isinstance(n, PackageName): return self.visitPackageName(n, o)
            elif isinstance(n, ExpressionName): return self.visitExpressionName(n, o)
            elif isinstance(n, MethodName): return self.visitMethodName(n, o)
            elif isinstance(n, PackageOrTypeName): return self.visitPackageOrTypeName(n, o)
            elif isinstance(n, AmbiguousName): return self.visitAmbiguousName(n, o)
            elif isinstance(n, CompilationUnit): return self.visitCompilationUnit(n, o)
            elif isinstance(n, ImportDeclarations): return self.visitImportDeclarations(n, o)
            elif isinstance(n, TypeDeclarations): return self.visitTypeDeclarations(n, o)
            elif isinstance(n, PackageDeclaration): return self.visitPackageDeclaration(n, o)
            elif isinstance(n, SingleTypeImportDeclaration): return self.visitSingleTypeImportDeclaration(n, o)
            elif isinstance(n, TypeImportOnDemandDeclaration): return self.visitTypeImportOnDemandDeclaration(n, o)
            elif isinstance(n, SingleStaticImportDeclaration): return self.visitSingleStaticImportDeclaration(n, o)
            elif isinstance(n, StaticImportOnDemandDeclaration): return self.visitStaticImportOnDemandDeclaration(n, o)
            elif isinstance(n, TypeDeclaration): return self.visitTypeDeclaration(n, o)
            elif isinstance(n, NormalClassDeclaration): return self.visitNormalClassDeclaration(n, o)
            elif isinstance(n, ClassModifiers): return self.visitClassModifiers(n, o)
            elif isinstance(n, TypeParameters): return self.visitTypeParameters(n, o)
            elif isinstance(n, TypeParameterList): return self.visitTypeParameterList(n, o)
            elif isinstance(n, Super): return self.visitSuper(n, o)
            elif isinstance(n, Interfaces): return self.visitInterfaces(n, o)
            elif isinstance(n, InterfaceTypeList): return self.visitInterfaceTypeList(n, o)
            elif isinstance(n, ClassBody): return self.visitClassBody(n, o)
            elif isinstance(n, ClassBodyDeclarations): return self.visitClassBodyDeclarations(n, o)
            elif isinstance(n, ClassMemberDeclaration): return self.visitClassMemberDeclaration(n, o)
            elif isinstance(n, FieldDeclaration): return self.visitFieldDeclaration(n, o)
            elif isinstance(n, VariableDeclarators): return self.visitVariableDeclarators(n, o)
            elif isinstance(n, VariableDeclarator): return self.visitVariableDeclarator(n, o)
            elif isinstance(n, VariableDeclaratorId): return self.visitVariableDeclaratorId(n, o)
            elif isinstance(n, FieldModifiers): return self.visitFieldModifiers(n, o)
            elif isinstance(n, MethodDeclaration): return self.visitMethodDeclaration(n, o)
            elif isinstance(n, MethodHeader): return self.visitMethodHeader(n, o)
            elif isinstance(n, ResultType): return self.visitResultType(n, o)
            elif isinstance(n, FormalParameterList): return self.visitFormalParameterList(n, o)
            elif isinstance(n, FormalParameters): return self.visitFormalParameters(n, o)
            elif isinstance(n, FormalParameter): return self.visitFormalParameter(n, o)
            elif isinstance(n, VariableModifiers): return self.visitVariableModifiers(n, o)
            elif isinstance(n, VariableModifier): return self.visitVariableModifier(n, o)
            elif isinstance(n, LastFormalParameter): return self.visitLastFormalParameter(n, o)
            elif isinstance(n, MethodModifiers): return self.visitMethodModifiers(n, o)
            elif isinstance(n, Throws): return self.visitThrows(n, o)
            elif isinstance(n, ExceptionTypeList): return self.visitExceptionTypeList(n, o)
            elif isinstance(n, MethodBody): return self.visitMethodBody(n, o)
            elif isinstance(n, StaticInitializer): return self.visitStaticInitializer(n, o)
            elif isinstance(n, ConstructorDeclaration): return self.visitConstructorDeclaration(n, o)
            elif isinstance(n, ConstructorDeclarator): return self.visitConstructorDeclarator(n, o)
            elif isinstance(n, ConstructorModifiers): return self.visitConstructorModifiers(n, o)
            elif isinstance(n, ConstructorBody): return self.visitConstructorBody(n, o)
            elif isinstance(n, EnumDeclaration): return self.visitEnumDeclaration(n, o)
            elif isinstance(n, EnumBody): return self.visitEnumBody(n, o)
            elif isinstance(n, EnumConstants): return self.visitEnumConstants(n, o)
            elif isinstance(n, EnumConstant): return self.visitEnumConstant(n, o)
            elif isinstance(n, Arguments): return self.visitArguments(n, o)
            elif isinstance(n, EnumBodyDeclarations): return self.visitEnumBodyDeclarations(n, o)
            elif isinstance(n, NormalInterfaceDeclaration): return self.visitNormalInterfaceDeclaration(n, o)
            elif isinstance(n, InterfaceModifiers): return self.visitInterfaceModifiers(n, o)
            elif isinstance(n, InterfaceBody): return self.visitInterfaceBody(n, o)
            elif isinstance(n, InterfaceMemberDeclarations): return self.visitInterfaceMemberDeclarations(n, o)
            elif isinstance(n, InterfaceMemberDeclaration): return self.visitInterfaceMemberDeclaration(n, o)
            elif isinstance(n, ConstantDeclaration): return self.visitConstantDeclaration(n, o)
            elif isinstance(n, ConstantModifiers): return self.visitConstantModifiers(n, o)
            elif isinstance(n, AbstractMethodDeclaration): return self.visitAbstractMethodDeclaration(n, o)
            elif isinstance(n, AbstractMethodModifiers): return self.visitAbstractMethodModifiers(n, o)
            elif isinstance(n, AnnotationTypeDeclaration): return self.visitAnnotationTypeDeclaration(n, o)
            elif isinstance(n, AnnotationTypeBody): return self.visitAnnotationTypeBody(n, o)
            elif isinstance(n, AnnotationTypeElementDeclarations): return self.visitAnnotationTypeElementDeclarations(n, o)
            elif isinstance(n, DefaultValue): return self.visitDefaultValue(n, o)
            elif isinstance(n, Annotations): return self.visitAnnotations(n, o)
            elif isinstance(n, NormalAnnotation): return self.visitNormalAnnotation(n, o)
            elif isinstance(n, ElementValuePairs): return self.visitElementValuePairs(n, o)
            elif isinstance(n, ElementValuePair): return self.visitElementValuePair(n, o)
            elif isinstance(n, ElementValueArrayInitializer): return self.visitElementValueArrayInitializer(n, o)
            elif isinstance(n, ElementValues): return self.visitElementValues(n, o)
            elif isinstance(n, MarkerAnnotation): return self.visitMarkerAnnotation(n, o)
            elif isinstance(n, SingleElementAnnotation): return self.visitSingleElementAnnotation(n, o)
            elif isinstance(n, ArrayInitializer): return self.visitArrayInitializer(n, o)
            elif isinstance(n, VariableInitializers): return self.visitVariableInitializers(n, o)
            elif isinstance(n, Block): return self.visitBlock(n, o)
            elif isinstance(n, BlockStatements): return self.visitBlockStatements(n, o)
            elif isinstance(n, LocalVariableDeclarationStatement): return self.visitLocalVariableDeclarationStatement(n, o)
            elif isinstance(n, LocalVariableDeclaration): return self.visitLocalVariableDeclaration(n, o)
            elif isinstance(n, IfThenStatement): return self.visitIfThenStatement(n, o)
            elif isinstance(n, IfThenElseStatement): return self.visitIfThenElseStatement(n, o)
            elif isinstance(n, IfThenElseStatementNoShortIf): return self.visitIfThenElseStatementNoShortIf(n, o)
            elif isinstance(n, EmptyStatement): return self.visitEmptyStatement(n, o)
            elif isinstance(n, LabeledStatement): return self.visitLabeledStatement(n, o)
            elif isinstance(n, LabeledStatementNoShortIf): return self.visitLabeledStatementNoShortIf(n, o)
            elif isinstance(n, ExpressionStatement): return self.visitExpressionStatement(n, o)
            elif isinstance(n, SwitchStatement): return self.visitSwitchStatement(n, o)
            elif isinstance(n, SwitchBlock): return self.visitSwitchBlock(n, o)
            elif isinstance(n, SwitchBlockStatementGroups): return self.visitSwitchBlockStatementGroups(n, o)
            elif isinstance(n, SwitchBlockStatementGroup): return self.visitSwitchBlockStatementGroup(n, o)
            elif isinstance(n, SwitchLabels): return self.visitSwitchLabels(n, o)
            elif isinstance(n, WhileStatement): return self.visitWhileStatement(n, o)
            elif isinstance(n, WhileStatementNoShortIf): return self.visitWhileStatementNoShortIf(n, o)
            elif isinstance(n, DoStatement): return self.visitDoStatement(n, o)
            elif isinstance(n, BasicForStatement): return self.visitBasicForStatement(n, o)
            elif isinstance(n, ForStatementNoShortIf): return self.visitForStatementNoShortIf(n, o)
            elif isinstance(n, StatementExpressionList): return self.visitStatementExpressionList(n, o)
            elif isinstance(n, EnhancedForStatement): return self.visitEnhancedForStatement(n, o)
            elif isinstance(n, BreakStatement): return self.visitBreakStatement(n, o)
            elif isinstance(n, ContinueStatement): return self.visitContinueStatement(n, o)
            elif isinstance(n, ReturnStatement): return self.visitReturnStatement(n, o)
            elif isinstance(n, ThrowStatement): return self.visitThrowStatement(n, o)
            elif isinstance(n, SynchronizedStatement): return self.visitSynchronizedStatement(n, o)
            elif isinstance(n, Catches): return self.visitCatches(n, o)
            elif isinstance(n, CatchClause): return self.visitCatchClause(n, o)
            elif isinstance(n, Finally): return self.visitFinally(n, o)
            elif isinstance(n, ArgumentList): return self.visitArgumentList(n, o)
            elif isinstance(n, DimExprs): return self.visitDimExprs(n, o)
            elif isinstance(n, DimExpr): return self.visitDimExpr(n, o)
            elif isinstance(n, PostIncrementExpression): return self.visitPostIncrementExpression(n, o)
            elif isinstance(n, PostDecrementExpression): return self.visitPostDecrementExpression(n, o)
            elif isinstance(n, PreIncrementExpression): return self.visitPreIncrementExpression(n, o)
            elif isinstance(n, PreDecrementExpression): return self.visitPreDecrementExpression(n, o)
            elif isinstance(n, AndExpression): return self.visitAndExpression(n, o)
            elif isinstance(n, ExclusiveOrExpression): return self.visitExclusiveOrExpression(n, o)
            elif isinstance(n, InclusiveOrExpression): return self.visitInclusiveOrExpression(n, o)
            elif isinstance(n, ConditionalAndExpression): return self.visitConditionalAndExpression(n, o)
            elif isinstance(n, ConditionalOrExpression): return self.visitConditionalOrExpression(n, o)
            elif isinstance(n, ConditionalExpression): return self.visitConditionalExpression(n, o)
            elif isinstance(n, Assignment): return self.visitAssignment(n, o)
            elif isinstance(n, Commaopt): return self.visitCommaopt(n, o)
            elif isinstance(n, Ellipsisopt): return self.visitEllipsisopt(n, o)
            elif isinstance(n, LPGUserAction0): return self.visitLPGUserAction0(n, o)
            elif isinstance(n, LPGUserAction1): return self.visitLPGUserAction1(n, o)
            elif isinstance(n, LPGUserAction2): return self.visitLPGUserAction2(n, o)
            elif isinstance(n, LPGUserAction3): return self.visitLPGUserAction3(n, o)
            elif isinstance(n, LPGUserAction4): return self.visitLPGUserAction4(n, o)
            elif isinstance(n, IntegralType0): return self.visitIntegralType0(n, o)
            elif isinstance(n, IntegralType1): return self.visitIntegralType1(n, o)
            elif isinstance(n, IntegralType2): return self.visitIntegralType2(n, o)
            elif isinstance(n, IntegralType3): return self.visitIntegralType3(n, o)
            elif isinstance(n, IntegralType4): return self.visitIntegralType4(n, o)
            elif isinstance(n, FloatingPointType0): return self.visitFloatingPointType0(n, o)
            elif isinstance(n, FloatingPointType1): return self.visitFloatingPointType1(n, o)
            elif isinstance(n, WildcardBounds0): return self.visitWildcardBounds0(n, o)
            elif isinstance(n, WildcardBounds1): return self.visitWildcardBounds1(n, o)
            elif isinstance(n, ClassModifier0): return self.visitClassModifier0(n, o)
            elif isinstance(n, ClassModifier1): return self.visitClassModifier1(n, o)
            elif isinstance(n, ClassModifier2): return self.visitClassModifier2(n, o)
            elif isinstance(n, ClassModifier3): return self.visitClassModifier3(n, o)
            elif isinstance(n, ClassModifier4): return self.visitClassModifier4(n, o)
            elif isinstance(n, ClassModifier5): return self.visitClassModifier5(n, o)
            elif isinstance(n, ClassModifier6): return self.visitClassModifier6(n, o)
            elif isinstance(n, FieldModifier0): return self.visitFieldModifier0(n, o)
            elif isinstance(n, FieldModifier1): return self.visitFieldModifier1(n, o)
            elif isinstance(n, FieldModifier2): return self.visitFieldModifier2(n, o)
            elif isinstance(n, FieldModifier3): return self.visitFieldModifier3(n, o)
            elif isinstance(n, FieldModifier4): return self.visitFieldModifier4(n, o)
            elif isinstance(n, FieldModifier5): return self.visitFieldModifier5(n, o)
            elif isinstance(n, FieldModifier6): return self.visitFieldModifier6(n, o)
            elif isinstance(n, MethodDeclarator0): return self.visitMethodDeclarator0(n, o)
            elif isinstance(n, MethodDeclarator1): return self.visitMethodDeclarator1(n, o)
            elif isinstance(n, MethodModifier0): return self.visitMethodModifier0(n, o)
            elif isinstance(n, MethodModifier1): return self.visitMethodModifier1(n, o)
            elif isinstance(n, MethodModifier2): return self.visitMethodModifier2(n, o)
            elif isinstance(n, MethodModifier3): return self.visitMethodModifier3(n, o)
            elif isinstance(n, MethodModifier4): return self.visitMethodModifier4(n, o)
            elif isinstance(n, MethodModifier5): return self.visitMethodModifier5(n, o)
            elif isinstance(n, MethodModifier6): return self.visitMethodModifier6(n, o)
            elif isinstance(n, MethodModifier7): return self.visitMethodModifier7(n, o)
            elif isinstance(n, MethodModifier8): return self.visitMethodModifier8(n, o)
            elif isinstance(n, ConstructorModifier0): return self.visitConstructorModifier0(n, o)
            elif isinstance(n, ConstructorModifier1): return self.visitConstructorModifier1(n, o)
            elif isinstance(n, ConstructorModifier2): return self.visitConstructorModifier2(n, o)
            elif isinstance(n, ExplicitConstructorInvocation0): return self.visitExplicitConstructorInvocation0(n, o)
            elif isinstance(n, ExplicitConstructorInvocation1): return self.visitExplicitConstructorInvocation1(n, o)
            elif isinstance(n, ExplicitConstructorInvocation2): return self.visitExplicitConstructorInvocation2(n, o)
            elif isinstance(n, InterfaceModifier0): return self.visitInterfaceModifier0(n, o)
            elif isinstance(n, InterfaceModifier1): return self.visitInterfaceModifier1(n, o)
            elif isinstance(n, InterfaceModifier2): return self.visitInterfaceModifier2(n, o)
            elif isinstance(n, InterfaceModifier3): return self.visitInterfaceModifier3(n, o)
            elif isinstance(n, InterfaceModifier4): return self.visitInterfaceModifier4(n, o)
            elif isinstance(n, InterfaceModifier5): return self.visitInterfaceModifier5(n, o)
            elif isinstance(n, ExtendsInterfaces0): return self.visitExtendsInterfaces0(n, o)
            elif isinstance(n, ExtendsInterfaces1): return self.visitExtendsInterfaces1(n, o)
            elif isinstance(n, ConstantModifier0): return self.visitConstantModifier0(n, o)
            elif isinstance(n, ConstantModifier1): return self.visitConstantModifier1(n, o)
            elif isinstance(n, ConstantModifier2): return self.visitConstantModifier2(n, o)
            elif isinstance(n, AbstractMethodModifier0): return self.visitAbstractMethodModifier0(n, o)
            elif isinstance(n, AbstractMethodModifier1): return self.visitAbstractMethodModifier1(n, o)
            elif isinstance(n, AnnotationTypeElementDeclaration0): return self.visitAnnotationTypeElementDeclaration0(n, o)
            elif isinstance(n, AnnotationTypeElementDeclaration1): return self.visitAnnotationTypeElementDeclaration1(n, o)
            elif isinstance(n, AssertStatement0): return self.visitAssertStatement0(n, o)
            elif isinstance(n, AssertStatement1): return self.visitAssertStatement1(n, o)
            elif isinstance(n, SwitchLabel0): return self.visitSwitchLabel0(n, o)
            elif isinstance(n, SwitchLabel1): return self.visitSwitchLabel1(n, o)
            elif isinstance(n, SwitchLabel2): return self.visitSwitchLabel2(n, o)
            elif isinstance(n, TryStatement0): return self.visitTryStatement0(n, o)
            elif isinstance(n, TryStatement1): return self.visitTryStatement1(n, o)
            elif isinstance(n, PrimaryNoNewArray0): return self.visitPrimaryNoNewArray0(n, o)
            elif isinstance(n, PrimaryNoNewArray1): return self.visitPrimaryNoNewArray1(n, o)
            elif isinstance(n, PrimaryNoNewArray2): return self.visitPrimaryNoNewArray2(n, o)
            elif isinstance(n, PrimaryNoNewArray3): return self.visitPrimaryNoNewArray3(n, o)
            elif isinstance(n, PrimaryNoNewArray4): return self.visitPrimaryNoNewArray4(n, o)
            elif isinstance(n, Literal0): return self.visitLiteral0(n, o)
            elif isinstance(n, Literal1): return self.visitLiteral1(n, o)
            elif isinstance(n, Literal2): return self.visitLiteral2(n, o)
            elif isinstance(n, Literal3): return self.visitLiteral3(n, o)
            elif isinstance(n, Literal4): return self.visitLiteral4(n, o)
            elif isinstance(n, Literal5): return self.visitLiteral5(n, o)
            elif isinstance(n, Literal6): return self.visitLiteral6(n, o)
            elif isinstance(n, BooleanLiteral0): return self.visitBooleanLiteral0(n, o)
            elif isinstance(n, BooleanLiteral1): return self.visitBooleanLiteral1(n, o)
            elif isinstance(n, ClassInstanceCreationExpression0): return self.visitClassInstanceCreationExpression0(n, o)
            elif isinstance(n, ClassInstanceCreationExpression1): return self.visitClassInstanceCreationExpression1(n, o)
            elif isinstance(n, ArrayCreationExpression0): return self.visitArrayCreationExpression0(n, o)
            elif isinstance(n, ArrayCreationExpression1): return self.visitArrayCreationExpression1(n, o)
            elif isinstance(n, ArrayCreationExpression2): return self.visitArrayCreationExpression2(n, o)
            elif isinstance(n, ArrayCreationExpression3): return self.visitArrayCreationExpression3(n, o)
            elif isinstance(n, Dims0): return self.visitDims0(n, o)
            elif isinstance(n, Dims1): return self.visitDims1(n, o)
            elif isinstance(n, FieldAccess0): return self.visitFieldAccess0(n, o)
            elif isinstance(n, FieldAccess1): return self.visitFieldAccess1(n, o)
            elif isinstance(n, FieldAccess2): return self.visitFieldAccess2(n, o)
            elif isinstance(n, MethodInvocation0): return self.visitMethodInvocation0(n, o)
            elif isinstance(n, MethodInvocation1): return self.visitMethodInvocation1(n, o)
            elif isinstance(n, MethodInvocation2): return self.visitMethodInvocation2(n, o)
            elif isinstance(n, MethodInvocation3): return self.visitMethodInvocation3(n, o)
            elif isinstance(n, MethodInvocation4): return self.visitMethodInvocation4(n, o)
            elif isinstance(n, ArrayAccess0): return self.visitArrayAccess0(n, o)
            elif isinstance(n, ArrayAccess1): return self.visitArrayAccess1(n, o)
            elif isinstance(n, UnaryExpression0): return self.visitUnaryExpression0(n, o)
            elif isinstance(n, UnaryExpression1): return self.visitUnaryExpression1(n, o)
            elif isinstance(n, UnaryExpressionNotPlusMinus0): return self.visitUnaryExpressionNotPlusMinus0(n, o)
            elif isinstance(n, UnaryExpressionNotPlusMinus1): return self.visitUnaryExpressionNotPlusMinus1(n, o)
            elif isinstance(n, CastExpression0): return self.visitCastExpression0(n, o)
            elif isinstance(n, CastExpression1): return self.visitCastExpression1(n, o)
            elif isinstance(n, MultiplicativeExpression0): return self.visitMultiplicativeExpression0(n, o)
            elif isinstance(n, MultiplicativeExpression1): return self.visitMultiplicativeExpression1(n, o)
            elif isinstance(n, MultiplicativeExpression2): return self.visitMultiplicativeExpression2(n, o)
            elif isinstance(n, AdditiveExpression0): return self.visitAdditiveExpression0(n, o)
            elif isinstance(n, AdditiveExpression1): return self.visitAdditiveExpression1(n, o)
            elif isinstance(n, ShiftExpression0): return self.visitShiftExpression0(n, o)
            elif isinstance(n, ShiftExpression1): return self.visitShiftExpression1(n, o)
            elif isinstance(n, ShiftExpression2): return self.visitShiftExpression2(n, o)
            elif isinstance(n, RelationalExpression0): return self.visitRelationalExpression0(n, o)
            elif isinstance(n, RelationalExpression1): return self.visitRelationalExpression1(n, o)
            elif isinstance(n, RelationalExpression2): return self.visitRelationalExpression2(n, o)
            elif isinstance(n, RelationalExpression3): return self.visitRelationalExpression3(n, o)
            elif isinstance(n, RelationalExpression4): return self.visitRelationalExpression4(n, o)
            elif isinstance(n, EqualityExpression0): return self.visitEqualityExpression0(n, o)
            elif isinstance(n, EqualityExpression1): return self.visitEqualityExpression1(n, o)
            elif isinstance(n, AssignmentOperator0): return self.visitAssignmentOperator0(n, o)
            elif isinstance(n, AssignmentOperator1): return self.visitAssignmentOperator1(n, o)
            elif isinstance(n, AssignmentOperator2): return self.visitAssignmentOperator2(n, o)
            elif isinstance(n, AssignmentOperator3): return self.visitAssignmentOperator3(n, o)
            elif isinstance(n, AssignmentOperator4): return self.visitAssignmentOperator4(n, o)
            elif isinstance(n, AssignmentOperator5): return self.visitAssignmentOperator5(n, o)
            elif isinstance(n, AssignmentOperator6): return self.visitAssignmentOperator6(n, o)
            elif isinstance(n, AssignmentOperator7): return self.visitAssignmentOperator7(n, o)
            elif isinstance(n, AssignmentOperator8): return self.visitAssignmentOperator8(n, o)
            elif isinstance(n, AssignmentOperator9): return self.visitAssignmentOperator9(n, o)
            elif isinstance(n, AssignmentOperator10): return self.visitAssignmentOperator10(n, o)
            elif isinstance(n, AssignmentOperator11): return self.visitAssignmentOperator11(n, o)
            else: raise ValueError("visit(" + n.toString() + ")")
        
    

