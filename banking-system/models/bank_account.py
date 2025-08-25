from datetime import datetime

class BankAccount:
    def __init__(self, acc_no, name, initial_balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = initial_balance
        self.transactions = []
        self.add_transaction("create", initial_balance)

    def add_transaction(self, type, amount):
        current_datetime = datetime.now()
        ts = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "ts": ts,
            "type": type,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(transaction)

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction("deposit", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        self.add_transaction("withdraw", amount)
        return True
    
    def get_account_details(self):
        return self.name

    def get_balance(self):
        return self.balance
    
    def to_dict(self):
        return {
            "account_no": self.acc_no, 
            "name": self.name, 
            "balance": self.balance, 
            "transactions": self.transactions 
        }
