s=input("please enter a string:")

for i in range(0,len(s)):
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
        idx1=i
        break
for i in range(0,len(s)-1,-1):
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
        idx2=i
        break