

from _typeshed import Self
from AbstractToken import AbstractToken
from Protocol import IPrsStream


class Token (AbstractToken) :
  
    def __init__(self,startOffset: int, endOffset: int, kind: int, iPrsStream: IPrsStream = None): 
        super.__init__(startOffset, endOffset, kind, iPrsStream)
    
    def getFollowingAdjuncts(self) -> list: 

        stream = self.getIPrsStream()
        return [] if stream == None else stream.getFollowingAdjuncts(self.getTokenIndex())
      
    def getPrecedingAdjuncts(self) -> list: 
        stream = self.getIPrsStream()
        return [] if stream == None else stream.getPrecedingAdjuncts(self.getTokenIndex())

    

