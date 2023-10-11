
def correction(string=input('Enter a string: ')):
  
    s = string[0].upper()
    
    sp = '.?!'
    
  
    for i in range(1, len(string)):
        # Check if the current character is 'i' and  spaces.
        if (string[i - 1] == ' ') and (string[i + 1] == ' ') and string[i] == 'i':
            # Capitalize 'i' to 'I' in this case.
            s += 'I'
        else:
            # Check if the character before the current character is a space and the one before that is a punctuation mark.
            if (string[i - 1] == ' ') and (string[i - 2] in sp):  
            
                s += string[i].upper()
            else:
                
                s += string[i]
    return s


print(correction())
