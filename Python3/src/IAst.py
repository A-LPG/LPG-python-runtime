
from abc import ABCMeta, abstractmethod

from Protocol import IToken


class IAst(metaclass=ABCMeta):

    @abstractmethod
    def getNextAst(self):
        pass

    @abstractmethod
    def getParent(self): 
        pass

    @abstractmethod
    def getLeftIToken(self) -> IToken: 
        pass

    @abstractmethod
    def getRightIToken(self) -> IToken: 
        pass
    @abstractmethod
    def getPrecedingAdjuncts(self) -> list: 
        pass
    @abstractmethod
    def getFollowingAdjuncts(self) -> list:
        pass

    @abstractmethod
    def getChildren(self):
        pass

    @abstractmethod
    def getAllChildren(self):
        pass
      
    @abstractmethod
    def accept(self,v) -> None: 
        pass
