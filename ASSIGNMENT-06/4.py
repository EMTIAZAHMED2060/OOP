class NikeBangladesh:
    branches = []
    stocked = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    sold = 0

    @classmethod
    def status(cls):
        print('Nike Bangladesh Status:')
        print(f'Branches Opened:  {cls.branches}\nCurrently Stocked {cls.stocked}\nSold: {cls.sold}')

    def __init__(self, name):
        NikeBangladesh.branches.append(name)
        self.name = name
        self.branch_stocked = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        self.branch_sold = 0

    def details(self):
        print(f'{self.name} outlet:')
        print(f'Products Currently Stocked: {self.branch_stocked}\nSold: {self.branch_sold}')

    def restock_products(self, product):
        for item, quantity in product.items():
            NikeBangladesh.stocked[item] += quantity
            self.branch_stocked[item] += quantity

    def product_sold(self, product):
        for item, quantity in product.items():
            NikeBangladesh.stocked[item] -= quantity
            self.branch_stocked[item] -= quantity
            NikeBangladesh.sold += quantity
            self.branch_sold += quantity


print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restock_products(
    {"Air Jordan": 1200, "Cortez": 200, "Zoom Kobe": 200})
chittagong.restock_products(
    {"Air Jordan": 1000, "Cortez": 250, "Zoom Kobe": 100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.product_sold({"Air Jordan": 760, "Cortez": 90})
chittagong.product_sold({"Air Jordan": 520, "Zoom Kobe": 70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()