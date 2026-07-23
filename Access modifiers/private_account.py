class bank_account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

acc1 = bank_account("hamza", 60000)
# print(acc1.__balance)
print(acc1._bank_account__balance)
