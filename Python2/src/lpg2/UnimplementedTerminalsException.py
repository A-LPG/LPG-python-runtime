#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UnimplementedTerminalsException(Exception):
    __slots__ = "symbols"

    def __init__(self, symbols):
        self.symbols = symbols

    def getSymbols(self):
        return self.symbols
