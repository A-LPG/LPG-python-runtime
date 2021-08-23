#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.LexStream import LexStream


class LpgLexStream(LexStream):
    __slots__ = ()

    def __init__(self, fileName, inputChars=None, tab=LexStream.DEFAULT_TAB,
                 lineOffsets=None):
        super(LpgLexStream, self).__init__(fileName, inputChars, tab, lineOffsets)
