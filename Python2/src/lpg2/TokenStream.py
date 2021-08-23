#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class TokenStream(object):
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def getToken(self, end_token=None):
        pass

    @abstractmethod
    def getKind(self, i):
        pass

    @abstractmethod
    def getNext(self, i):
        pass

    @abstractmethod
    def getPrevious(self, i):
        pass

    @abstractmethod
    def getName(self, i):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def reset(self, i=None):
        pass

    @abstractmethod
    def badToken(self):
        pass

    @abstractmethod
    def getLine(self, i):
        pass

    @abstractmethod
    def getColumn(self, i):
        pass

    @abstractmethod
    def getEndLine(self, i):
        pass

    @abstractmethod
    def getEndColumn(self, i):
        pass

    @abstractmethod
    def afterEol(self, i):
        pass

    @abstractmethod
    def getFileName(self):
        pass

    @abstractmethod
    def getStreamLength(self):
        pass

    @abstractmethod
    def getFirstRealToken(self, i):
        pass

    @abstractmethod
    def getLastRealToken(self, i):
        pass

    @abstractmethod
    def reportError(self, errorCode, leftToken, rightToken, errorInfo=None, errorToken=None):
        pass
