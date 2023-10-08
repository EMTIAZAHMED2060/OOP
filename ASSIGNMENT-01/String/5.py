inp = input()
string = ''
special_characters = "$#@"
lower = False
upper = False
special = False
digit = False

for i in inp:
    i = ord(i)
    if 57 >= i >= 48:
        digit = True
    elif 90 >= i >= 65:
        upper = True
    elif 122 >= i >= 97:
        lower = True
    else:
        if chr(i) in special_characters:
            special = True

if not lower:
    string += 'lowercase letters missing, '
if not upper:
    string += 'uppercase letters missing, '
if not digit:
    string += 'digits missing, '
if not special:
    string += 'special characters missing, '

if string == '':
    print('OK')
else:
    print(string[:-2])  # Remove the trailing comma and space
