# Write your code here

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
Output:
Total Number of branch(s): 0
Total Sell: 0 Taka
#################################        
Branch Name: Dhanmondi
Branch Sell: 10000 Taka
-----------------------------------------       
Total Number of branch(s): 1
Total Sell: 10000 Taka
Branch Name: Dhanmondi, Branch Sell: 10000 Taka 
Branch consists of total sell's: 100.00%        
================================
Branch Name: Baily Road
Branch Sell: 5250 Taka
-----------------------------------------       
Total Number of branch(s): 2
Total Sell: 15250 Taka
Branch Name: Dhanmondi, Branch Sell: 10000 Taka 
Branch consists of total sell's: 65.57%
Branch Name: Baily Road, Branch Sell: 5250 Taka 
Branch consists of total sell's: 34.43%
================================
Branch Name: Gulshan
Branch Sell: 2700 Taka
-----------------------------------------       
Total Number of branch(s): 3
Total Sell: 17950 Taka
Branch Name: Dhanmondi, Branch Sell: 10000 Taka 
Branch consists of total sell's: 55.71%
Branch Name: Baily Road, Branch Sell: 5250 Taka 
Branch consists of total sell's: 29.25%
Branch Name: Gulshan, Branch Sell: 2700 Taka    
Branch consists of total sell's: 15.04%

Subtaks:
Create SultansDine class
Create 2 class variable and 1 class list
Create 1 class method
Calculation of branch sell is given below
If sellQuantity < 10:
Branch_sell = quantity * 300
Else if sellQuantity < 20:
Branch_sell = quantity * 350
Else
Branch_sell = quantity * 400
Calculation of branch’s sell percentage = (branch’s sell / total sell) * 100
