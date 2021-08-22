#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod
from lpg2.IMessageHandler import IMessageHandler
from lpg2.ILexStream import ILexStream
from lpg2.TokenStream import TokenStream
from lpg2.IToken import IToken
from lpg2.Utils import ArrayList


class IPrsStream(TokenStream):
    __slots__ = ()

    @abstractmethod
    def getMessageHandler(self) -> IMessageHandler:
        pass

    @abstractmethod
    def setMessageHandler(self, handler: IMessageHandler = None):
        pass

    @abstractmethod
    def getILexStream(self) -> ILexStream:
        pass

    @abstractmethod
    def setLexStream(self, lexStream: ILexStream):
        pass

    # /**
    # * @deprecated replaced by @link #getFirstRealToken():
    # *
    # */
    # getFirstErrorToken(i: int):

    # /**
    # * @deprecated replaced by @link #getLastRealToken():
    # *
    # */
    # getLastErrorToken(i: int):

    @abstractmethod
    def makeToken(self, startLoc: int, endLoc: int, kind: int):
        pass

    @abstractmethod
    def makeAdjunct(self, startLoc: int, endLoc: int, kind: int):
        pass

    @abstractmethod
    def removeLastToken(self):
        pass

    @abstractmethod
    def getLineCount(self) -> int:
        pass

    @abstractmethod
    def getSize(self) -> int:
        pass

    @abstractmethod
    def remapTerminalSymbols(self, ordered_parser_symbols: list, eof_symbol: int):
        pass

    @abstractmethod
    def orderedTerminalSymbols(self) -> list:
        pass

    @abstractmethod
    def mapKind(self, kind: int) -> int:
        pass

    @abstractmethod
    def resetTokenStream(self):
        pass

    @abstractmethod
    def getStreamIndex(self) -> int:
        pass

    @abstractmethod
    def setStreamIndex(self, index: int):
        pass

    @abstractmethod
    def setStreamLength(self, length: int = None):
        pass

    @abstractmethod
    def addToken(self, token: IToken):
        pass

    @abstractmethod
    def addAdjunct(self, adjunct: IToken):
        pass

    @abstractmethod
    def orderedExportedSymbols(self) -> list:
        pass

    @abstractmethod
    def getTokens(self) -> ArrayList:
        pass

    @abstractmethod
    def getAdjuncts(self) -> ArrayList:
        pass

    @abstractmethod
    def getFollowingAdjuncts(self, i: int) -> list:
        pass

    @abstractmethod
    def getPrecedingAdjuncts(self, i: int) -> list:
        pass

    @abstractmethod
    def getIToken(self, i: int) -> IToken:
        pass

    @abstractmethod
    def getTokenText(self, i: int) -> str:
        pass

    @abstractmethod
    def getStartOffset(self, i: int) -> int:
        pass

    @abstractmethod
    def getEndOffset(self, i: int) -> int:
        pass

    @abstractmethod
    def getLineOffset(self, i: int) -> int:
        pass

    @abstractmethod
    def getLineNumberOfCharAt(self, i: int) -> int:
        pass

    @abstractmethod
    def getColumnOfCharAt(self, i: int) -> int:
        pass

    @abstractmethod
    def getTokenLength(self, i: int) -> int:
        pass

    @abstractmethod
    def getLineNumberOfTokenAt(self, i: int) -> int:
        pass

    @abstractmethod
    def getEndLineNumberOfTokenAt(self, i: int) -> int:
        pass

    @abstractmethod
    def getColumnOfTokenAt(self, i: int) -> int:
        pass

    @abstractmethod
    def getEndColumnOfTokenAt(self, i: int) -> int:
        pass

    @abstractmethod
    def getInputChars(self) -> str:
        pass

    @abstractmethod
    def getInputBytes(self):
        pass

    @abstractmethod
    def toStringFromIndex(self, first_token: int, last_token: int) -> str:
        pass

    @abstractmethod
    def toString(self, t1: IToken, t2: IToken) -> str:
        pass

    @abstractmethod
    def getTokenIndexAtCharacter(self, offset: int) -> int:
        pass

    @abstractmethod
    def getTokenAtCharacter(self, offset: int) -> IToken:
        pass

    @abstractmethod
    def getTokenAt(self, i: int) -> IToken:
        pass

    @abstractmethod
    def dumpTokens(self):
        pass

    @abstractmethod
    def dumpToken(self, i: int):
        pass

    @abstractmethod
    def makeErrorToken(self, first: int, last: int, error: int, kind: int) -> int:
        pass
