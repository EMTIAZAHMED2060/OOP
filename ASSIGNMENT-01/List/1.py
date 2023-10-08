list1=[]
list2=[]
count=0
while True:
    inp=input()
    if inp=="STOP":
        break
    else:
        list1.append(int(inp))

for x in list1:
    if x not in list2:
        list2.append(x)

for y in list2:
    if y in list2:
        count+= list1.count(y)
    print(f"{y} - {count} times")