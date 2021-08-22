#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lpg2.ParseTable import ParseTable
from lpg2.RuleAction import RuleAction
from lpg2.IntTuple import IntTuple
from lpg2.Monitor import Monitor

from lpg2.IPrsStream import ILexStream
from lpg2.UnavailableParserInformationException import UnavailableParserInformationException
from lpg2.Utils import arraycopy


class LexParser(object):
    __slots__ = ('taking_actions', 'tokStream', 'prs', 'ra', 'START_STATE', 'LA_STATE_OFFSET', 'EOFT_SYMBOL',
                 'ACCEPT_ACTION', 'ERROR_ACTION', 'START_SYMBOL', 'NUM_RULES', 'action', 'stateStackTop',
                 'stackLength', 'stack', 'locationStack', 'tempStack', 'lastToken', 'currentAction', 'curtok',
                 'starttok', 'current_kind'
                 )

    def reset(self, tokStream: ILexStream, prs: ParseTable, ra: RuleAction):
        self.tokStream = tokStream
        self.prs = prs
        self.ra = ra
        self.START_STATE = prs.getStartState()
        self.LA_STATE_OFFSET = prs.getLaStateOffset()
        self.EOFT_SYMBOL = prs.getEoftSymbol()
        self.ACCEPT_ACTION = prs.getAcceptAction()
        self.ERROR_ACTION = prs.getErrorAction()
        self.START_SYMBOL = prs.getStartSymbol()
        self.NUM_RULES = prs.getNumRules()

    def __init__(self, tokStream: ILexStream = None, prs: ParseTable = None, ra: RuleAction = None):
        self.taking_actions: bool = False

        self.START_STATE: int = 0
        self.LA_STATE_OFFSET: int = 0
        self.EOFT_SYMBOL: int = 0
        self.ACCEPT_ACTION: int = 0
        self.ERROR_ACTION: int = 0
        self.START_SYMBOL: int = 0
        self.NUM_RULES: int = 0

        self.tokStream: ILexStream = None
        self.prs: ParseTable = None
        self.ra: RuleAction = None
        self.action: IntTuple = IntTuple(0)

        self.stateStackTop: int = 0
        self.stackLength: int = 0
        self.stack: list = []
        self.locationStack: list = []
        self.tempStack: list = []

        self.lastToken: int = 0
        self.currentAction: int = 0
        self.curtok: int = 0
        self.starttok: int = 0
        self.current_kind: int = 0
        if tokStream and prs and ra:
            self.reset(tokStream, prs, ra)

    #
    # Stacks portion
    #
    STACK_INCREMENT: int = 1024

    def reallocateStacks(self):
        old_stack_length: int = (0 if self.stack.__len__() == 0 else self.stackLength)
        self.stackLength += self.STACK_INCREMENT
        if old_stack_length == 0:
            self.stack = [0] * self.stackLength
            self.locationStack = [0] * self.stackLength
            self.tempStack = [0] * self.stackLength
        else:
            self.stack = arraycopy(self.stack, 0, [0] * self.stackLength, 0, old_stack_length)
            self.locationStack = arraycopy(self.locationStack, 0, [0] * self.stackLength, 0, old_stack_length)
            self.tempStack = arraycopy(self.tempStack, 0, [0] * self.stackLength, 0, old_stack_length)

        return

    #
    # The following functions can be invoked only when the parser is
    # processing actions. Thus, they can be invoked when the parser
    # was entered via the main entry point (parseCharacters():). When using
    # the incremental parser (via the entry point scanNextToken(int [], int)):,
    # they always return 0 when invoked. # TODO: Should we raise an Exception instead?
    # However, note that when parseActions(): is invoked after successfully
    # parsing an input with the incremental parser, then they can be invoked.
    #
    def getFirstToken(self, i: int = None) -> int:
        if i is None:
            return self.starttok

        return self.getToken(i)

    def getLastToken(self, i: int = None) -> int:
        if i is None:
            return self.lastToken

        if self.taking_actions:
            return (self.lastToken if i >= self.prs.rhs(self.currentAction) else self.tokStream.getPrevious(
                self.getToken(i + 1)))

        raise UnavailableParserInformationException()

    def getCurrentRule(self) -> int:
        if self.taking_actions:
            return self.currentAction

        raise UnavailableParserInformationException()

    #
    # Given a rule of the form     A ::= x1 x2 ... xn     n > 0
    #
    # the function getToken(i): yields the symbol xi, if xi is a terminal
    # or ti, if xi is a nonterminal that produced a str of the form
    # xi => ti w. If xi is a nullable nonterminal, then ti is the first
    #  symbol that immediately follows xi in the input (the lookahead).
    #
    def getToken(self, i: int) -> int:
        if self.taking_actions:
            return self.locationStack[self.stateStackTop + (i - 1)]

        raise UnavailableParserInformationException()

    def setSym1(self, i: int):
        pass

    def getSym(self, i: int) -> int:
        return self.getLastToken(i)

    def resetTokenStream(self, i: int):
        #
        # if i exceeds the upper bound, reset it to point to the last element.
        #
        self.tokStream.reset(self.tokStream.getStreamLength() if i > self.tokStream.getStreamLength() else i)
        self.curtok = self.tokStream.getToken()
        self.current_kind = self.tokStream.getKind(self.curtok)
        if not self.stack or self.stack.__len__() == 0:
            self.reallocateStacks()

        if self.action.capacity() == 0:
            self.action = IntTuple(1 << 10)

    #
    # Parse the input and create a stream of tokens.
    #
    def parseCharacters(self, start_offset: int, end_offset: int, monitor: Monitor):
        self.resetTokenStream(start_offset)
        while self.curtok <= end_offset:
            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if monitor and monitor.isCancelled():
                return

            self.lexNextToken(end_offset)

    #
    # Parse the input and create a stream of tokens.
    #
    def parseCharactersWhitMonitor(self, monitor: Monitor = None):
        #
        # Indicate that we are running the regular parser and that it's
        # ok to use the utility functions to query the parser.
        #
        self.taking_actions = True

        self.resetTokenStream(0)
        self.lastToken = self.tokStream.getPrevious(self.curtok)
        #
        # Until it reaches the end-of-file token, self outer loop
        # resets the parser and processes the next token.
        #

        # ProcessTokens:
        while self.current_kind != self.EOFT_SYMBOL:
            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if monitor is not None and monitor.isCancelled():
                break  # ProcessTokens

            self.stateStackTop = -1
            self.currentAction = self.START_STATE
            self.starttok = self.curtok
            b_continue_process_tokens: bool = False
            # ScanToken:
            while True:

                self.stateStackTop += 1
                if self.stateStackTop >= self.stack.__len__():
                    self.reallocateStacks()
                self.stack[self.stateStackTop] = self.currentAction

                self.locationStack[self.stateStackTop] = self.curtok

                #
                # Compute the action on the next character. If it is a reduce action, we do not
                # want to accept it until we are sure that the character in question is can be parsed.
                # What we are trying to avoid is a situation where Curtok is not the EOF token
                # but it yields a default reduce action in the current configuration even though
                # it cannot ultimately be shifted However, the state on top of the configuration also
                # contains a valid reduce action on EOF which, if taken, would lead to the successful
                # scanning of the token.
                #
                # Thus, if the character can be parsed, we proceed normally. Otherwise, we proceed
                # as if we had reached the end of the file (end of the token, since we are really
                # scanning).
                #
                if self.curtok == 275:
                    self.curtok = 275
                self.parseNextCharacter(self.curtok, self.current_kind)
                if self.curtok == 275:
                    self.curtok = 275

                if (self.currentAction == self.ERROR_ACTION and
                        self.current_kind != self.EOFT_SYMBOL):  # if not successful try EOF

                    save_next_token = self.tokStream.peek()  # save position after curtok
                    self.tokStream.reset(self.tokStream.getStreamLength() - 1)  # point to the end of the input
                    self.parseNextCharacter(self.curtok, self.EOFT_SYMBOL)
                    # assert (currentAction == ACCEPT_ACTION or currentAction == ERROR_ACTION):
                    self.tokStream.reset(save_next_token)  # reset the stream for the next token after curtok.

                #
                # At self point, currentAction is either a Shift, Shift-Reduce, Accept or Error action.
                #
                if self.currentAction > self.ERROR_ACTION:  # Shift-reduce

                    self.lastToken = self.curtok
                    self.curtok = self.tokStream.getToken()
                    self.current_kind = self.tokStream.getKind(self.curtok)
                    self.currentAction -= self.ERROR_ACTION
                    while True:
                        self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
                        self.ra.ruleAction(self.currentAction)
                        lhs_symbol = self.prs.lhs(self.currentAction)
                        if lhs_symbol == self.START_SYMBOL:
                            b_continue_process_tokens = True
                            break
                        self.currentAction = self.prs.ntAction(self.stack[self.stateStackTop], lhs_symbol)
                        if not self.currentAction <= self.NUM_RULES:
                            break
                    if b_continue_process_tokens:
                        break
                elif self.currentAction < self.ACCEPT_ACTION:  # Shift

                    self.lastToken = self.curtok
                    self.curtok = self.tokStream.getToken()
                    self.current_kind = self.tokStream.getKind(self.curtok)

                elif self.currentAction == self.ACCEPT_ACTION:
                    b_continue_process_tokens = True
                    break
                else:
                    break  # ScanToken ERROR_ACTION

            if b_continue_process_tokens:
                continue
            #
            # Whenever we reach self point, an error has been detected.
            # Note that the parser loop above can never reach the ACCEPT
            # point as it is short-circuited each time it reduces a phrase
            # to the START_SYMBOL.
            #
            # If an error is detected on a single bad character,
            # we advance to the next character before resuming the
            # scan. However, if an error is detected after we start
            # scanning a construct, we form a bad token out of the
            # characters that have already been scanned and resume
            # scanning on the character on which the problem was
            # detected. In other words, in that case, we do not advance.
            #
            if self.starttok == self.curtok:
                if self.current_kind == self.EOFT_SYMBOL:
                    break  # ProcessTokens
                self.tokStream.reportLexicalError(self.starttok, self.curtok)
                self.lastToken = self.curtok
                self.curtok = self.tokStream.getToken()
                self.current_kind = self.tokStream.getKind(self.curtok)

            else:
                self.tokStream.reportLexicalError(self.starttok, self.lastToken)

        self.taking_actions = False  # indicate that we are done

        return

    #
    # This function takes as argument a configuration ([stack, stackTop], [tokStream, curtok]):
    # and determines whether or not curtok can be validly parsed in self configuration. If so,
    # it parses curtok and returns the final shift or shift-reduce action on it. Otherwise, it
    # leaves the configuration unchanged and returns ERROR_ACTION.
    #
    def parseNextCharacter(self, token: int, kind: int):
        start_action: int = self.stack[self.stateStackTop]
        pos: int = self.stateStackTop
        tempStackTop: int = self.stateStackTop - 1

        self.currentAction = self.tAction(start_action, kind)

        b_break_scan: bool = False
        # Scan:
        while self.currentAction <= self.NUM_RULES:
            while True:
                lhs_symbol = self.prs.lhs(self.currentAction)
                if lhs_symbol == self.START_SYMBOL:
                    b_break_scan = True
                    break

                tempStackTop -= (self.prs.rhs(self.currentAction) - 1)

                state = (self.tempStack[tempStackTop] if tempStackTop > pos else self.stack[tempStackTop])

                self.currentAction = self.prs.ntAction(state, lhs_symbol)
                if not self.currentAction <= self.NUM_RULES:
                    break

            if b_break_scan:
                break

            if tempStackTop + 1 >= self.stack.__len__():
                self.reallocateStacks()
            #
            # ... Update the maximum useful position of the stack,
            # push goto state into (temporary): stack, and compute
            # the next action on the current symbol ...
            #
            pos = pos if pos < tempStackTop else tempStackTop
            self.tempStack[tempStackTop + 1] = self.currentAction

            self.currentAction = self.tAction(self.currentAction, kind)
        #
        # If no error was detected, we update the configuration up to the point prior to the
        # shift or shift-reduce on the token by processing all reduce and goto actions associated
        # with the current token.
        #
        if self.currentAction != self.ERROR_ACTION:
            #
            # Note that it is important that the global variable currentAction be used here when
            # we are actually processing the rules. The reason being that the user-defined function
            # ra.ruleAction(): may call def functions defined in self class (such as getLastToken()):
            # which require that currentAction be properly initialized.
            #

            self.currentAction = self.tAction(start_action, kind)
            # Replay:
            bBreakReplay: bool = False
            while self.currentAction <= self.NUM_RULES:
                self.stateStackTop -= 1
                while True:
                    self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
                    self.ra.ruleAction(self.currentAction)
                    lhs_symbol = self.prs.lhs(self.currentAction)
                    if lhs_symbol == self.START_SYMBOL:
                        self.currentAction = (self.ERROR_ACTION
                                              if self.starttok == token  # None str reduction to START_SYMBOL is illegal
                                              else self.ACCEPT_ACTION)
                        bBreakReplay = True
                        break  # Replay

                    self.currentAction = self.prs.ntAction(self.stack[self.stateStackTop], lhs_symbol)
                    if not self.currentAction <= self.NUM_RULES:
                        break
                if bBreakReplay:
                    break

                self.stateStackTop += 1
                if self.stateStackTop >= self.stack.__len__():
                    self.reallocateStacks()
                self.stack[self.stateStackTop] = self.currentAction

                self.locationStack[self.stateStackTop] = token

                self.currentAction = self.tAction(self.currentAction, kind)

        return

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
    def tAction(self, act: int, sym: int) -> int:
        act = self.prs.tAction(act, sym)
        return self.lookahead(act, self.tokStream.peek()) if act > self.LA_STATE_OFFSET else act

    def scanNextToken2(self) -> bool:
        return self.lexNextToken(self.tokStream.getStreamLength())

    def scanNextToken(self, start_offset: int = None) -> bool:
        if start_offset is None:
            return self.scanNextToken2()

        self.resetTokenStream(start_offset)
        return self.lexNextToken(self.tokStream.getStreamLength())

    def lexNextToken(self, end_offset: int) -> bool:
        #
        # Indicate that we are going to run the incremental parser and that
        # it's forbidden to use the utility functions to query the parser.
        #
        self.taking_actions = False

        self.stateStackTop = -1
        self.currentAction = self.START_STATE
        self.starttok = self.curtok
        self.action.reset()

        # ScanToken:
        while True:

            self.stateStackTop += 1
            if self.stateStackTop >= self.stack.__len__():
                self.reallocateStacks()
            self.stack[self.stateStackTop] = self.currentAction

            #
            # Compute the the action on the next character. If it is a reduce action, we do not
            # want to accept it until we are sure that the character in question is parsable.
            # What we are trying to avoid is a situation where self.curtok is not the EOF token
            # but it yields a default reduce self.action in the current configuration even though
            # it cannot ultimately be shifted However, the state on top of the configuration also
            # contains a valid reduce self.action on EOF which, if taken, would lead to the succesful
            # scanning of the token.
            #
            # Thus, if the character is parsable, we proceed normally. Otherwise, we proceed
            # as if we had reached the end of the file (end of the token, since we are really
            # scanning).
            #
            self.currentAction = self.lexNextCharacter(self.currentAction, self.current_kind)
            if (self.currentAction == self.ERROR_ACTION and
                    self.current_kind != self.EOFT_SYMBOL):  # if not successful try EOF

                save_next_token = self.tokStream.peek()  # save position after self.curtok
                self.tokStream.reset(self.tokStream.getStreamLength() - 1)  # point to the end of the input
                self.currentAction = self.lexNextCharacter(self.stack[self.stateStackTop], self.EOFT_SYMBOL)
                # assert (self.currentAction == self.ACCEPT_ACTION or self.currentAction == self.ERROR_ACTION):
                self.tokStream.reset(save_next_token)  # reset the stream for the next token after self.curtok.

            self.action.add(self.currentAction)  # save the self.action

            #
            # At self point, self.currentAction is either a Shift, Shift-Reduce, Accept or Error self.action.
            #
            if self.currentAction > self.ERROR_ACTION:  # Shift-reduce

                self.curtok = self.tokStream.getToken()
                if self.curtok > end_offset:
                    self.curtok = self.tokStream.getStreamLength()
                self.current_kind = self.tokStream.getKind(self.curtok)
                self.currentAction -= self.ERROR_ACTION
                while True:
                    lhs_symbol = self.prs.lhs(self.currentAction)
                    if lhs_symbol == self.START_SYMBOL:
                        self.parseActions()
                        return True

                    self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
                    self.currentAction = self.prs.ntAction(self.stack[self.stateStackTop], lhs_symbol)
                    if not self.currentAction <= self.NUM_RULES:
                        break

            elif self.currentAction < self.ACCEPT_ACTION:  # Shift

                self.curtok = self.tokStream.getToken()
                if self.curtok > end_offset:
                    self.curtok = self.tokStream.getStreamLength()
                self.current_kind = self.tokStream.getKind(self.curtok)

            elif self.currentAction == self.ACCEPT_ACTION:
                return True
            else:
                break  # ScanToken # self.ERROR_ACTION

        #
        # Whenever we reach self point, an error has been detected.
        # Note that the parser loop above can never reach the ACCEPT
        # point as it is short-circuited each time it reduces a phrase
        # to the self.START_SYMBOL.
        #
        # If an error is detected on a single bad character,
        # we advance to the next character before resuming the
        # scan. However, if an error is detected after we start
        # scanning a construct, we form a bad token out of the
        # characters that have already been scanned and resume
        # scanning on the character on which the problem was
        # detected. In other words, in that case, we do not advance.
        #
        if self.starttok == self.curtok:
            if self.current_kind == self.EOFT_SYMBOL:
                self.action = IntTuple(0)  # turn into garbage!
                return False

            self.lastToken = self.curtok
            self.tokStream.reportLexicalError(self.starttok, self.curtok)
            self.curtok = self.tokStream.getToken()
            if self.curtok > end_offset:
                self.curtok = self.tokStream.getStreamLength()
            self.current_kind = self.tokStream.getKind(self.curtok)

        else:
            self.lastToken = self.tokStream.getPrevious(self.curtok)
            self.tokStream.reportLexicalError(self.starttok, self.lastToken)

        return True

    #
    # This function takes as argument a configuration ([self.stack, stackTop], [self.tokStream, self.curtok]):
    # and determines whether or not the reduce self.action the self.curtok can be validly parsed in self
    # configuration.
    #
    def lexNextCharacter(self, act: int, kind: int):
        action_save = self.action.size()
        pos = self.stateStackTop,
        tempStackTop = self.stateStackTop - 1
        act = self.tAction(act, kind)
        # Scan:
        b_break_scan = False
        while act <= self.NUM_RULES:
            self.action.add(act)

            while True:
                lhs_symbol = self.prs.lhs(act)
                if lhs_symbol == self.START_SYMBOL:
                    if self.starttok == self.curtok:  # None str reduction to self.START_SYMBOL is illegal

                        act = self.ERROR_ACTION
                        b_break_scan = True
                        break  # Scan

                    else:
                        self.parseActions()
                        return self.ACCEPT_ACTION

                tempStackTop -= (self.prs.rhs(act) - 1)
                state = (self.tempStack[tempStackTop] if tempStackTop > pos else self.stack[tempStackTop])
                act = self.prs.ntAction(state, lhs_symbol)

                if not act <= self.NUM_RULES:
                    break
            if b_break_scan:
                break

            if tempStackTop + 1 >= self.stack.__len__():
                self.reallocateStacks()
            #
            # ... Update the maximum useful position of the self.stack,
            # push goto state into (temporary): self.stack, and compute
            # the next self.action on the current symbol ...
            #
            pos = pos if pos < tempStackTop else tempStackTop
            self.tempStack[tempStackTop + 1] = act
            act = self.tAction(act, kind)

        #
        # If an error was detected, we restore the original configuration.
        # Otherwise, we update configuration up to the point prior to the
        # shift or shift-reduce on the token.
        #
        if act == self.ERROR_ACTION:
            self.action.reset(action_save)
        else:
            self.stateStackTop = tempStackTop + 1
            for i in range(pos + 1, self.stateStackTop + 1):  # update stack
                self.stack[i] = self.tempStack[i]

        return act

    #
    # Now do the final parse of the input based on the actions in
    # the list "self.action" and the sequence of tokens in the token stream.
    #
    def parseActions(self):
        #
        # Indicate that we are running the regular parser and that it's
        # ok to use the utility functions to query the parser.
        #
        self.taking_actions = True

        self.curtok = self.starttok
        self.lastToken = self.tokStream.getPrevious(self.curtok)

        #
        # Reparse the input...
        #
        self.stateStackTop = -1
        self.currentAction = self.START_STATE
        # process_actions:
        b_break_process_actions = False
        for i in range(0, self.action.size()):
            self.stateStackTop += 1
            self.stack[self.stateStackTop] = self.currentAction
            self.locationStack[self.stateStackTop] = self.curtok

            self.currentAction = self.action.get(i)
            if self.currentAction <= self.NUM_RULES:  # a reduce self.action?

                self.stateStackTop -= 1  # turn reduction into shift-reduction
                while True:
                    self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
                    self.ra.ruleAction(self.currentAction)
                    lhs_symbol = self.prs.lhs(self.currentAction)
                    if lhs_symbol == self.START_SYMBOL:
                        # assert(starttok != self.curtok):  # None str reduction to self.START_SYMBOL is illegal
                        b_break_process_actions = True
                        break  # process_actions

                    self.currentAction = self.prs.ntAction(self.stack[self.stateStackTop], lhs_symbol)
                    if not self.currentAction <= self.NUM_RULES:
                        break
            else:  # a shift or shift-reduce self.action

                self.lastToken = self.curtok
                self.curtok = self.tokStream.getNext(self.curtok)
                if self.currentAction > self.ERROR_ACTION:  # a shift-reduce self.action?

                    self.current_kind = self.tokStream.getKind(self.curtok)
                    self.currentAction -= self.ERROR_ACTION
                    while True:
                        self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
                        self.ra.ruleAction(self.currentAction)
                        lhs_symbol = self.prs.lhs(self.currentAction)
                        if lhs_symbol == self.START_SYMBOL:
                            b_break_process_actions = True
                            break  # process_actions
                        self.currentAction = self.prs.ntAction(self.stack[self.stateStackTop], lhs_symbol)
                        if not self.currentAction <= self.NUM_RULES:
                            break

            if b_break_process_actions:
                break

        self.taking_actions = False  # indicate that we are done

        return
