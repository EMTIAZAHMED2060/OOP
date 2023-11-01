class Foodie:
    def __init__(self, name):
        self.name = name
        self.tot = 0
        self.items = []
        self.count = 0

    def order(self, *args):
        for orders in args:
            self.count += 1
            temp_tot = 0
            menus = orders.split('-')
            item_name = menus[0]
            quantity = int(menus[1])
            if item_name in menu:
                price_per_unit = menu[item_name]
                print(f"Ordered - {item_name}, quantity - {quantity}, price(per Unit) - {price_per_unit}")
                temp_tot += quantity * price_per_unit
                print(f"Total price - {temp_tot}")
                self.tot += temp_tot
                self.items.append(item_name)
            else:
                print(f"{item_name} is not in the menu.")

    def pay_tips(self, tips=0):
        if tips != 0:
            print(f"Gives {tips}/- tips to the waiter")
            self.tot += tips
        else:
            print("No tips to the waiter")

    def show_orders(self):
        x = ''
        x += f'{self.name} has {self.count} item(s) in the cart.\n'
        x += f'Items: {", ".join(self.items)}\n'
        x += f'Total spent: {self.tot}'
        return x

menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}


f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())
