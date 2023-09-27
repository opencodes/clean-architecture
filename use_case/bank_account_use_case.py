import json

from entitiy.bank_account import BankAccount


class BankAccountUseCase:
    bank_account: BankAccount

    def __init__(self, id, acc_no, owner_contact_id, balance):
        self.bank_account = BankAccount(id, acc_no, owner_contact_id, balance)
        print(self.bank_account)

    def get_bank_account(self):
        return self.bank_account

    def deposit(self, amount):
        bal = self.bank_account.balance
        self.bank_account.set_balance(bal + amount)

    def withdraw(self, amount):
        bal = self.bank_account.balance
        self.bank_account.set_balance(bal - amount)

    def to_json(self):
        return json.dumps(self.bank_account, default=lambda o: o.__dict__)
