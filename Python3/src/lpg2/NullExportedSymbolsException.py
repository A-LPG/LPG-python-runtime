#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NullExportedSymbolsException(Exception):

    def __init__(self, info: str = None):
        super().__init__()
        if info is None:
            self.info = "NullExportedSymbolsException"
        else:
            self.info = info

    def toString(self) -> str:
        return self.info
