

class A:
  temp = 5
 def __init__(self):
    self.y = A.temp - 2
5 self.sum = A.temp + 1
6 A.temp += 3
7 def methodA(self, m, n):
8 x = 0
9 self.y = self.y + m + (A.temp)
10 x = x + 2 + n
11 print(x, self.y, self.sum)
12 self.methodB(-2, 6)
13 self.sum = self.sum + x + A.temp
14 self.methodB(-4, self.sum, 3)
15 def methodB(self, m, n):
16 y = 5
17 y = y + self.y
18 self.sum = B.x + y + n
19 print(B.x, y, self.sum)
20 class B(A):
21 x = 1
22 def __init__(self, obj=None):
23 super().__init__()
24 if obj != None:
25 obj.sum = 11
26 self.y = A.temp + 4
27 self.sum = 3 + A.temp + B.x
28 def methodB(self, m, n, y=0):
29 y = y + self.y + n
30 B.x = m + self.y + n
31 self.sum = B.x + y + A.temp
32 print(B.x, y, self.sum)