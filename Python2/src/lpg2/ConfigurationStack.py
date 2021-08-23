#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.ConfigurationElement import ConfigurationElement
from lpg2.StateElement import StateElement
from lpg2.ObjectTuple import ObjectTuple


class ConfigurationStack(object):
    TABLE_SIZE = 1021  # 1021 is a prime
    __slots__ = ('prs', 'state_element_size', 'state_root', 'table',
                 'configuration_stack', 'max_configuration_size', 'stacks_size')

    def __init__(self, prs):
        self.prs = prs
        self.state_element_size = 1
        self.state_root = StateElement()

        self.state_root.number = prs.getStartState()

        self.table = [None] * ConfigurationStack.TABLE_SIZE
        self.configuration_stack = ObjectTuple(1 << 12)
        self.max_configuration_size = 0
        self.stacks_size = 0

    def makeStateList(self, parent, stack, index, stack_top):
        i = index
        while i <= stack_top:
            self.state_element_size += 1

            state = StateElement()

            state.number = stack[i]
            state.parent = parent

            parent.children = state

            parent = state
            i += 1

        return parent

    def findOrInsertStack(self, root, stack, index, stack_top):
        state_number = stack[index]
        p = root
        while p is not None:
            if p.number == state_number:
                if index == stack_top:
                    return p
                else:
                    if p.children is None:
                        return self.makeStateList(p, stack, index + 1, stack_top)
                    else:
                        return self.findOrInsertStack(p.children, stack, index + 1, stack_top)

            p = p.siblings

        self.state_element_size += 1

        node = StateElement()
        node.number = state_number
        node.parent = root.parent
        node.siblings = root.siblings
        root.siblings = node

        return node if index == stack_top else self.makeStateList(node, stack, index + 1, stack_top)

    def findConfiguration(self, stack, stack_top, curtok):

        last_element = self.findOrInsertStack(self.state_root, stack, 0, stack_top)

        hash_address = curtok % ConfigurationStack.TABLE_SIZE
        configuration = self.table[hash_address]
        while configuration:

            if configuration.curtok == curtok and last_element == configuration.last_element:
                return True
            configuration = configuration.next

        return False

    def push(self, stack, stack_top, conflict_index, curtok, action_length):

        configuration = ConfigurationElement()
        hash_address = curtok % ConfigurationStack.TABLE_SIZE

        configuration.next = self.table[hash_address]

        self.table[hash_address] = configuration
        self.max_configuration_size += 1  # keep track of int of configurations

        configuration.stack_top = stack_top
        self.stacks_size += (stack_top + 1)  # keep track of int of stack elements processed
        configuration.last_element = self.findOrInsertStack(self.state_root, stack, 0, stack_top)
        configuration.conflict_index = conflict_index
        configuration.curtok = curtok
        configuration.action_length = action_length

        self.configuration_stack.add(configuration)
        return

    def pop(self):

        if self.configuration_stack.size() > 0:
            index = self.configuration_stack.size() - 1
            configuration = self.configuration_stack.get(index)

            configuration.act = self.prs.baseAction(configuration.conflict_index)
            configuration.conflict_index += 1

            if self.prs.baseAction(configuration.conflict_index) == 0:
                self.configuration_stack.reset(index)

            return configuration
        else:
            return None

    def top(self):

        if self.configuration_stack.size() > 0:

            index = self.configuration_stack.size() - 1
            configuration = self.configuration_stack.get(index)
            configuration.act = self.prs.baseAction(configuration.conflict_index)
            return configuration
        else:
            return None

    def size(self):
        return self.configuration_stack.size()

    def maxConfigurationSize(self):
        return self.max_configuration_size

    def numStateElements(self):
        return self.state_element_size

    def stacksSize(self):
        return self.stacks_size
