
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

class JavaKWLexersym(object):
   Char_DollarSign : int  = 35
   Char_Percent : int  = 42
   Char__ : int  = 43
   Char_a : int  = 3
   Char_b : int  = 19
   Char_c : int  = 8
   Char_d : int  = 14
   Char_e : int  = 2
   Char_f : int  = 16
   Char_g : int  = 23
   Char_h : int  = 15
   Char_i : int  = 6
   Char_j : int  = 28
   Char_k : int  = 29
   Char_l : int  = 7
   Char_m : int  = 27
   Char_n : int  = 4
   Char_o : int  = 5
   Char_p : int  = 24
   Char_q : int  = 44
   Char_r : int  = 9
   Char_s : int  = 10
   Char_t : int  = 1
   Char_u : int  = 11
   Char_v : int  = 20
   Char_w : int  = 25
   Char_x : int  = 36
   Char_y : int  = 26
   Char_z : int  = 37
   Char_A : int  = 12
   Char_B : int  = 38
   Char_C : int  = 21
   Char_D : int  = 30
   Char_E : int  = 31
   Char_F : int  = 45
   Char_G : int  = 39
   Char_H : int  = 46
   Char_I : int  = 17
   Char_J : int  = 32
   Char_K : int  = 47
   Char_L : int  = 33
   Char_M : int  = 48
   Char_N : int  = 13
   Char_O : int  = 18
   Char_P : int  = 49
   Char_Q : int  = 50
   Char_R : int  = 51
   Char_S : int  = 52
   Char_T : int  = 22
   Char_U : int  = 40
   Char_V : int  = 34
   Char_W : int  = 53
   Char_X : int  = 54
   Char_Y : int  = 55
   Char_Z : int  = 56
   Char_EOF : int  = 41

   orderedTerminalSymbols : list= [
                 "",
                 "t",
                 "e",
                 "a",
                 "n",
                 "o",
                 "i",
                 "l",
                 "c",
                 "r",
                 "s",
                 "u",
                 "A",
                 "N",
                 "d",
                 "h",
                 "f",
                 "I",
                 "O",
                 "b",
                 "v",
                 "C",
                 "T",
                 "g",
                 "p",
                 "w",
                 "y",
                 "m",
                 "j",
                 "k",
                 "D",
                 "E",
                 "J",
                 "L",
                 "V",
                 "DollarSign",
                 "x",
                 "z",
                 "B",
                 "G",
                 "U",
                 "EOF",
                 "Percent",
                 "_",
                 "q",
                 "F",
                 "H",
                 "K",
                 "M",
                 "P",
                 "Q",
                 "R",
                 "S",
                 "W",
                 "X",
                 "Y",
                 "Z"
             ]

   numTokenKinds : int  = 57
   isValidForParser : bool = True

