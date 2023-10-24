class Store:
    
    def __init__(self, balance):
        print("New branch created!")
        self.balance = balance
        self.total_items = {}
        
    def viewAllItems(self):
        if self.total_items == {}:
            print("There are no items in your inventory")
        else:
            print('All items',(',').join(self.total_items.keys()))
    def viewAllItemDetails(self):
        print(self.total_items)
    def add_item(self,lista):
        temp = {}
        temp['stock'] = lista[1]
        temp['buying_price'] = lista[2]
        temp['selling_price'] = lista[3]
        self.balance -= lista[1]*lista[2]
        
        if lista[0] not in self.total_items:
            print('Item added', lista[0])
            self.total_items[lista[0]] = temp
            
    def sell_item(self,name,quan):
        if self.total_items[name]['stock'] < quan:
            print(f"Sorry! {name} is not available at your desired quantity. Currently we have: {self.total_items[name]['stock']}")
        else:
            self.total_items[name]['stock'] -= quan
            self.balance += self.total_items[name]['selling_price']*quan
            
    def restock_item(self,name, buy):
        self.total_items[name]['stock'] += buy
        self.balance -= self.total_items[name]['buying_price']*buy


print("==========================")
branch1 = Store(5000)
print(f"Current Balance: {branch1.balance}")
print(f"Total items: {branch1.total_items}")
branch1.viewAllItems()
branch1.viewAllItemDetails()
print("==========================")
print(f"Current Balance: {branch1.balance}")
branch1.add_item(["ChaCha Noodles", 10, 5, 8])
print(f"Current Balance: {branch1.balance}")
branch1.add_item(["Sparrow Shampoo", 5, 10, 20])
print(f"Current Balance: {branch1.balance}")
print("==========================")
branch1.viewAllItems()
print()
branch1.viewAllItemDetails()
print()
print("==========================")
print(f"Current Balance: {branch1.balance}\n")
branch1.sell_item("ChaCha Noodles", 15)
print(f"Current Balance: {branch1.balance}\n")
branch1.viewAllItemDetails()
print()
branch1.sell_item("ChaCha Noodles", 10)
print()
print(f"Current Balance: {branch1.balance}\n")
branch1.viewAllItemDetails()
print()
print("==========================")
print(f"Current Balance: {branch1.balance}\n")
branch1.restock_item("ChaCha Noodles", 5)
print()
branch1.viewAllItemDetails()
print()
print(f"Current Balance: {branch1.balance}\n")
print("==========================")