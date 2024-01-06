class Product:
    def __init__(self, product_id, name, price, quantity_available, discount_percentage=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_available = quantity_available
        self.discount_percentage = discount_percentage

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * (percentage/100))
    
    def __str__(self):
        return f"{self.name}"

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = []
        self.purchasedProduct = []

    def __str__(self):
        return f"Products Purchased: {self.purchasedProduct}"


    def add_to_cart(self, newProduct):
        isInCart = False
        for product in self.cart:
            if product.product_id == newProduct.product_id:
                isInCart = True
                break
        if isInCart == False:
            self.cart.append(newProduct)
    
    def calculate_cart_total(self):
        totalValue = 0
        for product in self.cart:
            totalValue += product.price
        return totalValue

def process_order(customer, inventoryList):
    for product in inventoryList:
        if product in customer.cart:
            if product.quantity_available > 0:
                product.quantity_available -= 1
                customer.cart.remove(product)
                customer.purchasedProduct.append(product)
    customer.cart = []

def display_order_summary(customer):
    totalAmount = 0
    for product in customer.cart:
        totalPrice = product.price * product.quantity_available
        totalAmount += totalPrice
    
    print(f"Customer ID: {customer.customer_id}, Customer Name: {customer.name}, Customer Email: {customer.email}")
    print(f"Products Purchased: ", end='')
    for purchase in customer.purchasedProduct:
        print(purchase," ", end='')
    print("\n")
    for product in customer.purchasedProduct:
        print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}")
    print("Total Amount: ", totalAmount)



product1 = Product(product_id=1, name="Laptop", price=1200, quantity_available=10)
product2 = Product(product_id=2, name="Printer", price=300, quantity_available=8)

inventory_list = [product1, product2]

customer = Customer(customer_id=1, name="Alice", email="alice@example.com")

customer.add_to_cart(product1)
customer.add_to_cart(product2)

print(product1.apply_discount(10))

cart_total = customer.calculate_cart_total()
print("Cart Total: ", cart_total)

process_order(customer, inventory_list)

display_order_summary(customer)




