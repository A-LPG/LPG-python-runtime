#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta
from lpg2.IToken import IToken


class AbstractToken(IToken):
    __metaclass__ = ABCMeta
    __slots__ = (
        'iPrsStream', 'startOffset', 'endOffset', 'kind', 'tokenIndex',
        'adjunctIndex'
    )

    def __init__(self, startOffset=0, endOffset=0, kind=0, iPrsStream=None):
        self.iPrsStream = iPrsStream
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.kind = kind
        self.tokenIndex = 0
        self.adjunctIndex = 0

    def getKind(self):
        return self.kind

    def setKind(self, kind):
        self.kind = kind

    def getStartOffset(self):
        return self.startOffset

    def setStartOffset(self, startOffset):
        self.startOffset = startOffset

    def getEndOffset(self):
        return self.endOffset

    def setEndOffset(self, endOffset):
        self.endOffset = endOffset

    def getTokenIndex(self):
        return self.tokenIndex

    def setTokenIndex(self, tokenIndex):
        self.tokenIndex = tokenIndex

    def setAdjunctIndex(self, adjunctIndex):
        self.adjunctIndex = adjunctIndex

    def getAdjunctIndex(self):
        return self.adjunctIndex

    def getIPrsStream(self):
        return self.iPrsStream

    def getILexStream(self):
        return None if self.iPrsStream is None else self.iPrsStream.getILexStream()

    def getLine(self):
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getLineNumberOfCharAt(self.startOffset)

    def getColumn(self):
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getColumnOfCharAt(self.startOffset)

    def getEndLine(self):
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getLineNumberOfCharAt(self.endOffset)

    def getEndColumn(self):
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getColumnOfCharAt(self.endOffset)

    def toString(self):
        return "<toString>" if self.iPrsStream is None else self.iPrsStream.toString(self, self)
