from __future__ import annotations
from abc import ABC, abstractmethod

from classes.Account import Account


class DepositSessionInterface(ABC):

    @abstractmethod
    def depositSessionInterface(self, account: Account):
        pass

