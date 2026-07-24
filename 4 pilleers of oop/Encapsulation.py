class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Account No.", self.account_no, "has debited Rs", amount)
            print("Total amount in account is", self.get_balance())

    def credit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Account No.", self.account_no, "has credited Rs", amount)
            print("Total amount in account is", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)

print("Balance:", acc1.get_balance())
print("Account No:", acc1.account_no)

acc1.debit(1000)
acc1.credit(50000)
acc1.debit(5000)

acc1.debit(100000)   
acc1.credit(-500)    