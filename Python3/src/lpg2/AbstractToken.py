#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABC

from lpg2.IPrsStream import IPrsStream
from lpg2.IToken import IToken


class AbstractToken(IToken, ABC):
    __slots__ = (
        'iPrsStream', 'startOffset', 'endOffset', 'kind', 'tokenIndex',
        'adjunctIndex'
    )

    def __init__(self, startOffset: int = 0, endOffset: int = 0, kind: int = 0, iPrsStream: IPrsStream = None):
        super().__init__()
        self.iPrsStream = iPrsStream
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.kind = kind
        self.tokenIndex: int = 0
        self.adjunctIndex: int = 0

    def getKind(self) -> int:
        return self.kind

    def setKind(self, kind: int):
        self.kind = kind

    def getStartOffset(self) -> int:
        return self.startOffset

    def setStartOffset(self, startOffset: int):
        self.startOffset = startOffset

    def getEndOffset(self) -> int:
        return self.endOffset

    def setEndOffset(self, endOffset: int):
        self.endOffset = endOffset

    def getTokenIndex(self) -> int:
        return self.tokenIndex

    def setTokenIndex(self, tokenIndex: int):
        self.tokenIndex = tokenIndex

    def setAdjunctIndex(self, adjunctIndex: int):
        self.adjunctIndex = adjunctIndex

    def getAdjunctIndex(self) -> int:
        return self.adjunctIndex

    def getIPrsStream(self):
        return self.iPrsStream

    def getILexStream(self):
        return None if self.iPrsStream is None else self.iPrsStream.getILexStream()

    def getLine(self) -> int:
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getLineNumberOfCharAt(self.startOffset)

    def getColumn(self) -> int:
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getColumnOfCharAt(self.startOffset)

    def getEndLine(self) -> int:
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getLineNumberOfCharAt(self.endOffset)

    def getEndColumn(self) -> int:
        return 0 if self.iPrsStream is None else self.iPrsStream.getILexStream().getColumnOfCharAt(self.endOffset)

    def toString(self) -> str:
        return "<toString>" if self.iPrsStream is None else self.iPrsStream.toString(self, self)
