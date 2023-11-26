class Student:
    def __init__(self, name, student_id, cgpa):
        self.__name = name
        self.__student_id = student_id
        self.__cgpa = cgpa

    def getName(self):
        return self.__name

    def getId(self):
        return self.__student_id

    def getCGPA(self):
        return self.__cgpa

    def setId(self, new_id):
        self.__student_id = new_id


class Department:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def findStudent(self, student_id):
        for student in self.__students:
            if student.getId() == student_id:
                print("Student Info:")
                print("Student name:", student.getName())
                return
        print("Student with this ID doesn't exist, Please give a valid ID")

    def addStudent(self, *students):
        for student in students:
            is_unique_id = True
            for existing_student in self.__students:
                if existing_student.getId() == student.getId():
                    is_unique_id = False
                    break

            if is_unique_id:
                print(f"Welcome to {self.__name} department, {student.getName()}")
                self.__students.append(student)
            else:
                print("Student with the same ID already exists. Please try with another ID")

    def details(self):
        print(f"Department Name: {self.__name}")
        print(f"Number of students: {len(self.__students)}")
        print("Details of the students:")
        for student in self.__students:
            print(f"Student name: {student.getName()}, ID: {student.getId()}, CGPA: {student.getCGPA()}")


s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()
