x=[]
u=[]
while(True):
    i =input()
    if i == "STOP":
        break
    x.append(int(i))
    if int(i) not in u:
        u.append(int(i))


print(u)
print(x)