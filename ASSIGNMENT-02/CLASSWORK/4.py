def palindrome(wps):
    new_wps = ""
    for letter in wps:
        if letter != " ":
            new_wps += letter
    wps = new_wps[::-1]
    if new_wps == wps:
        print("Palindrome")
    else:
        print("Not a palindrome")
palindrome("nurses run")