from interfaces.CurrencyListenerInterface import CurrencyListenerInterface
from classes.CurrencyListener import CurrencyListener
from classes.Account import Account
from db import db

class ChangeManager:
    def __init__(self, name):
        self.currencyListenerList = self.start(name) #id keeper

    def start(self, name):
        currency = db.currencies.find({"name": name})[0]
        #listeners = [listener for listener in currency.changeManager]
        listeners = []
        try:
            for manager_id in currency["changeManager"]:
                manager = db.changeManager.find({"_id": manager_id})[0]
                accounts = []
                for account_id in manager["listenersList"]:
                    accounts.append(account_id)
                listeners.append(CurrencyListener(manager["rate"], accounts))

            return listeners
        except:
            return []


    def addListener(self, change, account: Account, name):
        for listener in self.currencyListenerList:
            if listener.changeRate == change:
                listener.addAccount(account)
                return 0

        self.currencyListenerList.append(CurrencyListener(change))
        account_id = db.accounts.find({"_id": account.accountID})[0]
        print(type(account_id["_id"]))
        manager = db.changeManager.insert_one({"rate": float(change), "listenersList": [account_id["_id"]]})
        result = db.currencies.update({"name": name}, {'$push': {"changeManager": manager.inserted_id}})
        return 1

    def changeNotify(self, change, name):
        # currency = db.currencies.find({"name": name})[0]
        # managerList = []
        # for manager_id in currency["changeManager"]:
        #     manager = db.changeManager.find({"_id": manager_id})[0]
        #     managerList.append(manager)
        #
        #     if manager["rate"] == float(change):
        #         print(manager["rate"])
        #         for account_id in manager["listenersList"]:
        #             listener.showMessage(name)
        for listener in self.currencyListenerList:
            if float(listener.changeRate) == float(change):
                listener.showMessage(name)
            # for listener in manager["listenersList"]:
            #     listenerList = db.changeManager.find({"_id": listener})
            #     for manager in listenerList:

