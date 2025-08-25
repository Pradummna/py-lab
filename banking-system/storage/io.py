import json
import os
from models.bank_account import BankAccount

def save_accounts(file_name, accounts):
    data = {}
    for acc_no, account in accounts.items():
        data[acc_no] = account.to_dict()

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Accounts saved to {file_name}")

def load_accounts(file_name):
    if not os.path.exists(file_name):
        print("No existing accounts file found. Starting fresh.")
        return {}
    
    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        accounts = {}
        for acc_no, acc_data in data.items():
            account = BankAccount(
                acc_no,
                acc_data['name'],
                acc_data['balance']
            )
            # restore transactions too
            account.transactions = acc_data.get("transactions", [])
            accounts[acc_no] = account    

        print(f"Loaded {len(accounts)} accounts from {file_name}")
        return accounts

    except (json.JSONDecodeError, KeyError):
        print("Error: Corrupted accounts file. Starting fresh.")
        return {}
