while True:
  inp = input().split()
  if inp == ['STOP']:
    break
  else:
    num = [int(i) for i in inp]
    l = []
    l2 = []
    for j in range(len(num)-1):
      l.append(abs(num[j]-num[j+1]))
      l2.append(j+1)
  l.sort()
  if l == l2:
    print('UB Jumper')
  else:
    print('Not UB Jumper')