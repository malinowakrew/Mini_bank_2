from __future__ import annotations
from abc import ABC, abstractmethod

class LogInterface(ABC):
    @abstractmethod
    def logIn(self):
        pass