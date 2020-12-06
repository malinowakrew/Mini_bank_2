# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.Wallet import *
from classes.Account import *
from classes.Session import *
from datetime import datetime
from classes.Oversee import *

def user (account: Account,
         session: Session) -> None:
    if type(account) == Oversee:
        chose = input("You want to use yout administrator account?")
        if chose == "YES":
            run = True
            print("Administartor Account")
        else:
            run = False
            print("Normaln user Account")
        while run:
            account.showUsersInterface()
            chose = input("You want to check something else?")

            if (chose != "YES"):
                chose = input("You want to use your private account?")
                if chose == "YES":
                    run = False
                    print("Normal user Account")
                else:
                    return 0
    run = True
    while run:
        print("Menu\n"
              "1. Show currencies\n"
              "2. Account balance\n"
              "3. Pay\n"
              "4. Add money\n"
              "5. Log out\n"
              "6. Exchange money\n")
        choose = int(input("Type numer from menu: "))

        if choose == 5:
            run = False
        elif choose == 4:
            account.addMoneyInterface()
        elif choose == 3:
            account.payInterface()
        elif choose == 2:
            account.BalanceInterface()
        elif choose == 1:
            session.BalanceInterface(account)
        elif choose == 6:
            session.depositSessionInterface(account)

    return 0

def oversee(account: Oversee):
    run = True
    while run:
        account.showUsersInterface()
        chose = input("You want to check something else?")

        if (chose != "YES"):
            chose = input("You want to use your private account?")
            if chose == "YES":
                run = False
                print("Normal user Account")
            else:
                return 0

def main() -> None:
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    """
    ac = Account("pass")
    ac.walletsInit()
    po = Wallet(0.9292, "frank")
    try:
        po.pay(69)
    except NotEnoughFounds as e:
        print(e)

    result = db.currencies.insert_one({"name": "frank",
                                    "rate": 18,
                                       "date": datetime.now()})



    result = db.accounts.insert_one({"name": "złoty",
                                       "date": datetime.now()})

    """
    session = Session()
    run = True
    while run:
        print("Menu\n"
              "1. Show currencies\n"
              "2. Log in\n"
              "3. Create Account\n"
              "4. Stop\n")

        choose = int(input("Type numer from menu: "))

        if choose == 4:
            run = False
        elif choose == 3:
            session.createAccountInterface()
        elif choose == 2:
            run = False
            account = session.logInInterface()
            if account == None:
                raise LogError
            user(account, session)

        elif choose == 1:
            session.BalanceInterface()
        else:
            print("Try to choose one more time")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
