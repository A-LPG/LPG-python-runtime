
'''////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2007 IBM Corporation.
// All rights reserved. This program and the accompanying materials
// are made available under the terms of the Eclipse Public License v1.0
// which accompanies this distribution, and is available at
// http://www.eclipse.org/legal/epl-v10.html
//
//Contributors:
//    Philippe Charles (pcharles@us.ibm.com) - initial API and implementation

////////////////////////////////////////////////////////////////////////////////'''


    ##line 104 "LexerTemplateF.gi

from lpg2  import  RuleAction, ParseTable, LexParser, ILexStream, IPrsStream, Monitor,LpgLexStream
from LPGLexerprs  import  LPGLexerprs 
from LPGLexersym  import  LPGLexersym  
from LPGKWLexer  import  LPGKWLexer 

    ##line 7 "LPGLexer.gi



    ##line 2 "LexerBasicMapF.gi

from LPGParsersym import  LPGParsersym  

    ##line 114 "LexerTemplateF.gi

class LPGLexer (RuleAction):

    prs : ParseTable =  LPGLexerprs()
    def getParseTable(self) -> ParseTable :
        return LPGLexer.prs 

    def getParser(self) ->LexParser :  return self.lexParser 

    def getToken(self, i: int)  -> int:
        return self.lexParser.getToken(i) 

    def getRhsFirstTokenIndex(self, i: int) -> int: 
        return self.lexParser.getFirstToken(i) 

    def getRhsLastTokenIndex(self, i: int)  -> int:
        return self.lexParser.getLastToken(i) 

    def getLeftSpan(self) -> int:
        return self.lexParser.getToken(1) 

    def getRightSpan(self) -> int : 
        return self.lexParser.getLastToken() 

    def resetKeywordLexer(self) : 
    
        if not self.kwLexer:
           self.kwLexer =  LPGKWLexer(self.lexStream.getInputChars(), LPGParsersym.TK_MACRO_NAME)
        self.kwLexer.setInputChars(self.lexStream.getInputChars())
    
    def reset(self, filename : str,  tab: int = 4, input_chars: str = None) : 
    
        self.lexStream =  LPGLexerLpgLexStream(filename,input_chars, tab)
        self.lexParser.reset(self.lexStream, LPGLexer.prs,  self)
        self.resetKeywordLexer()
    
    
    def ruleAction(self,ruleNumber: int) :
        act = self.__rule_action[ruleNumber]
        if act:
            act() 

    def __init__(self, filename: str,  tab: int =  4 ,input_chars : str = None):
    
        super().__init__()
        self.__rule_action = [None]* (1130 + 2)
        self.kwLexer :  LPGKWLexer = None
        self.printTokens : bool =False
        self.lexParser  : LexParser =  LexParser()
        self.lexStream: LPGLexerLpgLexStream 
        self.initRuleAction()
        self.lexStream =  LPGLexerLpgLexStream(filename,input_chars, tab)
        self.lexParser.reset(  self.lexStream, LPGLexer.prs,  self)
        self.resetKeywordLexer()
    

    def getILexStream(self) ->ILexStream : 
        return  self.lexStream 

    def initializeLexer(self,prsStream : IPrsStream ,  start_offset : int, end_offset : int) :  
    
        if self.lexStream.getInputChars() is  None:
            raise  ValueError("LexStream was not initialized")
        self.lexStream.setPrsStream(prsStream)
        prsStream.makeToken(start_offset, end_offset, 0) # Token list must start with a bad token
    
    def addEOF(self,prsStream : IPrsStream, end_offset : int ) : 
    
        prsStream.makeToken(end_offset, end_offset, LPGParsersym.TK_EOF_TOKEN) # and end with the end of file token
        prsStream.setStreamLength(prsStream.getSize())
    

    def lexerWithPosition(self,prsStream: IPrsStream , start_offset: int , end_offset: int, monitor: Monitor = None) : 
    
        if start_offset <= 1:
            self.initializeLexer(prsStream, 0, -1)
        else :
            self.initializeLexer(prsStream, start_offset - 1, start_offset - 1)

        self.lexParser.parseCharacters(start_offset, end_offset,monitor)

        self.addEOF(prsStream, ( self.lexStream.getStreamIndex() if end_offset >= self.lexStream.getStreamIndex() else  end_offset + 1))
    
    def lexer(self,prsStream: IPrsStream ,  monitor: Monitor = None) : 
    
        self.initializeLexer(prsStream, 0, -1)
        self.lexParser.parseCharactersWhitMonitor(monitor)
        self.addEOF(prsStream, self.lexStream.getStreamIndex())
    
    '''/**
     * If a parse stream was not passed to self Lexical analyser then we
     * simply report a lexical error. Otherwise, we produce a bad token.
     */'''
    def reportLexicalError(self, startLoc: int,  endLoc: int):  
        prs_stream = self.lexStream.getIPrsStream()
        if (not prs_stream):
            self.lexStream.reportLexicalError(startLoc, endLoc)
        else: 
            #
            # Remove any token that may have been processed that fall in the
            # range of the lexical error... then add one error token that spans
            # the error range.
            #
            i: int = prs_stream.getSize() - 1
            while  i > 0 : 
                if prs_stream.getStartOffset(i) >= startLoc:
                     prs_stream.removeLastToken()
                else:
                     break
                i-=1
            
            prs_stream.makeToken(startLoc, endLoc, 0) # add an error token to the self.prsStream
                
    

    ##line 12 "LPGLexer.gi

 
    ##line 164 "LexerBasicMapF.gi


    '''#
    # The Lexer contains an array of characters as the input stream to be parsed.
    # There are methods to retrieve and classify characters.
    # The lexparser "token" is implemented simply as the index of the next character in the array.
    # The Lexer : the abstract class LpgLexStream with an implementation of the abstract
    # method getKind.  The template defines the Lexer class and the lexer() method.
    # A driver creates the action class, "Lexer", passing an Option object to the constructor.
    #'''


    ECLIPSE_TAB_VALUE: int = 4

    def getKeywordKinds(self) :  

        if  self.kwLexer is None:
            raise ValueError("please initilize kwLexer")
        
        return self.kwLexer.getKeywordKinds() 
    
    def makeToken1(self,left_token: int,right_token: int, kind: int) :
    
        self.lexStream.makeToken(left_token, right_token, kind)
    
    
    def makeToken(self, arg0: int, arg1: int= None, arg2: int = None) :
    
        if arg1 is not None and arg2 is not None:
            self.makeToken1(arg0,arg1,arg2)
            return 
        
        startOffset  = self.getLeftSpan()
        endOffset = self.getRightSpan()
        self.lexStream.makeToken(startOffset, endOffset, arg0)
        if self.printTokens: 
           self.printValue(startOffset, endOffset)
    

    def makeComment(self,kind : int) :
    
        startOffset =  self.getLeftSpan()
        endOffset =  self.getRightSpan()
        self.lexStream.getIPrsStream().makeAdjunct(startOffset, endOffset, kind)
    

    def skipToken(self) : 

        if self.printTokens:  self.printValue( self.getLeftSpan(),  self.getRightSpan())
    
    
    def checkForKeyWord1(self) : 
    
        if not self.kwLexer:
            raise ValueError("please initilize kwLexer")
        
        startOffset =  self.getLeftSpan()
        endOffset =  self.getRightSpan()
        kwKind = self.kwLexer.lexer(startOffset, endOffset)
        self.lexStream.makeToken(startOffset, endOffset, kwKind)
        if  self.printTokens:  self.printValue(startOffset, endOffset)
    
    
    #
    # This flavor of checkForKeyWord is necessary when the default kind
    # (which is returned when the keyword filter doesn't match) is something
    # other than _IDENTIFIER.
    #
    def checkForKeyWord(self,defaultKind :int = None) : 
    
        if defaultKind is None:
            self.checkForKeyWord1()
            return
       
        if self.kwLexer is None:
            raise ValueError("please initilize kwLexer")
        
        startOffset =  self.getLeftSpan()
        endOffset =  self.getRightSpan()
        kwKind =  self.kwLexer.lexer(startOffset, endOffset)
        if kwKind == LPGParsersym.TK_MACRO_NAME:
           kwKind = defaultKind
        self.lexStream.makeToken(startOffset, endOffset, kwKind)
        if self.printTokens: 
           self.printValue(startOffset, endOffset)
    
    
    def printValue(self, startOffset : int, endOffset : int) : 
    
         s = self.lexStream.getInputChars()[startOffset:endOffset  + 1]
         print(s, end='')
    

  

    ##line 232 "LexerTemplateF.gi

    def initRuleAction(self) : 


        #
        # Rule 1:  Token ::= white
        #
         def Act1():
             self.skipToken() 
         self.__rule_action[1] = Act1


        #
        # Rule 2:  Token ::= singleLineComment
        #
         def Act2():
             self.makeComment(LPGParsersym.TK_SINGLE_LINE_COMMENT) 
         self.__rule_action[2] = Act2


        #
        # Rule 4:  Token ::= MacroSymbol
        #
         def Act4():
             self.checkForKeyWord()
         self.__rule_action[4] = Act4


        #
        # Rule 5:  Token ::= Symbol
        #
         def Act5():
             self.checkForKeyWord(LPGParsersym.TK_SYMBOL)
         self.__rule_action[5] = Act5


        #
        # Rule 6:  Token ::= Block
        #
         def Act6():
             self.makeToken(LPGParsersym.TK_BLOCK)
         self.__rule_action[6] = Act6


        #
        # Rule 7:  Token ::= Equivalence
        #
         def Act7():
             self.makeToken(LPGParsersym.TK_EQUIVALENCE)
         self.__rule_action[7] = Act7


        #
        # Rule 8:  Token ::= Equivalence ?
        #
         def Act8():
             self.makeToken(LPGParsersym.TK_PRIORITY_EQUIVALENCE)
         self.__rule_action[8] = Act8


        #
        # Rule 9:  Token ::= #
        #
         def Act9():
             self.makeToken(LPGParsersym.TK_SHARP)
         self.__rule_action[9] = Act9


        #
        # Rule 10:  Token ::= Arrow
        #
         def Act10():
             self.makeToken(LPGParsersym.TK_ARROW)
         self.__rule_action[10] = Act10


        #
        # Rule 11:  Token ::= Arrow ?
        #
         def Act11():
             self.makeToken(LPGParsersym.TK_PRIORITY_ARROW)
         self.__rule_action[11] = Act11


        #
        # Rule 12:  Token ::= |
        #
         def Act12():
             self.makeToken(LPGParsersym.TK_OR_MARKER)
         self.__rule_action[12] = Act12


        #
        # Rule 13:  Token ::= [
        #
         def Act13():
             self.makeToken(LPGParsersym.TK_LEFT_BRACKET)
         self.__rule_action[13] = Act13


        #
        # Rule 14:  Token ::= ]
        #
         def Act14():
             self.makeToken(LPGParsersym.TK_RIGHT_BRACKET)
         self.__rule_action[14] = Act14


        #
        # Rule 859:  OptionLines ::= OptionLineList
        #
         def Act859():
            
                  '''// What ever needs to happen after the options have been 
                  // scanned must happen here.'''
        
         self.__rule_action[859] = Act859

      
        #
        # Rule 868:  options ::= % oO pP tT iI oO nN sS
        #
         def Act868():
            
                  self.makeToken(self.getLeftSpan(), self.getRightSpan(), LPGParsersym.TK_OPTIONS_KEY)
        
         self.__rule_action[868] = Act868

      
        #
        # Rule 869:  OptionComment ::= singleLineComment
        #
         def Act869():
             self.makeComment(LPGParsersym.TK_SINGLE_LINE_COMMENT) 
         self.__rule_action[869] = Act869


        #
        # Rule 893:  separator ::= ,$comma
        #
         def Act893():
              self.makeToken(self.getLeftSpan(), self.getRightSpan(), LPGParsersym.TK_COMMA) 
         self.__rule_action[893] = Act893


        #
        # Rule 894:  option ::= action_block$ab optionWhite =$eq optionWhite ($lp optionWhite filename$fn optionWhite ,$comma1 optionWhite block_begin$bb optionWhite ,$comma2 optionWhite block_end$be optionWhite )$rp optionWhite
        #
         def Act894():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)
                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(11), self.getRhsLastTokenIndex(11), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(13), self.getRhsLastTokenIndex(13), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(15), self.getRhsLastTokenIndex(15), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(17), self.getRhsLastTokenIndex(17), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[894] = Act894

      
        #
        # Rule 897:  option ::= ast_block$ab optionWhite =$eq optionWhite ($lp optionWhite block_begin$bb optionWhite ,$comma2 optionWhite block_end$be optionWhite )$rp optionWhite
        #
         def Act897():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)

                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(11), self.getRhsLastTokenIndex(11), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(13), self.getRhsLastTokenIndex(13), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[897] = Act897

      
        #
        # Rule 902:  option ::= ast_directory$ad optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act902():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[902] = Act902

      
        #
        # Rule 905:  option ::= ast_type$at optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act905():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[905] = Act905

      
        #
        # Rule 908:  option ::= attributes$a optionWhite
        #
         def Act908():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[908] = Act908


        #
        # Rule 909:  option ::= no attributes$a optionWhite
        #
         def Act909():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[909] = Act909


        #
        # Rule 911:  option ::= automatic_ast$a optionWhite
        #
         def Act911():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[911] = Act911


        #
        # Rule 912:  option ::= no automatic_ast$a optionWhite
        #
         def Act912():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[912] = Act912


        #
        # Rule 913:  option ::= automatic_ast$aa optionWhite =$eq optionWhite automatic_ast_value$val optionWhite
        #
         def Act913():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[913] = Act913

      
        #
        # Rule 917:  option ::= backtrack$b optionWhite
        #
         def Act917():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[917] = Act917


        #
        # Rule 918:  option ::= no backtrack$b optionWhite
        #
         def Act918():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[918] = Act918


        #
        # Rule 920:  option ::= byte$b optionWhite
        #
         def Act920():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[920] = Act920


        #
        # Rule 921:  option ::= no byte$b optionWhite
        #
         def Act921():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[921] = Act921


        #
        # Rule 923:  option ::= conflicts$c optionWhite
        #
         def Act923():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[923] = Act923


        #
        # Rule 924:  option ::= no conflicts$c optionWhite
        #
         def Act924():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[924] = Act924


        #
        # Rule 926:  option ::= dat_directory$dd optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act926():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[926] = Act926

      
        #
        # Rule 929:  option ::= dat_file$df optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act929():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[929] = Act929

      
        #
        # Rule 931:  option ::= dcl_file$df optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act931():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[931] = Act931

      
        #
        # Rule 933:  option ::= def_file$df optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act933():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[933] = Act933

      
        #
        # Rule 935:  option ::= debug$d optionWhite
        #
         def Act935():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[935] = Act935


        #
        # Rule 936:  option ::= no debug$d optionWhite
        #
         def Act936():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[936] = Act936


        #
        # Rule 938:  option ::= edit$e optionWhite
        #
         def Act938():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[938] = Act938


        #
        # Rule 939:  option ::= no edit$e optionWhite
        #
         def Act939():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[939] = Act939


        #
        # Rule 941:  option ::= error_maps$e optionWhite
        #
         def Act941():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[941] = Act941


        #
        # Rule 942:  option ::= no error_maps$e optionWhite
        #
         def Act942():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[942] = Act942


        #
        # Rule 945:  option ::= escape$e optionWhite =$eq optionWhite anyNonWhiteChar$val optionWhite
        #
         def Act945():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
                
        
         self.__rule_action[945] = Act945

      
        #
        # Rule 947:  option ::= export_terminals$et optionWhite =$eq optionWhite filename$fn optionWhite
        #
         def Act947():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[947] = Act947

      
        #
        # Rule 948:  option ::= export_terminals$et optionWhite =$eq optionWhite ($lp optionWhite filename$fn optionWhite )$rp optionWhite
        #
         def Act948():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)
                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[948] = Act948

      
        #
        # Rule 949:  option ::= export_terminals$et optionWhite =$eq optionWhite ($lp optionWhite filename$fn optionWhite ,$comma optionWhite export_prefix$ep optionWhite )$rp optionWhite
        #
         def Act949():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)
                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(11), self.getRhsLastTokenIndex(11), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(13), self.getRhsLastTokenIndex(13), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[949] = Act949

      
        #
        # Rule 950:  option ::= export_terminals$et optionWhite =$eq optionWhite ($lp optionWhite filename$fn optionWhite ,$comma1 optionWhite export_prefix$ep optionWhite ,$comma2 optionWhite export_suffix$es optionWhite )$rp optionWhite
        #
         def Act950():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)
                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(11), self.getRhsLastTokenIndex(11), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(13), self.getRhsLastTokenIndex(13), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(15), self.getRhsLastTokenIndex(15), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(17), self.getRhsLastTokenIndex(17), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[950] = Act950

      
        #
        # Rule 955:  option ::= extends_parsetable$e optionWhite
        #
         def Act955():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[955] = Act955


        #
        # Rule 956:  option ::= no extends_parsetable$e optionWhite
        #
         def Act956():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[956] = Act956


        #
        # Rule 957:  option ::= extends_parsetable$ep optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act957():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[957] = Act957

      
        #
        # Rule 960:  option ::= factory$f optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act960():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[960] = Act960

      
        #
        # Rule 962:  option ::= file_prefix$fp optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act962():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[962] = Act962

      
        #
        # Rule 965:  option ::= filter$f optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act965():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[965] = Act965

      
        #
        # Rule 967:  option ::= first$f optionWhite
        #
         def Act967():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[967] = Act967


        #
        # Rule 968:  option ::= no first$f optionWhite
        #
         def Act968():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[968] = Act968


        #
        # Rule 970:  option ::= follow$f optionWhite
        #
         def Act970():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[970] = Act970


        #
        # Rule 971:  option ::= no follow$f optionWhite
        #
         def Act971():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[971] = Act971


        #
        # Rule 973:  option ::= goto_default$g optionWhite
        #
         def Act973():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[973] = Act973


        #
        # Rule 974:  option ::= no goto_default$g optionWhite
        #
         def Act974():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[974] = Act974


        #
        # Rule 977:  option ::= headers$h optionWhite =$eq optionWhite ($lp optionWhite filename$fn optionWhite ,$comma1 optionWhite block_begin$bb optionWhite ,$comma2 optionWhite block_end$be optionWhite )$rp optionWhite
        #
         def Act977():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)
                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(11), self.getRhsLastTokenIndex(11), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(13), self.getRhsLastTokenIndex(13), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(15), self.getRhsLastTokenIndex(15), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(17), self.getRhsLastTokenIndex(17), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[977] = Act977

      
        #
        # Rule 979:  option ::= imp_file$if optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act979():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[979] = Act979

      
        #
        # Rule 982:  option ::= import_terminals$it optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act982():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[982] = Act982

      
        #
        # Rule 985:  option ::= include_directory$id optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act985():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[985] = Act985

      
        #
        # Rule 989:  option ::= lalr_level$l optionWhite
        #
         def Act989():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[989] = Act989


        #
        # Rule 990:  option ::= no lalr_level$l optionWhite
        #
         def Act990():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[990] = Act990


        #
        # Rule 991:  option ::= lalr_level$l optionWhite =$eq optionWhite number$val optionWhite
        #
         def Act991():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[991] = Act991

      
        #
        # Rule 996:  option ::= list$l optionWhite
        #
         def Act996():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[996] = Act996


        #
        # Rule 997:  option ::= no list$l optionWhite
        #
         def Act997():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[997] = Act997


        #
        # Rule 999:  option ::= margin$m optionWhite =$eq optionWhite number$val optionWhite
        #
         def Act999():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[999] = Act999

      
        #
        # Rule 1001:  option ::= max_cases$mc optionWhite =$eq optionWhite number$val optionWhite
        #
         def Act1001():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1001] = Act1001

      
        #
        # Rule 1004:  option ::= names$n optionWhite
        #
         def Act1004():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1004] = Act1004


        #
        # Rule 1005:  option ::= no names$n optionWhite
        #
         def Act1005():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1005] = Act1005


        #
        # Rule 1006:  option ::= names$n optionWhite =$eq optionWhite names_value$val optionWhite
        #
         def Act1006():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1006] = Act1006

      
        #
        # Rule 1011:  option ::= nt_check$n optionWhite
        #
         def Act1011():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1011] = Act1011


        #
        # Rule 1012:  option ::= no nt_check$n optionWhite
        #
         def Act1012():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1012] = Act1012


        #
        # Rule 1015:  option ::= or_marker$om optionWhite =$eq optionWhite anyNonWhiteChar$val optionWhite
        #
         def Act1015():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1015] = Act1015

      
        #
        # Rule 1018:  option ::= out_directory$dd optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1018():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1018] = Act1018

      
        #
        # Rule 1021:  option ::= parent_saved$ps optionWhite
        #
         def Act1021():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1021] = Act1021
 

        #
        # Rule 1022:  option ::= no parent_saved$ps optionWhite
        #
         def Act1022():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1022] = Act1022
 

        #
        # Rule 1025:  option ::= package$p optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1025():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1025] = Act1025

      
        #
        # Rule 1027:  option ::= parsetable_interfaces$pi optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1027():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1027] = Act1027

      
        #
        # Rule 1031:  option ::= prefix$p optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1031():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1031] = Act1031

      
        #
        # Rule 1033:  option ::= priority$p optionWhite
        #
         def Act1033():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1033] = Act1033


        #
        # Rule 1034:  option ::= no priority$p optionWhite
        #
         def Act1034():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1034] = Act1034


        #
        # Rule 1036:  option ::= programming_language$pl optionWhite =$eq optionWhite programming_language_value$val optionWhite
        #
         def Act1036():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1036] = Act1036

      
        #
        # Rule 1040:  option ::= prs_file$pf optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1040():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1040] = Act1040

      
        #
        # Rule 1043:  option ::= quiet$q optionWhite
        #
         def Act1043():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1043] = Act1043


        #
        # Rule 1044:  option ::= no quiet$q optionWhite
        #
         def Act1044():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1044] = Act1044


        #
        # Rule 1046:  option ::= read_reduce$r optionWhite
        #
         def Act1046():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1046] = Act1046


        #
        # Rule 1047:  option ::= no read_reduce$r optionWhite
        #
         def Act1047():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1047] = Act1047


        #
        # Rule 1050:  option ::= remap_terminals$r optionWhite
        #
         def Act1050():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1050] = Act1050


        #
        # Rule 1051:  option ::= no remap_terminals$r optionWhite
        #
         def Act1051():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1051] = Act1051


        #
        # Rule 1054:  option ::= scopes$s optionWhite
        #
         def Act1054():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1054] = Act1054
 

        #
        # Rule 1055:  option ::= no scopes$s optionWhite
        #
         def Act1055():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1055] = Act1055
 

        #
        # Rule 1057:  option ::= serialize$s optionWhite
        #
         def Act1057():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1057] = Act1057
 

        #
        # Rule 1058:  option ::= no serialize$s optionWhite
        #
         def Act1058():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1058] = Act1058
 

        #
        # Rule 1060:  option ::= shift_default$s optionWhite
        #
         def Act1060():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1060] = Act1060
 

        #
        # Rule 1061:  option ::= no shift_default$s optionWhite
        #
         def Act1061():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1061] = Act1061
 

        #
        # Rule 1064:  option ::= single_productions$s optionWhite
        #
         def Act1064():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1064] = Act1064
 

        #
        # Rule 1065:  option ::= no single_productions$s optionWhite
        #
         def Act1065():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1065] = Act1065
 

        #
        # Rule 1068:  option ::= slr$s optionWhite
        #
         def Act1068():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1068] = Act1068
 

        #
        # Rule 1069:  option ::= no slr$s optionWhite
        #
         def Act1069():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1069] = Act1069
 

        #
        # Rule 1071:  option ::= soft_keywords$s optionWhite
        #
         def Act1071():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1071] = Act1071
 

        #
        # Rule 1072:  option ::= no soft_keywords$s optionWhite
        #
         def Act1072():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1072] = Act1072
 

        #
        # Rule 1076:  option ::= states$s optionWhite
        #
         def Act1076():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1076] = Act1076
 

        #
        # Rule 1077:  option ::= no states$s optionWhite
        #
         def Act1077():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1077] = Act1077
 

        #
        # Rule 1079:  option ::= suffix$s optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1079():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1079] = Act1079

      
        #
        # Rule 1081:  option ::= sym_file$sf optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1081():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1081] = Act1081

      
        #
        # Rule 1084:  option ::= tab_file$tf optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1084():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1084] = Act1084

      
        #
        # Rule 1087:  option ::= template$t optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1087():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1087] = Act1087

      
        #
        # Rule 1089:  option ::= trailers$t optionWhite =$eq optionWhite ($lp optionWhite filename$fn optionWhite ,$comma1 optionWhite block_begin$bb optionWhite ,$comma2 optionWhite block_end$be optionWhite )$rp optionWhite
        #
         def Act1089():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_LEFT_PAREN)
                  self.makeToken(self.getRhsFirstTokenIndex(7), self.getRhsLastTokenIndex(7), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(9), self.getRhsLastTokenIndex(9), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(11), self.getRhsLastTokenIndex(11), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(13), self.getRhsLastTokenIndex(13), LPGParsersym.TK_COMMA)
                  self.makeToken(self.getRhsFirstTokenIndex(15), self.getRhsLastTokenIndex(15), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(17), self.getRhsLastTokenIndex(17), LPGParsersym.TK_RIGHT_PAREN)
        
         self.__rule_action[1089] = Act1089

      
        #
        # Rule 1091:  option ::= table$t optionWhite
        #
         def Act1091():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1091] = Act1091
 

        #
        # Rule 1092:  option ::= no table$t optionWhite
        #
         def Act1092():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1092] = Act1092
 

        #
        # Rule 1093:  option ::= table$t optionWhite =$eq optionWhite programming_language_value$val optionWhite
        #
         def Act1093():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1093] = Act1093

      
        #
        # Rule 1095:  option ::= trace$t optionWhite
        #
         def Act1095():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1095] = Act1095
 

        #
        # Rule 1096:  option ::= no trace$t optionWhite
        #
         def Act1096():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1096] = Act1096
 

        #
        # Rule 1097:  option ::= trace$t optionWhite =$eq optionWhite trace_value$val optionWhite
        #
         def Act1097():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1097] = Act1097

      
        #
        # Rule 1102:  option ::= variables$v optionWhite
        #
         def Act1102():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1102] = Act1102
 

        #
        # Rule 1103:  option ::= no variables$v optionWhite
        #
         def Act1103():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1103] = Act1103
 

        #
        # Rule 1104:  option ::= variables$v optionWhite =$eq optionWhite variables_value$val optionWhite
        #
         def Act1104():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1104] = Act1104

      
        #
        # Rule 1111:  option ::= verbose$v optionWhite
        #
         def Act1111():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1111] = Act1111
 

        #
        # Rule 1112:  option ::= no verbose$v optionWhite
        #
         def Act1112():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1112] = Act1112
 

        #
        # Rule 1114:  option ::= visitor$v optionWhite
        #
         def Act1114():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1114] = Act1114
 

        #
        # Rule 1115:  option ::= no visitor$v optionWhite
        #
         def Act1115():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1115] = Act1115
 

        #
        # Rule 1116:  option ::= visitor$v optionWhite =$eq optionWhite visitor_value$val optionWhite
        #
         def Act1116():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1116] = Act1116

      
        #
        # Rule 1121:  option ::= visitor_type$vt optionWhite =$eq optionWhite Value$val optionWhite
        #
         def Act1121():
            
                  self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL)
                  self.makeToken(self.getRhsFirstTokenIndex(3), self.getRhsLastTokenIndex(3), LPGParsersym.TK_EQUAL)
                  self.makeToken(self.getRhsFirstTokenIndex(5), self.getRhsLastTokenIndex(5), LPGParsersym.TK_SYMBOL)
        
         self.__rule_action[1121] = Act1121

      
        #
        # Rule 1124:  option ::= warnings$w optionWhite
        #
         def Act1124():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1124] = Act1124
 

        #
        # Rule 1125:  option ::= no warnings$w optionWhite
        #
         def Act1125():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1125] = Act1125
 

        #
        # Rule 1127:  option ::= xreference$x optionWhite
        #
         def Act1127():
              self.makeToken(self.getRhsFirstTokenIndex(1), self.getRhsLastTokenIndex(1), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1127] = Act1127
 

        #
        # Rule 1128:  option ::= no xreference$x optionWhite
        #
         def Act1128():
              self.makeToken(self.getRhsFirstTokenIndex(2), self.getRhsLastTokenIndex(2), LPGParsersym.TK_SYMBOL) 
         self.__rule_action[1128] = Act1128
 

    ##line 236 "LexerTemplateF.gi

    


    ##line 7 "LexerBasicMapF.gi
 
