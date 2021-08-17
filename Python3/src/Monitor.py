
from abc import ABCMeta, abstractmethod


class Monitor(metaclass=ABCMeta):

    @abstractmethod 
    def isCancelled(self) -> bool:
        return False

