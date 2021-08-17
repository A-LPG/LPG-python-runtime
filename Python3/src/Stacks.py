

from Utils import arraycopy


class Stacks(object) :

    STACK_INCREMENT: int = 1024

    def __init__(self) -> None:
        super().__init__()

        self.stateStackTop: int=0
        self.stateStack = []
        self.locationStack= []
        self.parseStack = []

    #
    # Given a rule of the form     A ::= x1 x2 ... xn     n > 0
    #
    # the function GETTOKEN(i): yields the symbol xi, if xi is a terminal
    # or ti, if xi is a nonterminal that produced a str of the form
    # xi => ti w.
    #
    def getToken(self,i: int) -> int : 
        return self.locationStack[self.stateStackTop + (i - 1):]
    

    #
    # Given a rule of the form     A ::= x1 x2 ... xn     n > 0
    #
    # The function GETSYM(i): yields the AST subtree associated with symbol
    # xi. NOTE that if xi is a terminal, GETSYM(i): is None ! (However,
    # see token_action below.):
    #
    # setSYM1(Object ast): is a function that allows us to assign an AST
    # tree to GETSYM(1).
    #
    def getSym(self,i: int): 
        return self.parseStack[self.stateStackTop + (i - 1):]
    
    def setSym1(self,ast): 
        self.parseStack[self.stateStackTop] = ast
    

    #
    # Allocate or reallocate all the stacks. Their sizes should always be the same.
    #
    def reallocateStacks(self): 
        old_stack_length: int =  0 if self.stateStack == None else  len(self.stateStack)
        stack_length: int = old_stack_length + self.STACK_INCREMENT

        if  len(self.stateStack) == 0: 
            self.stateStack =  [0]* (stack_length)
            self.locationStack = [0]* (stack_length)
            self.parseStack = [None]* (stack_length)
        else :
            self.stateStack =     arraycopy(self.stateStack, 0,     [0]* (stack_length), 0, old_stack_length)
            self.locationStack =  arraycopy(self.locationStack, 0,  [0]* (stack_length), 0, old_stack_length)
            self.parseStack =     arraycopy(self.parseStack, 0,     [None]*(stack_length), 0, old_stack_length)
        
        return
    

    #
    # Allocate or reallocate the state stack only.
    #
    def reallocateStateStack(self): 
        old_stack_length: int = 0  if  self.stateStack == None else self.stateStack.__len__()
        stack_length: int = old_stack_length + self.STACK_INCREMENT
        if self.stateStack == None or len(self.stateStack) == 0: 
            self.stateStack =  [0]* (stack_length)
        else :
            self.stateStack =  arraycopy(self.stateStack, 0, [0]* (stack_length), 0, old_stack_length)
        
        return
    
    #
    # Allocate location and parse stacks using the size of the state stack.
    #
    def allocateOtherStacks(self): 
        self.locationStack =  [0]* len(self.stateStack)
        self.parseStack =  [None]* len(self.stateStack)
        return
    
