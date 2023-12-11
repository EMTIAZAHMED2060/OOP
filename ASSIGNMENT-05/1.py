class Course:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department
        self.__courses = []

    def addCourse(self, course):
        self.__courses.append(course)

    def printDetail(self):
        print("====================================")
        print("Name: ", self.__name)
        print("Department: ", self.__department)
        print("List of courses")
        print("====================================")
        for course in self.__courses:
            print(course.name)

class Student:
    ID = 0

    def __init__(self, name, department, age, cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.ID += 1
        self.ID = Student.ID

    def showDetails(self):
        print("ID:", self.ID)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Age:", self.age)
        print("CGPA:", self.cgpa)

    @classmethod
    def from_String(cls, details):
        name, department, age, cgpa = details.split("-")
        age = int(age)
        cgpa = float(cgpa)
        return cls(name, department, age, cgpa)

s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails() 
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails() 

# Difference between class variable and instance variable:
print("Difference between class variable and instance variable:")
print("A class variable is shared among all instances of a class, while an instance variable is unique to each instance.")
print("Class variables are defined outside of any methods in the class, and they are accessed using the class name.")
print("Instance variables are defined within methods or the constructor, and they are accessed using the instance name.")

# Difference between instance method and class method:
print("Difference between instance method and class method:")
print("An instance method operates on an instance of a class and can access and modify instance variables.")
print("A class method operates on the class itself and can access and modify class variables.")
print("Instance methods are defined without the @classmethod decorator, while class methods are defined with the @classmethod decorator.")