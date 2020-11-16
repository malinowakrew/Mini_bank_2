import random

class User():
    def __init__(self, name, surname, ID) -> None:
        self.userID = ID
        self.name = name
        self.surname = surname

    def getData(self):
        return {"ID": self.userID,
                "name": self.name,
                "surname": self.surname}