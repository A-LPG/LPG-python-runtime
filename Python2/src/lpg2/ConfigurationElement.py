#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ConfigurationElement(object):
    __slots__ = ('next', 'last_element', 'stack_top', 'action_length',
                 'conflict_index', 'curtok', 'act')

    def __init__(self):
        self.next = None
        self.last_element = None
        self.stack_top = 0
        self.action_length = 0
        self.conflict_index = 0
        self.curtok = 0
        self.act = 0

    def retrieveStack(self, stack):
        tail = self.last_element
        i = self.stack_top
        while i >= 0:
            if not tail:
                return
            stack[i] = tail.number
            tail = tail.parent
            i -= 1
        return
