#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class TokenStream(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def getToken(self, end_token: int = None) -> int:
        pass

    @abstractmethod
    def getKind(self, i: int) -> int:
        pass

    @abstractmethod
    def getNext(self, i: int) -> int:
        pass

    @abstractmethod
    def getPrevious(self, i: int) -> int:
        pass

    @abstractmethod
    def getName(self, i: int) -> str:
        pass

    @abstractmethod
    def peek(self) -> int:
        pass

    @abstractmethod
    def reset(self, i: int = None):
        pass

    @abstractmethod
    def badToken(self) -> int:
        pass

    @abstractmethod
    def getLine(self, i: int) -> int:
        pass

    @abstractmethod
    def getColumn(self, i: int) -> int:
        pass

    @abstractmethod
    def getEndLine(self, i: int) -> int:
        pass

    @abstractmethod
    def getEndColumn(self, i: int) -> int:
        pass

    @abstractmethod
    def afterEol(self, i: int) -> int:
        pass

    @abstractmethod
    def getFileName(self) -> str:
        pass

    @abstractmethod
    def getStreamLength(self) -> int:
        pass

    @abstractmethod
    def getFirstRealToken(self, i: int) -> int:
        pass

    @abstractmethod
    def getLastRealToken(self, i: int) -> int:
        pass

    @abstractmethod
    def reportError(self, errorCode: int, leftToken: int, rightToken: int, errorInfo=None, errorToken: int = None):
        pass
