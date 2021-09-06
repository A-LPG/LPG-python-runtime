
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

class LPGLexersym(object):
   Char_CtlCharNotWS : int  = 102
   Char_LF : int  = 5
   Char_CR : int  = 6
   Char_HT : int  = 1
   Char_FF : int  = 2
   Char_a : int  = 15
   Char_b : int  = 40
   Char_c : int  = 24
   Char_d : int  = 30
   Char_e : int  = 7
   Char_f : int  = 31
   Char_g : int  = 42
   Char_h : int  = 50
   Char_i : int  = 13
   Char_j : int  = 70
   Char_k : int  = 44
   Char_l : int  = 18
   Char_m : int  = 34
   Char_n : int  = 28
   Char_o : int  = 22
   Char_p : int  = 36
   Char_q : int  = 56
   Char_r : int  = 11
   Char_s : int  = 20
   Char_t : int  = 9
   Char_u : int  = 38
   Char_v : int  = 52
   Char_w : int  = 53
   Char_x : int  = 48
   Char_y : int  = 45
   Char_z : int  = 68
   Char__ : int  = 26
   Char_A : int  = 16
   Char_B : int  = 41
   Char_C : int  = 25
   Char_D : int  = 32
   Char_E : int  = 8
   Char_F : int  = 33
   Char_G : int  = 43
   Char_H : int  = 51
   Char_I : int  = 14
   Char_J : int  = 71
   Char_K : int  = 46
   Char_L : int  = 19
   Char_M : int  = 35
   Char_N : int  = 29
   Char_O : int  = 23
   Char_P : int  = 37
   Char_Q : int  = 57
   Char_R : int  = 12
   Char_S : int  = 21
   Char_T : int  = 10
   Char_U : int  = 39
   Char_V : int  = 54
   Char_W : int  = 55
   Char_X : int  = 49
   Char_Y : int  = 47
   Char_Z : int  = 69
   Char_0 : int  = 58
   Char_1 : int  = 59
   Char_2 : int  = 60
   Char_3 : int  = 61
   Char_4 : int  = 62
   Char_5 : int  = 63
   Char_6 : int  = 64
   Char_7 : int  = 65
   Char_8 : int  = 66
   Char_9 : int  = 67
   Char_AfterASCII : int  = 72
   Char_Space : int  = 3
   Char_DoubleQuote : int  = 97
   Char_SingleQuote : int  = 98
   Char_Percent : int  = 74
   Char_VerticalBar : int  = 76
   Char_Exclamation : int  = 77
   Char_AtSign : int  = 78
   Char_BackQuote : int  = 79
   Char_Tilde : int  = 80
   Char_Sharp : int  = 92
   Char_DollarSign : int  = 100
   Char_Ampersand : int  = 81
   Char_Caret : int  = 82
   Char_Colon : int  = 83
   Char_SemiColon : int  = 84
   Char_BackSlash : int  = 85
   Char_LeftBrace : int  = 86
   Char_RightBrace : int  = 87
   Char_LeftBracket : int  = 93
   Char_RightBracket : int  = 94
   Char_QuestionMark : int  = 73
   Char_Comma : int  = 4
   Char_Dot : int  = 88
   Char_LessThan : int  = 99
   Char_GreaterThan : int  = 95
   Char_Plus : int  = 89
   Char_Minus : int  = 27
   Char_Slash : int  = 90
   Char_Star : int  = 91
   Char_LeftParen : int  = 96
   Char_RightParen : int  = 75
   Char_Equal : int  = 17
   Char_EOF : int  = 101

   orderedTerminalSymbols : list= [
                 "",
                 "HT",
                 "FF",
                 "Space",
                 "Comma",
                 "LF",
                 "CR",
                 "e",
                 "E",
                 "t",
                 "T",
                 "r",
                 "R",
                 "i",
                 "I",
                 "a",
                 "A",
                 "Equal",
                 "l",
                 "L",
                 "s",
                 "S",
                 "o",
                 "O",
                 "c",
                 "C",
                 "_",
                 "Minus",
                 "n",
                 "N",
                 "d",
                 "f",
                 "D",
                 "F",
                 "m",
                 "M",
                 "p",
                 "P",
                 "u",
                 "U",
                 "b",
                 "B",
                 "g",
                 "G",
                 "k",
                 "y",
                 "K",
                 "Y",
                 "x",
                 "X",
                 "h",
                 "H",
                 "v",
                 "w",
                 "V",
                 "W",
                 "q",
                 "Q",
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
                 "z",
                 "Z",
                 "j",
                 "J",
                 "AfterASCII",
                 "QuestionMark",
                 "Percent",
                 "RightParen",
                 "VerticalBar",
                 "Exclamation",
                 "AtSign",
                 "BackQuote",
                 "Tilde",
                 "Ampersand",
                 "Caret",
                 "Colon",
                 "SemiColon",
                 "BackSlash",
                 "LeftBrace",
                 "RightBrace",
                 "Dot",
                 "Plus",
                 "Slash",
                 "Star",
                 "Sharp",
                 "LeftBracket",
                 "RightBracket",
                 "GreaterThan",
                 "LeftParen",
                 "DoubleQuote",
                 "SingleQuote",
                 "LessThan",
                 "DollarSign",
                 "EOF",
                 "CtlCharNotWS"
             ]

   numTokenKinds : int  = 102
   isValidForParser : bool = True

