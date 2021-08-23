#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.ConfigurationStack import ConfigurationStack
from lpg2.IntTuple import IntTuple

from lpg2.Stacks import Stacks

from lpg2.ParseErrorCodes import ParseErrorCodes
from lpg2.Utils import arraycopy
import time


class RepairCandidate(object):
    __slots__ = ('symbol', 'location')

    def __init__(self):
        self.symbol = 0
        self.location = 0


class PrimaryRepairInfo(object):
    __slots__ = ('distance', 'misspellIndex', 'code', 'bufferPosition', 'symbol')

    def __init__(self, clone=None):
        self.distance = 0
        self.misspellIndex = 0
        self.code = 0
        self.bufferPosition = 0
        self.symbol = 0

        if clone:
            self.copy(clone)

    def copy(self, clone):
        self.distance = clone.distance
        self.misspellIndex = clone.misspellIndex
        self.code = clone.code
        self.bufferPosition = clone.bufferPosition
        self.symbol = clone.symbol
        return


class SecondaryRepairInfo(object):
    __slots__ = ('code', 'distance', 'bufferPosition', 'stackPosition', 'numDeletions',
                 'symbol', 'recoveryOnNextStack')

    def __init__(self):
        self.code = 0
        self.distance = 0
        self.bufferPosition = 0
        self.stackPosition = 0
        self.numDeletions = 0
        self.symbol = 0
        self.recoveryOnNextStack = False


class StateInfo(object):
    __slots__ = ('state', 'next')

    def __init__(self, state, next_state):
        self.state = state
        self.next = next_state


