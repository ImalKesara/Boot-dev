class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def widraw(self, amount):
        self.__balance = self.__balance - amount

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(500)
account.widraw(20)
val = account.get_balance()
print(val)
