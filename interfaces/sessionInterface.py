from __future__ import annotations
from abc import ABC, abstractmethod

class sessionInterface(ABC):
    @abstractmethod
    def calculateBalance(self):
        pass

    @abstractmethod
    def currenciesInit(self):
        pass

    @abstractmethod
    def createAccount(self):
        pass

    @abstractmethod
    def displayCurrencies(self):
        pass

    @abstractmethod
    def logIn(self):
        pass

    @abstractmethod
    def calculateAmountOfMoney(self):
        pass