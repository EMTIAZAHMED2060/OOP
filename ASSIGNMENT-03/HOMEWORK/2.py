class box:
    def __init__(self,nums):
        self.height=nums[0]
        self.width=nums[1]
        self.breadth=nums[2]
        print("Creating a Box!")

    def boxDescription(self):
        print("Height:", self.height)
        print("Width:", self.width)
        print("Breadth:", self.breadth)
    def volume(self):
        volume = self.height * self.width * self.breadth
        return f"the volume of the box is {volume} cubic units"


# Write your class code here
print("Box 1")
b1 = box([10,10,10])
print("=========================")
b1.boxDescription()
print(b1.volume())
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
b2.boxDescription()
print(b2.volume())
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
b3.boxDescription()
print(b3.volume())

one = (b3 == b2)
b3.width = 100
two = (b3 == b2)
print(one,two)
print(b2.width)