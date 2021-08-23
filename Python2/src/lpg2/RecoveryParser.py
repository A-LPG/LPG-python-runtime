#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from lpg2.BadParseException import BadParseException
from lpg2.ConfigurationStack import ConfigurationStack
from lpg2.DiagnoseParser import DiagnoseParser, PrimaryRepairInfo

from lpg2.IntTuple import IntTuple

from lpg2.ParseErrorCodes import ParseErrorCodes

from lpg2.Utils import arraycopy


class RecoveryParser(DiagnoseParser):
    __slots__ = ('parser', 'action', 'tokens', 'actionStack', 'scope_repair')

    #
    # maxErrors is the maximum int of errors to be repaired
    # maxTime is the maximum amount of time allowed for diagnosing
    # but at least one error must be diagnosed 
    #
    def __init__(self, parser, action, tokens, tokStream, prs, maxErrors=0, maxTime=0, monitor=None):
        super(RecoveryParser, self).__init__(tokStream, prs, maxErrors, maxTime, monitor)
        self.parser = parser
        self.action = action
        self.tokens = tokens
        self.actionStack = []
        self.scope_repair = PrimaryRepairInfo()

    def reallocateStacks(self):
        super(RecoveryParser, self).reallocateStacks()
        if self.actionStack is None or self.actionStack.__len__() == 0:
            self.actionStack = [0] * (len(self.stateStack))
        else:
            old_stack_length = self.actionStack.__len__()
            self.actionStack = arraycopy(self.actionStack, 0, [0] * (len(self.stateStack)), 0, old_stack_length)

        return

    def reportError(self, scope_index, error_token):
        text = "\""

        i = self.scopeSuffix(scope_index)
        while self.scopeRhs(i) != 0:
            if not self.isNullable(self.scopeRhs(i)):
                symbol_index = (self.nonterminalIndex(self.scopeRhs(i) - self.NT_OFFSET)
                                if self.scopeRhs(i) > self.NT_OFFSET
                                else self.terminalIndex(self.scopeRhs(i)))
                if self.name(symbol_index).__len__() > 0:
                    if text.__len__() > 1:  # Not just starting quote?
                        text += " "  # add a space separator

                    text += self.name(symbol_index)
            i += 1

        text += "\""
        self.tokStream.reportError(ParseErrorCodes.SCOPE_CODE, error_token, error_token, [text])
        return

    def recover(self, marker_token, error_token):
        if not self.stateStack or len(self.stateStack) == 0:
            self.reallocateStacks()

        self.tokens.reset()
        self.tokStream.reset()
        self.tokens.add(self.tokStream.getPrevious(self.tokStream.peek()))
        restart_token = (marker_token if marker_token != 0 else self.tokStream.getToken())
        old_action_size = 0
        self.stateStackTop = 0
        self.stateStack[self.stateStackTop] = self.START_STATE
        while True:
            self.action.reset(old_action_size)
            if not self.fixError(restart_token, error_token):
                raise BadParseException(error_token)

            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if self.monitor and self.monitor.isCancelled():
                break

            #
            # At self stage, we have a recovery configuration. See how
            # far we can go with it.
            #
            restart_token = error_token
            self.tokStream.reset(error_token)
            old_action_size = self.action.size()  # save the old size in case we encounter a  error
            error_token = self.parser.backtrackParse(self.stateStack, self.stateStackTop, self.action, 0)
            self.tokStream.reset(self.tokStream.getNext(restart_token))
            if not error_token != 0:  # no error found
                break
        return restart_token

    #
    # Given the configuration consisting of the states in stateStack
    # and the sequence of tokens (current_kind, followed by the tokens
    # in tokStream):, fixError parses up to error_token in the tokStream
    # recovers, if possible, from that error and returns the result.
    # While doing self, it also computes the location_stack information
    # and the sequence of actions that matches up with the result that
    # it returns.
    #
    def fixError(self, start_token, error_token):
        #
        # Save information about the current configuration.
        #
        curtok = start_token
        current_kind = self.tokStream.getKind(curtok)
        first_stream_token = self.tokStream.peek()

        self.buffer[1] = error_token
        self.buffer[0] = self.tokStream.getPrevious(self.buffer[1])
        for k in range(2, self.BUFF_SIZE):
            self.buffer[k] = self.tokStream.getNext(self.buffer[k - 1])

        self.scope_repair.distance = 0
        self.scope_repair.misspellIndex = 0
        self.scope_repair.bufferPosition = 1

        #
        # Clear the configuration stack.
        #
        self.main_configuration_stack = ConfigurationStack(self.prs)

        #
        # Keep parsing until we reach the end of file and succeed or
        # an error is encountered. The list of actions executed will
        # be stored in the "action" tuple.
        #
        self.locationStack[self.stateStackTop] = curtok
        self.actionStack[self.stateStackTop] = self.action.size()
        act = self.tAction(self.stateStack[self.stateStackTop], current_kind)
        while True:
            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if self.monitor and self.monitor.isCancelled():
                return True

            if act <= self.NUM_RULES:
                self.action.add(act)  # save this reduce action
                self.stateStackTop -= 1

                while True:
                    self.stateStackTop -= (self.rhs(act) - 1)
                    act = self.ntAction(self.stateStack[self.stateStackTop], self.lhs(act))
                    if not act <= self.NUM_RULES:
                        break

                self.stateStackTop += 1
                if self.stateStackTop >= len(self.stateStack):
                    self.reallocateStacks()
                self.stateStack[self.stateStackTop] = act

                self.locationStack[self.stateStackTop] = curtok
                self.actionStack[self.stateStackTop] = self.action.size()
                act = self.tAction(act, current_kind)
                continue

            elif act == self.ERROR_ACTION:

                if curtok != error_token or self.main_configuration_stack.size() > 0:
                    configuration = self.main_configuration_stack.pop()
                    if configuration is None:
                        act = self.ERROR_ACTION
                    else:
                        self.stateStackTop = configuration.stack_top
                        configuration.retrieveStack(self.stateStack)
                        act = configuration.act
                        curtok = configuration.curtok
                        self.action.reset(configuration.action_length)
                        current_kind = self.tokStream.getKind(curtok)
                        self.tokStream.reset(self.tokStream.getNext(curtok))
                        continue

                break

            elif act > self.ACCEPT_ACTION and act < self.ERROR_ACTION:

                if self.main_configuration_stack.findConfiguration(self.stateStack, self.stateStackTop, curtok):
                    act = self.ERROR_ACTION
                else:
                    self.main_configuration_stack.push(self.stateStack, self.stateStackTop, act + 1, curtok,
                                                       self.action.size())
                    act = self.baseAction(act)

                continue

            else:

                if act < self.ACCEPT_ACTION:

                    self.action.add(act)  # save self shift action
                    curtok = self.tokStream.getToken()
                    current_kind = self.tokStream.getKind(curtok)

                elif act > self.ERROR_ACTION:

                    self.action.add(act)  # save self shift-reduce action
                    curtok = self.tokStream.getToken()
                    current_kind = self.tokStream.getKind(curtok)
                    act -= self.ERROR_ACTION
                    while True:
                        self.stateStackTop -= (self.rhs(act) - 1)
                        act = self.ntAction(self.stateStack[self.stateStackTop], self.lhs(act))
                        if not act <= self.NUM_RULES:
                            break

                else:
                    break  # assert(act == ACCEPT_ACTION):  THIS IS NOT SUPPOSED TO HAPPEN!!!

                self.stateStackTop += 1
                if self.stateStackTop >= len(self.stateStack):
                    self.reallocateStacks()
                self.stateStack[self.stateStackTop] = act

                if curtok == error_token:
                    self.scopeTrial(self.scope_repair, self.stateStack, self.stateStackTop)
                    if self.scope_repair.distance >= self.MIN_DISTANCE:

                        self.tokens.add(start_token)
                        token = first_stream_token
                        while token != error_token:
                            self.tokens.add(token)
                            token = self.tokStream.getNext(token)

                        self.acceptRecovery(error_token)
                        break  # equivalent to: return true;

                self.locationStack[self.stateStackTop] = curtok
                self.actionStack[self.stateStackTop] = self.action.size()
                act = self.tAction(act, current_kind)

        return act != self.ERROR_ACTION

    def acceptRecovery(self, error_token):
        #
        #
        #
        # int action_size = action.size():

        #
        # Simulate parsing actions required for self sequence of scope
        # recoveries.
        # TODO: need to add action and fix the location_stack?
        #
        recovery_action = IntTuple()
        for k in range(0, self.scopeStackTop + 1):
            scope_index = self.scopeIndex[k]
            la = self.scopeLa(scope_index)

            #
            # Compute the action (or set of actions in case of conflicts): that
            # can be executed on the scope lookahead symbol. Save the action(s):
            # in the action tuple.
            #
            recovery_action.reset()
            act = self.tAction(self.stateStack[self.stateStackTop], la)
            if act > self.ACCEPT_ACTION and act < self.ERROR_ACTION:  # conflicting actions?
                while True:

                    recovery_action.add(self.baseAction(act))
                    act += 1

                    if not self.baseAction(act) != 0:
                        break
            else:
                recovery_action.add(act)

            #
            # For each action defined on the scope lookahead symbol,
            # try scope recovery. At least one action should succeed!
            #
            start_action_size = self.action.size()
            index = 0
            for index in range(0, recovery_action.size()):

                #
                # Reset the action tuple each time through self loop
                # to clear previous actions that may have been added
                # because of a failed call to completeScope.
                #
                self.action.reset(start_action_size)
                self.tokStream.reset(error_token)
                self.tempStackTop = self.stateStackTop - 1
                max_pos = self.stateStackTop

                act = recovery_action.get(index)
                while act <= self.NUM_RULES:
                    self.action.add(act)  # save self reduce action
                    #
                    # ... Process all goto-reduce actions following
                    # reduction, until a goto action is computed ...
                    #
                    while True:
                        lhs_symbol = self.lhs(act)
                        self.tempStackTop -= (self.rhs(act) - 1)
                        act = (self.tempStack[self.tempStackTop]
                               if self.tempStackTop > max_pos else self.stateStack[self.tempStackTop])
                        act = self.ntAction(act, lhs_symbol)
                        if not act <= self.NUM_RULES:
                            break
                    if self.tempStackTop + 1 >= len(self.stateStack):
                        self.reallocateStacks()

                    max_pos = max_pos if max_pos < self.tempStackTop else self.tempStackTop
                    self.tempStack[self.tempStackTop + 1] = act
                    act = self.tAction(act, la)

                #
                # If the lookahead symbol is parsable, then we check
                # whether or not we have a match between the scope
                # prefix and the transition symbols corresponding to
                # the states on top of the stack.
                #
                if act != self.ERROR_ACTION:
                    self.tempStackTop += 1
                    self.nextStackTop = self.tempStackTop

                    for i in range(0, max_pos + 1):
                        self.nextStack[i] = self.stateStack[i]

                    #
                    # NOTE that we do not need to update location_stack and
                    # actionStack here because, once the rules associated with
                    # these scopes are reduced, all these states will be popped
                    # from the stack.
                    #
                    for i in range(max_pos + 1, self.tempStackTop + 1):
                        self.nextStack[i] = self.tempStack[i]

                    if self.completeScope(self.action, self.scopeSuffix(scope_index)):
                        i = self.scopeSuffix(self.scopeIndex[k])
                        while self.scopeRhs(i) != 0:
                            self.tokens.add(self.tokStream.makeErrorToken
                                            (error_token,
                                             self.tokStream.getPrevious(error_token),
                                             error_token, self.scopeRhs(i)))
                            i += 1

                        self.reportError(self.scopeIndex[k], self.tokStream.getPrevious(error_token))
                        break

            # assert (index < recovery_action.size()): # sanity check!
            self.stateStackTop = self.nextStackTop
            arraycopy(self.nextStack, 0, self.stateStack, 0, self.stateStackTop + 1)

        return

    def completeScope(self, action, scope_rhs_index):
        kind = self.scopeRhs(scope_rhs_index)
        if kind == 0:
            return True

        act = self.nextStack[self.nextStackTop]

        if kind > self.NT_OFFSET:
            lhs_symbol = kind - self.NT_OFFSET
            if self.baseCheck(act + lhs_symbol) != lhs_symbol:
                # is there a valid
                # action defined on
                # lhs_symbol?
                return False

            act = self.ntAction(act, lhs_symbol)

            #
            # if action is a goto-reduce action, save it as a shift-reduce
            # action.
            #
            action.add(act + self.ERROR_ACTION if act <= self.NUM_RULES else act)
            while act <= self.NUM_RULES:
                self.nextStackTop -= (self.rhs(act) - 1)
                act = self.ntAction(self.nextStack[self.nextStackTop], self.lhs(act))

            self.nextStackTop += 1
            self.nextStack[self.nextStackTop] = act
            return self.completeScope(action, scope_rhs_index + 1)

        #
        # Processing a terminal
        #
        act = self.tAction(act, kind)
        action.add(act)  # save self terminal action
        if act < self.ACCEPT_ACTION:
            self.nextStackTop += 1
            self.nextStack[self.nextStackTop] = act
            return self.completeScope(action, scope_rhs_index + 1)

        elif act > self.ERROR_ACTION:
            act -= self.ERROR_ACTION
            while True:
                self.nextStackTop -= (self.rhs(act) - 1)
                act = self.ntAction(self.nextStack[self.nextStackTop], self.lhs(act))
                if not act <= self.NUM_RULES:
                    break

            self.nextStackTop += 1
            self.nextStack[self.nextStackTop] = act
            return True

        elif act > self.ACCEPT_ACTION and act < self.ERROR_ACTION:  # conflicting actions?

            save_action_size = action.size()
            i = act
            while self.baseAction(i) != 0:  # consider only shift and shift-reduce actions

                action.reset(save_action_size)
                act = self.baseAction(i)
                action.add(act)  # save self terminal action
                if act <= self.NUM_RULES:  # Ignore reduce actions
                    pass
                elif act < self.ACCEPT_ACTION:

                    self.nextStackTop += 1
                    self.nextStack[self.nextStackTop] = act
                    if self.completeScope(action, scope_rhs_index + 1):
                        return True

                elif act > self.ERROR_ACTION:

                    act -= self.ERROR_ACTION
                    while True:
                        self.nextStackTop -= (self.rhs(act) - 1)
                        act = self.ntAction(self.nextStack[self.nextStackTop], self.lhs(act))
                        if not act <= self.NUM_RULES:
                            break
                    self.nextStackTop += 1
                    self.nextStack[self.nextStackTop] = act
                    return True
                i += 1

        return False
