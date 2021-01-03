# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.Wallet import *
#from classes.Account import *
from classes.Session import *
from classes.Oversee import *

def user (account,
         session: SessionClient) -> None:

    run = True
    while run:
        print("Menu\n"
              "1. Show currencies\n"
              "2. Account balance\n"
              "3. Pay\n"
              "4. Add money\n"
              "5. Log out\n"
              "6. Exchange money\n"
              "7. Messages\n"
              "8. Subscribe currency\n")
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
        elif choose == 7:
            account.showMessages()
        elif choose == 8:
            session.subscribeCurrency(account)

    return 0


def oversee(account, session):
    run = True
    while run:
        decision = input("Do you want to change currency?")
        if decision == "YES":
            account.changeCurrencyRate()

        account.showUsersInterface()
        chose = input("You want to check something else?")

        if (chose != "YES"):
            #czy ja tego potrzebuję?
            chose = input("You want to use your private account?")
            if chose == "YES":
                run = False
                print("Log into your normal account")
                account = session.logInInterface()
                if account == None:
                    raise LogError
                user(account, session)
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
    implementacja = Session()
    session = SessionClient(implementacja)
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
            if type(account) == Oversee:
                oversee(account, session)
            else:
                user(account, session)

        elif choose == 1:
            session.BalanceInterface()
        else:
            print("Try to choose one more time")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
