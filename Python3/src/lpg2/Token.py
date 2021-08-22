#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.AbstractToken import AbstractToken
from lpg2.IPrsStream import IPrsStream


class Token(AbstractToken):
    __slots__ = ()

    def __init__(self, startOffset: int, endOffset: int, kind: int, iPrsStream: IPrsStream = None):
        super().__init__(startOffset, endOffset, kind, iPrsStream)

    def getFollowingAdjuncts(self) -> list:
        stream = self.getIPrsStream()
        return [] if stream is None else stream.getFollowingAdjuncts(self.getTokenIndex())

    def getPrecedingAdjuncts(self) -> list:
        stream = self.getIPrsStream()
        return [] if stream is None else stream.getPrecedingAdjuncts(self.getTokenIndex())
