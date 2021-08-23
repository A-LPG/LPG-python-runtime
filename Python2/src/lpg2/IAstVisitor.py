#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IAstVisitor(object):
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def preVisit(self, element):
        pass

    @abstractmethod
    def postVisit(self, element):
        pass
