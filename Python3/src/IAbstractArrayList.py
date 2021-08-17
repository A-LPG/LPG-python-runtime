from abc import ABCMeta, abstractmethod



class IAbstractArrayList(metaclass=ABCMeta):

    @abstractmethod
    def size(self) -> int : 
       pass

    @abstractmethod
    def getElementAt(self,i: int): 
       pass

    @abstractmethod
    def getList(self): 
       pass

    @abstractmethod
    def add(self,elt): 
       pass
  

