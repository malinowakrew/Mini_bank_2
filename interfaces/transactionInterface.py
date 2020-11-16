from __future__ import annotations
from abc import ABC, abstractmethod

class TransactionInterface(ABC):
    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def addMoney(self):
        pass