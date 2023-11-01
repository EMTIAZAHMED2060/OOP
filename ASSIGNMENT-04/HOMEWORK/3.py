class Department:

  def __init__(self, dep = 'ChE Department', sec = 5):
    self.dep = dep
    self.sec = sec
    self.ave = 0
    self.tot = 0

    print(f'The {self.dep} Department has {self.sec} sections')

  def add_students(self, *args):
    self.net = 0
    if len(args) == self.sec:
      for i in args:
        self.net += i
      self.ave = self.net/self.sec
      print(f"The {self.dep} has an averange of {round(self.ave,2)} students in each section.")
    else:
      print(f"{self.dep} doesn't have {len(args)} sections" )

  def merge_Department(self,*args):
    self.tot = self.ave * self.sec
    return_statement = ''
    for deps in args:
      self.tot += deps.ave*deps.sec
      return_statement += f'{deps.dep} is merged to {self.dep}\n'

    self.ave = self.tot/ self.sec
    return_statement += f'Now the {self.dep} has an average of {round(self.ave,2)} students in each section.'

    return return_statement



d1 = Department()
print('1-----------------------------------')
d2 = Department('MME Department')
print('2-----------------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------------')
print(mega.merge_Department(d3))