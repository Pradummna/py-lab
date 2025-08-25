from models.bank_account import BankAccount

class AccountManager:
    def __init__(self):
        self.accounts = {}
    
    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)

    def create_account(self, acc_no, name, initial_balance):
        account = self.get_account(acc_no)
        if account is not None:
            print(f"Account no: {acc_no} already exists. Try another one.")
            return
        account = BankAccount(acc_no, name, initial_balance)
        self.accounts[acc_no] = account
        print(f"Account {acc_no} created successfully.")

    def find_account(self, acc_no):
        account = self.get_account(acc_no)
        if account is None:
            print("Account not found.")
            return
        print("---- Account Details ----")
        print(f"Account No   : {account.acc_no}")
        print(f"Account Name : {account.get_account_details()}")

    def deposit(self, acc_no, amount):
        account = self.get_account(acc_no)
        if account is None:
            print("Account not found.")
            return
        account.deposit(amount)
        print(f"Deposited {amount} to {acc_no}.")

    def withdraw(self, acc_no, amount):
        account = self.get_account(acc_no)
        if account is None:
            print("Account not found.")
            return
        if account.withdraw(amount):
            print(f"Withdrawn {amount} from {acc_no}.")

    def get_balance(self, acc_no):
        account = self.get_account(acc_no)
        if account is None:
            print("Account not found.")
            return   
        print(f"Balance for {acc_no}: {account.get_balance()}")

    def view_history(self, acc_no):
        account = self.get_account(acc_no)
        if account is None:
            print("Account not found.")
            return
        print("---- Transaction History ----")
        for transaction in account.transactions:
            print(transaction)
