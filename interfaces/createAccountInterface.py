from __future__ import annotations
from abc import ABC, abstractmethod

class CreateAccountInterface(ABC):
    @abstractmethod
    def createAccount(self, password, name, surname, currency):
        pass