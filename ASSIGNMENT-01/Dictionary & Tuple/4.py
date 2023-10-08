'''
ADE CF

2 3 3 3 2 2 2 3 3 3


'''
d = { '1' : '.,?!:' , '2' : 'ABC' , '3' : 'DEF' , '4' : 'GHI' , '5' : 'JKL' , '6' : 'MNO' , '7' : 'PQRS' , '8' : 'TUV', '9' : 'WXYZ' , '0' : ' '}
s = input().upper()
ns = ''
for i in s:
  for j,k in d.items():
    for l in range(len(k)):
      if k[l] == i:
        ns+=(j*(l+1))
print(ns)