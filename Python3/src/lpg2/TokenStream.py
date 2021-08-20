#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class TokenStream(metaclass=ABCMeta):

    @abstractmethod
    def getToken(self, end_token: int = None) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getKind(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getNext(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getPrevious(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getName(self, i: int) -> str:
        '''please Implemente in subclass'''

    @abstractmethod
    def peek(self) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def reset(self, i: int = None):
        '''please Implemente in subclass'''

    @abstractmethod
    def badToken(self) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getLine(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getColumn(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getEndLine(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getEndColumn(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def afterEol(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getFileName(self) -> str:
        '''please Implemente in subclass'''

    @abstractmethod
    def getStreamLength(self) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getFirstRealToken(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def getLastRealToken(self, i: int) -> int:
        '''please Implemente in subclass'''

    @abstractmethod
    def reportError(self, errorCode: int, leftToken: int, rightToken: int, errorInfo=None, errorToken: int = None):
        '''please Implemente in subclass'''
