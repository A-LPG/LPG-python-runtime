#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from lpg2.IToken import IToken
from lpg2.Utils import ArrayList
from lpg2.IAstVisitor import IAstVisitor


class IAst(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def getNextAst(self):
        pass

    @abstractmethod
    def getParent(self):
        pass

    @abstractmethod
    def getLeftIToken(self) -> IToken:
        pass

    @abstractmethod
    def getRightIToken(self) -> IToken:
        pass

    @abstractmethod
    def getPrecedingAdjuncts(self) -> list:
        pass

    @abstractmethod
    def getFollowingAdjuncts(self) -> list:
        pass

    @abstractmethod
    def getChildren(self) -> ArrayList:
        pass

    @abstractmethod
    def getAllChildren(self) -> ArrayList:
        pass

    @abstractmethod
    def accept(self, v: IAstVisitor) -> None:
        pass
