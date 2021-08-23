#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TokenStreamNotIPrsStreamException(Exception):
    __slots__ = 'info'

    def __init__(self, info=None):

        if info is None:
            self.info = "TokenStreamNotIPrsStreamException"
        else:
            self.info = info

    def toString(self):
        return self.info
