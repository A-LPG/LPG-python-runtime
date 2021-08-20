#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class BadParseException(Exception):

    def __init__(self, errorToken: int):
        super().__init__()
        self.error_token = errorToken
