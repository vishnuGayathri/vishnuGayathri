class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount} into the account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew {amount} from the account.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Holder Name: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: {self.__account_balance}")

# Create an instance of the BankAccount class
bank_account = BankAccount("123456789", "Taehyung")

# Test deposit and withdrawal functionality
bank_account.deposit(1000)
bank_account.display_balance()

bank_account.withdraw(500)
bank_account.display_balance()