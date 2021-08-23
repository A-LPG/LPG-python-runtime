#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.Token import Token


class ErrorToken(Token):
    __slots__ = ('firstToken', 'lastToken', 'errorToken')

    def __init__(self, firstToken, lastToken, errorToken, startOffset, endOffset, kind):
        Token.__init__(startOffset, endOffset, kind, firstToken.getIPrsStream())
        self.firstToken = firstToken
        self.lastToken = lastToken
        self.errorToken = errorToken

    def getFirstToken(self):
        return self.getFirstRealToken()

    def getFirstRealToken(self):
        return self.firstToken

    def getLastToken(self):
        return self.getLastRealToken()

    def getLastRealToken(self):
        return self.lastToken

    def getErrorToken(self):
        return self.errorToken

    def getPrecedingAdjuncts(self):
        return self.firstToken.getPrecedingAdjuncts()

    def getFollowingAdjuncts(self):
        return self.lastToken.getFollowingAdjuncts()
