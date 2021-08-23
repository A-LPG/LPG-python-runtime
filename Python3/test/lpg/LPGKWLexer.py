
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


    ##line 24 "KeywordTemplateF.gi

from LPGKWLexerprs    import  LPGKWLexerprs  
from LPGKWLexersym    import  LPGKWLexersym  
from LPGParsersym    import  LPGParsersym  

    ##line 69 "KeywordTemplateF.gi

class LPGKWLexer(LPGKWLexerprs):

    def getKeywordKinds(self) ->list :  return self.keywordKind 

    def lexer(self,curtok : int, lasttok : int) -> int :

        current_kind = LPGKWLexer.getKind(ord(self.inputChars[curtok]))
                
        act = self.tAction(self.START_STATE, current_kind)
        while act > self.NUM_RULES and act < self.ACCEPT_ACTION:
            curtok+=1
            current_kind = ( LPGKWLexersym.Char_EOF if curtok > lasttok else 
                            LPGKWLexer.getKind(ord(self.inputChars[curtok])))
            act = self.tAction(act, current_kind)

        if act > self.ERROR_ACTION:
        
            curtok += 1
            act -= self.ERROR_ACTION
        return self.keywordKind[0 if (act == self.ERROR_ACTION or curtok <= lasttok) else act]

    def setInputChars(self, inputChars: str):   
        self.inputChars = inputChars 


    ##line 9 "KWLexerFoldedCaseMapF.gi

    '''#
    # Each upper case letter is mapped into its corresponding
    # lower case counterpart. For example, if an 'A' appears
    # in the input, it is mapped into LPGKWLexersym.Char_a just
    # like 'a'.
    #'''

    tokenKind: list = [0]*(128)  
   
    tokenKind[ord('$'[0])] = LPGKWLexersym.Char_DollarSign
    tokenKind[ord('%'[0])] = LPGKWLexersym.Char_Percent
    tokenKind[ord('_'[0])] = LPGKWLexersym.Char__

    tokenKind[ord('a'[0])] = LPGKWLexersym.Char_a
    tokenKind[ord('b'[0])] = LPGKWLexersym.Char_b
    tokenKind[ord('c'[0])] = LPGKWLexersym.Char_c
    tokenKind[ord('d'[0])] = LPGKWLexersym.Char_d
    tokenKind[ord('e'[0])] = LPGKWLexersym.Char_e
    tokenKind[ord('f'[0])] = LPGKWLexersym.Char_f
    tokenKind[ord('g'[0])] = LPGKWLexersym.Char_g
    tokenKind[ord('h'[0])] = LPGKWLexersym.Char_h
    tokenKind[ord('i'[0])] = LPGKWLexersym.Char_i
    tokenKind[ord('j'[0])] = LPGKWLexersym.Char_j
    tokenKind[ord('k'[0])] = LPGKWLexersym.Char_k
    tokenKind[ord('l'[0])] = LPGKWLexersym.Char_l
    tokenKind[ord('m'[0])] = LPGKWLexersym.Char_m
    tokenKind[ord('n'[0])] = LPGKWLexersym.Char_n
    tokenKind[ord('o'[0])] = LPGKWLexersym.Char_o
    tokenKind[ord('p'[0])] = LPGKWLexersym.Char_p
    tokenKind[ord('q'[0])] = LPGKWLexersym.Char_q
    tokenKind[ord('r'[0])] = LPGKWLexersym.Char_r
    tokenKind[ord('s'[0])] = LPGKWLexersym.Char_s
    tokenKind[ord('t'[0])] = LPGKWLexersym.Char_t
    tokenKind[ord('u'[0])] = LPGKWLexersym.Char_u
    tokenKind[ord('v'[0])] = LPGKWLexersym.Char_v
    tokenKind[ord('w'[0])] = LPGKWLexersym.Char_w
    tokenKind[ord('x'[0])] = LPGKWLexersym.Char_x
    tokenKind[ord('y'[0])] = LPGKWLexersym.Char_y
    tokenKind[ord('z'[0])] = LPGKWLexersym.Char_z

    tokenKind[ord('A'[0])] = LPGKWLexersym.Char_a
    tokenKind[ord('B'[0])] = LPGKWLexersym.Char_b
    tokenKind[ord('C'[0])] = LPGKWLexersym.Char_c
    tokenKind[ord('D'[0])] = LPGKWLexersym.Char_d
    tokenKind[ord('E'[0])] = LPGKWLexersym.Char_e
    tokenKind[ord('F'[0])] = LPGKWLexersym.Char_f
    tokenKind[ord('G'[0])] = LPGKWLexersym.Char_g
    tokenKind[ord('H'[0])] = LPGKWLexersym.Char_h
    tokenKind[ord('I'[0])] = LPGKWLexersym.Char_i
    tokenKind[ord('J'[0])] = LPGKWLexersym.Char_j
    tokenKind[ord('K'[0])] = LPGKWLexersym.Char_k
    tokenKind[ord('L'[0])] = LPGKWLexersym.Char_l
    tokenKind[ord('M'[0])] = LPGKWLexersym.Char_m
    tokenKind[ord('N'[0])] = LPGKWLexersym.Char_n
    tokenKind[ord('O'[0])] = LPGKWLexersym.Char_o
    tokenKind[ord('P'[0])] = LPGKWLexersym.Char_p
    tokenKind[ord('Q'[0])] = LPGKWLexersym.Char_q
    tokenKind[ord('R'[0])] = LPGKWLexersym.Char_r
    tokenKind[ord('S'[0])] = LPGKWLexersym.Char_s
    tokenKind[ord('T'[0])] = LPGKWLexersym.Char_t
    tokenKind[ord('U'[0])] = LPGKWLexersym.Char_u
    tokenKind[ord('V'[0])] = LPGKWLexersym.Char_v
    tokenKind[ord('W'[0])] = LPGKWLexersym.Char_w
    tokenKind[ord('X'[0])] = LPGKWLexersym.Char_x
    tokenKind[ord('Y'[0])] = LPGKWLexersym.Char_y
    tokenKind[ord('Z'[0])] = LPGKWLexersym.Char_z

    @classmethod
    def getKind(cls, c: int) -> int:
        return ( LPGKWLexer.tokenKind[c] if c < 128  else  0)
    

    ##line 98 "KeywordTemplateF.gi

    def __init__(self, inputChars: str,  identifierKind: int):
        super().__init__()
        self.inputChars : str = None
        self.keywordKind  : list  =  [0]*(29 + 1)
        self.inputChars = inputChars
        self.keywordKind[0] = identifierKind

        #
        # Rule 1:  Keyword ::= KeyPrefix a l i a s
        #

        self.keywordKind[1] = (LPGParsersym.TK_ALIAS_KEY)
      
    
        #
        # Rule 2:  Keyword ::= KeyPrefix a s t
        #

        self.keywordKind[2] = (LPGParsersym.TK_AST_KEY)
      
    
        #
        # Rule 3:  Keyword ::= KeyPrefix d e f i n e
        #

        self.keywordKind[3] = (LPGParsersym.TK_DEFINE_KEY)
      
    
        #
        # Rule 4:  Keyword ::= KeyPrefix d i s j o i n t p r e d e c e s s o r s e t s
        #

        self.keywordKind[4] = (LPGParsersym.TK_DISJOINTPREDECESSORSETS_KEY)
      
    
        #
        # Rule 5:  Keyword ::= KeyPrefix d r o p r u l e s
        #

        self.keywordKind[5] = (LPGParsersym.TK_DROPRULES_KEY)
      
    
        #
        # Rule 6:  Keyword ::= KeyPrefix d r o p s y m b o l s
        #

        self.keywordKind[6] = (LPGParsersym.TK_DROPSYMBOLS_KEY)
      
    
        #
        # Rule 7:  Keyword ::= KeyPrefix e m p t y
        #

        self.keywordKind[7] = (LPGParsersym.TK_EMPTY_KEY)
      
    
        #
        # Rule 8:  Keyword ::= KeyPrefix e n d
        #

        self.keywordKind[8] = (LPGParsersym.TK_END_KEY)
      
    
        #
        # Rule 9:  Keyword ::= KeyPrefix e r r o r
        #

        self.keywordKind[9] = (LPGParsersym.TK_ERROR_KEY)
      
    
        #
        # Rule 10:  Keyword ::= KeyPrefix e o l
        #

        self.keywordKind[10] = (LPGParsersym.TK_EOL_KEY)
      
    
        #
        # Rule 11:  Keyword ::= KeyPrefix e o f
        #

        self.keywordKind[11] = (LPGParsersym.TK_EOF_KEY)
      
    
        #
        # Rule 12:  Keyword ::= KeyPrefix e x p o r t
        #

        self.keywordKind[12] = (LPGParsersym.TK_EXPORT_KEY)
      
    
        #
        # Rule 13:  Keyword ::= KeyPrefix g l o b a l s
        #

        self.keywordKind[13] = (LPGParsersym.TK_GLOBALS_KEY)
      
    
        #
        # Rule 14:  Keyword ::= KeyPrefix h e a d e r s
        #

        self.keywordKind[14] = (LPGParsersym.TK_HEADERS_KEY)
      
    
        #
        # Rule 15:  Keyword ::= KeyPrefix i d e n t i f i e r
        #

        self.keywordKind[15] = (LPGParsersym.TK_IDENTIFIER_KEY)
      
    
        #
        # Rule 16:  Keyword ::= KeyPrefix i m p o r t
        #

        self.keywordKind[16] = (LPGParsersym.TK_IMPORT_KEY)
      
    
        #
        # Rule 17:  Keyword ::= KeyPrefix i n c l u d e
        #

        self.keywordKind[17] = (LPGParsersym.TK_INCLUDE_KEY)
      
    
        #
        # Rule 18:  Keyword ::= KeyPrefix k e y w o r d s
        #

        self.keywordKind[18] = (LPGParsersym.TK_KEYWORDS_KEY)
      
    
        #
        # Rule 19:  Keyword ::= KeyPrefix s o f t k e y w o r d s
        #

        self.keywordKind[19] = (LPGParsersym.TK_SOFT_KEYWORDS_KEY)
      
    
        #
        # Rule 20:  Keyword ::= KeyPrefix n a m e s
        #

        self.keywordKind[20] = (LPGParsersym.TK_NAMES_KEY)
      
    
        #
        # Rule 21:  Keyword ::= KeyPrefix n o t i c e
        #

        self.keywordKind[21] = (LPGParsersym.TK_NOTICE_KEY)
      
    
        #
        # Rule 22:  Keyword ::= KeyPrefix t e r m i n a l s
        #

        self.keywordKind[22] = (LPGParsersym.TK_TERMINALS_KEY)
      
    
        #
        # Rule 23:  Keyword ::= KeyPrefix r e c o v e r
        #

        self.keywordKind[23] = (LPGParsersym.TK_RECOVER_KEY)
      
    
        #
        # Rule 24:  Keyword ::= KeyPrefix r u l e s
        #

        self.keywordKind[24] = (LPGParsersym.TK_RULES_KEY)
      
    
        #
        # Rule 25:  Keyword ::= KeyPrefix s t a r t
        #

        self.keywordKind[25] = (LPGParsersym.TK_START_KEY)
      
    
        #
        # Rule 26:  Keyword ::= KeyPrefix t r a i l e r s
        #

        self.keywordKind[26] = (LPGParsersym.TK_TRAILERS_KEY)
      
    
        #
        # Rule 27:  Keyword ::= KeyPrefix t y p e s
        #

        self.keywordKind[27] = (LPGParsersym.TK_TYPES_KEY)
      
    
    ##line 109 "KeywordTemplateF.gi

        for i in range(0, len(self.keywordKind)):
            if self.keywordKind[i] == 0:
                self.keywordKind[i] = identifierKind
        

