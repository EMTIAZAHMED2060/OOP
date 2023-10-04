t=input("please input a string:")
upper_case=0
lower_case=0
for each in t:
    if ord(each) >= ord('A') and ord(each) <= ord('Z'):
        upper_case+=1
    elif ord(each) >= ord('a') and ord(each) <= ord('z'):
        lower_case+=1
if upper_case > lower_case:
    print(t.upper())
else:
    print(t.lower())