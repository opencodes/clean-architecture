from entitiy.account_interface import Account


class BankAccount(Account):
    balance: float

    def __init__(self, id, account_number, name, balance):
        self.id = id
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_acc_no(self):
        return self.account_number

    def set_acc_no(self, account_number):
        self.account_number = account_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
