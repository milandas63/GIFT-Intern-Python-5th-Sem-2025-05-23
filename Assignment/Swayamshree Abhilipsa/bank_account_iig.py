class InsufficientFundsError(Exception):
    def __init__(self):
        print("Insufficient balance")

class bank_account:
    def __init__(self, name, acc_no):
        self.name, self.acc_no, self.balance = name, acc_no, 0
    def show(self):
        print(f"NAME : {self.name}")
        print(f"ACC_NO : {self.acc_no}")
    def deposite(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited successfully !")
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFundsError()
            else:
                self.balance = self.balance - amount
                print(f"{amount} withdrawed from account !")
                print(f"Current Balance : {self.balance}")
        except InsufficientFundsError:
            print("Asked amount is not available !")

acc_holder1 = bank_account('Kasturi', 123456)
acc_holder1.show()
acc_holder1.deposite(500)
acc_holder1.withdraw(1000)





    

