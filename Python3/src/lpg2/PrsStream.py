#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from LexStream import LexStream
from Token import Token
from ErrorToken import ErrorToken
from Adjunct import Adjunct
# import  Utf8LexStream  from Utf8LexStream"
from IMessageHandler import IMessageHandler
from NullTerminalSymbolsException import NullTerminalSymbolsException
from UndefinedEofSymbolException import UndefinedEofSymbolException
from UnimplementedTerminalsException import UnimplementedTerminalsException

from Protocol import IPrsStream, ILexStream, IToken
from Utils import ArrayList


#
# PrsStream holds an arraylist of tokens "lexed" from the input stream.
#
class PrsStream(IPrsStream):

    def __init__(self, iLexStream: ILexStream = None):
        self.iLexStream: ILexStream = None
        self.kindMap: list = []
        self.tokens: ArrayList = ArrayList()
        self.adjuncts: ArrayList = ArrayList()
        self.index: int = 0
        self.len: int = 0
        if (iLexStream):
            self.iLexStream = iLexStream
            iLexStream.setPrsStream(self)
            self.resetTokenStream()

    def orderedExportedSymbols(self) -> list:
        return []

    def remapTerminalSymbols(self, ordered_parser_symbols: list, eof_symbol: int):
        # lexStream might be None, maybe only erroneously, but it has happened
        if (not self.iLexStream):
            raise ReferenceError("PrsStream.remapTerminalSymbols(..):  lexStream is None")

        ordered_lexer_symbols: list = self.iLexStream.orderedExportedSymbols()
        if (ordered_lexer_symbols is None):
            raise NullTerminalSymbolsException()

        if (ordered_parser_symbols is None):
            raise NullTerminalSymbolsException()

        unimplemented_symbols: ArrayList = ArrayList()
        if (ordered_lexer_symbols != ordered_parser_symbols):
            self.kindMap = [0] * (ordered_lexer_symbols.__len__())
            terminal_map = dict()
            for i in range(0, ordered_lexer_symbols.__len__()):
                terminal_map[ordered_lexer_symbols[i]] = i

            for k in range(0, ordered_parser_symbols.__len__()):
                k: int = terminal_map.get(ordered_parser_symbols[i])
                if (k != None):
                    self.kindMap[k] = i
                else:
                    if (i == eof_symbol):
                        raise UndefinedEofSymbolException()

                    unimplemented_symbols.add(i)

        if (unimplemented_symbols.size() > 0):
            raise UnimplementedTerminalsException(unimplemented_symbols)

    def mapKind(self, kind: int) -> int:
        return (kind if self.kindMap.__len__() == 0 else self.kindMap[kind])

    def resetTokenStream(self):
        self.tokens = ArrayList()
        self.index = 0
        self.adjuncts = ArrayList()

    def setLexStream(self, lexStream: ILexStream):
        self.iLexStream = lexStream
        self.resetTokenStream()

    def resetLexStream(self, lexStream: ILexStream):

        if (lexStream):
            lexStream.setPrsStream(self)
            self.iLexStream = lexStream

    def makeToken(self, startLoc: int, endLoc: int, kind: int):
        token: Token = Token(startLoc, endLoc, self.mapKind(kind), self)
        token.setTokenIndex(self.tokens.size())
        self.tokens.add(token)
        token.setAdjunctIndex(self.adjuncts.size())

    def removeLastToken(self):
        last_index: int = self.tokens.size() - 1
        token: Token = self.tokens.get(last_index)
        adjuncts_size: int = self.adjuncts.size()
        while (adjuncts_size > token.getAdjunctIndex()):
            adjuncts_size -= 1
            self.adjuncts.remove(adjuncts_size)

        self.tokens.remove(last_index)

    def makeErrorToken(self, firsttok: int, lasttok: int, errortok: int, kind: int) -> int:
        index: int = self.tokens.size()  # the next index

        #
        # Note that when creating an error token, we do not remap its kind.
        # Since self is not a lexical operation, it is the responsibility of
        # the calling program (a parser driver): to pass to us the proper kind
        # that it wants for an error token.
        #
        token: Token = ErrorToken(self.getIToken(firsttok),
                                  self.getIToken(lasttok),
                                  self.getIToken(errortok),
                                  self.getStartOffset(firsttok),
                                  self.getEndOffset(lasttok),
                                  kind)

        token.setTokenIndex(self.tokens.size())
        self.tokens.add(token)
        token.setAdjunctIndex(self.adjuncts.size())

        return index

    def addToken(self, token: IToken):
        token.setTokenIndex(self.tokens.size())
        self.tokens.add(token)
        token.setAdjunctIndex(self.adjuncts.size())

    def makeAdjunct(self, startLoc: int, endLoc: int, kind: int):
        token_index: int = self.tokens.size() - 1  # index of last token processed
        adjunct: Adjunct = Adjunct(startLoc, endLoc, self.mapKind(kind), self)
        adjunct.setAdjunctIndex(self.adjuncts.size())
        adjunct.setTokenIndex(token_index)
        self.adjuncts.add(adjunct)

    def addAdjunct(self, adjunct: IToken):
        token_index: int = self.tokens.size() - 1  # index of last token processed
        adjunct.setTokenIndex(token_index)
        adjunct.setAdjunctIndex(self.adjuncts.size())
        self.adjuncts.add(adjunct)

    def getTokenText(self, i: int) -> str:
        t: IToken = self.tokens.get(i)
        return t.toString()

    def getStartOffset(self, i: int) -> int:
        t: IToken = self.tokens.get(i)
        return t.getStartOffset()

    def getEndOffset(self, i: int) -> int:
        t: IToken = self.tokens.get(i)
        return t.getEndOffset()

    def getTokenLength(self, i: int) -> int:
        t: IToken = self.tokens.get(i)
        return t.getEndOffset() - t.getStartOffset() + 1

    def getLineNumberOfTokenAt(self, i: int) -> int:
        if (not self.iLexStream): return 0
        t: IToken = self.tokens.get(i)
        return self.iLexStream.getLineNumberOfCharAt(t.getStartOffset())

    def getEndLineNumberOfTokenAt(self, i: int) -> int:
        if (not self.iLexStream): return 0
        t: IToken = self.tokens.get(i)
        return self.iLexStream.getLineNumberOfCharAt(t.getEndOffset())

    def getColumnOfTokenAt(self, i: int) -> int:
        if (not self.iLexStream): return 0
        t: IToken = self.tokens.get(i)
        return self.iLexStream.getColumnOfCharAt(t.getStartOffset())

    def getEndColumnOfTokenAt(self, i: int) -> int:
        if (not self.iLexStream): return 0
        t: IToken = self.tokens.get(i)
        return self.iLexStream.getColumnOfCharAt(t.getEndOffset())

    def orderedTerminalSymbols(self) -> list:
        return []

    def getLineOffset(self, i: int) -> int:
        if (not self.iLexStream): return 0
        return self.iLexStream.getLineOffset(i)

    def getLineCount(self) -> int:
        if (not self.iLexStream): return 0
        return self.iLexStream.getLineCount()

    def getLineNumberOfCharAt(self, i: int) -> int:
        if (not self.iLexStream): return 0
        return self.iLexStream.getLineNumberOfCharAt(i)

    def getColumnOfCharAt(self, i: int) -> int:
        return self.getColumnOfCharAt(i)

    def getFirstErrorToken(self, i: int) -> int:
        return self.getFirstRealToken(i)

    def getFirstRealToken(self, i: int) -> int:
        while (i >= self.len):
            i = (self.tokens.get(i)).getFirstRealToken().getTokenIndex()

        return i

    def getLastErrorToken(self, i: int) -> int:
        return self.getLastRealToken(i)

    def getLastRealToken(self, i: int) -> int:
        while (i >= self.len):
            i = (self.tokens.get(i)).getLastRealToken().getTokenIndex()

        return i

    def getInputChars(self) -> str:
        return self.iLexStream.getInputChars() if isinstance(self.iLexStream, LexStream) else ""

    def getInputBytes(self):
        #  return (self.iLexStream instanceof Utf8LexStream ? (<Utf8LexStream>self.iLexStream).getInputBytes(): : None):
        return ""

    def toStringFromIndex(self, first_token: int, last_token: int) -> str:
        return self.toString(self.tokens.get(first_token), self.tokens.get(last_token))

    def toString(self, t1: IToken, t2: IToken) -> str:
        if (not self.iLexStream): return ""
        return self.iLexStream.toString(t1.getStartOffset(), t2.getEndOffset())

    def getSize(self) -> int:
        return self.tokens.size()

    def setSize(self):
        self.len = self.tokens.size()

    def getTokenIndexAtCharacter(self, offset: int) -> int:
        low: int = 0,
        high: int = self.tokens.size()
        while (high > low):
            mid: int = (high + low) // 2
            mid_element: IToken = self.tokens.get(mid)
            if (offset >= mid_element.getStartOffset() and offset <= mid_element.getEndOffset()):
                return mid
            else:
                if (offset < mid_element.getStartOffset()):
                    high = mid
                else:
                    low = mid + 1

        return -(low - 1)

    def getTokenAtCharacter(self, offset: int) -> IToken:
        tokenIndex: int = self.getTokenIndexAtCharacter(offset)
        return None if (tokenIndex < 0) else self.getTokenAt(tokenIndex)

    def getTokenAt(self, i: int) -> IToken:
        return self.tokens.get(i)

    def getIToken(self, i: int) -> IToken:
        return self.tokens.get(i)

    def getTokens(self) -> ArrayList:
        return self.tokens

    def getStreamIndex(self) -> int:
        return self.index

    def getStreamLength(self) -> int:
        return self.len

    def setStreamIndex(self, index: int):
        self.index = index

    def setStreamLength2(self):
        self.len = self.tokens.size()

    def setStreamLength(self, length: int = -1):
        if (-1 == len):
            self.setStreamLength2()
            return

        self.len = len

    def getILexStream(self) -> ILexStream:
        return self.iLexStream

    def getLexStream(self) -> ILexStream:
        return self.iLexStream

    def dumpTokens(self):
        if (self.getSize() <= 2):
            return

        print(" Kind \tOffset \tLen \tLine \tCol \tText\n")
        for i in range(1, self.getSize()):
            self.dumpToken(i)

    def dumpToken(self, i: int):
        print(" (" + self.getKind(i) + "):")
        print(" \t" + self.getStartOffset(i))
        print(" \t" + self.getTokenLength(i))
        print(" \t" + self.getLineNumberOfTokenAt(i))
        print(" \t" + self.getColumnOfTokenAt(i))
        print(" \t" + self.getTokenText(i))
        print("\n")

    def getAdjunctsFromIndex(self, i: int) -> list:
        start_index: int = (self.tokens.get(i)).getAdjunctIndex()
        end_index: int = (self.adjuncts.size() if (i + 1 == self.tokens.size())
                          else (self.tokens.get(self.getNext(i))).getAdjunctIndex())
        size: int = end_index - start_index
        slice: list = [None] * (size)
        j: int = start_index
        k: int = 0
        while (j < end_index):
            slice[k] = self.adjuncts.get(j)
            k += 1
            j += 1

        return slice

    def getFollowingAdjuncts(self, i: int) -> list:
        return self.getAdjunctsFromIndex(i)

    def getPrecedingAdjuncts(self, i: int) -> IToken:
        return self.getAdjunctsFromIndex(self.getPrevious(i))

    def getAdjuncts(self) -> ArrayList:
        return self.adjuncts

    def getToken2(self) -> int:
        self.index = self.getNext(self.index)
        return self.index

    def getToken(self, end_token: int = None) -> int:
        if (None == end_token):
            return self.getToken2()
        self.index = (self.getNext(self.index) if self.index < end_token else self.len - 1)
        return self.index

    def getKind(self, i: int) -> int:
        t: IToken = self.tokens.get(i)
        return t.getKind()

    def getNext(self, i: int) -> int:
        i += 1
        return (i if i < self.len else self.len - 1)

    def getPrevious(self, i: int) -> int:
        return (0 if i <= 0 else i - 1)

    def getName(self, i: int) -> str:
        return self.getTokenText(i)

    def peek(self) -> int:
        return self.getNext(self.index)

    def reset1(self):
        self.index = 0

    def reset2(self, i: int):
        self.index = self.getPrevious(i)

    def reset(self, i: int = None):
        if i is None:
            self.reset1()

        else:
            self.reset2(i)

    def badToken(self) -> int:
        return 0

    def getLine(self, i: int) -> int:
        return self.getLineNumberOfTokenAt(i)

    def getColumn(self, i: int) -> int:
        return self.getColumnOfTokenAt(i)

    def getEndLine(self, i: int) -> int:
        return self.getEndLineNumberOfTokenAt(i)

    def getEndColumn(self, i: int) -> int:
        return self.getEndColumnOfTokenAt(i)

    def afterEol(self, i: int) -> bool:
        return (True if i < 1 else self.getEndLineNumberOfTokenAt(i - 1) < self.getLineNumberOfTokenAt(i))

    def getFileName(self) -> str:
        if (not self.iLexStream): return ""
        return self.iLexStream.getFileName()

    #
    # Here is where we report errors.  The default method is simply to print the error message to the console.
    # However, the user may supply an error message handler to process error messages.  To support that
    # a message handler class is provided that has a single method handleMessage().  The user has his
    # error message handler class implement the IMessageHandler class and provides an object of self type
    # to the runtime using the setMessageHandler(errorMsg): method. If the message handler object is set,
    # the reportError methods will invoke its handleMessage(): method.
    #
    # IMessageHandler errMsg = None # the error message handler object is declared in LexStream
    #
    def setMessageHandler(self, errMsg: IMessageHandler):
        self.iLexStream.setMessageHandler(errMsg)

    def getMessageHandler(self) -> IMessageHandler:
        return self.iLexStream.getMessageHandler()

    def reportError(self, errorCode: int, leftToken: int, rightToken: int, errorInfo, errorToken: int = 0):
        tempInfo: list
        if (isinstance(errorInfo, str)):
            tempInfo = [errorInfo]

        elif (isinstance(errorInfo, list)):
            tempInfo = errorInfo

        else:
            tempInfo = []

        self.iLexStream.reportLexicalError(self.getStartOffset(leftToken), self.getEndOffset(rightToken),
                                           errorCode, self.getStartOffset(errorToken), self.getEndOffset(errorToken),
                                           tempInfo)
