
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

from LPGKWLexersym import  LPGKWLexersym  
from lpg2 import ParseTable
class LPGKWLexerprs(ParseTable,LPGKWLexersym):
    ERROR_SYMBOL  = 0
    def getErrorSymbol(self): return self.ERROR_SYMBOL

    SCOPE_UBOUND  = 0
    def getScopeUbound(self): return self.SCOPE_UBOUND

    SCOPE_SIZE  = 0
    def getScopeSize(self): return self.SCOPE_SIZE

    MAX_NAME_LENGTH  = 0
    def getMaxNameLength(self): return self.MAX_NAME_LENGTH

    NUM_STATES  = 145
    def getNumStates(self): return self.NUM_STATES

    NT_OFFSET  = 30
    def getNtOffset(self): return self.NT_OFFSET

    LA_STATE_OFFSET  = 208
    def getLaStateOffset(self): return self.LA_STATE_OFFSET

    MAX_LA  = 0
    def getMaxLa(self): return self.MAX_LA

    NUM_RULES  = 29
    def getNumRules(self): return self.NUM_RULES

    NUM_NONTERMINALS  = 3
    def getNumNonterminals(self): return self.NUM_NONTERMINALS

    NUM_SYMBOLS  = 33
    def getNumSymbols(self): return self.NUM_SYMBOLS

    START_STATE  = 30
    def getStartState(self): return self.START_STATE

    IDENTIFIER_SYMBOL  = 0
    def getIdentifier_SYMBOL(self): return self.IDENTIFIER_SYMBOL

    EOFT_SYMBOL  = 27
    def getEoftSymbol(self): return self.EOFT_SYMBOL

    EOLT_SYMBOL  = 31
    def getEoltSymbol(self): return self.EOLT_SYMBOL

    ACCEPT_ACTION  = 178
    def getAcceptAction(self): return self.ACCEPT_ACTION

    ERROR_ACTION  = 179
    def getErrorAction(self): return self.ERROR_ACTION

    BACKTRACK  = False
    def getBacktrack(self): return self.BACKTRACK

    def getStartSymbol(self): return self.lhs(0)
    def isValidForParser(self)  :  return LPGKWLexersym.isValidForParser


    _isNullable = [0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0
        ]
    def isNullable(self, index): return  LPGKWLexerprs._isNullable[index] != 0

    _prosthesesIndex = [0,
            2,3,1
        ]
    def prosthesesIndex(self, index): return  LPGKWLexerprs._prosthesesIndex[index]

    _isKeyword = [0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0
        ]
    def isKeyword(self, index): return  LPGKWLexerprs._isKeyword[index] != 0

    _baseCheck = [0,
            6,4,7,24,10,12,6,4,6,4,
            4,7,8,8,11,7,8,9,13,6,
            7,10,8,6,6,9,6,1,1
        ]
    def baseCheck(self, index): return  LPGKWLexerprs._baseCheck[index]
    _rhs  = _baseCheck
    def rhs(self, index) : return LPGKWLexerprs._rhs[index]

    _baseAction = [
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,2,2,
            26,33,34,37,1,39,12,44,45,62,
            22,65,67,17,35,51,68,14,5,70,
            30,71,72,73,77,80,42,79,82,86,
            85,87,54,88,95,96,97,100,99,103,
            105,109,112,117,113,115,120,121,125,124,
            123,130,131,8,132,133,134,136,139,143,
            145,146,147,149,148,156,153,157,161,162,
            165,159,167,166,176,178,180,184,185,186,
            174,57,168,190,191,194,196,198,201,203,
            206,205,207,210,215,213,217,211,219,221,
            225,228,229,230,223,233,239,234,241,244,
            245,247,248,250,253,237,259,262,255,263,
            265,267,271,273,276,277,278,281,282,283,
            288,286,292,296,298,293,303,287,305,307,
            308,311,313,312,317,319,320,179,179
        ]
    def baseAction(self, index): return  LPGKWLexerprs._baseAction[index]
    _lhs  = _baseAction
    def lhs(self, index) : return LPGKWLexerprs._lhs[index]

    _termCheck = [0,
            0,1,2,3,0,5,6,0,8,9,
            10,0,1,0,3,11,0,10,18,3,
            4,0,22,23,13,0,10,14,12,0,
            9,10,3,12,0,1,0,3,0,1,
            6,0,26,0,0,20,21,4,4,5,
            0,8,2,0,16,14,0,7,2,3,
            7,0,1,27,0,1,0,0,15,0,
            0,0,0,7,7,5,0,8,0,0,
            8,0,1,12,0,0,0,0,4,11,
            3,15,13,8,0,0,0,11,0,0,
            4,2,0,9,0,0,11,5,0,1,
            6,0,0,15,0,4,0,1,6,0,
            0,1,0,0,0,6,12,3,5,0,
            0,0,0,0,4,0,7,4,0,4,
            9,19,0,5,0,0,0,0,0,17,
            2,6,0,11,8,0,0,2,0,7,
            0,0,6,2,0,0,0,0,24,5,
            4,4,25,0,14,0,18,0,3,0,
            1,16,5,0,0,0,13,3,3,0,
            0,8,2,0,1,0,1,0,0,10,
            0,1,0,1,0,0,0,10,3,0,
            0,5,0,9,0,6,0,3,0,7,
            0,5,0,13,0,1,6,0,0,0,
            3,3,0,0,16,13,0,8,0,1,
            0,9,2,0,0,2,0,0,15,0,
            0,2,0,7,0,19,12,10,0,7,
            2,0,0,1,0,0,0,6,2,5,
            0,17,0,1,4,0,0,0,2,4,
            0,0,0,3,3,0,0,0,11,7,
            3,0,0,2,9,0,1,0,0,2,
            14,9,0,1,0,1,0,0,2,2,
            0,0,0,2,4,3,0,1,0,0,
            0,2,0,5,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0
        ]
    def termCheck(self, index): return  LPGKWLexerprs._termCheck[index]

    _termAction = [0,
            179,43,38,35,179,36,40,179,45,44,
            37,179,50,179,49,73,179,105,39,63,
            62,179,42,41,48,179,64,72,65,179,
            58,56,75,57,179,68,179,66,179,47,
            67,179,61,179,179,34,34,51,54,53,
            179,52,69,179,46,81,179,70,127,128,
            189,179,55,178,179,59,179,179,190,179,
            179,179,179,60,71,76,179,74,179,179,
            78,179,83,77,179,179,179,179,85,82,
            87,79,80,84,179,179,179,86,179,179,
            89,90,179,187,179,179,88,181,179,93,
            92,179,179,91,179,94,179,95,96,179,
            179,99,179,179,179,98,97,100,101,179,
            179,179,179,179,104,179,103,108,179,109,
            106,102,179,110,179,179,179,179,179,107,
            203,113,179,111,114,179,179,206,179,116,
            179,179,117,199,179,179,179,179,112,204,
            120,129,115,179,118,179,119,179,122,179,
            124,121,123,179,179,179,186,126,188,179,
            179,125,180,179,131,179,132,179,179,130,
            179,200,179,134,179,179,179,133,135,179,
            179,195,179,136,179,137,179,138,179,139,
            179,191,179,140,179,182,142,179,179,179,
            202,143,179,179,141,145,179,144,179,196,
            179,146,193,179,179,192,179,179,147,179,
            179,205,179,149,179,152,148,150,179,151,
            197,179,179,155,179,179,179,153,201,156,
            179,154,179,158,157,179,179,179,184,159,
            179,179,179,161,194,179,179,179,160,162,
            163,179,179,185,164,179,165,179,179,198,
            168,166,179,167,179,169,179,179,170,171,
            179,179,179,174,172,173,179,175,179,179,
            179,183,179,176
        ]
    def termAction(self, index): return  LPGKWLexerprs._termAction[index]
    def asb(self, index): return 0
    def asr(self, index): return 0
    def nasb(self, index) : return 0
    def nasr(self, index) : return 0
    def terminalIndex(self, index): return 0
    def nonterminalIndex(self, index) : return 0
    def scopePrefix(self, index) : return 0
    def scopeSuffix(self, index): return 0
    def scopeLhs(self, index) : return 0
    def scopeLa(self, index): return 0
    def scopeStateSet(self, index) : return 0
    def scopeRhs(self, index) : return 0
    def scopeState(self, index): return 0
    def inSymb(self, index) : return 0
    def name(self, index)  : return ""
    def originalState(self, state ): return 0
    def asi(self, state ): return 0
    def nasi(self, state  ): return 0
    def inSymbol(self, state ) : return 0

    #/**
     # assert(! goto_default)
     #/
    def ntAction(self, state,  sym):
        return LPGKWLexerprs._baseAction[state + sym]
    

    #/**
     #* assert(! shift_default)
     #*/
    def tAction(self, state, sym):
        i = LPGKWLexerprs._baseAction[state]
        k = i + sym
        return LPGKWLexerprs._termAction[  k if LPGKWLexerprs._termCheck[k] == sym else i]
    
    def lookAhead(self, la_state, sym):
        k = la_state + sym
        return LPGKWLexerprs._termAction[  k if LPGKWLexerprs._termCheck[k] == sym else  la_state]
    