class DiagnoseParser(Stacks):
    STACK_INCREMENT = 256
    BUFF_UBOUND = 31
    BUFF_SIZE = 32
    MAX_DISTANCE = 30
    MIN_DISTANCE = 3
    NIL = -1

    def setMonitor(self, monitor):
        self.monitor = monitor

    __slots__ = ('monitor', 'tokStream',
                 'prs', 'ERROR_SYMBOL', 'SCOPE_SIZE', 'MAX_NAME_LENGTH', 'NT_OFFSET',
                 'LA_STATE_OFFSET', 'NUM_RULES', 'NUM_SYMBOLS',
                 'START_STATE', 'EOFT_SYMBOL', 'EOLT_SYMBOL', 'ACCEPT_ACTION', 'ERROR_ACTION',
                 'sym_list', 'maxErrors', 'maxTime',
                 'tempStackTop', 'tempStack', 'prevStackTop', 'prevStack', 'nextStackTop', 'nextStack',
                 'scopeStackTop', 'scopeIndex', 'scopePosition', 'buffer', 'stateSeen', 'statePoolTop',
                 'statePool', 'main_configuration_stack')

    def __init__(self, tokStream, prs, maxErrors=0, maxTime=0, monitor=None):

        super(DiagnoseParser, self).__init__()
        self.monitor = monitor
        self.tokStream = tokStream
        self.prs = prs

        self.ERROR_SYMBOL = 0
        self.SCOPE_SIZE = 0
        self.MAX_NAME_LENGTH = 0
        self.NT_OFFSET = 0
        self.LA_STATE_OFFSET = 0
        self.NUM_RULES = 0
        self.NUM_SYMBOLS = 0
        self.START_STATE = 0
        self.EOFT_SYMBOL = 0
        self.EOLT_SYMBOL = 0
        self.ACCEPT_ACTION = 0
        self.ERROR_ACTION = 0

        self.sym_list = []

        self.maxErrors = 0

        self.maxTime = 0

        self.stateStackTop = 0
        self.stateStack = []

        self.locationStack = []

        self.tempStackTop = 0
        self.tempStack = []

        self.prevStackTop = 0
        self.prevStack = []

        self.nextStackTop = 0
        self.nextStack = []

        self.scopeStackTop = 0
        self.scopeIndex = []
        self.scopePosition = []

        self.buffer = [0] * self.BUFF_SIZE

        self.stateSeen = []

        self.statePoolTop = 0
        self.statePool = []

        self.monitor = monitor
        self.maxErrors = maxErrors
        self.maxTime = maxTime
        self.tokStream = tokStream
        self.prs = prs
        self.main_configuration_stack = ConfigurationStack(prs)
        self.ERROR_SYMBOL = prs.getErrorSymbol()
        self.SCOPE_SIZE = prs.getScopeSize()
        self.MAX_NAME_LENGTH = prs.getMaxNameLength()
        self.NT_OFFSET = prs.getNtOffset()
        self.LA_STATE_OFFSET = prs.getLaStateOffset()
        self.NUM_RULES = prs.getNumRules()
        self.NUM_SYMBOLS = prs.getNumSymbols()
        self.START_STATE = prs.getStartState()
        self.EOFT_SYMBOL = prs.getEoftSymbol()
        self.EOLT_SYMBOL = prs.getEoltSymbol()
        self.ACCEPT_ACTION = prs.getAcceptAction()
        self.ERROR_ACTION = prs.getErrorAction()
        self.sym_list = [0] * (self.NUM_SYMBOLS + 1)

    def rhs(self, index):
        return self.prs.rhs(index)

    def baseAction(self, index):
        return self.prs.baseAction(index)

    def baseCheck(self, index):
        return self.prs.baseCheck(index)

    def lhs(self, index):
        return self.prs.lhs(index)

    def termCheck(self, index):
        return self.prs.termCheck(index)

    def termAction(self, index):
        return self.prs.termAction(index)

    def asb(self, index):
        return self.prs.asb(index)

    def asr(self, index):
        return self.prs.asr(index)

    def nasb(self, index):
        return self.prs.nasb(index)

    def nasr(self, index):
        return self.prs.nasr(index)

    def terminalIndex(self, index):
        return self.prs.terminalIndex(index)

    def nonterminalIndex(self, index):
        return self.prs.nonterminalIndex(index)

    def symbolIndex(self, index):
        return self.nonterminalIndex(index - self.NT_OFFSET) if index > self.NT_OFFSET else self.terminalIndex(index)

    def scopePrefix(self, index):
        return self.prs.scopePrefix(index)

    def scopeSuffix(self, index):
        return self.prs.scopeSuffix(index)

    def scopeLhs(self, index):
        return self.prs.scopeLhs(index)

    def scopeLa(self, index):
        return self.prs.scopeLa(index)

    def scopeStateSet(self, index):
        return self.prs.scopeStateSet(index)

    def scopeRhs(self, index):
        return self.prs.scopeRhs(index)

    def scopeState(self, index):
        return self.prs.scopeState(index)

    def inSymb(self, index):
        return self.prs.inSymb(index)

    def name(self, index):
        return self.prs.name(index)

    def originalState(self, state):
        return self.prs.originalState(state)

    def asi(self, state):
        return self.prs.asi(state)

    def nasi(self, state):
        return self.prs.nasi(state)

    def inSymbol(self, state):
        return self.prs.inSymbol(state)

    def ntAction(self, state, sym):
        return self.prs.ntAction(state, sym)

    def isNullable(self, symbol):
        return self.prs.isNullable(symbol)

    def reallocateStacks(self):
        old_stack_length = 0 if self.stateStack is None else len(self.stateStack)
        stack_length = old_stack_length + self.STACK_INCREMENT

        if self.stateStack is None or len(self.stateStack) == 0:
            self.stateStack = [0] * stack_length
            self.locationStack = [0] * stack_length
            self.tempStack = [0] * stack_length
            self.prevStack = [0] * stack_length
            self.nextStack = [0] * stack_length
            self.scopeIndex = [0] * stack_length
            self.scopePosition = [0] * stack_length
        else:
            self.stateStack = arraycopy(self.stateStack, 0, [0] * stack_length, 0, old_stack_length)
            self.locationStack = arraycopy(self.locationStack, 0, [0] * stack_length, 0, old_stack_length)
            self.tempStack = arraycopy(self.tempStack, 0, [0] * stack_length, 0, old_stack_length)
            self.prevStack = arraycopy(self.prevStack, 0, [0] * stack_length, 0, old_stack_length)
            self.nextStack = arraycopy(self.nextStack, 0, [0] * stack_length, 0, old_stack_length)
            self.scopeIndex = arraycopy(self.scopeIndex, 0, [0] * stack_length, 0, old_stack_length)
            self.scopePosition = arraycopy(self.scopePosition, 0, [0] * stack_length, 0, old_stack_length)

        return

    def diagnose(self, error_token=0):
        self.diagnoseEntry(0, error_token)

    def diagnoseEntry(self, marker_kind, error_token=None):
        if error_token is not None:
            self.diagnoseEntry2(marker_kind, error_token)
        else:
            self.diagnoseEntry1(marker_kind)

    def diagnoseEntry1(self, marker_kind):
        self.reallocateStacks()
        self.tempStackTop = 0
        self.tempStack[self.tempStackTop] = self.START_STATE
        self.tokStream.reset()
        current_token = 0
        current_kind = 0
        if marker_kind == 0:
            current_token = self.tokStream.getToken()
            current_kind = self.tokStream.getKind(current_token)
        else:
            current_token = self.tokStream.peek()
            current_kind = marker_kind

        error_token = self.parseForError(current_kind)
        #
        # If an error was found, start the diagnosis and recovery.
        #
        if error_token != 0:
            self.diagnoseEntry(marker_kind, error_token)

        return

    def diagnoseEntry2(self, marker_kind, error_token):
        action = IntTuple(1 << 18)
        startTime = time.time()
        errorCount = 0

        #
        # Compute sequence of actions that leads us to the
        # error_token.
        #
        if self.stateStack is None or len(self.stateStack) == 0:
            self.reallocateStacks()

        self.tempStackTop = 0
        self.tempStack[self.tempStackTop] = self.START_STATE
        self.tokStream.reset()
        current_token = 0
        current_kind = 0
        if marker_kind == 0:
            current_token = self.tokStream.getToken()
            current_kind = self.tokStream.getKind(current_token)
        else:
            current_token = self.tokStream.peek()
            current_kind = marker_kind

        self.parseUpToError(action, current_kind, error_token)

        #
        # Start parsing
        #
        self.stateStackTop = 0
        self.stateStack[self.stateStackTop] = self.START_STATE

        self.tempStackTop = self.stateStackTop
        arraycopy(self.tempStack, 0, self.stateStack, 0, self.tempStackTop + 1)

        self.tokStream.reset()
        if marker_kind == 0:
            current_token = self.tokStream.getToken()
            current_kind = self.tokStream.getKind(current_token)
        else:
            current_token = self.tokStream.peek()
            current_kind = marker_kind

        self.locationStack[self.stateStackTop] = current_token

        #
        # Process a terminal
        #
        act = 0
        while True:
            #
            # Synchronize state stacks and update the location stack
            #
            prev_pos = -1
            self.prevStackTop = -1

            next_pos = -1
            self.nextStackTop = -1

            pos = self.stateStackTop
            self.tempStackTop = self.stateStackTop - 1
            arraycopy(self.stateStack, 0, self.tempStack, 0, self.stateStackTop + 1)

            action_index = 0
            act = action.get(action_index)  # tAction(act, current_kind):
            action_index += 1

            #
            # When a reduce action is encountered, we compute all REDUCE
            # and associated goto actions induced by the current token.
            # Eventually, a SHIFT, SHIFT-REDUCE, ACCEPT or ERROR action is
            # computed...
            #
            while act <= self.NUM_RULES:

                while True:
                    self.tempStackTop -= (self.rhs(act) - 1)
                    act = self.ntAction(self.tempStack[self.tempStackTop], self.lhs(act))
                    if not (act <= self.NUM_RULES):
                        break

                #
                # ... Update the maximum useful position of the
                # (STATE_):STACK, push goto state into stack, and
                # compute next action on current symbol ...
                #
                if self.tempStackTop + 1 >= len(self.stateStack):
                    self.reallocateStacks()

                pos = pos if pos < self.tempStackTop else self.tempStackTop
                self.tempStack[self.tempStackTop + 1] = act

                act = action.get(action_index)  # tAction(act, current_kind):
                action_index += 1

            #
            # At self point, we have a shift, shift-reduce, accept or error
            # action.  STACK contains the configuration of the state stack
            # prior to executing any action on current_token. next_stack contains
            # the configuration of the state stack after executing all
            # reduce actions induced by current_token.  The variable pos indicates
            # the highest position in STACK that is still useful after the
            # reductions are executed.
            #
            while act > self.ERROR_ACTION or act < self.ACCEPT_ACTION:

                #
                # if the parser needs to stop processing,
                # it may do so here.
                #
                if self.monitor and self.monitor.isCancelled():
                    return

                self.nextStackTop = self.tempStackTop + 1

                for i in range(next_pos + 1, self.nextStackTop + 1):
                    self.nextStack[i] = self.tempStack[i]

                for k in range(pos + 1, self.nextStackTop + 1):
                    self.locationStack[k] = self.locationStack[self.stateStackTop]

                #
                # If we have a shift-reduce, process it as well as
                # the goto-reduce actions that follow it.
                #
                if act > self.ERROR_ACTION:

                    act -= self.ERROR_ACTION
                    while True:
                        self.nextStackTop -= (self.rhs(act) - 1)
                        act = self.ntAction(self.nextStack[self.nextStackTop], self.lhs(act))
                        if not act <= self.NUM_RULES:
                            break

                    pos = pos if pos < self.nextStackTop else self.nextStackTop

                if self.nextStackTop + 1 >= len(self.stateStack):
                    self.reallocateStacks()

                self.tempStackTop = self.nextStackTop

                self.nextStackTop += 1
                self.nextStack[self.nextStackTop] = act

                next_pos = self.nextStackTop
                #
                # Simulate the parser through the next token without
                # destroying STACK or next_stack.
                #
                current_token = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(current_token)

                act = action.get(action_index)  # tAction(act, current_kind)
                action_index += 1

                while act <= self.NUM_RULES:
                    #
                    # ... Process all goto-reduce actions following
                    # reduction, until a goto action is computed ...
                    #

                    while True:
                        lhs_symbol = self.lhs(act)
                        self.tempStackTop -= (self.rhs(act) - 1)
                        act = (self.tempStack[self.tempStackTop] if self.tempStackTop > next_pos
                               else self.nextStack[self.tempStackTop])

                        act = self.ntAction(act, lhs_symbol)
                        if not act <= self.NUM_RULES:
                            break
                    #
                    # ... Update the maximum useful position of the
                    # (STATE_):STACK, push GOTO state into stack, and
                    # compute next action on current symbol ...
                    #
                    if self.tempStackTop + 1 >= len(self.stateStack):
                        self.reallocateStacks()

                    next_pos = next_pos if next_pos < self.tempStackTop else self.tempStackTop
                    self.tempStack[self.tempStackTop + 1] = act

                    act = action.get(action_index)  # tAction(act, current_kind)
                    action_index += 1

                #
                # No error was detected, Read next token into
                # PREVTOK element, advance CURRENT_TOKEN pointer and
                # update stacks.
                #
                if act != self.ERROR_ACTION:
                    self.prevStackTop = self.stateStackTop
                    for i in range(prev_pos + 1, self.prevStackTop + 1):
                        self.prevStack[i] = self.stateStack[i]

                    prev_pos = pos

                    self.stateStackTop = self.nextStackTop
                    for k in range(pos + 1, self.stateStackTop + 1):
                        self.stateStack[k] = self.nextStack[k]

                    self.locationStack[self.stateStackTop] = current_token
                    pos = next_pos

            #
            # At self stage, either we have an ACCEPT or an ERROR
            # action.
            #
            if act == self.ERROR_ACTION:
                #
                # An error was detected.
                #
                errorCount += 1
                #
                # Check time and error limits after the first error encountered
                # Exit if int of errors exceeds maxError or if maxTime reached
                #
                if errorCount > 1:
                    if self.maxErrors > 0 and errorCount > self.maxErrors:
                        break

                    if self.maxTime > 0 and time.time() - startTime > self.maxTime:
                        break

                candidate = self.errorRecovery(current_token)
                #
                # if the parser needs to stop processing,
                # it may do so here.
                #
                if self.monitor and self.monitor.isCancelled():
                    return

                act = self.stateStack[self.stateStackTop]

                #
                # If the recovery was successful on a nonterminal candidate,
                # parse through that candidate and "read" the next token.
                #
                if candidate.symbol == 0:
                    break
                elif candidate.symbol > self.NT_OFFSET:
                    lhs_symbol = candidate.symbol - self.NT_OFFSET
                    act = self.ntAction(act, lhs_symbol)
                    while act <= self.NUM_RULES:
                        self.stateStackTop -= (self.rhs(act) - 1)
                        act = self.ntAction(self.stateStack[self.stateStackTop], self.lhs(act))

                    self.stateStackTop += 1
                    self.stateStack[self.stateStackTop] = act

                    current_token = self.tokStream.getToken()
                    current_kind = self.tokStream.getKind(current_token)
                    self.locationStack[self.stateStackTop] = current_token
                else:
                    current_kind = candidate.symbol
                    self.locationStack[self.stateStackTop] = candidate.location

                #
                # At self stage, we have a recovery configuration. See how
                # far we can go with it.
                #
                next_token = self.tokStream.peek()
                self.tempStackTop = self.stateStackTop
                arraycopy(self.stateStack, 0, self.tempStack, 0, self.stateStackTop + 1)
                error_token = self.parseForError(current_kind)

                if error_token != 0:
                    self.tokStream.reset(next_token)
                    self.tempStackTop = self.stateStackTop
                    arraycopy(self.stateStack, 0, self.tempStack, 0, self.stateStackTop + 1)
                    self.parseUpToError(action, current_kind, error_token)
                    self.tokStream.reset(next_token)
                else:
                    act = self.ACCEPT_ACTION

            if not act != self.ACCEPT_ACTION:  # for while loop
                break
        return

    #
    # Given the configuration consisting of the states in tempStack
    # and the sequence of tokens (current_kind, followed by the tokens
    # in tokStream):, keep parsing until either the parse completes
    # successfully or it encounters an error. If the parse is not
    # succesful, we return the farthest token on which an error was
    # encountered. Otherwise, we return 0.
    #
    def parseForError(self, current_kind):
        error_token = 0
        #
        # Get next token in stream and compute initial action
        #
        curtok = self.tokStream.getPrevious(self.tokStream.peek())
        act = self.tAction(self.tempStack[self.tempStackTop], current_kind)
        #
        # Allocate configuration stack.
        #
        configuration_stack = ConfigurationStack(self.prs)

        #
        # Keep parsing until we reach the end of file and succeed or
        # an error is encountered. The sym_list of actions executed will
        # be store in the "action" tuple.
        #
        while True:
            if act <= self.NUM_RULES:

                self.tempStackTop -= 1

                while True:
                    self.tempStackTop -= (self.rhs(act) - 1)
                    act = self.ntAction(self.tempStack[self.tempStackTop], self.lhs(act))
                    if not act <= self.NUM_RULES:
                        break
            elif act > self.ERROR_ACTION:

                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
                act -= self.ERROR_ACTION

                while True:
                    self.tempStackTop -= (self.rhs(act) - 1)
                    act = self.ntAction(self.tempStack[self.tempStackTop], self.lhs(act))
                    if not act <= self.NUM_RULES:
                        break

            elif act < self.ACCEPT_ACTION:
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)

            elif act == self.ERROR_ACTION:

                error_token = (error_token if error_token > curtok else curtok)

                configuration = configuration_stack.pop()
                if configuration is None:
                    act = self.ERROR_ACTION
                else:
                    self.tempStackTop = configuration.stack_top
                    configuration.retrieveStack(self.tempStack)
                    act = configuration.act
                    curtok = configuration.curtok
                    # no need to execute: action.reset(configuration.action_length):
                    current_kind = self.tokStream.getKind(curtok)
                    self.tokStream.reset(self.tokStream.getNext(curtok))
                    continue

                break

            elif act > self.ACCEPT_ACTION:

                if configuration_stack.findConfiguration(self.tempStack, self.tempStackTop, curtok):
                    act = self.ERROR_ACTION
                else:
                    configuration_stack.push(self.tempStack, self.tempStackTop, act + 1, curtok, 0)
                    act = self.baseAction(act)

                continue

            else:
                break  # assert(act == ACCEPT_ACTION):

            self.tempStackTop += 1
            if self.tempStackTop >= len(self.tempStack):
                self.reallocateStacks()
            self.tempStack[self.tempStackTop] = act

            act = self.tAction(act, current_kind)

        return error_token if act == self.ERROR_ACTION else 0

    #
    # Given the configuration consisting of the states in tempStack
    # and the sequence of tokens (current_kind, followed by the tokens
    # in tokStream):, parse up to error_token in the tokStream and store
    # all the parsing actions executed in the "action" tuple.
    #
    def parseUpToError(self, action, current_kind, error_token):
        #
        # Assume predecessor of next token and compute initial action
        #
        curtok = self.tokStream.getPrevious(self.tokStream.peek())
        act = self.tAction(self.tempStack[self.tempStackTop], current_kind)
        #
        # Allocate configuration stack.
        #
        configuration_stack = ConfigurationStack(self.prs)
        #
        # Keep parsing until we reach the end of file and succeed or
        # an error is encountered. The sym_list of actions executed will
        # be store in the "action" tuple.
        #
        action.reset()
        while True:
            if act <= self.NUM_RULES:
                action.add(act)  # save this reduce action
                self.tempStackTop -= 1

                while True:
                    self.tempStackTop -= (self.rhs(act) - 1)
                    act = self.ntAction(self.tempStack[self.tempStackTop], self.lhs(act))
                    if not act <= self.NUM_RULES:
                        break
            elif act > self.ERROR_ACTION:

                action.add(act)  # save self shift-reduce action
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
                act -= self.ERROR_ACTION

                while True:
                    self.tempStackTop -= (self.rhs(act) - 1)
                    act = self.ntAction(self.tempStack[self.tempStackTop], self.lhs(act))
                    if not act <= self.NUM_RULES:
                        break

            elif act < self.ACCEPT_ACTION:

                action.add(act)  # save self shift action
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)

            elif act == self.ERROR_ACTION:

                if curtok != error_token:
                    configuration = configuration_stack.pop()
                    if configuration is None:
                        act = self.ERROR_ACTION
                    else:
                        self.tempStackTop = configuration.stack_top
                        configuration.retrieveStack(self.tempStack)
                        act = configuration.act
                        curtok = configuration.curtok
                        action.reset(configuration.action_length)
                        current_kind = self.tokStream.getKind(curtok)
                        self.tokStream.reset(self.tokStream.getNext(curtok))
                        continue

                break

            elif act > self.ACCEPT_ACTION:
                if configuration_stack.findConfiguration(self.tempStack, self.tempStackTop, curtok):
                    act = self.ERROR_ACTION
                else:
                    configuration_stack.push(self.tempStack, self.tempStackTop, act + 1, curtok, action.size())
                    act = self.baseAction(act)

                continue
            else:
                break  # assert(act == ACCEPT_ACTION):

            self.tempStackTop += 1
            if self.tempStackTop >= len(self.tempStack):
                self.reallocateStacks()
            self.tempStack[self.tempStackTop] = act

            act = self.tAction(act, current_kind)

        action.add(self.ERROR_ACTION)
        return

    #
    # Try to parse until first_symbol and all tokens in BUFFER have
    # been consumed, or an error is encountered. Return the int
    # of tokens that were expended before the parse blocked.
    #
    def parseCheck(self, stack, stack_top, first_symbol, buffer_position):
        buffer_index = 0
        current_kind = 0

        local_stack = [0] * (stack.__len__())
        local_stack_top = stack_top

        for i in range(0, stack_top + 1):
            local_stack[i] = stack[i]

        configuration_stack = ConfigurationStack(self.prs)

        #
        # If the first symbol is a nonterminal, process it here.
        #
        act = local_stack[local_stack_top]
        if first_symbol > self.NT_OFFSET:
            lhs_symbol = first_symbol - self.NT_OFFSET
            buffer_index = buffer_position
            current_kind = self.tokStream.getKind(self.buffer[buffer_index])
            self.tokStream.reset(self.tokStream.getNext(self.buffer[buffer_index]))
            act = self.ntAction(act, lhs_symbol)
            while act <= self.NUM_RULES:
                local_stack_top -= (self.rhs(act) - 1)
                act = self.ntAction(local_stack[local_stack_top], self.lhs(act))

        else:
            local_stack_top -= 1
            buffer_index = buffer_position - 1
            current_kind = first_symbol
            self.tokStream.reset(self.buffer[buffer_position])

        #
        # Start parsing the remaining symbols in the buffer
        #
        local_stack_top += 1
        if local_stack_top >= len(local_stack):  # Stack overflow!!!
            return buffer_index

        local_stack[local_stack_top] = act

        act = self.tAction(act, current_kind)

        while True:

            if act <= self.NUM_RULES:  # reduce action

                local_stack_top -= self.rhs(act)
                act = self.ntAction(local_stack[local_stack_top], self.lhs(act))
                while act <= self.NUM_RULES:
                    local_stack_top -= (self.rhs(act) - 1)
                    act = self.ntAction(local_stack[local_stack_top], self.lhs(act))
            elif act > self.ERROR_ACTION:  # shift-reduce action

                if buffer_index == self.MAX_DISTANCE:
                    buffer_index += 1
                    break
                else:
                    buffer_index += 1

                current_kind = self.tokStream.getKind(self.buffer[buffer_index])
                self.tokStream.reset(self.tokStream.getNext(self.buffer[buffer_index]))
                act -= self.ERROR_ACTION

                while True:
                    local_stack_top -= (self.rhs(act) - 1)
                    act = self.ntAction(local_stack[local_stack_top], self.lhs(act))
                    if not act <= self.NUM_RULES:
                        break

            elif act < self.ACCEPT_ACTION:  # shift action

                if buffer_index == self.MAX_DISTANCE:
                    buffer_index += 1
                    break
                else:
                    buffer_index += 1

                current_kind = self.tokStream.getKind(self.buffer[buffer_index])
                self.tokStream.reset(self.tokStream.getNext(self.buffer[buffer_index]))

            elif act == self.ERROR_ACTION:

                configuration = configuration_stack.pop()
                if configuration is None:
                    act = self.ERROR_ACTION
                else:
                    local_stack_top = configuration.stack_top
                    configuration.retrieveStack(local_stack)
                    act = configuration.act
                    buffer_index = configuration.curtok
                    # no need to execute: action.reset(configuration.action_length):
                    current_kind = self.tokStream.getKind(self.buffer[buffer_index])
                    self.tokStream.reset(self.tokStream.getNext(self.buffer[buffer_index]))
                    continue

                break

            elif act > self.ACCEPT_ACTION:

                if configuration_stack.findConfiguration(local_stack, local_stack_top, buffer_index):
                    act = self.ERROR_ACTION
                else:
                    configuration_stack.push(local_stack, local_stack_top, act + 1, buffer_index, 0)
                    act = self.baseAction(act)

                continue

            else:
                break

            local_stack_top += 1
            if local_stack_top >= len(local_stack):  # Stack overflow!!!
                break

            local_stack[local_stack_top] = act
            act = self.tAction(act, current_kind)

        return self.MAX_DISTANCE if act == self.ACCEPT_ACTION else buffer_index

    #
    #  This routine is invoked when an error is encountered.  It
    # tries to diagnose the error and recover from it.  If it is
    # successful, the state stack, the current token and the buffer
    # are readjusted i.e., after a successful recovery,
    # state_stack_top points to the location in the state stack
    # that contains the state on which to recover current_token
    # identifies the symbol on which to recover.
    #
    # Up to three configurations may be available when self routine
    # is invoked. PREV_STACK may contain the sequence of states
    # preceding any action on prevtok, STACK always contains the
    # sequence of states preceding any action on current_token, and
    # NEXT_STACK may contain the sequence of states preceding any
    # action on the successor of current_token.
    #
    def errorRecovery(self, error_token):
        prevtok = self.tokStream.getPrevious(error_token)

        #
        # Try primary phase recoveries. If not successful, try secondary
        # phase recoveries.  If not successful and we are at end of the
        # file, we issue the end-of-file error and quit. Otherwise, ...
        #
        candidate = self.primaryPhase(error_token)
        if candidate.symbol != 0:
            return candidate

        candidate = self.secondaryPhase(error_token)
        if candidate.symbol != 0:
            return candidate

        #
        # At self point, primary and (initial attempt at): secondary
        # recovery did not work.  We will now get into "panic mode" and
        # keep trying secondary phase recoveries until we either find
        # a successful recovery or have consumed the remaining input
        # tokens.
        #
        if self.tokStream.getKind(error_token) != self.EOFT_SYMBOL:
            while self.tokStream.getKind(self.buffer[self.BUFF_UBOUND]) != self.EOFT_SYMBOL:
                candidate = self.secondaryPhase(self.buffer[self.MAX_DISTANCE - self.MIN_DISTANCE + 2])
                if candidate.symbol != 0:
                    return candidate

        #
        # If no successful recovery is found and we have reached the
        # end of the file, check whether or not any scope recovery is
        # applicable at the end of the file after discarding some
        # states.
        #
        scope_repair = PrimaryRepairInfo()
        scope_repair.bufferPosition = self.BUFF_UBOUND
        top = self.stateStackTop
        while top >= 0:
            self.scopeTrial(scope_repair, self.stateStack, top)
            if scope_repair.distance > 0:
                break
            top -= 1

        #
        # If any scope repair was successful, emit the message now
        #
        for i in range(0, self.scopeStackTop):
            self.emitError(ParseErrorCodes.SCOPE_CODE,
                           -self.scopeIndex[i],
                           self.locationStack[self.scopePosition[i]],
                           self.buffer[1],
                           self.nonterminalIndex(self.scopeLhs(self.scopeIndex[i])))

        #
        # If the original error_token was already pointing to the EOF, issue the EOF-reached message.
        #
        if self.tokStream.getKind(error_token) == self.EOFT_SYMBOL:
            self.emitError(ParseErrorCodes.EOF_CODE,
                           self.terminalIndex(self.EOFT_SYMBOL),
                           prevtok,
                           prevtok)
        else:
            #
            # We reached the end of the file while panicking. Delete all
            # remaining tokens in the input.
            #
            i = self.BUFF_UBOUND
            while self.tokStream.getKind(self.buffer[i]) == self.EOFT_SYMBOL:
                i -= 1

            self.emitError(ParseErrorCodes.DELETION_CODE,
                           self.terminalIndex(self.tokStream.getKind(error_token)),
                           error_token,
                           self.buffer[i])

        #
        # Create the "failed" candidate and return it.
        #
        candidate.symbol = 0
        candidate.location = self.buffer[self.BUFF_UBOUND]  # point to EOF
        return candidate

    #
    # This function tries primary and scope recovery on each
    # available configuration.  If a successful recovery is found
    # and no secondary phase recovery can do better, a diagnosis is
    # issued, the configuration is updated and the function returns
    # "True".  Otherwise, it returns "False".
    #
    def primaryPhase(self, error_token):
        #
        # Initialize the buffer.
        #
        i = (3 if self.nextStackTop >= 0 else 2)
        self.buffer[i] = error_token
        j = i
        while j > 0:
            self.buffer[j - 1] = self.tokStream.getPrevious(self.buffer[j])
            j -= 1

        for k in range(i + 1, self.BUFF_SIZE):
            self.buffer[k] = self.tokStream.getNext(self.buffer[k - 1])

        #
        # If NEXT_STACK_TOP > 0 then the parse was successful on CURRENT_TOKEN
        # and the error was detected on the successor of CURRENT_TOKEN. In
        # that case, first check whether or not primary recovery is
        # possible on next_stack ...
        #
        repair = PrimaryRepairInfo()
        if self.nextStackTop >= 0:
            repair.bufferPosition = 3
            self.checkPrimaryDistance(repair, self.nextStack, self.nextStackTop)

        #
        # ... Try primary recovery on the current token and compare
        # the quality of self recovery to the one on the next token...
        #
        base_repair = PrimaryRepairInfo(repair)
        base_repair.bufferPosition = 2
        self.checkPrimaryDistance(base_repair, self.stateStack, self.stateStackTop)
        if base_repair.distance > repair.distance or base_repair.misspellIndex > repair.misspellIndex:
            repair = base_repair

        #
        # Finally, if prev_stack_top >= 0 try primary recovery on
        # the prev_stack configuration and compare it to the best
        # recovery computed thus far.
        #
        if self.prevStackTop >= 0:
            prev_repair = PrimaryRepairInfo(repair)
            prev_repair.bufferPosition = 1
            self.checkPrimaryDistance(prev_repair, self.prevStack, self.prevStackTop)
            if prev_repair.distance > repair.distance or prev_repair.misspellIndex > repair.misspellIndex:
                repair = prev_repair

        #
        # Before accepting the best primary phase recovery obtained,
        # ensure that we cannot do better with a similar secondary
        # phase recovery.
        #
        candidate = RepairCandidate()
        if self.nextStackTop >= 0:  # next_stack available

            if self.secondaryCheck(self.nextStack, self.nextStackTop, 3, repair.distance):
                return candidate

        else:
            if self.secondaryCheck(self.stateStack, self.stateStackTop, 2, repair.distance):
                return candidate

        #
        # First, adjust distance if the recovery is on the error token
        # it is important that the adjustment be made here and not at
        # each primary trial to prevent the distance tests from being
        # biased in favor of deferred recoveries which have access to
        # more input tokens...
        #
        repair.distance = repair.distance - repair.bufferPosition + 1

        #
        # ...Next, adjust the distance if the recovery is a deletion or
        # (some form of): substitution...
        #
        if (repair.code == ParseErrorCodes.INVALID_CODE or
                repair.code == ParseErrorCodes.DELETION_CODE or
                repair.code == ParseErrorCodes.SUBSTITUTION_CODE or
                repair.code == ParseErrorCodes.MERGE_CODE):
            repair.distance -= 1

        #
        # ... After adjustment, check if the most successful primary
        # recovery can be applied.  If not, continue with more radical
        # recoveries...
        #
        if repair.distance < self.MIN_DISTANCE:
            return candidate

        #
        # When processing an insertion error, if the token preceeding
        # the error token is not available, we change the repair code
        # into a BEFORE_CODE to instruct the reporting routine that it
        # indicates that the repair symbol should be inserted before
        # the error token.
        #
        if repair.code == ParseErrorCodes.INSERTION_CODE:
            if self.tokStream.getKind(self.buffer[repair.bufferPosition - 1]) == 0:
                repair.code = ParseErrorCodes.BEFORE_CODE

        #
        # Select the proper sequence of states on which to recover,
        # update stack accordingly and call diagnostic routine.
        #
        if repair.bufferPosition == 1:
            self.stateStackTop = self.prevStackTop
            arraycopy(self.prevStack, 0, self.stateStack, 0, self.stateStackTop + 1)
        else:
            if self.nextStackTop >= 0 and repair.bufferPosition >= 3:
                self.stateStackTop = self.nextStackTop
                arraycopy(self.nextStack, 0, self.stateStack, 0, self.stateStackTop + 1)
                self.locationStack[self.stateStackTop] = self.buffer[3]

        return self.primaryDiagnosis(repair)

    #
    #  This function checks whether or not a given state has a
    # candidate, whose str representaion is a merging of the two
    # tokens at positions buffer_position and buffer_position+1 in
    # the buffer.  If so, it returns the candidate in question
    # otherwise it returns 0.
    #
    def mergeCandidate(self, state, buffer_position):
        name = self.tokStream.getName(self.buffer[buffer_position]) + self.tokStream.getName(
            self.buffer[buffer_position + 1])
        k = self.asi(state)
        while self.asr(k) != 0:
            i = self.terminalIndex(self.asr(k))
            if len(name) == len(self.name(i)):
                if name.lower() == (self.name(i).lower()):
                    return self.asr(k)
            k += 1
        return 0

    #
    # This procedure takes as arguments a parsing configuration
    # consisting of a state stack (stack and stack_top): and a fixed
    # int of input tokens (starting at buffer_position): in the
    # input BUFFER and some reference arguments: repair_code,
    # distance, misspell_index, candidate, and stack_position
    # which it sets based on the best possible recovery that it
    # finds in the given configuration.  The effectiveness of a
    # a repair is judged based on two criteria:
    #
    #       1): the int of tokens that can be parsed after the repair
    #              is applied: distance.
    #       2): how close to perfection is the candidate that is chosen:
    #              misspell_index.
    #
    # When self procedure is entered, distance, misspell_index and
    # repair_code are assumed to be initialized.
    #

    def checkPrimaryDistance(self, repair, stck, stack_top):
        #
        #  First, try scope recovery.
        #
        scope_repair = PrimaryRepairInfo(repair)
        self.scopeTrial(scope_repair, stck, stack_top)
        if scope_repair.distance > repair.distance:
            repair.copy(scope_repair)

        #
        #  Next, try merging the error token with its successor.
        #
        symbol = self.mergeCandidate(stck[stack_top], repair.bufferPosition)
        if symbol != 0:
            j = self.parseCheck(stck, stack_top, symbol, repair.bufferPosition + 2)
            if (j > repair.distance) or (j == repair.distance and repair.misspellIndex < 10):
                repair.misspellIndex = 10
                repair.symbol = symbol
                repair.distance = j
                repair.code = ParseErrorCodes.MERGE_CODE

        #
        # Next, try deletion of the error token.
        #
        j = self.parseCheck(stck,
                            stack_top,
                            self.tokStream.getKind(self.buffer[repair.bufferPosition + 1]),
                            repair.bufferPosition + 2)

        k = (10 if self.tokStream.getKind(self.buffer[repair.bufferPosition]) == self.EOLT_SYMBOL and
                   self.tokStream.afterEol(self.buffer[repair.bufferPosition + 1])
             else 0)

        if j > repair.distance or (j == repair.distance and k > repair.misspellIndex):
            repair.misspellIndex = k
            repair.code = ParseErrorCodes.DELETION_CODE
            repair.distance = j

        #
        # Update the error configuration by simulating all reduce and
        # goto actions induced by the error token. Then assign the top
        # most state of the  configuration to next_state.
        #
        next_state = stck[stack_top]
        max_pos = stack_top
        self.tempStackTop = stack_top - 1

        self.tokStream.reset(self.buffer[repair.bufferPosition + 1])
        tok = self.tokStream.getKind(self.buffer[repair.bufferPosition])
        act = self.tAction(next_state, tok)
        while act <= self.NUM_RULES:

            while True:
                lhs_symbol = self.lhs(act)
                self.tempStackTop -= (self.rhs(act) - 1)
                act = (self.tempStack[self.tempStackTop]
                       if self.tempStackTop > max_pos
                       else
                       stck[self.tempStackTop])

                act = self.ntAction(act, lhs_symbol)
                if not act <= self.NUM_RULES:
                    break

            max_pos = max_pos if max_pos < self.tempStackTop else self.tempStackTop
            self.tempStack[self.tempStackTop + 1] = act
            next_state = act
            act = self.tAction(next_state, tok)

        #
        #  Next, place the sym_list of candidates in proper order.
        #
        root = 0
        i = self.asi(next_state)
        while self.asr(i) != 0:
            symbol = self.asr(i)
            if symbol != self.EOFT_SYMBOL and symbol != self.ERROR_SYMBOL:
                if root == 0:
                    self.sym_list[symbol] = symbol
                else:
                    self.sym_list[symbol] = self.sym_list[root]
                    self.sym_list[root] = symbol

                root = symbol
            i += 1

        if stck[stack_top] != next_state:
            i = self.asi(stck[stack_top])
            while self.asr(i) != 0:
                symbol = self.asr(i)
                if symbol != self.EOFT_SYMBOL and symbol != self.ERROR_SYMBOL and self.sym_list[symbol] == 0:
                    if root == 0:
                        self.sym_list[symbol] = symbol
                    else:
                        self.sym_list[symbol] = self.sym_list[root]
                        self.sym_list[root] = symbol

                    root = symbol

                i += 1

        head = self.sym_list[root]
        self.sym_list[root] = 0
        root = head

        #
        #  Next, try insertion for each possible candidate available in
        # the current state, except EOFT and ERROR_SYMBOL.
        #

        symbol = root
        while symbol != 0:
            m = self.parseCheck(stck, stack_top, symbol, repair.bufferPosition)
            n = (10 if symbol == self.EOLT_SYMBOL and self.tokStream.afterEol(self.buffer[repair.bufferPosition])
                 else 0)

            if (m > repair.distance or
                    (m == repair.distance and n > repair.misspellIndex)):
                repair.misspellIndex = n
                repair.distance = m
                repair.symbol = symbol
                repair.code = ParseErrorCodes.INSERTION_CODE

            symbol = self.sym_list[symbol]

        #
        #  Next, Try substitution for each possible candidate available
        # in the current state, except EOFT and ERROR_SYMBOL.
        #
        symbol = root
        while symbol != 0:

            m = self.parseCheck(stck, stack_top, symbol, repair.bufferPosition + 1)
            n = (
                10 if symbol == self.EOLT_SYMBOL and self.tokStream.afterEol(self.buffer[repair.bufferPosition + 1])
                else self.misspell(symbol, self.buffer[repair.bufferPosition]))
            if (m > repair.distance or
                    (m == repair.distance and n > repair.misspellIndex)):
                repair.misspellIndex = n
                repair.distance = m
                repair.symbol = symbol
                repair.code = ParseErrorCodes.SUBSTITUTION_CODE

            s = symbol
            symbol = self.sym_list[symbol]
            self.sym_list[s] = 0  # reset element

        #
        # Next, we try to insert a nonterminal candidate in front of the
        # error token, or substituting a nonterminal candidate for the
        # error token. Precedence is given to insertion.
        #
        nt_index = self.nasi(stck[stack_top])
        while self.nasr(nt_index) != 0:
            symbol = self.nasr(nt_index) + self.NT_OFFSET
            n = self.parseCheck(stck, stack_top, symbol, repair.bufferPosition + 1)
            if n > repair.distance:
                repair.misspellIndex = 0
                repair.distance = n
                repair.symbol = symbol
                repair.code = ParseErrorCodes.INVALID_CODE

            n = self.parseCheck(stck, stack_top, symbol, repair.bufferPosition)
            if n > repair.distance or (n == repair.distance and repair.code == ParseErrorCodes.INVALID_CODE):
                repair.misspellIndex = 0
                repair.distance = n
                repair.symbol = symbol
                repair.code = ParseErrorCodes.INSERTION_CODE

            nt_index += 1

        return

    #
    # This procedure is invoked to issue a diagnostic message and
    # adjust the input buffer.  The recovery in question is either
    # the insertion of one or more scopes, the merging of the error
    # token with its successor, the deletion of the error token,
    # the insertion of a single token in front of the error token
    # or the substitution of another token for the error token.
    #
    def primaryDiagnosis(self, repair):
        #
        #  Issue diagnostic.
        #
        prevtok = self.buffer[repair.bufferPosition - 1]
        current_token = self.buffer[repair.bufferPosition]

        if (repair.code == ParseErrorCodes.INSERTION_CODE or
                repair.code == ParseErrorCodes.BEFORE_CODE):

            name_index = (self.getNtermIndex(self.stateStack[self.stateStackTop],
                                             repair.symbol,
                                             repair.bufferPosition)
                          if repair.symbol > self.NT_OFFSET
                          else self.getTermIndex(self.stateStack,
                                                 self.stateStackTop,
                                                 repair.symbol,
                                                 repair.bufferPosition))

            tok = (prevtok if repair.code == ParseErrorCodes.INSERTION_CODE else current_token)
            self.emitError(repair.code, name_index, tok, tok)

        elif repair.code == ParseErrorCodes.INVALID_CODE:

            name_index = self.getNtermIndex(self.stateStack[self.stateStackTop],
                                            repair.symbol,
                                            repair.bufferPosition + 1)
            self.emitError(repair.code, name_index, current_token, current_token)

        elif repair.code == ParseErrorCodes.SUBSTITUTION_CODE:

            name_index = 0
            if repair.misspellIndex >= 6:
                name_index = self.terminalIndex(repair.symbol)
            else:
                name_index = self.getTermIndex(self.stateStack,
                                               self.stateStackTop,
                                               repair.symbol,
                                               repair.bufferPosition + 1)
                if name_index != self.terminalIndex(repair.symbol):
                    repair.code = ParseErrorCodes.INVALID_CODE

            self.emitError(repair.code, name_index, current_token, current_token)

        elif repair.code == ParseErrorCodes.MERGE_CODE:
            self.emitError(repair.code,
                           self.terminalIndex(repair.symbol),
                           current_token,
                           self.tokStream.getNext(current_token))

        elif repair.code == ParseErrorCodes.SCOPE_CODE:

            for i in range(0, self.scopeStackTop):
                self.emitError(repair.code,
                               -self.scopeIndex[i],
                               self.locationStack[self.scopePosition[i]],
                               prevtok,
                               self.nonterminalIndex(self.scopeLhs(self.scopeIndex[i])))

            repair.symbol = self.scopeLhs(self.scopeIndex[self.scopeStackTop]) + self.NT_OFFSET
            self.stateStackTop = self.scopePosition[self.scopeStackTop]
            self.emitError(repair.code,
                           -self.scopeIndex[self.scopeStackTop],
                           self.locationStack[self.scopePosition[self.scopeStackTop]],
                           prevtok,
                           self.getNtermIndex(self.stateStack[self.stateStackTop],
                                              repair.symbol,
                                              repair.bufferPosition))
        else:  # deletion
            self.emitError(repair.code, self.terminalIndex(self.ERROR_SYMBOL), current_token, current_token)

        #
        #  Update buffer.
        #
        candidate = RepairCandidate()

        if (repair.code == ParseErrorCodes.INSERTION_CODE or
                repair.code == ParseErrorCodes.BEFORE_CODE or
                repair.code == ParseErrorCodes.SCOPE_CODE):
            candidate.symbol = repair.symbol
            candidate.location = self.buffer[repair.bufferPosition]
            self.tokStream.reset(self.buffer[repair.bufferPosition])

        elif (repair.code == ParseErrorCodes.INVALID_CODE or
              repair.code == ParseErrorCodes.SUBSTITUTION_CODE):
            candidate.symbol = repair.symbol
            candidate.location = self.buffer[repair.bufferPosition]
            self.tokStream.reset(self.buffer[repair.bufferPosition + 1])

        elif repair.code == ParseErrorCodes.MERGE_CODE:
            candidate.symbol = repair.symbol
            candidate.location = self.buffer[repair.bufferPosition]
            self.tokStream.reset(self.buffer[repair.bufferPosition + 2])

        else:  # deletion
            candidate.location = self.buffer[repair.bufferPosition + 1]
            candidate.symbol = self.tokStream.getKind(self.buffer[repair.bufferPosition + 1])
            self.tokStream.reset(self.buffer[repair.bufferPosition + 2])

        return candidate

    #
    # This function takes as parameter an integer STACK_TOP that
    # points to a STACK element containing the state on which a
    # primary recovery will be made the terminal candidate on which
    # to recover and an integer: buffer_position, which points to
    # the position of the next input token in the BUFFER.  The
    # parser is simulated until a shift (or shift-reduce): action
    # is computed on the candidate.  Then we proceed to compute the
    # the name index of the highest level nonterminal that can
    # directly or indirectly produce the candidate.
    #
    def getTermIndex(self, stck, stack_top, tok, buffer_position):
        #
        # Initialize stack index of temp_stack and initialize maximum
        # position of state stack that is still useful.
        #
        act = stck[stack_top]
        max_pos = stack_top
        highest_symbol = tok

        self.tempStackTop = stack_top - 1

        #
        # Compute all reduce and associated actions induced by the
        # candidate until a SHIFT or SHIFT-REDUCE is computed. ERROR
        # and ACCEPT actions cannot be computed on the candidate in
        # self context, since we know that it is suitable for recovery.
        #
        self.tokStream.reset(self.buffer[buffer_position])
        act = self.tAction(act, tok)
        while act <= self.NUM_RULES:
            #
            # Process all goto-reduce actions following reduction,
            # until a goto action is computed ...
            #
            while True:
                lhs_symbol = self.lhs(act)
                self.tempStackTop -= (self.rhs(act) - 1)
                act = (self.tempStack[self.tempStackTop]
                       if self.tempStackTop > max_pos
                       else stck[self.tempStackTop])

                act = self.ntAction(act, lhs_symbol)
                if not act <= self.NUM_RULES:
                    break
            #
            # Compute  maximum useful position of (STATE_):stack,
            # push goto state into the stack, and compute next
            # action on candidate ...
            #
            max_pos = max_pos if max_pos < self.tempStackTop else self.tempStackTop
            self.tempStack[self.tempStackTop + 1] = act
            act = self.tAction(act, tok)

        #
        # At self stage, we have simulated all actions induced by the
        # candidate and we are ready to shift or shift-reduce it. First,
        # set tok and next_ptr appropriately and identify the candidate
        # as the initial highest_symbol. If a shift action was computed
        # on the candidate, update the stack and compute the next
        # action. Next, simulate all actions possible on the next input
        # token until we either have to shift it or are about to reduce
        # below the initial starting point in the stack (indicated by
        # max_pos as computed in the previous loop).  At that point,
        # return the highest_symbol computed.
        #
        self.tempStackTop += 1  # adjust top of stack to reflect last goto
        # next move is shift or shift-reduce.

        threshold = self.tempStackTop

        tok = self.tokStream.getKind(self.buffer[buffer_position])
        self.tokStream.reset(self.buffer[buffer_position + 1])

        if act > self.ERROR_ACTION:  # shift-reduce on candidate?
            act -= self.ERROR_ACTION
        elif act < self.ACCEPT_ACTION:  # shift on candidate
            self.tempStack[self.tempStackTop + 1] = act
            act = self.tAction(act, tok)

        while act <= self.NUM_RULES:
            #
            # Process all goto-reduce actions following reduction,
            # until a goto action is computed ...
            #
            while True:
                lhs_symbol = self.lhs(act)
                self.tempStackTop -= (self.rhs(act) - 1)

                if self.tempStackTop < threshold:
                    return (self.nonterminalIndex(highest_symbol - self.NT_OFFSET)
                            if highest_symbol > self.NT_OFFSET
                            else self.terminalIndex(highest_symbol))

                if self.tempStackTop == threshold:
                    highest_symbol = lhs_symbol + self.NT_OFFSET

                act = (self.tempStack[self.tempStackTop]
                       if self.tempStackTop > max_pos
                       else stck[self.tempStackTop])

                act = self.ntAction(act, lhs_symbol)
                if not act <= self.NUM_RULES:
                    break

            self.tempStack[self.tempStackTop + 1] = act
            act = self.tAction(act, tok)

        return (self.nonterminalIndex(highest_symbol - self.NT_OFFSET) if highest_symbol > self.NT_OFFSET
                else self.terminalIndex(highest_symbol))

    #
    # This function takes as parameter a starting state int:
    # start, a nonterminal symbol, A (candidate):, and an integer,
    # buffer_position,  which points to the position of the next
    # input token in the BUFFER.
    # It returns the highest level non-terminal B such that
    # B =>*rm A.  I.e., there does not exists a nonterminal C such
    # that C =>+rm B. (Recall that for an LALR(k): grammar if
    # C =>+rm B, it cannot be the case that B =>+rm C):
    #
    def getNtermIndex(self, start, sym, buffer_position):
        highest_symbol = sym - self.NT_OFFSET
        tok = self.tokStream.getKind(self.buffer[buffer_position])
        self.tokStream.reset(self.buffer[buffer_position + 1])

        #
        # Initialize stack index of temp_stack and initialize maximum
        # position of state stack that is still useful.
        #
        self.tempStackTop = 0
        self.tempStack[self.tempStackTop] = start

        act = self.ntAction(start, highest_symbol)
        if act > self.NUM_RULES:  # goto action?
            self.tempStack[self.tempStackTop + 1] = act
            act = self.tAction(act, tok)

        while act <= self.NUM_RULES:
            #
            # Process all goto-reduce actions following reduction,
            # until a goto action is computed ...
            #
            while True:
                self.tempStackTop -= (self.rhs(act) - 1)
                if self.tempStackTop < 0:
                    return self.nonterminalIndex(highest_symbol)

                if self.tempStackTop == 0:
                    highest_symbol = self.lhs(act)

                act = self.ntAction(self.tempStack[self.tempStackTop], self.lhs(act))
                if not act <= self.NUM_RULES:
                    break
            self.tempStack[self.tempStackTop + 1] = act
            act = self.tAction(act, tok)

        return self.nonterminalIndex(highest_symbol)

    #
    #  Check whether or not there is a high probability that a
    # given str is a misspelling of another.
    # Certain singleton symbols (such as ":" and ""): are also
    # considered to be misspellings of each other.
    #
    def misspell(self, sym, tok):
        #
        # Set up the two strings in question. Note that there is a "0"
        # gate added at the end of each str. This is important as
        # the algorithm assumes that it can "peek" at the symbol immediately
        # following the one that is being analysed.
        #
        s1 = (self.name(self.terminalIndex(sym))).lower()
        n = s1.__len__()
        s1 += '\u0000'
        s2 = (self.tokStream.getName(tok)).lower()

        m = (s2.__len__() if s2.__len__() < self.MAX_NAME_LENGTH else self.MAX_NAME_LENGTH)
        s2 = s2[0:m] + '\u0000'

        #
        #  Singleton misspellings:
        #
        #        <---->     ,
        #
        #        <---->     :
        #
        #  .      <---->     ,
        #
        #  '      <---->     "
        #
        #
        if n == 1 and m == 1:
            if ((s1[0] == ';' and s2[0] == ',') or
                    (s1[0] == ',' and s2[0] == ';') or
                    (s1[0] == ';' and s2[0] == ':') or
                    (s1[0] == ':' and s2[0] == ';') or
                    (s1[0] == '.' and s2[0] == ',') or
                    (s1[0] == ',' and s2[0] == '.') or
                    (s1[0] == '\'' and s2[0] == '\"') or
                    (s1[0] == '\"' and s2[0] == '\'')):
                return 3

        #
        # Scan the two strings. Increment "match" count for each match.
        # When a transposition is encountered, increase "match" count
        # by two but count it as one error. When a typo is found, skip
        # it and count it as one error. Otherwise we have a mismatch if
        # one of the strings is longer, increment its index, otherwise,
        # increment both indices and continue.
        #
        # This algorithm is an adaptation of a bool misspelling
        # algorithm proposed by Juergen Uhl.
        #
        count = 0
        prefix_length = 0
        num_errors = 0

        i = 0
        j = 0

        while (i < n) and (j < m):
            if s1[i] == s2[j]:
                count += 1
                i += 1
                j += 1
                if num_errors == 0:
                    prefix_length += 1

            elif s1[i + 1] == s2[j] and s1[i] == s2[j + 1]:  # transposition

                count += 2
                i += 2
                j += 2
                num_errors += 1

            elif s1[i + 1] == s2[j + 1]:  # mismatch

                i += 2
                j += 2
                num_errors += 1

            else:

                if (n - i) > (m - j):
                    i += 1

                elif (m - j) > (n - i):
                    j += 1

                else:
                    i += 1
                    j += 1

                num_errors += 1

        if i < n or j < m:
            num_errors += 1

        if num_errors > ((n if n < m else m) / 6 + 1):
            count = prefix_length

        return (count * 10) // ((s1.__len__() if n < s1.__len__() else n) + num_errors)

    def scopeTrial(self, repair, stack, stack_top):

        if (self.stateSeen is None or self.stateSeen.__len__() == 0 or self.stateSeen.__len__()
                < len(self.stateStack)):
            self.stateSeen = [0] * (len(self.stateStack))

        for i in range(0, len(self.stateStack)):
            self.stateSeen[i] = DiagnoseParser.NIL

        self.statePoolTop = 0
        if (self.statePool is None or self.statePool.__len__() == 0 or
                self.statePool.__len__() < len(self.stateStack)):
            self.statePool = [None] * (len(self.stateStack))

        self.scopeTrialCheck(repair, stack, stack_top, 0)

        repair.code = ParseErrorCodes.SCOPE_CODE

        repair.misspellIndex = 10

        return

    def scopeTrialCheck(self, repair, stack, stack_top, indx):

        i = self.stateSeen[stack_top]
        while i != DiagnoseParser.NIL:
            if self.statePool[i].state == stack[stack_top]:
                return
            i = self.statePool[i].next

        old_state_pool_top = self.statePoolTop
        self.statePoolTop += 1

        if self.statePoolTop >= self.statePool.__len__():
            self.statePool = arraycopy(self.statePool, 0, [None] * (self.statePoolTop * 2), 0, self.statePoolTop)

        self.statePool[old_state_pool_top] = StateInfo(stack[stack_top], self.stateSeen[stack_top])
        self.stateSeen[stack_top] = old_state_pool_top

        action = IntTuple(1 << 3)
        for i in range(0, self.SCOPE_SIZE):
            #
            # Compute the action (or set of actions in case of conflicts): that
            # can be executed on the scope lookahead symbol. Save the action(s):
            # in the action tuple.
            #
            action.reset()
            act = self.tAction(stack[stack_top], self.scopeLa(i))
            if act > self.ACCEPT_ACTION and act < self.ERROR_ACTION:  # conflicting actions?

                while True:

                    action.add(self.baseAction(act))
                    act += 1

                    if not self.baseAction(act) != 0:
                        break
            else:
                action.add(act)

            #
            # For each action defined on the scope lookahead symbol,
            # try scope recovery.
            #
            for action_index in range(0, action.size()):

                self.tokStream.reset(self.buffer[repair.bufferPosition])
                self.tempStackTop = stack_top - 1
                max_pos = stack_top

                act = action.get(action_index)
                while act <= self.NUM_RULES:
                    #
                    # ... Process all goto-reduce actions following
                    # reduction, until a goto action is computed ...
                    #
                    while True:
                        lhs_symbol = self.lhs(act)
                        self.tempStackTop -= (self.rhs(act) - 1)
                        act = (self.tempStack[self.tempStackTop] if self.tempStackTop > max_pos
                               else stack[self.tempStackTop])

                        act = self.ntAction(act, lhs_symbol)
                        if not act <= self.NUM_RULES:
                            break
                    if self.tempStackTop + 1 >= len(self.stateStack):
                        return

                    max_pos = max_pos if max_pos < self.tempStackTop else self.tempStackTop
                    self.tempStack[self.tempStackTop + 1] = act
                    act = self.tAction(act, self.scopeLa(i))

                #
                # If the lookahead symbol is parsable, then we check
                # whether or not we have a match between the scope
                # prefix and the transition symbols corresponding to
                # the states on top of the stack.
                #
                if act != self.ERROR_ACTION:

                    k = self.scopePrefix(i)
                    j = self.tempStackTop + 1
                    while (
                            j >= (max_pos + 1) and
                            self.inSymbol(self.tempStack[j]) == self.scopeRhs(k)):
                        k += 1
                        j -= 1

                    if j == max_pos:
                        while (
                                j >= 1 and self.inSymbol(stack[j]) == self.scopeRhs(k)
                        ):
                            j -= 1
                            k += 1

                    #
                    # If the prefix matches, check whether the state
                    # newly exposed on top of the stack, (after the
                    # corresponding prefix states are popped from the
                    # stack):, is in the set of "source states" for the
                    # scope in question and that it is at a position
                    # below the threshold indicated by MARKED_POS.
                    #
                    marked_pos = (max_pos + 1 if max_pos < stack_top else stack_top)
                    if self.scopeRhs(k) == 0 and j < marked_pos:  # match?
                        stack_position = j
                        j = self.scopeStateSet(i)
                        while stack[stack_position] != self.scopeState(j) and self.scopeState(j) != 0:
                            j += 1

                        #
                        # If the top state is valid for scope recovery,
                        # the left-hand side of the scope is used as
                        # starting symbol and we calculate how far the
                        # parser can advance within the forward context
                        # after parsing the left-hand symbol.
                        #
                        if self.scopeState(j) != 0:  # state was found
                            previous_distance = repair.distance
                            distance = self.parseCheck(stack,
                                                       stack_position,
                                                       self.scopeLhs(i) + self.NT_OFFSET,
                                                       repair.bufferPosition)

                            #
                            # if the recovery is not successful, we
                            # update the stack with all actions induced
                            # by the left-hand symbol, and recursively
                            # call SCOPE_TRIAL_CHECK to try again.
                            # Otherwise, the recovery is successful. If
                            # the  distance is greater than the
                            # initial SCOPE_DISTANCE, we update
                            # SCOPE_DISTANCE and set scope_stack_top to INDX
                            # to indicate the int of scopes that are
                            # to be applied for a succesful  recovery.
                            # NOTE that self procedure cannot get into
                            # an infinite loop, since each prefix match
                            # is guaranteed to take us to a lower point
                            # within the stack.
                            #
                            if (distance - repair.bufferPosition + 1) < self.MIN_DISTANCE:
                                top = stack_position
                                act = self.ntAction(stack[top], self.scopeLhs(i))
                                while act <= self.NUM_RULES:
                                    top -= (self.rhs(act) - 1)
                                    act = self.ntAction(stack[top], self.lhs(act))

                                top += 1
                                j = act
                                act = stack[top]  # save
                                stack[top] = j  # swap
                                self.scopeTrialCheck(repair, stack, top, indx + 1)
                                stack[top] = act  # restore

                            elif distance > repair.distance:

                                self.scopeStackTop = indx
                                repair.distance = distance

                            #
                            # If no other recovery possibility is left (due to
                            # backtracking and we are at the end of the input,
                            # then we favor a scope recovery over all other kinds
                            # of recovery.
                            #
                            if (
                                    # TODO: main_configuration_stack.size(): == 0 and # no other bactracking possibilities left
                                    self.tokStream.getKind(self.buffer[repair.bufferPosition]) == self.EOFT_SYMBOL and
                                    repair.distance == previous_distance):
                                self.scopeStackTop = indx
                                repair.distance = self.MAX_DISTANCE

                            #
                            # If self scope recovery has beaten the
                            # previous distance, then we have found a
                            # better recovery (or self recovery is one
                            # of a sym_list of scope recoveries). Record
                            # its information at the proper location
                            # (INDX): in SCOPE_INDEX and SCOPE_STACK.
                            #
                            if repair.distance > previous_distance:
                                self.scopeIndex[indx] = i
                                self.scopePosition[indx] = stack_position
                                return

    #
    # This function computes the ParseCheck distance for the best
    # possible secondary recovery for a given configuration that
    # either deletes none or only one symbol in the forward context.
    # If the recovery found is more effective than the best primary
    # recovery previously computed, then the function returns True.
    # Only misplacement, scope and manual recoveries are attempted
    # simple insertion or substitution of a nonterminal are tried
    # in CHECK_PRIMARY_DISTANCE as part of primary recovery.
    #
    def secondaryCheck(self, stack, stack_top, buffer_position, distance):
        top = stack_top - 1
        while top >= 0:
            j = self.parseCheck(stack,
                                top,
                                self.tokStream.getKind(self.buffer[buffer_position]),
                                buffer_position + 1)
            if ((j - buffer_position + 1) > self.MIN_DISTANCE) and (j > distance):
                return True

            top -= 1

        scope_repair = PrimaryRepairInfo()
        scope_repair.bufferPosition = buffer_position + 1
        scope_repair.distance = distance
        self.scopeTrial(scope_repair, stack, stack_top)
        return (scope_repair.distance - buffer_position) > self.MIN_DISTANCE and scope_repair.distance > distance

    #
    # Secondary_phase is a bool function that checks whether or
    # not some form of secondary recovery is applicable to one of
    # the error configurations. First, if "next_stack" is available,
    # misplacement and secondary recoveries are attempted on it.
    # Then, in any case, these recoveries are attempted on "stack".
    # If a successful recovery is found, a diagnosis is issued, the
    # configuration is updated and the function returns "True".
    # Otherwise, the function returns False.
    #
    def secondaryPhase(self, error_token):
        repair = SecondaryRepairInfo()
        misplaced_repair = SecondaryRepairInfo()

        #
        # If the next_stack is available, try misplaced and secondary
        # recovery on it first.
        #
        next_last_index = 0
        if self.nextStackTop >= 0:

            save_location = 0

            self.buffer[2] = error_token
            self.buffer[1] = self.tokStream.getPrevious(self.buffer[2])
            self.buffer[0] = self.tokStream.getPrevious(self.buffer[1])
            for k in range(3, self.BUFF_UBOUND):
                self.buffer[k] = self.tokStream.getNext(self.buffer[k - 1])

            self.buffer[self.BUFF_UBOUND] = self.tokStream.badToken()  # elmt not available
            #
            # If we are at the end of the input stream, compute the
            # index position of the first EOFT symbol (last useful
            # index).
            #
            next_last_index = self.MAX_DISTANCE - 1
            while (next_last_index >= 1 and
                   self.tokStream.getKind(self.buffer[next_last_index]) == self.EOFT_SYMBOL):
                next_last_index -= 1

            next_last_index = next_last_index + 1

            save_location = self.locationStack[self.nextStackTop]
            self.locationStack[self.nextStackTop] = self.buffer[2]
            misplaced_repair.numDeletions = self.nextStackTop
            self.misplacementRecovery(misplaced_repair, self.nextStack, self.nextStackTop, next_last_index, True)
            if misplaced_repair.recoveryOnNextStack:
                misplaced_repair.distance += 1

            repair.numDeletions = self.nextStackTop + self.BUFF_UBOUND
            self.secondaryRecovery(repair,
                                   self.nextStack,
                                   self.nextStackTop,
                                   next_last_index, True)

            if repair.recoveryOnNextStack:
                repair.distance += 1

            self.locationStack[self.nextStackTop] = save_location
        else:  # next_stack not available, initialize ...
            misplaced_repair.numDeletions = self.stateStackTop
            repair.numDeletions = self.stateStackTop + self.BUFF_UBOUND

        #
        # Try secondary recovery on the "stack" configuration.
        #
        self.buffer[3] = error_token

        self.buffer[2] = self.tokStream.getPrevious(self.buffer[3])
        self.buffer[1] = self.tokStream.getPrevious(self.buffer[2])
        self.buffer[0] = self.tokStream.getPrevious(self.buffer[1])

        for k in range(4, self.BUFF_SIZE):
            self.buffer[k] = self.tokStream.getNext(self.buffer[k - 1])

        last_index = self.MAX_DISTANCE - 1
        while (last_index >= 1 and
               self.tokStream.getKind(self.buffer[last_index]) == self.EOFT_SYMBOL):
            last_index -= 1

        last_index += 1

        self.misplacementRecovery(misplaced_repair, self.stateStack, self.stateStackTop, last_index, False)

        self.secondaryRecovery(repair, self.stateStack, self.stateStackTop, last_index, False)

        #
        # If a successful misplaced recovery was found, compare it with
        # the most successful secondary recovery.  If the misplaced
        # recovery either deletes fewer symbols or parse-checks further
        # then it is chosen.
        #
        if misplaced_repair.distance > self.MIN_DISTANCE:

            if (misplaced_repair.numDeletions <= repair.numDeletions or
                    (misplaced_repair.distance - misplaced_repair.numDeletions) >=
                    (repair.distance - repair.numDeletions)):
                repair.code = ParseErrorCodes.MISPLACED_CODE
                repair.stackPosition = misplaced_repair.stackPosition
                repair.bufferPosition = 2
                repair.numDeletions = misplaced_repair.numDeletions
                repair.distance = misplaced_repair.distance
                repair.recoveryOnNextStack = misplaced_repair.recoveryOnNextStack

        #
        # If the successful recovery was on next_stack, update: stack,
        # buffer, location_stack and last_index.
        #
        if repair.recoveryOnNextStack:

            self.stateStackTop = self.nextStackTop
            arraycopy(self.nextStack, 0, self.stateStack, 0, self.stateStackTop + 1)

            self.buffer[2] = error_token
            self.buffer[1] = self.tokStream.getPrevious(self.buffer[2])
            self.buffer[0] = self.tokStream.getPrevious(self.buffer[1])

            for k in range(3, self.BUFF_UBOUND):
                self.buffer[k] = self.tokStream.getNext(self.buffer[k - 1])

            self.buffer[self.BUFF_UBOUND] = self.tokStream.badToken()  # elmt not available

            self.locationStack[self.nextStackTop] = self.buffer[2]
            last_index = next_last_index

        #
        # Next, try scope recoveries after deletion of one, two, three,
        # four ... buffer_position tokens from the input stream.
        #
        if repair.code == ParseErrorCodes.SECONDARY_CODE or repair.code == ParseErrorCodes.DELETION_CODE:
            scope_repair = PrimaryRepairInfo()
            scope_repair.bufferPosition = 2
            while (
                    scope_repair.bufferPosition <= repair.bufferPosition and
                    repair.code != ParseErrorCodes.SCOPE_CODE):

                self.scopeTrial(scope_repair, self.stateStack, self.stateStackTop)
                j = (last_index if scope_repair.distance == self.MAX_DISTANCE
                     else scope_repair.distance)

                k = scope_repair.bufferPosition - 1
                if ((scope_repair.distance - k) > self.MIN_DISTANCE and (j - k) > (
                        repair.distance - repair.numDeletions)):
                    i = self.scopeIndex[self.scopeStackTop]  # upper bound
                    repair.code = ParseErrorCodes.SCOPE_CODE
                    repair.symbol = self.scopeLhs(i) + self.NT_OFFSET
                    repair.stackPosition = self.stateStackTop
                    repair.bufferPosition = scope_repair.bufferPosition

                scope_repair.bufferPosition += 1  # for while loop

        #
        # If a successful repair was not found, quit!  Otherwise, issue
        # diagnosis and adjust configuration...
        #
        candidate = RepairCandidate()
        if repair.code == 0:
            return candidate

        self.secondaryDiagnosis(repair)

        #
        # Update buffer based on int of elements that are deleted.
        #

        if repair.code == ParseErrorCodes.MISPLACED_CODE:
            candidate.location = self.buffer[2]
            candidate.symbol = self.tokStream.getKind(self.buffer[2])
            self.tokStream.reset(self.tokStream.getNext(self.buffer[2]))

        elif repair.code == ParseErrorCodes.DELETION_CODE:
            candidate.location = self.buffer[repair.bufferPosition]
            candidate.symbol = self.tokStream.getKind(self.buffer[repair.bufferPosition])
            self.tokStream.reset(self.tokStream.getNext(self.buffer[repair.bufferPosition]))

        else:  # SCOPE_CODE or SECONDARY_CODE
            candidate.symbol = repair.symbol
            candidate.location = self.buffer[repair.bufferPosition]
            self.tokStream.reset(self.buffer[repair.bufferPosition])

        return candidate

    #
    # This bool function checks whether or not a given
    # configuration yields a better misplacement recovery than
    # the best misplacement recovery computed previously.
    #
    def misplacementRecovery(self, repair, stack, stack_top, last_index,
                             stack_flag):
        previous_loc = self.buffer[2]
        stack_deletions = 0
        top = stack_top - 1
        while top >= 0:
            if self.locationStack[top] < previous_loc:
                stack_deletions += 1

            previous_loc = self.locationStack[top]

            parse_distance = self.parseCheck(stack, top, self.tokStream.getKind(self.buffer[2]), 3)
            j = (last_index if parse_distance == self.MAX_DISTANCE else parse_distance)
            if ((parse_distance > self.MIN_DISTANCE) and (j - stack_deletions) > (
                    repair.distance - repair.numDeletions)):
                repair.stackPosition = top
                repair.distance = j
                repair.numDeletions = stack_deletions
                repair.recoveryOnNextStack = stack_flag

            top -= 1

        return

    #
    # This function checks whether or not a given
    # configuration yields a better secondary recovery than the
    # best misplacement recovery computed previously.
    #
    def secondaryRecovery(self, repair, stack, stack_top,
                          last_index, stack_flag):
        previous_loc = self.buffer[2]
        stack_deletions = 0
        top = stack_top
        while top >= 0 and repair.numDeletions >= stack_deletions:
            if self.locationStack[top] < previous_loc:
                stack_deletions += 1

            previous_loc = self.locationStack[top]
            i = 2
            while (i <= (last_index - self.MIN_DISTANCE + 1) and
                   (repair.numDeletions >= (stack_deletions + i - 1))):

                parse_distance = self.parseCheck(stack, top, self.tokStream.getKind(self.buffer[i]), i + 1)
                j = (last_index if parse_distance == self.MAX_DISTANCE else parse_distance)

                if (parse_distance - i + 1) > self.MIN_DISTANCE:

                    k = stack_deletions + i - 1
                    if ((k < repair.numDeletions) or
                            (j - k) > (repair.distance - repair.numDeletions) or
                            ((repair.code == ParseErrorCodes.SECONDARY_CODE) and (j - k) == (
                                    repair.distance - repair.numDeletions))):
                        repair.code = ParseErrorCodes.DELETION_CODE
                        repair.distance = j
                        repair.stackPosition = top
                        repair.bufferPosition = i
                        repair.numDeletions = k
                        repair.recoveryOnNextStack = stack_flag

                ll = self.nasi(stack[top])
                while ll >= 0 and self.nasr(ll) != 0:
                    symbol = self.nasr(ll) + self.NT_OFFSET
                    parse_distance = self.parseCheck(stack, top, symbol, i)
                    j = (last_index if parse_distance == self.MAX_DISTANCE else parse_distance)

                    if (parse_distance - i + 1) > self.MIN_DISTANCE:

                        k = stack_deletions + i - 1
                        if k < repair.numDeletions or (j - k) > (repair.distance - repair.numDeletions):
                            repair.code = ParseErrorCodes.SECONDARY_CODE
                            repair.symbol = symbol
                            repair.distance = j
                            repair.stackPosition = top
                            repair.bufferPosition = i
                            repair.numDeletions = k
                            repair.recoveryOnNextStack = stack_flag
                    ll += 1

                i += 1

            top -= 1

        return

    #
    # This procedure is invoked to issue a secondary diagnosis and
    # adjust the input buffer.  The recovery in question is either
    # an automatic scope recovery, a manual scope recovery, a
    # secondary substitution or a secondary deletion.
    #
    def secondaryDiagnosis(self, repair):

        if repair.code == ParseErrorCodes.SCOPE_CODE:
            if repair.stackPosition < self.stateStackTop:
                self.emitError(ParseErrorCodes.DELETION_CODE,
                               self.terminalIndex(self.ERROR_SYMBOL),
                               self.locationStack[repair.stackPosition],
                               self.buffer[1])

            for i in range(0, self.scopeStackTop):
                self.emitError(ParseErrorCodes.SCOPE_CODE,
                               -self.scopeIndex[i],
                               self.locationStack[self.scopePosition[i]],
                               self.buffer[1],
                               self.nonterminalIndex(self.scopeLhs(self.scopeIndex[i])))

            repair.symbol = self.scopeLhs(self.scopeIndex[self.scopeStackTop]) + self.NT_OFFSET
            self.stateStackTop = self.scopePosition[self.scopeStackTop]
            self.emitError(ParseErrorCodes.SCOPE_CODE,
                           -self.scopeIndex[self.scopeStackTop],
                           self.locationStack[self.scopePosition[self.scopeStackTop]],
                           self.buffer[1],
                           self.getNtermIndex(self.stateStack[self.stateStackTop],
                                              repair.symbol,
                                              repair.bufferPosition))

        else:
            self.emitError(repair.code,
                           (self.getNtermIndex(self.stateStack[repair.stackPosition],
                                               repair.symbol,
                                               repair.bufferPosition)
                            if repair.code == ParseErrorCodes.SECONDARY_CODE
                            else self.terminalIndex(self.ERROR_SYMBOL)),

                           self.locationStack[repair.stackPosition],
                           self.buffer[repair.bufferPosition - 1])

            self.stateStackTop = repair.stackPosition

        return

    #
    # This method is invoked by an LPG PARSER or a semantic
    # routine to process an error message.
    #

    def emitError(self, msg_code, name_index, left_token, right_token, scope_name_index=0):

        left_token_loc = (right_token if left_token > right_token else left_token)
        right_token_loc = right_token

        token_name = (
            ("\"" + self.name(name_index) + "\""
             if name_index >= 0 and not self.name(name_index).upper() == "ERROR" else ""))

        if msg_code == ParseErrorCodes.INVALID_CODE:
            msg_code = ParseErrorCodes.INVALID_CODE if token_name.__len__() == 0 \
                else ParseErrorCodes.INVALID_TOKEN_CODE

        if msg_code == ParseErrorCodes.SCOPE_CODE:
            token_name = "\""
            i = self.scopeSuffix(-name_index)

            while self.scopeRhs(i) != 0:

                if not self.isNullable(self.scopeRhs(i)):
                    symbol_index = (self.nonterminalIndex(self.scopeRhs(i) - self.NT_OFFSET)
                                    if self.scopeRhs(i) > self.NT_OFFSET else self.terminalIndex(self.scopeRhs(i)))

                    if self.name(symbol_index).__len__() > 0:
                        if token_name.__len__() > 1:  # Not just starting quote?
                            token_name += " "  # add a space separator

                        token_name += self.name(symbol_index)

                i += 1

            token_name += "\""

        self.tokStream.reportError(msg_code, left_token, right_token, token_name)
        return

    #
    # keep looking ahead until we compute a valid action
    #
    def lookahead(self, act, token):
        act = self.prs.lookAhead(act - self.LA_STATE_OFFSET, self.tokStream.getKind(token))
        return self.lookahead(act, self.tokStream.getNext(token)) if act > self.LA_STATE_OFFSET else act

    #
    # Compute the next action defined on act and sym. If self
    # action requires more lookahead, these lookahead symbols
    # are in the token stream beginning at the next token that
    # is yielded by peek().
    #
    def tAction(self, act, sym):
        act = self.prs.tAction(act, sym)
        return self.lookahead(act, self.tokStream.peek()) if act > self.LA_STATE_OFFSET else act
