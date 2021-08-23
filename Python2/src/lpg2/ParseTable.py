#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class ParseTable(object):
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def baseCheck(self, index):
        pass

    @abstractmethod
    def rhs(self, index):
        pass

    @abstractmethod
    def baseAction(self, index):
        pass

    @abstractmethod
    def lhs(self, index):
        pass

    @abstractmethod
    def termCheck(self, index):
        pass

    @abstractmethod
    def termAction(self, index):
        pass

    @abstractmethod
    def asb(self, index):
        pass

    @abstractmethod
    def asr(self, index):
        pass

    @abstractmethod
    def nasb(self, index):
        pass

    @abstractmethod
    def nasr(self, index):
        pass

    @abstractmethod
    def terminalIndex(self, index):
        pass

    @abstractmethod
    def nonterminalIndex(self, index):
        pass

    @abstractmethod
    def scopePrefix(self, index):
        pass

    @abstractmethod
    def scopeSuffix(self, index):
        pass

    @abstractmethod
    def scopeLhs(self, index):
        pass

    @abstractmethod
    def scopeLa(self, index):
        pass

    @abstractmethod
    def scopeStateSet(self, index):
        pass

    @abstractmethod
    def scopeRhs(self, index):
        pass

    @abstractmethod
    def scopeState(self, index):
        pass

    @abstractmethod
    def inSymb(self, index):
        pass

    @abstractmethod
    def name(self, index):
        pass

    @abstractmethod
    def originalState(self, state):
        pass

    @abstractmethod
    def asi(self, state):
        pass

    @abstractmethod
    def nasi(self, state):
        pass

    @abstractmethod
    def inSymbol(self, state):
        pass

    @abstractmethod
    def ntAction(self, state, sym):
        pass

    @abstractmethod
    def tAction(self, act, sym):
        pass

    @abstractmethod
    def lookAhead(self, act, sym):
        pass

    @abstractmethod
    def getErrorSymbol(self):
        pass

    @abstractmethod
    def getScopeUbound(self):
        pass

    @abstractmethod
    def getScopeSize(self):
        pass

    @abstractmethod
    def getMaxNameLength(self):
        pass

    @abstractmethod
    def getNumStates(self):
        pass

    @abstractmethod
    def getNtOffset(self):
        pass

    @abstractmethod
    def getLaStateOffset(self):
        pass

    @abstractmethod
    def getMaxLa(self):
        pass

    @abstractmethod
    def getNumRules(self):
        pass

    @abstractmethod
    def getNumNonterminals(self):
        pass

    @abstractmethod
    def getNumSymbols(self):
        pass

    @abstractmethod
    def getStartState(self):
        pass

    @abstractmethod
    def getStartSymbol(self):
        pass

    @abstractmethod
    def getEoftSymbol(self):
        pass

    @abstractmethod
    def getEoltSymbol(self):
        pass

    @abstractmethod
    def getAcceptAction(self):
        pass

    @abstractmethod
    def getErrorAction(self):
        pass

    @abstractmethod
    def isNullable(self, symbol):
        pass

    @abstractmethod
    def isValidForParser(self):
        pass

    @abstractmethod
    def getBacktrack(self):
        pass
