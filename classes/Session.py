from datetime import datetime

from interfaces.logInterface import *
from interfaces.createAccountInterface import *
from interfaces.financialInterface import *

from db import db
from classes.Currency import Currency
from classes.Account import Account

from errors import Error

class LogError(Error):
    def __init__(self, message="Passwd is not correct") -> None:
        self.message = message
        super().__init__(self.message)

class AccountAlreadyExist(Error):
    def __init__(self, message="Use other name xd") -> None:
        self.message = message
        super().__init__(self.message)

#Klasa

class Session(LogInterface, CreateAccountInterface, FinancialInterface):
    def __init__(self) -> None:
        self.date = datetime.now()
        self.currencies = self.currenciesInit()


    def currenciesInit(self):
        currencies = []
        for currencyDB in db.currencies.find():
            currencies.append(Currency(currencyDB.get('name'), currencyDB.get('rate'), currencyDB.get('_id')))

        return currencies

    def display_History(self):
        pass

    def show(self):
        for currency in self.currencies:
            print(currency.getCurrency()["name"])

    def displayCurrencies(self):
        list = []
        for currency in self.currencies:
            list.append(currency.getCurrency()["name"])
        return list

    def createAccount(self, nick, password, name, surname, currency):
        checkUser = db.accounts.find_one({"nick": nick})
        if checkUser == None:

            resultUser = db.users.insert_one({"name": name,
                                              "surname": surname,
                                              })

            currency = db.currencies.find_one({"name": currency})

            resultwallet = db.wallets.insert_one({"currency": {"id": currency['_id'],
                                                               "db": "currencies"},
                                                  "founds": 0})

            resultAccount = db.accounts.insert_one({"password": password,
                                                    "nick": nick,
                                                    "user": {"ref": "user",
                                                             "id": resultUser.inserted_id,
                                                             "db": "users"},
                                                    "wallets": [{"id": resultwallet.inserted_id,
                                                                 "db": "wallets",
                                                                 "special": "mainWallet"}]})

            return resultAccount.inserted_id
        else:
            raise AccountAlreadyExist

    def calculateBalance(self, defaultCurrencyName):
        #efaultCurrencyValue = db.currencies.find_one({"name": defaultCurrencyName})
        values = {}
        for currency in self.currencies:
            if currency.name == defaultCurrencyName:
                defaultCurrencyValue = currency

        if defaultCurrencyValue == None:
            raise ValueError

        for currency in self.currencies:
            if currency.name != defaultCurrencyName:
                values[currency.name] = int(defaultCurrencyValue.rate)/currency.rate
        return values

    def logIn(self, nick, password):
        accountDB = db.accounts.find_one({"nick": nick})

        if accountDB['password'] == password:
            return Account(accountDB['_id'])
        else:
            raise LogError


    def getCurrencies(self):
        return self.currencies

    def findCurrency(self):
        pass

    #Interfaces
    def createAccountInterface(self):
        print(f"Creating account")
        nick = input("Nick: ")
        password = input("Password: ")
        name = input("Name: ")
        surname = input("Surname: ")
        print("Currency: ")

        for number, currency in enumerate(self.displayCurrencies()):
            print(f"{number+1}. {currency}")

        currencyChoose = input("Type number of choosed currency: ")
        currency = self.displayCurrencies()
        type(currency)
        currency = currency[int(currencyChoose)-1]

        try:
            self.createAccount(nick, password, name, surname, currency)
        except Exception as error:
            print(error)

    def logInInterface(self):
        print("Sign in")
        nick = input("Nick: ")
        password = input("Password: ")

        try:
            Account = self.logIn(nick, password)
            print(f"Welcom {Account.user.name}")
            return Account
        except Exception as error:
            print(error)
