#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.AbstractToken import AbstractToken
from lpg2.IPrsStream import IPrsStream


class Adjunct(AbstractToken):
    __slots__ = ()

    def __init__(self, start_offset: int, end_offset: int, kind: int, prs_stream: IPrsStream = None):
        super().__init__(start_offset, end_offset, kind, prs_stream)

    def getFollowingAdjuncts(self) -> list:
        return []

    def getPrecedingAdjuncts(self) -> list:
        return []
