from interfaces.CurrencyListenerInterface import CurrencyListenerInterface
from classes.Account import Account
from db import db


class CurrencyListener(CurrencyListenerInterface):
    def __init__(self, changeRate, accountList):
        self.changeRate = changeRate
        self.accountList = accountList

    def showMessage(self, currency):
        message = f"Currency that you have been following {currency} change rate about {self.changeRate}"
        for account in self.accountList:
            print(account)
            #account.addMessage(f"Currency that you have been following {currency} change rate about {self.changeRate}")
            result = db.accounts.update({"_id": account}, {"$push": {"messages": message}})

    def addAccount(self, account: Account, name):
        self.accountList.append(account)
        #result = db.currencies.update({"name": name}, {'$push': {"changeManager": account_id["_id"]}})


