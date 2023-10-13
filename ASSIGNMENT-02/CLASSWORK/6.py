def correction(string = input('Enter a string: ') ):
  s = string[0].upper()
  sp = '.?!'
  for i in range(1,len(string)):
    if (string[i-1] == ' ') and (string[i+1] == ' ') and string[i] == 'i':
      s+='I'
    else:
      if (string[i-1] == ' ') and (string[i-2] in sp):
        s+=string[i].upper()
      else:
        s+=string[i]
  return s
print(correction())