#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class StateElement(object):
    __slots__ = ('parent', 'children', 'siblings', 'number')

    def __init__(self):
        self.parent: StateElement = None
        self.children: StateElement = None
        self.siblings: StateElement = None
        self.number: int = 0
