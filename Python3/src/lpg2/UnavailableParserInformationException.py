#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UnavailableParserInformationException(Exception):

    def __init__(self, info: str = None):
        super().__init__()
        if info is None:
            self.info = "Unavailable parser Information Exception"
        else:
            self.info = info

    def toString(self) -> str:
        return self.info
