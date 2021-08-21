#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IAstVisitor(metaclass=ABCMeta):

    @abstractmethod
    def preVisit(self, element) -> bool:
        pass

    @abstractmethod
    def postVisit(self, element) -> None:
        pass
