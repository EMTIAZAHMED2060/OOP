
class Student:
    ID = 0

    def __init__(self, n, d, a, cg):
        self.n = n
        self.d = d
        self.age = a
        self.cg = cg
        Student.ID += 1

    def showDetails(self):
        print("ID:", Student.ID)
        print("Name:", self.n)
        print("Department:", self.d)
        print("Age:", self.age)
        print("CGPA:", self.cg)
        print("-----------------------")

    @classmethod
    def from_string(cls, info):
        n, d, a, cg = info.split("-")
        obj = cls(n, d, a, cg)
        return obj

s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_string("Sumaiya-BBA-23-3.96")
s4.showDetails()

