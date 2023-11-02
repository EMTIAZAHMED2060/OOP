class Student:
    def __init__(self, name, cgpa, credits=0, department="CSE"):
        self.name = name
        self.cgpa = cgpa
        self.credits = credits
        self.department = department

    def checkScholarshipEligibility(self):
        if self.cgpa >= 3.7 and self.credits >= 12:
            return "Merit-based scholarship"
        elif self.cgpa >= 3.5:
            return "Need-based scholarship"
        else:
            return "No scholarship"

    def showDetails(self):
        scholarship_status = self.checkScholarshipEligibility()
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"CGPA: {self.cgpa}")
        print(f"Number of Credits: {self.credits}")
        print(f"Scholarship Status: {scholarship_status}")

# Driver code
print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
print(f"{std1.name} is eligible for {std1.checkScholarshipEligibility()}.")
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15, "BBA")
print('--------------------------')
print(f"{std2.name} is eligible for {std2.checkScholarshipEligibility()}.")
print('--------------------------')
print(f"{std3.name} is eligible for {std3.checkScholarshipEligibility()}.")
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
print(f"{std4.name} is eligible for {std4.checkScholarshipEligibility()}.")
print('--------------------------')
std4.showDetails()
