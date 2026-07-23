class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    def display_info(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self._balance)

acc1 = BankAccount("Abdullah", 60000)
acc2 = BankAccount("Ali", 80000)

print(acc1._balance)
print(acc2._balance)

acc1.display_info()
acc2.display_info()