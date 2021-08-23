#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod



class IAst(object):
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def getNextAst(self):
        pass

    @abstractmethod
    def getParent(self):
        pass

    @abstractmethod
    def getLeftIToken(self):
        pass

    @abstractmethod
    def getRightIToken(self):
        pass

    @abstractmethod
    def getPrecedingAdjuncts(self):
        pass

    @abstractmethod
    def getFollowingAdjuncts(self):
        pass

    @abstractmethod
    def getChildren(self):
        pass

    @abstractmethod
    def getAllChildren(self):
        pass

    @abstractmethod
    def accept(self, v):
        pass
