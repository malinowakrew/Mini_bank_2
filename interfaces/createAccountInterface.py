from __future__ import annotations
from abc import ABC, abstractmethod


class AccountInterface(ABC):

    @abstractmethod
    def createAccountInterface(self):
        pass

    @abstractmethod
    def logInInterface(self):
        pass
