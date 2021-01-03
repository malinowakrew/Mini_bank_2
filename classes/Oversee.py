from db import db
from classes.Account import Account
from classes.User import User

from bson.objectid import ObjectId

from interfaces.oversee import OverseeInterface
#from classes.Builders import *
from classes.Currency import Currency

class Oversee(OverseeInterface): #Account):
    """
    def __init__(self, ID)->None:
        super().__init__(ID)
        pass
    """
    def __init__(self, ID, user)-> None:
        #super().__init__(ID, user, wallets, mainWallet)
        self.accountID = ObjectId(ID)
        self.user = user


    def userData(self):
        users = []
        userDB = db.users.find()

        for user in userDB:
            users.append(User(user["name"], user["surname"], user["_id"]))

        return users

    def userWallets(self, user: User):
        accountDB = db.accounts.find_one({"user": {'ref': 'user', 'id': ObjectId(user.userID), 'db': 'users'}})
        print(f"\nNick: {accountDB['nick']}")
        """
        director = Director()
        builder = BuildOverseeAccount()
        director.builder = builder

        userAccount = director.makeOversee(accountDB['_id'])

        userAccount.showInterface()
        """

    #Interfaces
    def showUsersInterface(self):
        userList = self.userData()
        for number, user in enumerate(userList):
            userData = user.getData()
            print(f"{number+1}. {userData['ID']}: {userData['surname']} {userData['name']}")

        chose = int(input("Choose number of user whoch you want to show wallets details: "))

        chosenUser = userList[chose-1]

        self.userWallets(chosenUser)

    def changeCurrencyRate(self):
        currencyName = input("Currency name: ")
        currencyDB = db.currencies.find({"name": currencyName})[0]
        currency = Currency(currencyDB.get('name'), currencyDB.get('rate'), currencyDB.get('_id'))
        change = input("How much: ")
        currency.changeRate(change)

"""
def main():
    oversee = Oversee()
    oversee.showUsersInterface()


if __name__ == "__main__":
    main()
    
"""