#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Monitor(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def isCancelled(self) -> bool:
        return False
