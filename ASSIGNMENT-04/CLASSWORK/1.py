class Student:
    def __init__(self, name, id, department="CSE"):
        self.name = name
        self.id = id
        self.department = department
        self.daily_effort = 0

    def dailyEffort(self, hours):
        self.daily_effort = hours

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.department}")
        print(f"Daily Effort: {self.daily_effort} hour(s)")

        if self.daily_effort <= 2:
            print("Suggestion: Should give more effort!")
        elif self.daily_effort <= 4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Excellent! Now motivate others!")

# Driver code (unchanged)
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
