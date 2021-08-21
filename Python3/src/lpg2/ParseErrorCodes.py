#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class ParseErrorCodes(object):

    LEX_ERROR_CODE = 0
    ERROR_CODE = 1
    BEFORE_CODE = 2
    INSERTION_CODE = 3
    INVALID_CODE = 4
    SUBSTITUTION_CODE = 5
    SECONDARY_CODE = 5
    DELETION_CODE = 6
    MERGE_CODE = 7
    MISPLACED_CODE = 8
    SCOPE_CODE = 9
    EOF_CODE = 10
    INVALID_TOKEN_CODE = 11
    ERROR_RULE_ERROR_CODE = 11
    ERROR_RULE_WARNING_CODE = 12
    NO_MESSAGE_CODE = 13

    MANUAL_CODE = 14

    errorMsgText: list = [
        "unexpected character ignored",  # $NON-NLS-1$
        "parsing terminated at this token",  # $NON-NLS-1$
        " inserted before this token",  # $NON-NLS-1$
        " expected after this token",  # $NON-NLS-1$
        "unexpected input discarded",  # $NON-NLS-1$
        " expected instead of this input",  # $NON-NLS-1$
        " unexpected token(s): ignored",  # $NON-NLS-1$
        " formed from merged tokens",  # $NON-NLS-1$
        "misplaced construct(s):",  # $NON-NLS-1$
        " inserted to complete scope",  # $NON-NLS-1$
        " reached after this token",  # $NON-NLS-1$
        " is invalid",  # $NON-NLS-1$
        " is ignored",  # $NON-NLS-1$
        ""  # $NON-NLS-1$
    ]
