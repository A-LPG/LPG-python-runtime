#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.StateElement import StateElement


class ConfigurationElement(object):

    def __init__(self, info: str = None):
        self.next: ConfigurationElement = None
        self.last_element: StateElement = None
        self.stack_top: int = 0
        self.action_length: int = 0
        self.conflict_index: int = 0
        self.curtok: int = 0
        self.act: int = 0

    def retrieveStack(self, stack):
        tail = self.last_element
        i: int = self.stack_top
        while i >= 0:
            if not tail:
                return
            stack[i] = tail.number
            tail = tail.parent
            i -= 1
        return
