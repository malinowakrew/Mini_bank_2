from datetime import datetime
from bson.objectid import ObjectId
from classes.ChangeManager import ChangeManager
from db import db

class Currency():
    def __init__(self, name, rate, ID) -> None:
        self.currencyID = ObjectId(ID)
        self.name = name
        self.rate = rate
        self.date = datetime.now()
        self.changeManager = ChangeManager(name)

    def getCurrency(self):
        return({"name": self.name,
                "rate": self.rate,
                "date": self.date
                })

    def changeRate(self, change):
        old_rate = self.rate
        self.rate = float(change)
        result = db.currencies.update({"name": self.name}, {'$inc': {'rate': float(change)}})
        self.changeManager.changeNotify(change, self.name)
