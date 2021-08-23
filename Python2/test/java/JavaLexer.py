
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


    ##line 104 "LexerTemplateF.gi

from lpg2  import  RuleAction, ParseTable, LexParser, ILexStream, IPrsStream, Monitor,LpgLexStream
from JavaLexerprs  import  JavaLexerprs 
from JavaLexersym  import  JavaLexersym  
from JavaKWLexer  import  JavaKWLexer 

    ##line 2 "LexerBasicMapF.gi

from JavaParsersym import  JavaParsersym  

    ##line 114 "LexerTemplateF.gi

class JavaLexer (RuleAction):

    prs  =  JavaLexerprs()
    def getParseTable(self) :
        return JavaLexer.prs 

    def getParser(self)  :  return self.lexParser 

    def getToken(self, i)  :
        return self.lexParser.getToken(i) 

    def getRhsFirstTokenIndex(self, i) : 
        return self.lexParser.getFirstToken(i) 

    def getRhsLastTokenIndex(self, i)  :
        return self.lexParser.getLastToken(i) 

    def getLeftSpan(self) :
        return self.lexParser.getToken(1) 

    def getRightSpan(self)  : 
        return self.lexParser.getLastToken() 

    def resetKeywordLexer(self) : 
    
        if not self.kwLexer:
           self.kwLexer =  JavaKWLexer(self.lexStream.getInputChars(), JavaParsersym.TK_IDENTIFIER)
        self.kwLexer.setInputChars(self.lexStream.getInputChars())
    
    def reset(self, filename ,  tab = 4, input_chars = None) : 
    
        self.lexStream =  JavaLexerLpgLexStream(filename,input_chars, tab)
        self.lexParser.reset(self.lexStream, JavaLexer.prs,  self)
        self.resetKeywordLexer()
    
    
    def ruleAction(self,ruleNumber) :
        act = self.__rule_action[ruleNumber]
        if act:
            act() 

    def __init__(self, filename,  tab =  4 ,input_chars  = None):
    
        
        self.__rule_action = [None]* (352 + 2)
        self.kwLexer = None
        self.printTokens  =False
        self.lexParser  =  LexParser()
     
        self.initRuleAction()
        self.lexStream =  JavaLexerLpgLexStream(filename,input_chars, tab)
        self.lexParser.reset(  self.lexStream, JavaLexer.prs,  self)
        self.resetKeywordLexer()
    

    def getILexStream(self): 
        return  self.lexStream 

    def initializeLexer(self,prsStream ,  start_offset , end_offset ) :  
    
        if self.lexStream.getInputChars() is  None:
            raise  ValueError("LexStream was not initialized")
        self.lexStream.setPrsStream(prsStream)
        prsStream.makeToken(start_offset, end_offset, 0) # Token list must start with a bad token
    
    def addEOF(self,prsStream , end_offset  ) : 
    
        prsStream.makeToken(end_offset, end_offset, JavaParsersym.TK_EOF_TOKEN) # and end with the end of file token
        prsStream.setStreamLength(prsStream.getSize())
    

    def lexerWithPosition(self,prsStream, start_offset , end_offset, monitor = None) : 
    
        if start_offset <= 1:
            self.initializeLexer(prsStream, 0, -1)
        else :
            self.initializeLexer(prsStream, start_offset - 1, start_offset - 1)

        self.lexParser.parseCharacters(start_offset, end_offset,monitor)

        self.addEOF(prsStream, ( self.lexStream.getStreamIndex() if end_offset >= self.lexStream.getStreamIndex() else  end_offset + 1))
    
    def lexer(self,prsStream,  monitor = None) : 
    
        self.initializeLexer(prsStream, 0, -1)
        self.lexParser.parseCharactersWhitMonitor(monitor)
        self.addEOF(prsStream, self.lexStream.getStreamIndex())
    
    '''/**
     * If a parse stream was not passed to self Lexical analyser then we
     * simply report a lexical error. Otherwise, we produce a bad token.
     */'''
    def reportLexicalError(self, startLoc,  endLoc):  
        prs_stream = self.lexStream.getIPrsStream()
        if (not prs_stream):
            self.lexStream.reportLexicalError(startLoc, endLoc)
        else: 
            #
            # Remove any token that may have been processed that fall in the
            # range of the lexical error... then add one error token that spans
            # the error range.
            #
            i = prs_stream.getSize() - 1
            while  i > 0 : 
                if prs_stream.getStartOffset(i) >= startLoc:
                     prs_stream.removeLastToken()
                else:
                     break
                i-=1
            
            prs_stream.makeToken(startLoc, endLoc, 0) # add an error token to the self.prsStream
                
    

    ##line 164 "LexerBasicMapF.gi


    '''#
    # The Lexer contains an array of characters as the input stream to be parsed.
    # There are methods to retrieve and classify characters.
    # The lexparser "token" is implemented simply as the index of the next character in the array.
    # The Lexer : the abstract class LpgLexStream with an implementation of the abstract
    # method getKind.  The template defines the Lexer class and the lexer() method.
    # A driver creates the action class, "Lexer", passing an Option object to the constructor.
    #'''


    ECLIPSE_TAB_VALUE = 4

    def getKeywordKinds(self) :  

        if  self.kwLexer is None:
            raise ValueError("please initilize kwLexer")
        
        return self.kwLexer.getKeywordKinds() 
    
    def makeToken1(self,left_token,right_token, kind) :
    
        self.lexStream.makeToken(left_token, right_token, kind)
    
    
    def makeToken(self, arg0, arg1= None, arg2 = None) :
    
        if arg1 is not None and arg2 is not None:
            self.makeToken1(arg0,arg1,arg2)
            return 
        
        startOffset  = self.getLeftSpan()
        endOffset = self.getRightSpan()
        self.lexStream.makeToken(startOffset, endOffset, arg0)
        if self.printTokens: 
           self.printValue(startOffset, endOffset)
    

    def makeComment(self,kind) :
    
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
    def checkForKeyWord(self, defaultKind=None) : 
    
        if defaultKind is None:
            self.checkForKeyWord1()
            return
       
        if self.kwLexer is None:
            raise ValueError("please initilize kwLexer")
        
        startOffset =  self.getLeftSpan()
        endOffset =  self.getRightSpan()
        kwKind =  self.kwLexer.lexer(startOffset, endOffset)
        if kwKind == JavaParsersym.TK_IDENTIFIER:
           kwKind = defaultKind
        self.lexStream.makeToken(startOffset, endOffset, kwKind)
        if self.printTokens: 
           self.printValue(startOffset, endOffset)
    
    
    def printValue(self, startOffset, endOffset) : 
    
         s = self.lexStream.getInputChars()[startOffset:endOffset  + 1]
         print s,
    

  

    ##line 232 "LexerTemplateF.gi

    def initRuleAction(self) : 


        #
        # Rule 1:  Token ::= Identifier
        #
         def Act1():
                self.checkForKeyWord()
      
         self.__rule_action[1] = Act1

    
        #
        # Rule 2:  Token ::= " SLBody "
        #
         def Act2():
                self.makeToken(JavaParsersym.TK_StringLiteral)
      
         self.__rule_action[2] = Act2

    
        #
        # Rule 3:  Token ::= ' NotSQ '
        #
         def Act3():
                self.makeToken(JavaParsersym.TK_CharacterLiteral)
      
         self.__rule_action[3] = Act3

    
        #
        # Rule 4:  Token ::= IntegerLiteral
        #
         def Act4():
                self.makeToken(JavaParsersym.TK_IntegerLiteral)
      
         self.__rule_action[4] = Act4

    
        #
        # Rule 5:  Token ::= FloatingPointLiteral
        #
         def Act5():
                self.makeToken(JavaParsersym.TK_FloatingPointLiteral)
      
         self.__rule_action[5] = Act5

    
        #
        # Rule 6:  Token ::= DoubleLiteral
        #
         def Act6():
                self.makeToken(JavaParsersym.TK_DoubleLiteral)
      
         self.__rule_action[6] = Act6

    
        #
        # Rule 7:  Token ::= / * Inside Stars /
        #
         def Act7():
                self.skipToken()
      
         self.__rule_action[7] = Act7

    
        #
        # Rule 8:  Token ::= SLC
        #
         def Act8():
                self.skipToken()
      
         self.__rule_action[8] = Act8

    
        #
        # Rule 9:  Token ::= WS
        #
         def Act9():
                self.skipToken()
      
         self.__rule_action[9] = Act9

    
        #
        # Rule 10:  Token ::= +
        #
         def Act10():
                self.makeToken(JavaParsersym.TK_PLUS)
      
         self.__rule_action[10] = Act10

    
        #
        # Rule 11:  Token ::= -
        #
         def Act11():
                self.makeToken(JavaParsersym.TK_MINUS)
      
         self.__rule_action[11] = Act11

    
        #
        # Rule 12:  Token ::= *
        #
         def Act12():
                self.makeToken(JavaParsersym.TK_MULTIPLY)
      
         self.__rule_action[12] = Act12

    
        #
        # Rule 13:  Token ::= /
        #
         def Act13():
                self.makeToken(JavaParsersym.TK_DIVIDE)
      
         self.__rule_action[13] = Act13

    
        #
        # Rule 14:  Token ::= (
        #
         def Act14():
                self.makeToken(JavaParsersym.TK_LPAREN)
      
         self.__rule_action[14] = Act14

    
        #
        # Rule 15:  Token ::= )
        #
         def Act15():
                self.makeToken(JavaParsersym.TK_RPAREN)
      
         self.__rule_action[15] = Act15

    
        #
        # Rule 16:  Token ::= =
        #
         def Act16():
                self.makeToken(JavaParsersym.TK_EQUAL)
      
         self.__rule_action[16] = Act16

    
        #
        # Rule 17:  Token ::= ,
        #
         def Act17():
                self.makeToken(JavaParsersym.TK_COMMA)
      
         self.__rule_action[17] = Act17

    
        #
        # Rule 18:  Token ::= :
        #
         def Act18():
                self.makeToken(JavaParsersym.TK_COLON)
      
         self.__rule_action[18] = Act18

    
        #
        # Rule 19:  Token ::= ;
        #
         def Act19():
                self.makeToken(JavaParsersym.TK_SEMICOLON)
      
         self.__rule_action[19] = Act19

    
        #
        # Rule 20:  Token ::= ^
        #
         def Act20():
                self.makeToken(JavaParsersym.TK_XOR)
      
         self.__rule_action[20] = Act20

    
        #
        # Rule 21:  Token ::= %
        #
         def Act21():
                self.makeToken(JavaParsersym.TK_REMAINDER)
      
         self.__rule_action[21] = Act21

    
        #
        # Rule 22:  Token ::= ~
        #
         def Act22():
                self.makeToken(JavaParsersym.TK_TWIDDLE)
      
         self.__rule_action[22] = Act22

    
        #
        # Rule 23:  Token ::= |
        #
         def Act23():
                self.makeToken(JavaParsersym.TK_OR)
      
         self.__rule_action[23] = Act23

    
        #
        # Rule 24:  Token ::= &
        #
         def Act24():
                self.makeToken(JavaParsersym.TK_AND)
      
         self.__rule_action[24] = Act24

    
        #
        # Rule 25:  Token ::= <
        #
         def Act25():
                self.makeToken(JavaParsersym.TK_LESS)
      
         self.__rule_action[25] = Act25

    
        #
        # Rule 26:  Token ::= >
        #
         def Act26():
                self.makeToken(JavaParsersym.TK_GREATER)
      
         self.__rule_action[26] = Act26

    
        #
        # Rule 27:  Token ::= .
        #
         def Act27():
                self.makeToken(JavaParsersym.TK_DOT)
      
         self.__rule_action[27] = Act27

    
        #
        # Rule 28:  Token ::= !
        #
         def Act28():
                self.makeToken(JavaParsersym.TK_NOT)
      
         self.__rule_action[28] = Act28

    
        #
        # Rule 29:  Token ::= [
        #
         def Act29():
                self.makeToken(JavaParsersym.TK_LBRACKET)
      
         self.__rule_action[29] = Act29

    
        #
        # Rule 30:  Token ::= ]
        #
         def Act30():
                self.makeToken(JavaParsersym.TK_RBRACKET)
      
         self.__rule_action[30] = Act30

    
        #
        # Rule 31:  Token ::= {
        #
         def Act31():
                self.makeToken(JavaParsersym.TK_LBRACE)
      
         self.__rule_action[31] = Act31

    
        #
        # Rule 32:  Token ::= }
        #
         def Act32():
                self.makeToken(JavaParsersym.TK_RBRACE)
      
         self.__rule_action[32] = Act32

    
        #
        # Rule 33:  Token ::= ?
        #
         def Act33():
                self.makeToken(JavaParsersym.TK_QUESTION)
      
         self.__rule_action[33] = Act33

    
        #
        # Rule 34:  Token ::= @
        #
         def Act34():
                self.makeToken(JavaParsersym.TK_AT)
      
         self.__rule_action[34] = Act34

    
        #
        # Rule 35:  Token ::= + +
        #
         def Act35():
                self.makeToken(JavaParsersym.TK_PLUS_PLUS)
      
         self.__rule_action[35] = Act35

    
        #
        # Rule 36:  Token ::= - -
        #
         def Act36():
                self.makeToken(JavaParsersym.TK_MINUS_MINUS)
      
         self.__rule_action[36] = Act36

    
        #
        # Rule 37:  Token ::= = =
        #
         def Act37():
                self.makeToken(JavaParsersym.TK_EQUAL_EQUAL)
      
         self.__rule_action[37] = Act37

    
        #
        # Rule 38:  Token ::= < =
        #
         def Act38():
                self.makeToken(JavaParsersym.TK_LESS_EQUAL)
      
         self.__rule_action[38] = Act38

    
        #
        # Rule 39:  Token ::= ! =
        #
         def Act39():
                self.makeToken(JavaParsersym.TK_NOT_EQUAL)
      
         self.__rule_action[39] = Act39

    
        #
        # Rule 40:  Token ::= < <
        #
         def Act40():
                self.makeToken(JavaParsersym.TK_LEFT_SHIFT)
      
         self.__rule_action[40] = Act40

    
        #
        # Rule 41:  Token ::= + =
        #
         def Act41():
                self.makeToken(JavaParsersym.TK_PLUS_EQUAL)
      
         self.__rule_action[41] = Act41

    
        #
        # Rule 42:  Token ::= - =
        #
         def Act42():
                self.makeToken(JavaParsersym.TK_MINUS_EQUAL)
      
         self.__rule_action[42] = Act42

    
        #
        # Rule 43:  Token ::= * =
        #
         def Act43():
                self.makeToken(JavaParsersym.TK_MULTIPLY_EQUAL)
      
         self.__rule_action[43] = Act43

    
        #
        # Rule 44:  Token ::= / =
        #
         def Act44():
                self.makeToken(JavaParsersym.TK_DIVIDE_EQUAL)
      
         self.__rule_action[44] = Act44

    
        #
        # Rule 45:  Token ::= & =
        #
         def Act45():
                self.makeToken(JavaParsersym.TK_AND_EQUAL)
      
         self.__rule_action[45] = Act45

    
        #
        # Rule 46:  Token ::= | =
        #
         def Act46():
                self.makeToken(JavaParsersym.TK_OR_EQUAL)
      
         self.__rule_action[46] = Act46

    
        #
        # Rule 47:  Token ::= ^ =
        #
         def Act47():
                self.makeToken(JavaParsersym.TK_XOR_EQUAL)
      
         self.__rule_action[47] = Act47

    
        #
        # Rule 48:  Token ::= % =
        #
         def Act48():
                self.makeToken(JavaParsersym.TK_REMAINDER_EQUAL)
      
         self.__rule_action[48] = Act48

    
        #
        # Rule 49:  Token ::= < < =
        #
         def Act49():
                self.makeToken(JavaParsersym.TK_LEFT_SHIFT_EQUAL)
      
         self.__rule_action[49] = Act49

    
        #
        # Rule 50:  Token ::= | |
        #
         def Act50():
                self.makeToken(JavaParsersym.TK_OR_OR)
      
         self.__rule_action[50] = Act50

    
        #
        # Rule 51:  Token ::= & &
        #
         def Act51():
                self.makeToken(JavaParsersym.TK_AND_AND)
      
         self.__rule_action[51] = Act51

    
        #
        # Rule 52:  Token ::= . . .
        #
         def Act52():
                self.makeToken(JavaParsersym.TK_ELLIPSIS)
      
         self.__rule_action[52] = Act52

    
    ##line 236 "LexerTemplateF.gi

    


    ##line 7 "LexerBasicMapF.gi
 
