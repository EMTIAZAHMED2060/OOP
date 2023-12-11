#task-6
class Train:
  def __init__(self,name,*dis):
    self.name=name
    self.route=dis
    self.start=dis[0]
    self.destination=dis[-1]
    self.trps=[]
    print(f"Welcome aboard on {self.name}\nStart: {self.start}\nDestination: {self.destination}")
  
  def addPassenger(self,*other):
    for i in other:
      print(f"{i.name} welcome aboard")
      self.trps.append(i)
      
  def allPassengerDetails(self):
    for i in self.trps:
      if len(i.destination)==0:
        i.start=self.start
        i.finish=self.destination

      elif len(i.destination)==1:
        i.start=i.destination[0]
        i.finish=self.destination

      elif len(i.destination)==2:
        i.start=i.destination[0]
        i.finish=i.destination[1]
#done-----------------------------------------
      stt=0
      fin=0

      for x in range(len(self.route)):
        if i.start == self.route[x]:
          stt = x
        elif i.finish == self.route[x]:
          fin = x
        else:
          pass
      print(f"Name: {i.name},Start: {i.start},Destination: {i.finish},Fair: ${(fin-stt)*100}")
      
        

class Passenger:
  def __init__(self,n,*dis):
    self.name=n
    self.destination=dis
    self.start=None
    self.finish=None


t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
print("1========================")
p1 =Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke","Manhattan")
p3 = Passenger("Hinata","Manhattan","Brooklyn")
print("2========================")
t1.addPassenger(p2,p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
print("5========================")
p4 =Passenger("Max","London","Brussels")
p5 = Passenger("Eleven","Paris")
p6 = Passenger("Mike","Brussels")
t2.addPassenger(p4,p5,p6)
print("6========================")
t2.allPassengerDetails()