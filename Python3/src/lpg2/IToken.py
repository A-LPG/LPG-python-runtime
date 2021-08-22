#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IToken(metaclass=ABCMeta):
    __slots__ = ()
    EOF: int = 0xffff

    @abstractmethod
    def getKind(self) -> int:
        pass

    @abstractmethod
    def setKind(self, kind: int):
        pass

    @abstractmethod
    def getStartOffset(self) -> int:
        pass

    @abstractmethod
    def setStartOffset(self, startOffset: int):
        pass

    @abstractmethod
    def getEndOffset(self) -> int:
        pass

    @abstractmethod
    def setEndOffset(self, endOffset: int):
        pass

    @abstractmethod
    def getTokenIndex(self) -> int:
        pass

    @abstractmethod
    def setTokenIndex(self, i: int):
        pass

    @abstractmethod
    def getAdjunctIndex(self) -> int:
        pass

    @abstractmethod
    def setAdjunctIndex(self, i: int):
        pass

    @abstractmethod
    def getPrecedingAdjuncts(self) -> list:
        pass

    @abstractmethod
    def getFollowingAdjuncts(self) -> list:
        pass

    @abstractmethod
    def getILexStream(self):
        pass

    @abstractmethod
    def getIPrsStream(self):
        pass

    @abstractmethod
    def getLine(self) -> int:
        pass

    @abstractmethod
    def getColumn(self) -> int:
        pass

    @abstractmethod
    def getEndLine(self) -> int:
        pass

    @abstractmethod
    def getEndColumn(self) -> int:
        pass

    @abstractmethod
    def toString(self) -> str:
        pass
