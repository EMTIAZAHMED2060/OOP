class Train():
    def __init__(self,*args):
        self.lst=list(args)
        self.travel = self.lst[1:]
        self.passengers = []
        
        print(f'Welcome aboard on {self.lst[0]}\nStart: {self.lst[1]}\nDestination: {self.lst[-1]}')
    def addPassenger(self,*passenger):
        demo_list = list(passenger)
        for i in demo_list:
            self.passengers.append(i)
        for i in self.passengers:
            if i.up == None:
                i.up = self.lst[1] 
            if i.down == None:
                i.down = self.lst[-1]

        for i in demo_list:
            print(f'{i.name} welcome aboard')
            
            idx = 0
            for j in range(len(self.travel)):
                if i.down == self.travel[j]:
                    idx = j
            for j in range(len(self.travel)):
                if i.up == self.travel[j]:
                    idx -= j
                
            total = idx*100
            i.fare = total  
        
    def allPassengerDetails(self):
        for i in (self.passengers):
            print(f"Name: {i.name},Start: {i.up},Destination:\n{i.down},Fair: ${i.fare}")

class Passenger():
    def __init__(self,name,up=None,down=None):
        self.name=name
        self.fare = 0
        self.up = up
        self.down = down

# Driver Code
t1 = Train('T1-Express', 'New York', 'Manhattan', 'Brooklyn', 'Boston')
print("1========================")
p1 = Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke", "Manhattan")
p3 = Passenger("Hinata", "Manhattan", "Brooklyn")
print("2========================")
t1.addPassenger(p2, p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")

t2 = Train('Europe-Express', 'London', 'Paris', 'Brussels', 'Turkey')
print("5========================")
p4 = Passenger("Max", "London", "Brussels")
p5 = Passenger("Eleven", "Paris")
p6 = Passenger("Mike", "Brussels")
t2.addPassenger(p4, p5, p6)
print("6========================")
t2.allPassengerDetails()
