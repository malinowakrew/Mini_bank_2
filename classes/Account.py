import random
import pymongo

from interfaces.transactionInterface import *
from interfaces.financialInterface import *

from db import db
from classes.Wallet import Wallet
from classes.User import User

from bson.objectid import ObjectId

class Account(TransactionInterface, FinancialInterface):
    def __init__(self, ID) -> None:
        self.accountID = ObjectId(ID)
        self.wallets = self.walletsInit()
        self.mainWallet = self.mainWalletInit()
        self.user = self.userInit()

    def userInit(self):
        accountDB = db.accounts.find_one({'_id': self.accountID})

        userDB = db.users.find_one({"_id": (accountDB['user'])['id']})
        #print(f"Witam Cię, {userDB['name']}")
        return User(userDB["name"], userDB["surname"], userDB["_id"])

    def walletsInit(self):
        wallets = []
        accountDB = db.accounts.find_one({"_id": self.accountID})
        for walletDB in accountDB["wallets"]:
            wallet = db.wallets.find_one({"_id": walletDB['id']})
            currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})

            wallets.append(Wallet(wallet['founds'], currencyName['name'], wallet['_id']))
        return wallets

    def mainWalletInit(self):
        accountDB = db.accounts.find_one({"_id": self.accountID})
        walletDB = accountDB['wallets'][0]
        wallet = db.wallets.find_one({"_id": walletDB['id']})
        currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})
        return(Wallet(wallet['founds'], currencyName['name'], wallet['_id']))

    def transfer(self, money, currency):
        if self.mainWallet.funds >= money:
            for wallet in self.wallets:
                if wallet.currency == currency.name:
                    result = db.wallets.update({'_id': wallet.walletID}, {"$inc": {"founds": money}})
                    self.addMoney(-money)

    def deposit(self):
        pass

    def show(self):
        print("Masz na koncie:")
        for wallet in self.wallets:
            print(f"{wallet.currency}: {wallet.funds}")

    def addMoney(self, money):
        walletDB = db.wallets.update({'_id': self.mainWallet.walletID}, {"$inc": {"founds": money}})
        self.wallets = self.walletsInit()



    def display_History(self):
        pass

    def addWallet(self, currency):
        result = db.wallets.insert_one({'currency': {"id": currency.currencyID,
                                            "db": "currencies"},
                                        'founds': 0})

        result = db.accounts.update({'_id': self.accountID}, {"$push": {"wallets": {'id': result.inserted_id,
                                                                          'db': "wallets"}}})

        self.wallets = self.walletsInit()

    def createWallets(self):
        pass

    def displayWallets(self):
        pass

    def checkMainWallet(self):
        pass

def test():
    ac = Account("98")
    ac.walletsInit()

if __name__ == "__main__":
    test()