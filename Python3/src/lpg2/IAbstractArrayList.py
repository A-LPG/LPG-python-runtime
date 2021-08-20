#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from Utils import ArrayList

class IAbstractArrayList(metaclass=ABCMeta):

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def getElementAt(self, i: int):
        pass

    @abstractmethod
    def getList(self) -> ArrayList:
        pass

    @abstractmethod
    def add(self, elt):
        pass