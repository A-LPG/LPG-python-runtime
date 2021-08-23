
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

from JavaLexersym import  JavaLexersym  
from lpg2 import ParseTable
class JavaLexerprs(ParseTable,JavaLexersym):
    ERROR_SYMBOL : int = 0
    def getErrorSymbol(self) -> int: return self.ERROR_SYMBOL

    SCOPE_UBOUND : int = 0
    def getScopeUbound(self) -> int: return self.SCOPE_UBOUND

    SCOPE_SIZE : int = 0
    def getScopeSize(self) -> int: return self.SCOPE_SIZE

    MAX_NAME_LENGTH : int = 0
    def getMaxNameLength(self) -> int: return self.MAX_NAME_LENGTH

    NUM_STATES : int = 65
    def getNumStates(self) -> int: return self.NUM_STATES

    NT_OFFSET : int = 102
    def getNtOffset(self) -> int: return self.NT_OFFSET

    LA_STATE_OFFSET : int = 895
    def getLaStateOffset(self) -> int: return self.LA_STATE_OFFSET

    MAX_LA : int = 1
    def getMaxLa(self) -> int: return self.MAX_LA

    NUM_RULES : int = 352
    def getNumRules(self) -> int: return self.NUM_RULES

    NUM_NONTERMINALS : int = 39
    def getNumNonterminals(self) -> int: return self.NUM_NONTERMINALS

    NUM_SYMBOLS : int = 141
    def getNumSymbols(self) -> int: return self.NUM_SYMBOLS

    START_STATE : int = 353
    def getStartState(self) -> int: return self.START_STATE

    IDENTIFIER_SYMBOL : int = 0
    def getIdentifier_SYMBOL(self) -> int: return self.IDENTIFIER_SYMBOL

    EOFT_SYMBOL : int = 99
    def getEoftSymbol(self) -> int: return self.EOFT_SYMBOL

    EOLT_SYMBOL : int = 103
    def getEoltSymbol(self) -> int: return self.EOLT_SYMBOL

    ACCEPT_ACTION : int = 542
    def getAcceptAction(self) -> int: return self.ACCEPT_ACTION

    ERROR_ACTION : int = 543
    def getErrorAction(self) -> int: return self.ERROR_ACTION

    BACKTRACK : bool = False
    def getBacktrack(self) ->bool: return self.BACKTRACK

    def getStartSymbol(self) -> int: return self.lhs(0)
    def isValidForParser(self) -> bool :  return JavaLexersym.isValidForParser


    _isNullable : list = [0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,1,0,0,0,0,1,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0
        ]
    def isNullable(self, index: int) ->bool : return  JavaLexerprs._isNullable[index] != 0

    _prosthesesIndex : list = [0,
            24,25,32,28,29,30,13,18,20,27,
            31,14,19,21,26,35,39,2,3,4,
            5,6,7,8,9,10,11,12,15,16,
            17,22,23,33,34,36,37,1,38
        ]
    def prosthesesIndex(self, index: int) ->int : return  JavaLexerprs._prosthesesIndex[index]

    _isKeyword : list = [0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0
        ]
    def isKeyword(self, index: int) ->bool : return  JavaLexerprs._isKeyword[index] != 0

    _baseCheck : list = [0,
            1,3,3,1,1,1,5,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,2,2,2,2,2,2,
            2,2,2,2,2,2,2,2,3,2,
            2,3,1,2,3,4,1,2,2,3,
            2,3,2,2,3,3,2,3,2,2,
            0,1,2,2,2,0,2,1,2,1,
            2,2,2,3,2,3,3,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,2,3,1,1,1,1,1,1,
            1,1,1,1,1,2,1,2,2,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,6,2,1,1,1,1,1,
            1,1,6,2,2,2,2,2,2,2,
            2,2
        ]
    def baseCheck(self, index: int) ->int : return  JavaLexerprs._baseCheck[index]
    _rhs : list = _baseCheck
    def rhs(self, index: int)  -> int: return JavaLexerprs._rhs[index]

    _baseAction : list = [
            18,18,18,18,18,18,18,18,18,18,
            18,18,18,18,18,18,18,18,18,18,
            18,18,18,18,18,18,18,18,18,18,
            18,18,18,18,18,18,18,18,18,18,
            18,18,18,18,18,18,18,18,18,18,
            18,18,18,22,22,22,22,24,24,24,
            24,24,24,24,23,23,23,23,25,25,
            25,25,26,26,27,27,20,20,7,7,
            30,30,31,31,31,13,13,13,10,10,
            10,10,10,4,4,4,4,4,5,5,
            5,5,5,5,5,5,5,5,5,5,
            5,5,5,5,5,5,5,5,5,5,
            5,5,5,5,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            1,1,1,1,1,1,1,1,1,1,
            11,11,11,11,11,11,11,11,3,3,
            3,3,3,3,3,3,3,3,3,3,
            2,2,34,34,34,8,8,9,9,12,
            12,15,15,29,29,28,28,19,19,19,
            35,35,35,35,35,35,35,35,35,35,
            35,35,35,35,35,35,35,35,35,35,
            35,35,35,35,35,35,35,35,35,16,
            16,16,16,16,16,16,16,16,16,16,
            16,16,16,16,16,16,16,16,16,16,
            16,16,16,16,16,16,16,36,36,36,
            36,36,36,36,36,36,36,36,36,36,
            36,36,36,36,36,36,36,36,36,36,
            36,36,36,36,36,37,37,37,37,37,
            37,37,37,37,37,37,37,37,37,37,
            37,37,37,37,37,37,37,37,37,37,
            37,37,37,14,14,14,14,39,39,32,
            32,32,32,32,32,32,32,33,33,33,
            33,33,33,33,33,33,21,21,21,21,
            21,21,21,21,21,17,17,17,17,17,
            17,17,17,407,531,1063,79,530,530,530,
            440,608,199,532,1179,198,198,198,975,1117,
            79,373,361,682,196,4,5,6,1052,355,
            433,364,1,70,451,355,70,70,70,509,
            528,963,70,528,528,528,70,442,70,308,
            77,954,450,77,77,77,528,1183,413,1181,
            528,202,632,103,68,1182,77,68,68,68,
            60,65,946,68,955,344,528,68,977,68,
            62,66,77,205,75,77,382,75,75,75,
            931,79,715,473,473,473,993,100,63,67,
            1161,1017,54,422,996,456,1041,369,998,58,
            64,516,976,369,412,75,456,399,75,335,
            1128,79,473,684,81,81,81,739,481,481,
            481,763,490,490,490,56,787,494,494,494,
            811,498,498,498,835,502,502,502,859,343,
            343,343,883,506,506,506,907,334,334,334,
            1084,470,1095,522,1106,524,1170,470,1184,522,
            1180,524,1139,79,1150,79,1018,184,733,681,
            853,979,980,805,877,925,986,1015,1185,1186,
            1187,543,543
        ]
    def baseAction(self, index: int) ->int : return  JavaLexerprs._baseAction[index]
    _lhs : list = _baseAction
    def lhs(self, index: int)  -> int: return JavaLexerprs._lhs[index]

    _termCheck : list = [0,
            0,1,2,3,4,5,6,7,8,9,
            10,11,12,13,14,15,16,17,18,19,
            20,21,22,23,24,25,26,27,28,29,
            30,31,32,33,34,35,36,37,38,39,
            40,41,42,43,44,45,46,47,48,49,
            50,51,52,53,54,55,56,57,58,59,
            60,61,62,63,64,65,66,67,68,69,
            70,71,72,73,74,75,76,77,78,79,
            80,81,82,83,84,85,86,87,88,89,
            90,91,92,93,94,95,96,97,98,0,
            100,101,0,1,2,3,4,5,6,7,
            8,9,10,11,12,13,14,15,16,17,
            18,19,20,21,22,23,24,25,26,27,
            28,29,30,31,32,33,34,35,36,37,
            38,39,40,41,42,43,44,45,46,47,
            48,49,50,51,52,53,54,55,56,57,
            58,59,60,61,62,63,64,65,66,67,
            68,69,70,71,72,73,74,75,76,77,
            78,79,80,81,82,83,84,85,86,87,
            88,89,90,91,92,93,94,95,96,97,
            98,0,100,101,0,1,2,3,4,5,
            6,7,8,9,10,11,12,13,14,15,
            16,17,18,19,20,21,22,23,24,25,
            26,27,28,29,30,31,32,33,34,35,
            36,37,38,39,40,41,42,43,44,45,
            46,47,48,49,50,51,52,53,54,55,
            56,57,58,59,60,61,62,63,64,65,
            66,67,68,69,70,71,72,73,74,75,
            76,77,78,79,80,81,82,83,84,85,
            86,87,88,89,90,91,92,93,94,95,
            96,97,98,0,0,0,102,0,1,2,
            3,4,5,6,7,8,9,10,11,12,
            13,14,15,16,17,18,19,20,21,22,
            23,24,25,26,27,28,29,30,31,32,
            33,34,35,36,37,38,39,40,41,42,
            43,44,45,46,47,48,49,50,51,52,
            53,54,55,56,57,58,59,60,61,62,
            63,64,65,66,67,68,69,70,71,72,
            73,74,75,76,77,78,79,80,81,82,
            83,84,85,86,87,88,89,90,91,92,
            93,94,95,96,97,98,0,1,2,3,
            4,5,6,7,8,9,10,11,12,13,
            14,15,16,17,18,19,20,21,22,23,
            24,25,26,27,28,29,30,31,32,33,
            34,35,36,37,38,39,40,41,42,43,
            44,45,46,47,48,49,50,51,52,53,
            54,55,56,57,58,59,60,61,62,63,
            64,65,66,67,68,69,70,71,72,73,
            74,75,76,0,78,79,80,81,82,83,
            84,85,86,87,88,89,90,91,92,93,
            94,95,96,0,0,0,100,101,0,1,
            2,3,4,5,6,7,8,9,10,11,
            12,13,14,15,16,17,18,19,20,21,
            22,23,0,25,26,27,28,29,30,31,
            32,33,34,35,36,37,38,39,40,41,
            42,43,44,45,46,47,48,49,50,51,
            52,53,54,55,56,57,58,59,60,61,
            62,63,64,65,66,67,68,69,70,71,
            72,73,74,75,76,77,78,79,80,81,
            82,83,84,85,86,87,88,89,90,91,
            92,93,94,95,96,97,98,0,1,2,
            3,4,5,6,7,8,9,10,11,12,
            13,14,15,16,17,0,19,20,21,22,
            23,0,25,26,27,28,29,30,0,32,
            33,0,11,12,13,14,39,40,41,42,
            43,44,45,46,47,48,49,50,51,52,
            53,54,55,56,57,58,59,60,61,62,
            63,64,65,66,67,68,69,70,71,72,
            0,0,75,0,1,2,3,4,5,6,
            7,8,9,10,11,12,13,14,15,16,
            17,0,19,20,21,22,23,0,25,0,
            0,31,0,30,0,1,2,3,4,5,
            6,7,8,9,10,11,12,13,14,15,
            16,17,0,19,20,21,22,23,0,1,
            2,3,4,5,6,7,8,9,10,11,
            12,13,14,15,16,17,24,19,20,21,
            22,23,0,1,2,3,4,5,6,7,
            8,9,10,11,12,13,14,15,16,17,
            99,19,20,21,22,23,0,1,2,3,
            4,5,6,7,8,9,10,11,12,13,
            14,15,16,17,0,19,20,21,22,23,
            0,1,2,3,4,5,6,7,8,9,
            10,11,12,13,14,15,16,17,24,19,
            20,21,22,23,0,1,2,3,4,5,
            6,7,8,9,10,11,12,13,14,15,
            16,17,0,19,20,21,22,23,0,1,
            2,3,4,5,6,7,8,9,10,11,
            12,13,14,15,16,17,0,19,20,21,
            22,23,0,1,2,3,4,5,6,7,
            8,9,10,11,12,13,14,15,16,17,
            24,19,20,21,22,23,0,1,2,3,
            4,5,6,7,8,9,10,11,12,13,
            14,15,16,17,0,19,20,21,22,23,
            0,1,2,3,4,5,6,7,8,9,
            10,11,12,13,14,0,16,17,24,0,
            0,99,0,0,0,25,11,12,13,14,
            30,31,0,1,2,3,4,5,6,7,
            8,18,18,11,0,0,0,15,0,0,
            0,0,0,0,0,0,24,0,26,27,
            28,29,0,18,18,0,34,0,1,2,
            3,4,5,6,7,8,32,33,11,24,
            18,36,15,18,0,0,0,0,0,0,
            0,24,0,26,27,28,29,11,12,13,
            14,34,16,17,0,18,0,0,24,77,
            0,1,2,3,4,5,6,7,8,9,
            10,0,1,2,3,4,5,6,7,8,
            9,10,0,1,2,3,4,5,6,7,
            8,9,10,99,77,35,36,99,99,0,
            0,0,31,0,1,2,3,4,5,6,
            7,8,9,10,0,1,2,3,4,5,
            6,7,8,9,10,0,1,2,3,4,
            5,6,7,8,9,10,0,1,2,3,
            4,5,6,7,8,9,10,0,1,2,
            3,4,5,6,7,8,9,10,0,1,
            2,3,4,5,6,7,8,9,10,0,
            1,2,3,4,5,6,7,8,9,10,
            0,1,2,3,4,5,6,7,8,0,
            1,2,3,4,5,6,7,8,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,18,18,18,
            18,18,0,0,0,0,0,0,24,24,
            24,0,0,0,0,37,38,0,35,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,73,0,0,0,74,76,0,79,80,
            78,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,100,101,
            0,0,0,0,0,0,0,0,0
        ]
    def termCheck(self, index: int) ->int : return  JavaLexerprs._termCheck[index]

    _termAction : list = [0,
            543,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,612,
            413,613,613,613,613,613,613,613,613,613,
            613,613,613,613,613,613,613,613,613,76,
            613,613,543,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,550,616,611,611,611,611,611,611,611,
            611,611,611,611,611,611,611,611,611,611,
            611,71,611,611,8,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,618,618,618,618,618,618,618,
            618,618,618,543,543,543,618,543,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,545,620,620,620,620,620,620,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,620,620,620,458,620,620,620,620,620,
            620,620,620,620,620,620,620,620,620,620,
            620,620,620,620,620,620,543,368,531,531,
            531,531,531,531,531,531,531,530,530,530,
            530,530,530,530,446,530,530,530,530,530,
            389,530,530,530,530,530,530,378,530,530,
            447,518,462,532,532,530,530,530,530,530,
            530,530,530,530,530,530,530,530,530,530,
            530,530,530,530,530,530,530,530,530,530,
            530,530,530,530,530,530,530,530,530,532,
            415,530,409,543,407,520,454,424,401,577,
            565,428,561,562,574,575,572,573,576,560,
            569,557,558,543,543,543,532,532,543,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,543,528,528,528,528,528,528,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,528,528,528,391,528,528,528,528,
            528,528,528,528,528,528,528,528,528,528,
            528,528,528,528,528,528,528,1,742,742,
            742,742,742,742,742,742,742,742,741,741,
            741,741,741,741,741,543,741,741,741,741,
            741,59,741,741,741,741,741,741,543,741,
            741,543,608,603,603,608,741,741,741,741,
            741,741,741,741,741,741,741,741,741,741,
            741,741,741,741,741,741,741,741,741,741,
            741,741,741,741,741,741,741,741,741,741,
            543,543,741,55,624,624,624,624,624,624,
            624,624,624,624,624,624,624,624,624,624,
            624,543,624,624,624,624,624,543,599,543,
            543,595,543,599,543,473,473,473,473,473,
            473,473,473,473,473,473,473,473,473,473,
            473,473,543,473,473,473,473,473,543,481,
            481,481,481,481,481,481,481,481,481,481,
            481,481,481,481,481,481,546,481,481,481,
            481,481,543,490,490,490,490,490,490,490,
            490,490,490,490,490,490,490,490,490,490,
            542,490,490,490,490,490,543,494,494,494,
            494,494,494,494,494,494,494,494,494,494,
            494,494,494,494,160,494,494,494,494,494,
            543,498,498,498,498,498,498,498,498,498,
            498,498,498,498,498,498,498,498,182,498,
            498,498,498,498,543,502,502,502,502,502,
            502,502,502,502,502,502,502,502,502,502,
            502,502,197,502,502,502,502,502,543,886,
            886,886,886,886,886,886,886,886,886,886,
            886,886,886,886,886,886,161,886,886,886,
            886,886,543,506,506,506,506,506,506,506,
            506,506,506,506,506,506,506,506,506,506,
            182,506,506,506,506,506,543,877,877,877,
            877,877,877,877,877,877,877,877,877,877,
            877,877,877,877,162,877,877,877,877,877,
            4,622,622,622,622,622,622,622,622,622,
            622,610,606,606,610,61,456,456,182,543,
            543,1,543,28,21,597,609,605,605,609,
            597,510,543,533,534,535,536,537,538,539,
            540,582,591,891,78,11,20,888,78,195,
            543,543,543,543,543,163,894,543,890,892,
            889,477,16,585,590,12,893,543,878,878,
            878,878,878,878,878,878,442,442,891,182,
            580,579,888,586,164,543,6,40,543,543,
            543,894,543,890,892,889,486,607,601,601,
            607,893,456,456,543,592,543,543,182,895,
            543,369,369,369,369,369,369,369,369,369,
            369,27,355,355,355,355,355,355,355,355,
            355,355,82,622,622,622,622,622,622,622,
            622,622,622,4,895,514,512,4,9,543,
            543,543,529,83,470,470,470,470,470,470,
            470,470,470,470,543,522,522,522,522,522,
            522,522,522,522,522,543,524,524,524,524,
            524,524,524,524,524,524,85,622,622,622,
            622,622,622,622,622,622,622,84,622,622,
            622,622,622,622,622,622,622,622,87,622,
            622,622,622,622,622,622,622,622,622,86,
            622,622,622,622,622,622,622,622,622,622,
            182,516,516,516,516,516,516,516,516,183,
            727,727,727,727,727,727,727,727,9,13,
            24,23,25,10,165,166,167,543,543,543,
            543,543,543,543,543,543,543,587,588,589,
            581,584,543,543,543,543,543,543,182,182,
            182,543,543,543,543,739,739,543,578,543,
            543,543,543,543,543,543,543,543,543,543,
            543,543,543,543,543,543,543,543,543,543,
            543,543,543,543,543,543,543,543,543,543,
            543,739,543,543,543,593,594,543,617,411,
            526,543,543,543,543,543,543,543,543,543,
            543,543,543,543,543,543,543,543,739,739
        ]
    def termAction(self, index: int) ->int : return  JavaLexerprs._termAction[index]
    def asb(self, index: int) -> int: return 0
    def asr(self, index: int) -> int: return 0
    def nasb(self, index: int)  -> int: return 0
    def nasr(self, index: int)  -> int: return 0
    def terminalIndex(self, index: int) -> int: return 0
    def nonterminalIndex(self, index: int)  -> int: return 0
    def scopePrefix(self, index: int)  -> int: return 0
    def scopeSuffix(self, index: int) -> int: return 0
    def scopeLhs(self, index: int)  -> int: return 0
    def scopeLa(self, index: int) -> int: return 0
    def scopeStateSet(self, index: int)  -> int: return 0
    def scopeRhs(self, index: int)  -> int: return 0
    def scopeState(self, index: int) -> int: return 0
    def inSymb(self, index: int)  -> int: return 0
    def name(self, index: int)  -> str: return ""
    def originalState(self, state : int) -> int: return 0
    def asi(self, state : int) -> int: return 0
    def nasi(self, state : int ) -> int: return 0
    def inSymbol(self, state : int)  -> int: return 0

    #/**
     # assert(! goto_default)
     #/
    def ntAction(self, state : int,  sym : int) -> int:
        return JavaLexerprs._baseAction[state + sym]
    

    #/**
     #* assert(! shift_default)
     #*/
    def tAction(self, state : int,  sym : int)-> int:
        i = JavaLexerprs._baseAction[state]
        k = i + sym
        return JavaLexerprs._termAction[  k if JavaLexerprs._termCheck[k] == sym else i]
    
    def lookAhead(self, la_state : int , sym: int)-> int:
        k = la_state + sym
        return JavaLexerprs._termAction[  k if JavaLexerprs._termCheck[k] == sym else  la_state]
    

