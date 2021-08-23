#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.LexStream import LexStream
from lpg2.Token import Token
from lpg2.ErrorToken import ErrorToken
from lpg2.Adjunct import Adjunct

from lpg2.NullTerminalSymbolsException import NullTerminalSymbolsException
from lpg2.UndefinedEofSymbolException import UndefinedEofSymbolException
from lpg2.UnimplementedTerminalsException import UnimplementedTerminalsException

from lpg2.IPrsStream import IPrsStream
from lpg2.Utils import ArrayList


#
# PrsStream holds an arraylist of tokens "lexed" from the input stream.
#
class PrsStream(IPrsStream):
    __slots__ = ('iLexStream', 'kindMap', 'tokens',
                 'adjuncts', 'index', 'len')

    def __init__(self, lex=None):
        self.iLexStream = None
        self.kindMap = []
        self.tokens = ArrayList()
        self.adjuncts = ArrayList()
        self.index = 0
        self.len = 0
        if lex is not None:
            self.iLexStream = lex
            lex.setPrsStream(self)
            self.resetTokenStream()

    def orderedExportedSymbols(self):
        return []

    def remapTerminalSymbols(self, ordered_parser_symbols, eof_symbol):
        # lexStream might be None, maybe only erroneously, but it has happened
        if self.iLexStream is None:
            raise ReferenceError("PrsStream.remapTerminalSymbols(..):  lexStream is None")

        ordered_lexer_symbols = self.iLexStream.orderedExportedSymbols()
        if ordered_lexer_symbols is None:
            raise NullTerminalSymbolsException()

        if ordered_parser_symbols is None:
            raise NullTerminalSymbolsException()

        unimplemented_symbols = ArrayList()
        if ordered_lexer_symbols != ordered_parser_symbols:
            self.kindMap = [0] * (ordered_lexer_symbols.__len__())
            terminal_map = dict()
            for i in range(0, ordered_lexer_symbols.__len__()):
                terminal_map[ordered_lexer_symbols[i]] = i

            for i in range(0, ordered_parser_symbols.__len__()):
                k = terminal_map.get(ordered_parser_symbols[i], None)
                if k is not None:
                    self.kindMap[k] = i
                else:
                    if i == eof_symbol:
                        raise UndefinedEofSymbolException()

                    unimplemented_symbols.add(i)

        if unimplemented_symbols.size() > 0:
            raise UnimplementedTerminalsException(unimplemented_symbols)

    def mapKind(self, kind):
        return kind if self.kindMap is None or self.kindMap.__len__() == 0 else self.kindMap[kind]

    def resetTokenStream(self):
        self.tokens = ArrayList()
        self.index = 0
        self.adjuncts = ArrayList()

    def setLexStream(self, lexStream):
        self.iLexStream = lexStream
        self.resetTokenStream()

    def resetLexStream(self, lexStream):

        if lexStream is not None:
            lexStream.setPrsStream(self)
            self.iLexStream = lexStream

    def makeToken(self, startLoc, endLoc, kind):
        token = Token(startLoc, endLoc, self.mapKind(kind), self)
        token.setTokenIndex(self.tokens.size())
        self.tokens.add(token)
        token.setAdjunctIndex(self.adjuncts.size())

    def removeLastToken(self):
        last_index = self.tokens.size() - 1
        token = self.tokens.get(last_index)
        adjuncts_size = self.adjuncts.size()
        while adjuncts_size > token.getAdjunctIndex():
            adjuncts_size -= 1
            self.adjuncts.remove(adjuncts_size)

        self.tokens.remove(last_index)

    def makeErrorToken(self, firsttok, lasttok, errortok, kind):
        index = self.tokens.size()  # the next index

        #
        # Note that when creating an error token, we do not remap its kind.
        # Since self is not a lexical operation, it is the responsibility of
        # the calling program (a parser driver): to pass to us the proper kind
        # that it wants for an error token.
        #
        token = ErrorToken(self.getIToken(firsttok),
                           self.getIToken(lasttok),
                           self.getIToken(errortok),
                           self.getStartOffset(firsttok),
                           self.getEndOffset(lasttok),
                           kind)

        token.setTokenIndex(self.tokens.size())
        self.tokens.add(token)
        token.setAdjunctIndex(self.adjuncts.size())

        return index

    def addToken(self, token):
        token.setTokenIndex(self.tokens.size())
        self.tokens.add(token)
        token.setAdjunctIndex(self.adjuncts.size())

    def makeAdjunct(self, startLoc, endLoc, kind):
        token_index = self.tokens.size() - 1  # index of last token processed
        adjunct = Adjunct(startLoc, endLoc, self.mapKind(kind), self)
        adjunct.setAdjunctIndex(self.adjuncts.size())
        adjunct.setTokenIndex(token_index)
        self.adjuncts.add(adjunct)

    def addAdjunct(self, adjunct):
        token_index = self.tokens.size() - 1  # index of last token processed
        adjunct.setTokenIndex(token_index)
        adjunct.setAdjunctIndex(self.adjuncts.size())
        self.adjuncts.add(adjunct)

    def getTokenText(self, i):
        t = self.tokens.get(i)
        return t.toString()

    def getStartOffset(self, i):
        t = self.tokens.get(i)
        return t.getStartOffset()

    def getEndOffset(self, i):
        t = self.tokens.get(i)
        return t.getEndOffset()

    def getTokenLength(self, i):
        t = self.tokens.get(i)
        return t.getEndOffset() - t.getStartOffset() + 1

    def getLineNumberOfTokenAt(self, i):
        if not self.iLexStream:
            return 0
        t = self.tokens.get(i)
        return self.iLexStream.getLineNumberOfCharAt(t.getStartOffset())

    def getEndLineNumberOfTokenAt(self, i):
        if not self.iLexStream: return 0
        t = self.tokens.get(i)
        return self.iLexStream.getLineNumberOfCharAt(t.getEndOffset())

    def getColumnOfTokenAt(self, i):
        if not self.iLexStream: return 0
        t = self.tokens.get(i)
        return self.iLexStream.getColumnOfCharAt(t.getStartOffset())

    def getEndColumnOfTokenAt(self, i):
        if not self.iLexStream: return 0
        t = self.tokens.get(i)
        return self.iLexStream.getColumnOfCharAt(t.getEndOffset())

    def orderedTerminalSymbols(self):
        return []

    def getLineOffset(self, i):
        if not self.iLexStream: return 0
        return self.iLexStream.getLineOffset(i)

    def getLineCount(self):
        if not self.iLexStream: return 0
        return self.iLexStream.getLineCount()

    def getLineNumberOfCharAt(self, i):
        if not self.iLexStream: return 0
        return self.iLexStream.getLineNumberOfCharAt(i)

    def getColumnOfCharAt(self, i):
        return self.getColumnOfCharAt(i)

    def getFirstErrorToken(self, i):
        return self.getFirstRealToken(i)

    def getFirstRealToken(self, i):
        while i >= self.len:
            i = (self.tokens.get(i)).getFirstRealToken().getTokenIndex()

        return i

    def getLastErrorToken(self, i):
        return self.getLastRealToken(i)

    def getLastRealToken(self, i):
        while i >= self.len:
            i = (self.tokens.get(i)).getLastRealToken().getTokenIndex()

        return i

    def getInputChars(self):
        return self.iLexStream.getInputChars() if isinstance(self.iLexStream, LexStream) else ""

    def getInputBytes(self):
        #  return (self.iLexStream instanceof Utf8LexStream ? (<Utf8LexStream>self.iLexStream).getInputBytes(): : None):
        return ""

    def toStringFromIndex(self, first_token, last_token):
        return self.toString(self.tokens.get(first_token), self.tokens.get(last_token))

    def toString(self, t1, t2):
        if not self.iLexStream: return ""
        return self.iLexStream.toString(t1.getStartOffset(), t2.getEndOffset())

    def getSize(self):
        return self.tokens.size()

    def setSize(self):
        self.len = self.tokens.size()

    def getTokenIndexAtCharacter(self, offset):
        low = 0
        high = self.tokens.size()
        while high > low:
            mid = (high + low) // 2
            mid_element = self.tokens.get(mid)
            if offset >= mid_element.getStartOffset() and offset <= mid_element.getEndOffset():
                return mid
            else:
                if offset < mid_element.getStartOffset():
                    high = mid
                else:
                    low = mid + 1

        return -(low - 1)

    def getTokenAtCharacter(self, offset):
        token_index = self.getTokenIndexAtCharacter(offset)
        return None if (token_index < 0) else self.getTokenAt(token_index)

    def getTokenAt(self, i):
        return self.tokens.get(i)

    def getIToken(self, i):
        return self.tokens.get(i)

    def getTokens(self):
        return self.tokens

    def getStreamIndex(self):
        return self.index

    def getStreamLength(self):
        return self.len

    def setStreamIndex(self, index):
        self.index = index

    def setStreamLength2(self):
        self.len = self.tokens.size()

    def setStreamLength(self, length=None):
        if length is None:
            self.setStreamLength2()
            return

        self.len = length

    def getILexStream(self):
        return self.iLexStream

    def getLexStream(self):
        return self.iLexStream

    def dumpTokens(self):
        if self.getSize() <= 2:
            return

        print " Kind \tOffset \tLen \tLine \tCol \tText\n"
        for i in range(1, self.getSize() - 1):
            self.dumpToken(i)

    def dumpToken(self, i):

        print " (" + str(self.getKind(i)) + "):",
        print " \t" + str(self.getStartOffset(i)),
        print " \t" + str(self.getTokenLength(i)),
        print " \t" + str(self.getLineNumberOfTokenAt(i)),
        print " \t" + str(self.getColumnOfTokenAt(i)),
        print " \t" + str(self.getTokenText(i))

    def getAdjunctsFromIndex(self, i):
        start_index = (self.tokens.get(i)).getAdjunctIndex()
        end_index = (self.adjuncts.size()
                     if (i + 1 == self.tokens.size())
                     else (self.tokens.get(self.getNext(i))).getAdjunctIndex())
        size = end_index - start_index
        token_slice = [None] * size
        j = start_index
        k = 0
        while j < end_index:
            token_slice[k] = self.adjuncts.get(j)
            k += 1
            j += 1

        return token_slice

    #
    # Return an iterator for the adjuncts that follow token i.
    #
    def getFollowingAdjuncts(self, i):
        return self.getAdjunctsFromIndex(i)

    def getPrecedingAdjuncts(self, i):
        return self.getAdjunctsFromIndex(self.getPrevious(i))

    def getAdjuncts(self):
        return self.adjuncts

    def getToken2(self):
        self.index = self.getNext(self.index)
        return self.index

    def getToken(self, end_token=None):
        if end_token is None:
            return self.getToken2()
        self.index = (self.getNext(self.index) if self.index < end_token else self.len - 1)
        return self.index

    def getKind(self, i):
        t = self.tokens.get(i)
        return t.getKind()

    def getNext(self, i):
        i += 1
        return i if i < self.len else self.len - 1

    def getPrevious(self, i):
        return 0 if i <= 0 else i - 1

    def getName(self, i):
        return self.getTokenText(i)

    def peek(self):
        return self.getNext(self.index)

    def reset1(self):
        self.index = 0

    def reset2(self, i):
        self.index = self.getPrevious(i)

    def reset(self, i=None):
        if i is None:
            self.reset1()
        else:
            self.reset2(i)

    def badToken(self):
        return 0

    def getLine(self, i):
        return self.getLineNumberOfTokenAt(i)

    def getColumn(self, i):
        return self.getColumnOfTokenAt(i)

    def getEndLine(self, i):
        return self.getEndLineNumberOfTokenAt(i)

    def getEndColumn(self, i):
        return self.getEndColumnOfTokenAt(i)

    def afterEol(self, i):
        return True if i < 1 else self.getEndLineNumberOfTokenAt(i - 1) < self.getLineNumberOfTokenAt(i)

    def getFileName(self):
        if not self.iLexStream:
            return ""
        return self.iLexStream.getFileName()

    #
    # Here is where we report errors.  The default method is simply to print the error message to the console.
    # However, the user may supply an error message handler to process error messages.  To support that
    # a message handler class is provided that has a single method handleMessage().  The user has his
    # error message handler class implement the IMessageHandler class and provides an object of self type
    # to the runtime using the setMessageHandler(errorMsg): method. If the message handler object is set,
    # the reportError methods will invoke its handleMessage(): method.
    #
    # IMessageHandler errMsg = None # the error message handler object is declared in LexStream
    #
    def setMessageHandler(self, handler=None):
        self.iLexStream.setMessageHandler(handler)

    def getMessageHandler(self):
        return self.iLexStream.getMessageHandler()

    def reportError(self, errorCode, leftToken, rightToken, errorInfo=None, errorToken=0):
        temp_info = None
        if isinstance(errorInfo, str):
            temp_info = [errorInfo]
        elif isinstance(errorInfo, list):
            temp_info = errorInfo
        else:
            temp_info = []

        self.iLexStream.reportLexicalError(self.getStartOffset(leftToken), self.getEndOffset(rightToken),
                                           errorCode, self.getStartOffset(errorToken), self.getEndOffset(errorToken),
                                           temp_info)
