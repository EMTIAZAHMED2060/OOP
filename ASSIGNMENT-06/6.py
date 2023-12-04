class SultansDine:
    total_branches = 0
    total_sell = 0
    branch_list = []

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {cls.total_branches}")
        print(f"Total Sell: {cls.total_sell} Taka")

    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.branch_sell = 0
        SultansDine.total_branches += 1
        SultansDine.branch_list.append(self)

    def sellQuantity(self, quantity):
        if quantity < 10:
            self.branch_sell = quantity * 300
        elif quantity < 20:
            self.branch_sell = quantity * 350
        else:
            self.branch_sell = quantity * 400
        SultansDine.total_sell += self.branch_sell

    def branchInformation(self):
        print(f"Branch Name: {self.branch_name}")
        print(f"Branch Sell: {self.branch_sell} Taka")
        for branch in SultansDine.branch_list:
            sell_percentage = (branch.branch_sell / SultansDine.total_sell) * 100
            print(f"Branch Name: {branch.branch_name}, Branch Sell: {branch.branch_sell} Taka")
            print(f"Branch consists of total sell's: {sell_percentage:.2f}%")
        print("================================")

# Test the class
SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()


