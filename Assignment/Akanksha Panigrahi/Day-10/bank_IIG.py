class InsufficientFundError(Exception):
    def __init__(self):
        print("Insufficient Balance!!!")
class BankAccount:
    def __init__(self, name, accountno):
        self.name= name
        self.accountno=accountno
        self.balance=0
    def show(self):
        print("NAME OF THE DEPOSITER:",(self.name))
        print("ACCOUNT NUMBER:",(self.accountno))
    def deposit(self,amount):
        self.balance+=amount
        print("Amt Deposited successfully!!")
    def withdraw (self,amount):
        try:
            if amount> self.balance:
                raise InsufficientFundError()
            else:
                self.balance-=amount
                print(f"{amount} withdrawed from account!!")
                print(f"Current Balance:{self.balance}")
        except InsufficientFundError:
            print("Account has no enough money as demanded!!")
holder1 = BankAccount('Akanksha', 10000)
holder1.show()
holder1.deposit(1000)
holder1.withdraw(500000)