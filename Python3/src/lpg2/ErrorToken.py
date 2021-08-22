#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.IPrsStream import IToken
from lpg2.Token import Token


class ErrorToken(Token):
    __slots__ = ('firstToken', 'lastToken', 'errorToken')

    def __init__(self, firstToken: IToken, lastToken: IToken, errorToken: IToken, startOffset: int, endOffset: int,
                 kind: int):
        super().__init__(startOffset, endOffset, kind, firstToken.getIPrsStream())
        self.firstToken = firstToken
        self.lastToken = lastToken
        self.errorToken = errorToken

    def getFirstToken(self) -> IToken:
        return self.getFirstRealToken()

    def getFirstRealToken(self) -> IToken:
        return self.firstToken

    def getLastToken(self) -> IToken:
        return self.getLastRealToken()

    def getLastRealToken(self) -> IToken:
        return self.lastToken

    def getErrorToken(self) -> IToken:
        return self.errorToken

    def getPrecedingAdjuncts(self) -> list:
        return self.firstToken.getPrecedingAdjuncts()

    def getFollowingAdjuncts(self) -> list:
        return self.lastToken.getFollowingAdjuncts()
