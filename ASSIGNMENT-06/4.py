class NikeBangladesh:
    bch = []
    stk = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    sd = 0

    @classmethod
    def status(cls):
        print('Nike Bangladesh Status:')
        print(f'Branches Opened:  {cls.bch}\nCurrently Stocked {cls.stk}\nSold: {cls.sd}')

    def __init__(self, name):
        NikeBangladesh.bch.append(name)
        self.name = name
        self.bstk = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        self.branch_sold = 0

    def details(self):
        print(f'{self.name} outlet:')
        print(f'Products Currently Stocked: {self.bstk}\nSold: {self.branch_sold}')

    def restock_products(self, product):
        for item, qun in product.items():
            NikeBangladesh.stk[item] += qun
            self.bstk[item] += qun

    def product_sold(self, product):
        for item, quan in product.items():
            NikeBangladesh.stk[item] -= quan
            self.bstk[item] -= quan
            NikeBangladesh.sd += quan
            self.branch_sold += quan


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