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
    sesja = Session()
    #sesja.show()
    #result = db.wallets.insert_one({"currency": "złoty", "founds": 17})
    #sesja.createAccount("EdytaM", "123", "Adaś", "Lubaniecki", "złoty")
    A = sesja.logIn("EdytaM", "123")
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
        if c.name == "dolar":
            A.transfer(7, c)
    A.show()
    """
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
