#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import abstractmethod
from lpg2 import IMessageHandler

from lpg2.TokenStream import TokenStream


class ILexStream(TokenStream):

    @abstractmethod
    def getIPrsStream(self):
        pass

    @abstractmethod
    def setPrsStream(self, stream):
        pass

    @abstractmethod
    def getLineCount(self) -> int:
        pass

    @abstractmethod
    def orderedExportedSymbols(self) -> list:
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
    def getCharValue(self, i: int) -> str:
        pass

    @abstractmethod
    def getIntValue(self, i: int) -> int:
        pass

    @abstractmethod
    def makeToken(self, start_loc: int, end_loc: int, kind: int):
        pass

    @abstractmethod
    def setMessageHandler(self, handler: IMessageHandler):
        pass

    @abstractmethod
    def getMessageHandler(self) -> IMessageHandler:
        pass

    @abstractmethod
    def getLocation(self, left_loc: int, right_loc: int) -> int:
        pass

    @abstractmethod
    def reportLexicalError(self, left_loc: int, right_loc: int, error_code: int = None,
                           error_left_loc_arg: int = None, error_right_loc_arg: int = None, error_info: list = None):
        pass

    @abstractmethod
    def toString(self, startOffset: int, endOffset: int) -> str:
        pass
