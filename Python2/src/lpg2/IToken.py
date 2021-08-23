#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IToken(object):
    __metaclass__ = ABCMeta
    __slots__ = ()
    EOF = 0xffff

    @abstractmethod
    def getKind(self):
        pass

    @abstractmethod
    def setKind(self, kind):
        pass

    @abstractmethod
    def getStartOffset(self):
        pass

    @abstractmethod
    def setStartOffset(self, startOffset):
        pass

    @abstractmethod
    def getEndOffset(self):
        pass

    @abstractmethod
    def setEndOffset(self, endOffset):
        pass

    @abstractmethod
    def getTokenIndex(self):
        pass

    @abstractmethod
    def setTokenIndex(self, i):
        pass

    @abstractmethod
    def getAdjunctIndex(self):
        pass

    @abstractmethod
    def setAdjunctIndex(self, i):
        pass

    @abstractmethod
    def getPrecedingAdjuncts(self):
        pass

    @abstractmethod
    def getFollowingAdjuncts(self):
        pass

    @abstractmethod
    def getILexStream(self):
        pass

    @abstractmethod
    def getIPrsStream(self):
        pass

    @abstractmethod
    def getLine(self):
        pass

    @abstractmethod
    def getColumn(self):
        pass

    @abstractmethod
    def getEndLine(self):
        pass

    @abstractmethod
    def getEndColumn(self):
        pass

    @abstractmethod
    def toString(self):
        pass
