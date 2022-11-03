class BankAccount:
    # Attributes: Balance
    # Functions: Constructor, Get_balance, Deposit, Pay

    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self):
        print(f"Balance is {self.balance}.")

    def deposit(self, deposit_sum):
        self.balance += deposit_sum

    def pay(self, payment_sum):
        if self.balance >= payment_sum:
            self.balance -= payment_sum
            # print(self.balance)
            # print("True")
            return True
        else:
            # print("False")
            return False


class User:
    # Attributes: Username, BankAccount
    # Functions: Constructor, Deposit, Pay

    def __init__(self, username, bank_account):
        self.username = username
        self.bank_account = BankAccount(bank_account)

    def get_balance(self):
        print(f"Balance is {self.bank_account.get_balance}.")

    def deposit(self, balance):
        return self.bank_account.deposit(balance)

    def pay(self, balance):
        return self.bank_account.pay(balance)
