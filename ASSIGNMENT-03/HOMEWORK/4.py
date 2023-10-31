class abcTech:
    def __init__(self, name, designation, department):
        self.name = name
        self.designation = designation
        self.department = department
        self.programming_skills = []
        self.frameworks = []
        print("-------------------------")
        print(f"Welcome to abcTech, {self.name}!")

    def addProgrammingSkills(self, skills):
        self.programming_skills.append(skills)

    def addFrameworks(self, frameworks):
        self.frameworks.append(frameworks)
    def printInfo(self):
        print("-------------------------")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Department: {self.department}")
    
        print("Programming Skills: ", end="")
        for skill in self.programming_skills:
            print(skill, end=", ")
        print()  # Print a newline to end the line
    
        print("Frameworks: ", end="")
        for framework in self.frameworks:
            print(framework, end=", ")
        print()  # Print a newline to end the line


    

    def calculateSalary(self, base_salary, working_hours):
        if working_hours > 144:
            extra_hours = working_hours - 144
            extra_payment = extra_hours * 800
            return base_salary + extra_payment
        else:
            return base_salary

# Driver Code
print("-------------------------")
b1 =abcTech("Tamim Hasan", "Software Engineer", "Android Development")
print("-------------------------")
b1.addProgrammingSkills(["Java", "Python"])
b1.addProgrammingSkills(["Dart", "C++"])
b1.addFrameworks(["Express.js", "React"])
b1.printInfo()
print("-------------------------")
print(f"Your salary for this month is Tk. {b1.calculateSalary(45000, 156)}")
print("-------------------------")
print("-------------------------")
b2 =abcTech("Jahin Khandoker", "Senior Developer", "App Development")
print("-------------------------")
b2.addProgrammingSkills(["Java", "Dart", "Swift"])
b2.addFrameworks(["Flutter", "React Native"])
b2.addFrameworks(["Xamarin"])
b2.printInfo()
print("-------------------------")
print(f"Your salary for this month is Tk. {b2.calculateSalary(103000, 123)}")
print("-------------------------")
