from __future__ import annotations
from abc import ABC, abstractmethod

#from classes.Session import Session

class TransactionInterface(ABC):
    @abstractmethod
    def transferInterface(self):
        pass

    @abstractmethod
    def depositInterface(self, session):
        pass

    """
    @abstractmethod
    def show(self):
        pass
    """

    @abstractmethod
    def addMoneyInterface(self):
        pass

    @abstractmethod
    def payInterface(self):
        pass