class  JavaLexerLpgLexStream(LpgLexStream):
    
    tokenKind  =[
        JavaLexersym.Char_CtlCharNotWS,    # 000    0x00
        JavaLexersym.Char_CtlCharNotWS,    # 001    0x01
        JavaLexersym.Char_CtlCharNotWS,    # 002    0x02
        JavaLexersym.Char_CtlCharNotWS,    # 003    0x03
        JavaLexersym.Char_CtlCharNotWS,    # 004    0x04
        JavaLexersym.Char_CtlCharNotWS,    # 005    0x05
        JavaLexersym.Char_CtlCharNotWS,    # 006    0x06
        JavaLexersym.Char_CtlCharNotWS,    # 007    0x07
        JavaLexersym.Char_CtlCharNotWS,    # 008    0x08
        JavaLexersym.Char_HT,              # 009    0x09
        JavaLexersym.Char_LF,              # 010    0x0A
        JavaLexersym.Char_CtlCharNotWS,    # 011    0x0B
        JavaLexersym.Char_FF,              # 012    0x0C
        JavaLexersym.Char_CR,              # 013    0x0D
        JavaLexersym.Char_CtlCharNotWS,    # 014    0x0E
        JavaLexersym.Char_CtlCharNotWS,    # 015    0x0F
        JavaLexersym.Char_CtlCharNotWS,    # 016    0x10
        JavaLexersym.Char_CtlCharNotWS,    # 017    0x11
        JavaLexersym.Char_CtlCharNotWS,    # 018    0x12
        JavaLexersym.Char_CtlCharNotWS,    # 019    0x13
        JavaLexersym.Char_CtlCharNotWS,    # 020    0x14
        JavaLexersym.Char_CtlCharNotWS,    # 021    0x15
        JavaLexersym.Char_CtlCharNotWS,    # 022    0x16
        JavaLexersym.Char_CtlCharNotWS,    # 023    0x17
        JavaLexersym.Char_CtlCharNotWS,    # 024    0x18
        JavaLexersym.Char_CtlCharNotWS,    # 025    0x19
        JavaLexersym.Char_CtlCharNotWS,    # 026    0x1A
        JavaLexersym.Char_CtlCharNotWS,    # 027    0x1B
        JavaLexersym.Char_CtlCharNotWS,    # 028    0x1C
        JavaLexersym.Char_CtlCharNotWS,    # 029    0x1D
        JavaLexersym.Char_CtlCharNotWS,    # 030    0x1E
        JavaLexersym.Char_CtlCharNotWS,    # 031    0x1F
        JavaLexersym.Char_Space,           # 032    0x20
        JavaLexersym.Char_Exclamation,     # 033    0x21
        JavaLexersym.Char_DoubleQuote,     # 034    0x22
        JavaLexersym.Char_Sharp,           # 035    0x23
        JavaLexersym.Char_DollarSign,      # 036    0x24
        JavaLexersym.Char_Percent,         # 037    0x25
        JavaLexersym.Char_Ampersand,       # 038    0x26
        JavaLexersym.Char_SingleQuote,     # 039    0x27
        JavaLexersym.Char_LeftParen,       # 040    0x28
        JavaLexersym.Char_RightParen,      # 041    0x29
        JavaLexersym.Char_Star,            # 042    0x2A
        JavaLexersym.Char_Plus,            # 043    0x2B
        JavaLexersym.Char_Comma,           # 044    0x2C
        JavaLexersym.Char_Minus,           # 045    0x2D
        JavaLexersym.Char_Dot,             # 046    0x2E
        JavaLexersym.Char_Slash,           # 047    0x2F
        JavaLexersym.Char_0,               # 048    0x30
        JavaLexersym.Char_1,               # 049    0x31
        JavaLexersym.Char_2,               # 050    0x32
        JavaLexersym.Char_3,               # 051    0x33
        JavaLexersym.Char_4,               # 052    0x34
        JavaLexersym.Char_5,               # 053    0x35
        JavaLexersym.Char_6,               # 054    0x36
        JavaLexersym.Char_7,               # 055    0x37
        JavaLexersym.Char_8,               # 056    0x38
        JavaLexersym.Char_9,               # 057    0x39
        JavaLexersym.Char_Colon,           # 058    0x3A
        JavaLexersym.Char_SemiColon,       # 059    0x3B
        JavaLexersym.Char_LessThan,        # 060    0x3C
        JavaLexersym.Char_Equal,           # 061    0x3D
        JavaLexersym.Char_GreaterThan,     # 062    0x3E
        JavaLexersym.Char_QuestionMark,    # 063    0x3F
        JavaLexersym.Char_AtSign,          # 064    0x40
        JavaLexersym.Char_A,               # 065    0x41
        JavaLexersym.Char_B,               # 066    0x42
        JavaLexersym.Char_C,               # 067    0x43
        JavaLexersym.Char_D,               # 068    0x44
        JavaLexersym.Char_E,               # 069    0x45
        JavaLexersym.Char_F,               # 070    0x46
        JavaLexersym.Char_G,               # 071    0x47
        JavaLexersym.Char_H,               # 072    0x48
        JavaLexersym.Char_I,               # 073    0x49
        JavaLexersym.Char_J,               # 074    0x4A
        JavaLexersym.Char_K,               # 075    0x4B
        JavaLexersym.Char_L,               # 076    0x4C
        JavaLexersym.Char_M,               # 077    0x4D
        JavaLexersym.Char_N,               # 078    0x4E
        JavaLexersym.Char_O,               # 079    0x4F
        JavaLexersym.Char_P,               # 080    0x50
        JavaLexersym.Char_Q,               # 081    0x51
        JavaLexersym.Char_R,               # 082    0x52
        JavaLexersym.Char_S,               # 083    0x53
        JavaLexersym.Char_T,               # 084    0x54
        JavaLexersym.Char_U,               # 085    0x55
        JavaLexersym.Char_V,               # 086    0x56
        JavaLexersym.Char_W,               # 087    0x57
        JavaLexersym.Char_X,               # 088    0x58
        JavaLexersym.Char_Y,               # 089    0x59
        JavaLexersym.Char_Z,               # 090    0x5A
        JavaLexersym.Char_LeftBracket,     # 091    0x5B
        JavaLexersym.Char_BackSlash,       # 092    0x5C
        JavaLexersym.Char_RightBracket,    # 093    0x5D
        JavaLexersym.Char_Caret,           # 094    0x5E
        JavaLexersym.Char__,               # 095    0x5F
        JavaLexersym.Char_BackQuote,       # 096    0x60
        JavaLexersym.Char_a,               # 097    0x61
        JavaLexersym.Char_b,               # 098    0x62
        JavaLexersym.Char_c,               # 099    0x63
        JavaLexersym.Char_d,               # 100    0x64
        JavaLexersym.Char_e,               # 101    0x65
        JavaLexersym.Char_f,               # 102    0x66
        JavaLexersym.Char_g,               # 103    0x67
        JavaLexersym.Char_h,               # 104    0x68
        JavaLexersym.Char_i,               # 105    0x69
        JavaLexersym.Char_j,               # 106    0x6A
        JavaLexersym.Char_k,               # 107    0x6B
        JavaLexersym.Char_l,               # 108    0x6C
        JavaLexersym.Char_m,               # 109    0x6D
        JavaLexersym.Char_n,               # 110    0x6E
        JavaLexersym.Char_o,               # 111    0x6F
        JavaLexersym.Char_p,               # 112    0x70
        JavaLexersym.Char_q,               # 113    0x71
        JavaLexersym.Char_r,               # 114    0x72
        JavaLexersym.Char_s,               # 115    0x73
        JavaLexersym.Char_t,               # 116    0x74
        JavaLexersym.Char_u,               # 117    0x75
        JavaLexersym.Char_v,               # 118    0x76
        JavaLexersym.Char_w,               # 119    0x77
        JavaLexersym.Char_x,               # 120    0x78
        JavaLexersym.Char_y,               # 121    0x79
        JavaLexersym.Char_z,               # 122    0x7A
        JavaLexersym.Char_LeftBrace,       # 123    0x7B
        JavaLexersym.Char_VerticalBar,     # 124    0x7C
        JavaLexersym.Char_RightBrace,      # 125    0x7D
        JavaLexersym.Char_Tilde,           # 126    0x7E

        JavaLexersym.Char_AfterASCII,      # for all chars in range 128..65534
        JavaLexersym.Char_EOF              # for '\uffff' or 65535 
    ]
            
    def getKind(self,i) :  # Classify character at ith location
    
        c = ( 0xffff if i >= self.getStreamLength() else  self.getIntValue(i))
        return (   JavaLexerLpgLexStream.tokenKind[c] if c < 128 # ASCII Character
                   else  (JavaLexersym.Char_EOF if c == 0xffff  else 
                           JavaLexersym.Char_AfterASCII) )
    
    def orderedExportedSymbols(self) : 
        return JavaParsersym.orderedTerminalSymbols 

    def __init__(self, fileName, inputChars= None, tab= None) :
        super(JavaLexerLpgLexStream, self).__init__(fileName, inputChars, tab)
     
    

