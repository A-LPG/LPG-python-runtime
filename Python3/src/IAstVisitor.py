from abc import ABCMeta, abstractmethod

from IAst import IAst



class IAstVisitor (metaclass=ABCMeta):

    @abstractmethod   
    def preVisit(self,element: IAst) -> bool: 
       pass

    @abstractmethod   
    def postVisit(self,element: IAst) -> None: 
       pass

