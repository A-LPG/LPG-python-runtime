from IntSegmentedTuple import IntSegmentedTuple
from Stacks  import  Stacks  
from Monitor import  Monitor 
from IntTuple import  IntTuple  
from TokenStream import  TokenStream  
from ParseTable import  ParseTable  
from RuleAction import  RuleAction  
from BadParseException import  BadParseException  
from UnavailableParserInformationException import  UnavailableParserInformationException  
from BadParseSymFileException import  BadParseSymFileException  
from NotDeterministicParseTableException import  NotDeterministicParseTableException  

class DeterministicParser(Stacks): 
    def __init__(self,tokStream: TokenStream = None , prs: ParseTable = None, ra: RuleAction = None, monitor: Monitor = None): 
        super().__init__()

        self.taking_actions: bool = False
        self.markerKind: int = 0
        self.monitor: Monitor = None
        self.START_STATE: int=0
        self.NUM_RULES: int=0
        self.NT_OFFSET: int=0
        self.LA_STATE_OFFSET: int=0
        self.EOFT_SYMBOL: int=0
        self.ACCEPT_ACTION: int=0
        self.ERROR_ACTION: int=0
        self.ERROR_SYMBOL: int = 0

        self.lastToken: int=0
        self.currentAction: int=0
        self.action: IntTuple =  IntTuple(0)

        self.tokStream: TokenStream =  None
        self.prs: ParseTable =  None
        self.ra: RuleAction =  None
        self.reset(tokStream, prs, ra, monitor)
    #
    # keep looking ahead until we compute a valid action
    #
    def lookahead(self,act: int, token: int) -> int : 
        act = self.prs.lookAhead(act - self.LA_STATE_OFFSET, self.tokStream.getKind(token))
        return (self.lookahead(act, self.tokStream.getNext(token)) if act > self.LA_STATE_OFFSET else act)
    
    #
    # Compute the next action defined on act and sym. If self
    # action requires more lookahead, these lookahead symbols
    # are in the token stream beginning at the next token that
    # is yielded by peek().
    #
    def tAction1(self,act: int, sym: int) -> int : 
        act = self.prs.tAction(act, sym)
        return (self.lookahead(act, self.tokStream.peek()) if act > self.LA_STATE_OFFSET else  act)
    
    #
    # Compute the next action defined on act and the next k tokens
    # whose types are stored in the array sym starting at location
    # index. The array sym is a circular buffer. If we reach the last
    # element of sym and we need more lookahead, we proceed to the
    # first element.
    # 
    # assert(sym.__len__() == prs.getMaxLa()):
    #
    def tAction(self,act: int, sym , index: int) -> int : 
       
        act = self.prs.tAction(act, sym[index])
        while (act > self.LA_STATE_OFFSET): 
            index = ((index + 1) % sym.__len__())
            act = self.prs.lookAhead(act - self.LA_STATE_OFFSET, sym[index])
        
        return act
    
    #
    # Process reductions and continue...
    #
    def processReductions(self): 
        while True: 
            self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
            self.ra.ruleAction(self.currentAction)
            self.currentAction = self.prs.ntAction( self.stateStack[self.stateStackTop],
                                                    self.prs.lhs(self.currentAction))
            if (not self.currentAction <= self.NUM_RULES):
                 break
        return
    
    #
    # The following functions can be invoked only when the parser is
    # processing actions. Thus, they can be invoked when the parser
    # was entered via the main entry point (parse():). When using
    # the incremental parser (via the entry point parse(int [], int)):,
    # an Exception is thrown if any of these functions is invoked?
    # However, note that when parseActions(): is invoked after successfully
    # parsing an input with the incremental parser, then they can be invoked.
    #
    def getCurrentRule(self) -> int : 
        if (self.taking_actions): 
            return self.currentAction
        
        raise  UnavailableParserInformationException()
    
    def getFirstToken1(self) -> int : 
        if (self.taking_actions): 
            return self.getToken(1)
        
        raise  UnavailableParserInformationException()
    
    def getFirstToken(self,i: int = None)-> int : 
        if (None == i): 
            return self.getFirstToken1()
        
        if (self.taking_actions): 
            return self.getToken(i)
        
        raise  UnavailableParserInformationException()
    
    def getLastToken1(self) -> int : 
        if (self.taking_actions): 
            return self.lastToken
        
        raise  UnavailableParserInformationException()
    
    def getLastToken(self,i: int = None) -> int : 
        if (None == i): 
            return self.getLastToken1()
        
        if (self.taking_actions): 
            return (  self.lastToken if i >= self.prs.rhs(self.currentAction) else 
                      self.tokStream.getPrevious(self.getToken(i + 1)))
        
        raise  UnavailableParserInformationException()
    
    def setMonitor(self,monitor: Monitor): 
        self.monitor = monitor
    
    def reset1(self): 
        self.taking_actions = False
        self.markerKind = 0
        if (self.action.capacity() != 0 ): 
            self.action.reset()
        
    
    def reset2(self,tokStream: TokenStream,monitor: Monitor = None): 
        self.monitor = monitor
        self.tokStream = tokStream
        self.reset1()
    
   
    def reset(self,tokStream: TokenStream = None , prs: ParseTable = None, ra: RuleAction  = None , monitor: Monitor = None): 
        if (ra):
            self.ra = ra

        if (prs):
            self.prs = prs
            self.START_STATE = prs.getStartState()
            self.NUM_RULES = prs.getNumRules()
            self.NT_OFFSET = prs.getNtOffset()
            self.LA_STATE_OFFSET = prs.getLaStateOffset()
            self.EOFT_SYMBOL = prs.getEoftSymbol()
            self.ERROR_SYMBOL = prs.getErrorSymbol()
            self.ACCEPT_ACTION = prs.getAcceptAction()
            self.ERROR_ACTION = prs.getErrorAction()
            if (not prs.isValidForParser()): 
                raise  BadParseSymFileException()
            if (prs.getBacktrack()): raise  NotDeterministicParseTableException()
        
        if (None == tokStream): 
            self.reset1()
            return
        
        self.reset2(tokStream, monitor)


    def parseEntry(self,marker_kind: int = 0): 
        #
        # Indicate that we are running the regular parser and that it's
        # ok to use the utility functions to query the parser.
        #
        self.taking_actions = True
        #
        # Reset the token stream and get the first token.
        #
        self.tokStream.reset()
        self.lastToken = self.tokStream.getPrevious(self.tokStream.peek())
        curtok: int
        current_kind: int
        if (marker_kind == 0): 
            curtok = self.tokStream.getToken()
            current_kind = self.tokStream.getKind(curtok)
        else :
            curtok = self.lastToken
            current_kind = marker_kind
        
        #
        # Start parsing.
        #
        self.reallocateStacks()# make initial allocation
        self.stateStackTop = -1
        self.currentAction = self.START_STATE


        while True: 
            
            #
            # if the parser needs to stop processing,
            # it may do so here.
            #
            if (self.monitor != None and self. monitor.isCancelled()): 
                self.taking_actions = False # indicate that we are done
                return None
            self.stateStackTop +=1
            if (self.stateStackTop >= self.stateStack.__len__()): 
                self.reallocateStacks()
               
            
            self.stateStack[self.stateStackTop] = self.currentAction

            self.locationStack[self.stateStackTop] = curtok

            self.currentAction = self.tAction1(self.currentAction, current_kind)

            if (self.currentAction <= self. NUM_RULES): 
                self. stateStackTop-=1 # make reduction look like a shift-reduce
                self.processReductions()
            
            elif (self.currentAction > self.ERROR_ACTION): 
                self.lastToken = curtok
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
                self.currentAction -= self.ERROR_ACTION
                self.processReductions()
            
            elif (self.currentAction < self.ACCEPT_ACTION): 
                self. lastToken = curtok
                curtok = self.tokStream.getToken()
                current_kind = self.tokStream.getKind(curtok)
            
            else :
                break
        

        self. taking_actions = False # indicate that we are done

        if (self.currentAction == self.ERROR_ACTION):
            raise  BadParseException(curtok)

        return self.parseStack[0 if marker_kind == 0 else  1]
    
    #
    # This method is invoked when using the parser in an incremental mode
    # using the entry point parse(int [], int).
    #
    def resetParser(self): 
        self.resetParserEntry(0)
    
    #
    # This method is invoked when using the parser in an incremental mode
    # using the entry point parse(int [], int).
    #
    def resetParserEntry(self,marker_kind: int): 
        self.markerKind = marker_kind
        if (self.stateStack == None or self.stateStack.__len__() == 0): 
            self.reallocateStacks()# make initial allocation
        
        self.stateStackTop = 0
        self.stateStack[self.stateStackTop] = self.START_STATE
        if (self.action.capacity() == 0): 
            self.action =  IntTuple(1 << 20)
        else :
            self.action.reset()
        
        #
        # Indicate that we are going to run the incremental parser and that
        # it's forbidden to use the utility functions to query the parser.
        #
        self.taking_actions = False
        if (marker_kind != 0): 
            sym: list =  [0]
            sym[0] = self.markerKind
            self.parse(sym, 0)
        
    
    #
    # Find a state in the state stack that has a valid action on ERROR token
    #
    def  recoverableState(self,state: int) -> bool :
        k: int = self.prs.asi(state)
        while (self.prs.asr(k) != 0 ): 
            if (self.prs.asr(k) == self.ERROR_SYMBOL): 
                return True
            k+=1
        
        return False
    

    #
    # Reset the parser at a point where it can legally process
    # the error token. If we can't do that, reset it to the beginning.
    #
    def errorReset(self): 
        gate: int = ( 0 if self.markerKind == 0 else 1)
        while ( self.stateStackTop >= gate): 
            if (self.recoverableState(self.stateStack[self.stateStackTop])): 
                break
            self.stateStackTop-=1
        
        if (self.stateStackTop < gate): 
            self.resetParserEntry(self.markerKind)
        
        return
    

    #
    # This is an incremental LALR(k): parser that takes as argument
    # the next k tokens in the input. If these k tokens are valid for
    # the current configuration, it advances past the first of the k
    # tokens and returns either:
    #
    #    . the last transition induced by that token 
    #    . the Accept action
    #
    # If the tokens are not valid, the initial configuration remains
    # unchanged and the Error action is returned.
    #
    # Note that it is the user's responsibility to start the parser in a
    # proper configuration by initially invoking the method resetParser
    # prior to invoking self function.
    #
    def parse(self,sym, index: int): 
    

        # assert(sym.__len__() == prs.getMaxLa()):

        #
        # First, we save the current length of the action tuple, in
        # case an error is encountered and we need to restore the
        # original configuration.
        #
        # Next, we declara and initialize the variable pos which will
        # be used to indicate the highest useful position in stateStack
        # as we are simulating the actions induced by the next k input
        # terminals in sym.
        #
        # The location stack will be used here as a temporary stack
        # to simulate these actions. We initialize its first useful
        # offset here.
        #
        save_action_length: int = self.action.size()
        pos: int = self.stateStackTop
        location_top: int = self.stateStackTop - 1

        #
        # When a reduce action is encountered, we compute all REDUCE
        # and associated goto actions induced by the current token.
        # Eventually, a SHIFT, SHIFT-REDUCE, ACCEPT or ERROR action is
        # computed...
        #
        self.currentAction = self.tAction(self.stateStack[self.stateStackTop], sym, index)
        while (self.currentAction <= self.NUM_RULES):
        
            self.action.add(self.currentAction)
            while True: 
                location_top -= (self.prs.rhs(self.currentAction) - 1)
                state: int = (self.locationStack[location_top]
                    if location_top > pos  else  self.stateStack[location_top])

                self.currentAction = self.prs.ntAction(state, self.prs.lhs(self.currentAction))
                if (not self.currentAction <= self.NUM_RULES):
                    break

            #
            # ... Update the maximum useful position of the
            # stateSTACK, push goto state into stack, and
            # continue by compute next action on current symbol
            # and reentering the loop...
            #
            pos = pos  if pos < location_top else location_top
            if (location_top + 1 >= self.locationStack.__len__()): 
                self.reallocateStacks()
            
            self.locationStack[location_top + 1] = self.currentAction
            self.currentAction = self.tAction(self.currentAction, sym, index)
        
        #
        # At self point, we have a shift, shift-reduce, accept or error
        # action. stateSTACK contains the configuration of the state stack
        # prior to executing any action on the currenttoken. locationStack
        # contains the configuration of the state stack after executing all
        # reduce actions induced by the current token. The variable pos
        # indicates the highest position in the stateSTACK that is still
        # useful after the reductions are executed.
        #
        if (self.currentAction > self.ERROR_ACTION or# SHIFT-REDUCE action ?
            self.currentAction < self.ACCEPT_ACTION): # SHIFT action ?
        
            self.action.add(self.currentAction)
            #
            # If no error was detected, update the state stack with 
            # the info that was temporarily computed in the locationStack.
            #
            self.stateStackTop = location_top + 1
            for i in range(pos + 1, self.stateStackTop + 1):
                self.stateStack[i] = self.locationStack[i]
            

            #
            # If we have a shift-reduce, process it as well as
            # the goto-reduce actions that follow it.
            #

            if (self.currentAction > self.ERROR_ACTION): 
                self.currentAction -= self.ERROR_ACTION
                while True: 
                    self.stateStackTop -= (self.prs.rhs(self.currentAction) - 1)
                    self.currentAction = self.prs.ntAction(self.stateStack[self.stateStackTop],
                                                           self.prs.lhs(self.currentAction))
                    if(not self.currentAction <= self.NUM_RULES):
                        break
            
            #
            # Process the final transition - either a shift action of
            # if we started out with a shift-reduce, the final GOTO
            # action that follows it.
            #
            self.stateStackTop +=1
            if(self.stateStackTop >= self.stateStack.__len__()):
                self.reallocateStacks()
            
            self.stateStack[self.stateStackTop] = self.currentAction
        
        elif (self.currentAction == self.ERROR_ACTION): 
            self.action.reset(save_action_length)# restore original action state.
        

        
        return self.currentAction
    
    #
    # Now do the final parse of the input based on the actions in
    # the list "action" and the sequence of tokens in the token stream.
    #
    def parseActions(self):
    
        #
        # Indicate that we are processing actions now (for the incremental
        # parser): and that it's ok to use the utility functions to query the
        # parser.
        #
        self.taking_actions = True
        self.tokStream.reset()
        self.lastToken = self.tokStream.getPrevious(self.tokStream.peek())
        curtok: int = (self.tokStream.getToken() if self.markerKind == 0 else  self.lastToken)

        try: 
            #
            # Reparse the input...
            #
            self.stateStackTop = -1
            self.currentAction = self.START_STATE
            for i in  range(0, self.action.size()) :

            
                #
                # if the parser needs to stop processing, it may do so here.
                #
                if (self.monitor  and self.monitor.isCancelled()): 
                    self.taking_actions = False
                    return None
                self.stateStackTop+=1
                self.stateStack[self.stateStackTop] = self.currentAction
                self.locationStack[self.stateStackTop] = curtok

                self.currentAction = self.action.get(i)
                if (self.currentAction <= self.NUM_RULES): # a reduce action?
                
                    self.stateStackTop-=1# turn reduction intoshift-reduction
                    self.processReductions()
                
                else: # a shift or shift-reduce action
                
                    self.lastToken = curtok
                    curtok = self.tokStream.getToken()
                    if (self.currentAction > self.ERROR_ACTION): 
                        self.currentAction -= self.ERROR_ACTION
                        self.processReductions()
                    
                

        except Exception  as ex: # if any exception is thrown, indicate BadParse
        
            self.taking_actions = False
            raise  BadParseException(curtok)
        
        self.taking_actions = False# indicate that we are done.
        self.action =  IntTuple(0)
        return self.parseStack[ 0 if self.markerKind == 0 else 1]
    


