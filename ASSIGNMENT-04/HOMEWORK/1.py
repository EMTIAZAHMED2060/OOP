class Student:
    def __init__(self, name, cgpa, credits=0, department="CSE"):
        # Initialize instance variables
        self.name = name
        self.cgpa = cgpa
        self.credits = credits
        self.department = department

    def checkScholarshipEligibility(self):
        if self.cgpa >= 3.7 and self.credits >= 12:
            print(f"{self.name} is eligible for Merit-based scholarship.")
        elif self.cgpa >= 3.0 and self.department == "BBA":
            print(f"{self.name} is eligible for Need-based scholarship.")
        else:
            print(f"{self.name} is not eligible for scholarship.")

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"CGPA: {self.cgpa}")
        print(f"Number of Credits: {self.credits}")
        self.checkScholarshipEligibility()



#driver code
print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
