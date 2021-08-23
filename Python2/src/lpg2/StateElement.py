#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class StateElement(object):
    __slots__ = ('parent', 'children', 'siblings', 'number')

    def __init__(self):
        self.parent = None
        self.children = None
        self.siblings = None
        self.number = 0
