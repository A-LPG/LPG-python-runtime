#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class BadParseException(Exception):
    __slots__ = 'error_token'

    def __init__(self, errorToken):

        self.error_token = errorToken
