#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NullExportedSymbolsException(Exception):
    __slots__ = 'info'

    def __init__(self, info=None):

        if info is None:
            self.info = "NullExportedSymbolsException"
        else:
            self.info = info

    def toString(self):
        return self.info
