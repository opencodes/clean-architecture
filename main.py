# This is a sample Python script.
from interactor.bank_account_interactor import BankAccountInteractor


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    bank_ctrl = BankAccountInteractor()
    bank_output = bank_ctrl.add_bank_account({
        "id": "1",
        "acc_no": "123-456-789",
        "owner_contact_id": "c1",
        "balance": 5000,
    })
    print(bank_output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
