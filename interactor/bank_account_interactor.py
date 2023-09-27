
from use_case.bank_account_use_case import BankAccountUseCase


class BankAccountInteractor:

    def __int__(self):
        pass

    def add_bank_account(self, req_body: dict):
        bank_acc = BankAccountUseCase(**req_body)
        bank_acc.deposit(5000)
        bank_acc.withdraw(100)
        return bank_acc.to_json()
