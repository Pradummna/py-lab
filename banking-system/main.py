from services.manager import AccountManager
from storage.io import save_accounts, load_accounts
import random

filename = "accounts.json"

def generate_account_no(length=7):
    digits = [str(random.randint(1, 9)) for _ in range(length)]
    return "".join(digits)

def input_warning():
    print("Field cannot be empty.")

def enter_acc_no():
    while True:
        acc_no = input("Enter Account no: ")
        if not acc_no:
            input_warning()
            continue
        if not acc_no.isdigit():
            print("Account number must contain only digits.")
            continue
        return acc_no

def menu():
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Find Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. View Transaction History")
    print("7. Exit")
    print("==================================")

def main():
    manager = AccountManager()
    manager.accounts = load_accounts(filename)

    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            acc_no = generate_account_no()
            while True:
                name = input("Enter Name: ").strip()
                if not name:
                    input_warning()
                    continue
                break
            
            while True:
                try:
                    print("Enter balance in decimal format (e.g. 1000.00)")
                    balance = float(input("Enter initial balance: "))
                    if balance <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Incorrect Value. Try Again")
            print(f"Your account no is: {acc_no}")
            manager.create_account(acc_no, name, balance)
            save_accounts(filename, manager.accounts)

        elif choice == "2":
            print("\nFind Account")
            acc_no = enter_acc_no()
            manager.find_account(acc_no)
            
        elif choice == "3":
            print("\nDeposit Section")
            acc_no = enter_acc_no()
            while True:
                try:
                    amount = float(input("Enter Amount in (0000.00) format: "))
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    break    
                except ValueError:
                    print("Incorrect Amount. Use this format (1000.00): ")
            manager.deposit(acc_no, amount)
            save_accounts(filename, manager.accounts)

        elif choice == "4":
            print("\nWithdraw Section")
            acc_no = enter_acc_no()
            while True:
                try:
                    amount = float(input("Enter Amount in (0000.00) format: "))
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Incorrect Amount. Use this format (1000.00): ")
            manager.withdraw(acc_no, amount)
            save_accounts(filename, manager.accounts)

        elif choice == "5":
            print("\nCheck Your Balance")
            acc_no = enter_acc_no()
            manager.get_balance(acc_no)

        elif choice == "6":
            print("\nCheck All Transactions")
            acc_no = enter_acc_no()
            manager.view_history(acc_no)

        elif choice == "7":
            print("Exiting... Accounts saved successfully.")
            break

        else:
            print("Wrong Input. Try again.")

if __name__ == "__main__":
    main()
