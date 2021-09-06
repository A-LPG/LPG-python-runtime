
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

class LPGKWLexersym(object):
   Char_DollarSign : int  = 20
   Char_Percent : int  = 21
   Char__ : int  = 28
   Char_a : int  = 8
   Char_b : int  = 17
   Char_c : int  = 14
   Char_d : int  = 9
   Char_e : int  = 1
   Char_f : int  = 15
   Char_g : int  = 22
   Char_h : int  = 23
   Char_i : int  = 6
   Char_j : int  = 24
   Char_k : int  = 18
   Char_l : int  = 7
   Char_m : int  = 12
   Char_n : int  = 10
   Char_o : int  = 4
   Char_p : int  = 11
   Char_q : int  = 29
   Char_r : int  = 3
   Char_s : int  = 2
   Char_t : int  = 5
   Char_u : int  = 16
   Char_v : int  = 25
   Char_w : int  = 19
   Char_x : int  = 26
   Char_y : int  = 13
   Char_z : int  = 30
   Char_EOF : int  = 27

   orderedTerminalSymbols : list= [
                 "",
                 "e",
                 "s",
                 "r",
                 "o",
                 "t",
                 "i",
                 "l",
                 "a",
                 "d",
                 "n",
                 "p",
                 "m",
                 "y",
                 "c",
                 "f",
                 "u",
                 "b",
                 "k",
                 "w",
                 "DollarSign",
                 "Percent",
                 "g",
                 "h",
                 "j",
                 "v",
                 "x",
                 "EOF",
                 "_",
                 "q",
                 "z"
             ]

   numTokenKinds : int  = 30
   isValidForParser : bool = True

