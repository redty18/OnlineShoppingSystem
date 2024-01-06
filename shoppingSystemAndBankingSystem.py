class Product:
    def __init__(self, product_id, name, price, quantity_available, category, discount_percentage=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_available = quantity_available
        self.discount_percentage = discount_percentage
        self.category = category

    def __str__(self):
        print(f"Product ID: {self.product_id}, Product Name: {self.name}, Product Price: {self.price}, Product Quantity: {self.quantity_available}")

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * (percentage/100))
        return self.price
    
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = []
        self.purchasedProduct = []
    
    def __str__(self):
        print(f"Customer ID: {self.customer_id}, Customer Name: {self.name}, Customer Email: {self.email}")

    def add_to_cart(self, product):
        self.cart.append(product)

    def calculate_cart_value(self):
        totalValue = 0
        for items in self.purchasedProduct:
            totalValue += items.price
        return totalValue

class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def __str__(self):
        print(f"Account Number: {self.account_number}, Account Holder Name: {self.account_holder_name}, Balance: {self.balance}")
    
    def deposit(self, account, money):
        for items in account:
            items.balance = items.balance + money
        return
    
    def withdraw(self, account, money):
        for items in account:
            if items.balance < money:
                print("Insufficient Funds, withdraw a lesser amount.")
            else:
                items.balance = items.balance - money
    
class BankCustomer():
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.accounts = []

    def __str__(self):
        print(f"Customer ID: {self.customer_id}, Customer Name: {self.name}, Customer Email: {self.email}")
    
    def open_account(self, newAccount):
        self.accounts.append(newAccount)

    def close_account(self, existingAccount):
        if existingAccount in self.accounts:
            self.accounts.remove(existingAccount)
        else:
            print("This account doesn't exist.")

    def display_bank_accounts(self):
        print(f"Customer ID: {self.customer_id}, Customer Name: {self.name}")
        print(f"Bank Accounts: ", end='')
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.balance}")

def purchase_with_bank_account(customer, bankCustomer, product, quantity):
    totalPurchaseAmount = product.price * quantity

    if totalPurchaseAmount < bankCustomer.accounts[0].balance:
        bankCustomer.accounts[0].balance = bankCustomer.accounts[0].balance - totalPurchaseAmount
    else:
        print("Insufficient Funds.")

    if product.quantity_available != 0:
        product.quantity_available = product.quantity_available - quantity
        customer.cart.remove(product)
        customer.purchasedProduct.append(product)
    else:
        print("No Products Left.")
    
def display_combined_summary(customer):
    print(f"Customer ID: {customer.customer_id}, Customer Name: {customer.name}, Customer Email: {customer.email}")
    print("\nBank Accounts: ", end='')
    for account in customer.accounts:
        print(f"Account Number: {account.account_number}, Account Holder: {account.account_holder_name}, Balance: {account.balance}")
    print("\nShopping Cart: ", end='')
    for item in customer.purchasedProduct:
        print(f"Product ID: {item.product_id}, Product Name: {item.name}, Product Price: {item.price}")
    print(f"Total Spending: {customer.calculate_cart_value()}")


product1 = Product(product_id=1, name="Laptop", price=1200, quantity_available=5, discount_percentage=10, category="Electronics")
product2 = Product(product_id=2, name="Book", price=20, quantity_available=20, category="Books")


# Create a customer object
customer = Customer(customer_id=1, name="Alice", email="alice@example.com")


# Add products to the customer's cart
customer.add_to_cart(product1)
customer.add_to_cart(product2)


# Create a bank customer object
bank_customer = BankCustomer(customer_id=1, name="Alice", email="alice@example.com")


# Open a bank account for the customer
account1 = Account(account_number=101, account_holder_name="Alice", balance=1500)
bank_customer.open_account(account1)


# Display customer's shopping cart and bank account details before the purchase
print("Before Purchase:")
print("Shopping Cart Total:", customer.calculate_cart_value())
bank_customer.display_bank_accounts()


# Purchase with bank account
purchase_with_bank_account(customer, bank_customer, product1, quantity=1)


# Display customer's shopping cart and bank account details after the purchase
print("\nAfter Purchase:")
print("Shopping Cart Total:", customer.calculate_cart_value())
bank_customer.display_bank_accounts()
    
    


    


