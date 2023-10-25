class StudentDatabase:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    self.grades = {}
  def calculateGPA(self,lsg,semester):
    self.lsg = lsg
    self.semester = semester
    coursename = []
    sum  = 0
    count = 0
    dic = {}
    for i in self.lsg:
      i = i.split(': ')
      coursename.append(i[0])
      sum+=float(i[1])
      count+=1
    dic[tuple(coursename)] = round((sum/count),2)
    self.grades[self.semester] = dic
    dic = {}
    sum = 0
    count = 0
  def printDetails(self): 
    print(f'Name: {self.name}\nID: {self.id}')
    for j,k in self.grades.items():
      print(f'Courses taken in {j}:')
      for m,n in k.items():
        for l in m:
          print(l)
        print(f'GPA: {n}')
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()