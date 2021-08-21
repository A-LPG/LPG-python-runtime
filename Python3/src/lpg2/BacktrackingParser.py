#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import lpg2
from lpg2.BadParseException import BadParseException
from lpg2.BadParseSymFileException import BadParseSymFileException
from lpg2.ConfigurationStack import ConfigurationStack
from lpg2.ErrorToken import ErrorToken
from lpg2.IntSegmentedTuple import IntSegmentedTuple
from lpg2.IntTuple import IntTuple
from lpg2.Monitor import Monitor
from lpg2.NotBacktrackParseTableException import NotBacktrackParseTableException
from lpg2.ParseTable import ParseTable
from lpg2.IPrsStream import IPrsStream

from lpg2.RuleAction import RuleAction
from lpg2.Stacks import Stacks
from lpg2.TokenStream import TokenStream
from lpg2.TokenStreamNotIPrsStreamException import TokenStreamNotIPrsStreamException
from lpg2.Utils import arraycopy
import sys


class BacktrackingParser(Stacks):

    def __init__(self, tokStream: TokenStream = None, prs: ParseTable = None, ra: RuleAction = None,
                 monitor: Monitor = None):
        super().__init__()
        self.monitor: Monitor = None
        self.START_STATE: int = 0
        self.NUM_RULES: int = 0
        self.NT_OFFSET: int = 0
        self.LA_STATE_OFFSET: int = 0
        self.EOFT_SYMBOL: int = 0
        self.ERROR_SYMBOL: int = 0
        self.ACCEPT_ACTION: int = 0
        self.ERROR_ACTION: int = 0

        self.lastToken: int = 0
        self.currentAction: int = 0

        self.tokStream: TokenStream = tokStream
        self.prs: ParseTable = prs
        self.ra: RuleAction = ra

        self.action: IntSegmentedTuple = IntSegmentedTuple(10, 1024)
        self.tokens: IntTuple = IntTuple(0)
        self.actionStack: list = []
        self.skipTokens: bool = False  # True if error productions are used to skip tokens
        self.markerTokenIndex: int = 0
        self.reset(tokStream, prs, ra, monitor)

    #
    # A starting marker indicates that we are dealing with an entry point
    # for a given nonterminal. We need to execute a shift action on the
    # marker in order to parse the entry point in question.
    #

    def getMarkerToken(self, marker_kind: int, start_token_index: int):
        if marker_kind == 0:
            return 0
        else:
            if self.markerTokenIndex == 0:
                if not isinstance(self.tokStream, IPrsStream):
                    raise TokenStreamNotIPrsStreamException()

                self.markerTokenIndex = self.tokStream.makeErrorToken(self.tokStream.getPrevious(start_token_index),
                                                                      self.tokStream.getPrevious(start_token_index),
                                                                      self.tokStream.getPrevious(start_token_index),
                                                                      marker_kind)
            else:
                temp: IPrsStream = self.tokStream
                temp.getIToken(self.markerTokenIndex).setKind(marker_kind)

        return self.markerTokenIndex

    #
    # Override the getToken function in Stacks.
    #
    def getToken(self, i: int) -> int:
        return self.tokens.get(self.locationStack[self.stateStackTop + (i - 1)])

    def getCurrentRule(self) -> int:
        return self.currentAction

    def getFirstToken2(self) -> int:
        return self.tokStream.getFirstRealToken(self.getToken(1))

    def getFirstToken(self, i: int = None) -> int:
        if i is None:
            return self.getFirstToken2()

        return self.tokStream.getFirstRealToken(self.getToken(i))

    def getLastToken2(self) -> int:
        return self.tokStream.getLastRealToken(self.lastToken)

    def getLastToken(self, i: int = None) -> int:
        if i is None:
            return self.getLastToken2()

        l: int = (self.lastToken if i >= self.prs.rhs(self.currentAction) else
                  self.tokens.get(self.locationStack[self.stateStackTop + i] - 1))
        return self.tokStream.getLastRealToken(l)

    def setMonitor(self, monitor: Monitor):
        self.monitor = monitor

    def reset1(self):
        self.action.reset()
        self.skipTokens = False
        self.markerTokenIndex = 0

    def reset2(self, tokStream: TokenStream, monitor: Monitor = None):
        self.monitor = monitor
        self.tokStream = tokStream
        self.reset1()

    def reset(self, tokStream: TokenStream = None, prs: ParseTable = None, ra: RuleAction = None,
              monitor: Monitor = None):

        if prs is not None:
            self.prs = prs
            self.START_STATE = prs.getStartState()
            self.NUM_RULES = prs.getNumRules()
            self.NT_OFFSET = prs.getNtOffset()
            self.LA_STATE_OFFSET = prs.getLaStateOffset()
            self.EOFT_SYMBOL = prs.getEoftSymbol()
            self.ERROR_SYMBOL = prs.getErrorSymbol()
            self.ACCEPT_ACTION = prs.getAcceptAction()
            self.ERROR_ACTION = prs.getErrorAction()
            if not prs.isValidForParser():
                raise BadParseSymFileException()
            if not prs.getBacktrack():
                raise NotBacktrackParseTableException()

        if ra is not None:
            self.ra = ra

        if not tokStream:
            self.reset1()
            return

        self.reset2(tokStream, monitor)

    def reset3(self, tokStream: TokenStream, prs: ParseTable, ra: RuleAction):
        self.reset(tokStream, prs, ra)

    #
    # Allocate or reallocate all the stacks. Their sizes should always be the same.
    #
    def reallocateOtherStacks(self, start_token_index: int):
        if not self.actionStack or self.actionStack.__len__() == 0:
            length = len(self.stateStack)
            self.actionStack = [0] * length
            self.locationStack = [0] * length
            self.parseStack = [None] * length
            self.actionStack[0] = 0
            self.locationStack[0] = start_token_index
        elif self.actionStack.__len__() < len(self.stateStack):
            length = len(self.stateStack)
            old_length: int = self.actionStack.__len__()
            self.actionStack = arraycopy(self.actionStack, 0, [0] * length, 0, old_length)
            self.locationStack = arraycopy(self.locationStack, 0, [0] * length, 0, old_length)
            self.parseStack = arraycopy(self.parseStack, 0, [None] * length, 0, old_length)

        return

    # def fuzzyParse()
    #    return self.fuzzyParseEntry(0, lpg.lang.Integer.MAX_VALUE):
    #
    def fuzzyParse(self, max_error_count: int = None):
        if max_error_count is None:
            max_error_count = sys.maxsize

        return self.fuzzyParseEntry(0, max_error_count)

    # def fuzzyParseEntry(marker_kind: int)
    #    return self.fuzzyParseEntry(marker_kind, lpg.lang.Integer.MAX_VALUE):
    #
    def fuzzyParseEntry(self, marker_kind: int, max_error_count: int = None):
        if max_error_count is None:
            max_error_count = sys.maxsize

        self.action.reset()
        self.tokStream.reset()  # Position at first token.
        self.reallocateStateStack()
        self.stateStackTop = 0
        self.stateStack[0] = self.START_STATE

        #
        # The tuple tokens will eventually contain the sequence 
        # of tokens that resulted in a successful parse. We leave
        # it up to the "Stream" implementer to define the predecessor
        # of the first token as he sees fit.
        #
        first_token: int = self.tokStream.peek()
        start_token: int = first_token
        marker_token: int = self.getMarkerToken(marker_kind, first_token)

        self.tokens = IntTuple(self.tokStream.getStreamLength())
        self.tokens.add(self.tokStream.getPrevious(first_token))

        error_token: int = self.backtrackParseInternal(self.action, marker_token)
        if error_token != 0:  # an error was detected?
            if not isinstance(self.tokStream, IPrsStream):
                raise TokenStreamNotIPrsStreamException()

            rp = lpg2.RecoveryParser(self, self.action, self.tokens, self.tokStream, self.prs, max_error_count, 0,
                                self.monitor)
            start_token = rp.recover(marker_token, error_token)

        if marker_token != 0 and start_token == first_token:
            self.tokens.add(marker_token)

        t = start_token

        while self.tokStream.getKind(t) != self.EOFT_SYMBOL:
            self.tokens.add(t)
            t = self.tokStream.getNext(t)

        self.tokens.add(t)
        return self.parseActions(marker_kind)

    def parse(self, max_error_count: int = 0):
        return self.parseEntry(0, max_error_count)

    #
    # Parse input allowing up to max_error_count Error token recoveries.
    # When max_error_count is 0, no Error token recoveries occur.
    # When max_error is > 0, it limits the int of Error token recoveries.
    # When max_error is < 0, the int of error token recoveries is unlimited.
    # Also, such recoveries only require one token to be parsed beyond the recovery point.
    # (normally two tokens beyond the recovery point must be parsed):
    # Thus, a negative max_error_count should be used when error productions are used to 
    # skip tokens.
    #
    def parseEntry(self, marker_kind: int = 0, max_error_count: int = 0):
        self.action.reset()
        self.tokStream.reset()  # Position at first token.

        self.reallocateStateStack()
        self.stateStackTop = 0
        self.stateStack[0] = self.START_STATE

        self.skipTokens = max_error_count < 0

        if max_error_count > 0 and isinstance(self.tokStream, IPrsStream):
            max_error_count = 0

        #
        # The tuple tokens will eventually contain the sequence 
        # of tokens that resulted in a successful parse. We leave
        # it up to the "Stream" implementer to define the predecessor
        # of the first token as he sees fit.
        #
        self.tokens = IntTuple(self.tokStream.getStreamLength())
        self.tokens.add(self.tokStream.getPrevious(self.tokStream.peek()))

        start_token_index: int = self.tokStream.peek()
        repair_token: int = self.getMarkerToken(marker_kind, start_token_index)
        start_action_index: int = self.action.size()  # obviously 0
        temp_stack: list = [0] * (self.stateStackTop + 1)
        arraycopy(self.stateStack, 0, temp_stack, 0, len(temp_stack))

        initial_error_token = self.backtrackParseInternal(self.action, repair_token)
        error_token: int = initial_error_token
        count: int = 0
        while error_token != 0:

            if count == max_error_count:
                raise BadParseException(initial_error_token)

            self.action.reset(start_action_index)
            self.tokStream.reset(start_token_index)
            self.stateStackTop = len(temp_stack) - 1
            arraycopy(temp_stack, 0, self.stateStack, 0, len(temp_stack))
            self.reallocateOtherStacks(start_token_index)

            self.backtrackParseUpToError(repair_token, error_token)
            self.stateStackTop = self.findRecoveryStateIndex(self.stateStackTop)
            while self.stateStackTop >= 0:

                recovery_token = self.tokens.get(self.locationStack[self.stateStackTop] - 1)
                repair_token = self.errorRepair(self.tokStream,
                                                (
                                                    recovery_token if recovery_token >= start_token_index else error_token),
                                                error_token)

                if repair_token != 0:
                    break
                self.stateStackTop = self.findRecoveryStateIndex(self.stateStackTop - 1)

            if self.stateStackTop < 0:
                raise BadParseException(initial_error_token)

            temp_stack = [0] * (self.stateStackTop + 1)
            arraycopy(self.stateStack, 0, temp_stack, 0, len(temp_stack))

            start_action_index = self.action.size()
            start_token_index = self.tokStream.peek()

            error_token = self.backtrackParseInternal(self.action, repair_token)
            count += 1

        if repair_token != 0:
            self.tokens.add(repair_token)

        t = start_token_index
        while self.tokStream.getKind(t) != self.EOFT_SYMBOL:
            self.tokens.add(t)
            t = self.tokStream.getNext(t)

        self.tokens.add(t)
        return self.parseActions(marker_kind)

    #
    # Process reductions and continue...
    #
    def process_reductions(self):
        while True:
            self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
            self.ra.ruleAction(self.currentAction)
            self.currentAction = self.prs.ntAction(self.stateStack[self.stateStackTop],
                                                   self.prs.lhs(self.currentAction))
            if not self.currentAction <= self.NUM_RULES:
                break
        return

    #
    # Now do the final parse of the input based on the actions in
    # the list "action" and the sequence of tokens in list "tokens".
    #
    def parseActions(self, marker_kind: int):
        ti: int = -1
        curtok: int

        ti += 1
        self.lastToken = self.tokens.get(ti)

        ti += 1
        curtok = self.tokens.get(ti)

        self.allocateOtherStacks()
        #
        # Reparse the input...
        #
        self.stateStackTop = -1
        self.currentAction = self.START_STATE
        for i in range(0, self.action.size()):
            #
            # if the parser needs to stop processing, it may do so here.
            #
            if self.monitor and self.monitor.isCancelled():
                return None

            self.stateStackTop += 1
            self.stateStack[self.stateStackTop] = self.currentAction

            self.locationStack[self.stateStackTop] = ti

            self.currentAction = self.action.get(i)
            if self.currentAction <= self.NUM_RULES:  # a reduce action?
                self.stateStackTop -= 1  # make reduction look like shift-reduction
                self.process_reductions()
            else:  # a shift or shift-reduce action
                if self.tokStream.getKind(curtok) > self.NT_OFFSET:
                    badtok: ErrorToken = self.tokStream.getIToken(curtok)
                    raise BadParseException(badtok.getErrorToken().getTokenIndex())

                self.lastToken = curtok

                ti += 1
                curtok = self.tokens.get(ti)

                if self.currentAction > self.ERROR_ACTION:
                    self.currentAction -= self.ERROR_ACTION
                    self.process_reductions()

        return self.parseStack[0 if marker_kind == 0 else 1]

    #
    # Process reductions and continue...
    #
    def process_backtrack_reductions(self, act: int):
        while True:
            self.stateStackTop -= (self.prs.rhs(act) - 1)
            act = self.prs.ntAction(self.stateStack[self.stateStackTop], self.prs.lhs(act))
            if not act <= self.NUM_RULES:
                break

        return act

    #
    # This method is intended to be used by the type RecoveryParser.
    # Note that the action tuple passed here must be the same action
    # tuple that was passed down to RecoveryParser. It is passed back
    # to self method as documention.
    #
    def backtrackParse(self, stack, stack_top: int, action: IntSegmentedTuple, initial_token: int):
        self.stateStackTop = stack_top
        arraycopy(stack, 0, self.stateStack, 0, self.stateStackTop + 1)
        return self.backtrackParseInternal(action, initial_token)

    #
    # Parse the input until either the parse completes successfully or
    # an error is encountered. This function returns an integer that
    # represents the last action that was executed by the parser. If
    # the parse was succesful, then the tuple "action" contains the
    # successful sequence of actions that was executed.
    #
    def backtrackParseInternal(self, action: IntSegmentedTuple, initial_token: int):
        #
        # Allocate configuration stack.
        #
        configuration_stack: ConfigurationStack = ConfigurationStack(self.prs)

        #
        # Keep parsing until we successfully reach the end of file or
        # an error is encountered. The list of actions executed will
        # be stored in the "action" tuple.
        #
        error_token: int = 0
        maxStackTop: int = self.stateStackTop
        start_token: int = self.tokStream.peek()
        curtok: int = (initial_token if initial_token > 0 else self.tokStream.getToken())
        current_kind: int = self.tokStream.getKind(curtok)
        act: int = self.tAction(self.stateStack[self.stateStackTop], current_kind)
        #
        # The main driver loop
        #
        while True:
            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if self.monitor and self.monitor.isCancelled():
                return 0

            if act <= self.NUM_RULES:
                action.add(act)  # save self reduce action
                self.stateStackTop -= 1
                act = self.process_backtrack_reductions(act)

            elif act > self.ERROR_ACTION:

                action.add(act)  # save self shift-reduce action
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
                act = self.process_backtrack_reductions(act - self.ERROR_ACTION)

            elif act < self.ACCEPT_ACTION:

                action.add(act)  # save self shift action
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)

            elif act == self.ERROR_ACTION:

                error_token = (error_token if error_token > curtok else curtok)

                configuration = configuration_stack.pop()
                if configuration is None:
                    act = self.ERROR_ACTION
                else:
                    action.reset(configuration.action_length)
                    act = configuration.act
                    curtok = configuration.curtok
                    current_kind = self.tokStream.getKind(curtok)
                    self.tokStream.reset(start_token if curtok == initial_token else
                                         self.tokStream.getNext(curtok))

                    self.stateStackTop = configuration.stack_top
                    configuration.retrieveStack(self.stateStack)
                    continue

                break

            elif act > self.ACCEPT_ACTION:

                if configuration_stack.findConfiguration(self.stateStack, self.stateStackTop, curtok):
                    act = self.ERROR_ACTION
                else:
                    configuration_stack.push(self.stateStack, self.stateStackTop, act + 1, curtok, action.size())
                    act = self.prs.baseAction(act)
                    maxStackTop = self.stateStackTop if self.stateStackTop > maxStackTop else maxStackTop

                continue

            else:
                break  # assert(act == ACCEPT_ACTION):

            self.stateStackTop += 1
            if self.stateStackTop >= len(self.stateStack):
                self.reallocateStateStack()

            self.stateStack[self.stateStackTop] = act

            act = self.tAction(act, current_kind)

        return error_token if act == self.ERROR_ACTION else 0

    def backtrackParseUpToError(self, initial_token: int, error_token: int):
        #
        # Allocate configuration stack.
        #
        configuration_stack = ConfigurationStack(self.prs)

        #
        # Keep parsing until we successfully reach the end of file or
        # an error is encountered. The list of actions executed will
        # be stored in the "action" tuple.
        #
        start_token: int = self.tokStream.peek()
        curtok: int = (initial_token if initial_token > 0 else self.tokStream.getToken())
        current_kind: int = self.tokStream.getKind(curtok)
        act: int = self.tAction(self.stateStack[self.stateStackTop], current_kind)

        self.tokens.add(curtok)
        self.locationStack[self.stateStackTop] = self.tokens.size()
        self.actionStack[self.stateStackTop] = self.action.size()

        while True:
            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if self.monitor and self.monitor.isCancelled():
                return

            if act <= self.NUM_RULES:
                self.action.add(act)  # save self reduce action
                self.stateStackTop -= 1
                act = self.process_backtrack_reductions(act)

            elif act > self.ERROR_ACTION:

                self.action.add(act)  # save self shift-reduce action
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
                self.tokens.add(curtok)
                act = self.process_backtrack_reductions(act - self.ERROR_ACTION)

            elif act < self.ACCEPT_ACTION:

                self.action.add(act)  # save self shift action
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
                self.tokens.add(curtok)

            elif act == self.ERROR_ACTION:

                if curtok != error_token:
                    configuration = configuration_stack.pop()
                    if configuration is None:
                        act = self.ERROR_ACTION
                    else:
                        self.action.reset(configuration.action_length)
                        act = configuration.act
                        next_token_index: int = configuration.curtok
                        self.tokens.reset(next_token_index)
                        curtok = self.tokens.get(next_token_index - 1)
                        current_kind = self.tokStream.getKind(curtok)
                        self.tokStream.reset(start_token if curtok == initial_token else self.tokStream.getNext(curtok))
                        self.stateStackTop = configuration.stack_top
                        configuration.retrieveStack(self.stateStack)
                        self.locationStack[self.stateStackTop] = self.tokens.size()
                        self.actionStack[self.stateStackTop] = self.action.size()
                        continue

                break

            elif act > self.ACCEPT_ACTION:

                if configuration_stack.findConfiguration(self.stateStack, self.stateStackTop, self.tokens.size()):
                    act = self.ERROR_ACTION
                else:
                    configuration_stack.push(self.stateStack, self.stateStackTop, act + 1, self.tokens.size(),
                                             self.action.size())
                    act = self.prs.baseAction(act)

                continue
            else:
                break  # assert(act == ACCEPT_ACTION):

            self.stateStackTop += 1
            self.stateStack[self.stateStackTop] = act  # no need to check if out of bounds

            self.locationStack[self.stateStackTop] = self.tokens.size()
            self.actionStack[self.stateStackTop] = self.action.size()
            act = self.tAction(act, current_kind)

        return

    def repairable(self, error_token: int) -> bool:
        #
        # Allocate configuration stack.
        #
        configuration_stack: ConfigurationStack = ConfigurationStack(self.prs)

        #
        # Keep parsing until we successfully reach the end of file or
        # an error is encountered. The list of actions executed will
        # be stored in the "action" tuple.
        #
        start_token: int = self.tokStream.peek()
        final_token: int = self.tokStream.getStreamLength()  # unreachable
        curtok: int = 0
        current_kind: int = self.ERROR_SYMBOL
        act: int = self.tAction(self.stateStack[self.stateStackTop], current_kind)

        while True:

            if act <= self.NUM_RULES:
                self.stateStackTop -= 1
                act = self.process_backtrack_reductions(act)

            elif act > self.ERROR_ACTION:

                curtok = self.tokStream.getToken()
                if curtok > final_token:
                    return True

                current_kind = self.tokStream.getKind(curtok)
                act = self.process_backtrack_reductions(act - self.ERROR_ACTION)

            elif act < self.ACCEPT_ACTION:

                curtok = self.tokStream.getToken()
                if curtok > final_token:
                    return True

                current_kind = self.tokStream.getKind(curtok)

            elif act == self.ERROR_ACTION:

                configuration = configuration_stack.pop()
                if configuration is None:
                    act = self.ERROR_ACTION
                else:
                    self.stateStackTop = configuration.stack_top
                    configuration.retrieveStack(self.stateStack)
                    act = configuration.act
                    curtok = configuration.curtok
                    if curtok == 0:
                        current_kind = self.ERROR_SYMBOL
                        self.tokStream.reset(start_token)
                    else:
                        current_kind = self.tokStream.getKind(curtok)
                        self.tokStream.reset(self.tokStream.getNext(curtok))

                    continue

                break

            elif act > self.ACCEPT_ACTION:

                if configuration_stack.findConfiguration(self.stateStack, self.stateStackTop, curtok):
                    act = self.ERROR_ACTION
                else:
                    configuration_stack.push(self.stateStack, self.stateStackTop, act + 1, curtok, 0)
                    act = self.prs.baseAction(act)

                continue
            else:
                break  # assert(act == ACCEPT_ACTION):

            #
            # We consider a configuration to be acceptable for recovery
            # if we are able to consume enough symbols in the remainining
            # tokens to reach another potential recovery point past the
            # original error token.
            #
            if (curtok > error_token) and (final_token == self.tokStream.getStreamLength()):
                #
                # If the ERROR_SYMBOL is a valid Action Adjunct in the state
                # "act" then we set the terminating token as the successor of
                # the current token. I.e., we have to be able to parse at least
                # two tokens past the resynch point before we claim victory.
                #
                if self.recoverableState(act):
                    final_token = curtok if self.skipTokens else self.tokStream.getNext(curtok)

            self.stateStackTop += 1
            if self.stateStackTop >= len(self.stateStack):
                self.reallocateStateStack()

            self.stateStack[self.stateStackTop] = act

            act = self.tAction(act, current_kind)

        #
        # If we can reach the end of the input successfully, we claim victory.
        #
        return act == self.ACCEPT_ACTION

    def recoverableState(self, state: int) -> bool:
        k: int = self.prs.asi(state)
        while self.prs.asr(k) != 0:
            if self.prs.asr(k) == self.ERROR_SYMBOL:
                return True
            k += 1

        return False

    def findRecoveryStateIndex(self, start_index: int) -> int:
        i: int
        i = start_index
        while i >= 0:
            #
            # If the ERROR_SYMBOL is an Action Adjunct in state stateStack[i]
            # then chose i as the index of the state to recover on.
            #
            if self.recoverableState(self.stateStack[i]):
                break
            i -= 1

        if i >= 0:  # if a recoverable state, remove None reductions, if any.
            k: int
            k = i - 1
            while k >= 0:
                if self.locationStack[k] != self.locationStack[i]:
                    break
                k -= 1

            i = k + 1

        return i

    def errorRepair(self, stream: IPrsStream, recovery_token: int, error_token: int) -> int:
        temp_stack: list = [0] * (self.stateStackTop + 1)
        arraycopy(self.stateStack, 0, temp_stack, 0, len(temp_stack))

        while stream.getKind(recovery_token) != self.EOFT_SYMBOL:

            stream.reset(recovery_token)
            if self.repairable(error_token):
                break

            self.stateStackTop = len(temp_stack) - 1
            arraycopy(temp_stack, 0, self.stateStack, 0, len(temp_stack))
            recovery_token = stream.getNext(recovery_token)

        if stream.getKind(recovery_token) == self.EOFT_SYMBOL:
            stream.reset(recovery_token)
            if not self.repairable(error_token):
                self.stateStackTop = len(temp_stack) - 1
                arraycopy(temp_stack, 0, self.stateStack, 0, len(temp_stack))
                return 0

        self.stateStackTop = len(temp_stack) - 1
        arraycopy(temp_stack, 0, self.stateStack, 0, len(temp_stack))
        stream.reset(recovery_token)
        self.tokens.reset(self.locationStack[self.stateStackTop] - 1)
        self.action.reset(self.actionStack[self.stateStackTop])

        return stream.makeErrorToken(self.tokens.get(self.locationStack[self.stateStackTop] - 1),
                                     stream.getPrevious(recovery_token),
                                     error_token,
                                     self.ERROR_SYMBOL)

    #
    # keep looking ahead until we compute a valid action
    #
    def lookahead(self, act: int, token: int) -> int:
        act = self.prs.lookAhead(act - self.LA_STATE_OFFSET, self.tokStream.getKind(token))
        return self.lookahead(act, self.tokStream.getNext(token)) if act > self.LA_STATE_OFFSET else act

    #
    # Compute the next action defined on act and sym. If self
    # action requires more lookahead, these lookahead symbols
    # are in the token stream beginning at the next token that
    # is yielded by peek().
    #
    def tAction(self, act: int, sym: int):
        act = self.prs.tAction(act, sym)
        return self.lookahead(act, self.tokStream.peek()) if act > self.LA_STATE_OFFSET else act
