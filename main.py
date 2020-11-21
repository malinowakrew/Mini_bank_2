# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.Wallet import *
from classes.Account import *
from classes.Session import *
from datetime import datetime

def print_hi(name):
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
    while(run):
        print("Menu\n"
              "1. Show currencies\n"
              "2. Log in\n"
              "3. Create account\n"
              "4. Stop\n")
        choose = int(input("Type numer from menu: "))

        if(choose == 4):
            run = False
        elif (choose == 3):
            session.createAccountInterface()
        elif (choose == 2):

            # sesja.show()
            # result = db.wallets.insert_one({"currency": "złoty", "founds": 17})
            # sesja.createAccountInterface()
            A = session.logInInterface()
            A.addMoneyInterface()
        elif (choose == 1):
            pass
        else:
            print("Try to choose one more time")
    """
    A = sesja.logIn("EdytaMroz", "123")
    for wallet in A.wallets:
        print(wallet.getFounds())
    #print(lambda wall: )
    dic = sesja.calculateBalance("złoty")

    A.show()

    for i in dic:
        print(f"Za 1 {'złoty'} możesz otrzymać {dic[i]} {i}")

    lista_c = sesja.getCurrencies()

    A.addMoney(78)
    for c in lista_c:
        if c.name == "frank":
            A.addWallet(c)
            A.transfer(7, c)
    print("Przed")
    A.show()

    print("Po")
    A.pay(2, "frank")
    A.show()
    
    print("main")
    print(A.mainWallet.getFounds())
    A.addMoney(89.0)
    A.show()
    
    konto = Account("lol")
    for wal in konto.wallets:
        print(wal.getFounds())
    """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
