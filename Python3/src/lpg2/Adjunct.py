#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AbstractToken import AbstractToken
from Protocol import IPrsStream


class Adjunct(AbstractToken):

    def __init__(self, startOffset: int, endOffset: int, kind: int, prsStream: IPrsStream = None):
        super().__init__(startOffset, endOffset, kind, prsStream)

    def getFollowingAdjuncts(self) -> list:
        return []

    def getPrecedingAdjuncts(self) -> list:
        return []
