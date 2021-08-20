#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from LexStream import LexStream
from IntSegmentedTuple import IntSegmentedTuple


class LpgLexStream(LexStream):

    def __init__(self, fileName: str, inputChars: str = None, tab: int = LexStream.DEFAULT_TAB,
                 lineOffsets: IntSegmentedTuple = None):
        super().__init__(fileName, inputChars, tab, lineOffsets)
