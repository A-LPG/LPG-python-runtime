#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IAbstractArrayList(object):
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def getElementAt(self, i):
        pass

    @abstractmethod
    def getList(self):
        pass

    @abstractmethod
    def add(self, elt):
        pass
