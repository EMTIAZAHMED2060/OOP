class Student:
    total_students = 0
    brac_university_students = 0
    other_institution_students = 0

    def __init__(self, name, department, institution="BRAC University"):
        self.name = name
        self.department = department
        self.institution = institution
        Student.total_students += 1
        if institution == "BRAC University":
            Student.brac_university_students += 1
        else:
            Student.other_institution_students += 1

    @classmethod
    
    def createStudent(cls, name, department, institution="BRAC University"):
        return cls(name, department, institution)

    @classmethod
    def printDetails(cls):
        print("Total Student(s):", cls.total_students)
        print("BRAC University Student(s):", cls.brac_university_students)
        print("Other Institution Student(s):", cls.other_institution_students)

    def individualDetail(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Institution:", self.institution)
        
        
Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
