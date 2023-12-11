

class SultansDine:
    total_branches = 0
    total_sell = 0
    branch_list = []

    def __init__(self, branch_name):
        self.branch = branch_name
        SultansDine.total_branches += 1

    def sell_quantity(self, quantity):
        if quantity < 10:
            self.sell = quantity * 300
        elif quantity < 20:
            self.sell = quantity * 350
        else:
            self.sell = quantity * 400
        SultansDine.total_sell += self.sell

    def branch_information(self):
        print(f"Branch Name: {self.branch}\nBranch Sell: {self.sell} Taka")
        SultansDine.branch_list.append(self)
        
    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {cls.total_branches}\nTotal Sell: {cls.total_sell} Taka")
        for branch in cls.branch_list:
            print(f"Branch Name: {branch.branch}, Branch Sell: {branch.sell} Taka\nBranch consists of total sell's: {round((branch.sell/cls.total_sell)*100,2)}%")

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sell_quantity(25)
dhanmondi.branch_information()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sell_quantity(15)
baily_road.branch_information()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sell_quantity(9)
gulshan.branch_information()
print('-----------------------------------------')
SultansDine.details()
