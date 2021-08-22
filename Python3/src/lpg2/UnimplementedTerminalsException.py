#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.Utils import ArrayList


class UnimplementedTerminalsException(Exception):
    __slots__ = "symbols"

    def __init__(self, symbols: ArrayList):
        super().__init__()
        self.symbols = symbols

    def getSymbols(self) -> ArrayList:
        return self.symbols
