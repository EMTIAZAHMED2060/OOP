class CellPackage :
  def __init__(self,price,data,talk_time,messages,percentage,validity):
    self.price=int(price)
    self.data=int(data[0:-3])
    self.talk_time=int(talk_time)
    self.messages=int(messages)
    self.percentage=int(percentage[0:-1])
    self.cashback=int(self.price*self.percentage//100)
    self.validity=int(validity)

  def print_all(self):
    if self.data!=0:
      print("Data = ",self.data*1024,"MB")
    if self.talk_time!=0:
      print("Talktime =",self.talk_time,"Minutes")
    if self.messages!=0:
      print("SMS/MMS =",self.messages)
    if self.validity!=0:
      print("Validity =",self.validity,"Days")
    if self.price!=0:
      print("--> Price =",self.price,"tk")
    if self.cashback!=0:
      print("Buy now to get",self.cashback,"tk cashback")




# Driver Code
# Subtask 1: Write the CellPackage Class

pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
pkg.print_all()
# Subtask 2: Check each attribute and print

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
# Subtask 3: Check each attribute and print
pkg2.print_all()

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
# Subtask 4: Check each attribute and print
pkg4.print_all()