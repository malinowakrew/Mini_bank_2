from interfaces.builderInterface import buildInterface
from classes.User import User
from classes.Wallet import Wallet
from classes.Account import Account
from classes.Oversee import Oversee

from db import db
from bson.objectid import ObjectId

class BuildNormalAccount(buildInterface):
    def buildUser(self, accountID):
        accountDB = db.accounts.find_one({'_id': accountID})

        userDB = db.users.find_one({"_id": (accountDB['user'])['id']})
        return User(userDB["name"], userDB["surname"], userDB["_id"])

    def buildWallets(self, accountID):
        wallets = []
        accountDB = db.accounts.find_one({"_id": accountID})
        for walletDB in accountDB["wallets"]:
            wallet = db.wallets.find_one({"_id": walletDB['id']})
            currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})

            wallets.append(Wallet(wallet['founds'], currencyName['name'], wallet['_id']))
        return wallets

    def buildMainWallet(self, accountID):
        accountDB = db.accounts.find_one({"_id": accountID})
        walletDB = accountDB['wallets'][0]
        wallet = db.wallets.find_one({"_id": walletDB['id']})
        currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})
        return (Wallet(wallet['founds'], currencyName['name'], wallet['_id']))

    def buildMessages(self, accountID):
        accountDB = db.accounts.find_one({"_id": accountID})
        messagesDB = accountDB['messages']
        return messagesDB

    def reset(self):
        pass

class BuildOverseeAccount(buildInterface):
    def buildUser(self, accountID):
        accountDB = db.accounts.find_one({'_id': accountID})

        userDB = db.users.find_one({"_id": (accountDB['user'])['id']})
        return User(userDB["name"], userDB["surname"], userDB["_id"])

    def buildWallets(self, accountID):
        pass

    def buildMainWallet(self, accountID):
        pass

    def reset(self):
        pass
    """
    def buildWallets(self, accountID):
        wallets = []
        accountDB = db.accounts.find_one({"_id": accountID})
        for walletDB in accountDB["wallets"]:
            wallet = db.wallets.find_one({"_id": walletDB['id']})
            currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})

            wallets.append(Wallet(wallet['founds'], currencyName['name'], wallet['_id']))
        return wallets

    def buildMainWallet(self, accountID):
        accountDB = db.accounts.find_one({"_id": accountID})
        walletDB = accountDB['wallets'][0]
        wallet = db.wallets.find_one({"_id": walletDB['id']})
        currencyName = db.currencies.find_one({'_id': (wallet['currency'])['id']})
        return (Wallet(wallet['founds'], currencyName['name'], wallet['_id']))

    def reset(self):
        pass
    """

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> buildInterface:
        return self._builder

    @builder.setter
    def builder(self, builder: buildInterface) -> None:
        self._builder = builder

    def makeAccount(self, ID):
        user = self._builder.buildUser(ID)
        wallets = self._builder.buildWallets(ID)
        mainWallet = self._builder.buildMainWallet(ID)
        messages = self._builder.buildMessages(ID)

        account: Account = Account(ID, user, wallets, mainWallet, messages)
        return account

    def makeOversee(self, ID):
        user = self._builder.buildUser(ID)
        #wallets = self._builder.buildWallets(ID)
        #mainWallet = self._builder.buildMainWallet(ID)

        account: Oversee = Oversee(ID, user)
        return account


"""
if __name__ == "__main__":
    director = Director()
    builder = BuildOverseeAccount()
    director.builder = builder


    ac = director.makeOversee(ObjectId("5fba5496d969c7f2def41484"))
    print(ac.showUsersInterface())
"""