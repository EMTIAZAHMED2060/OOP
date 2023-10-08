d = {}
while True:
  st = input()
  if st == 'STOP':
    break
  else:
    if st not in d:
      d[st] = 1
    else:
      d[st]+=1
for i,j in d.items():
  print(f'{i} - {j} times')