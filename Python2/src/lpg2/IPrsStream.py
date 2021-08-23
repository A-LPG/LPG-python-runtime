#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod
from lpg2.TokenStream import TokenStream


class IPrsStream(TokenStream):
    __slots__ = ()

    @abstractmethod
    def getMessageHandler(self):
        pass

    @abstractmethod
    def setMessageHandler(self, handler=None):
        pass

    @abstractmethod
    def getILexStream(self):
        pass

    @abstractmethod
    def setLexStream(self, lexStream):
        pass

    # /**
    # * @deprecated replaced by @link #getFirstRealToken():
    # *
    # */
    # getFirstErrorToken(i):

    # /**
    # * @deprecated replaced by @link #getLastRealToken():
    # *
    # */
    # getLastErrorToken(i):

    @abstractmethod
    def makeToken(self, startLoc, endLoc, kind):
        pass

    @abstractmethod
    def makeAdjunct(self, startLoc, endLoc, kind):
        pass

    @abstractmethod
    def removeLastToken(self):
        pass

    @abstractmethod
    def getLineCount(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def remapTerminalSymbols(self, ordered_parser_symbols, eof_symbol):
        pass

    @abstractmethod
    def orderedTerminalSymbols(self):
        pass

    @abstractmethod
    def mapKind(self, kind):
        pass

    @abstractmethod
    def resetTokenStream(self):
        pass

    @abstractmethod
    def getStreamIndex(self):
        pass

    @abstractmethod
    def setStreamIndex(self, index):
        pass

    @abstractmethod
    def setStreamLength(self, length=None):
        pass

    @abstractmethod
    def addToken(self, token):
        pass

    @abstractmethod
    def addAdjunct(self, adjunct):
        pass

    @abstractmethod
    def orderedExportedSymbols(self):
        pass

    @abstractmethod
    def getTokens(self):
        pass

    @abstractmethod
    def getAdjuncts(self):
        pass

    @abstractmethod
    def getFollowingAdjuncts(self, i):
        pass

    @abstractmethod
    def getPrecedingAdjuncts(self, i):
        pass

    @abstractmethod
    def getIToken(self, i):
        pass

    @abstractmethod
    def getTokenText(self, i):
        pass

    @abstractmethod
    def getStartOffset(self, i):
        pass

    @abstractmethod
    def getEndOffset(self, i):
        pass

    @abstractmethod
    def getLineOffset(self, i):
        pass

    @abstractmethod
    def getLineNumberOfCharAt(self, i):
        pass

    @abstractmethod
    def getColumnOfCharAt(self, i):
        pass

    @abstractmethod
    def getTokenLength(self, i):
        pass

    @abstractmethod
    def getLineNumberOfTokenAt(self, i):
        pass

    @abstractmethod
    def getEndLineNumberOfTokenAt(self, i):
        pass

    @abstractmethod
    def getColumnOfTokenAt(self, i):
        pass

    @abstractmethod
    def getEndColumnOfTokenAt(self, i):
        pass

    @abstractmethod
    def getInputChars(self):
        pass

    @abstractmethod
    def getInputBytes(self):
        pass

    @abstractmethod
    def toStringFromIndex(self, first_token, last_token):
        pass

    @abstractmethod
    def toString(self, t1, t2):
        pass

    @abstractmethod
    def getTokenIndexAtCharacter(self, offset):
        pass

    @abstractmethod
    def getTokenAtCharacter(self, offset):
        pass

    @abstractmethod
    def getTokenAt(self, i):
        pass

    @abstractmethod
    def dumpTokens(self):
        pass

    @abstractmethod
    def dumpToken(self, i):
        pass

    @abstractmethod
    def makeErrorToken(self, first, last, error, kind):
        pass
