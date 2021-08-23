#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.AbstractToken import AbstractToken


class Adjunct(AbstractToken):
    __slots__ = ()

    def __init__(self, start_offset, end_offset, kind, prs_stream=None):
        super(Adjunct, self).__init__(start_offset, end_offset, kind, prs_stream)

    def getFollowingAdjuncts(self):
        return []

    def getPrecedingAdjuncts(self):
        return []
