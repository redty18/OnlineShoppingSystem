class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder Name: {self.account_holder_name}, Balance: {self.balance}"

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money >= self.balance:
            print("You do not have enough money to withdraw.")
        else:
            self.balance -= money

class Customer:
    def __init__(self, customer_id, name, accounts):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
    
    def __str__(self):
        return f"{self.accounts}"

    def open_account(self, newAccount):
        self.accounts.append(newAccount)
    
    def close_account(self, existingAccount):
        if existingAccount in self.accounts:
            self.accounts.remove(existingAccount)
        else:
            print("This account doesn't exist")
    
    def display_accounts(self):
        print(f"Customr ID: {self.customer_id}, Customer Name: {self.name}")
        print("Accounts Availale: ", end='')
        for accounts in self.accounts:
            print(accounts)

def transfer_funds(withdrawFromAccount, depositToAccount, amount):
    if amount > withdrawFromAccount.balance:
        print("Transfer denied, insufficient funds available.")
    else:
        withdrawFromAccount.balance = withdrawFromAccount.balance - amount
        depositToAccount.balance = depositToAccount.balance + amount
        print(withdrawFromAccount)
        print(depositToAccount)

def calculate_total_balance(accounts):
    totalBalance = 0
    for account in accounts:
        totalBalance += account.balance
    return totalBalance

account1 = Account(account_number=1, account_holder_name="Bob", balance=10000)
account2 = Account(account_number=2, account_holder_name="Alice", balance=5000)

transfer_funds(account1, account2, 5000)
