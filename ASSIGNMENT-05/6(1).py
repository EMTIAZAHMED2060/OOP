class BracuStudent:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.__pass=False
    def get_pass(self):
        self.__pass=True
    def showPass(self):
        return self.__pass
    def show_details(self):
        print(f'Student Name: {self.name}Lives in {self.location}\nHave Bus Pass? {self.__pass}')
class BracuBus:
    def __init__(self,area,capacity=2):
        self.area=area
        self.capacity=capacity
        self.students=[]
    def show_details(self):
        print(f'Bus Route: {self.area}\nPassengers Count: {len(self.students)} (Max: {self.capacity})\nPassengers On Board: {self.students}')
    def board(self,*args):
        if len(args)==0:
            print('No passengers!')
        else:
            for i in args:
                if i.showPass()==True:
                    if i.location==self.area:
                        if len(self.students)<self.capacity:
                            print(f'{i.name} boarded the bus.')
                            self.students.append(i.name)
                        else:
                            print('Bus is full!')
                    else:
                        print('You got on the wrong bus!')
                else:
                    print("You don't have a bus pass!")
st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()