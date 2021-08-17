from abc import ABCMeta, abstractmethod
from IMessageHandler import IMessageHandler

from TokenStream import TokenStream




class IToken (metaclass=ABCMeta):
    EOF : int = 0xffff

    @abstractmethod 
    def getKind(self) -> int : 
        pass      
    @abstractmethod 
    def setKind(self,kind: int): 
       pass
    @abstractmethod 
    def getStartOffset(self)-> int : 
       pass   
    @abstractmethod  
    def setStartOffset(self,startOffset: int):
       pass
    @abstractmethod 
    def getEndOffset(self)-> int : 
       pass
    @abstractmethod    
    def setEndOffset(self,endOffset: int): 
       pass
    @abstractmethod   
    def getTokenIndex(self)-> int : 
        pass   
    @abstractmethod   
    def setTokenIndex(self,i: int): 
       pass
    @abstractmethod   
    def getAdjunctIndex(self)-> int :  
       pass
    @abstractmethod   
    def setAdjunctIndex(self,i: int): 
       pass
    @abstractmethod   
    def getPrecedingAdjuncts(self)-> list : 
       pass
    @abstractmethod   
    def getFollowingAdjuncts(self)-> list :  
       pass
    @abstractmethod   
    def getILexStream(self):
       pass
    @abstractmethod   
    def getIPrsStream(self): 
       pass
    @abstractmethod   
    def getLine(self)-> int : 
       pass
    @abstractmethod   
    def getColumn(self)-> int : 
       pass
    @abstractmethod   
    def getEndLine(self)-> int : 
       pass
    @abstractmethod   
    def getEndColumn(self)-> int : 
       pass
    @abstractmethod   
    def toString(self)-> str : 
       pass




class ILexStream(TokenStream): 

    @abstractmethod   
    def getIPrsStream(self): 
       pass
    @abstractmethod   
    def setPrsStream(self,stream): 
       pass
    @abstractmethod   
    def getLineCount(self)-> int : 
       pass
    @abstractmethod   
    def orderedExportedSymbols(self) -> list: 
       pass
    @abstractmethod   
    def getLineOffset(self,i: int)-> int :  
       pass
    @abstractmethod   
    def getLineNumberOfCharAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getColumnOfCharAt(self,i: int)-> int : 
       pass

    @abstractmethod   
    def getCharValue(self,i: int)-> str : 
        pass
    @abstractmethod   
    def getIntValue(self,i: int)-> int : 
       pass 

    @abstractmethod   
    def makeToken(self,startLoc: int, endLoc: int, kind: int): 
       pass
    @abstractmethod   
    def setMessageHandler(self,errMsg: IMessageHandler): 
       pass
    @abstractmethod   
    def getMessageHandler(self) -> IMessageHandler : 
       pass
    @abstractmethod   
    def getLocation(self,left_loc: int, right_loc: int) -> int : 
       pass
    @abstractmethod   
    def reportLexicalError(self,left_loc: int, right_loc: int, errorCode: int = None, error_left_loc: int = None,
     error_right_loc: int = None, errorInfo: list = None): 
        pass

    @abstractmethod   
    def toString(self,startOffset: int, endOffset: int) -> str : 
       pass


 


class IPrsStream ( TokenStream ):
    @abstractmethod   
    def getMessageHandler(self): 
       pass       
    @abstractmethod   
    def setMessageHandler(self,errMsg: IMessageHandler = None):
       pass
    @abstractmethod   
    def getILexStream(self): 
       pass
    @abstractmethod   
    def setLexStream(self,lexStream: ILexStream): 
       pass
    #/**
    # * @deprecated replaced by @link #getFirstRealToken():
    # *
    # */
    #getFirstErrorToken(i: int): 

    #/**
    # * @deprecated replaced by @link #getLastRealToken():
    # *
    # */
    #getLastErrorToken(i: int): 

    @abstractmethod   
    def makeToken(self,startLoc: int, endLoc: int, kind: int): 
       pass       
    @abstractmethod   
    def makeAdjunct(self,startLoc: int, endLoc: int, kind: int): 
       pass
    @abstractmethod   
    def removeLastToken(self): 
       pass
    @abstractmethod   
    def getLineCount(self)-> int: 
       pass
    @abstractmethod   
    def getSize(self)-> int: 
       pass
    @abstractmethod   
    def remapTerminalSymbols(self,ordered_parser_symbols: list, eof_symbol: int): 
       pass
    @abstractmethod   
    def orderedTerminalSymbols(self) -> list: 
       pass
    @abstractmethod   
    def mapKind(self,kind: int)-> int:  
       pass
    @abstractmethod   
    def resetTokenStream(self): 
       pass
    @abstractmethod   
    def getStreamIndex(self)-> int: 
       pass
    @abstractmethod   
    def setStreamIndex(self,index: int): 
       pass
    @abstractmethod   
    def setStreamLength(self)-> int: 
       pass
    @abstractmethod   
    def setStreamLength(self,len: int): 
       pass
    @abstractmethod   
    def addToken(self,token: IToken): 
       pass
    @abstractmethod   
    def addAdjunct(self,adjunct: IToken): 
       pass
    @abstractmethod   
    def orderedExportedSymbols(self) -> list: 
       pass
    @abstractmethod   
    def getTokens(self) -> list : 
       pass
    @abstractmethod   
    def getAdjuncts(self) -> list: 
       pass
    @abstractmethod   
    def getFollowingAdjuncts(self,i: int) -> list: 
       pass
    @abstractmethod   
    def getPrecedingAdjuncts(self,i: int) -> list: 
       pass
    @abstractmethod   
    def getIToken(self,i: int) -> IToken: 
       pass
    @abstractmethod   
    def getTokenText(self,i: int) -> str : 
       pass
    @abstractmethod   
    def getStartOffset(self,i: int) -> int : 
       pass
    @abstractmethod   
    def getEndOffset(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getLineOffset(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getLineNumberOfCharAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getColumnOfCharAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getTokenLength(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getLineNumberOfTokenAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getEndLineNumberOfTokenAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getColumnOfTokenAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getEndColumnOfTokenAt(self,i: int)-> int : 
       pass
    @abstractmethod   
    def getInputChars(self) : 
       pass
    @abstractmethod   
    def getInputBytes(self): 
       pass
    @abstractmethod   
    def toStringFromIndex(self,first_token: int, last_token: int) -> str: 
       pass
    @abstractmethod   
    def toString(self,t1: IToken, t2: IToken) -> str: 
       pass
    @abstractmethod   
    def getTokenIndexAtCharacter(self,offset: int) -> int : 
       pass
    @abstractmethod   
    def getTokenAtCharacter(self,offset: int) -> IToken: 
       pass
    @abstractmethod   
    def getTokenAt(self,i: int)-> IToken: 
       pass
    @abstractmethod   
    def dumpTokens(self): 
       pass
    @abstractmethod   
    def dumpToken(self,i: int): 
        pass      
    @abstractmethod   
    def makeErrorToken(self,first: int, last: int, error: int, kind: int)-> int : 
       pass

