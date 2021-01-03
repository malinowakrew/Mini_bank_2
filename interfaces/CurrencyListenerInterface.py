from __future__ import annotations
from abc import ABC, abstractmethod


class CurrencyListenerInterface(ABC):
    @abstractmethod
    def showMessage(self, currency):
        pass