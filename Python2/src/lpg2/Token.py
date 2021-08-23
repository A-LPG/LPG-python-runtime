#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.AbstractToken import AbstractToken


class Token(AbstractToken):
    __slots__ = ()

    def __init__(self, startOffset, endOffset, kind, iPrsStream=None):
        super(Token, self).__init__(startOffset, endOffset, kind, iPrsStream)

    def getFollowingAdjuncts(self):
        stream = self.getIPrsStream()
        return [] if stream is None else stream.getFollowingAdjuncts(self.getTokenIndex())

    def getPrecedingAdjuncts(self):
        stream = self.getIPrsStream()
        return [] if stream is None else stream.getPrecedingAdjuncts(self.getTokenIndex())
