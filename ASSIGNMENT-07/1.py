#task1:
class KK_tea:
    name='KK Regular Tea'
    sale={'KK Regular Tea':0}

    def __init__(self,price,q=50):
          
          self.price=price
          self.quantity=q
          self.weight=q*2
          self.status=False

    def product_detail(self):
         print(f"Name: {self.name}, Weight: {self.weight} \nTea Bags: {self.quantity}, Price: {self.price} \nStatus: {self.status}")

    @classmethod
    def total_sales(cls):
         print('Total sales:',cls.sale)

    @classmethod
    def update_sold_status_regular(cls,*args):
          for i in args:
            i.status=True
            cls.sale[cls.name]+=1

class KK_flavoured_tea(KK_tea):
     def __init__(self,name,b,c):
          self.name="KK"+" "+name+" "+"Tea"
          super().__init__(b,c)

     @classmethod
     def update_sold_status_flavoured(cls,*args):
          for i in args:
            i.status=True
            if i.name not in cls.sale:
               cls.sale[i.name]=1
            else:
               cls.sale[i.name]+=1

t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()