class  LPGLexerLpgLexStream(LpgLexStream):
    
    tokenKind : list =[
        LPGLexersym.Char_CtlCharNotWS,    # 000    0x00
        LPGLexersym.Char_CtlCharNotWS,    # 001    0x01
        LPGLexersym.Char_CtlCharNotWS,    # 002    0x02
        LPGLexersym.Char_CtlCharNotWS,    # 003    0x03
        LPGLexersym.Char_CtlCharNotWS,    # 004    0x04
        LPGLexersym.Char_CtlCharNotWS,    # 005    0x05
        LPGLexersym.Char_CtlCharNotWS,    # 006    0x06
        LPGLexersym.Char_CtlCharNotWS,    # 007    0x07
        LPGLexersym.Char_CtlCharNotWS,    # 008    0x08
        LPGLexersym.Char_HT,              # 009    0x09
        LPGLexersym.Char_LF,              # 010    0x0A
        LPGLexersym.Char_CtlCharNotWS,    # 011    0x0B
        LPGLexersym.Char_FF,              # 012    0x0C
        LPGLexersym.Char_CR,              # 013    0x0D
        LPGLexersym.Char_CtlCharNotWS,    # 014    0x0E
        LPGLexersym.Char_CtlCharNotWS,    # 015    0x0F
        LPGLexersym.Char_CtlCharNotWS,    # 016    0x10
        LPGLexersym.Char_CtlCharNotWS,    # 017    0x11
        LPGLexersym.Char_CtlCharNotWS,    # 018    0x12
        LPGLexersym.Char_CtlCharNotWS,    # 019    0x13
        LPGLexersym.Char_CtlCharNotWS,    # 020    0x14
        LPGLexersym.Char_CtlCharNotWS,    # 021    0x15
        LPGLexersym.Char_CtlCharNotWS,    # 022    0x16
        LPGLexersym.Char_CtlCharNotWS,    # 023    0x17
        LPGLexersym.Char_CtlCharNotWS,    # 024    0x18
        LPGLexersym.Char_CtlCharNotWS,    # 025    0x19
        LPGLexersym.Char_CtlCharNotWS,    # 026    0x1A
        LPGLexersym.Char_CtlCharNotWS,    # 027    0x1B
        LPGLexersym.Char_CtlCharNotWS,    # 028    0x1C
        LPGLexersym.Char_CtlCharNotWS,    # 029    0x1D
        LPGLexersym.Char_CtlCharNotWS,    # 030    0x1E
        LPGLexersym.Char_CtlCharNotWS,    # 031    0x1F
        LPGLexersym.Char_Space,           # 032    0x20
        LPGLexersym.Char_Exclamation,     # 033    0x21
        LPGLexersym.Char_DoubleQuote,     # 034    0x22
        LPGLexersym.Char_Sharp,           # 035    0x23
        LPGLexersym.Char_DollarSign,      # 036    0x24
        LPGLexersym.Char_Percent,         # 037    0x25
        LPGLexersym.Char_Ampersand,       # 038    0x26
        LPGLexersym.Char_SingleQuote,     # 039    0x27
        LPGLexersym.Char_LeftParen,       # 040    0x28
        LPGLexersym.Char_RightParen,      # 041    0x29
        LPGLexersym.Char_Star,            # 042    0x2A
        LPGLexersym.Char_Plus,            # 043    0x2B
        LPGLexersym.Char_Comma,           # 044    0x2C
        LPGLexersym.Char_Minus,           # 045    0x2D
        LPGLexersym.Char_Dot,             # 046    0x2E
        LPGLexersym.Char_Slash,           # 047    0x2F
        LPGLexersym.Char_0,               # 048    0x30
        LPGLexersym.Char_1,               # 049    0x31
        LPGLexersym.Char_2,               # 050    0x32
        LPGLexersym.Char_3,               # 051    0x33
        LPGLexersym.Char_4,               # 052    0x34
        LPGLexersym.Char_5,               # 053    0x35
        LPGLexersym.Char_6,               # 054    0x36
        LPGLexersym.Char_7,               # 055    0x37
        LPGLexersym.Char_8,               # 056    0x38
        LPGLexersym.Char_9,               # 057    0x39
        LPGLexersym.Char_Colon,           # 058    0x3A
        LPGLexersym.Char_SemiColon,       # 059    0x3B
        LPGLexersym.Char_LessThan,        # 060    0x3C
        LPGLexersym.Char_Equal,           # 061    0x3D
        LPGLexersym.Char_GreaterThan,     # 062    0x3E
        LPGLexersym.Char_QuestionMark,    # 063    0x3F
        LPGLexersym.Char_AtSign,          # 064    0x40
        LPGLexersym.Char_A,               # 065    0x41
        LPGLexersym.Char_B,               # 066    0x42
        LPGLexersym.Char_C,               # 067    0x43
        LPGLexersym.Char_D,               # 068    0x44
        LPGLexersym.Char_E,               # 069    0x45
        LPGLexersym.Char_F,               # 070    0x46
        LPGLexersym.Char_G,               # 071    0x47
        LPGLexersym.Char_H,               # 072    0x48
        LPGLexersym.Char_I,               # 073    0x49
        LPGLexersym.Char_J,               # 074    0x4A
        LPGLexersym.Char_K,               # 075    0x4B
        LPGLexersym.Char_L,               # 076    0x4C
        LPGLexersym.Char_M,               # 077    0x4D
        LPGLexersym.Char_N,               # 078    0x4E
        LPGLexersym.Char_O,               # 079    0x4F
        LPGLexersym.Char_P,               # 080    0x50
        LPGLexersym.Char_Q,               # 081    0x51
        LPGLexersym.Char_R,               # 082    0x52
        LPGLexersym.Char_S,               # 083    0x53
        LPGLexersym.Char_T,               # 084    0x54
        LPGLexersym.Char_U,               # 085    0x55
        LPGLexersym.Char_V,               # 086    0x56
        LPGLexersym.Char_W,               # 087    0x57
        LPGLexersym.Char_X,               # 088    0x58
        LPGLexersym.Char_Y,               # 089    0x59
        LPGLexersym.Char_Z,               # 090    0x5A
        LPGLexersym.Char_LeftBracket,     # 091    0x5B
        LPGLexersym.Char_BackSlash,       # 092    0x5C
        LPGLexersym.Char_RightBracket,    # 093    0x5D
        LPGLexersym.Char_Caret,           # 094    0x5E
        LPGLexersym.Char__,               # 095    0x5F
        LPGLexersym.Char_BackQuote,       # 096    0x60
        LPGLexersym.Char_a,               # 097    0x61
        LPGLexersym.Char_b,               # 098    0x62
        LPGLexersym.Char_c,               # 099    0x63
        LPGLexersym.Char_d,               # 100    0x64
        LPGLexersym.Char_e,               # 101    0x65
        LPGLexersym.Char_f,               # 102    0x66
        LPGLexersym.Char_g,               # 103    0x67
        LPGLexersym.Char_h,               # 104    0x68
        LPGLexersym.Char_i,               # 105    0x69
        LPGLexersym.Char_j,               # 106    0x6A
        LPGLexersym.Char_k,               # 107    0x6B
        LPGLexersym.Char_l,               # 108    0x6C
        LPGLexersym.Char_m,               # 109    0x6D
        LPGLexersym.Char_n,               # 110    0x6E
        LPGLexersym.Char_o,               # 111    0x6F
        LPGLexersym.Char_p,               # 112    0x70
        LPGLexersym.Char_q,               # 113    0x71
        LPGLexersym.Char_r,               # 114    0x72
        LPGLexersym.Char_s,               # 115    0x73
        LPGLexersym.Char_t,               # 116    0x74
        LPGLexersym.Char_u,               # 117    0x75
        LPGLexersym.Char_v,               # 118    0x76
        LPGLexersym.Char_w,               # 119    0x77
        LPGLexersym.Char_x,               # 120    0x78
        LPGLexersym.Char_y,               # 121    0x79
        LPGLexersym.Char_z,               # 122    0x7A
        LPGLexersym.Char_LeftBrace,       # 123    0x7B
        LPGLexersym.Char_VerticalBar,     # 124    0x7C
        LPGLexersym.Char_RightBrace,      # 125    0x7D
        LPGLexersym.Char_Tilde,           # 126    0x7E

        LPGLexersym.Char_AfterASCII,      # for all chars in range 128..65534
        LPGLexersym.Char_EOF              # for '\uffff' or 65535 
    ]
            
    def getKind(self,i: int) ->int :  # Classify character at ith location
    
        c = ( 0xffff if i >= self.getStreamLength() else  self.getIntValue(i))
        return (   LPGLexerLpgLexStream.tokenKind[c] if c < 128 # ASCII Character
                   else  (LPGLexersym.Char_EOF if c == 0xffff  else 
                           LPGLexersym.Char_AfterASCII) )
    
    def orderedExportedSymbols(self) -> list: 
        return LPGParsersym.orderedTerminalSymbols 

    def __init__(self, fileName: str, inputChars: str= None, tab: int= None) :
        super().__init__(fileName, inputChars, tab)
     
    

