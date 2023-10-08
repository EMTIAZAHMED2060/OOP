n = input().split()
k = int(n[1])
count = 0
ip = input().split(' ')
l = []
for i in ip:
  l.append(int(i))
for j in l:
  if (j+k) <= 5:
    count+=1
print(count//3)