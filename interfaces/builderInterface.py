from __future__ import annotations
from abc import ABC, abstractmethod

class buildInterface(ABC):
    @abstractmethod
    def buildUser(self, accountID):
        pass

    @abstractmethod
    def buildWallets(self, accountID):
        pass

    @abstractmethod
    def buildMainWallet(self, accountID):
        pass

    @abstractmethod
    def reset(self):
        pass