from datetime import datetime

#from classes.Account import *
from interfaces.createAccountInterface import *
from interfaces.financialInterface import *
from interfaces.depositInterface import *
from interfaces.sessionInterface import *


from classes.Currency import Currency

from classes.Builders import *

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

class Session(sessionInterface): #LogInterface, CreateAccountInterface, FinancialInterface, DepositSessionInterface):
    def __init__(self) -> None:
        self.date = datetime.now()
        self.currencies = self.currenciesInit()


    def currenciesInit(self):
        currencies = []
        for currencyDB in db.currencies.find():
            currencies.append(Currency(currencyDB.get('name'), currencyDB.get('rate'), currencyDB.get('_id')))

        return currencies


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
                                                                 "special": "mainWallet"}],
                                                    "messages": ["Welcome"]})

            return resultAccount.inserted_id
        else:
            raise AccountAlreadyExist

    def calculateBalance(self, defaultCurrencyName):
        #efaultCurrencyValue = db.currencies.find_one({"name": defaultCurrencyName})
        values = {}
        defaultCurrencyValue = None
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
        director = Director()
        admin = False
        try:
            accountDB['administrator']
            admin = True
        except Exception as error:
            pass

        if admin:
            chose = input("Do you want to use admin account?")
            if chose == "YES":
                print("Admin")
                if accountDB['password'] == password:
                    builder = BuildOverseeAccount()
                    director.builder = builder

                    return director.makeOversee(accountDB['_id'])

        if accountDB['password'] == password:
            print("Normal user")
            builder = BuildNormalAccount()
            director.builder = builder

            return director.makeAccount(ObjectId(accountDB['_id']))
        else:
            print("Problem")
            raise LogError

    def calculateAmountOfMoney(self, currencyValues, money):
        moneyDict = dict()
        for value in currencyValues:
            moneyDict[value] = currencyValues[value] * money
        return moneyDict



class SessionClient(AccountInterface, FinancialInterface, DepositSessionInterface):
    def __init__(self, session):
        self.session = session

    #Interfaces
    def showInterface(self):
        for number, currency in enumerate(self.session.currencies):
            print(f"{number}. {currency.getCurrency()['name']}")

    def createAccountInterface(self):
        print(f"Creating account")
        nick = input("Nick: ")
        password = input("Password: ")
        name = input("Name: ")
        surname = input("Surname: ")
        print("Currency: ")

        for number, currency in enumerate(self.session.displayCurrencies()):
            print(f"{number+1}. {currency}")

        currencyChoose = input("Type number of choosed currency: ")
        currency = self.session.displayCurrencies()
        type(currency)
        currency = currency[int(currencyChoose)-1]

        try:
            self.session.createAccount(nick, password, name, surname, currency)
        except Exception as error:
            print(error)

    def logInInterface(self):
        print("Sign in")
        nick = input("Nick: ")
        password = input("Password: ")

        try:
            account = self.session.logIn(nick, password)
            print(f"Welcome {account.user.name}")
            return account
        except Exception as error:
            print(error)

    def BalanceInterface(self, account=None):
        self.showInterface()

        chooseCurrency = input("Choose default currency: ")
        dictCurrencies: dict = self.session.calculateBalance(chooseCurrency)

        for currency in dictCurrencies:
            print(f"{currency}: {dictCurrencies[currency]}")

        if account != None:
            choose = input("Type 'YES' if you want to calculate money")
            if choose == "YES":
                money = float(input("Money to exchange in default currency which you choose before: "))
                moneyDict = self.session.calculateAmountOfMoney(dictCurrencies, money)

                print(f"Exchanging {money} {chooseCurrency} you can get: ")
                for value in moneyDict:
                    print(f"{moneyDict[value]} {value}")



    def depositSessionInterface(self, account: Account):
        walletsList = account.displayWallets()

        for wallet in walletsList:
            print(f"{wallet[0]}: {wallet[1]}")

        choose = 'NEW'
        if len(walletsList) >= 2:
            choose = input("Type 'NEW' if you want to create new wallet or type 'OLD' if you want use existing wallet")
        else:
            print("You have to make more wallets to exchange money")

        if choose == "NEW":
            self.showInterface()

            newCurrency = input("Choose new currency: ")
            for currency in self.session.currencies:
                if currency.name == newCurrency:
                    more = currency
            try:
                account.addWallet(more)
                print(f"Wallet {more} was created")
            except Exception as error:
                print(error)

            choose = 'OLD'

        if choose == "OLD":
            less = input("Transfer money FROM: ")
            more = input("TO: ")
            money = float(input("Money: "))

            dictCurrencies: dict = self.session.calculateBalance(less)

            currencyDict = self.session.calculateAmountOfMoney(dictCurrencies, money)

            print(currencyDict[more])
            transferMoney = float(currencyDict[more])
            account.deposit(transferMoney, more, less, money)
        else:
            raise ValueError

    def subscribeCurrency(self, account: Account):
        for currency in self.session.currencies:
            print(currency.name)

        decision1 = input("Choose currency to subscribe: ")

        for currency in self.session.currencies:
            if currency.name == decision1:
                chosenCurrency: Currency = currency

        decision2 = input("How much it have to change?")

        chosenCurrency.changeManager.addListener(decision2, account, decision1)
