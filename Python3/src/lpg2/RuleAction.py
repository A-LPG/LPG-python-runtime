#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class RuleAction(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def ruleAction(self, ruleNumber: int) -> None:
        pass
