class Product:
    def __init__(self, name, price):
        self.name = name.lower()
        self.price = price 

# ========================================

from product import Product

class ShoppingCart:
    def __init__ (self):
        self.cart = {}

def addProduct (self, product, quantity):
    if product.name in self.cart:
        self.cart[product.name] ["quantity"] += quantity 
    else:
        self.cart[product.name]= {"product":product,"quantiy":quantity}
        print (f"{quantity} x {product} added to cart")

def removeProduct(self, product_name, quantity):
    product_name = product_name.lower()
    if product_name in self.cart:
        if quantity >= self.cart[product_name]["quantity"]:
            del self.cart[product_name]
            print(f"{product_name} removed from the cart.")
        else:
                self.cart[product_name] ["quantity"] -= quantity 
                print (f"{quantity} x {product_name} removed from the cart")
    else:
         print("Product not found.")

def view_cart (self):
    if not self.cart:
        print("Your cart is empty.")
        return

    print("\n===Your Cart===") 
    for item in self.cart.values():
        product = item["product"]
        quantity = item["quantity"]

    print(f"{product.name.capitalize()} - {quantity} pcs at PHP {product.price} each")

def calculate_total(self):
    total = 0
    for item in self.cart.values():
        total += item["product"].price * item["quantity"]
        print(f"You total amount is {total}")

# ==============================

from product import Product
from cart import ShoppingCart

products = {
    "apple":Product("apple",20),
    "banana":Product("banana", 10),
    "coconut":Product("coconut", 30),
    "dalandan":Product("dalandan", 40),
    "guyabano":Product("guyabano", 50)
}

cart = ShoppingCart()

def show_menu():
    print("===Menu===")
    print("[1] Show Products")
    print("[2] Add a Product")
    print("[3] Remove a Product")
    print("[4] View Cart")
    print("[5] Calculate the Total")
    print("[6] Exit")

def show_products():
    print("\n===Avaialable products===")
    for prodcut in products.values():
        print("f{product.name.capitalize()} - PHP {product.price}")

while True:
    show_menu()
    choice = input(int("Enter your choice: (1-6: "))

    if choice == 1:
        show_products()
    elif choice == 2:
        name = input("Enter product name to add").lower()
        qty = input(int("Enter how many: "))
        if name in products:
            cart.add_product(products[name], qty)
        else:
            print("Product not found")

    elif choice == 3:
        print("Enter product name to remove: ").lower()
        cart.remove_product(name,qty)
    elif choice == 4:
        cart.view_cart
    elif choice == 5:
        cart.calculate_total()
    elif choice == 6:
        print("Thank you for shopping!")
        break
    else: 
        print("Invalid choice. Please try again.")

