class CellPackage:
  def __init__(self, price, data, talktime, messages, cashback, validity):
    self.price, self.data, self.talk_time, self.messages, self.cashback, self.validity = price, data, talktime, messages, cashback, validity

  def calculate(self):
    data = self.data.split(" ")
    self.data = int(data[0])*1024
    cashback = self.cashback.split("%")
    self.cashback = int(self.price*int(cashback[0])/100)

pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
pkg.calculate()
dic = { pkg.data : f"Data = {pkg.data} MB", pkg.talk_time: f"Talktime = {pkg.talk_time} Minutes",
       pkg.messages: f"SMS/MMS = {pkg.messages}",
        pkg.validity: f"Validity = {pkg.validity} Days\n--> Price = {pkg.price} tk",
        pkg.cashback: f"Buy now to get {pkg.cashback} tk cashback."}
for i,j in dic.items():
  if i != 0:
    print(j)


pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
pkg2.calculate()
dic = { pkg2.data : f"Data = {pkg2.data} MB", pkg2.talk_time: f"Talktime = {pkg2.talk_time} Minutes",
       pkg2.messages: f"SMS/MMS = {pkg2.messages}",
        pkg2.validity: f"Validity = {pkg2.validity} Days\n--> Price = {pkg2.price} tk",
        pkg2.cashback: f"Buy now to get {pkg2.cashback} tk cashback."}
for i,j in dic.items():
  if i != 0:
    print(j)


pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
pkg4.calculate()
dic = { pkg4.data : f"Data = {pkg4.data} MB", pkg4.talk_time: f"Talktime = {pkg4.talk_time} Minutes",
       pkg4.messages: f"SMS/MMS = {pkg4.messages}",
        pkg4.validity: f"Validity = {pkg4.validity} Days\n--> Price = {pkg4.price} tk",
        pkg4.cashback: f"Buy now to get {pkg4.cashback} tk cashback."}
for i,j in dic.items():
  if i != 0:
    print(j)