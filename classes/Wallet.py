from db import db

#from errors import NotEnoughFounds
from classes.Currency import *

class Error(Exception):
    pass

class NotEnoughFounds(Error):
    def __init__(self, message="Not enough founds on your account") -> None:
        self.message = message
        super().__init__(self.message)

class Wallet():
    def __init__(self, funds, currency, ID):
        self.funds = funds
        self.currency = currency
        self.walletID = ID

    def getFounds(self):
        return self.funds

    def changeFounds(self, founds):
        walletData = db.wallets.find_one({"currency": str(self.currency)})
        id = walletData['_id']
        results = db.wallets.update_one({'_id': id}, {"$set": {'founds': str(founds)}})

        return walletData

    def pay(self, founds):
        walletData = db.wallets.find_one({"currency": str(self.currency)})
        walletFounds = walletData['founds']
        if(float(walletFounds) < founds):
            raise NotEnoughFounds
        else:
            results = db.wallets.update_one({'_id': walletData['_id']}, {"$inc": {'founds': -1.0 * founds}})

        return results

