class Farmer:
    # Constructor to initialize the farmer's name and goods
    def __init__(self, name=None):
        if name is not None:
            self.name = name
            print(f"Welcome to your farm, {self.name}!")
        else:
            self.name = "your farm"
            print("Welcome to your farm!")
        self.crops = []
        self.fishes = []

    # Method to add crops to the farm
    def addCrops(self, *crops):
        count = len(crops)
        if count == 0:
            print("No crop(s) added.")
        else:
            self.crops.extend(crops)
            print(f"{count} crop(s) added.")

    # Method to add fishes to the farm
    def addFishes(self, *fishes):
        count = len(fishes)
        if count == 0:
            print("No fish added.")
        else:
            self.fishes.extend(fishes)
            print(f"{count} fish(s) added.")

    # Method to display the goods in the farm
    def showGoods(self):
        if self.name != "your farm":
            print("Welcome to your farm. Your farm ID is", id(self), "!")
    
        if self.crops:
            print("You have", len(self.crops), "crop(s):", end=" ")
            crop_list = ', '.join(self.crops)
            print(crop_list)
        else:
            print("You don't have any crop(s).")
    
        if self.fishes:
            print("You have", len(self.fishes), "fish(s):", end=" ")
            fish_list = ', '.join(self.fishes)
            print(fish_list)
        else:
            print("You don't have any fish(s).")
    
        print("-------------------")



# Driver Code
f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")

f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")

f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
