from __future__ import annotations
from abc import ABC, abstractmethod

#from classes.Session import Session

class TransactionInterface(ABC):
    @abstractmethod
    def transferInterface(self):
        pass

    @abstractmethod
    def addMoneyInterface(self):
        pass

    @abstractmethod
    def payInterface(self):
        pass