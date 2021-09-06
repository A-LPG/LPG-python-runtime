
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

class JavaLexersym(object):
   Char_CtlCharNotWS : int  = 102
   Char_LF : int  = 100
   Char_CR : int  = 101
   Char_HT : int  = 37
   Char_FF : int  = 38
   Char_a : int  = 19
   Char_b : int  = 15
   Char_c : int  = 20
   Char_d : int  = 12
   Char_e : int  = 16
   Char_f : int  = 11
   Char_g : int  = 39
   Char_h : int  = 40
   Char_i : int  = 41
   Char_j : int  = 42
   Char_k : int  = 43
   Char_l : int  = 25
   Char_m : int  = 44
   Char_n : int  = 26
   Char_o : int  = 45
   Char_p : int  = 46
   Char_q : int  = 47
   Char_r : int  = 27
   Char_s : int  = 48
   Char_t : int  = 28
   Char_u : int  = 29
   Char_v : int  = 49
   Char_w : int  = 50
   Char_x : int  = 32
   Char_y : int  = 51
   Char_z : int  = 52
   Char__ : int  = 53
   Char_A : int  = 21
   Char_B : int  = 22
   Char_C : int  = 23
   Char_D : int  = 13
   Char_E : int  = 17
   Char_F : int  = 14
   Char_G : int  = 54
   Char_H : int  = 55
   Char_I : int  = 56
   Char_J : int  = 57
   Char_K : int  = 58
   Char_L : int  = 30
   Char_M : int  = 59
   Char_N : int  = 60
   Char_O : int  = 61
   Char_P : int  = 62
   Char_Q : int  = 63
   Char_R : int  = 64
   Char_S : int  = 65
   Char_T : int  = 66
   Char_U : int  = 67
   Char_V : int  = 68
   Char_W : int  = 69
   Char_X : int  = 33
   Char_Y : int  = 70
   Char_Z : int  = 71
   Char_0 : int  = 1
   Char_1 : int  = 2
   Char_2 : int  = 3
   Char_3 : int  = 4
   Char_4 : int  = 5
   Char_5 : int  = 6
   Char_6 : int  = 7
   Char_7 : int  = 8
   Char_8 : int  = 9
   Char_9 : int  = 10
   Char_AfterASCII : int  = 72
   Char_Space : int  = 73
   Char_DoubleQuote : int  = 34
   Char_SingleQuote : int  = 24
   Char_Percent : int  = 81
   Char_VerticalBar : int  = 74
   Char_Exclamation : int  = 82
   Char_AtSign : int  = 83
   Char_BackQuote : int  = 97
   Char_Tilde : int  = 84
   Char_Sharp : int  = 98
   Char_DollarSign : int  = 75
   Char_Ampersand : int  = 76
   Char_Caret : int  = 85
   Char_Colon : int  = 86
   Char_SemiColon : int  = 87
   Char_BackSlash : int  = 77
   Char_LeftBrace : int  = 88
   Char_RightBrace : int  = 89
   Char_LeftBracket : int  = 90
   Char_RightBracket : int  = 91
   Char_QuestionMark : int  = 92
   Char_Comma : int  = 93
   Char_Dot : int  = 31
   Char_LessThan : int  = 78
   Char_GreaterThan : int  = 94
   Char_Plus : int  = 35
   Char_Minus : int  = 36
   Char_Slash : int  = 79
   Char_Star : int  = 80
   Char_LeftParen : int  = 95
   Char_RightParen : int  = 96
   Char_Equal : int  = 18
   Char_EOF : int  = 99

   orderedTerminalSymbols : list= [
                 "",
                 "0",
                 "1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6",
                 "7",
                 "8",
                 "9",
                 "f",
                 "d",
                 "D",
                 "F",
                 "b",
                 "e",
                 "E",
                 "Equal",
                 "a",
                 "c",
                 "A",
                 "B",
                 "C",
                 "SingleQuote",
                 "l",
                 "n",
                 "r",
                 "t",
                 "u",
                 "L",
                 "Dot",
                 "x",
                 "X",
                 "DoubleQuote",
                 "Plus",
                 "Minus",
                 "HT",
                 "FF",
                 "g",
                 "h",
                 "i",
                 "j",
                 "k",
                 "m",
                 "o",
                 "p",
                 "q",
                 "s",
                 "v",
                 "w",
                 "y",
                 "z",
                 "_",
                 "G",
                 "H",
                 "I",
                 "J",
                 "K",
                 "M",
                 "N",
                 "O",
                 "P",
                 "Q",
                 "R",
                 "S",
                 "T",
                 "U",
                 "V",
                 "W",
                 "Y",
                 "Z",
                 "AfterASCII",
                 "Space",
                 "VerticalBar",
                 "DollarSign",
                 "Ampersand",
                 "BackSlash",
                 "LessThan",
                 "Slash",
                 "Star",
                 "Percent",
                 "Exclamation",
                 "AtSign",
                 "Tilde",
                 "Caret",
                 "Colon",
                 "SemiColon",
                 "LeftBrace",
                 "RightBrace",
                 "LeftBracket",
                 "RightBracket",
                 "QuestionMark",
                 "Comma",
                 "GreaterThan",
                 "LeftParen",
                 "RightParen",
                 "BackQuote",
                 "Sharp",
                 "EOF",
                 "LF",
                 "CR",
                 "CtlCharNotWS"
             ]

   numTokenKinds : int  = 102
   isValidForParser : bool = True

