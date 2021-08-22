#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.LexStream import LexStream
from lpg2.IntSegmentedTuple import IntSegmentedTuple


class LpgLexStream(LexStream):
    __slots__ = ()

    def __init__(self, fileName: str, inputChars: str = None, tab: int = LexStream.DEFAULT_TAB,
                 lineOffsets: IntSegmentedTuple = None):
        super().__init__(fileName, inputChars, tab, lineOffsets)
