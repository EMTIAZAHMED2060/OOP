class Shopidify:
    def __init__(self, account_type="Guest"):
        self.account_type = account_type
        self.cart = {}
        self.history = []

        if account_type == "Guest":
            print(f"Welcome to Shopidify {account_type}")
        else:
            print(f"Welcome {account_type} to Shopidify")

    def add_to_cart(self, *items):
        for item in items:
            if isinstance(item, str):
                self.cart[item] = self.cart.get(item, 0) + 1
            elif isinstance(item, list):
                for i in range(0, len(item), 2):
                    self.cart[item[i]] = self.cart.get(item[i], 0) + item[i + 1]

    def display_cart(self):
        if self.account_type == "Guest":
            print(f"Items in the cart for Guest:")
        else:
            print(f"Items in the cart for {self.account_type}:")

        for item, quantity in self.cart.items():
            print(f"- {item}: {quantity}x")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Add items to the cart first.")
            return

        self.history.append(self.cart.copy())
        self.cart.clear()
        print(f"Checkout completed for {self.account_type}")

    def display_history(self):
        print(f"Purchase history for {self.account_type}:")

        for i, transaction in enumerate(self.history, 1):
            print(f"Transaction {i}:")
            for item, quantity in transaction.items():
                print(f"- {item}: {quantity}x")

# Test the Shopidify class
guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")