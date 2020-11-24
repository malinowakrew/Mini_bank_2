from __future__ import annotations
from abc import ABC, abstractmethod

class OverseeInterface(ABC):
    @abstractmethod
    def showUsersInterface(self):
        pass