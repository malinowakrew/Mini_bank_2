from __future__ import annotations
from abc import ABC, abstractmethod

class FinancialInterface(ABC):
    @abstractmethod
    def display_History(self):
        pass

    @abstractmethod
    def show(self):
        pass
