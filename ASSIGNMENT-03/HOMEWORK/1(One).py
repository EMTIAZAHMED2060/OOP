class CellPackage:
  def __init__(self, price, data, talktime, messages, cashback, validity):
    self.price, self.data, self.talk_time, self.messages, self.cashback, self.validity = price, data, talktime, messages, cashback, validity

  def calculate(self):
    data = self.data.split(" ")
    self.data = int(data[0])*1024
    cashback = self.cashback.split("%")
    self.cashback = int(self.price*int(cashback[0])/100)
    
#driver code ----------------------------------------------------------------

pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
pkg.calculate()
if pkg.data != 0:
  print(f"Data = {pkg.data} MB")
if pkg.talk_time != 0:
  print(f"Talktime = {pkg.talk_time} Minutes")
if pkg.messages != 0:
  print(f"SMS/MMS = {pkg.messages}")
print(f"Validity = {pkg.validity} Days\n--> Price = {pkg.price} tk")
if pkg.cashback != 0:
  print(f"Buy now to get {pkg.cashback} tk cashback.")
pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)

print('============= Package 2 =============')
pkg2.calculate()
if pkg2.data != 0:
  print(f"Data = {pkg2.data} MB")
if pkg2.talk_time != 0:
  print(f"Talktime = {pkg2.talk_time} Minutes")
if pkg2.messages != 0:
  print(f"SMS/MMS = {pkg2.messages}")
print(f"Validity = {pkg2.validity} Days\n--> Price = {pkg2.price} tk")
if pkg2.cashback != 0:
  print(f"Buy now to get {pkg2.cashback} tk cashback.")

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
pkg4.calculate()
if pkg4.data != 0:
  print(f"Data = {pkg4.data} MB")
if pkg4.talk_time != 0:
  print(f"Talktime = {pkg4.talk_time} Minutes")
if pkg4.messages != 0:
  print(f"SMS/MMS = {pkg4.messages}")
print(f"Validity = {pkg4.validity} Days\n--> Price = {pkg4.price} tk")
if pkg4.cashback != 0:
  print(f"Buy now to get {pkg4.cashback} tk cashback.")
