
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


    ##line 24 "KeywordTemplateF.gi

from JavaKWLexerprs    import  JavaKWLexerprs  
from JavaKWLexersym    import  JavaKWLexersym  
from JavaParsersym    import  JavaParsersym  

    ##line 69 "KeywordTemplateF.gi

class JavaKWLexer(JavaKWLexerprs):

    def getKeywordKinds(self):  return self.keywordKind 

    def lexer(self,curtok , lasttok )  :

        current_kind = JavaKWLexer.getKind(ord(self.inputChars[curtok]))
                
        act = self.tAction(self.START_STATE, current_kind)
        while act > self.NUM_RULES and act < self.ACCEPT_ACTION:
            curtok+=1
            current_kind = ( JavaKWLexersym.Char_EOF if curtok > lasttok else 
                            JavaKWLexer.getKind(ord(self.inputChars[curtok])))
            act = self.tAction(act, current_kind)

        if act > self.ERROR_ACTION:
        
            curtok += 1
            act -= self.ERROR_ACTION
        return self.keywordKind[0 if (act == self.ERROR_ACTION or curtok <= lasttok) else act]

    def setInputChars(self, inputChars):   
        self.inputChars = inputChars 


    ##line 10 "KWLexerMapF.gi

    tokenKind=  [0]*128
   
    tokenKind[ord('$'[0])] = JavaKWLexersym.Char_DollarSign
    tokenKind[ord('%'[0])] = JavaKWLexersym.Char_Percent
    tokenKind[ord('_'[0])] = JavaKWLexersym.Char__

    tokenKind[ord('a'[0])] = JavaKWLexersym.Char_a
    tokenKind[ord('b'[0])] = JavaKWLexersym.Char_b
    tokenKind[ord('c'[0])] = JavaKWLexersym.Char_c
    tokenKind[ord('d'[0])] = JavaKWLexersym.Char_d
    tokenKind[ord('e'[0])] = JavaKWLexersym.Char_e
    tokenKind[ord('f'[0])] = JavaKWLexersym.Char_f
    tokenKind[ord('g'[0])] = JavaKWLexersym.Char_g
    tokenKind[ord('h'[0])] = JavaKWLexersym.Char_h
    tokenKind[ord('i'[0])] = JavaKWLexersym.Char_i
    tokenKind[ord('j'[0])] = JavaKWLexersym.Char_j
    tokenKind[ord('k'[0])] = JavaKWLexersym.Char_k
    tokenKind[ord('l'[0])] = JavaKWLexersym.Char_l
    tokenKind[ord('m'[0])] = JavaKWLexersym.Char_m
    tokenKind[ord('n'[0])] = JavaKWLexersym.Char_n
    tokenKind[ord('o'[0])] = JavaKWLexersym.Char_o
    tokenKind[ord('p'[0])] = JavaKWLexersym.Char_p
    tokenKind[ord('q'[0])] = JavaKWLexersym.Char_q
    tokenKind[ord('r'[0])] = JavaKWLexersym.Char_r
    tokenKind[ord('s'[0])] = JavaKWLexersym.Char_s
    tokenKind[ord('t'[0])] = JavaKWLexersym.Char_t
    tokenKind[ord('u'[0])] = JavaKWLexersym.Char_u
    tokenKind[ord('v'[0])] = JavaKWLexersym.Char_v
    tokenKind[ord('w'[0])] = JavaKWLexersym.Char_w
    tokenKind[ord('x'[0])] = JavaKWLexersym.Char_x
    tokenKind[ord('y'[0])] = JavaKWLexersym.Char_y
    tokenKind[ord('z'[0])] = JavaKWLexersym.Char_z

    tokenKind[ord('A'[0])] = JavaKWLexersym.Char_A
    tokenKind[ord('B'[0])] = JavaKWLexersym.Char_B
    tokenKind[ord('C'[0])] = JavaKWLexersym.Char_C
    tokenKind[ord('D'[0])] = JavaKWLexersym.Char_D
    tokenKind[ord('E'[0])] = JavaKWLexersym.Char_E
    tokenKind[ord('F'[0])] = JavaKWLexersym.Char_F
    tokenKind[ord('G'[0])] = JavaKWLexersym.Char_G
    tokenKind[ord('H'[0])] = JavaKWLexersym.Char_H
    tokenKind[ord('I'[0])] = JavaKWLexersym.Char_I
    tokenKind[ord('J'[0])] = JavaKWLexersym.Char_J
    tokenKind[ord('K'[0])] = JavaKWLexersym.Char_K
    tokenKind[ord('L'[0])] = JavaKWLexersym.Char_L
    tokenKind[ord('M'[0])] = JavaKWLexersym.Char_M
    tokenKind[ord('N'[0])] = JavaKWLexersym.Char_N
    tokenKind[ord('O'[0])] = JavaKWLexersym.Char_O
    tokenKind[ord('P'[0])] = JavaKWLexersym.Char_P
    tokenKind[ord('Q'[0])] = JavaKWLexersym.Char_Q
    tokenKind[ord('R'[0])] = JavaKWLexersym.Char_R
    tokenKind[ord('S'[0])] = JavaKWLexersym.Char_S
    tokenKind[ord('T'[0])] = JavaKWLexersym.Char_T
    tokenKind[ord('U'[0])] = JavaKWLexersym.Char_U
    tokenKind[ord('V'[0])] = JavaKWLexersym.Char_V
    tokenKind[ord('W'[0])] = JavaKWLexersym.Char_W
    tokenKind[ord('X'[0])] = JavaKWLexersym.Char_X
    tokenKind[ord('Y'[0])] = JavaKWLexersym.Char_Y
    tokenKind[ord('Z'[0])] = JavaKWLexersym.Char_Z

    @classmethod
    def getKind(cls, c) :
        # 0 <= c < 128? 
        return JavaKWLexer.tokenKind[c] if (c & 0xFFFFFF80) == 0  else  0
    

    ##line 98 "KeywordTemplateF.gi

    def __init__(self, inputChars,  identifierKind):
        
        self.inputChars  = None
        self.keywordKind    =  [0]*(88 + 1)
        self.inputChars = inputChars
        self.keywordKind[0] = identifierKind

        #
        # Rule 1:  KeyWord ::= a b s t r a c t
        #

        self.keywordKind[1] = (JavaParsersym.TK_abstract)
      
    
        #
        # Rule 2:  KeyWord ::= a s s e r t
        #

        self.keywordKind[2] = (JavaParsersym.TK_assert)
      
    
        #
        # Rule 3:  KeyWord ::= b o o l e a n
        #

        self.keywordKind[3] = (JavaParsersym.TK_boolean)
      
    
        #
        # Rule 4:  KeyWord ::= b r e a k
        #

        self.keywordKind[4] = (JavaParsersym.TK_break)
      
    
        #
        # Rule 5:  KeyWord ::= b y t e
        #

        self.keywordKind[5] = (JavaParsersym.TK_byte)
      
    
        #
        # Rule 6:  KeyWord ::= c a s e
        #

        self.keywordKind[6] = (JavaParsersym.TK_case)
      
    
        #
        # Rule 7:  KeyWord ::= c a t c h
        #

        self.keywordKind[7] = (JavaParsersym.TK_catch)
      
    
        #
        # Rule 8:  KeyWord ::= c h a r
        #

        self.keywordKind[8] = (JavaParsersym.TK_char)
      
    
        #
        # Rule 9:  KeyWord ::= c l a s s
        #

        self.keywordKind[9] = (JavaParsersym.TK_class)
      
    
        #
        # Rule 10:  KeyWord ::= c o n s t
        #

        self.keywordKind[10] = (JavaParsersym.TK_const)
      
    
        #
        # Rule 11:  KeyWord ::= c o n t i n u e
        #

        self.keywordKind[11] = (JavaParsersym.TK_continue)
      
    
        #
        # Rule 12:  KeyWord ::= d e f a u l t
        #

        self.keywordKind[12] = (JavaParsersym.TK_default)
      
    
        #
        # Rule 13:  KeyWord ::= d o
        #

        self.keywordKind[13] = (JavaParsersym.TK_do)
      
    
        #
        # Rule 14:  KeyWord ::= d o u b l e
        #

        self.keywordKind[14] = (JavaParsersym.TK_double)
      
    
        #
        # Rule 15:  KeyWord ::= e l s e
        #

        self.keywordKind[15] = (JavaParsersym.TK_else)
      
    
        #
        # Rule 16:  KeyWord ::= e n u m
        #

        self.keywordKind[16] = (JavaParsersym.TK_enum)
      
    
        #
        # Rule 17:  KeyWord ::= e x t e n d s
        #

        self.keywordKind[17] = (JavaParsersym.TK_extends)
      
    
        #
        # Rule 18:  KeyWord ::= f a l s e
        #

        self.keywordKind[18] = (JavaParsersym.TK_false)
      
    
        #
        # Rule 19:  KeyWord ::= f i n a l
        #

        self.keywordKind[19] = (JavaParsersym.TK_final)
      
    
        #
        # Rule 20:  KeyWord ::= f i n a l l y
        #

        self.keywordKind[20] = (JavaParsersym.TK_finally)
      
    
        #
        # Rule 21:  KeyWord ::= f l o a t
        #

        self.keywordKind[21] = (JavaParsersym.TK_float)
      
    
        #
        # Rule 22:  KeyWord ::= f o r
        #

        self.keywordKind[22] = (JavaParsersym.TK_for)
      
    
        #
        # Rule 23:  KeyWord ::= g o t o
        #

        self.keywordKind[23] = (JavaParsersym.TK_goto)
      
    
        #
        # Rule 24:  KeyWord ::= i f
        #

        self.keywordKind[24] = (JavaParsersym.TK_if)
      
    
        #
        # Rule 25:  KeyWord ::= i m p l e m e n t s
        #

        self.keywordKind[25] = (JavaParsersym.TK_implements)
      
    
        #
        # Rule 26:  KeyWord ::= i m p o r t
        #

        self.keywordKind[26] = (JavaParsersym.TK_import)
      
    
        #
        # Rule 27:  KeyWord ::= i n s t a n c e o f
        #

        self.keywordKind[27] = (JavaParsersym.TK_instanceof)
      
    
        #
        # Rule 28:  KeyWord ::= i n t
        #

        self.keywordKind[28] = (JavaParsersym.TK_int)
      
    
        #
        # Rule 29:  KeyWord ::= i n t e r f a c e
        #

        self.keywordKind[29] = (JavaParsersym.TK_interface)
      
    
        #
        # Rule 30:  KeyWord ::= l o n g
        #

        self.keywordKind[30] = (JavaParsersym.TK_long)
      
    
        #
        # Rule 31:  KeyWord ::= n a t i v e
        #

        self.keywordKind[31] = (JavaParsersym.TK_native)
      
    
        #
        # Rule 32:  KeyWord ::= n e w
        #

        self.keywordKind[32] = (JavaParsersym.TK_new)
      
    
        #
        # Rule 33:  KeyWord ::= n u l l
        #

        self.keywordKind[33] = (JavaParsersym.TK_null)
      
    
        #
        # Rule 34:  KeyWord ::= p a c k a g e
        #

        self.keywordKind[34] = (JavaParsersym.TK_package)
      
    
        #
        # Rule 35:  KeyWord ::= p r i v a t e
        #

        self.keywordKind[35] = (JavaParsersym.TK_private)
      
    
        #
        # Rule 36:  KeyWord ::= p r o t e c t e d
        #

        self.keywordKind[36] = (JavaParsersym.TK_protected)
      
    
        #
        # Rule 37:  KeyWord ::= p u b l i c
        #

        self.keywordKind[37] = (JavaParsersym.TK_public)
      
    
        #
        # Rule 38:  KeyWord ::= r e t u r n
        #

        self.keywordKind[38] = (JavaParsersym.TK_return)
      
    
        #
        # Rule 39:  KeyWord ::= s h o r t
        #

        self.keywordKind[39] = (JavaParsersym.TK_short)
      
    
        #
        # Rule 40:  KeyWord ::= s t a t i c
        #

        self.keywordKind[40] = (JavaParsersym.TK_static)
      
    
        #
        # Rule 41:  KeyWord ::= s t r i c t f p
        #

        self.keywordKind[41] = (JavaParsersym.TK_strictfp)
      
    
        #
        # Rule 42:  KeyWord ::= s u p e r
        #

        self.keywordKind[42] = (JavaParsersym.TK_super)
      
    
        #
        # Rule 43:  KeyWord ::= s w i t c h
        #

        self.keywordKind[43] = (JavaParsersym.TK_switch)
      
    
        #
        # Rule 44:  KeyWord ::= s y n c h r o n i z e d
        #

        self.keywordKind[44] = (JavaParsersym.TK_synchronized)
      
    
        #
        # Rule 45:  KeyWord ::= t h i s
        #

        self.keywordKind[45] = (JavaParsersym.TK_this)
      
    
        #
        # Rule 46:  KeyWord ::= t h r o w
        #

        self.keywordKind[46] = (JavaParsersym.TK_throw)
      
    
        #
        # Rule 47:  KeyWord ::= t h r o w s
        #

        self.keywordKind[47] = (JavaParsersym.TK_throws)
      
    
        #
        # Rule 48:  KeyWord ::= t r a n s i e n t
        #

        self.keywordKind[48] = (JavaParsersym.TK_transient)
      
    
        #
        # Rule 49:  KeyWord ::= t r u e
        #

        self.keywordKind[49] = (JavaParsersym.TK_true)
      
    
        #
        # Rule 50:  KeyWord ::= t r y
        #

        self.keywordKind[50] = (JavaParsersym.TK_try)
      
    
        #
        # Rule 51:  KeyWord ::= v o i d
        #

        self.keywordKind[51] = (JavaParsersym.TK_void)
      
    
        #
        # Rule 52:  KeyWord ::= v o l a t i l e
        #

        self.keywordKind[52] = (JavaParsersym.TK_volatile)
      
    
        #
        # Rule 53:  KeyWord ::= w h i l e
        #

        self.keywordKind[53] = (JavaParsersym.TK_while)
      
    
        #
        # Rule 54:  KeyWord ::= $ bB eE gG iI nN aA cC tT iI oO nN
        #

        self.keywordKind[54] = (JavaParsersym.TK_BeginAction)
      
    
        #
        # Rule 55:  KeyWord ::= $ bB eE gG iI nN jJ aA vV aA
        #

        self.keywordKind[55] = (JavaParsersym.TK_BeginJava)
      
    
        #
        # Rule 56:  KeyWord ::= $ eE nN dD aA cC tT iI oO nN
        #

        self.keywordKind[56] = (JavaParsersym.TK_EndAction)
      
    
        #
        # Rule 57:  KeyWord ::= $ eE nN dD jJ aA vV aA
        #

        self.keywordKind[57] = (JavaParsersym.TK_EndJava)
      
    
        #
        # Rule 58:  KeyWord ::= $ nN oO aA cC tT iI oO nN
        #

        self.keywordKind[58] = (JavaParsersym.TK_NoAction)
      
    
        #
        # Rule 59:  KeyWord ::= $ nN uU lL lL aA cC tT iI oO nN
        #

        self.keywordKind[59] = (JavaParsersym.TK_NullAction)
      
    
        #
        # Rule 60:  KeyWord ::= $ bB aA dD aA cC tT iI oO nN
        #

        self.keywordKind[60] = (JavaParsersym.TK_BadAction)
      
    
    ##line 109 "KeywordTemplateF.gi

        for i in range(0, len(self.keywordKind)):
            if self.keywordKind[i] == 0:
                self.keywordKind[i] = identifierKind
        

