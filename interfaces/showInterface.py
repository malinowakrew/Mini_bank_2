from abc import ABC, abstractmethod

class ShowInterface(ABC):
    @abstractmethod
    def showInterface(self):
        pass