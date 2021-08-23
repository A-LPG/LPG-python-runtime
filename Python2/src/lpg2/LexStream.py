#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lpg2.ILexStream import ILexStream
from lpg2.ParseErrorCodes import ParseErrorCodes

from lpg2.IntSegmentedTuple import IntSegmentedTuple

import codecs


#
# LexStream contains an array of characters as the input stream to be parsed.
# There are methods to retrieve and classify characters.
# The lexparser "token" is implemented simply as the index of the next character in the array.
# The user must subclass LexStreamBase and implement the abstract methods: getKind.
#
class LexStream(ILexStream):
    DEFAULT_TAB = 1
    __slots__ = ('index', 'streamLength', 'inputChars', 'fileName', 'lineOffsets', 'tab', 'prsStream', 'errMsg')

    def __init__(self, fileName, inputChars=None, tab=DEFAULT_TAB,
                 lineOffsets=None):
        self.index = -1
        self.streamLength = 0
        self.inputChars = ""
        self.fileName = ""
        self.lineOffsets = None
        self.tab = self.DEFAULT_TAB

        self.prsStream = None
        self.errMsg = None
        self.lineOffsets = IntSegmentedTuple(12)
        self.setLineOffset(-1)
        self.tab = tab
        self.initialize(fileName, inputChars, lineOffsets)

    def thisTab(self, tab=DEFAULT_TAB):
        self.lineOffsets = IntSegmentedTuple(12)
        self.setLineOffset(-1)
        self.tab = tab

    @staticmethod
    def readDataFrom(fileName, encoding='utf-8', errors='strict'):
        # read binary to avoid line ending conversion
        with open(fileName, 'rb') as file_item:
            _bytes = file_item.read()
            return codecs.decode(_bytes, encoding, errors)

    def initialize(self, fileName, input_content=None, lineOffsets=None):
        if input_content is None:
            try:
                input_content = self.readDataFrom(fileName, "utf-8")
            except Exception as ex:
                print(str(ex))
                raise ex

        if input_content is None:
            return

        self.setInputChars(input_content)
        self.setStreamLength(input_content.__len__())
        self.setFileName(fileName)
        if lineOffsets is not None:
            self.lineOffsets = lineOffsets
        else:
            self.computeLineOffsets()

    def computeLineOffsets(self):
        self.lineOffsets.reset()
        self.setLineOffset(-1)
        for i in range(0, self.inputChars.__len__()):
            if ord(self.inputChars[i]) == 0x0A:
                self.setLineOffset(i)

    def setInputChars(self, inputChars):
        self.inputChars = inputChars
        self.index = -1  # reset the start index to the beginning of the input

    def getInputChars(self):
        return self.inputChars

    def setFileName(self, fileName):
        self.fileName = fileName

    def getFileName(self):
        return self.fileName

    def setLineOffsets(self, lineOffsets):
        self.lineOffsets = lineOffsets

    def getLineOffsets(self):
        return self.lineOffsets

    def setTab(self, tab):
        self.tab = tab

    def getTab(self):
        return self.tab

    def setStreamIndex(self, index):
        self.index = index

    def getStreamIndex(self):
        return self.index

    def setStreamLength(self, length):
        self.streamLength = length

    def getStreamLength(self):
        return self.streamLength

    def setLineOffset(self, i):
        self.lineOffsets.add(i)

    def getLineOffset(self, i):
        return self.lineOffsets.get(i)

    def setPrsStream(self, stream):
        stream.setLexStream(self)
        self.prsStream = stream

    def getIPrsStream(self):
        return self.prsStream

    def orderedExportedSymbols(self):
        return []

    def getCharValue(self, i):
        return self.inputChars[i]

    def getIntValue(self, i):
        return ord(self.inputChars[i])

    def getLineCount(self):
        return self.lineOffsets.size() - 1

    def getLineNumberOfCharAt(self, i):
        index = self.lineOffsets.binarySearch(i)
        return -index if index < 0 else (1 if index == 0 else index)

    def getColumnOfCharAt(self, i):
        lineNo = self.getLineNumberOfCharAt(i)
        start = self.lineOffsets.get(lineNo - 1)
        if start + 1 >= self.streamLength:
            return 1
        for k in range(start + 1, i):
            if self.inputChars[k] == '\t':
                offset = (k - start) - 1
                start -= ((self.tab - 1) - offset % self.tab)

        return i - start

    def getToken2(self):
        self.index = self.getNext(self.index)
        return self.index

    def getToken(self, end_token=None):
        if end_token is None:
            return self.getToken2()

        self.index = (self.getNext(self.index) if self.index < end_token else self.streamLength)
        return self.index

    def getKind(self, i):
        return 0

    def next(self, i):
        return self.getNext(i)

    def getNext(self, i):
        i += 1
        return i if i < self.streamLength else self.streamLength

    def previous(self, i):
        return self.getPrevious(i)

    def getPrevious(self, i):
        return 0 if i <= 0 else i - 1

    def getName(self, i):
        return "" if i >= self.getStreamLength() else "" + self.getCharValue(i)

    def peek(self):
        return self.getNext(self.index)

    def reset(self, i=None):
        if i is not None:
            self.index = i - 1
        else:
            self.index = -1

    def badToken(self):
        return 0

    def getLine(self, i=None):
        if i is None:
            return self.getLineCount()

        return self.getLineNumberOfCharAt(i)

    def getColumn(self, i):
        return self.getColumnOfCharAt(i)

    def getEndLine(self, i):
        return self.getLine(i)

    def getEndColumn(self, i):
        return self.getColumnOfCharAt(i)

    def afterEol(self, i):
        return True if i < 1 else self.getLineNumberOfCharAt(i - 1) < self.getLineNumberOfCharAt(i)

    def getFirstErrorToken(self, i):
        return self.getFirstRealToken(i)

    def getFirstRealToken(self, i):
        return i

    def getLastErrorToken(self, i):
        return self.getLastRealToken(i)

    def getLastRealToken(self, i):
        return i

    def setMessageHandler(self, handler):
        self.errMsg = handler

    def getMessageHandler(self):
        return self.errMsg

    def makeToken(self, start_loc, end_loc, kind):
        if self.prsStream is not None:
            self.prsStream.makeToken(start_loc, end_loc, kind)
        else:
            self.reportLexicalError(start_loc, end_loc)

    '''/**
     * See IMessaageHandler for a description of the int[] return value.
     */'''

    def getLocation(self, left_loc, right_loc):
        length = (right_loc if right_loc < self.streamLength else self.streamLength - 1) - left_loc + 1
        return [left_loc,
                length,
                self.getLineNumberOfCharAt(left_loc),
                self.getColumnOfCharAt(left_loc),
                self.getLineNumberOfCharAt(right_loc),
                self.getColumnOfCharAt(right_loc)
                ]

    def reportLexicalError(self, left_loc, right_loc, error_code=None,
                           error_left_loc_arg=None, error_right_loc_arg=None, error_info=None):

        error_left_loc = 0
        if error_left_loc_arg is not None:
            error_left_loc = error_left_loc_arg

        error_right_loc = 0
        if error_right_loc_arg is not None:
            error_right_loc = error_right_loc_arg

        if error_info is None:
            error_info = []

        if error_code is None:
            error_code = (ParseErrorCodes.EOF_CODE if right_loc >= self.streamLength
                          else (ParseErrorCodes.LEX_ERROR_CODE
                                if left_loc == right_loc
                                else ParseErrorCodes.INVALID_TOKEN_CODE))

            token_text = ("End-of-file " if error_code == ParseErrorCodes.EOF_CODE
                          else ("\"" + self.inputChars[left_loc:  right_loc + 1] + "\" "
                                if error_code == ParseErrorCodes.INVALID_TOKEN_CODE
                                else "\"" + self.getCharValue(left_loc) + "\" "))

            error_info = [token_text]

        if self.errMsg is None:
            location_info = (self.getFileName() + ':' + str(self.getLineNumberOfCharAt(left_loc)) + ':'
                             + str(self.getColumnOfCharAt(left_loc)) + ':'
                             + str(self.getLineNumberOfCharAt(right_loc)) + ':'
                             + str(self.getColumnOfCharAt(right_loc)) + ':'
                             + str(error_left_loc) + ':'
                             + str(error_right_loc) + ':'
                             + str(error_code) + ": ")
            print "****Error: " + location_info,

            if error_info:
                for i in range(0, error_info.__len__()):
                    print error_info[i] + " ",

            print(ParseErrorCodes.errorMsgText[error_code])
        else:
            '''/**
             * This is the only method in the IMessageHandler interface
             * It is called with the following arguments:
             */'''
            self.errMsg.handleMessage(error_code,
                                      self.getLocation(left_loc, right_loc),
                                      self.getLocation(error_left_loc, error_right_loc),
                                      self.getFileName(),
                                      error_info)

    def reportError(self, errorCode, leftToken, rightToken, errorInfo=None, errorToken=0):

        if isinstance(errorInfo, str):
            temp_info = [errorInfo]

        elif isinstance(errorInfo, list):
            temp_info = errorInfo
        else:
            temp_info = []

        self.reportLexicalError(leftToken, rightToken, errorCode, errorToken, errorToken, temp_info)

    def toString(self, startOffset, endOffset):
        length = endOffset - startOffset + 1
        return ("$EOF" if endOffset >= self.inputChars.__len__() else (
            "" if length <= 0 else self.inputChars[startOffset: startOffset + length]))
