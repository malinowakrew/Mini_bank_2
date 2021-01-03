from __future__ import annotations
from abc import ABC, abstractmethod
import re


class AccountInterface(ABC):

    @abstractmethod
    def createAccountInterface(self):
        pass

    @abstractmethod
    def logInInterface(self):
        pass

# c = 13
# class Grandpa:
#     def __init__(self, name):
#         self.age = 75
#         self.name = name
#
#     @classmethod
#     def this_method_is_class(cls, name) -> Grandpa:
#         name = name + "Jacuś  "
#         grand = cls(name)
#         return grand
#
# class Grandma(Grandpa):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def glo(self):
#         global c
#         c += 3
#         print(c)
#         print(__call__)
#
# if __name__ == "__main__":
#
#
#     # one = Grandpa("Pierwszy")
#     # two = one.this_method_is_class("drugi")
#     # three = Grandma("Joanna")
#     #
#     # three.glo()
#     # print(c)
#     string = "bla bla[91]"
#     nowe = re.sub("\[[0-9]{1,2}\]", "*", string)
#     print(nowe)
#
#
#     #print(f"{two.name}jak")
