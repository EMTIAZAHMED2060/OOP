class StudentDatabase:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def calculateGPA(self, course_grades, semester):
        gpa = 0
        total_credits = 0

        for course_grade in course_grades:
            course, grade = course_grade.split(': ')
            credits = 3  # Each course is of 3 credits
            gpa += float(grade) * credits
            total_credits += credits

        gpa = gpa / total_credits

        if semester not in self.grades:
            self.grades[semester] = {}
        self.grades[semester][tuple(course_grades)] = gpa

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")

        for semester, courses in self.grades.items():
            print(f"Courses taken in {semester}:")
            for course_grades, gpa in courses.items():
                courses = [course for course, _ in [course.split(': ') for course in course_grades]]
                print("\n".join(courses))
                print(f"GPA: {gpa}")
                print('---')

# Write your code here
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()

# Grades for Pietro
# {'Summer2020': {('CSE230', 'CSE220', 'MAT110'): 4.0}, 'Summer2021': {('CSE250', 'CSE330'): 3.85}}
# ---------------------------------
# Name: Pietro
# ID: 10101222
# Courses taken in Summer2020: 
# CSE230
# CSE220
# MAT110
# GPA: 4.0
# Courses taken in Summer2021: 
# CSE250
# CSE330
# GPA: 3.85
# ---------------------------------
# Grades for Wanda
# {'Summer2022': {('CSE111', 'CSE260', 'ENG101'): 3.8}}
# ---------------------------------
# Name: Wanda
# ID: 10103332
# Courses taken in Summer2022: 
# CSE111
# CSE260
# ENG101
# GPA: 3.8
