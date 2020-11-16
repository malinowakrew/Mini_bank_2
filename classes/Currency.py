from datetime import datetime
from bson.objectid import ObjectId

class Currency():
    def __init__(self, name, rate, ID) -> None:
        self.currencyID = ObjectId(ID)
        self.name = name
        self.rate = rate
        self.date = datetime.now()

    def getCurrency(self):
        return({"name": self.name,
                "rate": self.rate,
                "date": self.date
                })