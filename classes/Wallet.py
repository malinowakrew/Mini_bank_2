from db import db

#from errors import NotEnoughFounds
#from classes.Currency import *

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
        results = db.wallets.update({'_id': self.walletID}, {"$inc": {'founds': founds}})
        return results

    def pay(self, foundsToPay):
        walletData = db.wallets.find_one({"_id": self.walletID})
        walletFounds = walletData['founds']
        if float(walletFounds) < foundsToPay:
            raise NotEnoughFounds
        else:
            results = db.wallets.update({'_id': self.walletID}, {"$inc": {'founds': -foundsToPay}})
            return results

