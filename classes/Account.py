import random
import pymongo

from interfaces.transactionInterface import *
from interfaces.financialInterface import *
from interfaces.showInterface import *

from db import db
from classes.Wallet import Wallet
from classes.User import User

from bson.objectid import ObjectId

class Account(TransactionInterface, FinancialInterface, ShowInterface):
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


    def displayWallets(self):
        list = []
        for wallet in self.wallets:
            list.append([wallet.currency, wallet.funds])
        return list

    def addWallet(self, currency):
        result = db.wallets.insert_one({'currency': {"id": currency.currencyID,
                                            "db": "currencies"},
                                        'founds': 0})

        result = db.accounts.update({'_id': self.accountID}, {"$push": {"wallets": {'id': result.inserted_id,
                                                                          'db': "wallets"}}})

        self.wallets = self.walletsInit()

    def createWallets(self):
        pass


    def checkMainWallet(self):
        pass


    #Interfaces

    def addMoneyInterface(self):
        print("Adding money")
        money = int(input("Money to add: "))

        try:
            self.mainWallet.changeFounds(money)
            self.wallets = self.walletsInit()
            print("Added")
            self.showInterface()
        except Exception as error:
            print(error)



    def payInterface(self):
        print("Pay for what you want")
        currencyToChoose = self.displayWallets()

        self.showInterface()

        Choose = input("Number of currency: ")
        try:
            currencyToPay: list = currencyToChoose[int(Choose)-1][0]
        except Exception as error:
            print(error)

        foundsToPay = int(input("Money: "))
        for wallet in self.wallets:
            if wallet.currency == currencyToPay:
                try:
                    result = wallet.pay(foundsToPay)
                except Exception as error:
                    print(error)

        self.wallets = self.walletsInit()

        self.showInterface()

    def transferInterface(self):
        pass

    def showInterface(self):
        print("Masz na koncie:")
        wallets = self.displayWallets()

        for number, wallet in enumerate(wallets):
            print(f"{number+1}. {wallet[0]}: {wallet[1]}")

    def BalanceInterface(self):
        pass





