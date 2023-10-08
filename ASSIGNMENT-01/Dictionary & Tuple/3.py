st = input().split(', ')
d = {}
for i in st:
  i = i.split(' : ')
  if i[1] not in d:
    d[i[1]] = [i[0]]
  else:
    d[i[1]] += [i[0]]
print(d)