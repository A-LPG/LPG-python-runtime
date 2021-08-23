#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import abstractmethod
from lpg2.TokenStream import TokenStream


class ILexStream(TokenStream):
    __slots__ = ()

    @abstractmethod
    def getIPrsStream(self):
        pass

    @abstractmethod
    def setPrsStream(self, stream):
        pass

    @abstractmethod
    def getLineCount(self):
        pass

    @abstractmethod
    def orderedExportedSymbols(self):
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
    def getCharValue(self, i):
        pass

    @abstractmethod
    def getIntValue(self, i):
        pass

    @abstractmethod
    def makeToken(self, start_loc, end_loc, kind):
        pass

    @abstractmethod
    def setMessageHandler(self, handler):
        pass

    @abstractmethod
    def getMessageHandler(self):
        pass

    @abstractmethod
    def getLocation(self, left_loc, right_loc):
        pass

    @abstractmethod
    def reportLexicalError(self, left_loc, right_loc, error_code=None,
                           error_left_loc_arg=None, error_right_loc_arg=None, error_info=None):
        pass

    @abstractmethod
    def toString(self, startOffset, endOffset):
        pass
