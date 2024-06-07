class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def remove_item(self, name):
        for item in self.cart:
            if item.name == name:
                self.cart.remove(item)
                return True
        return False

    def view_cart(self):
        for item in self.cart:
            print(item)

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item.price * item.quantity
        return total

    def clear_cart(self):
        self.cart.clear()

cart = ShoppingCart()
cart.add_item(Item("Laptop", 999.99, 1))
cart.add_item(Item("Mouse", 19.99, 2))

print("Items in the cart:")
cart.view_cart()

print("\nTotal cost:")
print(cart.calculate_total())

print("\nRemove Mouse:")
cart.remove_item("Mouse")
cart.view_cart()

print("\nClear cart:")
cart.clear_cart()
cart.view_cart()
