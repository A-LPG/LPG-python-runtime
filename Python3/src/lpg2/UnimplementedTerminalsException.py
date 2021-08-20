#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class UnimplementedTerminalsException(Exception):

    def __init__(self, symbols):
        super().__init__()
        self.symbols = symbols

    def getSymbols(self):
        return self.symbols
