class MangoTree:
    def __init__(self, variety):
        self.variety = variety
        self.height = 1
        self.number_of_mangoes = 0
    
        

    def growthUpdate(self, years):
        
        self.height += 3 * years
        if self.variety == "Gopalbhog":
            self.number_of_mangoes = 10 * self.height
        elif self.variety == "Amrapali":
            self.number_of_mangoes = 15 * self.height

#Driver code
print("Updated details after 5 years:")
mangoTree1 = MangoTree("Gopalbhog")
print("=====================================")
mangoTree1.growthUpdate(5)
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes clearon the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")

mangoTree2 = MangoTree("Amrapali")
mangoTree2.growthUpdate(5)
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")
