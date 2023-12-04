#task4:
class Student:
   def __init__(self,nm,id,dep):
      self.name=nm
      self.id=id
      self.dep=dep
      self.email=None
      self.password=None
      self.ls=None
      self.lst=[]
      print("Student object is created!")

class Usis:
    def __init__(self) :
      print(f"USIS is ready to use!")
    def login(self,obj):
       if obj.email ==None and obj.password==None:
          print(f"Email and password need to be set.")
       else:
          print(f"Login successful!")

    def advising(self,obj,*args):
        if len(args)==0:
          if obj.email==None and obj.password==None:
               print("Please login to advise course")
          else:
              print("You haven't selected any courses")
        else:
            lst2=[]
            for i in args:
                lst2.append(i)
            if len(lst2) <=3:
                obj.lst=lst2
                print("Advising successful!")
            else:
                print("You need special approval to take more than 3 courses.")
    def individualDetails(self,obj):
           return f"Name: {obj.name} \nID: {obj.id} \nDepartment: {obj.dep} \nAdvised course: {','.join(obj.lst)}"


rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110",
"CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))