#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Monitor(object):
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def isCancelled(self):
        return False
