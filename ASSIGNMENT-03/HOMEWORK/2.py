class box:
    def __init__(self, length, width, height):
        print("Creating a Box!")
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def boxDescription(self):
        print("Height:", self.height)
        print("Width:", self.width)
        print("Length:", self.length)

# Driver code
print("Box 1")
b1 = box(10, 10, 10)  
print("=========================")
b1.boxDescription()
print(b1.volume())
print("-------------------------")
print("Box 2")
b2 = box(30, 10, 10)  
print("=========================")
b2.boxDescription()
print(b2.volume())
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Length:", b2.length)
volume = b2.height * b2.width * b2.length
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
b3.boxDescription()
print(b3.volume())
