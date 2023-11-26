class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department
        self.email = None
        self.password = None
        self.logged_in = None

        print("Student object is created!")

class Usis:
    def __init__(self):
        self.students = []

        print("USIS is ready to use!")

    def login(self, student):
        if student.email and student.password:
            student.logged_in = True
            print("Login successful!")
        else:
            print("Email and password need to be set.")

    def advising(self, student, *courses):
        if not student.logged_in:
            print("Please login to advise courses!")
        else:
            if len(courses) > 3:
                print("You need special approval to take more than 3 courses.")
            else:
                student.advised_courses = courses
                print("Advising successful!")

    def individualDetails(self, student):
        return f"Name: {student.name}\nID: {student.student_id}\nDepartment: {student.department}\n" \
               f"Advised courses: {', '.join(student.advised_courses)}"


# Driver Code
rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com" # type: ignore
rakib.password = "1234" # type: ignore
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))
