from abc import ABCMeta, abstractmethod

class ParseTable(metaclass=ABCMeta): 
   
    @abstractmethod
    def baseCheck(self, index: int)-> int : 
       pass
    @abstractmethod
    def rhs(self, index: int)-> int : 
       pass
    @abstractmethod
    def baseAction(self, index: int)-> int :
       pass 
    @abstractmethod
    def lhs(self, index: int)-> int : 
       pass
    @abstractmethod
    def termCheck(self, index: int)-> int : 
       pass
    @abstractmethod
    def termAction(self, index: int)-> int : 
       pass
    @abstractmethod
    def asb(self, index: int)-> int : 
       pass
    @abstractmethod
    def asr(self, index: int)-> int :
       pass
    @abstractmethod
    def nasb(self, index: int)-> int : 
       pass
    @abstractmethod
    def nasr(self, index: int)-> int : 
       pass
    @abstractmethod
    def terminalIndex(self, index: int)-> int : 
       pass
    @abstractmethod
    def nonterminalIndex(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopePrefix(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopeSuffix(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopeLhs(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopeLa(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopeStateSet(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopeRhs(self, index: int)-> int : 
       pass
    @abstractmethod
    def scopeState(self, index: int)-> int : 
       pass
    @abstractmethod
    def inSymb(self, index: int)-> int : 
       pass

    @abstractmethod
    def name(self, index: int)-> str : 
       pass
      
    @abstractmethod
    def originalState(state: int)-> int : 
       pass
    @abstractmethod
    def asi(self, state: int)-> int :
       pass
    @abstractmethod
    def nasi(self, state: int)-> int :
       pass
    @abstractmethod
    def inSymbol(self, state: int)-> int :
       pass
    @abstractmethod
    def ntAction(self, state: int, sym: int)-> int :
       pass
    @abstractmethod
    def tAction(self,act: int, sym: int)-> int : 
       pass
    @abstractmethod
    def lookAhead(self,act: int, sym: int)-> int : 
       pass
    @abstractmethod
    def getErrorSymbol(self)-> int : 
       pass
    @abstractmethod
    def getScopeUbound(self)-> int : 
       pass
    @abstractmethod
    def getScopeSize(self)-> int : 
       pass
    @abstractmethod
    def getMaxNameLength(self)-> int : 
       pass
    @abstractmethod
    def getNumStates(self)-> int : 
       pass
    @abstractmethod
    def getNtOffset(self)-> int : 
       pass
    @abstractmethod
    def getLaStateOffset(self)-> int : 
       pass
    @abstractmethod
    def getMaxLa(self)-> int : 
       pass
    @abstractmethod
    def getNumRules(self)-> int : 
       pass
    @abstractmethod
    def getNumNonterminals(self)-> int : 
       pass
    @abstractmethod
    def getNumSymbols(self)-> int : 
       pass
    @abstractmethod
    def getStartState(self)-> int : 
       pass
    @abstractmethod
    def getStartSymbol(self)-> int : 
       pass
    @abstractmethod
    def getEoftSymbol(self)-> int : 
       pass
    @abstractmethod
    def getEoltSymbol(self)-> int : 
       pass
    @abstractmethod
    def getAcceptAction(self)-> int : 
       pass
    @abstractmethod
    def getErrorAction(self)-> int :
       pass
    @abstractmethod
    def isNullable(self,symbol: int)-> bool:
       pass
    @abstractmethod
    def isValidForParser(self)-> bool:
       pass
    @abstractmethod
    def getBacktrack(self) -> bool: 
       pass


  

