import random
import pymongo

from interfaces.transactionInterface import *
from interfaces.financialInterface import *
from interfaces.showInterface import *

from db import db
from classes.Wallet import Wallet
from classes.User import User
from classes.Currency import Currency
#from classes.Session import Session

from bson.objectid import ObjectId


class Account(TransactionInterface, FinancialInterface, ShowInterface):
    def __init__(self, ID, user, wallets, mainWallet) -> None:
        self.accountID = ObjectId(ID)
        self.wallets = wallets
        self.mainWallet = mainWallet
        self.user = user

    """
    def userInit(self):
        accountDB = db.accounts.find_one({'_id': self.accountID})

        userDB = db.users.find_one({"_id": (accountDB['user'])['id']})
        return User(userDB["name"], userDB["surname"], userDB["_id"])
    """

    def walletsUpdate(self):
        wallets = []
        accountDB = db.accounts.find_one({"_id": self.accountID})
        for walletDB in accountDB["wallets"]:
            wallet = db.wallets.find_one({"_id": walletDB['id']})
            currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})

            wallets.append(Wallet(wallet['founds'], currencyName['name'], wallet['_id']))
        return wallets

    """
    def mainWalletInit(self):
        accountDB = db.accounts.find_one({"_id": self.accountID})
        walletDB = accountDB['wallets'][0]
        wallet = db.wallets.find_one({"_id": walletDB['id']})
        currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})
        return (Wallet(wallet['founds'], currencyName['name'], wallet['_id']))

    """

    def transfer(self, money, currency):
        if self.mainWallet.funds >= money:
            for wallet in self.wallets:
                if wallet.currency == currency.name:
                    result = db.wallets.update({'_id': wallet.walletID}, {"$inc": {"founds": money}})
                    self.mainWallet.changeFounds(-money)

    def deposit(self, transferMoney, more, less, money):
        for wallet in self.wallets:
            if wallet.currency == more:
                wallet.changeFounds(transferMoney)

            if wallet.currency == less:
                wallet.changeFounds(-money)

        self.wallets = self.walletsUpdate()

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

        self.wallets = self.walletsUpdate()


    # Interfaces

    def addMoneyInterface(self):
        print("Adding money")
        money = float(input("Money to add: "))

        try:
            self.mainWallet.changeFounds(money)
            self.wallets = self.walletsUpdate()
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
            currencyToPay: list = currencyToChoose[int(Choose) - 1][0]
        except Exception as error:
            print(error)

        foundsToPay = float(input("Money: "))
        for wallet in self.wallets:
            if wallet.currency == currencyToPay:
                try:
                    result = wallet.pay(foundsToPay)
                except Exception as error:
                    print(error)

        self.wallets = self.walletsUpdate()

        self.showInterface()

    def transferInterface(self):
        pass

    def showInterface(self):
        print("All your money:")
        wallets = self.displayWallets()

        for number, wallet in enumerate(wallets):
            print(f"{number + 1}. {wallet[0]}: {wallet[1]}")

    def BalanceInterface(self):
        self.showInterface()
        userData = self.user.getData()

        for key in userData:
            print(f"{key}: {userData[key]}")

        print("\n")


