class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder, balance=0):
        account = Account(account_number, account_holder, balance)
        self.accounts.append(account)
        return account

    def list_accounts(self):
        for account in self.accounts:
            print(account)

# Example usage
bank = Bank()
bank.create_account("123456789", "Alice", 1000)
bank.create_account("987654321", "Bob", 500)

print("All accounts:")
bank.list_accounts()

print("\nDeposit 200 to Alice's account:")
account = bank.accounts[0]
account.deposit(200)
bank.list_accounts()

print("\nWithdraw 300 from Bob's account:")
account = bank.accounts[1]
account.withdraw(300)
bank.list_accounts()
 
